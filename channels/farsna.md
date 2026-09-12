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
<img src="https://cdn4.telesco.pe/file/VAwxHeuMcfOYwO5FawhPWJ7MBR-AUhXN4O5UtwjA4BcyjoEbeLCa9Sy0bI8x88eMDohopdK0jYLx1eHL0Svnh2qTO7-lw-M8hzwHWLDnfO9Iz8Kh4VfAV3xjzufosKEcP7qD7gzdwiL6ZmfL5efg2q-z6SE4JsUYXA6-U7CBfBZJhlVuBUkeZFiuAEs9gYGuDvUHahJZMgx0s0a8vEnobYfsjbtQaP5q1aoa3J0hItAY4muLglAf9TiwUJIzqZsMyu50jxVs7gf_yMwsl98Qlcj5oiiC654AoVA0Itvhh0fLPxJoXuXur1AjnfBOiqAuvoacfu_Cwx0IPRGsffzAdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-461531">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ مگاوات انرژی تجدید‌پذیر برق‌آبی به شبکهٔ برق تزریق شد
@Farsna</div>
<div class="tg-footer">👁️ 309 · <a href="https://t.me/farsna/461531" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461530">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/461530" target="_blank">📅 14:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae4DXayOGAePEDRhfOCXd4GbS-vhH6eiXYdx_Rg_xV49PSY_NeLuMWVbrD0DiUTi_o69zkptCFeGbHnRnz4wsud-5vhTUKAsTBvuHb60tIFEdB-3NpfLGvdIgvKwF5E7Qn1yBXtWBxVdlLVk2liyOHpo647wumFip6fBRbbuqvQ_A_TVOGId6r6idYH9zh0OFnp239AK6K4fSEcQ41wh6qQj43S2vLZnPf9eI062Cw3xZ6ygZ2dTWN34lsUd8ysEcrb3VSZWjfMyU0GwAksrkZCJBiyhHUdLXZjL_qLheLRG7sXYLrrU7iezMrAQNnAJfy5DZECYX5f2m9-EbEiaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brlQfW-nsGg9lm1Q5EPRnhlxfGaejMM9d9v0QMNv7arfkUwES_4S2fSL4M7oYFEMaiJNDdb--E4G2RBMEhANiU_nuWWn-YJGmBT79gFr0YnDN6f66Po3eA13I7NXBfdbV9p031z2V_BEg75ChG7CQMmvyJ18Tenc756882zlDMfO4xtFXy_3OdXSCh2iWjg_8aLmHTL3uE3K6DzJO3VRyTJMlVekdq9Uy6Jrn5NSh89q6Fgs4P3om1k-a0etz6g4bzkW-iIMC3WQvaLmc98uZudI5an3G2sJL7hJYuQY5jjyP1wPE2HV69UB8PxcnQM2OlSNWNJMGFTnMEdDt-qeZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">25 سال بعد از یازده سپتامبر؛ مردم دنیا درباره آن چه می‌گویند؟
🔹
در پی انتشار پستی از سوی پیت هگزث، وزیر جنگ آمریکا، که در آن مسلمانان و گروه‌های اسلام‌گرا مسئول حملات ۱۱ سپتامبر معرفی شده‌اند، شماری از کاربران با انتقاد از این روایت، تاکید کردند که این حادثه در چارچوب یک عملیات «پرچم دروغین» برای تحریک افکار عمومی آمریکا و جهان علیه کشورهای اسلامی و فراهم کردن زمینه جنگ‌های بعدی صورت گرفته است.
🔹
بخش دیگری از واکنش‌ها نیز به سابقه سیاست‌های آمریکا در قبال گروه‌های تروریستی اختصاص داشت. کاربران با اشاره به تاریخچه شکل‌گیری و گسترش القاعده و داعش، واشنگتن را به حمایت یا بهره‌برداری از گروه‌های مسلح برای پیشبرد اهداف خود در منطقه متهم کردند و مدعی شدند که آمریکا از تهدید گروه‌های تروریستی برای توجیه مداخلات نظامی خود در کشورهای اسلامی استفاده کرده است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/461527" target="_blank">📅 14:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
🔹
مقابلۀ عملیاتی با تحریم‌های یک‌جانبه و ضدبشری اولویت اعضای بریکس است. بریکس باید صدای عدالت باشد.
🔹
اعضای بریکس موظف به ایستادگی در برابر عادی‌سازی حمله به زیرساخت‌های غیرنظامی و تأسیسات…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/461526" target="_blank">📅 14:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bleGXamophasIwzTeCoxp4IXDHZSdGv_pHjUafrSWxqV_q2Qq8o39Fosatoph3VwokrPBMXBhUxtFGDhQ4oM8X5Ae95c_jw7uCwC04-1WJijHLe2RNzfNzXep1QICcZcMUiT4k1P8EZ6YzXOWVHEXmVvVlYlyRDrneR6NBrZQWaRfLA5CQZ27ALnfu1vynLvuTTQBzN_GBrSgCzjKN4WndfATl3IXiCDQGxdOjc0pb51vH_sT5bNh45ySIBE9eIfIiWqSGt6onLP8zYY-TuO26n3D-g8MipK91T-akd0JMerIL6OTkXkK7EVDHMRYg0FV6Dc61gmRz8kGIc9BSY2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه‌ها می‌توانند تا ۲۵ درصد آموزش مجازی داشته باشند
🔹
معاون آموزشی وزیر علوم: برنامهٔ وزارت علوم برای نیمسال اول سال تحصیلی ۱۴۰۵-۱۴۰۶، برگزاری حضوری کلاس‌های دانشگاه‌هاست.
🔹
دانشگاه‌ها براساس آیین‌نامهٔ جدید می‌توانند تا ۲۵ درصد آموزش خود را به‌صورت مجازی برگزار کنند و آموزش ترکیبی نیز در دستور کار قرار گرفته است.
🔹
وزارت علوم برای اجرای تدریجی این شیوه، کلاس‌های نمونه‌ای را در برخی دانشگاه‌ها آماده کرده است.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/461525" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461524">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/461524" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461523">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szMxxNuTxrjWhBjTEhbm84SiHPF-_-aKKYyqn4mu_fUvCnhp7wFnpnjXlJU6JgtIMJmARZdKnhT0HZ4pFXyHlr3DnYDpiBAqiOJAGG8FfGaKpmuz1mce57pPEPYEGW906IEsC0jnU3EqbfhRhdnqIJpI5K8vc2-qDRKjw-ULYLTSyK7Mzfy48kkItf7CW7-TSeWHtS46HxLI3jnMc72TVkt6IMTvCWQjm0PoA1UmuZiK3XMNTN5WdhszYaxHHhBjRwGLfOD8v7t24mIqGvDUStn2aBrQT4gukRoUw4lVG8XHKk7-ow2XNoiIG0mVXp97KMCWQaM9IGJ5F_ZOot_yjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: پوتین مایل به دستیابی به یک توافق است و اگر زلنسکی هم خواهان توافق باشد، خیلی عالی خواهد شد؛ مانع اصلی ۲ نفر هستند که از یکدیگر متنفرند.  @Farsna</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/461523" target="_blank">📅 13:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461522">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از به‌غنیمت‌گرفتن تجهیزات نظامی مزدوران سعودی پس‌از فرار در یمن
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/461522" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461521">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/461521" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده‌کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه کلید فتح قله‌های امنیت و اقتدار است
🔹
سپاه پاسداران در طول بیش از ۴ دهه همواره یکی از ستون‌های اصلی قدرت ملی، امنیت و بازدارندگی جمهوری اسلامی ایران بوده و امروز نیز با اتکا به ایمان، تجربه و توانمندی‌های…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/461518" target="_blank">📅 13:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQz8meuBfZeFn1mAjUkdrxh8DPCDMFPoNaRvxRQgikrEAnDBaJ3qcxACGiGgbDcJ4PIRyajJRT3_8fNE0R-yR7xcBZEJnKuMzsE6ldYUhZMRYKWwL6Q34_gS1MEmSp034NMqb_Zt77Yn6Vzf-MMA57TQVVTC0qnGQk08VjIaTRWM01naPVbUF_0qgrdnmam5T4jIvzZVV69JKNxMchLxkba94SOFd7sNm42XOdbristoCgO_aj7TLkEPX0L1lBtltwf9LGAWZMyM8Veqh_sWIYiuX7MJ-HRKRX6rj8zdXFmT-2zlEvrV615roaWvWG9zD1oonimsEGNT0zH6zc-ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده
🔹
آمریکایی ها به سد مستحکم ایمان و غیرت ایرانیان برخورد کرده اند و استیصال و درماندگی در رفتار و تصمیمات کاخ سفید موج می‌زند.
🔹
ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده است.…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/461517" target="_blank">📅 13:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWm-XzhE-YhyU6hjpDM3wmqyiDStUOFy0wbL3zJKMklbY0CoS_6-VX1VRuVIpMu5pip9ClCWf6wPGH-lscdYaz5Kdyn_sBzlK31VGkZGOczLhhODZLPRE5RoQcfw1klQveFUrVmWg-GAErdC5UczbkOaszr161YHj334k8Y0NzwyrDkFarpCrySltRTVLBiHYPNuZDXMKFipPaA6K9OUgc_-yfvssFjm6q_jYu2-aqiKO7AGHcPA2qBGA9Tb7VJT8vllPeIs_YgMJvL4id6k0uR2nkDSIAGMg7MmaYFmwlwTKZvhUn41pCugepTfLTz_a_laAQiknGy2HZaPyxLN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/461516" target="_blank">📅 13:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsplmAlroy7VxlwDq0dQryF5ev-IEpls-zGEN1tFbbclfVCZLU-d_pLEg1sVopTENMB39v2l44-vbuqyh2PskNrwEj16ynfU9K2-2UdQKOpWQZIUtFk7ZmdtLeOi1E-3R25sL8MAsctiAQuZUuKiKg_xI2VHtWkNyuKILPNEnI-EWNRa2VEtjRmFJlTWyIgXj8s76ALTimC6ZDIKL-S1384UPpq8rWtH-GeZ1Zh4YUMaPbJA_1rt1xcPiHHsucKcJY3xmBsZmO_yrqKwEoKIT4mu_UPb-6PCj2F73gcugH1kxFPa8YfKP03HfpfaWzKXfkO4qlrLJzsjaDq82f64wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه مشاهده کردند و واقعیت‌های نظامی ایران در میدان رونمایی می‌شوند. ارتش صهیونیستی بدون پشتیبانی آمریکایی ها در زمانی بسیار کوتاه فرو می پاشد.
🔹
فرمانده کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه، ستون استوار امنیت ملی و کلید فتح قله‌های امنیت و اقتدار است.
🔹
وحدت ناگسستنی ارتش و سپاه همان گونه که رهبران انقلاب اسلامی انتظار داشته و دارند، سپر آهنینی است که از کشورمان در برابر فتنه‌ها، ترفندها و توطئه‌های دشمنان، محافظت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/461515" target="_blank">📅 13:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmsyAErB97ReMsnwMiCeijGjXTVQBponeVxz7ceMWmmrdR3R3xdgBg54_otInb5N25A0zr_DvOVla1xNIuEX7008MGFR_Z7V5nmPamO744MftKUyTK0gdgl3kqMlyiBf5B9IRc1T_1u4KTk3boinD3toqZMFLbg4Gcl9BEW-hd4WZdSK8PD2myQRbYegpFiNczOFSPztoSazhICCWrzBzqnt4FF_Se62NXjZqG_XROwJqshpXXrXNmDHuIQP2KtQbs3E0tgHhDot0SPrseuO6xt9sr3PGrHOqEenvalRfFt-PCdVtSvcbs5bYsKri1E2wYRUfTYJPtJyhI1SoU2-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردزنی بورس در آغاز هفتهٔ جدید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۵ هزار واحدی به ۷ میلیون و ۲۷۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/461514" target="_blank">📅 12:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مرز خسروی باز است
🔹
گمرک خسروی: مرز خسروی باز است و فعالیت‌های تجاری و صادراتی در این مرز بدون مشکل ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/461513" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGSr_Uwz5wS5x9t9l4RLycR31_lDfvRGkoMltb9MRX2NvxVEq0JWQxT3nv1Q5nmNFzGTKn_EYcmCGr165BPtfLqN8o5AlvXsbRkpWKf9UOXTtJOVV04UnrbJJzRkogKyxL0x3-l0kmczSbrGA-Wm_vIAFv1I4q350dR3ReYw88k_DXfxOJ8WwREmLgKLS1ixr786NlYabhRX0f6pffqEx4tg3FV5jN4kgcv3bOIXXPaoP6_-oFqIts_ERcCBlCm2sCuVBr3q76kHL1nuoDCYSFKztsE4LJ_HMZiHy6rxiidb16E2InVzjMx14gTvAdRynwb7Bj-qxCaQ7Aono62WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/461512" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOiKTbJhYK7pmCOOPSoYml4W-EGTY5wAZllReotuabMjOA5PT5ejPUUKCeCu0B5l8IThlVTwk9C0_je1mhOZk94APVrqTkYowI3H5l_axr_yOt5fG3Svp_ctY-fRdWdFuJsKVpnaolPdNborBRTiNy2OG1_I_WaC0acEWZ45bJA_DCwbhsBOthQJTjumD1rT1ujM-Nh5gjeV71axjf58JZLTj-y4IaPWU46qpsouCdOIap0JvsrlWxrXvEDKB2GK6awcFHy45JtsmmNMIs8flOnj4zhUxgvIuuinGwKwVdkbsLLegtep0NZLcdPvIOTQPnjAT-jnA0RRNy_iwR7NkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد پتروشیمی خراسان ۳ برابر شد؛ ثبت رکورد ۱۲۷ هزار میلیارد ریالی در ۵ ماه نخست سال جاری
به گزارش روابط عمومی پتروشیمی خراسان، مهندس عیسی نوروزی‌پور، مدیرعامل شرکت پتروشیمی خراسان، با اعلام این خبر اظهار کرد: درآمدهای عملیاتی شرکت در پنج ماه نخست سال جاری با رشد ۲۰۹ درصدی نسبت به مدت مشابه سال گذشته، به بیش از ۱۲۷ هزار میلیارد ریال رسید.
وی افزود: از مجموع درآمدهای کسب‌شده، ۵۳ درصد مربوط به فروش صادراتی محصولات می باشد
همچنین نوروزی‌پور ادامه داد: پتروشیمی خراسان در همین مدت با *ثبت ۵ درصد افزایش تولید و تحقق ۹۸ درصدی بودجه تولید،* موفق به تولید  بیش از ۴۰۵ هزار  تن انواع محصولات اوره، آمونیاک و ملامین شده است.
مدیرعامل پتروشیمی خراسان خاطرنشان کرد: رشد قابل توجه درآمدهای عملیاتی در کنار افزایش تولید و تحقق بخش عمده برنامه بودجه‌ای، بیانگر تداوم روند رو به رشد عملکرد تولیدی و اقتصادی شرکت در سال جاری است که مرهون زحمات همکاران و متخصصین مجتمع میباشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/461511" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7FmQLYMGRP08Gothc_FbnPGSI35enqVQ3iB-GHxvHDUGbNJ5oXMj9laoIADx81d21UQQ9MBD834v_MpRamZLmFWOLXYA76txX6fuatekVp_yqiXENBt5jolmUVsTMwkoAvY1zOWl6Kud4dzgD6zpEFqmSy0h4dFsvxUUOEKur0VGvERp8Ph8JE0d_t5Lh3msxv446ka23M_GwEz-_i6IuVysVmmC8FfNjla6G3JcMFp7DZmXrnhbmx7XSz_-BwafQdUKTKOp6NKSXz5dEMRPRd_ggsmMHIT4Cv00UlP7I3-Pae2IMRXpqu53NnTjQinOXZPm2auqcgJ8_qJEd0UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بانک رفاه کارگران پل ارتباطی مستحکمی میان جامعه کارگری و کارفرمایی است
🔹️
سرپرست سازمان تأمین اجتماعی گفت: بانک رفاه کارگران، بازویی توانمند و پل ارتباطی مستحکمی میان جامعه کارفرمایی و کارگری است.
🔹️
دکتر محمدی با بیان این مطلب در نشست سراسری مدیران صف و ستاد بانک رفاه کارگران، بر ضرورت بهره‌گیری حداکثری از ابزارهای نوین بانکی تاکید کرد و گفت: استفاده از این ابزارها برای مدیریت تعهدات مالی و تسهیل در پرداخت به‌موقع مستمری‌ها، با جدیت تمام در سازمان تأمین اجتماعی دنبال می‌شود.
🔹️
وی خاطرنشان کرد: سال پرکاری پیش رو داریم و باید با تلاش دوچندان و مدیریت جهادی پای کار باشیم.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/461510" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/461509" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ موشکی کره‌شمالی به رزمایش ترامپ و شرکا
🔹
ستاد مشترک ارتش کره‌جنوبی اعلام کرد که پرتاب چندین موشک بالستیک از منطقهٔ «وونسان» کره‌شمالی را ساعت ۵:۲۰ صبح رصد کرده و در حال تحلیل مشخصات دقیق آن‌ها با طرف آمریکایی است.
🔹
این پرتاب‌ها یک روز پس‌از پایان رزمایش‌های نظامی مشترک کره‌جنوبی، ژاپن و آمریکا صورت گرفت. کره‌شمالی بارها در جریان یا پس‌از رزمایش‌های واشنگتن و متحدانش، دست به آزمایش‌های موشکی زده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/461508" target="_blank">📅 12:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMArBAq7LQfmsgZrt9YE9SDmoBzeCOfgpWSQFZ9mQy_rvCEJLFKH243BhQM44BmTaWierpeNzUisWNrtKuajfzzkzpSIMr1akxglLluIbtv32rXm61RmwYqRjv7Mb-gH6R1_RxgpHLZXyjQSz0o84eLtKLz2mrjUs0RToRl0gfNLHzJW4HTx39KSnLvlSUKuoQ8WhTvSEW3UvPDzZ8iz7NUcHcMsTTvs5fzwTSKrRglPbpQLPeWn97Fe7w48l2D5XzpfwwSks4xXz-WM28uGNVNS2Y1bdbya-gJQPvZDfuUl-YwXpSjIltpPImsRsdrMTyC0vXr_bOtkzaz_q6byXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلندقامتان ایران راهی فینال آسیا شدند
🏐
تیم ملی والیبال کشورمان در مرحلهٔ نیمه‌نهایی مسابقات قهرمانی آسیا با نتیجهٔ ۳ بر یک مقابل استرالیا به پیروزی رسید و راهی فینال این مسابقات شد.
🏐
ایران برای کسب عنوانی قهرمانی با برندهٔ دیدار ژاپن و کرهٔ جنوبی روبه‌رو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/461507" target="_blank">📅 12:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/461506" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmy7DEYil9SFClMd7WIDwK3-Wg5W0wRFADQBhXnbZmNqMBdJFgegogzuQF6AU6o_xbvh7rHUvdGuqC0tLuDinR9BRYnNOaXGnbpx6ljxEp81l_XrncJXmQ_02PC4uUYTT2d0qSBGhtEyKunikvy05rkwa1eWUzBtjamwer3J4-G8OW-AJ_1HV9bR_bfdORBgGJ20znUHIASD2u0s0vQrbh_Yh1jD0HBvP9zL220_e1PwDDCg2KnIDcKENd4Hm9kPCVnpPIQD5colak1wRs-11AjMnWCeVYce-LrXm6wQh1VS2jR11e6crq3OGUHU4Ts4nWh3KmkhcxH_s1pLXLWwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد ۱۲۳ مگاواتی آسیب‌دیده از جنگ به مدار بازگشت
مدیرعامل شرکت تعمیرات نیروگاهی ایران: واحد گازی ۱۲۳ مگاواتی G15 نیروگاه مبین انرژی در منطقهٔ پارس جنوبی که در جنگ تحمیلی دوم دچار آسیب‌های شدید شده بود، به‌چرخهٔ تولید بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/461505" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO3Swn83cFir_t9u6CmJZmqveWEZ38t3IhpYO2OCFMI0h-RK8pchO4tdH9FSt50mNdFhPyyUGoJytXSiSvgxe5N14VFBj10NRUNMDPsZbaxuEPJjfcq8awguJORKwSuM3e8bVBD1NONxmc7mbAqvTkR5Yb5j3eu-FwYZy_y7vkV7NpbJk4C-Axc_zPFIpAIM_1PO80Lnhood9QreITjkEJgPs8ape_J1GYJcqPw-YR9SqF7vF1F4yvMb-E3epr8MIyZPRML2ctjvlpCT3ASxWcZkxBpBWTJxXrdkG3bbvqs2yl655H7eVuMUQ1TEYX7Js9Im2SHfi6J1OPR2qGFoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/461504" target="_blank">📅 11:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghAilx2lO4QsmrHHcypiMCj0gEBNjpetD_0LVbMDuDPXik3kmoR5R2qUlUKhnSyqcZrhXQPEO4vri3MJ8NsHv4gi5Q_sT48JTixW2StAg--pEvlZhcXTY83LOrXGeCmvOAr_tl_SgXszRe9Uv9xL_opneDSHZ9P-UTUHxi7iDSAv_yOhYounyhL6em1LsX_EJ91DiQHbFEXuYWI8GxN0GIQg411Igqp9BkRD2LI6M4Mj-FXOLU3y_wvRMFRGHb_2Msqjp8W_IVbHJfvG4T_KWH-niqCgkNHZcIm9gMTfyrCJ408WZMIEH6SKr-kFTAzuWqJzYkCfso4xrBW2lkrMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رگبار و رعدوبرق در راه شمال و جنوب کشور
🔹
هواشناسی: درپی فعالیت سامانهٔ بارشی در بخش‌هایی از شمال‌غرب، سواحل دریای خزر و دامنه‌های البرز، امروز و فردا در این مناطق رگبار باران، رعدوبرق و وزش باد شدید موقت پیش‌بینی می‌شود.
🔹
همچنین در ۵ روز آینده، جنوب کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان با رگبار، رعدوبرق و وزش باد شدید موقت مواجه خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/461503" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فدراسیون فوتبال ۲۰۰۰ دلار جریمه شد
🔹
کنفدراسیون فوتبال آسیا، فدراسیون فوتبال ایران را به‌دلیل تأخیر در درخواست مجوز دیدار دوستانهٔ پرسپولیس مقابل آلانیا اسپور ترکیه، ۱۰۰۰ دلار جریمه کرد.
🔹
فدراسیون همچنین به‌دلیل ارسال دیرهنگام درخواست مجوز بازی دوستانهٔ تیم امید ایران مقابل کایسری‌اسپور ترکیه، ۱۰۰۰ دلار دیگر جریمه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/461502" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsZosIjsA5xmuYTBgi4VINChbKd46GEtk7K6rEtu9ZuWy2BQdvsk7L5rsGfnaBeLklbRIP6CL0vmIGVkVOWLyZg3zLQZxvEBxO7uRNYJB62BeX9Pmk2ItwvVeH5_ezuc5uxnRi95zjp0245uyIResHajPAbueQg28_GG4ildUIIRzSWfFRrnFXj9O7q6LJJ18f5SzH1X6n1MxcvQYWexx-i6F7zQhUMtFO_9Ncs-LIjTjfbi4Eej_eFCHy2CUdHNTPIrjNV0_X9nsii-ZfIb0uFHP_0tMhROtvyp5B9DB7vWDSpJYYs3YpQEBfuOOgEtJntXc9c2B7MO17Bg9FMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ سردار سیدمجید موسوی به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان هوافضای سپاه هدیه کردند
🔹
فرمانده نیروی هوافضای سپاه در پاسخ به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان این نیرو هدیه کردند، نوشت: برای بنده و هم‌رزمانم در نیروی هوافضا جای بسی افتخار است که جان‌فدای ملت بزرگ و عزت‌مندی هستیم که همچون شما گرامیان را در دل خود جا داده است.
🔹
هدیهٔ شما برکت و مایهٔ ریزش لطف الهی در بدنهٔ سازمان ما و ان‌شاءالله موجب خیر در زندگی مؤمنانه و انقلابی شما شود. ممنون لطف شما هستم.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461500" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkc5nXjOakdzRzM3Q9PCJvncoQffu88WxGYg1Bn2X1JUIi8tEyhIHpxUAKQIjIPQJUBoxwwUfWiaKkxTU93Q7sY52tNLzTfrfP95Rl7c7ZTAASxNkdTChcFnC64v8oEXhitT69tMsK-tMsVJyTe9ynSBRKZ1JSAN9QcCCLq6jrq031hyFjX_oor49r7FVa9KA7eRCu1iiUV_zfX_ztX6umj_iSoTF85kwvWC7ebQEhxxEXNsenV_d_mXY9LCxDWhftssb2eGOxEMsgSdYo_igAPnuM-GhdUiPj0S4FTGZyEGPjceYjRPShBG7TvtskEj_orFtS2dcLa7Xq_h08LHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور آموزش دهد و این مطالب نیز در قالب انیمیشن‌های کوتاه، کمتر از ۳ دقیقه، تولید شود؛ چراکه به‎گفتهٔ او «ذهن شهید رئیسی فرّار است».
🔸
گفتنی‌ است میانگین رشد اقتصادی ایران در ۳ سال پایانی دولت دوازدهم منفی ۲.۰۵ درصد بود، اما رشد اقتصادی کشور در سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ به‌ترتیب به ۵.۶، ۵ و نزدیک به ۶ درصد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461499" target="_blank">📅 10:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461498">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دانِ خوابالو» روی «جویِ خواب‌آلود» را سفید کرد
🔹
پس‌از انتشار تصاویر جدید از ترامپ در حال چرت‌زدن در یک دیدار رسمی، منتقدان با اشاره به لقب «جویِ خواب‌آلود» که او در اشاره به بایدن به‌کار می‌برد، خودش را «دانِ خوابالو» نامیدند.
🔹
انصاری، عضو دموکرات مجلس…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461498" target="_blank">📅 10:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cute8aj7UHyEIIeOJ5sZ6h19iKek7wMDw-7TIaRF3oof8uS7hTKV_ZmQp4dfsJNJi6cUDwB6Hl1UOb5UIw-I14lUATKCWcDJh3u_Lc-FIK3Z0pnq3DMzSbz5NsNfMKFVF8Y4AEWjJ0J33O_ADbPxoyf7kSXNo1jh2805QL9gNSPTnKXwikXMtJnrha4pa42JkiJDS6JM-odTn4hHeb3cwDyPYMjpYPLj13ivSg6qpphy5WJBGchsH1T12FhRWmxd66R5JIxScBm-D2HxsBpkxB6kltf6FIuuSihT5BfNF_zkvUBRp2GRbYd2BupHpwcyJbvCReqxNS0URp2lvjbejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2xO-cnBxWSriglBh9W0XQp65SC9NoVDL5euDbSIlWtHuJyG-SxcEv6iGjfTaFvfxozibZv-g309E-70BheCiU-bE_WgkK95h9LfzZoJfBUo0e7V6HpWpqUagLDh4r9LfpCI4ekY228_cMaAuwqbqiTiK44nO0NdAIZ1X2SFmPvJxaZxSTCWXMhhLq6Ks_QyOCDM4CfFjyZ74Fn55WpfI8lWC7DUtBEAWqasQ0fRzkKjfXPhshIp2MpuNxC4iamKdq-uMqUG8CiTZ92EGOITzhjgKDmOtyNdO2o6DoGbwr7kSfV9_ZJf7jfVOuW3OXUfN_4LBA8pRDj17yD4hwDc3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند با قُلدری مردم ایران را وادار به تسلیم کند می‌خواهد کاری کند که مردم به‌خاطر نبود معیشت و امکانات تسلیم شوند اما مردم ایران تسلیم نخواهند شد
🔹
اگر این‌ها مرد جنگ هستند با نظامیان بجنگند؛ با نان و معیشت و زیرساخت مردم چکار دارند؟…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461496" target="_blank">📅 09:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461495" target="_blank">📅 09:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htw4lvDkTDPunljnz8-zXNqi9MYnDtQNrhHjpz3L9glbNCWvmdXPiXvqrPu4AE6ZcBROCEJ1SbxBaH0bkY0LA2Z10-OwtpNZ0h-dxUbT_9s5YJnj24QHWVmrGkxCRCyisESWR8jdwtJjyTjSRPmqzLGqj3SpdX4iYJkwxxqHCs0ZPWAPN65R8yGEn5GkIaJM7GPtFlCFSTd3_pIhkOVTnxMsV--ed5FbOkf4cUaoXIoXuvFWWz8xt0sv7e_OXBER5nQzhnSbBVRAF9IRmSMyuox2P_zvCFW6QMqGHG047PPivq51oiWAkKO-Rfpl7B79rxsNE1UOn-hsfVjQb7S-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461494" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdrp4gK-RYb1r-s1QNVvNFaw56X24OW3gVhhAKnj9FBozrhm3bCxBJYYInJPVYZlphC7NHOHde8cSgboPBvdazzRbR19PJX88EH_nNWspuYw6Qe26LPS7O--IF0AMbsR_PUgeDh0_dz6FQiF25Z024WySKoD8U4bZRxumQoT0WuHbWXj5nAUrAMj6YQDdgaCpK_FW3PsSFD6Ku_AugYUYACeCRDv8933TTty1KggVi-QGcXraN8Z4A3-8s3eJ4G20TYtiSJNFJDTKvEbq5QQOIWEr0N8lOzv-CH9Rt9fdGPFWCSEKpn5mPEyvjVafmNU0NQDQ7OzoR5YOUsMazs-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۶۳،۴۱۳ تومان
🔹
یورو: ۱۸۹،۶۰۱ تومان
🔹
درهم: ۴۴،۴۹۶ تومان
🔹
یوآن: ۲۴،۳۶۴ تومان
🔹
روبل: ۱،۹۳۹ تومان
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461493" target="_blank">📅 09:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرماندار مهران: مرز مهران باز است و تردد در بخش‌های مسافری و تجاری در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461492" target="_blank">📅 09:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461491" target="_blank">📅 09:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvcugz3jTnSiiAnENvx9DlQqr5nCH4fkQo6cOWsFcy20tyyDYc65f89nThBQxQDGKeNYFf6Xov9gKuH_-Sfsp1hJSzlBVWbLj5gLqj4mv4AcVD39BV1aUlV6TH8MaeOqH3kX0CHL07UyT-o4X_bEUBaDUQJ4FAbB4Q-mdcu1DUH7eLxOfu5HOzFeewsr9_1xj3_oPHEfk7jAglD_jHXdZ2dt6I7h2DdUAMmzZYMG0C6CW18IxQQ55VLQnpVAbpTsEoFY4MdcPV82KNlM-MtQOxZEf__Gki08QNKyxfGRPt6zMON68m23q_Isg0BpRbXefgWfrbop-QrHByUVPQTBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461490" target="_blank">📅 08:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان آغاز شده است.
🔹
گزارش‌های اولیه از زخمی‌شدن و هلاکت تعدادی از اعضای این مقر در جریان این درگیری حکایت دارد. در حال حاضر تلاش برای دستگیری عوامل و پاکسازی نهایی این مقر در سراوان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461489" target="_blank">📅 08:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/461488" target="_blank">📅 07:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ضربۀ ایران به زنجیرۀ پشتیبانی هوایی آمریکا
🔹
ضربات اولیۀ ایران به پایگاه‌های نزدیک به خاک خود طی جنگ تحمیلی ۴۰ روزه مثل قطر، کویت و شرق عربستان که فاصله کمتر از ۶۰۰ تا ۷۰۰ کیلومتر از مرزهای ایران داشتند، این پایگاه‌ها را به‌شدت آسیب‌پذیر کرده بود.
🔹
اما کاهش چشمگیر توان رزمی این پایگاه‌ها، فرماندهی آمریکا را به چاره‌ای اساسی کشاند: عقب‌نشینی تاکتیکی به عمق بیابان. بدین‌ترتیب، مهم‌ترین تجهیزات هوایی و پدافندی به دو پایگاه دوردست الخرج در عربستان و الازرق در اردن منتقل شدند.
🔹
با انتقال دارایی‌ها به این دو پایگاه، یک واقعیت تازه شکل گرفت: تراکم بی‌سابقۀ سامانه‌های پدافندی و لایه‌های متعدد دفاع هوایی در اطراف الخرج و الازرق، آسمان منطقه را به یکی از امن‌ترین حریم‌های هوایی تبدیل کرد.
🔹
شبکۀ هوایی جدید، ترکیبی از پرنده‌های بدون سرنشین مانند MQ-9 و MQ-4 و همچنین پرنده‌های شناسایی رژیم صهیونیستی و از سوی دیگر، هواپیماهای سرنشین‌دار از انواع E-11، E-3 و E-2D بود.
🔹
اما در میانۀ این بن‌بست تاکتیکی، یک تغییر رویکرد همه‌چیز را دگرگون کرد. به‌جای تمرکز بر انهدام مستقیم سکوهای پرتاب، تیم‌های اطلاعاتی و عملیات ایران تصمیم گرفتند شبکۀ پشتیبانی و زنجیرۀ سوخت‌رسانی پایگاه‌های دوردست را هدف قرار دهند.
🔹
منطق این تصمیم ساده اما هوشمندانه بود: با وجود مسافت طولانی، جنگنده‌ها و آواکس‌های مستقر در الخرج و الازرق برای ادامۀ مأموریت‌های خود به سوخت‌رسانی هوایی وابسته بودند.
🔹
عملیات ترکیبی آغاز شد. در این بازۀ زمانی محدود، چندین پهپاد و موشک، هم‌زمان با یکدیگر، نقاط مختلف این زنجیره را هدف گرفتند.
🔹
نتیجه فراتر از پیش‌بینی‌های اولیه بود. هفت فروند سوخت‌رسان نظامی آسیب جدی دیدند که از میان آن‌ها، دو فروند به‌طور کامل منهدم شدند و لاشۀ آن‌ها در بیابان به‌جای ماند.
🔹
دست‌کم یک سامانۀ پدافندی تاد که از گران‌قیمت‌ترین و حساس‌ترین تجهیزات ضدموشکی به شمار می‌رود، به‌کلی از کار افتاد و منهدم شد. یک فروند آواکس دیگر نیز در جریان همان موج هدف قرار گرفت و سقوط کرد.
🔹
مرکز تعمیر و کنترل سوخت‌رسان‌ها که نقش حیاتی در تداوم عملیات هوایی ایفا می‌کرد، به‌شدت آسیب دید و عملاً از مدار خارج شد. حتی ساختمان‌های اسکان نیروهای آمریکایی نیز در این حملات تخریب شدند یا دچار خسارت قابل توجهی شدند که نشان از دقت بالا و شناخت کامل از موقعیت‌های حساس داشت.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/461487" target="_blank">📅 07:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۷، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461486" target="_blank">📅 07:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض رباتی!
🔹
حدود ۳۰ ربات در مقابل ساختمان وزارت امور دیجیتال لهستان در ورشو تجمع کردند و خواستار نظارت و قانون‌گذاری بیشتر در حوزۀ هوش مصنوعی شدند.
🔹
این تجمع با شعارهایی در حمایت از تدوین قوانین برای هوش مصنوعی برگزار شد و نگرانی دربارۀ پیامدهای گسترش فناوری‌های خودکار و تأثیر آنها بر بازار کار را برجسته کرد.
🔸
حضور ربات‌ها در این اعتراض، اقدامی نمادین برای جلب توجه افکار عمومی به بحث تنظیم‌گری هوش مصنوعی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/461485" target="_blank">📅 06:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwvvQXl6TRZH07-ExXUMEwJyba-PAKhJRJ1sgRtw-ST8U6DH4ZRHlQ3Ka-1QHPd0ojiPpCohO2uolIpAJW_xCewX5IOcqyEtkHAQujGmAzb5ULWHaa_bU9_48YK6-r3gpsSCn-b6uM67KWuE1U_bsLGNRfi1kS3CZ4v2FedBBiFCnecptgAk8mZNmRoeAFvRz5XhTgyEY4TcwCvfzP3Bf6KvPHVbh479O7c_KlDmFgQE_9oIPC7JYhuxunQOh_UcIfgUsH-oa0Xa4qYGRGITBKeSxYp-FFdj108CIgwa-1fifF3It_FRXl5RWAoNkPGURytGaoMArMK3vIvWWa6JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس انرژی اتمی: کرۀشمالی یک مجتمع غنی‌سازی جدید راه‌اندازی کرده است
🔹
آژانس بین‌المللی انرژی اتمی اعلام کرد، کرۀشمالی یک تأسیسات جدید غنی‌سازی اورانیوم در مجتمع هسته‌ای یونگ‌بیون ساخته است که می‌تواند ظرفیت استقرار حداکثر ۲۸ آبشار سانتریفیوژ را داشته باشد.
🔹
آژانس تأکید کرد که برای رصد فعالیت‌های هسته‌ای کرۀشمالی از تصاویر ماهواره‌ای و اطلاعات منابع باز استفاده کرده است، چرا که این نهاد از سال ۲۰۰۹ هیچ بازرس مستقیمی در کرۀشمالی نداشته است.
🔹
کرۀشمالی بارها اعلام کرده که جایگاه این کشور به‌عنوان یک دولت دارندۀ سلاح هسته‌ای «برگشت‌ناپذیر» است و آژانس حق دخالت در امور داخلی یک کشور هسته‌ای خارج از پیمان NPT را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461484" target="_blank">📅 05:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBINGIHpCtsbPRoM0vdhY6Hqu6X-TpVSYjD_c6oqHzMR9faWnof90D98nOy8b4EJNtTgOONRdJ0Aa1SWGJQ15WercaO5-hQioRWkqVoB7m-bl3bEMMg5RkW-kKVg45FGN8PShysZw_3RuOcDzIwhAB6ROtNArkN6s6AqqnqpcCtozzPP_TxCZoJ_pQcvx-R0b1J5Bu4v-y0vtk2n3i1V-BZvK5wouR1-aCTAZ8TCaMro9-JR0LIcR2GezcI7dR-AwmsnKR2o4Z5ceNT6Yc_fB26XvmCrwc_abXIb2540RM90myN6K3vhkokSw3TU0RmbAuaWmyqK7-Mp-qNTxyolXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی برای یک پروندۀ قتل شاهد ساخت
🔹
یک وکیل مدافع در نیومکزیکو برای تهیۀ لایحۀ تجدیدنظر از چت‌جی‌پی‌تی استفاده کرد، اما بخشی از اطلاعات تولیدشده شامل شهادت پلیس و شاهدانی بود که هرگز وجود نداشتند.
🔹
دادگاه عالی نیومکزیکو این وکیل را به‌دلیل ارائۀ اطلاعات جعلی، ۵ هزار دلار جریمه و به بی‌احترامی به دادگاه محکوم کرد.
🔹
وکیل گفته بود تصور می‌کرد چت‌جی‌پی‌تی یک خلاصۀ «ضدخطا» از پرونده ارائه می‌کند و از توانایی هوش مصنوعی برای ساختن اطلاعات نادرست اطلاع کافی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461483" target="_blank">📅 04:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی دقیق روسیه به نیروها و تجهیزات اوکراینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461482" target="_blank">📅 03:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خواهی کارهایت درست شود؟
🎙
آیت‌الله مجتهدی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461481" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌ ینبع عربستان متروکه شد
🔹
بارگیری نفت از پایانۀ ینبع عربستان واقع در دریای سرخ صفر شد.
🔹
خط لولۀ ینبع یکی از خطوط دورزن تنگۀ هرمز است که مهم‌ترین سهم در عبور نفت حین جنگ ایران و آمریکا را برعهده داشت.
🔸
روز گذشته انصارالله یمن به خط لولۀ تغذیۀ پایانۀ ینبع…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461480" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW-Pih1aRMHSlttaYn-NJjgilLE3CVckE082EeWYvp4RSMW6u65QHPMAg104_GHdnYrKXP_Dq_VIgcawX7ryeXq1hyq9guWlEzanHnI_4eF5s-C72iFlwl5hZhC0MmNhNkrbbHPNo6-hAy8xJ0GUYPgzKjck7EYeDjzuJQGDZv1XvN9a_-h9D4qVCnk2aPMPb3fnzQyorDVvUml1Wwodf81hNik6MyUBel9Zv3iVzgFqxZjduziLEGYTa2Y8n9yJtxn8zWpO_iuWh_NSfm1LZP8GlqiTb_ngc9NfoOkNg_br4nCqCXk-H2HFPilDfy51waI5FA8IGqDp88STy8mNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m17RUL0yR9S4JE3TJZPQtcKUiROH9YAihv3Hf3BJlZmhqKT3U_H3U7BpMRorJ84c7r-3NF78pb65txhd0fvSl7XEi_Cn1qACRYfWIkM2SchC9XlwS4d0RlmrZJjFfF-wVaoymUyL4IS6JSCg8o1mqEOsNvisDXS2D1ogsW-oI3XIAnYk8b2qZ7NdJFKh6oWx8qloCx18rgSbIJcA5BP7b7Udz5O9T6fNpn8zyEVWpIb1EBIYzHRs2Av2jKyGZjsCIU-U2w-GnFgmEXlBwrRCRqbyNSQkJvIsGs-kOzq7V4lApQijnYb5TcTRwuUTKpghmEkEPHf9ulb3PCu8Xwf7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vx6oKBX2t7uL66nxUaAtpu2YnCm4f8vK3Y00ZA3GPU38kRW8TWKstxvfaEs6_iXCAb-Po8LFK8DwQxUl8E1kMB-7nvDqjwwQ0GpX_VLAUmAatFO6FsLarrVkqpqLYSIJktzRFNZ6MHiSNXY5z0pl-TQev2vx_Xj8Qyyrv4WuQOwnbmFw5DLR8Lms56ezyq6ySivMGY8ppajzRzamJvYEaOCz2R5pcYvIoHjkk-tmDaBo21Q7Geb3Cu-9byhe8-LBqXdLm9ZnpPc4eV2Yg7lD0D6j-U96hw4lAnARmE12iGyh1EtnFtvrOf1rk5Tw7v_ohJVxSEyuWPunvIjDZv6Yww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grcHF5bszEqK3W3Pqf5AyxcoM4KuZn_ufaUMtQhj-h2YsytW8ubzhfEz8-pYEfcfnZtShZFQH4AnfGr8fvcjQQiWDWW4Iu-AXA5WdjVK7ZmusQuYiP9Qm_nu0pyKCcEo42Od7nTsWZa0QTz4KFnNhT90ALoefT9RFBqdmpl1GdTGFQS9QpULARdtwCMTk-mkZjimrdyWaKNXzt8487t_o4LOAvzi1l8UvytvdomO2DlxG4PLG4GEdgRNBc9Dyzt3hQR-eNgfdFjloY4Gos2QlMxSTnBwQDm2CR3xPkUu32YrDTzNLWzoAYe2mSCppWLs8pb91iEfT1WZlt35S042cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVn_6HZ6gwgFHmAOukOCeLE1PNhkXA2sg5XPVvVu8YUEmMM5DnMtq8U-JVTqi-9GXTUcgpTZEqxeaf3UnI1U60mpX9dr0muH5jq1Je4ZYUvaN5wcJE50bt6HdGb5Zc0bNGuN1Sk1jF2M9LAUzBkbV5W_4HXBcjmE8FJ0ZC4dKEyO4rCzm65gkQVA_iPckt4_Z4wD2gqkszCP1OGk-3vCcy1V7LOtn1BG1MOSkFy6cS8KGPwYSIU7Jh5qltDKQFkSEwY_v1I3NUsaoZfUsqHd7aT_cl3gefhPXtWrYnUxHMstRGmJMIoyAp68OLE-AtogLRK_NB3JoCPfuFNu9Q12JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUKO2K4I5ZEGHjv7YN2pcX9YY0Ec_3jjg1VeWbwCUUhh2MKdLdsXQ9SyORKZCwn0Fewh3vbZBUmY67hn6EvNf5BmudqMQpdKXEqEHRJTKwcOZgn2dsonEVo8R9NibrS7mOOX9ZEHrRlB3Ft7cJaciRI-KRj44tJTCi5HK-itvlEuwYNHCzPO0BlrhZygFFszbZFVU6koAP5BFcfpoSBKBvKfZtDopJAFcztKvLd96g9T2olo8DJdTBhVCWRtMJLdJ8FVIEFl5hPqQeNMV243tp06auhX3k5SSDJO0n3ZQHtdVIBpaU1Nw1LCNeSHQbh-8uqHUqWe2T0ncwSVRrsWCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان‌داری مردم تهران در میدان انقلاب اسلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/461474" target="_blank">📅 02:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdtxmQeHUbcl3cKEay7FSTf0noQW39NCbOnsgLQQ_n3SC764SvwJsFpYCJ0nzZAoDf4kgGGTvREu5ozd30f9Zc8dQlkj9ifw55rR6EFfb9gCAUzf1kOf5GbbhzBbXCUHNM_ZftMTTaezbtcp6Gsf6kAOp5Rr_WYMP_v1xRnvWcd3R86uKuE3pXm8H832RT2vkvmTmBWrXICtnSwHzrou71cgqdtXf2M8v4CTEQGgvG67K4Bs7neY-s6Ve0YLw5n0nyrnRsd1lDgV--SrGWDlyXVDqUzV7mz9MjJuU01y2YFynHSuO18FIeL0yUrRtk28k2yZSjnhrCAlSsTZE4qpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت اطلاعاتی آمریکا از عربستان در یمن
🔹
شبکۀ ای‌بی‌سی نیوز گزارش داد، دولت ترامپ در حال ارائۀ حمایت‌های قابل‌توجه اطلاعاتی و کمک در زمینۀ شناسایی و تعیین اهداف نظامی به عربستان سعودی است؛ اما فعلاً برنامه‌ای برای انجام حملات مستقیم علیه نیروهای انصارالله در یمن ندارد.
🔹
دو مقام آمریکایی در گفت‌وگو با این شبکه اعلام کردند که رویکرد دولت ترامپ ممکن است تغییر کند؛ به‌ویژه اگر تهدید علیه خطوط کشتیرانی در دریای سرخ به شکل قابل‌توجهی افزایش یابد.
🔹
به گفتۀ یکی از این مقام‌ها، محمد بن‌سلمان روز پنجشنبه دوبار با ترامپ گفت‌وگو کرده و در این تماس‌ها خواستار مداخلۀ نظامی مستقیم آمریکا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461473" target="_blank">📅 01:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461468">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHntnY9PaDwX_i7kciVK7CWOG3KPacSGkpInGrTM1XTlQoSEgY9YCWEFgPERcENcmpcWmoWjBc7QYvT-9ZGaziRdoIYjxSw9jw0VBODwCP-OSq8c_qcISXP8faGS5MSaEPwmvFpJprE78Rvo5ANurbPv5-DJFfe7JJZkxaWWszrQrlXulA8CNHvfv6FN_3rk7rgCxuMXeQ6NEs2nZA4TElHUjz2eZ1rOnMm08JMwYNjubXwEExQd09m_gZ-vTWnIzabcGyIoceCmVyi9uect3BnwAXSGHnnw1psaNhh0mqUkQZxhS0tPY8feDtFTzkvx1A8UdPnyv93yHfba02YyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce1J8U5EtHKdne4Cd9uD-jbDw2fmL7pUfUcU1kz1myIynHbeYXKX6U4hldkq8vKjof567cFwdSUwTF5NAJA_ubKf0lhU6xja8P074kfHPTIgFyGMBH-iGwekXqdxyQDJeY1F6S47qlO7zJjRK3taWls9fk4-q_CRxEBhTnIpLNLQ46Oeq3GVVYcUSngtnKc3CwMKQJ2FXSd2lDtV8fShAe61Sfri11lAbUTc-mRtuKL3CfHdEihLUezuLQytO9x53Bjk79Gibz6QHN4z6f_FYUT1WyXMLzS_MU3Q40l9wBhDv3fE_WXMuAfL39kv6grbL6_NtleKz3exOgGk2MLW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vj94lLT6QWEcBNgJG-gI_d37tZ7zt0Vcbex5DdpnpA7E8-hDBYpQOUdg5Mx_jggSwyBPOSRWjTCnmAxU13oAX7ZHTwNKqEnUgkFDXvL6ymd58Lx95pl5le37dJX-gHo_Z12JEa317C-PpiZdrP72ZSKnjAXG7xgLk9tQKQedTJjsZpnDf_fahjhf1aoNSzTFJUnLImJDm2rD9abwG7pigs8xeDgJ1FShUatgXh4L9FAxlcXNOv4xgEfz12Vxt62-s0YzAU7Hx0Z6vGoQILuKnSYDfZEebl4OcvdBBZFA8PzvqhYSpYybHoKyQXsM3ONHUxjNYX94BDCMi4OD0r3sZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0lNBt12HKIe6la3qViwHrIBqKft1zzP55czzY2bwITfdB7bKpDGopSvUF8wW62PPNslgQMawcnl5WhOCaIhGcuynUOF1Ew2CQ3B4oSj8HkYV60m5M7-HgwOdBUl9WYT2yDn_NEDrfGUxBQykIvKj7I7cGuUIq4TxyY0DF59z1YvRbOvgIHj5mF4sACw3SOc3BQv-sc28MVSlZWmkI4q5DYRqOZJnaYj0MxajZZCzgLvImLIKxehVDunvmPXV2p2L0w8K2NJc9I-QqjGXoHR_DApUZLYahly0gTKSoLeGSzpxkvS8wU7JpPmEEU1IwJ6V_DyScyNPcQanslAXxPShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QneU9sgO2ZBxdbYeKVofqFB-oS9ZwG8FF5fpA7I-QbBj97VHmdUSLNDh_1rikg58bkILKxMqAbweEPPMn21BStL5dqYIQhni1AsCkrfBIzyMIqcf5_lQGGlzGvdQtgZjB7Q8NaUaCd9l-uOa4by9q9C9Fz2cYAinbuGCsY8ykK19qc3h6qe-HQk7dZi5ySnLegNl2_-Y11Wz-rlOcgy0BiUasNih6NjagbZMPraOPlU0m60ciGX6mdsuWNknWpo_sfDc0pQ2rp1OZ4w0oBUAHTgvXRJrCbaH2ZEfuz0psiis1fsOY_tx3iSN0_eB7PWT7K0-o1fnPRK392k-GGRTFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۱ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461468" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461458">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7VgoCkUQkyymGrHEEWI289XPqNGAMPm1i6sqxsE5z7On0gyS8ZuSLWHb-XSYr_rrsDqYLbulTJTE5mC8uk3FJEdmhx8oiUQr-mSlYXndx8JRGmS3-T7-OMRbK5zNIguW_XZ2SeiDatf_EtzNgS2ogwyIBabd2y_CrCRmvPx4XLXDswFxDutkAYQZnWhcDLF5ET5-lfgXvU0wCGLDhbEF9H-0LPu6VkloNeK8kS1tclN8fFdvDxIHF-KP13EAR4ip0XEaj0yXz3F853qQf5hx9SgQ8a6VSVsM5Qsigut0INxFNhhV_YUUBxJ07jc_riAbnYEgcdN6k3ftH-Vq-OgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKekRnBcQwXmsRynLqp9NjYheBW5bZ4AFNYrab60QMtyLBWwQiLi2awOzEnUTEAfFBOD6azl2RnPDWVnQVeY7kErBydLkGa_Lg0W7B7ek1DNKXXdBAxu8IHfuW1QcL3XiFxe6VGQHiS5r4ATpNyIdROu1ATg1absRUaxP0tx9dayE1R67_DfkL9Qbxf_ZL1DbzhauVbscbiFIuUFi3KyjzuFGsjCAe2xT5YRJtY1DURUTUuNsaLyTreWuYZp88t4P4Um3MFzqV37XUVoJA3Y-DuUClB2rd_rqiKIh2_wifkh_UG5TVYX0TV5_hGq61uGVICEoravddAvavKgxtx57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_J588d5udLy1XiaizfvNyEWwwqeXZZgZGdhn2-0miY1TnV4UVa0_L44GkyQTMRZ9WlXw1VuzTtVhmX7I0XPH0JfbC0soRCjg-0UWIxh6tdxbWsIkddSmY_SyJSGRnw7L1Hig0YUQ-dl0q_pl8ocsDy6cUhbLUQ70HSC72CIKSSyqTdaYecUP55v5c_t6EyI4llzqDEaQToxcDsJF7hJiIQQ-G7JRBz-HR16NBIjFhEcmX4YVLfMBIwQpHHEdhOzoAD4G1gBV7phjad88xRhf-NfBq0KSmLjL7GyQkvTaEO7lrjqrAzuAd2cBhggGUwyQcOqyHM6eUry88iKpa4mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keKFRdbaa3eb46p7NgPX5S9mk-0D2pUYMDMGeHbKc-aCjxsGqG-L_GgOwZRNipRv3ytjBB3g0bvP-muHL99YZDSb_vYBUJ9XcGWQVWLy03cSajBFPLh-UVxNJXUbcZ_C6QT_kT-PQRBdSnKg8IqmP79K9FuZpqaQTXs83qhe27hJE6EuoOYMzvFhBwj7ykDMIt5uApgTjiuFIXJMygoRXyB1bldupFDrMZSUwz1xuBzvj3QvC2O-_0jwPP1YsEWgnvihtyzYrZjwY8kHjgwLPeg4-y-ggytFO3wxkfz7R2EspIgca3xTpxStUjiy4nJhwy08PAs2a072QJxh7rF4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeAySWeSH0vddlkVRp-DWT5MiS17XbzRTvMMf9yx8gDjfAchd0CRFoC-Hg5rWadVDecqWKE0sqt086OrV_V6j2AMG2nobl7IqynZql0ktdrM0o-h8_A09_IW3yHP3WiXWUIZL7ui3Mq2iEYBRd8gqz4jMzrU-Yox22cJjOVeMhEYTP9Cmd-rEw4-8uu7snIy7y5l72h9cOIp4m4_XUeEWLN-9xrkF8BF1dqkHY516tz2NEXiNIlWh8M_-ZoOvFiP-eVwun8Jes7zV0F_lsA9CQfx5I7gT4CPDobyFc4paUZ58JMZx2qoTYJdReGK_uW3dzL9eyd6TbqsXz_5nNW65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGME0P7RfzztRyMQddHTMfSUz0YRmSQZ8vNLzcnc9vw_BhqrEZTP76ducW8DwvT8YPo6psNgx93YjY_F_Jq8J81wUfwrVqUvkWcPr9_c80Y9CAbZilBHx77OnGptI93_2QUKPk0hf2lb9BddJeb05QV-bmnE_cKQjzLb7rju1QWUDV22T_c5uw6OKRFZSI2EHmXBD6lvwrPykt6ItPMW5z07SnCVv7xw-NiXJf7Sc31wnG9NF2nD51tPmWO-6R7EnTbLCp-bew-JKzaWSaOZtaVQhcqXMiLBnRSDmF4UZjmD-iH6rHjiXr53heAWuQ5LWJpgfVC3QPUJaVCVd3QXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DClk8yjt1hHxsoCQCpEIF9XiOndZB6WBaabNAU1b_XIgH7eFlWJNWDLFviKb2ArW7MpzHCauMRgEmxYCgocVZT-lo_6Vog7QcevjYAuQp1YAaubxPQhAqXKVQXbVvAP5yQS0PTww4O3_vfIUZWKuSerqgXm2-KmxEY7vNtx1OZcE3nV-2f192AkcQk9FhjaYpYJEahaxdf8lPzwYisPvVM_IPR044BSlaDBL1cnSpQKKIh0xHUbr0LM6HWXNAx3zD3JzwEyM4tMdZQ_pljg0_9Qfy4OrhZks5OvrqZYdIiqMun-ZEoryb63y6-IOvZIEp9dUQ78QyBBI1Ht1vKxUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UO125AEdGryQnC7Fb_LVVyhw45f3MnHJSHyF3gxGfjj23mwLRL41-4KE0mqE2jeNAzCjpxxPIlaPBj7Zre56ktrhB6RhsBnDxlxR4X1vRqmi9H-X0daItu4GiqXMiSUR4YjVYuL5gNyeacGPskKcLXQNpkey7BsoSy9i07dy6bMl-g3ZPVdT71bIQVBGIX4v7sJfCrRaH7CVxkwks3yhIDWKHCiLOX31kE12IBtG34yw7fxW0ZCrWH1RWtxMu0M0AiDWLPwnYwRZOseSfFwWhVhhp3SzGkSdT5A3c_qsb7tauhzK6PMoHm-D6LK5U24mcG1utsxpQhxKe11TCv2clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDLGq5izISk7wUkaqgVnEf0d6mkZ1xO369ZFMf4_AZUqYvc26tLfUKXL7xPSATxeWNw9xO3fo7C2-RYrWPuBSB13WoF2EUkErEWgD6oGy8uRqhRKULYS85jY2f6xqsOetZSPvAQwfBwHPpD1CcH1cpFt7jjogxa2m9opXISk39kQysX_t_42m_5F4S1YhFm_eyqxA7XRSRrvsUzHsj6fT2SwRG2rzS3IrIrRISII_-dAS80zDf3yh4faLFYqxQ5er8q900P7jdU7M3ageAZuElGw26lZbBCXm6Cb5K2kI0HAvyretTKvxMd9WZ26JQxdN4AhTmXZLoqiyyl6GgITew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRVEFsjDcAd-XF3Gb19dzT4DNjLIv_nubJn5gPfsy2yA11pod33bHcSyB7S0BisXxceinUAoDK4XdfKcie8k4hvBqd8GvAB8fcMEUfVTgRIlYWYuPNJQKP6vdvQMLuzBjRZgdObYLcvA3rHMvZb503r9otIukcd8-3Q4n2wVfoZC-Ig6b6L2z3im4c8zdS4YQT4Mx1fDe8_Hw9zZVhD14hOS3R4CrrvZavGu3ksfqqVHLB5pJmdM3cUkWYWXtP5ldeQDVnP-8u8pR-NymxnrgRly2p8OmXctHEMQlqFJR7xO2KbreBGscCZ7oLm8PJoz5ILvmtOsVPj14ujpKFULUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461458" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhfeY1WHycbWTXAL_aval-f3LKsiIgUGv61BqHjr5Wqj7YG38qRDwpBGxYj3aJisx5TeJ6T7FwVtB7BLQtfOCZihDS-Q5wbPlck6MnYvie2rCPB0O5AqLb475jU1PVkzJ4JHcaRzBMcey5qkF-jc5YqFsuCdgRJD4RFLdrAugZWy_RHuFYejZTLkx7BavIGrK_0XleC2xROJ5Re3D_4jzZQHLGE6XNB6xELWpSjkeYOaXC6KFpDBY3gOh27AVCK9JHOB69p8dSeFohpBmXoWrdVq2R--rdX-Rg35n19WtCA42VgZnjR8y9-g-Sk3ATb0JwOjDsAO7Rz2zsMZlnBLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکا به‌عنوان مربی و پرورش‌دهندۀ اصلی تروریسم در جهان، فاقد هرگونه صلاحیت برای تعیین معیار دربارۀ تعریف تروریسم است
🔹
سخنگوی وزارت خارجه دربارۀ ادعاهای وزیر جنگ آمریکا راجع به تروریسم و اتهام‌زنی به ایران در این خصوص نوشت: روایت وزیر جنگ آمریکا در سالگرد ۱۱ سپتامبر دربارۀ تروریسم دچار تناقض بنیادین است.
🔹
نمی‌توان جنگ‌افروزی کرد، مرتکب ترورهای وحشیانه شد، به غیرنظامیان حمله کرد و همزمان مدعی مبارزه با تروریسم و تعیین‌کننده تعریف آن بود.
🔹
عاملان ۱۱ سپتامبر ایرانی نبودند؛ بلکه همان کسانی بودند که آمریکا خود آنها را در دهه‌های پیشین سازماندهی کرده و پرورانده بود. پس از ۱۱ سپتامبر نیز آنچه در افغانستان و عراق به نام «جنگ علیه تروریسم» انجام دادید، حاصلی جز کشتار خیل عظیمی از غیرنظامیان بیگناه و ویرانی گسترده در افغانستان و عراق نداشت.
🔹
با این اوصاف، استفاده از سالگرد ۱۱ سپتامبر برای توجیه جنگ تجاوزکارانه علیه ایران، جنگی که با ترور بزدلانه مقامات یک کشور و هدف قرار دادن غیرنظامیان، از جمله زنان و کودکان، همراه بود، تلاشی شرورانه برای مشروعیت‌بخشی به تجاوزی غیرقانونی با استفاده از زبان مبارزه با تروریسم است.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461457" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461456">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">منابع عربی از وقوع انفجار در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461456" target="_blank">📅 01:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461455">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">منابع عربی از وقوع انفجار در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461455" target="_blank">📅 00:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461454">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf4c3kPbHH3iI2qJe4ducLOdWqs3D8DSM_rXE_0ZF66SYoBaTvL_BfIY8LWRziop194Fph-qpxBEr9-zlfJsHWTmUHL7oCZuZfVJ1KGXKD_h3-HXaNuY7GoNOuNJmmcs9FsQQzJbkPgGqfM9T9yP_67S_7nSoxRvbJlYlbAxqTchS3rkZyIVNeUzQihmnLoFGcgsDWw1z0dGg4Yu_kXCxeAeytXgl_77jzUiHmeU05O4bO7fKaiAZ8u055frAA9AiAq4g7QB8BgwbW6BgQyqFSOmz47nClOPsduFOUV37_jMOPrKdPvCPrmg_zQeCZol4z85sVCgRyqOG2OmTMCWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی مشکلی برای همراهی تیمش در لیگ نخبگان آسیا ندارد
🔹
پس از فحاشی‌های خداداد عزیزی علیه امید عالیشاه در پایان بازی تراکتور و گل‌گهر، او با حکم کمیتۀ انضباطی فدراسیون فوتبال چهار ماه از حضور در ورزشگاه‌های کشور محروم و ۲ میلیارد تومان جریمه شد.
🔹
با این حال از آنجایی که حکم عزیزی شامل مسابقات داخلی می‌شود، وی می‌تواند در لیگ نخبگان آسیا شاگردان جواد نکونام را همراهی کند.
🔹
برهمین اساس، عزیزی امروز همراه کاروان تراکتور راهی دبی می‌شود و در بازی با شباب الاهلی در هفتۀ نخست لیگ نخبگان روی نیمکت تیمش حضور خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/461454" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461453">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ عربستان حمله به خط لوله نفتی خود را تأیید کرد
🔹
وزارت انرژی عربستان خبر داد خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه، روز پنجشنبه، هدف حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/461453" target="_blank">📅 00:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461452">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV3-TZduaK25oxQipXHCISxpZ6_-nv41tKtm_8XkIXcFGz0KzDPDf2wWduesanX0CAMyYndrWNiYc_v5pWlhLC9l_FoNfUl4SMMGx0vcDGGhNrqyMoJfdlvRIhsy4yQiVFU01w-9Ip5-VqFTNSMjI6EVZHBsEn3-_-8EYjaEuokBN_3YSg5eSeJS_jDoFVAqELvX-0I_myXj_W1PsejY8FdxlCE5z-lbkGzmRM8sHobK_orSv3I0VTcWIv2l-2R8AoYi4qDoO5bCvWlx7FCPr4OvwPekYQoSV9FujQxcc-MuzHLEFwrk62Xqchute5gw2S8gR0dYCQ9WLolaMtLc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت وزیر سابق نیرو از قدرت مدیریت شهید رئیسی
🔹
علی‌اکبر محرابیان: اخلاص، تواضع، بردباری و مردم‌داری از ویژگی‌های برجستهٔ شهید رئیسی بود، اما نمی‌توان از هوش اقتصادی، حافظه و قدرت مدیریت ایشان نیز به‌سادگی گذشت.
🔹
در جلسات، شهید رئیسی نام پروژه‌ها، اعداد و درصد پیشرفت آن‌ها را به خاطر می‌سپرد و روند اجرای طرح‌ها را تا رسیدن به نتیجه پیگیری می‌کرد.
🔹
یادم هست یک بار در جلسه هیئت دولت، من درباره پیشرفت یک نیروگاه در جنوب کشور توضیح می‌دادم. ایشان وسط صحبت من گفتند: «آقای محرابیان، جلسه قبل گفتی ۴۷ درصد پیشرفت داشت. الان چقدر شده؟»
🔹
من نگاه کردم و دیدم واقعاً ایشان درست به خاطر دارند، گفتم: «الان ۵۳ درصد است.» گفتند: «پس در طول این مدت ۶ درصد پیشرفت داشته‌ایم. برنامه‌ات برای ماه آینده چیست؟ اگر همین روند ادامه پیدا کند، به موقع می‌رسیم؟»
🔹
شهید رئیسی معتقد بود مسئول باید نگران باشد و برای حل مشکلات تلاش کند، اما نباید اجازه دهد این نگرانی به مردم منتقل شود؛ چون اگر مسئول مضطرب باشد، مردم چه کنند؟
🔹
در سفر شهید رئیسی به خوزستان، پروژهٔ آبرسانی غدیر که اجرای آن ۵ سال زمان می‌برد، با پشتیبانی و پیگیری شهید رئیسی به طرحی یک‌ساله تبدیل شد و در نهایت با تأکید او برای کاهش زمان اجرا، این پروژه در ۱۰ ماه به سرانجام رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/461452" target="_blank">📅 23:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461451">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سرپرست وزارت نیروی دریایی آمریکا: ایران پایگاه ما در بحرین را کاملاً ویران و نابود کرد
🔹
عالی‌ترین مقام غیرنظامی نیروی دریایی آمریکا تأیید کرده است که یکی از پایگاه‌های کلیدی نیروی دریایی ایالات متحده در خاورمیانه طی درگیری‌های اخیر در جنگ ایران متحمل خسارات سنگینی شده است.
🔹
هانگ کائو (Hung Cao)، سرپرست وزارت نیروی دریایی آمریکا، در ۹ سپتامبر به نشریه «اپک تایمز» گفت: «آن‌ها بحرین را کاملاً ویران و نابود کردند.»
🔸
منظور او پایگاه پشتیبانی نیروی دریایی در بحرین بود که مقر فرماندهی مرکزی نیروهای دریایی آمریکا و ناوگان پنجم ایالات متحده به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461451" target="_blank">📅 23:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb66bf6c.mp4?token=UQbgf9rCWwVDH4jDz7zevlooGOiqALRcW78RxzmrG3ItoqzEzHjrpaKNGU66cEWH-MkZG9mkMMFqdSlkHHe86-hiLACOYx2olYBYiesBaccofSVVlex0BZ_XpvkGbc1bid1ZI9jU9Y676ep2T3sk_BE5BoBgzNjnAxMA4FuhPvK-lIbuVmBJHl_ALqHHIHXUc0CxKFN4y6tFJnKWSaFsbQHmBwKU5sZd2JHRBPlWpRHuhGYovmeGqRgYw2kMoqsSf0JQZeFupV10uLVM6vXrPky31n33vtV-y5L7zROncEun0QyDcvMVn58RVKgL0C1iIAUeU3D4XDfq0sX_2dCSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb66bf6c.mp4?token=UQbgf9rCWwVDH4jDz7zevlooGOiqALRcW78RxzmrG3ItoqzEzHjrpaKNGU66cEWH-MkZG9mkMMFqdSlkHHe86-hiLACOYx2olYBYiesBaccofSVVlex0BZ_XpvkGbc1bid1ZI9jU9Y676ep2T3sk_BE5BoBgzNjnAxMA4FuhPvK-lIbuVmBJHl_ALqHHIHXUc0CxKFN4y6tFJnKWSaFsbQHmBwKU5sZd2JHRBPlWpRHuhGYovmeGqRgYw2kMoqsSf0JQZeFupV10uLVM6vXrPky31n33vtV-y5L7zROncEun0QyDcvMVn58RVKgL0C1iIAUeU3D4XDfq0sX_2dCSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ سخنگوی وزارت خارجه به انتقادها از برگزاری نشست ایران با کشورهای حاشیهٔ خلیج‌فارس
🔹
بقایی: اینکه دیپلماسی با پشتوانهٔ میدان موفق شده کشورها را به این نتیجه برساند که راه‌حل امنیت منطقه این است که به‌دور از حضور بیگانگان با هم صحبت کنیم، دستاورد کمی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/461450" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461449">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2547a60937.mp4?token=IdlbtY-zrSC6Rief9jHASyg_cDpKeHN5Qiw3yWQW9sn83tc2aRUbTcWZyupMNXAoQsdZPO_Ly2BffPckt2BbERB3NM9W2Nf9nZLg9GKjkCH0PXRy-IH2mMcOnMz5SC6JLohpEduZoufZqtmnX5tP9h3pWNwGNpRUWvzqqveGswRz_HaaGXmWNBHNxC-N23nhx6ct-GjpZa9t_dzAHNHK3FcjCeqw4TsSzDNBC_EPst8hYd4mFedZE6Kl5gHq7j6iXai01Yuhfj2Vpa8-sw-KX3u83xtw0KcgdYRrGLeBFDHgzQTyz2PCL8w0YFaqqbO3QeDA3McKYPM6yKnA_HkKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2547a60937.mp4?token=IdlbtY-zrSC6Rief9jHASyg_cDpKeHN5Qiw3yWQW9sn83tc2aRUbTcWZyupMNXAoQsdZPO_Ly2BffPckt2BbERB3NM9W2Nf9nZLg9GKjkCH0PXRy-IH2mMcOnMz5SC6JLohpEduZoufZqtmnX5tP9h3pWNwGNpRUWvzqqveGswRz_HaaGXmWNBHNxC-N23nhx6ct-GjpZa9t_dzAHNHK3FcjCeqw4TsSzDNBC_EPst8hYd4mFedZE6Kl5gHq7j6iXai01Yuhfj2Vpa8-sw-KX3u83xtw0KcgdYRrGLeBFDHgzQTyz2PCL8w0YFaqqbO3QeDA3McKYPM6yKnA_HkKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461449" target="_blank">📅 23:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461448">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fubw0j-fMllq8hRVeogMT9XPWZgDYvXp7CJGp34ab3fgvOXjfN2aHHO3F16YkoAjIsb5W7s1AWyJ8hAAvbQOR1uv-8DO_BBuBvf_rP7a44Sj6CZqXRR3ixP5ZimGlgWgTZAW0HJYZ8Ccj6pqo8Tr75iwHIyyV9v35lmeu6E2tEZuTzbZ5zWbP_kZRyMCSgfv0XGuAlgAD6NIv_B-94sbQFYxLpnlKKa3yzZKWkBHb2pfnUQ-GSab6URk7LvybynOgrmKEvdm73owY0YHqJSiQOsB4Gtvike1W-Bqhksvxt2mT69KMG5Z42FwrQmbllgM3oLAgtJffZ2Szba3StSalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ خبر امیدوارکننده از ایران در یک قاب
🔹
از کاهش ناترازی برق و توسعه راه‌ها تا بازگشت کارخانه‌ها به تولید، رشد کشاورزی، توسعه خدمات درمانی و موفقیت‌های فرهنگی؛ مجموعه‌ای از خبرهای ۱۱ شهریور نشان می‌دهد بخشی از ظرفیت‌های کشور در مسیر فعال‌شدن و توسعه قرار گرفته است.
۲۰ هزار مگاوات از ناترازی برق کم شد
🔸
وزارت نیرو از کاهش ۲۰ هزار مگاواتی شکاف تولید و مصرف برق خبر داد و هم‌زمان طرح هوشمند «مهتاب» برای هوشمندسازی شبکه برق با استفاده از فناوری‌های نوین و هوش مصنوعی کلید خورد.
۹ کیلومتر دیگر از آزادراه حرم تا حرم افتتاح شد
🔸
۹ کیلومتر از آزادراه حرم تا حرم در محدوده آرادان ـ لاسجرد به بهره‌برداری رسید؛ پروژه‌ای برای افزایش ایمنی و تسهیل تردد در یکی از محورهای مهم زیارتی و ترانزیتی کشور.
نخستین صندوق ارزی بورس در راه است
🔸
پذیره‌نویسی نخستین صندوق ارزی بازار سرمایه از هفته آینده آغاز می‌شود؛ ابزاری برای سرمایه‌گذاری با بازدهی ارزی و حفظ ارزش دارایی‌ها.
تولید برنج ۱۶ درصد افزایش یافت
🔸
تولید برنج کشور با افزایش سطح زیرکشت، بارندگی مناسب و اجرای برنامه‌های فنی به حدود ۲ تا ۲.۲ میلیون تن رسید؛ بیش از ۹۰ درصد محصول نیز برداشت شده است.
کارخانه لبنیات خلخال پس از ۱۰ سال فعال شد
🔸
کارخانه شیر پاستوریزه و لبنیات خلخال پس از یک دهه تعطیلی با سرمایه‌گذاری بخش خصوصی به چرخه تولید بازگشت.
۱۰۴ کیلومتر راه روستایی در جنوب کرمان افتتاح شد
🔸
راهداری جنوب کرمان طی پنج ماه، ۱۰۴ کیلومتر راه روستایی را به بهره‌برداری رساند و عملیات احداث و بازگشایی ۲۵۰ کیلومتر دیگر را با اعتبار ۱۳۵۰ میلیارد تومان دنبال می‌کند.
۶ هزار نفر به خدمات آزمایشگاهی نزدیک‌تر شدند
🔸
با راه‌اندازی واحد آزمایشگاهی سراب قامیش سنندج، حدود ۶ هزار نفر از ساکنان ۱۹ روستای منطقه به خدمات تشخیصی نزدیک محل سکونت دسترسی پیدا کردند.
۲۵۰۰ واحد مسکن ملی وارد بازار اراک می‌شود
🔸
قرار است ۲۵۰۰ واحد مسکن ملی تا مهرماه در اراک تحویل شود؛ اقدامی که به گفته رئیس اتحادیه مشاوران املاک استان مرکزی می‌تواند از فشار تقاضا در بازار اجاره بکاهد.
جایزه بزرگ جشنواره کازان به سینمای ایران رسید
🔸
فیلم «سرزمین فرشته‌ها» ساخته بابک خواجه‌پاشا در بیست‌ودومین جشنواره بین‌المللی فیلم اسلامی کازان روسیه، جایزه بزرگ جشنواره را کسب کرد.
۷ واکسن از ۱۱ واکسن اجباری در داخل تولید می‌شود
🔸
رئیس مؤسسه تحقیقات واکسن و سرم‌سازی رازی اعلام کرد ۷ نمونه از ۱۱ واکسن سبد واکسیناسیون اجباری کشور در داخل تولید می‌شود.
۱۴.۴ کیلومتر از محور شاهرود
-
طرود بهسازی شد
🔸
۱۴.۴ کیلومتر از محور شاهرود-طرود با اعتبار ۴۴۵ میلیارد تومان به بهره‌برداری رسید؛ پروژه‌ای با هدف افزایش ایمنی و کاهش تصادفات.
دستگاه پیشرفته قلب در دزفول به‌کار گرفته شد
🔸
دانشگاه علوم پزشکی دزفول دستگاه «روتابلاتور» را با سرمایه‌گذاری ۱۶۰ میلیارد ریال در بیمارستان بزرگ دزفول راه‌اندازی کرد تا درمان‌های پیشرفته قلبی در شمال خوزستان و مناطق اطراف در دسترس باشد.
توقف کامیون‌ها در مرز جلفا ۷۵ درصد کم شد
🔸
با بازطراحی فرآیند تردد ناوگان سنگین در مرز جلفا، تعداد کامیون‌های متوقف در تیرپارک از ۱۵۰۰ دستگاه به ۴۰۰ دستگاه کاهش یافت.
رتبه نخست داوران به آهنگساز ایرانی رسید
🔸
پویا سرایی، آهنگساز و پژوهشگر موسیقی کلاسیک ایرانی، در نهمین مسابقه بین‌المللی آهنگسازی کارلوسان ویتاله در ایتالیا، رتبه نخست هیئت داوران را به دست آورد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/461448" target="_blank">📅 22:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461447">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550834d17.mp4?token=Ul-HpNb1kJ7-V97ZjPpbVjAlDRtJvw2xdDrPmuccgSpReGsMvMsYboAuQBhjn7VsnkW7vsi8CG8p8bykcgnR4sPhaRAQ-fkUjS5hKXxbgR7ZyqzaOy0QPCllb0mxSWhF9RlhrC1PR817jk22qrnV8QU_BbwZKZodiMUfKmsdADHr-amYWRKOw33h0KqMUmQgCi0cV-GkFKkhbQom_y0XGSdFGUACWKoZFihtVdc-ARJ63UX9HF2byHzV4eeV9g5sj9qEsk2WuH_oY-V-Q8Dgjrj10r_Zuiuds4wwanzewQcr2MKD4HI2y0DraIjXU1YJCDbmm2qXDlioIDuicAwptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550834d17.mp4?token=Ul-HpNb1kJ7-V97ZjPpbVjAlDRtJvw2xdDrPmuccgSpReGsMvMsYboAuQBhjn7VsnkW7vsi8CG8p8bykcgnR4sPhaRAQ-fkUjS5hKXxbgR7ZyqzaOy0QPCllb0mxSWhF9RlhrC1PR817jk22qrnV8QU_BbwZKZodiMUfKmsdADHr-amYWRKOw33h0KqMUmQgCi0cV-GkFKkhbQom_y0XGSdFGUACWKoZFihtVdc-ARJ63UX9HF2byHzV4eeV9g5sj9qEsk2WuH_oY-V-Q8Dgjrj10r_Zuiuds4wwanzewQcr2MKD4HI2y0DraIjXU1YJCDbmm2qXDlioIDuicAwptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: منشا حمله جنایتکارانه آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461447" target="_blank">📅 22:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461446">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2baea5ba.mp4?token=KW1vvOCV9ev1N1uocM04PtX62Zkwh8iX0p546yrlvP4z6s-fArpPOr9O_jagydaomV-L0LpvN-RYy8wbSuTZ1hHq-xEWbBhROI4Cx9EFqRz8OlNThnYdVRHNgBH9J4fsD_pd0uiXBcH3MR8Cs6rngUYXegdav86f6wXwHQPjqX8wl5WEVrDkGJve9Uda-8SnOCbTw-xbdo8o4B4ACVCxaB9wmhfvL4vFpmXg73PJo-C3PEqHy2fynjAa7CbnQgGy3G7JO5CIPXdywxYFn_RYyh763pdJgIh9Ed188vQn1QWpME-TO-sHwPs-LS-bT7TpfQ96Ipik8DZl3XNUaDOvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2baea5ba.mp4?token=KW1vvOCV9ev1N1uocM04PtX62Zkwh8iX0p546yrlvP4z6s-fArpPOr9O_jagydaomV-L0LpvN-RYy8wbSuTZ1hHq-xEWbBhROI4Cx9EFqRz8OlNThnYdVRHNgBH9J4fsD_pd0uiXBcH3MR8Cs6rngUYXegdav86f6wXwHQPjqX8wl5WEVrDkGJve9Uda-8SnOCbTw-xbdo8o4B4ACVCxaB9wmhfvL4vFpmXg73PJo-C3PEqHy2fynjAa7CbnQgGy3G7JO5CIPXdywxYFn_RYyh763pdJgIh9Ed188vQn1QWpME-TO-sHwPs-LS-bT7TpfQ96Ipik8DZl3XNUaDOvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در ۳۰ ثانیه ۷۲۰ هزار ترکش بر سر مردم لامرد ریخت!  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461446" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ما در وضعیت
«
نه‌ جنگ، نه‌ صلح
»
نیستیم؛ ما در وضعیت جنگ هستیم
🔹
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461445" target="_blank">📅 22:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461443">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مدیرعامل بورس تهران:بازگشایی نمادهای سهام عدالت درحال پیگیری است
🔹
سازمان بورس پیگیر برگزاری مجامع سهام عدالت استانی است. در صورت تأیید نهایی دولت و شورای‌عالی بورس، زمینه برای بازگشایی نماد این شرکت‌ها فراهم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461443" target="_blank">📅 22:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461442">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آتش‌سوزی گسترده در مسیر خط لولۀ نفت عربستان
🔹
داده‌های ماهواره‌ای ستونی متراکم از دود سیاه بر فراز جنوب مدینه در عربستان سعودی را نشان می‌دهد و گزارش‌های منتشرشده با استناد به داده‌های ماهواره‌ای، از وقوع آتش‌سوزی گسترده در یکی از تأسیسات مرتبط با خط لولۀ…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461442" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461441">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶.۵ ماه است خیابان‌ها قاب حضور ملت است
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461441" target="_blank">📅 22:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461440">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
آموزش‌وپرورش اعلام می‌کند مدارس دولتی حق دریافت وجه اجباری ندارند، اما در عمل چنین نیست. به‌دلیل افزایش شهریه مدارس غیردولتی، تقاضا برای مدارس دولتی زیاد شده و برخی مدارس از این شرایط سوءاستفاده می‌کنند. با وجود نامه
آموزش‌وپرورش منطقه ۵
، مدرسه از ثبت‌نام پسرم به بهانه نبود ظرفیت خودداری کرد اما بعد از پیگیری‌های فراوان و پرداخت ۱۰ میلیون تومان، ناگهان ظرفیت ایجاد شد! آیا این عدالت است؟
🔹
اغلب
فروشگاه‌های موتورسیکلت در خیابان ۱۷ شهریور تهران
بخشی از پیاده‌روی مقابل مغازه‌شان را هم جزو مغازه حساب می‌کنند و با قرار دادن موتورسیکلت‌ها، عبور و مرور مردم را واقعاً دشوار کرده‌اند. مسئول رسیدگی به این وضعیت کیست و مردم باید به کجا شکایت کنند؟ بعضی‌ها می‌گویند این مغازه‌ها بابت
استفاده از پیاده‌رو
به
شهرداری
پول می‌دهند؛ آیا چنین چیزی صحت دارد؟ خواهشمندم پیگیری کنید.
🔹
بنده یکی از داوطلبان
آزمون استخدامی فراگیر ۱۳
هستم که تیرماه ۱۴۰۴ در این آزمون شرکت کردم و برای دستگاه اجرایی اداره کار پذیرفته شدم. با وجود گذشت بیش از یک سال و طی‌شدن تمام مراحل شامل آزمون کتبی، مصاحبه تخصصی و گزینش هنوز
نتیجه نهایی و زمان به‌کارگیری پذیرفته‌شدگان مشخص نشده
است. با وجود پیگیری‌های مکرر از هسته گزینش کشور، سازمان امور استخدامی و منابع انسانی واحد استانی، نتیجه‌ای حاصل نشده است. این روند فرسایشی، داوطلبان و خانواده‌هایشان را با مشکلات جدی مواجه کرده و ممکن است باعث انصراف بسیاری از پذیرفته‌شدگان شود. لطفاً درخواست ما را به گوش مقامات تصمیم‌گیرنده برسانید.
🔹
لطفاً صدای مردم
خمینی‌شهر و درچه اصفهان
را به مسئولان برسانید. جاده منتهی به کارخانه رب آیدا و روستای جلال‌آباد وضعیت بسیار نامناسبی دارد و خرابی آن به خودروها آسیب می‌زند. تاکسی‌ها نیز به‌دلیل شرایط نامناسب جاده در این مسیر تردد نمی‌کنند. این مسیر نیاز فوری به
آسفالت
و مرمت دارد. مسئولان کارخانه می‌گویند مالیات و عوارض شهرداری پرداخت می‌کنند و جاده مربوط به آن‌ها نیست.
🔹
من با هزار بدبختی و به‌صورت قسطی یک پژو ۲۰۶ مدل ۸۲ خریده‌ام و تازه این ماه قرار است آخرین قسطم را پرداخت کنم. حالا با این
طرح جدید اسقاط خودروهای بالای ۲۰ سال
، واقعاً نمی‌دانم باید چه کار کنم. اگر قرار باشد این خودرو را اسقاط کنم، از کجا پول بیاورم و خودروی دیگری بخرم؟ آیا مسئولان شرایط اقتصادی قشر ضعیف و کارگر را در نظر گرفته‌اند؟ کسی که با سختی و قسط و قرض توانسته یک خودروی قدیمی بخرد، چطور می‌تواند یک‌باره آن را کنار بگذارد و خودروی جدید تهیه کند؟ مگر مسئولان از درآمد و توان مالی مردم بی‌خبرند؟
🔹
لطفا مسئولین درمورد
بازنشستگان کشوری
چاره‌ای بیندیشند. با این
حقوق پایین
و قیمت‌های سربه فلک کشیده چکار کنیم؟ پول درمان پرداخت کنیم یا پول خورد وخوراک و مسکن؟
🔹
چرا به مردم می‌گویید خاموشی برنامه‌ریزی‌شده نداریم و بعد قطعی‌ها را با عنوان‌هایی مثل خرابی یا مشکل انشعاب توجیه می‌کنید؟ اگر محدودیت یا کمبود برق وجود دارد، صادقانه به مردم اعلام کنید. این تناقض‌ها بیش از هر چیز اعتماد عمومی به مسئولان را از بین می‌برد.
🔹
برای ما احراز هویت انجام شده و حتی به دفتر خدمات دولت نیز مراجعه کرده‌ایم، اما کالابرگ همسرم که برای زیارت اربعین به عراق رفته بود، هنوز واریز نشده است. کالابرگ من واریز شده اما برای همسرم با وجود انجام احراز هویت، اعتباری شارژ نشده است. احتمالاً افراد دیگری نیز با این مشکل مواجه هستند. خواهشمندیم مسئولان وزارت تعاون این موضوع را بررسی و علت
عدم واریز کالابرگ
برخی زائران اربعین را پیگیری کنند.
🔹
در
آزادراه حرم تا حرم
، دو بار از ما عوارض گرفتند اما متأسفانه
وضعیت آسفالت
در خیلی از قسمت‌های مسیر بسیار خراب و نامناسب بود. حتی بخش‌هایی که عوارضی پرداخت نکردیم، آسفالت بهتری داشت. وقتی از مردم عوارض دریافت می‌شود انتظار می‌رود حداقل وضعیت جاده مناسب باشد.
🔹
دیشب به داروخانه رفتم و برای بچه‌ام دو مکمل و یک کپسول خریدم. فردی که بیرون داروخانه نشسته بود با دیدن پاکت داروهای من گفت همین‌ها را از
ترب
بخر؛
نصف قیمت داروخانه
است. باور نکردم اما وقتی بررسی کردم دیدم واقعاً قیمت‌ها تفاوت زیادی دارد. واقعاً ماجرا چیست؟ اگر این فروش‌ها غیرمجاز یا کلاهبرداری است، چرا نظارت و برخورد نمی‌شود؟ و اگر محصولات با همان کیفیت و اصالت عرضه می‌شوند، چرا باید در داروخانه‌ها با این اختلاف قیمت به فروش برسند؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/461440" target="_blank">📅 22:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461439">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌اللهی که منبرش سنگر مبارزه بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461439" target="_blank">📅 21:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وحدت در شب ۱۹۵ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461438" target="_blank">📅 21:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461437" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461436">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توکلی زاده، معاون امور اجتماعی و فرهنگی شهرداری تهران:
«بشکند آن قلمی که ننویسد مردم ایران هرشب در خیابان ایستادند» /
🔹
کجای دنیا مردم هرشب برای خون‌خواهی، دفاع از نیروهای مسلح و دعوت مسئولان به وحدت به خیابان می‌آیند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461436" target="_blank">📅 21:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461435">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFexTgm_vg3FmLK1z8iuSYAf17EaUNfC5dvL-4IARqWGk9-kg7RuEfoB1h7le6AK5sOp_yo0juEDzUqy8oegjyAR9YmM5efC3z80QxsgcAi_ONiGhRnq0l9f_vxNxIihA_6-ZN9SdNOIMYAU7nMpeDztv51aA4b7a4IDU1tHhYC4Zfnm3lQXUovoFmAAyWNpH6mf3aVE_jV0dju5a37DM09sYawoceuB5yFZ29NmrSD_hvHbkmGuPE3eQR96iN6nP370ReLcYE24FJGHXQHfSpzDJYUr82N8s3Mq44P6MWE40pPXxmpKoXs7n8YumFfRZqhEEn31RxA26a1vaVxb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش مدیریت
#تحول_گرا
در خلق ارزش پایدار؛ چگونه
#بيمه_البرز
هم‌زمان صدرنشین بازار و پشتیبان تولید ملی شد؟
شرکت بیمه البرز با اتخاذ رویکردی تحول‌گرا و ارائه بیمه زندگی و سرمایه‌گذاری پروژه‌محو‌ر، ضمن کسب
#جایگاه_نخست
صنعت بیمه با ثبت ۱۵.۵ همت حق‌بیمه تولیدی (رشد ۴۰۹ درصدی) و سهم ۲۴ درصدی بازار، طی سه ماه ۱.۵ همت از پس‌اندازهای خرد مردمی را به بخش‌های مولد صنعتی تزریق کرد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5096</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461435" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461434">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461434" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461433">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yj6OTHCp-agMMm714xRTXiMorY8fNVtXu770l9_GwTRe5vkg59_eN7WuynxZg9TEf0dQEYQPkBmLvDREemOMjUqsMMnGNvKzX0oSabJsBp_Y52Z3Sz9-Q73vtl5llJuM_I_LZwV0-hn0hBgI23qW9gC82PSBsPEFP-HJx5l0wya0J_q7wseb2vMpFMz6tIcbbZ5Ls-gd0kbovMBgfKvkRewaCMsiBPS1vzHDjGZpQXcSKMA7zDXg9xqzDLfrtVpTcgmnO7fpwOSI2aQZmqcsn3fef3LxOinWwhhBUlij9PB6MBUHGkG43ZFYY1CVlKProl0D9ykq-03JiJVSae3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: آمریکا دنبال ایجاد اختلاف در کشور است
🔹
آمریکا دنبال این است که بین جریان‌های داخل کشور اختلاف ایجاد کند و ما با حفظ انسجام نباید اجازه دهیم آن‌ها در این کار موفق شوند.
🔹
اسرائیلی‌ها منتظر فروپاشی خود در ۸۰ سالگی تأسیس رژیم صهیونی هستند و ان‌شاءالله زودتر از زمانی که رهبر شهید انقلاب فرمودند، رژیم از بین خواهد رفت.
🔹
ما با حفظ انسجام و وحدت داخلی باید با مسائلی مثل حجاب و سایر موضوعات فرهنگی مواجه شویم و اجازه ندهیم این مسائل انسجام داخلی را به هم بزند.
🔹
باید عرصه را برای حضور همه مردم با سلایق و رنگ‌های مختلف در بسیج فراهم کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461433" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461432">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌ بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461432" target="_blank">📅 21:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌
بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار دیگر ببینم.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461431" target="_blank">📅 21:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حملۀ تارتار به سازمان لیگ: دستی از غیب تصمیم به لغو گرفت
⚽️
سرمربی پرسپولیس پس از لغو بازی با خیبر: از این تصمیم غافلگیر و شوکه شدیم، چون مدیریت باشگاه و بنده هیچ درخواستی مبنی‌بر لغو مسابقه ارائه نداده بودیم و این تصمیم به صورت یک‌جانبه و بدون هماهنگی گرفته…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461429" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3aa62e63.mp4?token=rhlhABLL2J9u8OEvItj_lgXd8VIVAaNyEdqqM2_cedUuJeNtMeYhTLhMB7zs9gHgmv0cxwQErorg_yJ9DhAdA-hx0LzRWMpkska4F1NStIBASRLj1nIYpDA4tw9HR8Dy6ITR_U5mn64nEpDOi1xkMj-W-E29W_kXUJPq3yeCqygWxJ4-MOmf9n2ijIEHtjTaBEGZoLgUQX7p8sTbSzoUsGQI_MtCdN_jV0rgqZ5mqOEsGK7AZqypSSH_BqKfwiVndn6zayPN_SOABd7wOG9v9uKQlBokZbfBCgKB_hyxfMA2T3ZXE9DdbAHI5QGhPe9zd4AAIAvP8zV2HQxi3L5yAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3aa62e63.mp4?token=rhlhABLL2J9u8OEvItj_lgXd8VIVAaNyEdqqM2_cedUuJeNtMeYhTLhMB7zs9gHgmv0cxwQErorg_yJ9DhAdA-hx0LzRWMpkska4F1NStIBASRLj1nIYpDA4tw9HR8Dy6ITR_U5mn64nEpDOi1xkMj-W-E29W_kXUJPq3yeCqygWxJ4-MOmf9n2ijIEHtjTaBEGZoLgUQX7p8sTbSzoUsGQI_MtCdN_jV0rgqZ5mqOEsGK7AZqypSSH_BqKfwiVndn6zayPN_SOABd7wOG9v9uKQlBokZbfBCgKB_hyxfMA2T3ZXE9DdbAHI5QGhPe9zd4AAIAvP8zV2HQxi3L5yAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند با قُلدری مردم ایران را وادار به تسلیم کند می‌خواهد کاری کند که مردم به‌خاطر نبود معیشت و امکانات تسلیم شوند اما مردم ایران تسلیم نخواهند شد
🔹
اگر این‌ها مرد جنگ هستند با نظامیان بجنگند؛ با نان و معیشت و زیرساخت مردم چکار دارند؟ اگر این‌ها انسان‌اند چرا راه آب و غذای مردم را می‌بندند؟
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/461428" target="_blank">📅 20:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb125a3a80.mp4?token=k3NKuA54256Tk0ZTLbLiP_6WASwT_tflVgtNEM4OsAs4-mfScXcAn2G7UCKGDZWFoq8b2nZAP2jMY43BslJy3P3uim07-bHQLJGO_gmsupDCoxJfOycbwAqjciSJJN-qR_nZccAUonkGQiVRsrnbYDw2iBOoHtQmj66OU4u4igWaS2ZvKdM2rONPDsJNjJM9HRPwle09Xi106KNpgU2q8MNiDm3dlleX5BeG9BnXry3scO2w3nU86hN9h8L77IXoGZ-mBe5REqErDPBjNVvvNGA0pu_NMYoQsdOfy_UACMe_osivucHNdBJmy9mh4iQ0EnsGzN8AjNf1eXMmVKZmqpXtjB7dxcZIz_PZn808OIxdrgtm7EFRqpx2Ny_987Ypb4u49qoYJRc1bmnSAY7YenN_hoJrzcdOKwv1kAIpfg2t7WAE8jDOHp3JIu2hm2a8RS52u8vTHye4bLk4cnTrhD3tMxtGcXRyetIoj4yWLaA2cJ_Nj-41VS1M1o2Ce0KLeM8vfRWG3tsQ3cQ0y6dSgKTOYFi_AID_XmyluvUDJ6KVqaBS-2c3McWFYLVjTZBbzZKLQnu7rij9kvg7gE-MjrZOM1wQLaygJ-XLyfHQxyP4cS7zs265V44RNoXr7ZoUO0Cd2FgMRDm72QkOKyq3I004nJoTiosEWFsU82N12Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb125a3a80.mp4?token=k3NKuA54256Tk0ZTLbLiP_6WASwT_tflVgtNEM4OsAs4-mfScXcAn2G7UCKGDZWFoq8b2nZAP2jMY43BslJy3P3uim07-bHQLJGO_gmsupDCoxJfOycbwAqjciSJJN-qR_nZccAUonkGQiVRsrnbYDw2iBOoHtQmj66OU4u4igWaS2ZvKdM2rONPDsJNjJM9HRPwle09Xi106KNpgU2q8MNiDm3dlleX5BeG9BnXry3scO2w3nU86hN9h8L77IXoGZ-mBe5REqErDPBjNVvvNGA0pu_NMYoQsdOfy_UACMe_osivucHNdBJmy9mh4iQ0EnsGzN8AjNf1eXMmVKZmqpXtjB7dxcZIz_PZn808OIxdrgtm7EFRqpx2Ny_987Ypb4u49qoYJRc1bmnSAY7YenN_hoJrzcdOKwv1kAIpfg2t7WAE8jDOHp3JIu2hm2a8RS52u8vTHye4bLk4cnTrhD3tMxtGcXRyetIoj4yWLaA2cJ_Nj-41VS1M1o2Ce0KLeM8vfRWG3tsQ3cQ0y6dSgKTOYFi_AID_XmyluvUDJ6KVqaBS-2c3McWFYLVjTZBbzZKLQnu7rij9kvg7gE-MjrZOM1wQLaygJ-XLyfHQxyP4cS7zs265V44RNoXr7ZoUO0Cd2FgMRDm72QkOKyq3I004nJoTiosEWFsU82N12Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی و بازیکن خارجی که به استقلال نیامدند اما پول را می‌گیرند
تاجرنیا: با کاریله و استراندبرگ تفاهم می‌کنیم
سرپرست مدیرعاملی استقلال:
🎙
کاریله از ما شکایت کرده. درخواست مالی او از ما زیاد نیست. می‌خواهیم با نصف مبلغی که می‌خواهد توافق کنیم. با استراندبرگ، بازیکن سوئدی-موزامبیکی تفاهم کردیم. با مبلغ ناچیزی آن را جمع می‌کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461427" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدای شنیده‌شده در قشم مربوط‌ ‎به آزمایش پدافند هوایی بود
🔹
درپی شنیده‌شدن برخی صداها در محدوده شهرستان قشم در حوالی ساعت ۱۸، مسئولان اعلام کردند که این موضوع صرفاً مربوط به آزمایش و ارزیابی پدافند بوده است.
🔹
پیگیری‌ها از منابع رسمی در استانداری هرمزگان نیز نشان می‌دهد که هیچ‌گونه انفجار یا حادثه‌ای در این شهرستان رخ نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461426" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab4f3eb43.mp4?token=vZPKeygcHvXSeoBtQztF2IHBXN9-4w5XjrKQsp_DLdcgczmjOV4jD4M9Otpbcowillyu2A6LBKQ347hOxC-F37-bQdNrq0zo21XlCWxGtcjmYRsvK-rels5dCautanqnW5ziKFyzuGGd-oitm5taNah3syO7Kw3FqdSXJfTYhSMPLx7FPUuI4bqVYsZ5eGumE6rLKsTreh1UgHYTYEV1jqVPXwTo5AxBohLT7sF_8QHW5AzZ8hlbcEji7bc5uB4jPca1G5dwM2lBCdI9tUshOZeT2TUrvEIFXilUwlZ0rI0pOrFfbZbPu9FQ46oxairEOD4HGEQaTFcT7nIiXMfBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab4f3eb43.mp4?token=vZPKeygcHvXSeoBtQztF2IHBXN9-4w5XjrKQsp_DLdcgczmjOV4jD4M9Otpbcowillyu2A6LBKQ347hOxC-F37-bQdNrq0zo21XlCWxGtcjmYRsvK-rels5dCautanqnW5ziKFyzuGGd-oitm5taNah3syO7Kw3FqdSXJfTYhSMPLx7FPUuI4bqVYsZ5eGumE6rLKsTreh1UgHYTYEV1jqVPXwTo5AxBohLT7sF_8QHW5AzZ8hlbcEji7bc5uB4jPca1G5dwM2lBCdI9tUshOZeT2TUrvEIFXilUwlZ0rI0pOrFfbZbPu9FQ46oxairEOD4HGEQaTFcT7nIiXMfBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسخهٔ جدید اینترنشنال برای ایران: بمب اتمی!
🔹
ایران‌اینترنشنال که پیش‌تر برای حملهٔ نظامی به ایران، دست به دامن آمریکا و اسرائیل شده بود، حالا که از بی‌نتیجه بودن این حملات مطمئن شده، نسخهٔ «بمب اتمی» را می‌پیچید.
🔹
مجری و کارشناسان شبکه دربارهٔ این سناریو حرف می‌زنند که چه سلاحی می‌تواند تأسیسات زیرزمینی ایران را هدف قرار دهد و آیا استفاده از «سلاح تاکتیکی اتمی» می‌تواند راه‌حل باشد؟
🔹
اما شاید مهم‌تر از خود این بحث، ادبیاتی باشد که برای بیان آن انتخاب شده است.
🔹
در این برنامه، حمله‌ای که در صورت وقوع می‌تواند پیامدهایی فاجعه‌بار برای مردم و محیط‌زیست داشته باشد، با مفاهیمی مانند «بازدارندگی» و «اقدام پیشگیرانه برای حفظ صلح جهانی» توجیه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461425" target="_blank">📅 19:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDNXDJrRBl2o5S_zUUOOAGlslORwDh9MK3B_oPA6eLtH-YlVruj3V6bf7tXv0hgoAuoaKjx2Qi3lsNGq_PwlQSfCvM-Mmdp3GHJqy0wHGOun2bnAbfjQDwhXvOuhwQaT152N_Iq3dQKXvdnWm_69OoYzhAF9GpymbKJHsV4sveQpsnJd11csFIhfPTjqzhK14-fUr73V0bNrP04iHGgOrgEXZPuWwMItF2hXzhG4C8--I88l7WnXCIkWuyhnTdDjzFRIn25eoJ17G-en6h1GKwB7mecZj3vjlAcmiyOSAZLv-2Bg15SS5eu00aXPoQJ7jAha4eU6yGLA_Q-BnMzU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNzVIr41jLrXXDJAB1WG9pICCc9WKz1rkY3i69IwLgAjaL6qTCRFHf6k5pPPNE5LWJtKxE-JzewkkEoPRwBEqbLrr6Vqreqjr_1mWzH-uqOg2pwQQW2S6iFRq5Ua68DHgfmZmKvoTve_GyIq0XnsyRbuZVZBmcQYeRyjVJtt4IMHS_BNbSHHGbnLMUFpi_Bd4BkvPVlrjpdz_zmjzg4bYCAW_Cf_EdzGgNcdNxGoBoJ9Nf8VQm20l6JZ4judRl8_7z7Jfve8Q4qGDSNysRtmJ1TOSdioRYLRgm-036X3pMko8jSHCYLW7xVRv9vRfVoeACLndWLuXU5YEEO_KmddvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdkfPNrMgnTA9l5Ay4sUc8ROHl8heh6ooFQGzhzasevLTDQLTdukyJD_JsOvTeTi9MVmQO1ja7iqQX0GMuGOOLE_Y-dO_CDiqKQK69rdSOwJIU8lXaOgnvxgS0EyEwBkSrSqaMlp7KPppcfmJgRzXJI_54CVEo18FV2Ppq1WdMk3mJkmd-Rqfmw1G68PlXp-07W522G_l_Yylwxvvlh8iLcTRU4LIU6kUMJ1zC12VSph1_btAFGtZ3_i2N6rGSzlXANz3XLLQr0l6BmcFmQd6Zq3wvYjnkVU1m6-gENtLyKlgFCRHw9lRW8XOT6hFy9OlUJp5a6A_B0fVLyhPs7VEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGgN02qd3zoVd9lzBe6r32vqhrw3pK1YNK7nZ5dAzylFNZQo2scqZm4QTGGA7fqbJE3S-UXNMC7sBq_8HG4YSJqEduZqXV3vzNyKs86FDQVNS49iglGHaIVrPazaf0NL9U-zvAfieMkdCj0i5mFS0I2t72a2uLbQ_9yQBRx16oi_V3w4fdPTnuzTXWs4C4Impdud2BdZHW7Z-6eCvTVsCnmgnJi9uAsUDW0D7dTJAxJBy4nsrwwP4GRPdKPjQw8yE2NeVmForo13665XGEQJ_Z6RGSP9vCRMgkG_L3HoNEbQy2z6V6OeRxJRNnuq_J9M9QNrjUWoeDGxw7xZsmXrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIPo-h4LIxvkzspa3eSFg5cO1S7_fUEfSuUKuEUz327p8OSMYN4_biBenyu_9iKNiCj4h2kiUic4ZDdZJPwjJQQw51lV51kIwO6CcS-Lwl6yMXTKsUBX1NUndzuxOMwXweNcrqXDHCg_99RnmfSkclO_y9GaCPQTlDZqQCUYUWwo1UkXfen_AabIqof5-vU6rvyE_yT2NgSEQt3iYnc3SYw9pDx6Dkl8Z_qpHiO27P4bxBnBZ2O1odFuXk1_VO0rU10bMY1M9SHjy9MP1qveSTkD_l_CLx723tUazb1ZXdt5JZR5Tcfd7k-MoI9PPLtIvHSxvVQ2VWqEWEXeFSBTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EesaChFlZvhFnV7nS_R-iwqBl3T0II3RAUyPKWPgreTq8F9_Zmh7Urm2oOrv-mJMz5EoAY4LYkSk-vFZPlwfGI1196HnbiMue7XAGVOzsymM1cpvL7XSIaMy4yNmBbOognDa-DnnjMDtm_sNHqqRq0d8nw8fcz07M4k-lOJT2cFDkeSMc6ac5M1F2OvuM_8Ty0b9xh5DaQ-kZfUNaC1TqVxBUOZoBeMccwFd4LYNPxLIFxi_3t22naSM7z7ztSAlAjDXFinY1B5NkB3xShiY8mx3yu6eUiGGByiE3hwYf1rL0B93E9pAs83SdiAtEzIwhnJGxJN4X5sFCr_yMCYEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEE21Xy4C4E-k_jmt0MDP909s0ZdgnTWusHPIKQ5-dyhC5rsoKEBGkvtuhA0dh8hDKpX-HTopSeX0WbXzsPEw833jFujZs8K6jHZxmCzMin_bPjVieKuEZhjS87MMIFHb945ifIs0KEyKiHADx0E0VOQU1sabwjqvsNlNC7oe0Kh2s8Npcl2DvASNj5GT3_0Fmi032AT0-DO99xgJpnOyPQSsVEqSWEv0mkVWjOBrDy2s9jsBR21p4PDoxiE2RDnSWvU8zoUnyvRJradFLj9jZiaGnMXnwgGgTF_gh9TCCu35VXSZkRrWBYurOGa8EVNlxIXDjiEjZmxbU7GkeU-Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک بنای تاریخی با استشهاد محلی تخریب شد!
🔹
تصاویر تخریب «پادگان روس‌ها» در سبزوار شب گذشته در فضای مجازی چرخید و واکنش فعالان میراث فرهنگی را به دنبال داشت.
🔹
مدیرکل ثبت آثار وزارت میراث‌فرهنگی در گفت‌وگو با فارس می‌گوید: مالک با جمع‌آوری استشهاد محلی و طرح…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461418" target="_blank">📅 19:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22277b2e4e.mp4?token=vgTpQxfd1QF-L78DvjO7gd5u5hO7XImGitJAP233_QO_TYfwUwKozsWotdmwDp9tEFMqZcMcTyT0LDdeG-rgo0pwbz6prn62UpZwaIRegAg7hh9Jilf6Chu2XDO0B-2cFlIUgymmSvRS-eOSzdUcsUEEj2JODMsDZcJfvAZIzA-tlqNKtd2EtmF28Ls-D30ZVdn8cgJc_JCRAF28Xrh5N07MuaVJlioNbzZVKxJqASaVB2aWseKo3elrVDhtK6Jn7rRK5QVso1tAZf2EoVq7MmuQr1fUwSN0HrT0LD8sToKQU7fZeT_W3c6TTQj0GBCIoSWFYlpWFrf7LLC7WnhkBGWkMOVvrZN3QHvTmODmEVbpgbd3NGRNrxXLsUx8Ee2Xzb4rK7LifcDgVvR0RPL8-FP20MCumGpu_h96r0I3Y75LfjUvQVswHfXbpErkYvUfmngYW7XSMeTXEoCj9A3JgBcnS3Px1TLX5yk_pqcWVdPI7SlFbucs4pj3eAImOWXzfqmp4sj9bxCHiVXXaV5q8GOOjWfcwsu2ScfmLmHlRvVk3A6ASfnGxjyfTCglD_QZ2otaZsn-4IwX6JFWVjNadcmqlvet1I0t8HtjaVzUyYKPp_1_KxjwfT0y8ITTA_02RI9xUN047RpIg3j26PfdAE_EfEJ2w5NnVtXIVBvIzgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22277b2e4e.mp4?token=vgTpQxfd1QF-L78DvjO7gd5u5hO7XImGitJAP233_QO_TYfwUwKozsWotdmwDp9tEFMqZcMcTyT0LDdeG-rgo0pwbz6prn62UpZwaIRegAg7hh9Jilf6Chu2XDO0B-2cFlIUgymmSvRS-eOSzdUcsUEEj2JODMsDZcJfvAZIzA-tlqNKtd2EtmF28Ls-D30ZVdn8cgJc_JCRAF28Xrh5N07MuaVJlioNbzZVKxJqASaVB2aWseKo3elrVDhtK6Jn7rRK5QVso1tAZf2EoVq7MmuQr1fUwSN0HrT0LD8sToKQU7fZeT_W3c6TTQj0GBCIoSWFYlpWFrf7LLC7WnhkBGWkMOVvrZN3QHvTmODmEVbpgbd3NGRNrxXLsUx8Ee2Xzb4rK7LifcDgVvR0RPL8-FP20MCumGpu_h96r0I3Y75LfjUvQVswHfXbpErkYvUfmngYW7XSMeTXEoCj9A3JgBcnS3Px1TLX5yk_pqcWVdPI7SlFbucs4pj3eAImOWXzfqmp4sj9bxCHiVXXaV5q8GOOjWfcwsu2ScfmLmHlRvVk3A6ASfnGxjyfTCglD_QZ2otaZsn-4IwX6JFWVjNadcmqlvet1I0t8HtjaVzUyYKPp_1_KxjwfT0y8ITTA_02RI9xUN047RpIg3j26PfdAE_EfEJ2w5NnVtXIVBvIzgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئله من و ساپینتو ربطی به رفتنم به رختکن نداشت
فکر می‌کرد نمی‌توانم اخراجش کنم، همانجا عوضش کردم
سرپرست مدیرعاملی استقلال:
🎙
ساپینتو احساس می‌کرد خیلی جای پایش محکم است و آن نقطه‌ای است که می‌تواند مدیریت باشگاه را به چالش بکشد. من خیلی در قبالش صبور بودم. فکر می‌کرد نمی‌توانم عوضش کنم و من در همان نقطه اخراجش کردم.
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461417" target="_blank">📅 19:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۱.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/461416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۰.pdf</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461416" target="_blank">📅 19:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461415" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8LwFmuilhaWTjJwn1DnBUyXJuoQX4_hrmSTCjA0ZL1J_j_Gv-_gd1KT5Ah5UaCW0n5yYzI6QKyjQdBEv5niGSe99kUetjWFMzDFzdTIbCN0n_GOYCEpUMx_khvK4r2SRpuoJH78FdQQ1KBwWSyFTOa9YIsJ8mKISZBlp5fgHPRgJnl7ccV25zP2TyfP5mlTeYNPgZDNMrX4Uv-dg9kt2w6LIB0Tc-VTvK9hkdMO77IL6gMoFcS1snNiRSbDgqAL90j4o8HQk2NSZN5dz2HwaeVsXOqoNLa27avGRkpl-Y4EiXSxh999lpdA8VmG5WohyXA0eHA3cdkTluxFxVXLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYITbwoIbEidRU9-T6mbGbwgcvDmPsv0nGZerNr_-DZbj8T-phHjtW9iHkTbnrJcGxJdLbfvlI6QUX8pKfvk9wfqqvD8dOcZ51Oe5fQAWwIRUPjofhbzMPzF8boCMCIQ7PBnpnGcnZNXBqUrAlvO29ZNyr5siYM79qxAJ-aka51F-RSlqveo0TDwZ0noQzYSNGLFlBd_otPusrSAedoVOOGy_dVhaLTn7O6a-sjVQh5go7aIvEZ6nR-ggq_MkLDdZ4lD4jAPHhIYJa3jkYjgxwMEk5L2Y_TFDqNpZVM6UJFUm5PzDHCFayOfHetSqycFz7T1fQ-MgjLh-bXAL5ncqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b69dPvgWr5-l7z0815JR2D-pa7uDNR8emh7gOZAKw0nMlycY3eOOfNxs04Ttil3SE61W9Jai2kL1_7F0DQ9BNy1IPzDDzIZ1lBhjt3Q_y5KFkXKw9c_2qKzWXzDSm4L4hFXU8YgpjFcwuSpdLIatYCDzhbCyozLrIW9XYWP7o852TKlEEjc5mgH7hOUxZqM1q9yVU8YcCgWl17x3ikJW5EazcWbSM64TQd_DVT5zhDFFnYENAO46SFpJSRLeKSlqtYtlVlWUpLKTbiC0waKtO8LRv2_kXp8yNka4bqvW-DJUaVRPAGmLfyC-X5uPooMbqQn0GbK3o1D-CQKhA_gDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oosNJ8yUwV3sFCcfvhPBxaKYhwnSNE_L3rnIivq3VRWSXcUetEpwiKN2RApoKNX7jZdCjFIEAphvXRFAxmMaNnFok6eE_ZsNbSE-zI6k7iQKCBHVRFt1StIFolj3AVeMjogrpZrqei4za-mAEKR3LRwalgSZbwjbwRLcCMYfFB_w9iPsBsJ_eI6xyKKaBTeqfFBpM5pPkhLidGpOh8_SzWVTVq4wESu1A3a811jpB1ezH8HbGNaWzhdo6St4-MWEC-LmNF9yvbmYLDd9vrKqVIVt3EEecw5i6OwQSdUGFesfLrbGXWOcjYEeJOzmkxXiw4g7v8qY3njKcf827U67gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-NqSFxjTgYdExJH6Aa4OIt31avnR-ZWu-_QhTLFHcEEttBy841FB2GfXF2PGm_CYO2qdA7mB2oBi7HuXHnFfy36CyNcl8Vudmz39fdOehn25AeNNPz795v0HNBFvQA24PARP7exwqUTyqPI0m-1R7LF8JTtdz5UW4HRSUbo5ZkVOd73ypIQ1NbygEZbF7YPs66RhBeeiEohqxPYKrH1kSWVh0rV73z1OpdKsIAPinGKtvYT8GOtDSlo5MKuimzcY4ixWL3EdMejptAVxeQcKL5MkKO91HDMQjt-iwGx7qyfCcaUHNKxzsT-t_zhV_VTpM-UasFcvwK0ML74kB4Zfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461410" target="_blank">📅 18:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3b00cd2d.mp4?token=KbpuXo805a4sOGQRtCxwTD8YZ1CYe2x7Ir-S1aJ8_vnJV448MVI00v7ubODWhSFlLzjc5lFE7s2vIzYHccFWqIMGaGPdV7SQIy9zJ4TyyCYmI6xtbkX07qSFyi6Q36vu4mc0w3nLjuAg8XCsEBr4XePfomjoAGftXhP9BW5m7py33tX8R2QIsTHPYLYZ_9rqI92MzNDowD3s6m7RLZtakRrY_pzVgr5Ht8Ewc0GmOcJn4KXsCcXqoClRoOahUfqrEApNwhr7YKiiy_3H3hUv2vhmkbYeAP-RR6d1t2ejTrUKcjn9hZTBxkcZSzDMiTM8C-7IMHOb914Hj1qSZDRYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3b00cd2d.mp4?token=KbpuXo805a4sOGQRtCxwTD8YZ1CYe2x7Ir-S1aJ8_vnJV448MVI00v7ubODWhSFlLzjc5lFE7s2vIzYHccFWqIMGaGPdV7SQIy9zJ4TyyCYmI6xtbkX07qSFyi6Q36vu4mc0w3nLjuAg8XCsEBr4XePfomjoAGftXhP9BW5m7py33tX8R2QIsTHPYLYZ_9rqI92MzNDowD3s6m7RLZtakRrY_pzVgr5Ht8Ewc0GmOcJn4KXsCcXqoClRoOahUfqrEApNwhr7YKiiy_3H3hUv2vhmkbYeAP-RR6d1t2ejTrUKcjn9hZTBxkcZSzDMiTM8C-7IMHOb914Hj1qSZDRYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نکات معنوی از زبان رهبر انقلاب
🔹
اگر کسی استغفار بکند، مغفرت الهی برایش می‌آید و رحمت الهی شاملش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461409" target="_blank">📅 18:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94303b4379.mov?token=UobmQ0bFQ-wlO8BuPraVYBtsHiZhIaQoVFsUeY_-qYFM2SjUJ1WMiPVnkf91qU7gxN8RCKG-3NYxNbY44g5IcK06W8Mp9HUwHEzJxylMi79gaRb_NSz0U6kWgSiK-gcHFG2FLkc2BdcMlgXGRn84V8JYNntyH-KyVs3jF614ciX0XJYcg9124D1GzzdmM_qlc843-MbURXp6mEeKLsIYfh0DvzFh4xIef12d93YGf8u_SV1EHKFyHhhMnafKeg1Kr-KszDHVvfQLaJz2mIyR_boqATnl7nXjj3c2BPjTeP2HMZmhjcXqtVLHMDI1p-4WkZ3B8gZ8VhVbvmBLdsBNSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94303b4379.mov?token=UobmQ0bFQ-wlO8BuPraVYBtsHiZhIaQoVFsUeY_-qYFM2SjUJ1WMiPVnkf91qU7gxN8RCKG-3NYxNbY44g5IcK06W8Mp9HUwHEzJxylMi79gaRb_NSz0U6kWgSiK-gcHFG2FLkc2BdcMlgXGRn84V8JYNntyH-KyVs3jF614ciX0XJYcg9124D1GzzdmM_qlc843-MbURXp6mEeKLsIYfh0DvzFh4xIef12d93YGf8u_SV1EHKFyHhhMnafKeg1Kr-KszDHVvfQLaJz2mIyR_boqATnl7nXjj3c2BPjTeP2HMZmhjcXqtVLHMDI1p-4WkZ3B8gZ8VhVbvmBLdsBNSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان با نخست‌وزیر هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461408" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تبلیغ دارو ممنوع است
🔹
رئیس سازمان غذاودارو: شرکت‌های دارویی باید محصولات خود را صرفاً در چارچوب ضوابط علمی و برای جامعه پزشکی معرفی کنند.
🔹
معرفی علمی دارو در همایش‌ها و کنفرانس‌ها مجاز است، اما تبلیغ مستقیم دارو برای مصرف‌کننده نهایی ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461407" target="_blank">📅 18:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7QV-EI_JXhEeHMNE62UDrfy9d56v1RD_rSMuHobyjwZjL05tghh9tf3kkxk_G2sFM-MqeSvzoXB7rFTkhCazyhG9LPAOEp6Ba91Iw-GZtrrkrMnGiEMnIQvSVuvYfjrCcDBEe1foUOfgc0RsTa6q2Q9XoqEqxOhK_4l43DrG5fx09TzZWzu2fSg1o9lyfvwmSt4vN1_p9q97k5JZ5rUIW_PIfW3o7bCwmIO6p1LUzMLgCqOS9_NPsKKRDzg1SFAFX6acVGY6U6JO00UNv-TeIOJgQk9rtI0qPn6NZ7glgkmoxz-RcpDgVNLYm8fShIYCBGw9QyQVm3USpgU4djqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ هوش‌مصنوعی امارات از ترس ایران زیرزمینی می‌شود
🔹
پس پاسخ ایران به تجاوزات آمریکا و هدف قرار دادن زیرساخت‌های فناوری مرتبط با آمریکا در منطقه، امارات در حال بازنگری در معماری یکی از بزرگ‌ترین پروژه‌های هوش مصنوعی خود است.
🔹
پروژه‌ای ۵ گیگاواتی که قرار بود در قالب یک مجتمع ۲۶ کیلومترمربعی در ابوظبی ساخته شود به شبکه‌ای پراکنده از دیتاسنترهای کوچک‌تر در نقاط مختلف امارات تغییر خواهد کرد.
🔹
طرح اولیه امارات، که نخستین فاز آن با نام «استارگیت امارات» با سرمایه‌گذاری ۳۰ میلیارد دلاری و ظرفیت یک گیگاوات کلید خورده بود، قرار بود تمام نهادهای دولتی و تجاری این کشور را به پیشرفته‌ترین مدل‌های هوش مصنوعی جهان متصل کند.
🔹
بر اساس طراحی جدید، بخشی از تأسیسات ممکن است در زیر زمین ساخته شوند.
🔹
ایران در پاسخ به تجاوزات آمریکا برخی منافع آمریکا شامل زیرساخت‌های دیتاسنتری در امارات و بحرین را هدف قرار داد. در یکی از موارد، واحد ابری شرکت آمازون نیز اعلام کرد پس از برخورد با یک مرکز داده در امارات، برق آن مرکز قطع و آتش‌سوزی ایجاد شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461406" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtzq0eIrx8FgEfdav035ZbqddUVo7FSzx2oj-tvqH1ByZ5gdtoWL8hS9CXRcUm30M7DOi0kkhkJplHEF2sCmqstONf8nYHe9rqGTzYERr6BGzbr5dKXmTa4eDuInk6NZq3hgAItvnnyhu8JwwcLHuAzrSsrxCM7s2FnQlTrE63oe7K2klvRYUCImHGWUJ8Bn_-yKEni-KC8M5e0-NYO8TG0nsTCjC4EqIbjqiVefnO1ZS8Q-W1q1QE5nGC0xXWF6AsF1Z_yKC-X9eImDu9tbriAOXV3wWtixysONLJ1Z3oOuD1ZWH27nD4geNWm-RIbMxL-QnOU7sdudSSuTsiyEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d35eXFiFjKGHyDz2Z3Kpl7H9AQX24ESR9edjwciv0LB3KzZdNPdyp5_eq5IbKqO_41suQXJtSB2CxXDuzFGgthNnTtc1Vnbf8vYraf_Buw5-_VZNgpg8DQcPSRfNVLFVo-LrqRjY_C8PZT5moE8hEM21qaD3V4A8qt4sahHCQsAA1M2k6WUxnOjYk6f8uYK-yHbe3myZt983CWH7wZ0UQe3R5NKAPWuGheMu0Vpr-5G5c6FTt5t0TS-N24idh4_k50JLzU-xQlbTqjjiJCOLAA79pb-hssyMDZPVWmp7MH5peR2Dn_--ofRSNG4sZ7rCmaa1PCw0fGyDIV7DTu1D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOl7xP83Mbs-qEUNMS0QobkYsBSYrRrovHMDMOPAznTbIjqQa-KYqpbgPwFr_7uscm1zZ0Kzijh7Yul8ENlADMunWJC7tF1Cyaqxn-41xGCy4wk_aI3Yt1Bee6mqEVFws7_Ato1YfqTZ_sK41mtkMpPgXlj0aV8fLvi57K0vy4_dTE1m9LSwd09Dns3bKImYNqSjN0PvPiVG7dF3DNz5p9-6jKWXH0dIbGT2usCrafQgNA0qvvjEFKA6M9ToH918MhzJmM4oRFUti19BWC_DiNvXjnvLuTKvRMMAGZXdMF9ph8xfvaiHQVlLRRJi-uDIw9LRYtYi3NkYL3RNjxX0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np35zkr_JXW_eekLcQy2qEE4fre65DGrbedARB_cQT7X-Vm7GVue9T9eG8ROTSi0-siqu2J-BxQoNDicwpEP7X9Or3wduKEGYFCUiPmbkmD65u0ALgE8eVKEBfSLm50fFoOZveND4NUZjLbygvok33FMQZP0eJH9gbOsWAAOdYJ9h-28DRWzyGCgQHkivkKByutsgfaxBgjKLd7_g8JWZ94qjcvvE1VvmnszTnxTRDGLl63TDf9WtXbhAVVN2othy3z0-J0OW5Skh5n7Wp8jXdd6hUp2ydDZC3XCOUMzTQWL8FGRlqOdOt0ytwt4sG4S6NpWkTmpqGeq31wiJZUrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hsvah4H0xJCkzHgsKHu0MMwKTLtdefZYxp3MdyZsrjMuufaUOIMZVUgm6snqc_WJIWTAutgnNHqwBsExbHJxY1SVNuWKXhKaTsLE4wLaKYz8F0Ob1uxY2XWHZbS_iSKu4Ccopq0ogYNUMothC5yWTgAZJfmDMsOm5-5mdMOdQXmsy0STXqKjRTonj_KrEF-gDGd_ptN-Ne4Zg46l3W5GqSoUYiIfYywEL182n2i4TGRW02e-A1-CHpF8c6FJvxsqthVzSSTQLhoBpU7zEcMXkIR1JVX9rZyTCo3R2E-A6BRXrrp9e2NdYkYq1Y3bXz2xCfO6ogeDB2daiQVf3C684Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKjCSio4yGZe20mEEu0YyKSt4R_UL_Qb-87YmpBmunZTY56d7vzI37FoAQ0DmW2ZD54-HRvlzplnLdOA_lUhy5_xQ0ZBc38xcAspOZMzdQFG4gsQg0cB6ICsSjamT_SbJpRhbRxMect30wAXXx4GZxFRUb4A1oaF-kmWy_qOxcNLRq1KKAyWN7UfG3XNasW3f8WO1zJoD53M0_iCcXQ1z2NEzsgqWrINdUh-icXBKywGtZsJ5P_7Gf1iuV9_lgwgmNdSPr0CRSvUnL9jzyvhR-EzJGe23h3E9QEDKDphq74gbVToFafkJ8dc5uuVjlSdjF35Qd_0XkFYmtiy7t5osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m28ajtiEB42rDxoI-gPaiQVRQzHaUyoqDd_RuoYeUL6TJErmF66wHPfUHKEvFiFFv4ydeRonbDChrMrzlBQ6OJvuFtfdE97wirSNyymOB4KDBB3H9ky4fVH6ap0IqReDi9NnVUa3p5VpHUbnYw2nN47_2mZ3iuZ03wt1cEdODSpNZgt3uUyvFs3PlGMiyTsFP5xaFtQAliwPpLFCWAmnX2LkGyagk3Eiz-gOGVrusjwDe3SgDk23FYJOLVrShfvkjWm-Dn_5cZyncKqQAEhq3ZGfJn_KQc_7l8iDYK3JmKWexfWRwH0AmV938kODJK2DZZMrXfN2odptQhL_aZBuvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونق جاروبافی در خراسا‌ن‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461399" target="_blank">📅 18:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e75b37fe.mp4?token=E3Zm4Zy83A_M7GSj2upeBmjeNcLWg83HbqwcD3tXFqgRt3IAmaWimsa9_njJQ70bwuiZDOw_5nzX0aTSZNexGBxpcJmF5b4SVV_giaDD_6LnXKxkVTOBm24fSM9I0YF0HhrsT9yroQzkM91aaI3BrH9a_tcIGKp0StCyNzKI_CbszcrlYX8m3gdYrnNjQ_ei1vX9LRsOXUAiuvusTTGjV4j9xmKwxuEmIf6RiO9UuD-9HP2AYwmpz9bRF1Zwx5xvY8bX2QC4RJbpoSQUvSyhpFegvtGXBcMkfc57Gjjt1IC1Vq97C_C8TOQM18DWuSKLcaA4sJ94feC0NlJIGlzmdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e75b37fe.mp4?token=E3Zm4Zy83A_M7GSj2upeBmjeNcLWg83HbqwcD3tXFqgRt3IAmaWimsa9_njJQ70bwuiZDOw_5nzX0aTSZNexGBxpcJmF5b4SVV_giaDD_6LnXKxkVTOBm24fSM9I0YF0HhrsT9yroQzkM91aaI3BrH9a_tcIGKp0StCyNzKI_CbszcrlYX8m3gdYrnNjQ_ei1vX9LRsOXUAiuvusTTGjV4j9xmKwxuEmIf6RiO9UuD-9HP2AYwmpz9bRF1Zwx5xvY8bX2QC4RJbpoSQUvSyhpFegvtGXBcMkfc57Gjjt1IC1Vq97C_C8TOQM18DWuSKLcaA4sJ94feC0NlJIGlzmdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایه پوتین به گروه جی۷ در نشست بریکس
🔹
رئیس‌جمهور روسیه: بیش از ۴۰ درصد تولید ناخالص جهان در ۵ سال گذشته متعلق به اعضای بریکس بوده.
🔹
درحالی‌که سهم گروه موسوم به هفت بزرگ (جی۷) تنها ۲۹ درصد بوده؛ نمی‌دانم چرا آن ائتلاف را بزرگ می‌نامند!
🔹
گروه جی۷ یک گروه اقتصادی متشکل از آمریکا، انگلیس، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461398" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4610158.mp4?token=UX-eMdSRMVi4d7gTeJ-EZYgVBbwa_hypAX99gQTx6Tsc2-r4VR5cgUr4GTLdeLBOleDhfA82MQDCHO-hXtlO-uT1bNQ47259By8QOgt29Ue_ZBUIlWD1U8ClazE_4qHaTNMHgQ3JMOyjy4wHtniccJZZqAO-Mly2qaHotpmt1YcaBaqyOcSP5EmL09FP5RVcp8aIWUK31z-7qhhdHrWXH1Zo_MMT6GuhTF_7RqrcVIF8Z_obejTEm01c0fOqB184Dz59_795io03XrpqJLFlWk1YdYiq6c6ruIIkfSTcAboCZW1SJUMHNwExJBVSEdonJly2Y0FJf2ZQSkzEDc2mTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4610158.mp4?token=UX-eMdSRMVi4d7gTeJ-EZYgVBbwa_hypAX99gQTx6Tsc2-r4VR5cgUr4GTLdeLBOleDhfA82MQDCHO-hXtlO-uT1bNQ47259By8QOgt29Ue_ZBUIlWD1U8ClazE_4qHaTNMHgQ3JMOyjy4wHtniccJZZqAO-Mly2qaHotpmt1YcaBaqyOcSP5EmL09FP5RVcp8aIWUK31z-7qhhdHrWXH1Zo_MMT6GuhTF_7RqrcVIF8Z_obejTEm01c0fOqB184Dz59_795io03XrpqJLFlWk1YdYiq6c6ruIIkfSTcAboCZW1SJUMHNwExJBVSEdonJly2Y0FJf2ZQSkzEDc2mTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلیپی از ابراز ارادت مجاهدین یمنی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461397" target="_blank">📅 17:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3c267ee1.mp4?token=Rf87RbghrxdZL2_9sU2RqAJbXbIICAbcUomRaNHq-izw2SneI1JTb7zr03Obei-qEPHP-VZImhALqEPWchToGXXCyTSvy4ohpOf8p1GfoMvM7JXy-0x8vSsUC1-csqNS4KH7zttcVL4e5r1d82erFMKQePmXDlPc0Nyzu7zZiyrgwUwXOGYDj9ND6s0nnDgadsdr9-C4AIZwrgbCY598tcEIhgkGN1_mJOazLdjwHyDIRYZVjMqAlPEWS95LrDgtFvc8BPijbdbyh39aus8tglpR5p3b0mVS3hs4V_Yv6pQB3-ckAT_oqHok5m13WRgIHOSJlgfZZ1XytBt6CLS1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3c267ee1.mp4?token=Rf87RbghrxdZL2_9sU2RqAJbXbIICAbcUomRaNHq-izw2SneI1JTb7zr03Obei-qEPHP-VZImhALqEPWchToGXXCyTSvy4ohpOf8p1GfoMvM7JXy-0x8vSsUC1-csqNS4KH7zttcVL4e5r1d82erFMKQePmXDlPc0Nyzu7zZiyrgwUwXOGYDj9ND6s0nnDgadsdr9-C4AIZwrgbCY598tcEIhgkGN1_mJOazLdjwHyDIRYZVjMqAlPEWS95LrDgtFvc8BPijbdbyh39aus8tglpR5p3b0mVS3hs4V_Yv6pQB3-ckAT_oqHok5m13WRgIHOSJlgfZZ1XytBt6CLS1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461396" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk4L-je1Vfl33Lv1EezHWJYR-kRPjiaSUwN9ua46bDn5XOVyF5dcAx8CDCF5qKf92Q2P3N4zI2D43kZ-DeMQ65uvrOfZj9j_y2z-b36oxDuTDj-Vi_mBnYsS73O9lO2KNewHGNIiaqXNEVXHX7-5vNnpIetS6ugwbx47aj67BGt3cESMQguOnqx6y0zd-R9e8oAJx24Tg4KC36FWzAqOM20RWJt8HwbaZxSoZUuIn1y0L_f8SdTK8FP8uThMu-A1SnJ1bVWIDSRO9P2v2TcKvMOO6ZcqjyhJiZyH0twcO4YCfJnQFhFMzD0Cn3Cse9MvGiIrFPWOlRihBVttyu9New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست ایران، عراق و کشورهای خلیج‌فارس دوشنبه در عمان
🔹
سخگوی وزارت خارجه از برگزاری نشست منطقه‌ای با حضور کشورهای ساحلی خلیج فارس و عراق در روز دوشنبه در عمان خبر داد .
🔹
بقائی گفته در این نشست در خصوص تعیین مسیرهای امن برای دریانوردی تجاری در تنگه هرمز تبادل نظر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461395" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac23c245d.mp4?token=TAzf2dEG-hhTCVvL3cANeeKVt1_c3CLTjLiaLco1v1KoHJ8tkzZSqCPWelcK9A8DAm9WBKEzKXHc8ajqnj15BqfVHjrOm-B0I9paclYRlKczaBzFlg_DR9ybTV8G0hMXBjho4RJAw-ZxlD1XWUFhv0XfSs0ymJxNc872gsM3xaZ3OjNuBONhmrzmIK08wk6tI1T8_wDIAZveaKPg4fioJ7mOCx4zU3p6cRFZeFYZf90Y5dj7gG0QjPBb9L2ym70MvQjJdtpmF5k5MrYuPNUeSIk4yStdOpAmLIRDcSRBdMT3fzcLG40S6MikInWhUJln3V2BnvuL0MbC-CQ6QKW4ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac23c245d.mp4?token=TAzf2dEG-hhTCVvL3cANeeKVt1_c3CLTjLiaLco1v1KoHJ8tkzZSqCPWelcK9A8DAm9WBKEzKXHc8ajqnj15BqfVHjrOm-B0I9paclYRlKczaBzFlg_DR9ybTV8G0hMXBjho4RJAw-ZxlD1XWUFhv0XfSs0ymJxNc872gsM3xaZ3OjNuBONhmrzmIK08wk6tI1T8_wDIAZveaKPg4fioJ7mOCx4zU3p6cRFZeFYZf90Y5dj7gG0QjPBb9L2ym70MvQjJdtpmF5k5MrYuPNUeSIk4yStdOpAmLIRDcSRBdMT3fzcLG40S6MikInWhUJln3V2BnvuL0MbC-CQ6QKW4ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز ایران و ترکیه برخلاف شایعات جریان دارد
🔹
پیگیری خبرنگار فارس از پایانه مرزی بازرگان در آذربایجان غربی حاکی از تردد روان در این مرز بین‌المللی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461394" target="_blank">📅 17:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOgRXmS6_XP_8-n0TTv-3OjOO9j0tDWHYhBiN_6fqP7P30WOW3kI_nx-CtQIoD6-vEI7SPacaBqq5619rHvZPzdOnYpsLRgOPrE1DTQfDV3-Gx4_IzSGYBhyxig-q9dW6s-91U5MqObMjozHW8pJxn8lY7lFevui2CbUyYQJdzWMRPQdAPjyXMmxzl5S0CjdoKzqGTvCVMfbhnVsf2l-rqs40NOPXBXmH1yE0p3LvStqiVQYP_aA9C-bYq-5TRmWhgqejHGB6IUgNSxyUp8a6AbjkBLWZRu_ResFtowIm2TbPYmwxrJWdB714IzPn4sBiqQcLjMrwDS7SvVcCuRVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: بحران‌ مالی بدهی‌ها برای آمریکا  تازه آغاز ماجراست
🔹
وزیر خزانه‌داری آمریکا با شعف و افتخار از تمایل خود برای به فقر کشاندن ایرانیان و فروپاشی اقتصاد ما سخن می‌گوید؛ حال آنکه خود در برابر از دست رفتن اعتماد جهانی به نظام مالی آمریکا، ناتوان و درمانده مانده است.
🔹
بحران ناشی از هزینه‌های تأمین مالی بدهی‌های آمریکا، تازه آغاز ماجراست.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461393" target="_blank">📅 16:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=coYj50ivXOPoXx4rxcMqO3y4plCtNCfBrZgrvJJmuDyZFlREAE5zfA96IYAVPl3QQRbe3IFYsyq8D9Yfk7kyasinEkiqSKUlwl0biKC52os5JCXwnL8snfqOa2k0Bt9NDj8CyCq2G7lgGL_c3-Fz0oeK9TX7AYnx3kc75ECyMRuPI2c8cZytytKjJs2QHc2-txrt6ji7E0ce-X76gt5K3nC746hjhSa4jCtpWXMH9EFxmHmBD7ig3SObc4X62CTha4yXRqwvXv_BIt3OCLoEWBmguJ5ofMha5NbEUljIm0tYlP7wMw-RrwlPClQObnkxB2tiFuzUbdIEgj5qs8ZYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=coYj50ivXOPoXx4rxcMqO3y4plCtNCfBrZgrvJJmuDyZFlREAE5zfA96IYAVPl3QQRbe3IFYsyq8D9Yfk7kyasinEkiqSKUlwl0biKC52os5JCXwnL8snfqOa2k0Bt9NDj8CyCq2G7lgGL_c3-Fz0oeK9TX7AYnx3kc75ECyMRuPI2c8cZytytKjJs2QHc2-txrt6ji7E0ce-X76gt5K3nC746hjhSa4jCtpWXMH9EFxmHmBD7ig3SObc4X62CTha4yXRqwvXv_BIt3OCLoEWBmguJ5ofMha5NbEUljIm0tYlP7wMw-RrwlPClQObnkxB2tiFuzUbdIEgj5qs8ZYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
قالیباف: مداخله‌های مالی و یا حتی دروغ‌های خزانه‌داری آمریکا دیگر تاثیری در مهار قیمت نفت ندارد
🔹
«اگر دنبال یک راهنمایی برای آیندهٔ بازار نفت می‌گردید و مقامات اقتصادی دولت آمریکا چیزی نمی‌گویند، بیایید به آینده نگاهی بیندازیم: وزارت خزانه داری برای کنترل…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461392" target="_blank">📅 16:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pegxKYkzCl-e2tRBie9rDNWk_1ZB0k9g4o2pKMd4K9FwsSZ2LAsJ_RT2-9dCQNk_VLTce55ZNbmmMcXrk1KwroqwQ2E0OyglFHbrt1jsf22tE27jdMF-sloBjos3mDWMHc9mhxN7jwdPBlO4inRgOiFO0ZjiP9lgjpc2YeuvfZGeerkT-HfOREf5sB4xzXbeCIbN0jCS8fNjUoGYhkfWsHYsWjfj6jtqd6ulDEkDi_6y8x-F5nWOsBGjN80fEs6jIGBLnZQBoVH-k6t75jZOht_WAK6746KMSE7_gojNxUuitG0Z0M4CF87nUs4fm0kpHnbjRI-MGwY0JJ2K3E1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد جزایر آزادشده توسط انصارالله به ۴ رسید
🔹
نیروهای یمنی امروز با آزادسازی جزیرۀ میون از دست مزدوران سعودی و تثبیت تسلط بر جزایر زقر و حنیش بزرگ و کوچک به عملیات‌های خود ادامه دادند.
🔹
با تسلط نیروهای یمنی بر این جزایر در تنگۀ باب‌المندب، کنترل انصارالله…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461391" target="_blank">📅 16:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks7-jbLzzyFSQEZvAH6WY_NkBGYWDkQzximtht1dYKUoDG7Z6oRqrNRXaithW4mO3hD7PAIMHomyK2spATFUKx-0y9RwCL2cAboIibC3qf79AeNHeHe-2YlrH9lClqSxTYwiZszY1wcYVQz5RpULn5UxTB-f4GiU-Ll9Cr78NrQOBTlo7I6Cd-j5A3nzFEMIFtEoInCfeIIbRmOOpmDu6lHUG0TWFqj0uOgYPC0KOr6lkYLPe6CIEw1777oyoyyhHUpJBiIlMajncG86cKQEv9PWGimLtf4yGzx0HZaebXpA5OP9nDqdmz7KMkceL-vqRKzRulkTnN31ktUiJxh54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس شهادت ابوهیثم الیازوری، فرمانده محور خان‌یونس گردان‌های القسام را تایید کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461390" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
