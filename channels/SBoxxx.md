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
<img src="https://cdn4.telesco.pe/file/Z4ErEvFuU_W3foMTKVH8OXKpSR9qrEn2_vk5ugQj4UBPmt3cNrZ4Y0bfTVokdLsi29Eq6f1EIhvHfcYSbGLCW32lj-Dp2WlrxEEmjFSHoUasnBRrG6s1KmOT7o37G4zyBJFJTBQb24Q6a6j8O6xqg2h11O5gbXnJ_HUKtEfk88mtRu3Z4iZqkhfW6fy7qRQYxGfKl3rmqqge9SoaN1vLGCmYxO9dwcNgv4TEhyA7ZO95uxgkHXUfuqgYhsV8sPeMpQt75-WT8sblm0EcGfxyNU5fmdqrWWZgn5_3aSoxgW36Y1QQcZyFLjRCzH8ka1VjYRsVY3Dh7VGFszdTj1wyLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل:
شناورهای جنگی ترکیه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آن‌ها مسیرهای دریایی مشخص کردند.
نیروی دریایی اسرائیل سطح آمادگی خود را به منظور مقابله با هرگونه تحولی در دریای مدیترانه افزایش داده است.</div>
<div class="tg-footer">👁️ 282 · <a href="https://t.me/SBoxxx/20322" target="_blank">📅 21:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/20321" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20320" target="_blank">📅 15:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315342d71a.mp4?token=SL0DVlo0G18RYgX_1RHVcACQjufYpTeZUdb4kZUhp_IP__lMXRoCV-iJwi9B4Nq2wvyVERZSWoJHXbaRRG4UJQFts0k3JVDpzvx48l04TbCDayLJuAdFiSDbnxHHw64uewc8rcGew23L9ZmXS3Ar2q1P9tH0zQl_oxAHeR5pZfsD2Zo_yfSd8YTsp13TOKbQwEQGAmZsos-PVNrhlO1iKPOTDLhwHfmz_pvLlj7ChuQB-Bu9u4w5pIDeHBwj9YXSDqAO8g9LuZFSRtXtikkE1KF87RBUvAUHWiX-lrrAP2jTvuA5pCjp5iNm-zs7DMoEWyU0vsqNrP2ebezJAa7hcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315342d71a.mp4?token=SL0DVlo0G18RYgX_1RHVcACQjufYpTeZUdb4kZUhp_IP__lMXRoCV-iJwi9B4Nq2wvyVERZSWoJHXbaRRG4UJQFts0k3JVDpzvx48l04TbCDayLJuAdFiSDbnxHHw64uewc8rcGew23L9ZmXS3Ar2q1P9tH0zQl_oxAHeR5pZfsD2Zo_yfSd8YTsp13TOKbQwEQGAmZsos-PVNrhlO1iKPOTDLhwHfmz_pvLlj7ChuQB-Bu9u4w5pIDeHBwj9YXSDqAO8g9LuZFSRtXtikkE1KF87RBUvAUHWiX-lrrAP2jTvuA5pCjp5iNm-zs7DMoEWyU0vsqNrP2ebezJAa7hcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح یه خط فاضلاب
به مناسبت هفته دولت
اوج خلاقیت
فقط اون روبان قرمز روی شیر تانکر
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOmbX6Iqd8Qz73l0lk0UuNIrvKdpBwkyaacihwR0MJ7v-Z2QOxBP8JM80Xu-J724VVnlSfQbbZ2zspegw5zFkjd_qlV3hQMX_OUPyFMS6PAQshV6ALP77udUR2Hnf3--oNxBxuNTVtdo5G2XHMAxrT4_uTgvbGvQMaUUiWxMm66vgCuvdleGiW59Z5Udnd9ZHb1gM8euNBWFKYuHLqT950zhqWkSKOqJ2wF55-2P-Dmwmig5lDmYohzyy0qfq5jZJO1yHO6zOUC7sIifLqL8zQINFoIu--FyfjkXcgy_K7UbcXuvFB0TNrgGOPSAMfxoWLDM8Ty_fZ-GfAv79loocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClDkdBG5tz9HgGHocur5ki9O-q2vvdjOxp_uYLWhAALPuWLDUI5tG0RoRnHZknhRdW0hyLy6IXrq-4NqAe0CLue5PB_YkOU2kHQ8Wo8v9mjq7vG8k3af2bEPlvHOcZuQN90QXmZ2nWLwqbx3CTEpbXaDsm8nvNleQfTO7X4nFuRqn_k-wnJmgpuiBUjZ6ArcFucIA3wGnSlRONd9crkVKHHgf4EXsa2zAl8T8S1dpDNdISymUHpMQUW0Eh9mEOuw08A9hn8195E__VzpDXYQzRnFP93pUPgPYhEiMDkxuGnwYyBAgSb4CMoxhqnlFuK699RPchXMnYrkL7uU3gqynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6GQd8Ftosk-0qo3nLeTsSnufMc9GaXRpFok3SiSGDumnucWfsWbOGkXCbbtrxcRLcXkve1v0jX1ZDJfQnrbEDOxnukw3NO-2SNlqdBnHW_XfTx41lg08g_GlRSMORuyvgoCi6JlWQDONEr_4uvZ4vd1Jw7t4IJc5JkvvMGq-ILovuGbf_orG4geU_hBDBP6RuiY9RVsGep5QmuJn1ZfJRmsFTRmMHvjCJAVm5J2U_dKXWjkgk9dxNm_uLswhbOOSWbzaTYGZkWt0ylqPp21Vh3td4HPmuxnI16IoFrxaAldacMNlF5LOjEtZO--gh3_ErEGtW-eBGHan3u5SlP2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o74klLHGquZi5ceDaUABKter_BHIvF9A3vl8SFT8zmhn6CqWImSRULXvovu6OhpnPHpxnrP54JiaXntlFhTrYmOQlgx1-FY7PSehzRFuoXph_-D9YwSBISrm3DgZLQlF4wX9TtCAhdlZ88d7bRynHlPrbHPq6vLNvDNh5131-tlRwiC3NSnUE-_fDf1OUqfkgrOeUFh_qssUlQJ0WRQzy97My8--hdiMNpEdbWdfq-UZ8Gg4wruGq_9A8aLIuop_37ylbHTXbMwIbvmb9nIn3VBjQqAJDqSSWyG2VYKb5302Msg9fsefwpJQTykXnRsFyDgKNS302BA_1V1W7dCo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai-eXd_jUrAIOMBSMPy8KmUU-KZwp5JLhSRl-zHQY9h0Wm4tTS8tquoYmRGVFjjEHBkoxORunRayOXKQAU4gD-C8nE6cC5dSFg6gRjzJGXq4saDgoxEZKe0Lcn0GQdt4D6Ly9v7Wq9W1lVK2Ne-EeB1mcCnhw6UqJUbB-h8gDjpP8WYhTpmzIvp7HFCl8ib2AOYxTkhjx--EYoUCTCDE21alhhe13P5hOj1VSKDPSdCKHpMwVSJo3YI-yh9yQrbXsPfu4MJcwGoXo1hnahrvDv1-IA631mCxT80Hv0CpYRIE4RsZQD5q12P665IUkz-32QiOD0CWoL_ubeacqGMcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCe06zaK1WmMI7GVZEcDqGYruwJila6KU8mtQtLLnVPGLeumNXRBhs1fvl4HuuFBJuLaPMXA0X8faY3ApPhzCh3A52-2-4OuCjxgEBcvmuqMncOX7swvRikdSRFYuQNBiiZP3hwf4xZuzEYA7s2I4FUjU53lAb82F_CsOvc6vslKZ9L7PZ2l1NJ0hKTQHS3SodMD-4uHUemzxKXcm5nVGZ5BRsz5ADJU-2K9A-jHZs6hwD3ZLbeoap7gDfrX0FAwJ6sPLfAQfIUJ8LkZapFE3g1cO33QkEcsi8NU7KuEokIXMe3U-Ut0uq8eShO5k_5kmaR71_hZ6FV8j4-t0VZhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=bPbD0bU-TNpgX-UrETqTq1grdUSGx8jlJtqImmY0s_cG-y76_On86T7TblUZ2BMR97mm9MXurBa28ReUO5ZoGDjs_cRHyzD2XraTrCrOLhNWmekGghy2IKVkAbGQ6BJugUN-mckiZP1ZJX-xdzBpZM5GiS1n5pbJ-gluuQJM3bQc5dHBOnKFX1WFWPcS6XONhoVlCaS6XP4itiRs2hwgteFCxtNf_pZEwxYq0d3LOC34U0yPosBCFr2hQF0Wbyg_GK9UEqSgrW61BjU3Bl_m6xJ16eGcbaorgz-X6sE4r70HYzQIQlhIhq-FyUItLUDIIC5pVNyoHIsgP0SJ3nmP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=bPbD0bU-TNpgX-UrETqTq1grdUSGx8jlJtqImmY0s_cG-y76_On86T7TblUZ2BMR97mm9MXurBa28ReUO5ZoGDjs_cRHyzD2XraTrCrOLhNWmekGghy2IKVkAbGQ6BJugUN-mckiZP1ZJX-xdzBpZM5GiS1n5pbJ-gluuQJM3bQc5dHBOnKFX1WFWPcS6XONhoVlCaS6XP4itiRs2hwgteFCxtNf_pZEwxYq0d3LOC34U0yPosBCFr2hQF0Wbyg_GK9UEqSgrW61BjU3Bl_m6xJ16eGcbaorgz-X6sE4r70HYzQIQlhIhq-FyUItLUDIIC5pVNyoHIsgP0SJ3nmP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsEyewABPli3HXSare-myIcVqdLvwGe7wd2NDxIFE8fM5GhFUWxBdJxdhwf1BGDaCAjl5tLhC1xqg1kjvciOmcow9x6u8f64t5usSEdz8NH5hVUgzascKS3pXXSaPHMBAsyq9oZvMt4g_5sisc_1b2tOW--V05VpOKIBRdrTNvaZRkAqu1p8qF19FOx0-IzICDDJFeqs1itrN1LhA5lQfj740qJAGyJ4gjkCmt3-pI4M8Wxs0AC2ZX8ArfHQ-2wwSHRG_DtiX8ZW__0Uu4V11-y6qmsjhPTkWmqbsH_UzCB9RY-qJuCwCa36VbEkKQnqMyhLKeu_RTPvnTieSriZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
مواضع هاوکیش کوین وارش در نشست جکسون هول
مواضع هاوکیش کوین وارش در جکسون هول نشان داد اگر تورم با سرعت کافی به هدف ۲٪ نرسد، افزایش نرخ بهره همچنان روی میز است و فدرال رزرو لزوماً مسیر کاهش نرخ را ادامه نمی‌دهد.
بازار نیز این پیام را جدی گرفت؛ احتمال افزایش نرخ در سپتامبر از ۳۵٪ به ۵۶٪ رسید که می‌تواند به رشد بازده اوراق و دلار و افزایش فشار بر طلا و دارایی‌های پرریسک منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozcnk1cIB34uQKgwJukf1XhQQn4bKS7ObS32kh-RTkGW51jRlYoNAVZZ62WZB8DLHXKPKSOgggWiImlxJIUGqs1gF2wQJPQ3RzQbC4LK8VrIOXcfBVG9zYSDjmtzmh9ZzvTa9Y1N926f_kHUFq3q5BRurxDS-IMC4v3dz0Y-idpIyXcTJoDvdebv4Pl_lcCvY7gAlJvRCZt8MOk6NCnvRaWL8DPlrWr7-q5Vi-cFmKyRbNG-HJJNjmfh2w39zpE8xxK0riUKfQpY0wAEo9e5IGgoYIRwasevWbqpvPteOcZA3rk2F3IMe-dJvtHyHLzyXP_Rg1xQYpzhq1WBaoPZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoZPAzShwkdKTahh1pT7pA2dU00etTP5aftqrggm3fb96mYPZVX1BCWq0Ba_rGe09SVnsNbl_B8U7q7o-rsjoOONox3BlW8_KjvZUKt5hM3s_Ve0riWMFQ2uZ9eUy0AR2fLWrtj9MItkHByYZb5lmEo_NSkN8qfn1y6uSAV4ar1j7lEAFpiPiinrDdIBCI6q-723OobeIZQrk_ta2zDWZH-B87yHzN7xOLpMqd4B-8aHMptPkAJZF76TfT0kIz_J7naiGRJVGz9GrV7P33tlG6l7R1ZW62GSYe9nV2L4Py7BVm6pn50pUeWi2Pgkmn3tnhwub6D4Pq-v271r_oYbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4m3CRrWzx8GNYA8gZfEJxmfczrEbNZxxKKMnEtKYNKfKcO-a_ffK7FkLWz4MwC-tP_h82T_sPenkT18uR57xHvpzMgofR1GcPjqc9Ep5EE8umnUgtTtxedzlVSmRwfZFwdl23Ht-rItq2b76xmea2WPaXZXcorJeEAi-hqKyf0kE9JE2HJoLs1k7pZqw-DSgvzoKYuSqgNmQo6LAW_QOaqjM6Kipa4msxtII2oOW8wzEm2bHNbYoWpVQDVt_tlWuyRDSOW2qRO4EDda0m93Mvl-FxqQtR5fCy98rIR360jNzgEyCaKXhue4WxWfIfzhx_VSA6vi4JL2X76Jn6eznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbVhMg0MjIl8JlZegFgrsxU2oZ5G2r1YeHBRpIayzfM0jRlGLwOFn3ntbXaEC1zVrXWG5v9HW5fjb8ZYgDDCyXx0YN0SMURGAUEetVvHAsJbJe-wU4c4bzW94AJtl8yY45ZHBkwQzsYXdvMe3ZS8RebOHaqczg-WZX7ROhZq_K8IC6DdVi17yy79XWcnG-FtT738VWmgy9grEcLpFoIEdnjEaDi0nmWTn9ui3JR8y6UCZ8fhL2d5vaaSJvz8a--Ab3qa3s9lUyC6PBI3IXGArTgew4Yh-l4aWMyIx4aZZdwm9eXJEHAAVrvcSCDIuqrHDaA4wOi8MeSIIipKBCeG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyeBGv3V2oThBjnyzU5nTgUyVaDhJQtBfQba-_A_X7uc1keGXWAgeA5PUQLZVhoaG3eXMV-vw3DdItoM-1wkM9MUIghBvUcNS_BXXNktXo78Jbu6JLTzD6BUpezmjvFOOeT0pEwJ6QO3chqghlDzHxl9NtPjNrAflcirgTccMJYJwbgYR6zrbODZdsV0hoJDkWlbpfOlI-90sh_1xWISfGOWv0iIn_bYJ9RtPLiMIZDo8S-6DessBUoHPfy-3D7SAb2yX06SiCeAVm4hLNhJv4ZdMaLkL0V9wXMDTMRXnBGxXm4J8dQFU0FysdVEnOGPGmct0CChooRlncSyGAzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmJ0Zrs8Ve9QVhLqFe5XxAFYc27cWEOEf_zkuYtDMGH5GBzJms4d6xCEL_0KPQSY2jtWACYZ6U2_oEeKh6tI11Kn9VVHV5Mc3c58zN6fw3VROtwF9OblcVex8JhIfnXXyPKZQOcfEYXyHs2vHvySu_f1JQlPnbdEehh1N-QRsefQQUmv0ySZL5k8TokrDfmHpS64RNkS4gnBGUf3jev7SFrqhhApFEgh3K_XVlueNoXGiYAhfoD-uCuK1cwuNIPqG6pJvq_MVJy1hrU_zoeLUatQfwYmcHqdj0G1bCr91xnw0uToO2lOc3TRTRqNUGsMcZQK5dAqo_FTzem96sXKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9FqQtW2R2bQpu6_6HM7vDHUBteA7xxvdTcoSxXVoZef6l5xEYwcap5630WJf4F4M4z63JJu_3YJ9wZPk0C-dTlqyVnUZKVg-6GQSiApIUUbQljkwoAkk8BSpGcQGMwMcAcfl16bBRoL2PcP2vakUukXi5Tb_5L0zTUgTKq3dNBiJKuQIVb-AP0Ad_UGXoXFU2BvWEEYLpmhEHj1RXLJRMdpmwyrIYiiL1oGjkGsKeSE8rpjemAn7QK-jqoT9c3_nmwAZpu3JOUfvWN5p6BCwDBTmDYxBCViOhvhSrAJUgYGcMb-1Ff6Sh0TdWlgHRnZQASojJmO9vMBD9KqU4WH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAAFOUjgk-4HQs2Q6JvssZmlbvGXEClSdY10X8ldXdlitftKBsmVQ662MFnMhhwmjl-sdma0uOWkLS_7mViiXYNQjUyC4IBAoWMpl5MqJ8kOyWgBy9WEPmfc5922JnHn90-tNvCLCY5783qQgACk-pkgPM5tx4nF-ea8sZ-MdjHDBqFh5sFgXjOXnvkcInxes9il772pO369nd9sL7Qill5ZJ4EaE_kggIk1YUSHGXSfeWTE8lnG4j-FcEOgXd-bthy3hkMd3T04dNEF4WvJkwztTowbUTM_RsOpzyzdH87ZTIoibQ8TR5z19wN71s9Lw2_QjhYEefOg_QjHROwP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjthOBYy1lGbZXyoBVMulvihvExU3UMxejVkzPj3X0yAbsgRGxnL_f9TiXoAeseU7H_h9bJZIuEXhtJ3udRmvvlK_9KruazgCqd5uXq4Cn7T1crKf6--zz-568Rcg2odvL3zhBuMwHT1m7AHQCFp0vVLImvlsCOUtAAW1m4tsE-c1N2PN4nYnTZmamnx1gHhIpbfWjFHtiyPrOx7M8h_OE9-E0CgNxGkZsOm7qoRKRUb0Ls0GtUMMwMaH1vRndLbokcy78VGm9QtzDNGJRdTMPitulRPEYscFySNWmIP9E5aXws_H0-xA9WTHtfturrzKHZTb9x9utN9xWHUlWwsFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKVjv2dCijlPOBKoNYwOr-6V0BTYERixu3FJXfdSwqAZYdiEYzanrtWdqKjShEfv3FrG8-_glx5mjGYejd-Z9MfQMGjJqtoIASEJxFsSNjlTWsp7YLZ7RAer3os4jra7_lm7fEgFLA-HkiPkg2hOzS2IMT-rNev4b194i_ZypTItl04Hvuao9GhiHIMHAgIrREo46SAe_ojZlQ_l8srAPbaVLUFB_97A9U2fOfdeErOr62kWoxnuuToioNWyY2mh-X0lJcoh9Uixl8_1nXp70jJtEXF8nG-zQE11WrhqmSts48wU_N6D4y_ihbtS-82KFSKkeZxMe7uoqkZBogJT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slt-IHWU0QCib1rLZZUpaLBM3KsjRX6MZxPldY4bK1MvMZG8f5M7ZYPlAbmf0kJFluzlRnHToLR8KjGtTIQvk-7Tea7lalCX4M6LWLfi7xThljXSn2KL04_xrsPvGWqqWaajAZZXOKhfbWUedMPWtbzqOteUF0gKVgwHmYPJ-98fe2h8b-iaUPq23u-RhJrSztSTk4uAMcJ4EBfz6OiKuCZcSVwbZxlCerMWQRj6Stqot6Y4LoLlg3IOoN6YkCgkhfLq3UeYyROqdS0i4Qn5LtHkIzSUflPSwFoGTqzPTZYRmzO21THbXrJJbYZ21BxW9WJFPdi-o2hg0iQR6lUwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JATWyohnykGdBoJVHSFnySJCYhsv7Ievteg_HDH1gu-g-FJ6QH9EppUQRL6-Y1GvhSYvKFLQhIL39in9wu6qF94kcGOTJEf2lpj5YnWqrGp6vh5d7H0Nen_ycRb0dR5E9JbjbwwqBwfIUQuCcioSna_I0FBRQub8oQ847nP7TaFTifprXvj3SSj4TDt5Z6f5eVgRRhnA6fRI0o5bYaERd45KKxoz9uI5uqjHfPoOD8l06eLK4TEIZIHnjL3k76t99X6j6mwD8jp3kSyHtk83X9x88HJPEInNuIjA7tNURST5Xr85yrR-zN0kcTYwbonBUgZgEvMUIVUvloPwpmoQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvjMJH4l7HZU27eGr97JA-pp4hc0PA7LGG15cfBE8eVDInlRAT9bOD_EUynyt9qOO5jhXBnpgtgXHBxaVyL2maee_WHSwFPKfs-q4iMA4PEPxDnLl_VdX3z3Exv1kVXAshjcHByg_M0JO_5LQapUgcav9n7hD58AD9E8gLbi4GojvfrmrfMvXrzz2a6279lTrDHdBfBEEVpT20HVxd3y531wgj-Wt0hUcXujbi0zuDHktT5-m3HYG7DFfqa7rIEL_QqJLVvN0YFNmOegvTc1qRbGBJTYtojKPu09LKJXzN4TDbCk6C1s-Fqt6s2nTEFCOteBUF8XuiG_QG2GWGNmkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=t5ig117J8kE0QrmEG2eyZ90JGGWn3YtP44V2uNKDvZTivnj_UAu5rXDUxopZV_l3cmT9xqveTDHEJL6H3wQ0vP3IdTzUVYNomS93TT8n8FJLRtPvgw6H9lgWcejgQOIJEnbJfqg4BA6BV_VhP4kgwEgVyHbIii3pONV_rBLcKgDyT583ID5EJM7H-72HOliUMzFjpWktrjkRA0xprmLRphTPxynbpILpzgKF-m2etcZId1twjaWzlFIkTeGC5jUbOjcJgSEY6Yd-_-B7JnJs6DYo6vndKQmjBJKtrjyCpCFjxMFIJSRCIxMS2MsLfffnmRT1QLFXWjulV768JG-A1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=t5ig117J8kE0QrmEG2eyZ90JGGWn3YtP44V2uNKDvZTivnj_UAu5rXDUxopZV_l3cmT9xqveTDHEJL6H3wQ0vP3IdTzUVYNomS93TT8n8FJLRtPvgw6H9lgWcejgQOIJEnbJfqg4BA6BV_VhP4kgwEgVyHbIii3pONV_rBLcKgDyT583ID5EJM7H-72HOliUMzFjpWktrjkRA0xprmLRphTPxynbpILpzgKF-m2etcZId1twjaWzlFIkTeGC5jUbOjcJgSEY6Yd-_-B7JnJs6DYo6vndKQmjBJKtrjyCpCFjxMFIJSRCIxMS2MsLfffnmRT1QLFXWjulV768JG-A1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCiYBvgr4yjzSfp9OzMrEBT3xVZUDGA1stbf97_EvE3gQqCYURqEbAH2rrM9oksV0PmMhNgccB5eLwogJ3zbe8BUiJfBzL3PZaYPoR8zWy6NrXEthzK6MocgIeSHEDgWhHrJ9BXUdGKzfFscgJcmQGyiJL3pIuehr1gMWPRaEE_4PuNVIISAKFbw5j0HayydaXji57bq0e2uwScabSvYtPKzYe0MDbVlpfWhfmnaZrwJNqkcFKQjHVH7R_j9ivH-aC4j7NRH4dLenaUhey7oLX9AORvGl7rZgr9wbQOQdwbrHOxjJc750xmm4XKqtCizBLV8TBHFtfCOR3r5hmHRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7oU_dQ-TJ-RRAVgqnz62ioLGisBVUGIgSROlbBPugyMb7V8WL4vgB7T6Mu0lmzNSF7AX4Js3RpvK5OsevcHL9sifpYipKUKVou3ZvbukM_BxE-mQS6thVAZixwIswhKRStZbVdL0USUGLiOdCfl-It2l0GuDGaUIroHH2zg9d91HYvnZ0SRYu_VWcBwOddG8-BCpKKD78aZZ42PwZXD-hcIwH6jAc5fXMKjIBIZc1oxLXiG6c2M5oAziZVguMsmiPQ8xoQumNXOhxQsZ53M9XTpvLPW33UYQXhyVlTWhB9SVwQ-uucd4AFhbzjkDop9V5tpiqzI9U7QDMU3sXRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_W1GdFYO5KZg8B8CoyF9gQeq80xBOtRbYhJ3M3G3_JRy7DzjqiWG6oKbCyZC7XFzY_zp--RJWQf1rkEiuDM4Q7rO4PzTQT2G0ayhdo0VwgIaiXKLAsPigyCuNrbxVHJKBAlCNSxgXLjFdG9d7BbztPShFV1Hh-sk-vVAlOhjlfW6RMgJdyI1Zd1TvXCAoG00FIFPD4Rn2MTBylpk8w5b2x1-UnEZrX-ae7423LHzq9E_lrzweHvgEKVS7o5iPb8q4ozqmj9jbN11lON7BNOwTfAK4sd7-nWOl5DlJVxIcWQO43GAsJWLMUaM4a4igpd1mKwukMp_BuLpQxSYjeGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uPsE3qucMNdT0ro3yK4ibORaJHAsaTuu8pGbUwN-xC865U1fcnPAjFDDcZIIU6c34Hc6awlZrJIeIrA7VbPpX8yjx0QeO3-WTQ841GECGHMJxBHZAx2YXSmr4TPVMYKuX8kkSfEt7zRIMiLtwwTZD4yfE5Q6Dj2Mm5kzbCNgxntaHF30iwofrF0VF6RhF5f3KlQD3j_u0lhi9rKG4_ucd0Nfd_5BKI84uRTnnFhAIA5SPkgG45zgnHe3sr49cGcjCIh6OBA_Q768DpbeenkRunpx77-DuDzsGbnd3w0oJSWUIddma9inq9dT8-LeTQS6Haak45QmKPVbOrMFBr51XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uPsE3qucMNdT0ro3yK4ibORaJHAsaTuu8pGbUwN-xC865U1fcnPAjFDDcZIIU6c34Hc6awlZrJIeIrA7VbPpX8yjx0QeO3-WTQ841GECGHMJxBHZAx2YXSmr4TPVMYKuX8kkSfEt7zRIMiLtwwTZD4yfE5Q6Dj2Mm5kzbCNgxntaHF30iwofrF0VF6RhF5f3KlQD3j_u0lhi9rKG4_ucd0Nfd_5BKI84uRTnnFhAIA5SPkgG45zgnHe3sr49cGcjCIh6OBA_Q768DpbeenkRunpx77-DuDzsGbnd3w0oJSWUIddma9inq9dT8-LeTQS6Haak45QmKPVbOrMFBr51XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYSn705BAVl8GVwsJWxJa-KYMHUo62Bq2eL1TgopDSnKyYf3NUUAmQ_CtTl5bxUnuHFV6B1mQVmm2Fr3gEbBsHjV3axv-R7lOVw8XYjYoBO10HpUjqlDXX6efQuXzcikaosiEdx2dpuxrGY6PvSgz67qM5S9wvsOEcvkqSh_yayFmm4mn_MWafgT7hRGchViBU2n5FbUqk8KVJohIbVeIoKkk0xFRc0XPif92J56G79C3HGRidjvVdbAtVAmJx73YHxBjigqGEGc4AlDUOTx2L4koiSV7jUbuhb9kF7eVaUszjeEPBoyQnlovYkSlmxQAGaHUVzS53-VbvWKYli1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJbuq51IUHCV0TbTG6lOgyWBfA_FSUFtL6OBKhKyUhS7BDdZtRBPutKJhdgJxYLy-EFn75Cpds617feq3tE3DUAbtYgsaitjXFW2AnpYOTNYOZJlUewBmrw01lWKH5lwW30GJn4h_2z3tLQ4bzADETTfdywwkKrzae2kCU-R4UIeojRL-Eyt_KDp769FqIWHtTkCwSEXhqBJnWOqEFUuqdwwAw9EEF1tgJJLot7_IXEoyL6GgsDYOi8BvbAlicoYfh1HRbSCiXOPjfnKVvz7Z4buGtw5ez7ND6czgjkCqAQu3fO0pmtJnwgthbfejtrDXvhTIT7oFU0pfXYl5-gBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZXKcDVQqbwQPxkTCqBD4BWd1rQPo4zBrebQX2ECDzd1ASK7aRCnOEHcSyClibPM-HAhbqtl-qWLL_alRqA8xihtkfHIM87p35RPeepR0X_xjw6rKCIzVAv5tHx1TvUiwJUZqWLhUplspPkj5TTVcQFQ_stqqw07bpVSxMvIRABaXdXx4L08eWnEpwEvue8foaUsqFL2XSXzCV0k-_FeGeXQXqpxzCipIm8Z2N10Pj4xxvvup8diXyk6wIypDettCA-sM2djXOTGlwNwBANi7QBAhaRinB4HWEaPv8Ut-rinu3tRXZ2H-HXEqlC1adLd-UEKG4njJnncUSEcSKeOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYLloYwLg1sltVotIQjis5VeVrB7bv_evsRG0Pre23cyXkXKL55QtRRR9Wpr7pQLTW-UQ0PCYPkZJzfofwH-kjITkND4mU7Pwrrgs2zYZAxjXD0-cCSX1HEjHeVU7L4RaYJotvsEUpkZ7-2Ap3r_95k7loFZCmOmDCZqavmPVP2n27KUwNOuBBLKmx3o8rRbcCpt6IQup0exmmcbpBTEBXbvddTKy5sFc7yl2m0XZaCzFdl3nlQic4yZDMBrNgUsVyN2823qpLyztaBdEOHwFbxVIZYtYetkaCxlgROTGdbUyfX2KBY5LEqCkOb6DDSX_qvIjegJkMr1UGGg6y0mGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPJq8PoLFmlynw7GBAbBtVN_VDWtsQDnqnTkMNyomMhTatKISQRJxOk4HhQqIDpO1mgWKLwu2mvthskx1iOyA6Az6uUCzCT6AHyjdlvUvjyTRDqboBHHPai5B_Q2FegunuGpljFh60gwLpOOH-xvk7EvMrMwWx557yvT67K6La2Qa4MFQZ6FRVMCtKOreEMf7wK3GUlqOSEtVJ5--mLUnxzhuMGG49yOJ_oG9K1J5HIgYp-HK4JWmSDlARYSk9Y1-QE-BBHBHwFw2K3nvi1lg6atxDV0gK3MXpasC6CM52L9r9iGWE9QOOb8Uw4kUQh2j_UjsL_uc9RMMPiRdiCg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW0uGtUV0dKigWOuGhmEGGuJEAk7sw5tDOPrJ8lUDwKuggDcBwZ9Kp3DA2VllVpHm51NLgqcVJVeXB0M2hQ5fH2zkcT9qDPGwkuB4FfNWq4iVgf-vOYVZSh6tvNt7dLSkBgA0R6r92Z82gYbTRdVg74IZL5P8sfC41muvR7qQBrjkVU6MbmWRu4lCtThRTjGrefuyD3C302Di-WDyH8h7Cfq1G613BmWn5k_79VcLNLzNHrEI4rM2YU4T1wglGxsYmG3w6SpbFF_4Vz_e55czImhKnAbXK0plN6NFvK5waKy2g_2b3oCb9MbBbRxEhdr_ZdoZiFzg_ePY2kQbuJOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRPTai9IZKfRWqjEFoEvxaeUdzREkg8PoZoqQo7YBSac1YwlWM2k6BrJ5yVek6WHZpyaU_PQkBnoMGsYXclORNpTxZ7A5Avp0vS33Or_1SYbKM2hBHaPgRFoVYL8SeNUr9pWJumuBw1YOyneCUvPDyc6PW3VVIw6Xw2jkHt-B3IXiq91Z-3KhgNBJAgtxo_kgvg2q1r7hIP7MPCuPx5g5hEtyFCpfSc3PR-EyRZHmlW4wmlJqrxsBVMDl9rEP8lNuQYV3G1LmzeNlPgtrILUjaKwQnFpwtpaqqonz-4eID6gODi7KPtwW2b82Q_ZULTf0I0RP9cl_KkWwyHmiatJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
