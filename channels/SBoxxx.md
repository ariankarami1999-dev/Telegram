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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 128 · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 409 · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 431 · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=ikr_comZ8pLcQkcePHffImApZbSWiSiETbwira5Um8c9rxF525RbKqFIf-U_lOVG_KhA34ybR3mT162hbc_-BQkQoiAhP81PCcIbJLXo0_jtG6AiD6F2wzi158iEU40m_Gpvo73qnrJYejwtG-OgWXmb-wWzVUrkLIXrcC1PwG7Smz4_ieJ0N11PvXuEcgcEHMu6VfsMLbdT00hQKI9uCwCI4s7AsoWoIf_ihnYyJldmA6KzO6K5fN_CR3CYvJlyNkNSsea_ighMuWxtaQsxTZrWDbc_zxh76xmQUvXmVFWh_TWnI0nzFUdSQvRBWW5hAvkadfSXkuQQFrZ6_InEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=iEnfzeGpTTyLElAYkp918rrDyIWJpfgU7R8QwXQfAfF245YgD8VVWbsVvAiYldwvjWaCN88-b4C9qOvLcjiv_nSY7iKfa0ekzwRS4JT8LMCb5J2pgBfAmcrUrJ93nOjXxhc8W55lCw55V6FbyCPNjhNFAM3T2fh_Fd3xtZaXTI-tDDbmh6ETk25JB5iDYbR8owVx1ahKH-dlwmDwzzj7D3EjqdgPs83OGdX9_l4rTofxn5SFB1DIpn2XXnxzLsubDjDBY_W1Us0y7SMBqsXL9SPtnd56IMYAh6xGvTy_Lir6810r3Ge0p4aKZKUjPsvwF6pIitxQsa8jO2pjRQN-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClDkdBG5tz9HgGHocur5ki9O-q2vvdjOxp_uYLWhAALPuWLDUI5tG0RoRnHZknhRdW0hyLy6IXrq-4NqAe0CLue5PB_YkOU2kHQ8Wo8v9mjq7vG8k3af2bEPlvHOcZuQN90QXmZ2nWLwqbx3CTEpbXaDsm8nvNleQfTO7X4nFuRqn_k-wnJmgpuiBUjZ6ArcFucIA3wGnSlRONd9crkVKHHgf4EXsa2zAl8T8S1dpDNdISymUHpMQUW0Eh9mEOuw08A9hn8195E__VzpDXYQzRnFP93pUPgPYhEiMDkxuGnwYyBAgSb4CMoxhqnlFuK699RPchXMnYrkL7uU3gqynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBXP14-j5tGD5fJcWP_syTAeI1Hb1VqN7YcQRKl4cQlWzTwaCHIMBYa-CYewgVKb_CKlKF78sq_FuBkG2UWjXmmYak23jADZWbX6l6MOHhbNszYw_GkCG76s2RQKFVfWjJu-JzjmhJy9-Io8INtYeGpKzcbDo3RwmZm_VNWj00tKCL-fejbbqhqxWLdmd4ohJcYpQuVYBS0U3fp8VEcmKjnX0LmTvizRdoP3RANgClj35fmah2P23KaScRU6UuVRNF83wnBofnrOBJvo2JGN8gAIsVT3y6V87G9xG_4PtsC1PYARpuZP_0uWXtvbnKFmbW__JBRPD4FBV-JcvyE_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYjntyEq0Snag305RZOi4bDcrkru_InEMHXnjhLU9VtneuB8epQtYYQh3WDFjDTgxG2FxxeTNOWEk0BzwhYpzKGq_rp3gI1hKohRofG3R443p3WWAR_E6AyOeaPrxEkFJMhFiDk6XOGYe-sa0MZ2UFLfpyFoydivjnBe496tscBO4UpLXytEcVKJ66mFxPmz6vitfTrDecFfMokU6Qf-xuAmSwGAFeoL2zXWylUUMmcmcZ5oEX0HUiz4s7p-GPK0O4ckKpAUSaVGk31LNWqLSWLlXfAMYiLNyORDXnPsLJO4oclcQpfCYcFGkb58EYnIJArMnj9aB0WdTVrYWj7ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOEQz3_ZSjKz__23xHVUL_w_nE6Aa61eLU887sUBX6fY4VdhO0DTpnJInanY_pHRdpNZWt7h2UDEJk368sfoLskjsPkv5LMsir6WfHuE3mntlL2dfR9a5mkKaMkGB5uWDlYQKOsiqOZi4Lu6ReYrQirv1aIJzcZWy5TKgUm2BrpvirQd4WR5SEhnt5rocBFNKFxLFOzEOrSie1ubIv63vbPg7jvLgEg_3LnrE7qn20SGk8-HPjacVOcTKOrkgn7JGAdqz3v5PjkVxsJRiz-A6KbipJU2mARiATrruWpSgvyPINVWtrOsfySDdo1Dw4OLeHbw8J2Mn5hJebnCfxHlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5yo6Gbyf8-MReQhfOqf1SqxZooGBnKsHcWBCcPTjMZCm3PzscBwT4TMEOc1xa6RsJg6hrDGLOYIDyvyY0SpOXzP__kxnBlthWiCOV3weMPlUGEEaYc97AVWUkFB8cMPGsHRp8CU7VaQtoLphVxRVZPY4KHZZeQ5HMy3DgpNp3uR8F9DH0Xdf7aPVtlHVDUAOO6LREF7OO-Ti7Bze36Pz6qK8Y6z7l8odCIiGsswBwRSoB_bwThhJ5rPfIkGhO__lwBaSH08umQz-r8tCK1meNoafxdsGE3YgKuZ7SZ-qXy9_UomnmrH4-1orcC2B_1sXK82kE7JDj94xT0EA-EGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=fz8Ws_PMghuzz568eOXrhQGB-y2NP3hEDZLGOVRlKXnD3NJf2Zgf4mkDYv6PFm9XsHJ8u_XWi71Med0Cjt-HKzHI7F8EztbtNDNshNoYGueReqUYM3zA3ea-LWfgAKxKkHVAZUOyVv4DnwY0_yhdBek-5wGOvPVH2X2dku7pmmVz8dzbJsJnbEdSMdBdmsx7-5pqooBB_AqCLI-NDb41IP6U3DKmnMg846liEEA6nsy8GmvQ7xr7Uyxl8VuzsGDmJr_AOwanBy_A6LR06V33ksVaUH0BlgrNPhfu6xFj9nacqTnSKpXJdhsFGy2rurdkJe5b1NO5wkcn64BuSMA1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=fz8Ws_PMghuzz568eOXrhQGB-y2NP3hEDZLGOVRlKXnD3NJf2Zgf4mkDYv6PFm9XsHJ8u_XWi71Med0Cjt-HKzHI7F8EztbtNDNshNoYGueReqUYM3zA3ea-LWfgAKxKkHVAZUOyVv4DnwY0_yhdBek-5wGOvPVH2X2dku7pmmVz8dzbJsJnbEdSMdBdmsx7-5pqooBB_AqCLI-NDb41IP6U3DKmnMg846liEEA6nsy8GmvQ7xr7Uyxl8VuzsGDmJr_AOwanBy_A6LR06V33ksVaUH0BlgrNPhfu6xFj9nacqTnSKpXJdhsFGy2rurdkJe5b1NO5wkcn64BuSMA1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBLxiNhLHfY9oiLegdYT-SUbin-0sbkg7BTEIQNS-fS-ayRWwuY2stpFt2vEm4ksnHcRqEQXGwVkLcfWEb7UehfoyBmDPzelmm23UFi1Lbt3ZEEwqoJLatZwgyyJQMd6oSmtXbK8mQ7Wiagu_yN7dughcK9H0GUcqG7eCovgN24RfJy2ddEFZt-Yj__dSZJrA-lgTBKGJbf0trLE5tHo2Ak_R4_atV8Cql98hJQA6gcADHB595JwCudnQy40y43LigGB5UGD0ri07VczDJ8EdIKT_jbPnGgG80DAxdM7tSjDKpRMkYNQBxWZYGStmHlO-EH9SeJC5KT1a_0QYtzXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1DsLoUhWXuALBRXOEqDOPiELzXtmCuNkOAyo0QaGZabOTH-uxp2VEhATQC41L7V19roi2tGMGk5vQ2HnQdnYseJ9ymGarpwYRZiQi7WE3jFXc-3AsHm9MBWwlqbCOqCc1gOuOgNkXsjFaiONUwQUv52faLDUQh7HPAXPQFWoRzidaeKRkrqQc-8IYFBpfDDrcDciwxqszsaNUR8_OIJk6E7tAbZTXZGaQ7LuThl_vgIKx8s6uBXFW5sWak-AQpjQTiUFr8SHTVFlAu8YY9ud9aXMmCaLyi69tblGs5VW_9Agyo5_EK6flqOt1Kdbx7XeA1itniXTWKF7qe6MCWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GByalCC2I6qan7hymYebTxJJ8UtH7gdwLTjzdGyNGKkTW3r7bFE1PsBrcMOGUkApC4hIXvvXnt6h7vKT678FpeJcigwR1tIDNq89OPYtaRF98BdULN2Ukdp2gdR-oLpeMDFhpA3Nir3l-1QJO86sHl2lfJEB7mwwBoN8cvVXQIy3cPyjUd5v251mHA6r31-LdGrI6cyLLvUuLvlHf7qn4hl_9nb4Bg07_2GJBDhDzaX6LPBE_ppOn5d1KfLE1IQfm2kCAfWE3bQZC_pP0qJ7SB6yMOFgs6fd3xxO-47mB6EAKKcZasZ9odSyQKNSbJCnHtG-VcfKdIHWXvVdPcDkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWEiUqLAY851nK7ziERlqdqxCp6VPJUFLJAzPV9IcSSKCpo1E37lQAJO91vW_RUKsGkgDmkuo57Bm3SfTlSRrk4HKTaOG1itzzZZhnyoQxaZ_bdmL-ftAKHLUyxOOhxPK58wT8pkDrupwW2IV-Da0AgU0Vhn5faa3xcNOd4hUltU7m66NLfrnEzM7Gs6PmfBRYhM9XCAavG2JuqW-WqR4mVyknlWb1M-LOKkmPkvybFbeb__bwRQfA7r3_sd2un8dPaBuBgxWmXp64Av2vtubdUZpFjbWm9P1GsAsoEa8FyDQQQme7aivJIytFuNtOj4GFCO7h68mIMmlVEUPtuIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CupwOZM-1wUiTJVFUgvsQw33NrNAosvwItlx1xKOO3ugepr_lEZLWz_GMuEb5eIHF6jNvOoJbwGN0EFBkUM5QVrpGKhRb395EuqwPdyIhBiwX--scgTKSwN8_YPmEiC0U_hnFuxt3Fww1Kbb-VjwbaNafRm8tqEhof8y5XPDcCm8YEvV3VGxFGhGzoLJZX2P_5_5RHDP3IEB8PMOGaIfzrMTA_qo0bI9LEoJkwZ2QbBBrcdZecQpfEn1KOOQJy99fIFQdka-eRenaulOS2vXuxD4-2fDKP_xE2aZCQXL1i3jeUSrwrFwvY3BPjzpCYSTDUZclZuutrjqUX1H-mAFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOGVrASjBeMI_2sg_E4yZnwN8edSAEvbRpeWWIFVRLglvvZoDQp95IemILq9oiusKqb7XSsGW65N2NepDKr7qPsZhSbMM_fQWfiqOymi1eHlNRA-C26ivWaBBVnBHNMj8mGZele6ZTdCktI7GeV5o9LAVLPDItEl6Qgerc7AgY33rcRCtahTt_m3rPb_p_dmujRFdTbp7IiB1a8fY5ZmFdxcStunfxdbrALrDDwClQchxvbwOs8nBPsWvclk9tt4q_QSYkFNsHuroa3ciQhmUWmKU5hiB1COMVlXwazzwfSr7jqpMAlIam05FoLsN-pODHbhfBNSseY12A4QZ8EToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVafCqg-KPcQsJh-JCaBBljEBGOFzTvnJu3tKO1LJCWb9g8dbiaRWcGuVZ1aaC3pExd1BbWXjl0j9RVr6ohhrgy8MbOYZPUDUb1PWWW1fdHloBo7Vp2DUs1dEA5U4MRaBKim_M1U4fUa8MPQrNgo-DPPPm1FXFcrRv1GPKbcgxw6R9y9AnQ8UXQQSmUxvEpZgaJMR_GMOyMNm5CCPZnK3rq_iNjrGU4W0mY0YDy6AMqNtb375E4bjl3daA3DhO1xuvpOMKC1-Moa8WlD4jxg0zyJL1YGOrUP9Znbd3hY-sN7vnrpw-bViVY1JgzTPY7v0gFDZlpktXPjNc4KK8H8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGkeruVTGh9OtLGSRDglNyJJixeqFHCBWKmJ22lkfsqrj0l599cW2GXcjWuVD1s9l8_EpRtZGu-qlCD3yJuBFZdXTBSgUtHMp8I2_ofcfX4Esw-xMAnnxP2cz8C-dcBe4833zaAKrV-iSl7KFZdLLtavLs17fnKd2t_nyWcrwzQCMXP3N2cWtkDV5lXI_hHPWzGoivHCUVCJY_9x1FhizutB5H0NUCB4fU3aYCktb4KULw60GvjkAWfGIaE3xTRkODF1rr86Llxfx5JD0Cy1gQGRFaZo3t2yUtJmuQv-jI3mIWcB1_6nGKXdQJ3Eaui0VzBnTQD4yLQk_QnKd9dNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhUIGTJa_aXdc5bpDteeQUgAP81zEIkH_UP-uRG_dzT5Z4tBn1IsNm58yKgCIPmCEvzUvy5kc9x1dfThKaz8TnSjNar99xpvOn8-kqQvG3txoQhmkoSX8NAKxL3OvzhibdpqWqp4a6rttqp9pOF-yAj1s861EQjGOie6OFWIEDjurUyzRV30I7PNu-hLX2H7G8BM32tQmROnERzWHb6E2_LpG2M-wMwnA3jXs_Sa0NFXLxQca_vMynldI3xxqxGSIMl38inWL7zH9X4BoOX5wRCwHDQ13_tq9vxrZzWpM2T06B5w9G0nHp95NTqt6tG9Ow8Xu4jM88iMIMCGQzn-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoA8mlL4tyq6sWWBR-PrgKvsBqE3vzc4P3t-19GUD5S37PeaW7NHOlmKfmd_ZIACLZwgRgsSvkCyYljNljSRLJVWnGNPvJYihvqLZVlCEkYLZ68v7czbhPOF_DXuQ51S33rTluHjOEzRx47nrSKnHUTjR4Ktl5e_XYs8TqoKczFdHwHehKCOkmCq4W8ezSTAEgheZr2vxyUUPaw1n9-6gTz1dLfHS--L_kW6Sv54FiW27cBRz76520gHq3sq-qC9YCkTkrJbMmRLWoANQZE0FcgUEBdiNdTBlw9dAV15JkyymBjQ8EfaXNbgtwOrfEXapIKI8aKLC6i3qQUAoOSeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrJt4ARITykjugtkYNczpHioUNq6CtpreOZjGwpj5wqLtOjmNrTk556qSVka4aG9VnuBlxjIy4JO4_EXX0qJsQXR2muvi-o8OOWJAy4IowPTYj9UGPjsMCTK0b_8ploJApKr1ZOQaGFakS0l-GnOZECAZXKgTdNTPpn0TKe67-9PrPiRcdA7r9m0ljYeFMXEZhbtPbq9jKeiiww6VOAaZcc49dUR2Gu_GRIXUOf5QsU8BKJSe4txKr2QmSwBxTWc-DtnKHMMgJ3JqfnZkBRX1uZ2r51_8yqN-maMwbP0iSQRpmTMVtE_oImcEYmDUNDB0SrE4wByo4Ocq960WxNKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NT2s5qdl68sUNbKRzbhQ4b2kXCUEgKHAjH7vGUNBHAavmPzNBUj-uS7yRhEFEa0ZgiGBzaIG1anzZ9xA-JtGJMvN9kckFElDWaW05C7KF3zxSgjhIqlO2VD_5jU-C5a9hLH9h80vqcGsaMB9zUZPlmDMGtfkIQCKOpn8EarryyhpbQE5ze9lRoIAdsbM-UfiUnNCycG5Di4PqqjgE14dI6ejhUZJJUrOI0o50IhmetDFOlsjPUG7liqi8MsUsTwm3gkd987kclWHm9EYsNdPGlq2tmIqPIGTJPHihCFAiz73mNtll3V1l2mrfO3Rd5rPnmb3wlprPrN8Ej9Ii0Vu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHPaaNWDDiFPz7fmkiiTRG9jJlT14-NnGY2binOvF8BHjrmNtu1ysV38eUk8UwV5B9aiYa2t6U4IQM9ITgF0xe6rThluspbZNu6-nQpNWNtN8dQ4SwaZ1awKxoQ2psNys9sOrg1dGbk2LQbRowyVjJHM5E8s7MLGsmc8O-G1xoGVLaedqXCt0ZOwS5mYRaiOsOUUDnqbQd-LG9hRINckn-loESTEBRU4b0FYEEY5q1BVfMIg3l6wcUdSXDtAcbG-4jLzdHRQUexdJpdR1fRpSXNz4U4EnVcLFAwQbD2XNsEhv3u4odkH_2T3YtbsQZJQ_ZdlI3UIxlTes5uW4PrS8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=vHIbjrd3Ebbe99aKG4-04W_338sh-s0wHWgOxW2GJkCVA5S5yExvsCFAO3wpLFBch20kRMFij5YYLMlZs28q05Rl2D3eloXc9_1vf1RI8EsYqsFmrQ89DNh_cca05gVIPKY4p6nZTG8s_t8Xc_boMoek3osRAB7TZdsJ4wus0K4abt45Dey9p4WSacGXccglFTqtm11T6Vi_aoeKd8bShgsbciyrCx7OtQfviDHyCHQ9ofYu0Z600QN6GRPbPj33hUv7quzWu4I8bvsSDJAvOnsNWQTazrU2YHxYamBvnzfCKnXA9i8MOmPlDiGq4cZGJ4go2cpt1uvzamEfb6YNVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=vHIbjrd3Ebbe99aKG4-04W_338sh-s0wHWgOxW2GJkCVA5S5yExvsCFAO3wpLFBch20kRMFij5YYLMlZs28q05Rl2D3eloXc9_1vf1RI8EsYqsFmrQ89DNh_cca05gVIPKY4p6nZTG8s_t8Xc_boMoek3osRAB7TZdsJ4wus0K4abt45Dey9p4WSacGXccglFTqtm11T6Vi_aoeKd8bShgsbciyrCx7OtQfviDHyCHQ9ofYu0Z600QN6GRPbPj33hUv7quzWu4I8bvsSDJAvOnsNWQTazrU2YHxYamBvnzfCKnXA9i8MOmPlDiGq4cZGJ4go2cpt1uvzamEfb6YNVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGypi-aZ81avGiU2cDXq6qy-E8C1Y-KiWiWBkv7c2Yd-Gmqjyi92un1v_Eb546CH67aUZBPztMZmWEw7KFX-7Q_wNguW8FOhzy_uqr2sJcaz45ug0yALFPT0wKeQ8Or-37-iS9O0muSnFOAuPROgk3XNj0GUllkxAbJ15Ea625-abLzIZPnIjeN-Pl2YzNDiaMNZCH9DqjtRlt6dDNQpoUy8aMUTLpZ32mWhbTGCalSmZuHGjCDcRzJVAIIfxnykssINeGYuZWnq79amN8kzk-69KETVhKkClLuI3WSckMxSd9XYj-xU9EeFRIacvfn2AsijZb00xU_XoAfGLTfNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkWG_pIsAabEhxvxmq1CFKEoZrQFARej_5Xth8ircXKOmVOgEguQidKJzD4S1Hm66l_hPPfM6RYstgN_j4WVNv1LcO6VJaOe64IMwx2DnWZOdaJ3D1kyrmNtC4ZduK8_0Y4g36gUHcAHJ8Yqd4g-KX-qWUWrj3tZIlpn6S-6jpboUodgQ5srhdr5YKuaLAqPCvXnXzDt4uaiQDcIDM1REL6mqhUlv8uYfn03uIeHL3QgYY9gkJ4OBQs04Ij0LQjtT4IfAdGDAEb8Fz49P6yxNRupNLjuviihEkgVmeGGWOzDjg_otIuCnG_6C2F1wY2C2Uv5gx4cvyaom0vjEU4Hbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDS07d_BtaghDx1bT5OSbH1VY9KriJ_c-kfkjcIWPJrqtwS_WcumjBLAMJl-ARVbSr7l9XXOXoNTw3MVyRHOleM69hsDWJ1EyKw5-eftL-Q1_TnZ1dEuOwxsNgcQhzNBC5G4PZfElP01EEP91Rqy0bk-kSXOjbbaijNg_AHb5E8HvSZVef3G_c4ViuRcqjcPsGrlnhQUr1NUAI_7WU1SgA_UPVdOibXL1BuFe96NOwbV3C7dcb7WGj6fUoKAXoTsosBDVJCb7ABGYyzXSoUmkZ_0sk8zYOiPYeffqamD6R75RHjMGD8jP0pgiAR5tNSlKSM0q2Uy6nxd-DU051Fkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=eRsSQt40BFjofW9q2Tr4bb_otJrdTjvRQ4puo-O-Mm24LNEHpjgY-5cy0rv7NrgzKwON5tEfSiY5WJgk7F22riMjNLvZB4-Zw-SojLVTpCmP1yk7ZuV3QwrYMQ38jBOPcM7X89OOfU7iGdEeycZS1GnMqSxNRstnBTrNSRIIIKR1IvHGPqEuS7R1yy4Qw_bRbBp1mOcg3CvUIGb_fZDiaJBP3RLMDsC39QnsS4HU37oXb02SG1gXVnytKS84aM7jePr0yAgijzFOByHPC-37zsyZxhwGFXdRoSxLMEAWDQjpJvuUj4f6r_PXi-9DUaADMGI_THTRKxtEKhtEpuKnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=eRsSQt40BFjofW9q2Tr4bb_otJrdTjvRQ4puo-O-Mm24LNEHpjgY-5cy0rv7NrgzKwON5tEfSiY5WJgk7F22riMjNLvZB4-Zw-SojLVTpCmP1yk7ZuV3QwrYMQ38jBOPcM7X89OOfU7iGdEeycZS1GnMqSxNRstnBTrNSRIIIKR1IvHGPqEuS7R1yy4Qw_bRbBp1mOcg3CvUIGb_fZDiaJBP3RLMDsC39QnsS4HU37oXb02SG1gXVnytKS84aM7jePr0yAgijzFOByHPC-37zsyZxhwGFXdRoSxLMEAWDQjpJvuUj4f6r_PXi-9DUaADMGI_THTRKxtEKhtEpuKnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvVVBmEYxVenv5xLObbAk5imvWJ7GfW7X2_WGSgpwTVYcOlp90UOzvCmu8RQTgyJBBr0rc5ed06LN1oIV9-s5oPOfmcRDbyZc3kqasihag3-b76SiJ2wYX-s8S3yOA_yGMoeyS0VbogZOSdLEIlfmcXD30iO1M5tMdtWrDVjkl5boYaQDJvb0D48TW4eRl6aBr-lI07kmm40nRYTZriW8S2qJjEWbHaH7VVul8d4KO4Az5ZKXICL4B4GwyooULf2syaib7kZ1eD8KxiT66l4734DWasoxftmJu-ac0Xt-DXWL2zJPaYqycj3V28k7tz6irHhGqvFKGjxmF9PrGFN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97MV43YPqlY4nx9O2oq679XSg__MyP9BZppZn7TGZkxYcq-Af6tdTg8x3mdN9P07SSuDNqoA84p-BzN6ncg-LJkS4NC4iKJ5xqDLEBKixidtPU9EBhPk-zn6dcAtgdUZvvZ4NWnQNtTmb12KHctHZm1N18Iz-I81HAvOxiBaWeTEuCQ2IkY0_Q9N56vEGtqKGlLQxEoqTvtGhkyEs5_n4Vru5KFoU0SnLoB68wXrSSPWJPM74Sd0cWPkG9-f9Y1K7u54gzC2jqRLZNhogJ78hwu3r1EpHatX2E14cA3Yt6DnPTjGMyg02IljWvVM_RIGkXi0WGMJW2i6gMaKbIDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCFzHdHjzWnmk_t-io7P9r7FrySDcP88no0VC-7_VykZbN77MvXaCS_tcpzRW34JvyWz7EuqLDnCt0hGAlZqlEh65zZzrHOFy64xkwu_f5Z_dlxeLQowKvizscbOehV2AWD5JSz4fLcI-luFDvUh6l_JgDK0wMxu8hhUl-T2cOaDawfCe6cKqbuJFFvZQKfwx0StKTd8I74PaUd0BXxwl0qVr36bOq_TRE7yLntNeyw8FPPic4Vpr6MEYbAFQQbiHRDWUBQ3zcsRwxnxEE1jr9T6OhzgvV3XkiK9LRKZkJ_1OwcDmB2KL2SQOcHxFb9SJjKl1TtRpPAZGSqUauQpQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qn--3NVdihtwnO1xSDXPs73ooiCsqbz2kHHJ9b0TdPi2o3nz1J2xYt5HwHfHEUIeJq_Lv_9rfPtV-vZEZ10_AjQ4Ks0XybWACAyU38mvnvZT4314tmACi94dTpqZQlF4DjOlEFNseYzrlC8VrcpkmJ9OO4qKbesVeE-y0wetQ1OfVnKJofYP3J_eLbVvFYrwOD3mia2ECeJfJZSmo_aXOhAv87axegna2zOu24fb-jW0yvy6cceZEKNoVE4yaiguPcjzW_YLg0Nrk7e57AVzRGmH1ChZ_ClzL6EJY7aVW8OjWGrS-roFkQGMfvI457Ep4HinIbRrkZAD_r8YaerlDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g82UyFBUUvu1m30JVdQGtINdAl-Ie4sA08XVMjh7WIXZ8W1YaK_4t5ats02BU2U52WT0i68KbAQuTVjLLIcuDecOnfIokp1oBRBdrfS1IJTCm24N1ftkhFBBmjn6pZEBoaMtmqxtbFRtySoF1qMnvXJvl4snwqZbL4DshV0EAhzhbGPTEoXrVhJcqx2EOQN-D4b5UvLi2tNo1EccOND4mHZOrrlsQF505TyMcEDsGQCnwBFXYw61x0CawFVfha1RsmwAy0lZn0QvuhuDgXzBMbbvN6xuc960PO1GyzIdpxEiLlDatE6CXB-rw4R9At5yzuBGskCGLrWADpCiy_oFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTIr_E05RCo5tHqg9Cc41sx1Tpt1-3KYgv2KTaTCBPAvhyYijmWza-naI9Qu3jbUfPxr00hi7RdCRJkFjrJwK2GIWB6MOBbu-7RPWP4D7p36pNG0WdV3UDRZmp6gB9cEn17qIAPz2hKAzP1qbBO72xY6dU_AoQOtCLv4w1LWqjl-i53XY8mtrlPrctaTyHhKFuRPPvEiaWHQ3KiDgcK68YZilrRFPq0moTPBSbadOghEqC5EQpF0Z4xIXFmC91_76wAxpyPYRwnuI0Pf-MwBU8OaGyAo5Ao03L-Kah-UMh5T2962TXBxuX3Z2Ds1HbKwUJz4IDOwuETr4Ga2HwJKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbAP7h3qQtK9Epg61IvZ5EPKmc0IT51UhoE_Pd9uMx2j1h22VtM0dlkWZU9QGnEGjKHre47GZK5Htj3QB4Kv2SZnwNnjDDM42-ATY3Ed6VA612pFGRDlNWICFQawgcWnm1GRk71OctOhDbrLjcZxPp7HforiskZjPVl5x6iDjSHZrbVuhjurxYKJ_z8Y5DQD65ronywR-Hlp6GnNccWGAK4FKrKnpw1qIFb1R4iz1ku0OrRTh41PG_6lIXqXV6NmcPT-kWOZf8yBzeRa2nTYbkXziJQumdxbQkHJlQ_ZJDmq9CPcJeTLsOlea7-rXWbxl9pyFi51EhslIH0zQiyvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=txvd0ccJ3CHMnbe__yDHAJ2JbByohMoFmSzsOWoWgHZXZhuTg-QfwTxR6cp8bc5OHaSvxijGUUghKHOGdBMDDRE8dj04H7w9gVpZEFeQlEzFm9T7tCryrAvBf3YW-xzFd10NtcV-kyy7zIdD5IMx0crb3tm-waNMmg9UwhOMHDIJ-FYwmMUj5PPUagMVzypleVopjn_UFIUJRRpKwigjDaME-um095b_xlbiD7BfSm00rYqEsHGCIuIq8q75Qyk3gMXcgbaEEYZWMwraMrQHteXvqy9no7JMZEiUy-SnI37K43DcHLtp3jc2rWfNn-RdPcgkzBI9WUEttAQHsjv18w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=txvd0ccJ3CHMnbe__yDHAJ2JbByohMoFmSzsOWoWgHZXZhuTg-QfwTxR6cp8bc5OHaSvxijGUUghKHOGdBMDDRE8dj04H7w9gVpZEFeQlEzFm9T7tCryrAvBf3YW-xzFd10NtcV-kyy7zIdD5IMx0crb3tm-waNMmg9UwhOMHDIJ-FYwmMUj5PPUagMVzypleVopjn_UFIUJRRpKwigjDaME-um095b_xlbiD7BfSm00rYqEsHGCIuIq8q75Qyk3gMXcgbaEEYZWMwraMrQHteXvqy9no7JMZEiUy-SnI37K43DcHLtp3jc2rWfNn-RdPcgkzBI9WUEttAQHsjv18w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=uQJBTcnH0kiaNWeHhl8mNynCbD502U56_TyK2Ddi7t-rxi4Lhj_HFpyDYRHs6HIA0JjI6nKNgBUfugdkxES8Thb9MimQ52M-aF_6j0UYr-tWaIg_lJbRj9GIB8oBTiSaOTccx3P2wjhjyi3oqoQobM8BdDlP1HG3AvGbPfaga-_PQxI316TTCU5N8FMRaCgZuMQgi1p5pUcIGViBTN1gjlipI8LMc5_tRHmpits5W4z3WfN7_ucmKMI531pC7dG6yTv-SIxDan_hQ_UOSOCqCM6Qc3J-iH5QIvofs3dmaUtJSBBkW8We9Nvh1NqNCOht_mpGwQ4gxhetSh4xiv0wsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=uQJBTcnH0kiaNWeHhl8mNynCbD502U56_TyK2Ddi7t-rxi4Lhj_HFpyDYRHs6HIA0JjI6nKNgBUfugdkxES8Thb9MimQ52M-aF_6j0UYr-tWaIg_lJbRj9GIB8oBTiSaOTccx3P2wjhjyi3oqoQobM8BdDlP1HG3AvGbPfaga-_PQxI316TTCU5N8FMRaCgZuMQgi1p5pUcIGViBTN1gjlipI8LMc5_tRHmpits5W4z3WfN7_ucmKMI531pC7dG6yTv-SIxDan_hQ_UOSOCqCM6Qc3J-iH5QIvofs3dmaUtJSBBkW8We9Nvh1NqNCOht_mpGwQ4gxhetSh4xiv0wsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
