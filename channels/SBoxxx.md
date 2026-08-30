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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/20320" target="_blank">📅 15:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOmbX6Iqd8Qz73l0lk0UuNIrvKdpBwkyaacihwR0MJ7v-Z2QOxBP8JM80Xu-J724VVnlSfQbbZ2zspegw5zFkjd_qlV3hQMX_OUPyFMS6PAQshV6ALP77udUR2Hnf3--oNxBxuNTVtdo5G2XHMAxrT4_uTgvbGvQMaUUiWxMm66vgCuvdleGiW59Z5Udnd9ZHb1gM8euNBWFKYuHLqT950zhqWkSKOqJ2wF55-2P-Dmwmig5lDmYohzyy0qfq5jZJO1yHO6zOUC7sIifLqL8zQINFoIu--FyfjkXcgy_K7UbcXuvFB0TNrgGOPSAMfxoWLDM8Ty_fZ-GfAv79loocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClDkdBG5tz9HgGHocur5ki9O-q2vvdjOxp_uYLWhAALPuWLDUI5tG0RoRnHZknhRdW0hyLy6IXrq-4NqAe0CLue5PB_YkOU2kHQ8Wo8v9mjq7vG8k3af2bEPlvHOcZuQN90QXmZ2nWLwqbx3CTEpbXaDsm8nvNleQfTO7X4nFuRqn_k-wnJmgpuiBUjZ6ArcFucIA3wGnSlRONd9crkVKHHgf4EXsa2zAl8T8S1dpDNdISymUHpMQUW0Eh9mEOuw08A9hn8195E__VzpDXYQzRnFP93pUPgPYhEiMDkxuGnwYyBAgSb4CMoxhqnlFuK699RPchXMnYrkL7uU3gqynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBXP14-j5tGD5fJcWP_syTAeI1Hb1VqN7YcQRKl4cQlWzTwaCHIMBYa-CYewgVKb_CKlKF78sq_FuBkG2UWjXmmYak23jADZWbX6l6MOHhbNszYw_GkCG76s2RQKFVfWjJu-JzjmhJy9-Io8INtYeGpKzcbDo3RwmZm_VNWj00tKCL-fejbbqhqxWLdmd4ohJcYpQuVYBS0U3fp8VEcmKjnX0LmTvizRdoP3RANgClj35fmah2P23KaScRU6UuVRNF83wnBofnrOBJvo2JGN8gAIsVT3y6V87G9xG_4PtsC1PYARpuZP_0uWXtvbnKFmbW__JBRPD4FBV-JcvyE_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o74klLHGquZi5ceDaUABKter_BHIvF9A3vl8SFT8zmhn6CqWImSRULXvovu6OhpnPHpxnrP54JiaXntlFhTrYmOQlgx1-FY7PSehzRFuoXph_-D9YwSBISrm3DgZLQlF4wX9TtCAhdlZ88d7bRynHlPrbHPq6vLNvDNh5131-tlRwiC3NSnUE-_fDf1OUqfkgrOeUFh_qssUlQJ0WRQzy97My8--hdiMNpEdbWdfq-UZ8Gg4wruGq_9A8aLIuop_37ylbHTXbMwIbvmb9nIn3VBjQqAJDqSSWyG2VYKb5302Msg9fsefwpJQTykXnRsFyDgKNS302BA_1V1W7dCo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjgaL6yLPThpGLPjAgzJfP58f4UTJA3m6Acu1uW0KdnunoKTTwf0TeL-gD3lFPjH7QI2QZfYu_CogfXLFrWuRlwoUAnb7_hduWcUV7eokG2oOzq-Q35EBvAXIxv-bS08AQW-ASvNVn_cKnf1KgJiBUp7yDyphlrL3U8ALidW4DKn1cYbs5MVS9kgN0Diic488J2xBB4_qwF1_kz0_gi946_YV0HDwdoWuC1twpGcbhpX5dxddX_ZyHwpVatIPYySZkVz5_fHifR7PzU7YKHRnKXP3mx6d7EIH0EAFruzwHeEXRsJvbESJ6Io3Ti7Tc8yN1FMSLKr5GcxD9WcxU6h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzjCEri8QY_zalAC0x8xU4zSA3iFPiH7CV9Taqiu-0SXZBizRVk37d_0sRmPWWRjjGeVKylnoKiCWfFd-oS2No1ayfhWjzjnyIlgsZEAqsKZb4cio-A3Bn5lgI4udftGscN8V9-wW6-UgrSzcBkAkKERuJU8XhUEIvPXX2mZdPuzj7bOVjiU5Hk1X_UeXV5XnsWJ1NFQ7dYjuNLoC9_5tlJ3by4ZfPhBysGxr1WNYJZaWZcaTq90fJK3HMxKzC_KLEeci0mtnDyIsR8g2lhurbNGSvGnO7na-iTSV37nRRhOxSlARuXy_FArROEm3kC-XTHrastpkXYJbqCyv_myIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=fz8Ws_PMghuzz568eOXrhQGB-y2NP3hEDZLGOVRlKXnD3NJf2Zgf4mkDYv6PFm9XsHJ8u_XWi71Med0Cjt-HKzHI7F8EztbtNDNshNoYGueReqUYM3zA3ea-LWfgAKxKkHVAZUOyVv4DnwY0_yhdBek-5wGOvPVH2X2dku7pmmVz8dzbJsJnbEdSMdBdmsx7-5pqooBB_AqCLI-NDb41IP6U3DKmnMg846liEEA6nsy8GmvQ7xr7Uyxl8VuzsGDmJr_AOwanBy_A6LR06V33ksVaUH0BlgrNPhfu6xFj9nacqTnSKpXJdhsFGy2rurdkJe5b1NO5wkcn64BuSMA1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=fz8Ws_PMghuzz568eOXrhQGB-y2NP3hEDZLGOVRlKXnD3NJf2Zgf4mkDYv6PFm9XsHJ8u_XWi71Med0Cjt-HKzHI7F8EztbtNDNshNoYGueReqUYM3zA3ea-LWfgAKxKkHVAZUOyVv4DnwY0_yhdBek-5wGOvPVH2X2dku7pmmVz8dzbJsJnbEdSMdBdmsx7-5pqooBB_AqCLI-NDb41IP6U3DKmnMg846liEEA6nsy8GmvQ7xr7Uyxl8VuzsGDmJr_AOwanBy_A6LR06V33ksVaUH0BlgrNPhfu6xFj9nacqTnSKpXJdhsFGy2rurdkJe5b1NO5wkcn64BuSMA1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYmIWA1j1n6zF1X-VA7GwDR4q3M23Fl0fgZUqTbYiFMOrTdEQsvKYhtdhTxZoiDhPNup7IFYr_vffVA_PYDfSIut5olhRvEqDGt5tC51mcY1CyEB_p5NeLHuhq9lmNt4xh4q_MPuBUB1vBe2AEVQZnpYYY0Ue_bfL3iWSNMO2fuS36UkXHZELWKqWcui_lRffGfePtU0pHjd79rzQbR4P3fQn7-qeSYkxWY1leRCb5O3p189PQZdSAgOfvx_wcZtfgku3Hd-TeQ5P16S469SSkcydWqSnvusPGcWFZ0YFvKZxbXoMcnrTlx78CdBoGK3I8VZgazoEceIl_Fk8YsRUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBLxiNhLHfY9oiLegdYT-SUbin-0sbkg7BTEIQNS-fS-ayRWwuY2stpFt2vEm4ksnHcRqEQXGwVkLcfWEb7UehfoyBmDPzelmm23UFi1Lbt3ZEEwqoJLatZwgyyJQMd6oSmtXbK8mQ7Wiagu_yN7dughcK9H0GUcqG7eCovgN24RfJy2ddEFZt-Yj__dSZJrA-lgTBKGJbf0trLE5tHo2Ak_R4_atV8Cql98hJQA6gcADHB595JwCudnQy40y43LigGB5UGD0ri07VczDJ8EdIKT_jbPnGgG80DAxdM7tSjDKpRMkYNQBxWZYGStmHlO-EH9SeJC5KT1a_0QYtzXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoZPAzShwkdKTahh1pT7pA2dU00etTP5aftqrggm3fb96mYPZVX1BCWq0Ba_rGe09SVnsNbl_B8U7q7o-rsjoOONox3BlW8_KjvZUKt5hM3s_Ve0riWMFQ2uZ9eUy0AR2fLWrtj9MItkHByYZb5lmEo_NSkN8qfn1y6uSAV4ar1j7lEAFpiPiinrDdIBCI6q-723OobeIZQrk_ta2zDWZH-B87yHzN7xOLpMqd4B-8aHMptPkAJZF76TfT0kIz_J7naiGRJVGz9GrV7P33tlG6l7R1ZW62GSYe9nV2L4Py7BVm6pn50pUeWi2Pgkmn3tnhwub6D4Pq-v271r_oYbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4m3CRrWzx8GNYA8gZfEJxmfczrEbNZxxKKMnEtKYNKfKcO-a_ffK7FkLWz4MwC-tP_h82T_sPenkT18uR57xHvpzMgofR1GcPjqc9Ep5EE8umnUgtTtxedzlVSmRwfZFwdl23Ht-rItq2b76xmea2WPaXZXcorJeEAi-hqKyf0kE9JE2HJoLs1k7pZqw-DSgvzoKYuSqgNmQo6LAW_QOaqjM6Kipa4msxtII2oOW8wzEm2bHNbYoWpVQDVt_tlWuyRDSOW2qRO4EDda0m93Mvl-FxqQtR5fCy98rIR360jNzgEyCaKXhue4WxWfIfzhx_VSA6vi4JL2X76Jn6eznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWEiUqLAY851nK7ziERlqdqxCp6VPJUFLJAzPV9IcSSKCpo1E37lQAJO91vW_RUKsGkgDmkuo57Bm3SfTlSRrk4HKTaOG1itzzZZhnyoQxaZ_bdmL-ftAKHLUyxOOhxPK58wT8pkDrupwW2IV-Da0AgU0Vhn5faa3xcNOd4hUltU7m66NLfrnEzM7Gs6PmfBRYhM9XCAavG2JuqW-WqR4mVyknlWb1M-LOKkmPkvybFbeb__bwRQfA7r3_sd2un8dPaBuBgxWmXp64Av2vtubdUZpFjbWm9P1GsAsoEa8FyDQQQme7aivJIytFuNtOj4GFCO7h68mIMmlVEUPtuIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO5to1cqpLt8th2ikTQZpQEwiEal6PmTG46EKxiUsIgWeTmrAsvQSCUbIcnpXyHAI5_rn2VMuhC3B66lW11Di1iDC47a7UCWMnymTNNC3EwaL7HZkqRwZb96EOJ2Qb3RJC9U5Ik9XWryz0LSoRd1vZVj0zlSYnOSJ3X3rkOEQQhq4g0fx_38I5z_zcHYdrRVImgCW4SFu5qZ-dAQ9s1W8BUi3fu89Of5vaPj6EXu6RhEyy29AMNf1NVadan7rOEtuZqmViiSQunAzwXhzcqb_5vhv2ZCN9sTdVbScfFxeXCy2Y-dRt0WSdea4FsB-kAWu5uXSXEgbwmkp9zlN8ornQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8z19nr00TLrVEt9sYDsPhvYbu0UbE0tPaHr7hoSA7lm3MNIl6_MHOHSweis2UeqkRF8UPc5-H9CbtMgY9pMEJZ5Dg32wCs6b70T2R3sYG03HZyyu37suO8C3H_O9cQfRLQUdrPKjurBjQQUK31jus-nuw_3tNbg7YqsuT1vPpjgpnpQd0g1aL23ZhaS9R01zcVsqlqK56wGZibo7hp7ytXpXXq5dSPw8U2n8pGG8xVEwl0QBpqrp5EQQH9Yfe0Wp_iX3kAsjsDjXWCwc6owTj8Fxbs2CjJRPyW6FVcfisfkEwT9sqwMQhNrYNWztUO7ubbpKN9E3A53rfITYS0FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puaOsF-iT1Qo-ZakGV-XDGitZGjyTGt8fkYu0va_xKmOCM9DbwJ3YmTzF5oxbx68obwYkhpOWbCBeQTMGocyOeLFjj2yd4y-dCwWITe386gbRw5fPlHQIac8_C-ljzT8oaA9N7NBn52AP4YPz6qE_cGA2ymvpFuO0fJFPBMs6Uhww__keps2HXeh76ySHL_3wqLgwt9fxeuSRo5hR_rLX6yKPNU_DNqoi25ayaKAzbgLbBMXPgGFWChBYDzN5HLKDtBYU33I0oxxBREAe1ted2ES6z6rBkVhwuJMng9BimG4wbaPK6s31k6dyDDRC9KyrrhcLINBHo3BNWMRM1Qitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqAKni5c5KBIgYplXKvwCoB-X5gk9_skj6-QGYHdgHXbI86X4_X8RiBWq6-3N5VeV0wPhvF5qHCDQLeKcYe4kzvO9xnHJJs3vRGiWiznULL5lP_otv3gZ91oy-fwYetlcGlUKiWBaAwpJG1YT_-L6XNjnYFunaeoQYF6yvIWEwvKq7lJ_YuF07hq-OqShHiB5K2Tu9rAoGsKwFUsN6s6OBzgrE9Y33_vN2-NcGOeu6ecsUmBY2QjeLQGI4_Leoju6E2TO8x8HZwCw1Tvj65F6sXfr-940D0k4nkzVOd6YUW_KllHMwccY205oUsbwfRpKTvT9OxTVRnde2v1umLf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Naz7owRD97HpZAUjCqWB6YNgWXUKlTzme81Gk2xomYWLL0mqibX6ZmT7hnXDbMDmDS4_2Cz8AjIu369SGZklTj22ehYk0we2sNIFuPewrNIkWPmiYE18q9b5KiTspG80XLFpPGJGTNQJ-1gWAZyNcp9KIGqA49KxnaT2QmRYJZNXIKEM9wFRCN8qYQZmu8odeEPMef1CLoXnWuHl7JcaoF4FwOcHT4UqdlqccksLcaJ4b_qw40vwJ78-dIiSxY1UO62NP3IoYQu_fEv6qeWsqp8at9KRf6v6XfQ63V6yqWJAGJIoclOVVcovu91VHR2lCNDN4Xad3PQWyR9viAvdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQwlz1mKKpYEIvhwh1YxH4Mkbp5AnFGwYVJa7gKfuY5Wxq-a4DZOda1N2XmTYERojnGuizyLY2Zt3dfonU9ugQ2C7__ybTnT9gUR8HQNgrni2mxCOhEUwRHjIKSwYZUy9eLK-5dBVePnjeSUZtFuPZ-dZYcrxnvfBrjRnzRDQxCu6G5pujSNCJLu8uiEUC6PImznDEUAM7nzLCiftnxcs0-WTuW5gmwPixu_5hBAwIjZwY9qdHeAwBD1S0pCLAESDsxZP8SwHQN8lekjRRQW-NTt5UhF0ojQYfLMKbGAjZzs7WO56KcV4oYamEAiadwS6K_zPhkYBTCbdPBBKMzNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1PXkpn9TPl7psuIW8MaZKyUqpZHcqWkUXJ0zu4YWiujeGw3xg1u6TJImQKTtJPey9kZs-A904qntweILbK_9x89Ozdgr2YqGLuaD5N30AYzRlTo8eP6poTEuA5hJHErtK0jpMOWFcWk3gunSjJBq5MkC9Wo-Aq6JYyp33L3yaydQETpN6JmXyCZqpc7hgdlthF1KdEXBl0pFC5zDl-fk0lxpASkPeaWA0ewhEyWxWEhaZOPZwqKs_TeNK8qLenYGwE09YMRbznRg0pDeb7ZOhpI6NoqQQOIbJLmcPG4Pz-IPpzdZBvobnwCBrbqhBV4WpIXbcBhKr_JrH6wKdJPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTsD6OULpiai7PqxKOtWP6ap_kZuyLy_1Fwj_IDA-uxWRtUPOlpYARqUlsBKZ6zsCbgSToUZi8M5Th9ISTngShN3RYf2V7MDJ_quAa6-E7Q0fNcGjZtHBOVOlnkuGI9LIVgcXrebGWiS-Tg6bvRqllW9kfStyYOxku4ygK3_rYAVx5uDXjJaEEUxumOXrQQOgjHv0Q3VU8qFX1PZrYhHH52bj0Agk04VGMCORtCWOqdZSuHR1GqK37oHokGdTJYYOSO3RCzSCqZNKC9x6cgc0TbapvHLgUbz7z7ijl9LZKaNb5prcD5tg2t77dQf77SS4CRLjlRQAh8TVQJmwoZJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvIUyhkAuq-Mi_SCKB8thHRuy2YSfSao_YRpAvljeyUTyJtEvQB1-mAkh5rLYQypREmh4bkhucepjaoUVCoXFSMdHnnbzayXCfXIp23-ZuwAaBdzEu1LYyxDMU_MAG4KiCIkXGJJ94ePzHYp1az7TZUYByiQvHkpQNnZxy2HBt4oCTxehACgVpw10hbhfBuMkOk47-j907nJ-aLzT_peTO1rY120PXT-WctUkq8xKprNzPbbWCDyCEL0PJQEyzdD_ZHJvALZUGNCjgjqoKCOCDis3LBWhEODk9C3A5hrdTswb66JNNLijleSKkiZ9Mo9dkcd0FCqbjpnBZaeXooJJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Xnfk5CJDquH_TZgqUbgaAIS0OCVUQNQ0kbiBgWgzJu2DRyOx19dgSw8VfmNvJwxCei0J4H8gQxEHtV4etwpajuDHvqcdAvIyx1zBLKfdblkAX5BxXAxrW_RkTzBXzEAk1gPEL4WwGpwwy-E2_8ZBaIddJDEp1aVfNspobGTuWJUzbYOirEAXZvUSI21phBqsOOBBhpXA6P84ub1JU9-6eAbCmmBwsp_y6Y_D5DwTgaH8gfDV2kwsYneBiTVUPWKT3GQByLLPnU1nMRPgc97Yt_8RJlrsaWLk07aQF-_jNppG-4gzW80XkFB6GFbSwp9yETDCvfPnHs7-HK3fQ99ZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Xnfk5CJDquH_TZgqUbgaAIS0OCVUQNQ0kbiBgWgzJu2DRyOx19dgSw8VfmNvJwxCei0J4H8gQxEHtV4etwpajuDHvqcdAvIyx1zBLKfdblkAX5BxXAxrW_RkTzBXzEAk1gPEL4WwGpwwy-E2_8ZBaIddJDEp1aVfNspobGTuWJUzbYOirEAXZvUSI21phBqsOOBBhpXA6P84ub1JU9-6eAbCmmBwsp_y6Y_D5DwTgaH8gfDV2kwsYneBiTVUPWKT3GQByLLPnU1nMRPgc97Yt_8RJlrsaWLk07aQF-_jNppG-4gzW80XkFB6GFbSwp9yETDCvfPnHs7-HK3fQ99ZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U91mywFIzSXvcqnA1XOfNgesie0OSo6PldnU4mRMT1avwGjPEGXQLv0FrFXP5VZvKUqFOK8tJvHjZGOcfiOSq92RGJdmGwypLfzMQeFT_U6MRd0on_qDQaQhEjKNiUTKlbosa7_06dp-gZHv5foquYd3KrDiKsVkDfNgvr0oVD8XN8iXsj4sozhNkDMtXonAbULA6dDdBXRN4YBoP1dyFWpUrnEMCvXbFVuRppJ2f0Y4lDVDWBEGQE11Gs8kaeONoTzGzgyoVZvnvJxYzLyvO77bFuIpcGeRArE9AMveOgfo6qvIJAHinMkzWwVZM21z-95J3zXckU9DwrtMSVVVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGJyHVmmhnhTaHffDsoB1vQFmWSZ9SdO8jm5DL6NJV44ZOlVmoJvgg-n89axAt9igi4nn87QxLE2LZ2ejAgPu87m9xyscOhkXpyQysAgZ2wKjgIAGip1YsnCXpGn0sg9oDc9hJ-cRlikr3Fn0Mh86y2cdz63UuuOyIVMjmCLLZnf5cWNwI8-G8l5_JHQWtb-QLL4tgemcJcnC8XzEPnVIs1ddqh3yajThBiTlLYpMcCpZhx4XpA5xd0VSIBeA33bIBiDUHVM8mrIMtfl7-Tx0czYkTC4tWMj9DbrCaa2rBYKaJf7G7RqvNlmBqpfngsb_voJROzfb-yhqewYqrIGRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNfGTW0weHJX2sM_5Qv1cAR2LDbPW2u9h-JFEQVmzByJUcJa-m5tXNTnNIVtwMOTGa-1qVN9G0MpVCMJWd2zbHzDv2meoGzGnNHeSwaY2VrEJPIQLc8goVbAwSpg28HQknPwlmSyH-beV25Hbm19Ids4IQ6PHIR2XxjflanV56xKnfPSX267AsfFJgeIb4nvOcr4nUU1YnpE00Vz69QuENg1GaTHycdR0kDaYEwL5vz5BGNJsDOV8-ODwgCMtmXa2jD1FhOW-oUJ9mU3eSIOiJEB7KsnamqLH0ytob_YRP2L0QUOL3x4SnrsVCiXX5qyq1ZChiTKIsVA__DOZPj_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=pQ-xZZ0OYw9N1Bxwqxyve9wBWD2jSP0mv-d2_fjRFG098eDdGX1y3vUDoNj--C5-Bv3yci-dNeb7GH3sORpwks9EPFgTagLR9PzceEIg_OL1MAiVA2CBdBtITOVo0IscOAODN_YOcVpjxr8-s9kxV7XDtll5o2RLsacXlSFDdyswPqPWapMAQf9Ac2cVKNnQdAog5_ohW6trx4pdWlu-irRlvHt1aYg594-YLfEH6KmYcvP_2unLFsxZcttPE92QQulZR-dINhn50hIuBL1jc4UujmCuXSoEhJzx3uRswrFu0DgxUcat_hy9huyeQdN2NryeRn3HFyFzL8vUwgasiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=pQ-xZZ0OYw9N1Bxwqxyve9wBWD2jSP0mv-d2_fjRFG098eDdGX1y3vUDoNj--C5-Bv3yci-dNeb7GH3sORpwks9EPFgTagLR9PzceEIg_OL1MAiVA2CBdBtITOVo0IscOAODN_YOcVpjxr8-s9kxV7XDtll5o2RLsacXlSFDdyswPqPWapMAQf9Ac2cVKNnQdAog5_ohW6trx4pdWlu-irRlvHt1aYg594-YLfEH6KmYcvP_2unLFsxZcttPE92QQulZR-dINhn50hIuBL1jc4UujmCuXSoEhJzx3uRswrFu0DgxUcat_hy9huyeQdN2NryeRn3HFyFzL8vUwgasiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6xXDOpqE_uL6jiwcyiCSelLQq5yEW_xBjkV3EYPKglHuWu2zgK6RlciE73oZAqlUlZ6oUdXwmC0kGzeyshOG9MTsQYeTbLAtJDqGoF2sOTs0QtHFgQl5axAF8QeeytQ7mKNw2xOyvLymF24vd4hmF6jmavoesl6qGEq4XH-M_I1BApm9ESp7-5Ji_g1cHF_X3ORYtTnY3YnXNIzd6epzTqKqfDeuMNBStUEO2IFYn9-a3IL9XBwnlfdVpprHfH5WyEZLXJ5U3Od5gTLR9Zg4TAkdZJMD_71y8tdztqQ07ryN9J3tCOO2lduiSQPwQ_NAek5LdPwQcgo8ekraBIA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeSOBtna7vHqejJUyVGlW_RXEKqOA9PdR9vkSKXRrSKJM6JCXWTNl9NUjwhsVP28Qmou7JLuWuT5e3XPK8JGydq4hKAC49OvCnCdsXWFdFBNcDe6z7XnJtfmwAxXtlNflXknTHr-hotynoFSfO-FguMQNFm-p9XhCXtDMVHdl-HKv2ZsmyOx0cXg-JBJA7bJilPbSBjZj6G1m5SE_fp2be2n_RIIuEl3o2n6J_51XVyU14hHgX1LyZ-M_cGOKnsQ5SgjOSXKgJpB4mPttXwTW7KrMuSvkzm5NsaliSwcytVVvxb_U13rmlM4vp9lXW3vZmQYZsttbBqPD6_dCAwgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_OoO3CM5qurmsQ5QyuWS6_S8gi_lMh253Jc5LRjQdzshm_RCki1dI7iOn9TBhsAlJBbHQ52H1niC8udfPl1MKPeByuB9kcw-p8RAbVinrU30Q69fYmNEtbKieCW0aVXfQqQesYpb7526TzzTZsE8IyByY1G6dpoeFuNWMW99uLobxJQtxcCn7jBxcff661ognJ2AJh9sBE76Nkr4cJoUvkrY3PHfiIIBF2UtHu0shTK51PGiwuu3aezI_79zUspMVsZpdsL94u1w5IEDzDH8p5zepOlR4_K1JuX6BbxD0O1v7WAgubQkbyQWns4O9IiyNKldF_Vvrql8yfNev_AGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQUNv3Fd7mwSwiaouR5OK_Tb1aL2ZyjdjxLc6-U57oiBXNvk8I437n90g-mNUAwu8abPLclLqcJSU2YXzKCz6PYs6Qd5P8WRgvwzvJrgOvQRftwek8PJSMjs5lBVIqhFY8OS_gk50tCYfGXim24RwAF4bBv3LqHrLxKpGTv6TjVpICKAZurVuFv-uReph-P78miM6e7YOTVGk-a_4IgFn0a0-I9epeofVaspbT32Edugtapu7fM3EcwuQYXW-H6RLYWgKka1pZ3OG6Im-jhTo6Dq0_A--d-_7c9nThtt9gv7pwLXWcSUuAYCKp0t4DX4q6Nsd4GRBhhlHU9sMWoW0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrXK96oHk4OaOOd77Jyn00t0yOobX-RuBaFhzogQzSfy1qhiWsAM3W7h17y7nlMDz4C6GJyNNqqo3oSUFgIPxWzuhqpvh1OyARImIG49ezzn2YuLxO143FVYTKYMoEg6IqvOJi0uCjjZvRoqEMV2g61S5gTDHrbWZGC2jajLL8im40wf3Zi2ZrV-iHvc4LxXDCX5Z7jVQ0e4bYXA3K1rvQUWN6h9TC-sY9bLp0ZUkTqg37rwmdVK05MEGJb2LZYE1OMd3fAAdkBJ9FotPflYWypR3wuUYt27yd7GSBr9Sp5ohBqZ9GdYG4MjsHFnG1pZ4D_kobAjctoy2Adb6KFzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wgo751qhOAtvWdYrknI3Q2O5ibDGP30pmErn8ImIePeFCxxhwxi_f2uVVm32RdwuZRsaX-9gK_8VDUVCmPVf0nGH6_-fSF0MrmKi-5BAP0uJ1u1JUFsYVeL0a4_V7qHjgkWITvpm8zLVvZrlcMYQKF21ijlooBcKEtukYgLSJNp-bTYCEmlkjdZSJlz8nCXkE_m6mJd_EBK_SAI9B7MtY9tONtBnTdaZpqJNOjc8Rzq5WM1yZSZj_63_o-d8YujkhyC9geF1h5W-2hki1ZJ0yMwBV2_Qk7B4GJf7N0jtnIHVLH2bsj3SRepAhjES8Xq826dIl3tBVV-WbxbTUM2NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvNtpcZ9hI5Xnrq-w4lpoiGafrgZKjAfN2-9tIthKZteW0-p61UuKCO4-uHodpIUVWpjinzsnsxLAc7Felv0LAoKfneUDcauRDvVZZoUtyFeAryP9bRdp29PGfs7NPdrEgpu7sG_U_5n5bm6cyzptp0LvsS1t5nHi8kug5Frp88ejEgIdN5ImssNXigpI75aEOOemRtWKOtMiHWPTrWhQGPCkJpzeQKbRD_NTJuAOhemV9f4nrNLPK2kDKWoDk6haoev17ArWJ3aV9glexe_pUEybnPnlnVakpSzweuF2Q3rXu6Obo9ciq1dzPExs89OLjd5wv0EReXmQzyc4fl1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=oDAaewRN_5yTuEj0SG12netsTFAsfM9C4nf7h-Pa-NrKNRB6uXDSTZbaT-ct_ZSW6K9boHdeN3ZTl48oPF-iU2lFXy3xYH8RY4MInP0B266qqGHXR9ZGLV8rMXPyxgi-dCiiX_ARPtKF4PDErg740pNl_VoIUGkvdWaOzQ6zatcbjKk-UQUSC0pbMTMw7Cz5uH7wq-BZaogC5EAaDneoatFKIVMoEAfJsrGqB1k6byWEcS17Lf2Bg2SM0TQ2kTtlT8sQ_4qnRLgMVGi4OwjSHkGfkW-zeImZBNfpOmTnUa9GeNu2Mr3YWZ7Kbxl_yxBBG0QhhOk1V4UBMe8sfqD-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=oDAaewRN_5yTuEj0SG12netsTFAsfM9C4nf7h-Pa-NrKNRB6uXDSTZbaT-ct_ZSW6K9boHdeN3ZTl48oPF-iU2lFXy3xYH8RY4MInP0B266qqGHXR9ZGLV8rMXPyxgi-dCiiX_ARPtKF4PDErg740pNl_VoIUGkvdWaOzQ6zatcbjKk-UQUSC0pbMTMw7Cz5uH7wq-BZaogC5EAaDneoatFKIVMoEAfJsrGqB1k6byWEcS17Lf2Bg2SM0TQ2kTtlT8sQ_4qnRLgMVGi4OwjSHkGfkW-zeImZBNfpOmTnUa9GeNu2Mr3YWZ7Kbxl_yxBBG0QhhOk1V4UBMe8sfqD-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
