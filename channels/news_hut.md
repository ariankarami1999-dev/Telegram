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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 184K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 14:08:51</div>
<hr>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm8FhAvXjLMMrX46WIBm_paVAuAyFbF5_nfVY90sxKGgMQDrqgaM9iIdEgqxPI3SSQpkvWLq4ClwxSr1xb7BMtwM7HCq9k6-kJRQhNWlnhc7U1_hEOT4Obzb0ETVGrpMCrorEa3dKyBHsYXsKGFFqMRLZ6nZMvE1eWkJ2WUA4Ppk8npvtBrHpg432ZQxrMKG87ptKNIz3--cjOxdiG19ZdAFwAkmxPP7WuajVTOlGOEbbpiajhOC_Ts6RW_lBUdpajVRV0pmDgsX0E_bTklrDfIQNLmpKkj0Tmg4UdzEQsQ0rdbgOoDsxPMx6oa9fLk1qMvYx87ttVFV21zjqUBpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITeOkj7hUw2bgCGG2XC38YbG60Kgxt3o9nVfx3J_CrSjm4jptJ1u2U47dBkVDWOTuQP0NYgtFfhGZQlDLBJUf0KwZeKsIdPY346f8UdV7iTHTFO6BmDNcWLm8Zh-ydQ1YYvCq7aV1i21Jw2adT5rYtQvhL3XcBrguxMd8XEadl2tOXPf8a22TPDPs9SlknltJKAxY0OmDdPBpvpRUA-_Njf4gSAYl9A3gAE1HWtsqOuUudsId-N1wLeaz6qrl2xZFQZPANueFqIPPjR_Sra109iUIJ4iBEBCeKNizWJp9_blii-6IpbjjAnISWBcJAtxieYwVYDYOMF7bo2iOzoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRfAmhOZHZ1zWYjmXQUYvHpEPZjnn346TkQ8bUEZbqWj0_kI6J4nSIGT7_6WEvG2eOOb10BUU_mqD9f5Ow4LR97fHUMPbbvg3KFALYXz7XXkwDoeN6yFZw9PrEHj8R4h2WKv-uZtbt7bDXdGiGUsPhcUHJbjm-KNtKW8_s39RBwDD7kfeANosQGhh_Hq0kQcLhPz4GnChF_vEplbRgaNw95mR_7nevF0AStiGIrZIZQwfKuDxldG-uUiz5RYChBoUiZ3-18w5MT1Hz7TIkTCrP5LUVsFE4YdzkJJltWZKBKv_WZl1T8iYX7JbmyNPpj2h8EBgRfl_KQQPYRNF4dotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCF6NrUi8bl98tqOo-5vO2XBmXFZrImKrYZV_zN-Tyfz3ZB8v8uqyfx0JYSyToaqO7R5CYKcLUf_gdd3DsBxj4RcLIzM-vsWU62DOn3LMvet6ajNoiJv3w4IpRge_A0kzcQM8yav4n1HI8vnw7VKpJ8sRoZNz6NN_MYdcKURpHt3nl-36KlIVmUBzZ4LLgoql6vL-wq2l1tpr6-hcvdIfuW58TKVPfRQihqkvxnuaIfLVwsfgLdBTUIYefdui_CP4oviZNoJNmRKgWHu2Kmd3rf3MODbGDH2Z25ousoF9lHIaYJguhjqftRBGEbSUDdcPRdQ4CvJMAlNvJqgGa9y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Wjk4nRonzYYQZW9y1L3bffNTDfJ-vPG-1w6V5IWMrzvyYjw4as4CaBHmYNani8iO4OlUmCr0pBFzREZI6t0n4XBa6ac-71LM4YcfgkuA44F_tvKWjCVUXSrjSn-b1PQcKFt1uyZq8kK_wvi3uuD9jSbm-EivpWTf_lZHx-pBx2yD7i5MgxYfsFMoNhOXSrYmJxpirPwuApuuUNuex6MSmnfPOivoHwL5nrlz2s7a3cZrdDad6_A6bjzWjEElqOG2gG7mH1D8B2jtDRkOh7pT8FnRzdp_mc2uu3ZspzwqDklVMvtXB3Qv9dybHhM9AbsbR8njgvDKUsy1mCuDOx_zjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Wjk4nRonzYYQZW9y1L3bffNTDfJ-vPG-1w6V5IWMrzvyYjw4as4CaBHmYNani8iO4OlUmCr0pBFzREZI6t0n4XBa6ac-71LM4YcfgkuA44F_tvKWjCVUXSrjSn-b1PQcKFt1uyZq8kK_wvi3uuD9jSbm-EivpWTf_lZHx-pBx2yD7i5MgxYfsFMoNhOXSrYmJxpirPwuApuuUNuex6MSmnfPOivoHwL5nrlz2s7a3cZrdDad6_A6bjzWjEElqOG2gG7mH1D8B2jtDRkOh7pT8FnRzdp_mc2uu3ZspzwqDklVMvtXB3Qv9dybHhM9AbsbR8njgvDKUsy1mCuDOx_zjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=g5If-UU_JfZMIa_-JHQDqpmmximgHUFPT7pDjX5aXiGvQrFSQETAk17f3pqmtH20xiOj4SXko9u5DjBCyvF499W8HQcBlp35I58LlDGYDvR7ehtTh9Smxs95HZR6fgXlvgPP7H1HR7r_CvqtmIy9gZJlxVhkpqsL4Fldc08-QIfy_uvhQrna-WbG9uxdxAM2h2h4ygK3z3O1MjITxjq9yAD4NJLOQzVcitZgYgTMxuYrZMqazc68kRg0vYmosv4mvGb3_o4z1Cvb3D-BOYfNh0b8PFfxurU5XkAt9QU_4-fG7RG4oirGJKx4Ny5_MMNjaxo6dEqPhXA-z39SP1bqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=g5If-UU_JfZMIa_-JHQDqpmmximgHUFPT7pDjX5aXiGvQrFSQETAk17f3pqmtH20xiOj4SXko9u5DjBCyvF499W8HQcBlp35I58LlDGYDvR7ehtTh9Smxs95HZR6fgXlvgPP7H1HR7r_CvqtmIy9gZJlxVhkpqsL4Fldc08-QIfy_uvhQrna-WbG9uxdxAM2h2h4ygK3z3O1MjITxjq9yAD4NJLOQzVcitZgYgTMxuYrZMqazc68kRg0vYmosv4mvGb3_o4z1Cvb3D-BOYfNh0b8PFfxurU5XkAt9QU_4-fG7RG4oirGJKx4Ny5_MMNjaxo6dEqPhXA-z39SP1bqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHwZKSoIXQoAkUGt6bfwPKeoWE1xDniqWy97Jr1VHDGgq1u7cmolnm10pARiMygNo-ddeIWLtKtKsrC4Z2XYAglYqQUA1LLpluZTKhALUQRTkBaCBZTTvPTgPV3qFPo8YCqEgf1NbtkzNFOSgbnoQasF4GL46Hvmy6jK7hpTIpiQIue0lXY2nwjRB_pWRLiCkrPn5hrR3F7J1AzKeZsfUjeF9-r-U9bWU-QOydbO2lwKfbHPyCzNv0gvaU5nCpwGb0fWp7VnNIRYaLak-BRWRLNE8o6qEI5x6PHyxUJi_72SRpyTlI2at_Tx3H9iTFpIs4Lb9UdU0Oe-1wTjg3YhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tekLaxdUGDqYRwCBajwdfnF-pLtxl86cjyqw3AschZ9Nqlq2LjFmjaUmJ7xyCIKCDEwne0bzHCNN-_w7McuC76loz8E_Cu0Ysg617zcqEYxIEDB94oOZclUvrheBCaSmhQ1rTAfsblxAcgZbsaQVRtYJBvb9mR2vlrssNqYC353uYfHwGw0ONp-FDdHyOADjaNyq9XGx6Znf8RLPhf7YCF-pG8v6LDBLpu91ZwJMBwt63wi-f6WfzSRSyJHnXJiFHKjsYQwgqjQFtd8SBe3wymPZAf2-96X4DPY0RazRn9zB1QQ6WBbQZiYYde7mhRPbJ7CUOPcDWsuKK0p77i9I7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4qbZQo3jhbIaU1OOI5VnQJHx0goE6WC8pMr4WBKq8JKSnke6mUZyhIzIaJPvAoeu2TmAOd6e0kqQ0x_OSrJpsyEzEm7GEjO4YcsGyRPgkoKQwUaXfO-edtWDVyPx3AL5edQ5S0wf6_a0BmkmR9AzgUd5vLL55H9Tvr9cmKHHFlIYAywC6Ei4X8NEydywYmBkCG1zQvu78-jZvcQD-4VbjHYBpnbKp_wKsFq4jQbZn1iH-q-G5lGKH6g7N8ennWFYmFCJBcULn8TRd-VA5_FS_PhG_0r9A1XB1PFaplmBIAriKNMtPOMK_pnsNabzgjfRrNIE6TOgBcP5KfdaurXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g3NsfmONA3q3f-gr-kLCDAnrh7AFM7sxuY6y4Oz70Cq6-qdN8Fn1h4jYXD_xXwk-8QP2aH55PEUev7MzDPufq7tr9mwnFvgcMvW4PjFx0lT_8wdQVUJEoxBvQAWO86MYZcn8XddhkOaqHVWIXgNV3ZhsTPYfMR0Sdq3IKC94ol5S7snmr1t9ol7WlPB6YeecwzX21pDOSimz5U25p2JMe7JOEyOXriMn2sRuZcHv8eGeMhHS_gdsoEfTPQ-gBaVxlYg6An8QhiiQZTg3ATVQNcb4yn7EWhp4j2wLKskWjI-e993i3nF4Iv13EDhNIx0IgcyDT1cRQxM2O0zEe6uEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyaMGNNppORqfQYc7GdnjvzGYnI6nndRHdUiZC2hUQ1_6SdaKmIvbaQewO6B2ZqrL0s7GVJ7ZQooeadaR2mcr6rsr8ekIqon2ZynbbyY3UjsG_cay4-dmBZL00fQTtEZobzxHxexKZGLdZxm4UYFrxwzTd--429gztWvr5UH4B72xk-6ig2j2uP232_UPb_meS5QQwAqI9vg6XYqlYtLOosk_EnfGhyDn7RbaV2ojdXvB4RzBbOWLiBVj0RjOGD9pbRElTSF6s6AymqV4qLgeWNNtqz1iUrN0tZ0LPSs3U4ICL22wsM5KKrXWk_ydhR94o_Xj07zMDvk_CuykRjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsiF_czdiv3P_s_KBm5wvDzdsO4Ki5s-i3HsWXIxZUReCNC99AGrQkQxYXp16EA5SFEMZKSbFKqZ_A3hpib4CRDsdZ9APVPqmpmNIIFxBfu0W0Bep7I5WbK0pOJqoPAS82u534NYQbLFMV9x9k-607rBtJZS44doOjZu9eYu40kYdxNIOei37rr9pz5xzblUfcdwrt756TtFT1dJSXt-BT3hXhIr58LdGE7-blJ06AyKj7831TqrHMLs5FEVqKDA74iHb2y2hsd7YLkQDXaUqOV1JnarwdmPMnSSfyntj27Nk3gcgCS5cQYd3xUdg4ZC-d64WLsgzbehuUBky3fWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjWXpJrfEIYdzjudKjnBAw3XwumH2Jx-6Yh9BRDYf1g7QnfcPtN3aG0_YB2lgxyaaAt4jULCnpqppQFc2S1FHz5J-AjC6mvD4xLGdY2faO5GZ5WqMC9hiOGIKt6jzlaqPXgnA8YC7W05eRlJ2SqPMvcbOW3IsZk87RU4Byr8wmQ0gFmF4VdEvoVY3ERazBhWQ_tqV4V1_OQB_bavjjJki2L-Oy9L_tMQXPOvbu9t8n_Gw5XolhOVVXkRqkdNedOA5NaC6AVPVAQBxG9TZOCD0er-XV2RHfBW7Y9dJKNXCDntCEMXImfEs2AtC1IMfYjjkVu9Ot95KoPZzBAJQxRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhHvZwXvtcW6rKnbVk8xW5gdzzZGV2uxGSkNCC4vgMevqm9cdgYLM8PRKCEn9mTI7GMVJI6Jo-kLAByELHzeMHmM85cdJxPtGl00PskrP5tJ00JUlp1W97YMZIWFyfoo0-J5FeDHXAOtIjD1XQPFIdsKn9pdTZfQLGe9nnGJwLL9cEw78ucccum6fSui9WfD3Ya2-me_7hOXCQ53szt8JdvndhQ2_x9qhnGnjvdsfzDiBnFb2Jg-sujLqTJpI0hPl3xYmdwBLvjLyB7ceo5DdL6hxN_Jyezy28AuiOZBucrDdaluIums6WhdYZe4xzg8TJQuLIsn_QummbBZdBM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONhfIFY-F4rSHol8RkawhITl7MiOpP3Lven9H7aTJdE9qDbTiOZ7Yfw_jeMfFRzGePMQ7y6O4GSuZXfc8aKn7tm06UG3ncWiaCy7f7yOKGs7c6C-ELadh96qMMOyn2hZ4BFna5aV8-W-XdkxGg-5NE3AopIJLWsTHWt96KpJLo_94O4BPQ1qZpvNtJ9YSH3EGwJg54FVS9fPXwT-Pqc0NkdeAxJXm_QI-sUYk4B8MnVhiYUG6ChRjFA4J_2HhqtpMco7p5JYyUk-mE8IssjVcIq2XaFLiZjjB3KdHkwEmcAcoTvwDGOE3mL08LKSzKgS4kJz1i16G1V7JdIst-nd8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=GAQNZFEO3exKfwA3IFl5Lj9bZh4JV1_iv5bxg_aougOqPBefCT78sp8aYfJBxpRD0LTQcucLSJkqB3ID0TRBVw5VQQwmSYiTWdXSM92i2oVxADfA3YdmJ3FfmPVcm7u0dw-OmcHpIz_QYXFlL72x1ZVzfAW1Wtuu3sLG6A8y0XtmxdEABiqzZ2lLrVedn7rOW7gkltq0uOwzHnj0rLsDUDSjPmQ8NXX5M9IScxlFfJvUiutIPqZonQqfrY69r-_DAbzXQBnZp4rhfeSYsjXUhNCvzRmIMAW_8JIee5HSX2Rix9RtbfCNDse4mZX_6bb5QOb2Cf6A_jt1vnJgRqBQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNa-OaHDVneW-ap5qGJ_0cE_rLc-1YWUY3cGMB-eMbfwBqOWtowJlpP1wWnbQn7m0ruQLq4mkF3HN9NYgkZ56Ljvq4XKEsbCQy68enGHO2fgQDfuYmC81qYXwOzmlVRwJ6WLPkOsKnh0vzfvCeXzCANWHz0j953z9AsyYXlFADjXtnaXCJbPY7XLPeMwSjjniSFEZv776L26nuWkH6XyMwrOo4_I0d-M4o5MSr9JBUbJIh8Sfrxl7Mgw0QWEm2gSzygGcMb_4a2WyDEOa8sh7WsmdrbFSA047sf6HchxdzcxpEfWzGSExeqxOpb4de3k5MqpHAq3_OaIVWoXqpskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptkuYkyT4Ozb6RvAW7D0SsBzQz1jM_ahQlf-kfyv4LDPO_k3KddTn1lAaY7mXyIeMtfs01eTKlA96Fee1Tf-jGy1STn44qnd-Vxx5jqcNUxjutEtgS4wxS6dX3TpeKmYoHOypfwAdcuFW8XeAhUQGshcVDD8aChLsVGrA3SczYUhe3K9ZQFQo5-nnoQ02HTRyvo5vFIlmKt8ELLz0WPK15qKX4oFlry9wQqyCQdRYz-uxoORUEFfgPcJG7idXd08tugXDcpunOtV4TWAENIWrKn88JBt3lSukCYsbsmsNR69kJCebOhleBifMEvYBMVHNqJ6NGAE4R5rMK95jTnw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXb6QQGwU4YyxWrG_0PGLFXwU1i1QqgwksNtCStxLs-nE88Nw2wFxC3DE8UFMJNQGN__Xo7mhSTmfSLh-OvNFVuJUm4U2W7NZQRINMPVRR-FEYkuAWC7-WGEYRy51ZFEB_zjwaZX_Ampl3jza5YbjkwTDo2QfwqR1_AY8t6qcxmSHWS9V1_NM0qedeMn8z2szRa1XBKn54XUeV3bIyVkBwbhm7fOrsJOP7GmNU8Vm61WirsWQDQpBFhdpM6sNQN76nvMDyY_CicuNIR64gIQ7ngMa7_BC13xQ1irQ44-6lSl-n4C2OrTe0mBwi8kF-NEt4AQTqPZd7pht4AopZx3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3l1ucTDGjJ299KKr-hhzvZmeEQFxJQ4RK8xjWheTNv0jpbNWCPk8DSiPt1LIImGtlgHKuhEG3s74xbLHQOm_fr15X7DpSihjKd7gV1IUI5JKRQZQLT0G6OwDGmxJixTjZ5WP6oWrHu1LdNG0XouUFFZKoyHIDwXqdzwdd2t8l0cgjZvqnG2IEYGY8c05xK0csQUaHu4nideC-C6cplGTA4nhOs0nhA-qcbESb8LGKe66OV1Ee2Gv0_hjk1cgpSM3SCOLIp0RMLwW3Ihzprm8iXDPBEsRu7lOwJ3CNd6ESax5_CRAf23nQfRmi8x8KmNEqDEAUHljTBZVNxj9WpGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEySzESv1AWXAUKfY47pQWkrtAvqo0zmYGE8TLUdbP4aIzqq3PS5OTPcAYs21gSkIZkYwE3o8c1bXdas9BtJMAN117xKXay9eNszEtbJCPW-i09bP6B4KeQ36KRx1upYQy7sl-2aChZ7sWgDqocx5_WmCAjSuMnKxGBMmCTFD86UKoml2xQY_nupELOthAgb8JgJ99zqsaH0kKvTbNkTigdd81JAfT-8mkvFKdYonekhsUoASq58JEYkOBVq_5A4gEjFWYrChDtxhA3MlZ70_wLVJrEqlyaXs8IIXBd2kzA-0vR_wEru0BSTrHNq4tCQBMaV-HlszjSzND3mID7hyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=kPEMLPuY95L1EXNhDMP-4B9S_5v82csVDV7JRBMHswQ2J36BPz9VOR7RJDxoxXkywg2dv2oiQK1Z5qNO01OmXTEMu1Hd5lJy-g97RUVKiUU8eOxNrK5DMlpKEp4vDzkOcUCuvEqqAIT7_Lk-l83Ndk5lHSZ4_0c56rQo5RPJ2DFX0UQmISi_-jBa2UI3yoRA86lIwTA0kPnZrh5gos2KWAb3nDxzlJ0RUH7PKBl5m4-CyNZbMPHzHq-0mtDXs_dCrJXGi1zb3AIKLQTOXXGQvQWkQowgbxFjkwY2ByrJqojQgP3usrGO4kWe68Cg5YNYPVCE4a9y3EkMqRagFvCrPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=kPEMLPuY95L1EXNhDMP-4B9S_5v82csVDV7JRBMHswQ2J36BPz9VOR7RJDxoxXkywg2dv2oiQK1Z5qNO01OmXTEMu1Hd5lJy-g97RUVKiUU8eOxNrK5DMlpKEp4vDzkOcUCuvEqqAIT7_Lk-l83Ndk5lHSZ4_0c56rQo5RPJ2DFX0UQmISi_-jBa2UI3yoRA86lIwTA0kPnZrh5gos2KWAb3nDxzlJ0RUH7PKBl5m4-CyNZbMPHzHq-0mtDXs_dCrJXGi1zb3AIKLQTOXXGQvQWkQowgbxFjkwY2ByrJqojQgP3usrGO4kWe68Cg5YNYPVCE4a9y3EkMqRagFvCrPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMkfcvyDsBUPN3--kNHUkFhZWtMOvf2ANGSaL9_ToGoPvzoCP8m_7B8OPHT45NXqhKKHQb2esLBk4ZcK8lhQqS3SZqy59z30DYxFk8vUblaCnGOaad7WMwbyr-3G2ODAbJP6G_izRiK-S-Err-rd4rTBgVvNdoyUxEj1wvW0B-7EwJDtnWN3TfUyjSYvAZRmLqXlLFhIpZPvJ6BdwyL8cHWyQ5k1dKuKqEb8qacOavWVQiykBm47WP_s34kjG4lN2Ln0EH7GngaHA3bwLw0SR6pe7XESOsdGeZQcZ-lMNiuwrvYhee0OYSH9xq1ImZ-IrirQjJyh86GcCey7VzSqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmq_cpjtFCyH79CKMiYpsuJvRiBJGD4SwHCrp165iL1oIN3FWiCiTENDY54A94xR2OI_Pm8YGHzo0AQzxAoVXbA-wSH_gUTBkuCOoYOEmDnVblx7RsPwypGa4SbfzVXxwjGJfVBFDiWjUOxPw21Z3D7tx-fhV-3pezjATrYMCpe3cz4NKhnbCRBTniecM6IjiRVbVLI3QCFK95Nl-szslFEHfGnCKI9VYT-T9hCOYFs2DHyFjdxw8RGB4JZyRwDIgK8wKWMpRI9TcGUPYbeWuT0hF4-_quomS3BCVtchKm_d9W28D78OFLAE9QKc7owZqdYRmN2BJVMxdKS0T9-cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=NOtrK3F5XVLZ9UlYPf5izr-E43e4IXkyMHHzeX6zcLpQGy3WZ1MxeYsMRxgsRzjwYCWG9zhx2fDMGiDs2X1oVfcvcvXPXMBRHxtiuM1hqU8ldFunIe0ygUWzoojXqL_mRypstvmYBuVxf3n-8ZO7FX3dI4ET8Tk1KqILr15XEsUI76aiJa0_iRjxfOv5_bMQ78KyBqykOTrUHWc-rO_eOdSfkrpN-RgwhzWWeBETSbwESQPX1mapE1ItN1nfBJaQYH3FJ2pubYUsLivyMNle7cjFSudF1E2ehET6kuGlVuAenGHeT49spTNwYbXdlf2ujA_uAHDYrk9SdowLaSfYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=NOtrK3F5XVLZ9UlYPf5izr-E43e4IXkyMHHzeX6zcLpQGy3WZ1MxeYsMRxgsRzjwYCWG9zhx2fDMGiDs2X1oVfcvcvXPXMBRHxtiuM1hqU8ldFunIe0ygUWzoojXqL_mRypstvmYBuVxf3n-8ZO7FX3dI4ET8Tk1KqILr15XEsUI76aiJa0_iRjxfOv5_bMQ78KyBqykOTrUHWc-rO_eOdSfkrpN-RgwhzWWeBETSbwESQPX1mapE1ItN1nfBJaQYH3FJ2pubYUsLivyMNle7cjFSudF1E2ehET6kuGlVuAenGHeT49spTNwYbXdlf2ujA_uAHDYrk9SdowLaSfYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFw8s-btqeKCab6tRz-XQBnYvVZ7s0moytI2rRTiRj49HTvxbov-0vzoyT0kxy9v-KThAg4XRivloOk8b7AFAMJQ1oFmBCd071KfIxYI4yzfE8_m2235GUBGMaAlIZRCSjV9IcXhgvch3XZc2BR45GYGYJYYU76QY8hBDLtQm2FuxqJx6K8ExfQsL2Krs3Wt6MqlsTUo1h9C6RfEgRtlvMjaGGqIrnmxPrb1y0Vo9uCez8p6d937NCZ874abOcTgqsGaYc0fxJ_Waxer7-0uHoUq8tc36gM-qAxLCPDRqBDZ_q-57_e4Wa1nw0JkYPBE3DCKaqhP2wyiZWge9rIj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePz0nl8ecKyizAfauDzkSLXBQsJoMqvrNv277YG8esEGX59c6axA8FvuTT-Livu1m8tahSvfnZTGgevX1JG-TnEFfuQ7n0ELHy9m32DtJ1NRn4w3Mr713ZGZxoJ9mPR86A51X55OoP5xvT71-wZwEkiuWL29x_67wvl5xYDMuO6_7u1ftKKNu9oVp4qmdFABHfash21vOIA1yyf32VkhXW16i-lJpNamTo0AhTRguW6HLG-g6fHjOkoYlB449HQiSgGKZIcnEAj49fIC2RerbETr0SAVzu9CMAiQEbqAVuTnJbcgfvfWa7c7Wg0pn2arFMQ6poNusu2E2QDSga_3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=HqNmCEceU9zOzKnUgbCE4akcwp_3cU3ID0L7Zo_KE7ZEsPDNfGYNv8PgI3wEqHFb9CXz8wmoxLAq_pn3qdaGH38wZHCSLEsnlv8Es-JED1d0vgaa_Z_zHqYobGM_9Mzhy969ZyKZmLvC-9G-k2t3tFDloC8lWN_1BslFfOKvG20T5O0E__Ur43CRSrIw2l_fn9VRTPYui3dOm8ECHM-ziyJOaGvM0HWAlMA1N7aFYSYnSqxOIEdA8GYJj_jtyoZW7HidfCpgjXiYK6oQNGNEhB8m8pIWjbVemuIPO43qF6DSaxqYMW4ZUegIvIQ0eEEYAloSGlLDK6C63JN4RWK0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=HqNmCEceU9zOzKnUgbCE4akcwp_3cU3ID0L7Zo_KE7ZEsPDNfGYNv8PgI3wEqHFb9CXz8wmoxLAq_pn3qdaGH38wZHCSLEsnlv8Es-JED1d0vgaa_Z_zHqYobGM_9Mzhy969ZyKZmLvC-9G-k2t3tFDloC8lWN_1BslFfOKvG20T5O0E__Ur43CRSrIw2l_fn9VRTPYui3dOm8ECHM-ziyJOaGvM0HWAlMA1N7aFYSYnSqxOIEdA8GYJj_jtyoZW7HidfCpgjXiYK6oQNGNEhB8m8pIWjbVemuIPO43qF6DSaxqYMW4ZUegIvIQ0eEEYAloSGlLDK6C63JN4RWK0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcg-K0e3ceGzh8Dk7FJL_WcqwoTkmy0nNeepR0qQb3tT9DDnWWGO-oTuiOkCBcvJ9P3kH_OiXvtiD-fb-UAdRCXjzMDRjy3n8VqJzFzKp2OP2RWlLqkkIcAgLpuDzSFd--PAVk0Yuk9dBhTvvlmgIQ-J1Ny3lqFNwGf2GZfOYioS1cFA7B3gsCcFmEMFy_KeDusAiE4aaq3tMCbyN9hcn-3By3khzgsqVmv9mxiwR6VN2tyIQMdMaooPYyQfwjHU0uqWuE58G-YBwqQARs7zGD696ntEbvsmSLqqlGBGWysqTwYR4OSFEEzgzV8dS9t2ZshRFYg5W32MhM1J_lOHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=aKCOrHinuhIeNdrtKPe-sECF19xQpyEbc4dnFEAlNR3b0dSS9HoYqsWkBRKRwwFcH0AZpOvPiQxvdfWbfvywv_a4xMb6C1hizlAUFNVpIvrQtI3BXW_omkcWndmewjw6onJ174M1BxgIuB0QXsv09UMt2dn4HhsxQPKAdYSiBfxbM_vzrw0c8nbRSBZf1j9D3L5Qsjt-yl1jVYdW8-hS38VciUwm9R6rXHAQb6riPMa3VVG91G6Rnpm04uMkTr9ghHB8hOHPcJhZ7E_x5ShROs2qGO_I64oY6lBLLqDqfDJ_awH9RVv3Eg33lobvHzqR9Hle8r2eLaIP8jrMlSemCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=aKCOrHinuhIeNdrtKPe-sECF19xQpyEbc4dnFEAlNR3b0dSS9HoYqsWkBRKRwwFcH0AZpOvPiQxvdfWbfvywv_a4xMb6C1hizlAUFNVpIvrQtI3BXW_omkcWndmewjw6onJ174M1BxgIuB0QXsv09UMt2dn4HhsxQPKAdYSiBfxbM_vzrw0c8nbRSBZf1j9D3L5Qsjt-yl1jVYdW8-hS38VciUwm9R6rXHAQb6riPMa3VVG91G6Rnpm04uMkTr9ghHB8hOHPcJhZ7E_x5ShROs2qGO_I64oY6lBLLqDqfDJ_awH9RVv3Eg33lobvHzqR9Hle8r2eLaIP8jrMlSemCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkOew_xfJ5tJB2quQobMNECnRPQo2hHIsCHjfS8Tc_ppQTbxuOG0nFNd9DY5ZN6SuJbdQsAKuOPY1Z4ujz1U68qPbWGPgbpB-K_NOachG5g8DO2jIg-XKaEjkdGhhyz_Ww5XxK9pSxnqDVpZ_XqNakIVArhCNjumtVWKBL-XvwVsQoD6xyiB5Y3dO33_GJ_d1dWp7CfwgJPNL_12XML456mR10qRJsP3P-GhgP0s4rPzz3R3_BvFZybnRg7kgS0xC7a55rBrFBMDd2BoQcROrObSs7DL8l5PBt1bCZDbC2ghDwZcMbYrqG60ecMlLE-OyekSUfPLUR3zp9B1vD2AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARETMlRCMs3VmvdMopTBX05z5qc-hjzOgbXpKu05QhcLi6r-w2c8FWuxcFnD3D7dHkfVwH-FfMsgZjiF0CcqTWcER6tiTuJOS75KP_HbKsTrxpyYDbt1N8sjDqQCjJZ0f53UDFTdks8rg-G3inCFRyoPoMfZ1YOwDVfd-78BL7NYFKDy5DSQlWKbjzHJQpS8V6Qu786GTDd9UIfw3b1oxAfFdcxYnFMWl9vHEPTAokYybtQbqTS1zg5GBbQWSx4lir3ZF3R-UbFkgIagQhOD9hlNNK1lbcUw7PhKzV9JhEUG0aPHRzS3e2Lmqqc5QbaUfhhzExqCJGrgQsjSHTCL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=nnWPgBdoe27H0YnCBOLDCzIkoGBLYgttwOG_aa-vBqreeDETAIJgSUVw2cPVV7TAdoODpQQU_U5xzDaePS2dBs9UvBN2JJStPVC1bJMCldt_1zbTHElgaRqCzXPXo4XfqqNC-2OW2OEdX3-KCJhVFsow_Jn1oT6jIgkHBuq93UqEP6EtMTUvXe4JbiG4aAfClUwOKQ8Ql3INhkDeUeJNaCiy-ZHO_c473iFcoAhr5tesdRv79BdRjy_uSFBWyayWs7SWF8WjvYPk-7rVyrX4VcnQBr-LC_iaIXRkwjAz_pKFZwqMFdMl9ML_4ziNyjd8-ZSmpFzeJz13v4phIZarOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=nnWPgBdoe27H0YnCBOLDCzIkoGBLYgttwOG_aa-vBqreeDETAIJgSUVw2cPVV7TAdoODpQQU_U5xzDaePS2dBs9UvBN2JJStPVC1bJMCldt_1zbTHElgaRqCzXPXo4XfqqNC-2OW2OEdX3-KCJhVFsow_Jn1oT6jIgkHBuq93UqEP6EtMTUvXe4JbiG4aAfClUwOKQ8Ql3INhkDeUeJNaCiy-ZHO_c473iFcoAhr5tesdRv79BdRjy_uSFBWyayWs7SWF8WjvYPk-7rVyrX4VcnQBr-LC_iaIXRkwjAz_pKFZwqMFdMl9ML_4ziNyjd8-ZSmpFzeJz13v4phIZarOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFtYY9J2gqRgTxswCtze65q0iJQdapFv65pK4L1NglacblkI3oGq-nolkz08d19NLoa89mAP3OcgSO3hIo7XLn7Ko80Pp5s0tN80F-rdVPejvc185KUsNne9df5HXToJeBsPqINxj3lFylaWG5kTisjswkf9gcaKXdradTGyX4rp5A4W2MCTusdb6f8kMnAbqzSDd7vlwxcTtyCrk4ayfQCqpf4b4zlNRTd2Oak_RRHzt2ISDyLqeyN-kXKOYyM1yCrgWWCc4USrDmIObpAIGsI7udrHMq65WdvalOAchqWvpzcFT0Pl_BccLCBA6JlHiGuD_JDIV2K8FdUYSXhSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSp_sngRmTgyFE93o7rr_5Tp5aunEkEUTuqBa_W9QewOGaZiLkWekMbrp7myUdzi9dMOe0efHBX5_csTJAHh_nPMDNOIQTTLBuMZ404dA-NGfTcxU1rssB9q9uu6sG3ogcOXh-La-uQwAPel8zjvjR1AyoDqFDh03w_RN1hiG2nbHIrBRB8aDUn0wl-qAxMt6tfQDFKH1TYOZCW-aVsnsdyA_L2a0pffOuw7orNsefQPfSgArI2PItJ3yXvdKeyCPVLYlOCh4BhgIjSj_eFt6pzQVwKXNTHI_Bl5QCjer25cy3ltWQYo841W-GK8MEPRvPQQZOzCMtyozBjhHo4UHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=JYgEmHosfxg5XmKHesnhpxOYYM_nvgBqrZBGWgjN-Bt82fW3qSM7rO7uaYx4KMjZAHVlLKhdPAwtS-pz6tq891v8tMW6No_k8PtLYWYIkAR_GwrDzUV6hZ6GXwr-D5X9AVdcbpVx2skNrJfFUFg-f7uKVngohCG7ADZH4ee5udrUqUAy3AhVLmlnru9ljKzV1Gs942RwzZumhedXWE3Zfrgja9zzoPFNwxPd-m1OVOhlHhyBwDH0V_Y1XWlGSIUQ57L_e32MP1sfbNJLSdMLRP4uZB15aFx1_Jbg5v-TiHJ4v37ts9tmpiyTR4EWQxqTkYxjFu5_ytOz73Ns4xSqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=JYgEmHosfxg5XmKHesnhpxOYYM_nvgBqrZBGWgjN-Bt82fW3qSM7rO7uaYx4KMjZAHVlLKhdPAwtS-pz6tq891v8tMW6No_k8PtLYWYIkAR_GwrDzUV6hZ6GXwr-D5X9AVdcbpVx2skNrJfFUFg-f7uKVngohCG7ADZH4ee5udrUqUAy3AhVLmlnru9ljKzV1Gs942RwzZumhedXWE3Zfrgja9zzoPFNwxPd-m1OVOhlHhyBwDH0V_Y1XWlGSIUQ57L_e32MP1sfbNJLSdMLRP4uZB15aFx1_Jbg5v-TiHJ4v37ts9tmpiyTR4EWQxqTkYxjFu5_ytOz73Ns4xSqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHA9nW_R2I3bT2BXZ71zkY6Y2brlvSsBydL7SV7gK4qKz1WTFaAwDh-udyT7ViRoShbEcD9GYe1iFyfTbCFgMnFaOt3AghPeXUfv37va8NAPwe8HDrQtaLbzMUCl-NlMfAyj5op8WOZ064rb1s2v3fzScWb4IsFL4KdEzctUNb2ES8jv5byToAqevjNURWRm-oRzmI5dUkQ5RR50j5Ib8-QzEfHcpbz_sgpkDTSsuw76mLoFVtWL6nvDHCI7su6tI8fx8JolZC2VPVmb4UKyJiIjr-9Q9lCJLLxTG9ohqAo1jaAS4zDE1qvpuc5xkMUhPuo9wxhmun6ZusfxW8afBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8GVgR-PkEaS2n0XV3T9bPfzcI6VgdvWANya3Wp1NhCNepDuAxS3trn2fQtixXr-rLwPl93WpI1WYfEN7GvrFK-cuJWhHetjAyUpzYZnhG3Yu16mqqw1Hhcx6Xrd46R59UTLMYJ4gOM997GNGsjXNw-XGHqU-5tc_UFgasNt_VbUR8fnjYktuJfCHSZ0BpN3wLmS9UsbWcmpxHlTXWnnahrEd3fXp8a6noB6lFoBB9jXsZvWAy3AdDsHX4tyYIItzh58zgCwqE1Sbftnue2bXcR8zvURvRRKrRaK9uaZsr0WXbH2nUQrVSHN8GQSm4pPYh0BqYytSB1F25eOE1zLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hthJuz1acMYBkql9tKSa6Q2nc3Z3bRuTV2ailtPFe-vpDES6FFeEEKipT69YKuCTQb5nA-rKAVBuoZzOejYSsE5ZLszf5d-9L1mS0dYuy6PvBkEYE19Hcc85XlPlRqaU19F8KLRpe1gPxnMo6m_AXAqsix5mEeSsK4NX-YIfLs3dvCkt-1t6NgNkKyxY7mt7MaQ_eHsSW-0oURnJMOew6tvKqv1rJH114HW-cB1ipMtSjqPsI99Sib7EHei5AykLpSWtAMtLJSCIn4D7Km2DL5eY3dLhOg55psb5cgduFpmXnNiDqDm1R5fayb8QmssZ94wJc0p66V0DGREhj7mswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LG8BFKBdHEmvadVptQAhZlHkN4Rnxs2JKCYrSvpfhBObDUQaqsGzuR9uOT58iavQZsQe70qquHQMQQwoPQ756lXafNZuDqY0H1YYuGxYS5bkV99qN77wUh9tGnqtOeorARy5h4ZwUri0Yc0dRwoGS1I8W5zcmtAfvEm_pOuZGEpe1_sqwiXgW0c60R7KYqWiDox-hyZdH0AR07N7T5lQUF_Op4UIefSVUPL8dHRAfduWuU3xK-th7UDqFHoKD0F_xmWsWtvXllzQcjtSXTLrLUxPmRRLlU_75p27ko5CXzMESZkCFBRTnF3_ZuFCdVs9R-a4ks3m0A5O3pA5eEt8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcOnc00i4StZlqZmhiE82MhTIxjYnzNenyASWmH6AoiBAOmGBSZSMLgB30am2E_tV8jmjqpcw4NHeSxP8CCsfJf1dmXPwwuC9K1A_Ql-gvcXg1zWdrs8-QKfOZqawSw-WJU0cbWSp8rXQKfXurjA01JCT1uTntiICWVhMAZjVbPWgrvscb_s-qgq7geVbsyZ7v9AAaWoLtcJWcu-MXTZ_QxR6UMfir14iuSqXrr8N4Xy3OCnmOc9PyzVZqBvAHA_SHlD8YU-4oF6yf7PfHACCA17HAZ9lQNNj-bMrJY3kAqDHAzkpTNwMxE5cTShU0b_yuT8vp-yp_SCyE1BBVFSUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQI8HQ736dwu4YzTIX8MZA8BOW_IPr7nWWC_TB27Rxguu_0Bs6DAgcA48XdGycbonD9tM19z9Z5rGfVqIm6t5_iFdkkEWqI5eMN-Qb6xJHiqb-Izqrcl_OtMCgYxkECGjAwmT6-VuBO_j7AYNrn9Mb2w2rRJGYsPz2rc5DkUeI2ZCPS51DIkEINQxaBCeBYOjV-3vwT0YriEeq16bN_tPXhHOs6obDmp5rzirKaMZBghjzBMWpJYw3x6UMdr7swpD7lGMX6aNtRZUqDOYiZ1gTei1QcO9vQ-Ns4LsLZEylQz4wCgyaXy79uWIw-stoODHDWogvkSWoKvzodLzezV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoJurEwrUYaW__oJXETzTPhjL4oNq8drR7kQO-9BkS98ILZaYCHYRruVS7yu-kr45_y2gTZe6iZWzMKhYyaeCfsZya7-6AnTBPCz5vSpIEHfYkivd7sp1F2ldfHIy1iqJeiYl_757Qh1Meu8mK6tVOYaFd1q2kocgXZGlqNzs3lOjwFA6ODpqZjWq2ePujV9OD0I042yK9DlFnN0Q9kKEEMDKdQzJxowETNssBIHQ5fxY7hUL614V_yoxZGG1l87-jeuLUCWUS6st9CeqKyb62LzoZYSq88DQ3zHUDWjNEXcrpZNhxlNAGpHyOVhhrvOkaQ3Wg_InExUCCoZprTRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=uWcORYBEdKCZ6hQnDLJLGJFdbbIQ2x_AUtCFEMR482bWXpwg1X_jTHDBg4mpRZg8ku66IQpo5Ax5IT54kKdB985MaNj0B0_oQffXkUznSw7HoLteNitXxg-5pR8UYLKOhEKFY7QTJEliX4qbvQODjap9liq3WTpWekV4DnovLdeZgFkYwn-pdDxNKGWJRH6a8DjR3k0jx_U5u_oFCoW57ff2XNPO6M9PAIS7kbm2pI6rzEkl1CFR80PA4Tin-4Ah4TvnbmSAiN37OJKLXEBATtjvjn_osR5ICtVtjYigHyXNklMuhR3mxqd5nvRRenNeH_Ha-KcOfeE3hAt-z-iDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=uWcORYBEdKCZ6hQnDLJLGJFdbbIQ2x_AUtCFEMR482bWXpwg1X_jTHDBg4mpRZg8ku66IQpo5Ax5IT54kKdB985MaNj0B0_oQffXkUznSw7HoLteNitXxg-5pR8UYLKOhEKFY7QTJEliX4qbvQODjap9liq3WTpWekV4DnovLdeZgFkYwn-pdDxNKGWJRH6a8DjR3k0jx_U5u_oFCoW57ff2XNPO6M9PAIS7kbm2pI6rzEkl1CFR80PA4Tin-4Ah4TvnbmSAiN37OJKLXEBATtjvjn_osR5ICtVtjYigHyXNklMuhR3mxqd5nvRRenNeH_Ha-KcOfeE3hAt-z-iDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV9Y09DHd7gKwXmT-0pRrobZj66A-WXS1ZQBiBJeIR7eu51RAjH8fibRJD30C3-CiUeDisdBKgKFt7ip2xlQRZ4IPrFhiP6kimR0rskXH9Z4TBApqqXNmTCpsmELQ6D139nFTxAAoiyyF7vZAdmsIHxv7b7lfXkN6uuUfijmCezaPLkJpzAzYNGo3vkd_QCeRivMO2vX34Ed_vuJqX1viWgpZkyJ1cpKr28kSr8BU1YuFjd4mNkD6Imp-3XseL_vpW3uPwyWey1Efy9LxiamlZng9SLQ-1M8Y7HoHsG_W5RcJOyMwWSNGUXeefeWD2vELdCMTGjS9FBQsMaaU7Cmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYmTPmizhaNT8PekH-KMwlCg5Xaa3ftvYL-l-nNd6_C96Juv8i6z3DgZz_ExFijUxj_BBrfKkfYFYGK5w0B7jY8uU86umEwqn2zSaIS_bnGMltQmSv1KtxIfeu_NcTSWt78P9TPPMjkC-_wsz5_fwBXL0ws6PhggcjFrlgWabEJ-yUghIcHK7E_b7H_4OFg7h_Rrh71sr7aG2uHnWiN_BUdmSzbt9LOVVULvRj-lA_1hISYXYR8Io_MmTNj1SNXvm5DWGSOMgqIc8ViK7Kk2QQwzC-Xpyu8Sx-K76Sv-33ABthmfa28W0AEdXNeN00tENu0cpziiOncauwyDu9p8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-GYWIOhyiLr1AcglzhE9ood8vdB1YnyLzrzGvdTJAwIWcp2i5inDbuSbm5anbZc3qo6Swr5T5JtudyCU3Frr1QZT8LfEfgb4Xn-_RmIK3zKYRcZ9COCXn3wwBygdpPdp_sXM_krccYsUaEl296Sc_aKYzeGdwZKAnMTH7KX-HAwWUSkRUdpGP2BZT-uv3_rEx2sE5HmPbW6qTIfrLcJ-oYxxfpigUO0h8Qh59sv49dz65rpeEl_LnQF7kyGdReBJoYQC8V9PreWF80tiCVqrxxado_ot99iNbZ5_TSSYV4u5mGj9qE3Q7-bjOQcjFbR-Lhuv0Cn_EbtGMTF3qw3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBGbT1kknxHv9GF7OuJxYJnn5mNexpJuDMAesn_HQL6l3xaSTQxsg319M9M5UfcXX1OxNTi0WmFd1ll00URSdwkgq_fcaqCQci4GCXgcRtVhpQ2JPGt6zwYazLy0oR8hzoBgXeuP6wkIEEyXVXPUMDNuFUhloIy2I7akOpKT598ELDXTIJnMzmbAd030juTr2B2h8k1go5i-Y3zeL6zhzyfUgjdcUoK9OWp8VQWEK3-R2wk2hj3BUNIUv57ONHOz2k2NAfwZfJY3mMxmsP9Wh9VCTgCml_3eJapUUNqne0bIsUz0OowNnKkO1IkRt9kHoV8kD5VGXs_B48rKB2tXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=X9VGnbWh9v_x3tdMmfjASEP9XzDF6novWHh2yoSbyknEm9FuTHHV2_jEGK05La_jnJdAfITcXvU6-1uDRbv-rcBJEJjEsmww8eIbMvdr2nzDXfyig7ndw8qf0mz-heNNUjh8ZrrNhPygvnj_0uhhMwhu4z29iey1Zg6un_Ixz7PSY1u7frIWxT5WTmgF1-8t-9DMjnmNF8jMql7_xQV-OOidKfeO-UwbUD1h59omoXCptk_uUTnDvzgZS4FerxDzJUedj1V0mVRC0vgWLOQhn01JbeIh_gHOJO03jvrpMA8x5exSJpGUkWnZj_arffdxHgyvbCCos458n5qcgoPuuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=X9VGnbWh9v_x3tdMmfjASEP9XzDF6novWHh2yoSbyknEm9FuTHHV2_jEGK05La_jnJdAfITcXvU6-1uDRbv-rcBJEJjEsmww8eIbMvdr2nzDXfyig7ndw8qf0mz-heNNUjh8ZrrNhPygvnj_0uhhMwhu4z29iey1Zg6un_Ixz7PSY1u7frIWxT5WTmgF1-8t-9DMjnmNF8jMql7_xQV-OOidKfeO-UwbUD1h59omoXCptk_uUTnDvzgZS4FerxDzJUedj1V0mVRC0vgWLOQhn01JbeIh_gHOJO03jvrpMA8x5exSJpGUkWnZj_arffdxHgyvbCCos458n5qcgoPuuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=Hnr4XkIcrW8HLpHA99s4NHsgq4d1ttFZ7wkrM5SRESfgUgd3mZCCYUk5rcI_yXmEDNrhs_C1sJFCREfbPJ94WSQTtwUJ9m2XfEVZ877qewe6onLA7g8k7jMmyIyWvqmW3EZKJTWhjpk7wxCG36WaaJE4u3Q0R9Y1ICIAVXDnseIlZ6D-TUFyfqHGRg29qgnx4KfEvKdbFEKu13wO0uWDuW_LRmRxDr2dyyY7SAz6tJI2ZbUQ1yQ3LDXFpjOxMdUOd0KC797TT8p1CyEnBd8UEc3P3kB27nWj6FXTvtC7knfD1KdWHTuDvkHAqZi3idcyux6guCf2XqeT53bSSVAVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=Hnr4XkIcrW8HLpHA99s4NHsgq4d1ttFZ7wkrM5SRESfgUgd3mZCCYUk5rcI_yXmEDNrhs_C1sJFCREfbPJ94WSQTtwUJ9m2XfEVZ877qewe6onLA7g8k7jMmyIyWvqmW3EZKJTWhjpk7wxCG36WaaJE4u3Q0R9Y1ICIAVXDnseIlZ6D-TUFyfqHGRg29qgnx4KfEvKdbFEKu13wO0uWDuW_LRmRxDr2dyyY7SAz6tJI2ZbUQ1yQ3LDXFpjOxMdUOd0KC797TT8p1CyEnBd8UEc3P3kB27nWj6FXTvtC7knfD1KdWHTuDvkHAqZi3idcyux6guCf2XqeT53bSSVAVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=dqJQOaF-PtXNE-MzpsP5NUSzeUdsvrfn3kS9Mw5ekGeEixOcTnCywn1Ib7PAquvLZR3xu_qT1rh2e371Aba9HyO-iGVPNFTC5tw6wfV93ID62mIelTmnA5t4G3x8p3cl-fVce0xjUScUpfvxdQI4zRAvy0xLehV0skcVgWVWEsEZyhu2jmoRQSxiyDmsyIfb5PY3M5eqH99cfU9piIc5prz2en3F4AyplHludWKX_Hq0yqDaicXn6s-jfd8UBnGLpO-UthwV9EW3ypf-efCWMuFjxedT5Xywxtn88w01c96a7x514JB2KDmCzxd7GEqKN-wouv89Y0NjYc_VD0cn-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=dqJQOaF-PtXNE-MzpsP5NUSzeUdsvrfn3kS9Mw5ekGeEixOcTnCywn1Ib7PAquvLZR3xu_qT1rh2e371Aba9HyO-iGVPNFTC5tw6wfV93ID62mIelTmnA5t4G3x8p3cl-fVce0xjUScUpfvxdQI4zRAvy0xLehV0skcVgWVWEsEZyhu2jmoRQSxiyDmsyIfb5PY3M5eqH99cfU9piIc5prz2en3F4AyplHludWKX_Hq0yqDaicXn6s-jfd8UBnGLpO-UthwV9EW3ypf-efCWMuFjxedT5Xywxtn88w01c96a7x514JB2KDmCzxd7GEqKN-wouv89Y0NjYc_VD0cn-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUEDz0Bf67AhARl9-tU5O0-wLlECrytvXyX1xUVUH1gVwB2VmV6eke0djeYa276VTjnxfEnOCzrz9QBaSW6KWS868YLg2NOBc8tPSssga4OQIQvEHBivxfYfA4XKviONxOPRFpSay1ly8GXU65-DrXrv0PtR2Iue-Qm84b2IyXHwjVJ3VUM6wpE5u2AIyNZAVYOuQMk--8xGvWpToMUyS88k0vRY7edWu5dPswsNfUzlfSKt83Z2JrohvgUZXLeiqm13TEOk9LSzmcQyLGhE7Rlg0OQpdDw_Az4Q5qRyIreAeffsT2Y69Eo4rEhJkstTgcpCjVmGLF1z3Ruw-aj8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBZ1D81oQ2AnhGJuWV1hS-D1tggoJybVgMbvFhCysoDF-ro26IJuPARfHkYWhnGXYKXJ_0ZgmTs6unT_l349_aRJt8LENEt0pFCFTb2NUu9GB1iYMNCtpQFBdQqN-0RwRQquAUZ7-4IY8BUCMTombXcwT8SJDvCtGhRFQrCcCk9PlQi9HIyzEWC9eqj_OY8o6Fw7I6ZoBjQMVn_vtvm5a21XOqRQYjtiEUwVWHw9Xdp9_H3wiF2KNR19B1ETaxJQm7nqNZu2jFBOnCQ1rAkJnuRMM45z8uR2NY6ibOpK-aTUgWdF6OAXG6qpAFfK6iPHGK2I5_sDpx04W-C0Xt98OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=bJDMM7ylIH88bWNXLil3qoo8ePcsqtO8N4sGWGNy8Sj6_EbYOxP5RmvbrbuS0Ov3OWTKkH711J5KbxU4GyDsxUutNu3qLKYzMgSV3QhFyRZ6U68vxd5NyAfNU72px47kZWQKyt_2g713aX74QKPMsHXSB1hekbsoZN-rUAmpf9HdEG01RR4PfLf6DH6GwtFzv_TbliXZWzWPjoZo7MDc4M8pQO5gBUBrvo1a-NfeZCUlBsJlf6AOUAlgCDG4Orzq7dUgmT3YWIwiDBHlNQvWc5YrPV1-3uZBPQfrRQnaQVaja26Fxk6ddZRAi0HJTovJO7iDQSgMJQTPurQKeSd8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=bJDMM7ylIH88bWNXLil3qoo8ePcsqtO8N4sGWGNy8Sj6_EbYOxP5RmvbrbuS0Ov3OWTKkH711J5KbxU4GyDsxUutNu3qLKYzMgSV3QhFyRZ6U68vxd5NyAfNU72px47kZWQKyt_2g713aX74QKPMsHXSB1hekbsoZN-rUAmpf9HdEG01RR4PfLf6DH6GwtFzv_TbliXZWzWPjoZo7MDc4M8pQO5gBUBrvo1a-NfeZCUlBsJlf6AOUAlgCDG4Orzq7dUgmT3YWIwiDBHlNQvWc5YrPV1-3uZBPQfrRQnaQVaja26Fxk6ddZRAi0HJTovJO7iDQSgMJQTPurQKeSd8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=GKulcnJg_Pqdx52aI8ygagmQx8HhXXNDz7-52VKBYAoEBn2UtpROR2zFExyMaQm_kvG77E30jXgOBzgAuzf7pXDJwwxiKeiXbu-mf6UHEuDDaeWLWjWJbrFvjI67JSRqSr1tklY8bZ0nqLeqy_po2H5aarD1DB8C_349HZ5CGswudEIwG3lPkw7dGfXmFcfV1QY1je-NiOD0iRVqY3FdfKUibgS9tNITEt7lLD7RHpKPVOPE8M9LkN40Zw2DEWZZTS79fcFcv_g3P44vb23HJpJ8ZuSkN0i8VqKYGcFzk0i74-rylEbhsJqhzmZnkart7lwTLss7qA69iBIEzeMkbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=GKulcnJg_Pqdx52aI8ygagmQx8HhXXNDz7-52VKBYAoEBn2UtpROR2zFExyMaQm_kvG77E30jXgOBzgAuzf7pXDJwwxiKeiXbu-mf6UHEuDDaeWLWjWJbrFvjI67JSRqSr1tklY8bZ0nqLeqy_po2H5aarD1DB8C_349HZ5CGswudEIwG3lPkw7dGfXmFcfV1QY1je-NiOD0iRVqY3FdfKUibgS9tNITEt7lLD7RHpKPVOPE8M9LkN40Zw2DEWZZTS79fcFcv_g3P44vb23HJpJ8ZuSkN0i8VqKYGcFzk0i74-rylEbhsJqhzmZnkart7lwTLss7qA69iBIEzeMkbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbghPXWsmfMsrcpXVelJrNyiTXuQIhB0P4ZNZG56BioKMzzmyG4XZ87AhD56ImdzvokPGtPpHCbal4FriVisFqDjHXLbrThXU8d9NCX4Rz8r5AvIyXYGOfFnUZE5pZf-TfcYX_KwIxzGCXpTD65Uj51WaBuYms_ga_6yJODsXGyBsRY6i7BP3SXPjyld7c34hpe81QTikLvk2zsqv0m2cQj1ABooqEYibRI7Tq1pyjL_1t9pffYnLufxDynhpMkKEUIEVP5pzii5vxfM9xu4I17vnrTqHlTvZvRodX_4JVP4wihxBgmPI2dcmWGTssrSjikuNmcYYO2YkiRgPwuv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-M1zWiKVbINyZWBarVkL6wn9qrXQqGKAJHpssnCdfDV-_ylNvbU07EWm3blL5o69If1Wzeg9XigAP9YDMYa2KasagicJD1sAz4OqY81iW_IyBTIZfIac1HdsNix18vNlgA64loOCeu9KxoSpRtPOSL4eoGSrWg89W4LV8wZV2HzmpvKcxe0YZRQL4MiP_oxcTLZ8s2IUSZX-rerA9rM64Yn87UpUSFozyYGucJkBRJ4v8_19yck1SnE49w5WtdJVjVfqg4EIS2OP89zgy2y5tjNRoLsZ47EBNMERKeEQYuKQTCTjnkfVYQRwdtOw1icgkJavE5KHkRj2Ds4-lhHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1cIu0BJRyTEuSHjZkRFYmmWzlTZ-YoQh6BWTjs393cNT9bbKNpT2ksL1rhVnjzM4Tj0_J_Zsx3LVVbYDlp3g0suZ9f2BZPYPsS9ubVOCmqdTMAYUy1wfrXEW42jaEjtdYU6egWyCgpQuPE6vaN3rwGUPJHJ6Vivxmtx7ftFhcoo_lME31jsZeTRGtyIOewJqWmfRmLGSbX_uhrxuFovsQCysxbkHrmzUdUqHuEXLppcFrH37ugvgUVNMUtuSV9hr9AReoqQYHbGTGVXXZHqJoEgt2KCqBUIeIxyTcrfJgzureLACQ5uSz6-9qiIsWpJ87gUxSO5-JtLTPebTJJFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XEqXQIPjlZTiC-fFi0oAXf0UuCesvd_ZUrJlYltfUOp8by3Ry8DhzcldUc5Xsid2KjK9a73JBQyxv8XQwJBXXCgrPncem9rzrkSwdzmaepEHJXHLASRlQbifIPAi8HwQEGMyrtw5dTsM73XsloXAKkIbiQKSSa2UwQC-9zKThc08_RVuzl6wXm9WioyQ9NnjhMkoSzrXuOb_1uw8e7c3UxCzPJqvp2eXbJAVaNRLE1Eh2r5Ifazjd8GZai5eDO9dbfBtd7a9g7-QJs-EqBPDOZVzcWE2i_CshlBe_K9rWj3HVjmoBpJg0LyTFG4uUjxJNt2B3GNRHAvxeuobJiwRtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XEqXQIPjlZTiC-fFi0oAXf0UuCesvd_ZUrJlYltfUOp8by3Ry8DhzcldUc5Xsid2KjK9a73JBQyxv8XQwJBXXCgrPncem9rzrkSwdzmaepEHJXHLASRlQbifIPAi8HwQEGMyrtw5dTsM73XsloXAKkIbiQKSSa2UwQC-9zKThc08_RVuzl6wXm9WioyQ9NnjhMkoSzrXuOb_1uw8e7c3UxCzPJqvp2eXbJAVaNRLE1Eh2r5Ifazjd8GZai5eDO9dbfBtd7a9g7-QJs-EqBPDOZVzcWE2i_CshlBe_K9rWj3HVjmoBpJg0LyTFG4uUjxJNt2B3GNRHAvxeuobJiwRtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=na-bDA6T0acO71tw81uGDo_E8WpLuKaZInpFNgz-_8U-_vVdc0C9WfUTwn2mw4aUj1y-XCoWWgpdDIyNKyrnkuCTX8GyLRyPEITt31T47zQSDUFaeYCDa-ipVy-GQkCRnnT-0rb-sXuv6INpWM55SjyhbbNEJBzMaV_XodIHLdIsREtRU9vz505DddMSqM-9RitKoi71vEYDKek2tsghd8xywsjeQ8NlizlyJzKh3q_uFreUo39_swtERQAgSwngS170x9CgUkuEfZc-fz6NIAvnXxHOwd_T_Veiakl_3rYFAo161v-ALwsgV_vWMRXdR3D4OVpO_YUouUEQLYAumA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=na-bDA6T0acO71tw81uGDo_E8WpLuKaZInpFNgz-_8U-_vVdc0C9WfUTwn2mw4aUj1y-XCoWWgpdDIyNKyrnkuCTX8GyLRyPEITt31T47zQSDUFaeYCDa-ipVy-GQkCRnnT-0rb-sXuv6INpWM55SjyhbbNEJBzMaV_XodIHLdIsREtRU9vz505DddMSqM-9RitKoi71vEYDKek2tsghd8xywsjeQ8NlizlyJzKh3q_uFreUo39_swtERQAgSwngS170x9CgUkuEfZc-fz6NIAvnXxHOwd_T_Veiakl_3rYFAo161v-ALwsgV_vWMRXdR3D4OVpO_YUouUEQLYAumA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=VMQNoEblNujB9ogzcmhUpB1HkZmD0hSDcrs_Qb5z0X02UpHpWUSQJjPhAHnz2vRKkslnA0D3hJc3OLM8ECyM74cDsMFe0hh3UKGNAQQ-i-pVzewjrNEUiOFwYBO6faS5agcyYvr2ZmJJVF1gOWmNnEzuwfrTDI3eln2zJesc8oYBko5S4ttX795wQ8inb4roVl5rk-omKmmqW2dvVIRuPycYYbO-5d8fXTbmdABTK1OOJUPmmu9l5IuPoUOXWFKkrmrlMC9wfMl6jvJDiePiFxFuu8JBwKVO38SgpqlnZSKpk1kvU7QlIG99Gao-oRNecjLpLOMbvHTeWDohk3_NgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=VMQNoEblNujB9ogzcmhUpB1HkZmD0hSDcrs_Qb5z0X02UpHpWUSQJjPhAHnz2vRKkslnA0D3hJc3OLM8ECyM74cDsMFe0hh3UKGNAQQ-i-pVzewjrNEUiOFwYBO6faS5agcyYvr2ZmJJVF1gOWmNnEzuwfrTDI3eln2zJesc8oYBko5S4ttX795wQ8inb4roVl5rk-omKmmqW2dvVIRuPycYYbO-5d8fXTbmdABTK1OOJUPmmu9l5IuPoUOXWFKkrmrlMC9wfMl6jvJDiePiFxFuu8JBwKVO38SgpqlnZSKpk1kvU7QlIG99Gao-oRNecjLpLOMbvHTeWDohk3_NgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=dwS6WetqZEgX05MU-He4KCoNCgPJOdxTq4xVZWuwUGBqn-A5snZ5O8r737OKWeZIbTu3MOGSmR22G1iIUF3lzT7U7hxuJ7zgXa_ieqljI1gxKsQfXQca-1t3tvbLZeBvw8cR_ukk8EVTZetJ_8FUeuSBvszKubRSTJwhwFiaI9wfTx3_xv4DRuPObuSIOqiNbHdlxBKBdRu9cMxstMkdEV9rWoyou3D0i5CdTGRCXqxtsAhBFk095ns2Bw0QuJT3eFMBNAsKikY5IXbUTVDeFRZnlod9w4ND0o87hAZ0cGMoVZMo9iteUv1Cb5mN-OPwtFAczUhigDTotSNFvU3FlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=dwS6WetqZEgX05MU-He4KCoNCgPJOdxTq4xVZWuwUGBqn-A5snZ5O8r737OKWeZIbTu3MOGSmR22G1iIUF3lzT7U7hxuJ7zgXa_ieqljI1gxKsQfXQca-1t3tvbLZeBvw8cR_ukk8EVTZetJ_8FUeuSBvszKubRSTJwhwFiaI9wfTx3_xv4DRuPObuSIOqiNbHdlxBKBdRu9cMxstMkdEV9rWoyou3D0i5CdTGRCXqxtsAhBFk095ns2Bw0QuJT3eFMBNAsKikY5IXbUTVDeFRZnlod9w4ND0o87hAZ0cGMoVZMo9iteUv1Cb5mN-OPwtFAczUhigDTotSNFvU3FlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
