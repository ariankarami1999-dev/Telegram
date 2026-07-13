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
<img src="https://cdn4.telesco.pe/file/i8YK43z2eXTE5KeXgvS0kEYH8oPa8dGmhvM80gb9P29YPlqClGS_c4-i2J0OfNveJcQ7c59vgN8dWHk7aDJnyVQ4mZFyKX1QXt9paeD83s0lrfBdTw_--B5dOr3VWZa1Yc2722IYxri-xn8KqqBu3D1Tcz4vZ4UUt6a_v4a0xzXmWhYeuZ_j3YZ-ChAeyrgzKOvBVBzEeR5baLietXKMi_Zs3BjZqU6oQtpDrendq0UHLfoLDep_yqjGSEFjW92ofFrETUnJaKPwIMs6lSbabt4Hgb6XVvJk14KQee_PfQRVomAycKTMpFpPBfG-DTRCp2ZILHOqP6OvjD2P4jMsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 918K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-133802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پوتین: پاسخ روسیه به حملات اوکراین، متقابل و چندین برابر قدرتمندتر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/133802" target="_blank">📅 17:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f130a67f.mp4?token=vSx8AiiW2F6Qug_gjd0L_aRD42hFCu0GyvwCR7S28FcPtxiDq8_3qy3HjelZiZFdcWIouo9m841jHtYQgip4ryFv_p195HfLLXXHFcH-snC6l9NchDlD2VJNDvLNxvRzxdpUCf0FpSrrcLnv5MjuDKWlUu5LknR_MZllMIxBKMucv-DRImjypYh-YHz2WM-0WOTwftD6KMe90XDTvRA8rClzFeT82T6alqyfvDZPXt2UKMBvUO9scPngJkcztFJsltz0l34Si_fm2im-vYaBtDvgfCpZHwgei2DAn3IahZAfFgjw-eVkArpNCRjwGVJZ_z7TczK0PkP3OizDFfIFWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f130a67f.mp4?token=vSx8AiiW2F6Qug_gjd0L_aRD42hFCu0GyvwCR7S28FcPtxiDq8_3qy3HjelZiZFdcWIouo9m841jHtYQgip4ryFv_p195HfLLXXHFcH-snC6l9NchDlD2VJNDvLNxvRzxdpUCf0FpSrrcLnv5MjuDKWlUu5LknR_MZllMIxBKMucv-DRImjypYh-YHz2WM-0WOTwftD6KMe90XDTvRA8rClzFeT82T6alqyfvDZPXt2UKMBvUO9scPngJkcztFJsltz0l34Si_fm2im-vYaBtDvgfCpZHwgei2DAn3IahZAfFgjw-eVkArpNCRjwGVJZ_z7TczK0PkP3OizDFfIFWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی عجیب سالها قبل روح الله زم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/133801" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خبرگزاری دولت: قطعی برق در تهران بدون اطلاع قبلی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/133800" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های کشتیرانی:
تعداد نفت‌کش‌هایی که از تنگه هرمز عبور می‌کنند، دیروز به پایین‌ترین سطح خود در دو ماه اخیر کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/133799" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فنلاند سفیر روسیه را احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133798" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش فایننشال تایمز، دبی برنامه دارد تا با ساخت بندر جدیدی ، تنگه هرمز را دور بزند و وابستگی‌ به این تنگه را کم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/133797" target="_blank">📅 17:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یمن حریم هوایی خود را تا اطلاع ثانوی بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/133796" target="_blank">📅 17:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z68vfA1BbPuauvCwz_zh0vGJWqMVq_gNVZuBFYrPMHuGAWA8EkqVNKzYBx_X5e04k-9u7r9AeqIHShe8qM7v0IexYr6MTOZPAkhjJKSqLPie0QGXykCSukYYaSWRVFQ7m1E8MCVjlBnf0o9rEPOc1Jr3kMdTqeaym5JZYAMo18VPMSj8yofPWKlc4K0HH_x9Py0ovVMx6FK2RgOVG_NlZmEvcfbisGzP4-XvE1TROZcgwzX44tf2OnM50QePqfTGWmgxzJAffiNlcmp924xc8voICm3402cR_OT9W1_8WDdbW1tUnaUJHhWkoviv3IKV91CPegQeCq53aTboyDhFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه نظامی حوثی‌ها: پاسخ در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133795" target="_blank">📅 17:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmsBcXHzFxndUER5RDXAajaGil90y1wU4837GFZCy-916uiLJzjpSxMGWyHNUji86TAIkqrNROlSjMdhBeioEvtnv7XfyWqyO4mZw99ZmD8MfjR0J6GpwhUb8Y3-JVXYMJoT089-wGZfUsBC42_axLtydjlgjFqPcnDk_ZB_h3bT5vA6_0ZUjf7HX_NXNYXNMhD732ERyhGsGrjPLL9CIq1iQyUgr9YdVfx7XmwnZUXZoTwZkbM8eh1Vy7172VftTLnNal6O79VJJ4aXUlDwwoLrJtj4t8kctlFxnFiM4hrtnNGxNAXkjzAb-RQdlNTdwIBF6wLPAiStI9AofsTojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، کاخ سفید خود را با کاخ سفید دوران بایدن مقایسه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133794" target="_blank">📅 17:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOjevY-eDf7kO7M1hIZi9zYm-EqIubAPSdIEV_luuPCYSKg61n7WFb7nEJbUgpsaBm3k-m66Nzy_wB8gfcgkaCeJWxxPTlZmNvAFxoLjkXwJQH2TrthlRo_p2HZ3YLAiPx9EiqiddrKoMWCbMRwnJNk4Rc_aiXlwT3BWtNMokCAvy8oLk_wnCF9wd3jr98QGfaOhM-MvtIORit0u0WyGhJwiMT4Wfj3HGnN4A27wt2AvJMjPRgoaZUl4Yc06CaaWDwU2J3ArMhGAScyG5KfjArHDzYOyezrO68wnO_8T0m63paqy0EyOQLp7Y6dh25UQr-Yg9SPcXcrsUH9uk1MrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ جنگ با ایران رو شبیه یه «مأموریت تنبیهی» توصیف می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133793" target="_blank">📅 17:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf39227ea.mp4?token=Jd9FoiTFFr5nxOUmHNxZG9qL5fvoJoO_aG6xOYSjkKqyOCzqStXxgKtGml-lZVZz2LnneJTrjypqnG1oSpzBeaaqFbelEAJKxxFh7bVFOjVv-bTHkiLpDeaad6-ht_paJW9ktty2zIgQhjcCiNREautISBy0FI8_suM1mRGsztMgV8NidCY2XI2AY_sM235NVHFPShIOLGb-THC608l2PJPATfX4AzGezu8l0QaIejKsxkERofnzDF5PEf-cUknkDJkBQinC-_hiFBvxpPfyVaocSW3ativDwbHrHMmgxB6J___I36ba9S8aHRxXSEwpwgbrD8YTYZHcMwnfqWhUjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf39227ea.mp4?token=Jd9FoiTFFr5nxOUmHNxZG9qL5fvoJoO_aG6xOYSjkKqyOCzqStXxgKtGml-lZVZz2LnneJTrjypqnG1oSpzBeaaqFbelEAJKxxFh7bVFOjVv-bTHkiLpDeaad6-ht_paJW9ktty2zIgQhjcCiNREautISBy0FI8_suM1mRGsztMgV8NidCY2XI2AY_sM235NVHFPShIOLGb-THC608l2PJPATfX4AzGezu8l0QaIejKsxkERofnzDF5PEf-cUknkDJkBQinC-_hiFBvxpPfyVaocSW3ativDwbHrHMmgxB6J___I36ba9S8aHRxXSEwpwgbrD8YTYZHcMwnfqWhUjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه: در حالی که بخش‌های روس‌ستیز غرب در تلاش برای مبارزه با روسیه هستند، این کشور همچنان به روند توسعه خود ادامه می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/133792" target="_blank">📅 17:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvBS5re27p75smDZ3M6GTYBs2L79upVF8SmNp_-CXrOIBZFrBG7GFUuUv7WwRxoXykL26v4_SWKguQQ0nWIW6eRQvONUFr7FdHcf2OgaVdU_-j9QXuyp5Q6GGt4mgbJ3M7NXpS7Drdrou6Dny01LwxuHp2nrImN_Y2c7-HuDL9N7Eg6Uv3u7Jy9A9d1moUAMfB_0G2UI_W_Y9bTlJbiV-ic_0QrnvaRiN_LpePatsqrOV4PsHFGQygNaB8tQgDDClkATmsoeJm2P2rOQmTvFObd4HlUtRdUmmGoP5TCwJCpFk9ez2tz28DP8RqiqPgjgNTdDC17psfOl0SUVeJ4wrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت دوباره رفت بالای 79 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/133791" target="_blank">📅 16:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانه های عربی: سطح هشدار در تمامی فرودگاه‌های عربستان سعودی افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/133790" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNynf3Vmflp4JcDO236xMp8e7gPV1QM3IKTDLCNbJoyIgczRk6Mw7h56guGFgMXcvyMojLQ9_jgbRp4otWMTvIhXur8RilIOk2xsYWCWcZoIt71FzFOJz86gyyAgZYXkCXei0lNNxO7sqUnKCiAbPgPMDKzZFHFcdr7ffGSZhieIfe66C5dDD5Bx4TU_zlkYomgnz6OvL2QNaGNbkqfka-do27G88pka0xnwZ7yWvafj80BFVjixJj5WCI-YEZaWX0Xq_24jUi2MrjBTvO0EuwKvEMbJn305EyBxZ9c1-OOfn61texLBxOJJc0WDCGoCdc2Il5pDXNGsBr2vuvkSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWf-OJ7JcOyGY8K5h6JuSfAwUfxPwTUShfQ60fz-ChHak94-0c3qAmtJKBR-01bgWaqvoFnqdd13UTeJ7CgnYY24f-Z8fjFFT3YDnXs386FkinuOtPcdjhTnyU8YN1vPNMmPSs62nMK104Fz8IJdvWfoC65Xd5hZtc7FKCm0AfKCRR2vxzkj21-UbmT2hYVtusMW9VhEE-S2VuM8Bq0K05yzZYOXtFBK9kx8QXQKzwqB4Z6EqgCwhvsmFTp9HicSaysXcbFGxMbergvcI6Smod2fUiWJzyzLp5QpSLSaqINbPFJr1MBQHfagldam9rq5pY3Wo53rzU7AHngGdNl9Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترکیه و مصر یک توافقنامه همکاری امضا کردند که چارچوب همکاری‌های آینده آن‌ها در حوزه صنایع دفاعی را تعیین خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133788" target="_blank">📅 16:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزرای خارجه آلمان، فرانسه و بریتانیا حملات ایران به کشور های عربی و همچنین ناامن کردن تنگه هرمز را محکوم کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/133787" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی قرارگاه خاتم‌الانبیا:
نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/133786" target="_blank">📅 16:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خاتم الانبیا: مسئولیت همه ناامنی‌ها و گسترش جنگ در منطقه، متوجه آمریکا و کشورهایی می باشد که با ارتش جنایتکار آن کشور، همکاری می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133785" target="_blank">📅 16:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb0fc1149.mp4?token=VHINaSKFNYsEgvQesWr3aHMP46iGNlNmuWgWfWeCiRBdk6fBUOYkke1ue2tlqfPFxLzFJQiTUapKLt0FCZ5S13AfSPa5zL2Z2C4vAgF4dicfNnEulGDreggdm6NGjFYDS6kKgxKDuZB2dd1EFkNAgi2MGkDcw2bQvSJ5xgwDXGE7nQbYmo74UXW29amvi8MTOmS1nnXpwQxPX4yGs5-WAXNFRNeV_2Rp4THvtPUufrRHQ83vc2UycmGj0yaa9kuYIjjHqmbKAK4w9r45iLcS8cXVUaGh3QSm6arNFtEP5-H1LwgmSYQX_IQYpwOSkinQ7ANV5Ow5j_cElWV68To-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb0fc1149.mp4?token=VHINaSKFNYsEgvQesWr3aHMP46iGNlNmuWgWfWeCiRBdk6fBUOYkke1ue2tlqfPFxLzFJQiTUapKLt0FCZ5S13AfSPa5zL2Z2C4vAgF4dicfNnEulGDreggdm6NGjFYDS6kKgxKDuZB2dd1EFkNAgi2MGkDcw2bQvSJ5xgwDXGE7nQbYmo74UXW29amvi8MTOmS1nnXpwQxPX4yGs5-WAXNFRNeV_2Rp4THvtPUufrRHQ83vc2UycmGj0yaa9kuYIjjHqmbKAK4w9r45iLcS8cXVUaGh3QSm6arNFtEP5-H1LwgmSYQX_IQYpwOSkinQ7ANV5Ow5j_cElWV68To-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه بمباران فرودگاه صنعا توسط جنگنده‌های سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133784" target="_blank">📅 16:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اظهارات ترامپ درباره ایران: نرخ تورم در ایران ۳۵۰ درصد است.
🔴
شش ماه پیش، این نرخ ۵ درصد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133783" target="_blank">📅 16:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f9f23c23.mp4?token=fp2sQ0Z5s150FtNU4-Fhm0Rbx2RRoYgtifnJqjuf2jR6LfygHUbygPwEou7w7viQljISvZ41d3i1V4BiWksMIO-05ISMXhyXu8P_gVvNM4HeqI7qSVBFbqxtheDE0wt12c6FVpDg9dSjvopJovabiSCXBNIrM-_CDXmEyylSCYNahUlX_TsnbTPkImgkyJa5Lsxw132poRngPmzvueATpoUYI0kkZnst_RS7eZioNEJwSGfIaAFiHmaKx_Ys9c89dVvnpZhUw-ei07eanTGICBuwUGieB9nizKp2VlzaWGsapWgFTakUZ1ipdM1h-aVB_zXtW6_tRH9g4abbs89dvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f9f23c23.mp4?token=fp2sQ0Z5s150FtNU4-Fhm0Rbx2RRoYgtifnJqjuf2jR6LfygHUbygPwEou7w7viQljISvZ41d3i1V4BiWksMIO-05ISMXhyXu8P_gVvNM4HeqI7qSVBFbqxtheDE0wt12c6FVpDg9dSjvopJovabiSCXBNIrM-_CDXmEyylSCYNahUlX_TsnbTPkImgkyJa5Lsxw132poRngPmzvueATpoUYI0kkZnst_RS7eZioNEJwSGfIaAFiHmaKx_Ys9c89dVvnpZhUw-ei07eanTGICBuwUGieB9nizKp2VlzaWGsapWgFTakUZ1ipdM1h-aVB_zXtW6_tRH9g4abbs89dvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خمینی و سلیمانی رو اشتباه گرفت: من خمینی را کشتم، که یک ژنرال باهوش اما دیوانه بود.
🔴
ببخشید سلیمانی من سلیمانی را کشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133782" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: نمی‌توانیم انتظار داشته باشیم که کشورها از ما بخواهند به صورت رایگان از تنگه هرمز محافظت کنیم، همانطور که سال‌ها این کار را انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133781" target="_blank">📅 16:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3755f54a.mp4?token=nLKRZfgw28H89_JFkAvl2OB8EXfTAXcYURrGy7xr6XzdZxLZr4BcypxupS3IY1omiA2QBlQt1cG9Vb1GtbDSUjixQSpGk1YVRgl3fmn1icCtjNUPzrBZJfzPDUYAEWPqs6UVFpLMJQOwqvMWenfepoxNVcNDIbTsrKqVJGxA9oc9FnAjiWse7FxxQiy06CeynjbV_3EvxkQGzlXOM_6WuiEjASjf4T-2r29cIpJCo13-SX1-IqLnODbB3RwIX46-2htr5XfSxngCHTvfYRvtodbOnvVfgRUmwEyrAlQqZsW-aeb7zx9vK--c1DX0oC8jwLuFK9Wxq8hcDiFfmz95Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3755f54a.mp4?token=nLKRZfgw28H89_JFkAvl2OB8EXfTAXcYURrGy7xr6XzdZxLZr4BcypxupS3IY1omiA2QBlQt1cG9Vb1GtbDSUjixQSpGk1YVRgl3fmn1icCtjNUPzrBZJfzPDUYAEWPqs6UVFpLMJQOwqvMWenfepoxNVcNDIbTsrKqVJGxA9oc9FnAjiWse7FxxQiy06CeynjbV_3EvxkQGzlXOM_6WuiEjASjf4T-2r29cIpJCo13-SX1-IqLnODbB3RwIX46-2htr5XfSxngCHTvfYRvtodbOnvVfgRUmwEyrAlQqZsW-aeb7zx9vK--c1DX0oC8jwLuFK9Wxq8hcDiFfmz95Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
رژیم ایران ۵۲ هزار معترضِ رو کُشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133780" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ در مورد ایران: ایران در آستانه دستیابی به سلاح هسته‌ای قرار داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133779" target="_blank">📅 16:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ :هر بار که ایران پهپاد پرتاب کرده، نیروهای آمریکایی پاسخ بسیار سختی داده‌اند و ایران تاوان این اقدامات را پرداخت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133778" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61353409c.mp4?token=j8_ul6p9WyumbcCSY9ZRh8N5XQezfzZy8fJcEIfOuSASbEQmg7jYN4CmVWDi7Eyv8Fc_jkkMfsrpxFqUiIJem8vMqKgybx6t5GtALkdm_7yY-IdhYFuGWTA0UHo8qZ_k6mtSnXMh9yt8IuT5qXeCs5unWmgAFwOk8vtz5q38R6O3NW3ZJC6U8OYouCxQFbt49xyUBE8Eh8-rsAu5n92px_iNIJO2bn6NwSSEfEv1x4dgpv9RbaBQsNTzXHMTmkjjff9MCEd2X6Tn7WU4B_t_uZCj81iO_05DGzi-j24WEmfvnmy-FUt3YNtlOflyRrcdfgi6o3L8QspguGWNjDjBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61353409c.mp4?token=j8_ul6p9WyumbcCSY9ZRh8N5XQezfzZy8fJcEIfOuSASbEQmg7jYN4CmVWDi7Eyv8Fc_jkkMfsrpxFqUiIJem8vMqKgybx6t5GtALkdm_7yY-IdhYFuGWTA0UHo8qZ_k6mtSnXMh9yt8IuT5qXeCs5unWmgAFwOk8vtz5q38R6O3NW3ZJC6U8OYouCxQFbt49xyUBE8Eh8-rsAu5n92px_iNIJO2bn6NwSSEfEv1x4dgpv9RbaBQsNTzXHMTmkjjff9MCEd2X6Tn7WU4B_t_uZCj81iO_05DGzi-j24WEmfvnmy-FUt3YNtlOflyRrcdfgi6o3L8QspguGWNjDjBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اونا یه مشت آدم بد هستن، اینو مطمئن باشید
🔴
من معمولاً این‌جور حرف‌ها رو زیاد نمی‌زنم
🔴
الان هم با دردسرها و مشکلات خیلی جدی روبه‌رو هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/133777" target="_blank">📅 16:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: ما دیروز یک نشست ۱۱ ساعته با ایرانی‌ها برگزار کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133776" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: این یک توافق قطعی‌شده بود، و بعد آنها آن را شکستند. آنها همیشه توافق‌ها را نقض می‌کنند. ما با این افراد ۱۰ توافق داشته‌ایم و بنابراین ما فقط قرار است ضربه بسیار سختی به آنها بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133775" target="_blank">📅 16:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ : بایدن به سمت ایران متمایل شد و همین باعث شد ایران قوی‌تر بشه
🔴
ایران به خاطر سیاست‌های بایدن خیلی قدرتمندتر شد
🔴
البته به نظرم خود بایدن هم تصمیم‌گیر اصلی نبود، چون آدم باهوشی نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133774" target="_blank">📅 16:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: باید 47 سال پیش علیه ایران اقدام میشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133773" target="_blank">📅 15:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ : ما کنترل تنگه هرمز رو دست می‌گیریم
🔴
احتمالاً این کار رو انجام می‌دیم.
ما نگهبان تنگه هرمز می‌شیم و این بار بابتش پول می‌گیریم
🔴
۵۰ سال از این تنگه محافظت کردیم و حتی یه دلار هم نگرفتیم، اما از این به بعد ازش درآمد کسب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133772" target="_blank">📅 15:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ۵.۲ درصد از رؤسای جمهور کشته می‌شوند و ۸.۵ درصد هدف گلوله قرار می‌گیرند.
🔴
رئیس‌جمهور بودن خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133771" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ درباره ایران: اوباما از همه بدتر بود، چون اوباما واقعاً به طرف آنها رفت؛ چون، می‌دانید، او یک، خب، بهتر است نگوییم. بگذارید آن را برای زمان دیگری نگه داریم.
🔴
ایران مجموعه‌ای از "افراد بد" است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/133770" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / ترامپ: ایالات متحده قصد دارد حملات جدی علیه ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/133769" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ایران از من چیزی دریافت نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133768" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: ما عوارضی را برای اسکورت کشتی‌ها در تنگه هرمز دریافت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133767" target="_blank">📅 15:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ برای  بار هزارم درباره ایران: ما یک توافق داشتیم، و آن‌ها آن را نقض کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133766" target="_blank">📅 15:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: شب گذشته به ایران ضربه بسیار سنگینی وارد کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133765" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: ما همه چیز را از ایران می‌گیریم - نفت، طلا، زمین، غذا، همه چیز متعلق به آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/133764" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ: رهبران ایران مذاکره‌کنندگان حرفه‌ای هستند/ما کنترل تنگه هرمز را در دست خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133763" target="_blank">📅 15:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMg4ZpMB951XnGzTjahri3x2BN-cmFSIEd1sL7rpI--E4-AzVpYEI9NXXvFiThSTFSXEZh42mg8KxkFGUUBQTjwpe6uMysJy4wH--mq-bcpwRtoKnkyNOpLk8mgeSwmbnSr2_-92DOxsKjfHAOo6XubBTD7EX8OCE0JfKTFENohZj795N9MsaAfIz8JDCrsd_LBwdQiBidX_uMBeFsZgMNU00yeU5JTnzQRipGYikx-EVwpT16D17lWNZEDn7JWqXmHFeMaxrCQek-5KMU9kw2hQFM0zWee01sH-HGP3rnp04wJuaAU6C3NsPOhRJRfyLD-MLFICMIxSD9KFZkGazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a550f8c82.mov?token=CpSrgJPDd4Hvddprvhcby1Ygc2Qa89tK1RP9YsrvEY7adG693BFgP46MJWfhURSaElB73rowGniZ4SSCDKvteP3xuTRfYsEJMQ850FhqcfxlzJGdlQJ9pnqd-iVvmOw7sxnxzZ_Qwvzpwea01n9exX5UU7KhciM9sdV2JTjQ2Od0JAvcuY46PepJazdC_kUh7od29Guc9ydxCfGK50j3bcXJThSiDo6_BgYMo5NafXtSwtW2X1n-9aIDDNYGjnU3zjtIgMQhlZJpH4hicKjhygWUYFEZyf6O8sMUgzYOx0hEPOwcsdPk9VD7DkXYo4LP_AXWXVfHcCydHfbu1-GtzpuRM_00FpF-OgV89OvMSno_FyiDWseBmtKSStApHU5XxUvmHVDvrzYvdt06hnduJpKDuXnL8EDcUwBN8rqkDKW97W6E0Nxv01d1XtXeSdHmyEFa3pLyhP0aiVpJe9UaCyj1As8GJYNoUGQIdN3RDQDh0cigit7l3xwKzu2XrbIDpVNFQ8YsXv3MJIITtsoC_-PmhdmClJ5ZlSrTv9vEpWVAK5R024whgzGctxsD-ro7hcVBKuCmDcf_4m7Wmyw5_XMNCbKQB89bmq5fYAVzfTG249saLJ8P_ke3TL4_1B5SSv7oY_jpapfD7DOp9j_6JR-R7pT5uGMPFDnw-A97a00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a550f8c82.mov?token=CpSrgJPDd4Hvddprvhcby1Ygc2Qa89tK1RP9YsrvEY7adG693BFgP46MJWfhURSaElB73rowGniZ4SSCDKvteP3xuTRfYsEJMQ850FhqcfxlzJGdlQJ9pnqd-iVvmOw7sxnxzZ_Qwvzpwea01n9exX5UU7KhciM9sdV2JTjQ2Od0JAvcuY46PepJazdC_kUh7od29Guc9ydxCfGK50j3bcXJThSiDo6_BgYMo5NafXtSwtW2X1n-9aIDDNYGjnU3zjtIgMQhlZJpH4hicKjhygWUYFEZyf6O8sMUgzYOx0hEPOwcsdPk9VD7DkXYo4LP_AXWXVfHcCydHfbu1-GtzpuRM_00FpF-OgV89OvMSno_FyiDWseBmtKSStApHU5XxUvmHVDvrzYvdt06hnduJpKDuXnL8EDcUwBN8rqkDKW97W6E0Nxv01d1XtXeSdHmyEFa3pLyhP0aiVpJe9UaCyj1As8GJYNoUGQIdN3RDQDh0cigit7l3xwKzu2XrbIDpVNFQ8YsXv3MJIITtsoC_-PmhdmClJ5ZlSrTv9vEpWVAK5R024whgzGctxsD-ro7hcVBKuCmDcf_4m7Wmyw5_XMNCbKQB89bmq5fYAVzfTG249saLJ8P_ke3TL4_1B5SSv7oY_jpapfD7DOp9j_6JR-R7pT5uGMPFDnw-A97a00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از یک کشتی باری غیرنظامی با پرچم توگو که امروز صبح مورد اصابت پهپادهای انتحاری "گران-4" روسی قرار گرفت، در حالی که در حال تخلیه کودهای معدنی در یک بندر اوکراینی در منطقه اودسا بود.
🔴
گزارش شده است که ۱۰ نفر مجروح شده‌اند، که حداقل ۳ نفر از آن‌ها جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133761" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
دفتر سیاسی انصارالله یمن: در اقدامی تشدیدکننده و خطرناک، عربستان سعودی به فرودگاه صنعاء حمله هوایی کرد تا از بازگشت هیئت ما [از ایران] جلوگیری نماید، اما در این کار ناکام ماند.
🔴
جنایت هدف قرار دادن فرودگاه صنعاء، تجاوزی وحشیانه علیه مردم ما، تعرض آشکار به حاکمیت ملی و نقض قوانین بین‌المللی به شمار می‌رود.
🔴
هدف قرار دادن فرودگاه صنعاء گامی است که نشان‌دهنده سطح کینه و جنایت‌کاری رژیم سعودی و پشت پردهٔ آن یعنی آمریکا می‌باشد.
🔴
این حمله در چارچوب تحقق خواستهٔ آمریکا برای تداوم وضعیت محاصرهٔ ظالمانه‌ای صورت می‌گیرد که بیش از ۱۰ سال است برقرار است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/133760" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyV883juMicvMd7z0d7uiZecoV0R2RIFNueZz8D3ygBGWCA2HL8lrvT6rG0mJ3LEm4qlMxItv00__O45DGbHHmWFMguLO1PDYJKoAwMs3ZrcHFjIcSXW5w-Ur7ugE7vD3MM0Vyy12FLox17vqiTk-owCPRLvL4hh-MAhI3ispHaHDUACAK5nReTpHZ9AzQsGMYNiRFT-VJmZ42LIl08t20mAkYPDGcG-2ThLFn_Z0C7sBViAPMguZRNdx97XtCtsw0zICl2ZgkFvwvTwMa1P57KP30Bk7qDJx_5u3aITDREDlDj2YfsLHzGVDlH8q8F95e8dEdi2uvPmWqmtlVKTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون هواپیما ماهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133759" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvG26_e974S9EmixhUPOtMv7-ZdUvOMdPjFv_F0WsM3em0FcWG9s77i5hF0nwnhWCWsUrpLGpoe3HG6jUaooHJ0s2AaV62wH0AzCw0HZpzOZqcNZTTLd6D2-2vMaDQeEJm0Dkl8iB4WqHZkJ2DTQdbscQCyitGWpacgUPUiHNFCK4a_t0MIMrjrrQxkpTSzoty0AUWM4h9H5rwM9F146gnStgX5Jso0NO3ejfeI3E-43_voL6_aaaVP0kWOnanbAd2weGnQZC9xcvlWjeYlAUaPz6UeFQOmQ6QniIj5tpSvGMajbaxLcX21IP-dJZEVaStCJ7mi1qynxKvllnNE39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزام الاسد، عضو ارشد انصارالله یمن نوشت:  هواپیما به سلامت فرود آمد، هیئت اعزامی رسید و محاصره با قدرت شکسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133758" target="_blank">📅 15:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / تاییده نشده: برخی از مقامات و فرماندهان ایرانی برای ملاقات با مقامات انصارالله یمن (حوثی ها) در هواپیما حضور داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133757" target="_blank">📅 15:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر دفاع یمن اعلام کرد ما به هر طریقی که شده با ناقضان حریم هوایی یمن مقابله می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133756" target="_blank">📅 15:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فارس:  هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133755" target="_blank">📅 15:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فارس:  هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133754" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
حزام الأسد عضو انصارالله : رژیم سعودی متوجه خواهد شد که خودش، قبر خودش را با دست خود حفر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/133753" target="_blank">📅 15:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا: یک حادثه در فاصله ۵۰ مایل دریایی جنوب عدن در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133752" target="_blank">📅 15:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jY-Z9zZo6qtC33fFPFvmRnvRX0N8cFz_rpf4OO3OBgTxuj-quj0yjObbPQeFdbLJV0CGsgU8rEpslnENX1aSniSyQ0eBy-XrO43xTiRk6FdequorsZzlejndspHjz271Q7vXuMLI2_-Ue4DaX5SEX3EaMIWHhsp8uIs5QBsw0PF3YvPRDKLdtoB6xDLd85sT-PsOV4BaYN8hTo8QfzDjQASOI4oXbIIG7TOlsvpUItbDZa5gls6lwt5GjGYQs-jLWzzPIPY8VeoIcgqgru-mxpkOGlkQ7NVs3ByLdbjlSTXhMhNDZ0vmyucEXTjU1PZSrNPzEmDsRAxwvOrUmt7zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا: یک حادثه در فاصله ۵۰ مایل دریایی جنوب عدن در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133751" target="_blank">📅 15:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / عملیات یمن شروع شد
🔴
هدف قرار دادن یک کشتی نفتی در سواحل یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/133750" target="_blank">📅 15:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/ بریتانیا رسماً سپاه پاسداران  را به عنوان یک سازمان تروریستی معرفی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133749" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یحیی فست: دوران کاهش تنش تمام شد و بزودی از عربستان انتقام میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133748" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت امور خارجه دولت صنعاء اعلام کرد که عربستان سعودی اعلام جنگ کرده و باید مسئولیت کامل این اقدام را بر عهده بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133747" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت دفاع یمن: شبه‌نظامیان حوثی مانع از فرود هواپیمای ملی یمن در فرودگاه صنعا شدند و بر نقض حریم هوایی یمن توسط ایران اصرار ورزیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133746" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133745" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133744" target="_blank">📅 14:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133743" target="_blank">📅 14:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6kPVhmQtOOQh6iutEgvShDhYqp8zSQVJptjFPJ8SS_yiz170VS0fbt7rI14_e8y6y_FbQRM6HXJuQImeOtc9CoGOGRh9kYD1UdR99kQRmzpVankiMdkZtE2W3J-nn9CC70MtxW7SugY-3vHzL1GVwCzMpWbekqaBG9_iFHfvsvsEg0APrXdO4qJIB06mk2DJctnQHs0va4ocpQL_EZqQJejRp9jzDpVAI9y1szNRw5dfTiUr30Po2_FAQtMmBXES8jopjSSQaS0h9jzOIfeMDr_HBd32Gmt1K2RVqJXRaK0twlzAXmohNnRbs_g6f6YdLclmA1oB_kxTpsbM1tz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۳۳۰۰۰ نفر درحال مشاهده حرکت هواپیمای ماهان به سمت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133742" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133741" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: عربستان به مرحلۀ کاهش تنش‌ها پایان داد
🔴
حملۀ عربستان به فرودگاه صنعا بدون پاسخ و مجازات نخواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/133740" target="_blank">📅 14:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kmrv2NPMB89h_AsUlAihEZuB6sVBWvx0KHwaXqj5k-0p28aLkQtqyWy5djMYXATxsdq7jozkgGon91exHgZcekARdukA-x50S3AXpDEkxUimx_JlLi99rvvPmiK4q6wF4No7lWaw1NYTLVSY6nVwlLVzlXVb_D9ykEECX0T8spAkwCzgfkw_Nm3p3BMiDQcaNNDX4WEyGjqYrTaxy83xHgxlOicCbieGcQeGG-GMK9K1R2vNvKSkYk6SV9vQ4nZZg5iaaofSe4Jnyc-geDKEKNZf4zou8Jbe8uu3fdFiiYXITI0NuNOn_B4v_C6rDhnmIh5NnBWeUf-5fCQN72iuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/133739" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEaW_QLCyjMwHMVd-s6irPdZFFE4851sJuR1bfqOz2Xn43paKJPT6FOGzA_04__o_S6bNJM8nX4kukBaZVYgZWe53pYJripcmSPK4Jm2z7sdb6owSpnhMdOx7SlfsRNOQJ6DpcLB8IWjOSe155vkaxa_8WCeVIjG8gVnoDSAQodfJo71o8qg5lT_fUamS-7_BvxmAexXGqnwuFYKmNRgH6qA2vnxlmrTsERO_4iYKLzHUh2dNHRBPlA4rB51hblBkgTiMFS2AhnoF2Kbz3aKq0yznCcNisZKuMShUsIP7YYzUUu8Q_k0iwd68ttHQx9koY2oIkNvdcFRuugaFT0k5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiMZMT69Pmb7qY7y-O1uGr28CowRiCRK3JxHlYHx8zPp-bNv8GZDH_SeKm2_MZLUD6iVYgT0xl4arK_vQIH7BaGzw7ksNIz43YeXYh2qrgDrISI2YSk26a71JlNv5hASB0gFBKhXjIV-1X5n-pRF9VDiuv8IFEQEvYZczyikjapQl2Ll8XQszpBQ4lVOAwe5CGD9EIFSALfi2rs33DaJIGYJlNvYp88UEHP9Y8BmNQl7LMw2YeKpBmZwc0i1OKcuz0weP4KpczAZcHnd1eOvX3r0GklYPviSBG9JaYLdd4PSXhHG1iRlfPsAOzOYy15YpNVZZOoJOOk4ALl-cm8jmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/133737" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TypotTyIuj3bEKeFAIPLG03wPXRHHj27iMQh5XoKv0Y2gwlkrzeE060q7TKNOnae5D-v-4QNJIMEE-GAMpHwZvWHinUuZvyX5UtMXq_vKlqET1DhhQI7QYjVTp82HykiMyGi-r8buFZAgvXJZSNP3c4_pzSD81AYTygOTxWPg5BWc3I3AP4nuzH_3kXh3CJHDEaFJZP2PEFlIZbYpa5k5BhjFGbXL8wTgjb_XHRiWhEjISY0nzZXmfo8qv03zpor2v-52vBuRYQekwN1OItI3qst4JTDZUN5M49n8ENZfRczF4BKc-jdMmbcavaTd-70yjpqSW-FM22OsCvDvUcfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های سعودی، فرودگاه صنعا را بمباران کردند و دود بر فراز این فرودگاه دیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133736" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔴
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/133735" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
چین: تردد از تنگه هرمز باید به درستی مدیریت شود، تنگه هرمز یک آب‌راه بین‌المللی برای کشتیرانی است
🔴
از سرگیری هرچه سریع‌تر تردد آزاد و ایمن در این تنگه به نفع تمامی طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133734" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صداسیما: تنگه هرمز به دلیل نقض تفاهم‌نامه توسط ارتش آمریکا، همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133733" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر دفاع یمن: با تمام توان با هواپیماهای متخاصم ایرانی مقابله خواهیم کرد
🔴
ما ایران را از نظر قانونی و اخلاقی مسئول نقض حریم هوایی یمن می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133732" target="_blank">📅 14:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
صدای انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133731" target="_blank">📅 14:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7c6c71e3.mp4?token=OxVou1YjIXsaIirGz3I2DgrRuN2WmcRM6sXaxMOhEzPzq3y04UcXsnNqhFFWaC-0FBEl9uA7C3_0269GYnK8MRSpJWMg7a_YEABWFNne2ZLga2UK_jMBUgXRjN2nvah1U1zWmr7-MV4Xy_xNpS4Gflb7cNyVOJI90QQSCgnJp64XWYhUOQ-z3q4D_h_8YIUulGvsKG0S-_3SYin_tRY9F6CL8cjUE7ftnrqghfH87uc3robCZrPTaYrHgDQtbjn_vwiWD_uMvJ9I2v1A30GzBFhchBPnq_YvQ38EdJwSMffS50jN2jfRVxt-sntDHSS7J5cVJshrsD8_UHhUVVSR1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7c6c71e3.mp4?token=OxVou1YjIXsaIirGz3I2DgrRuN2WmcRM6sXaxMOhEzPzq3y04UcXsnNqhFFWaC-0FBEl9uA7C3_0269GYnK8MRSpJWMg7a_YEABWFNne2ZLga2UK_jMBUgXRjN2nvah1U1zWmr7-MV4Xy_xNpS4Gflb7cNyVOJI90QQSCgnJp64XWYhUOQ-z3q4D_h_8YIUulGvsKG0S-_3SYin_tRY9F6CL8cjUE7ftnrqghfH87uc3robCZrPTaYrHgDQtbjn_vwiWD_uMvJ9I2v1A30GzBFhchBPnq_YvQ38EdJwSMffS50jN2jfRVxt-sntDHSS7J5cVJshrsD8_UHhUVVSR1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل ویرانگر در شمال شرقی چین، خودروها همچون اسباب‌بازی با خود برد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133730" target="_blank">📅 14:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfb74VW4f2oJF5MHbYjlH1GL6uoBBXyQNw0yKg8PHlGbt-U0CD-pVxn3uOq2008xgrhpC7oq0K7oTwrqvhsdegk7W1Zx3x6kdJr1pHBUarIgDo-_Hqqk-AF0Jn_xfd1xebXI_NGh4alw-jwdBYtKoAvt6sU0bzpR486rr-yE8IhuIJLY16DI711QpwWtlPWvFpZ5puF-HEkh99TkxJFQPh8JnMK7NmBsX8NFuaAPffPW_ymqYl4kfvijJuZDV-sF9rSOuqD4_tiYpO6SF2cpfN56ELAmDGayskHnfKanvZ_-pbYMAXCMuqmMQaMrg43pFpLhl7IHxmT5Hym3vBP3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تولید قطعات بمب هسته‌ای جدید B61-13 آمریکا زودتر از موعد به پایان رسید
🔴
دیفنس بلاگ گزارش داد اداره ملی امنیت هسته‌ای آمریکا (NNSA) فرآیند «شکل‌دهی الماس» تمام قطعات بمب گرانشی هسته‌ای جدید B61-13 را سه ماه زودتر از برنامه در مجتمع Y-12 تنسی تکمیل کرد. این موفقیت پس از اتمام اولین سری از این بمب‌ها در می ۲۰۲۵ (حدود یک سال زودتر از موعد مقرر) رخ داد و این برنامه را به یکی از سریع‌ترین برنامه‌های تسلیحات هسته‌ای آمریکا از زمان جنگ سرد تبدیل کرده است.
🔴
بمب B61-13 با حداکثر قدرت ۳۶۰ کیلوتن (حدود ۲۴ برابر بمب هیروشیما) جایگزین بمب‌های قدیمی B61-7 شده و قرار است بر روی بمب‌افکن‌های استراتژیک نسل ششم B-21 Raider نیروی هوایی آمریکا نصب شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133728" target="_blank">📅 14:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YocaDMnwynSgV_J5FrDCnz-s9QrQOUQM62h1mXV-RaIbXxlf1fR5Rz7p18M6o3zvKUrT2YoNaFrbyZ5kN9ZB2HoeEKIkXRyyhILZl-JaEXYHLFnV70MFUVNZm7h40cbhYuR88mxPI4dqQi-x6rXGUuspBwRfhh0kaVlDVM8BjnMJAqn0lzJRw1V5E-yl2Gx4nGjgPIY6D-eHgy6IMr-QmBQyQzRorjEQOJ1OUrOVhVAbLRUC15xW0j8cjojpYcer7qMADIjs4fGoHqlfTqqMjapzQrYCwr_uD6VQcFqjqT4RGG7O0L6y6S018zOL9vZzpoQC751KFQHhjt6y_4OSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون یک هواپیمای ماهان ایر بر درحال حرکت به سمت صنعاء است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133727" target="_blank">📅 14:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارشاتی از شنیده شدن صدای انفجار در شهر جم بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133726" target="_blank">📅 14:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: در سفر کوتاهی که به مسقط داشتم با وزیر خارجه عمان دیدار کردم
🔴
به همراه هیئت‌های حقوقی و فنی، درباره هماهنگی دو کشور ساحلی تنگه هرمز برای مدیریت این تنگه و تردد کشتیرانی به گفتگو پرداختیم.
🔴
این گفتگوها را در سطوح سیاسی و فنی ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133725" target="_blank">📅 14:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
صدای انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133724" target="_blank">📅 14:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136347dee7.mp4?token=GRRwM0i44l67ehjXWZM3hDfrcVBjH8WXD0z5MiHwGRHyaDMYgQzcpk06wWMYwqXGi9etU3Rs1a23XEVUl-bcj_wnvvFRaXun1XP56veJc2PmSsqEtrWBF8QwWjZSggMEm96AqUp5_2r2deJBMw_d2kSf3Q58fyourOe9ZtoIsDNrTQ6ekp9F7MX7R4bPoxuMSoNU63m6eOybTy-ifN6UzTCooAwXLM48YNMEqzIC8KqLISWAAT3DFrHEB8TpU-jEmdkG1AY4dji3wCcjuwKrJi_KOehOZXWQiQHUgBaBIgVPJc3DBKk-1MgdPrZtgLsL_kSimY2IN0mDyQp6txyWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136347dee7.mp4?token=GRRwM0i44l67ehjXWZM3hDfrcVBjH8WXD0z5MiHwGRHyaDMYgQzcpk06wWMYwqXGi9etU3Rs1a23XEVUl-bcj_wnvvFRaXun1XP56veJc2PmSsqEtrWBF8QwWjZSggMEm96AqUp5_2r2deJBMw_d2kSf3Q58fyourOe9ZtoIsDNrTQ6ekp9F7MX7R4bPoxuMSoNU63m6eOybTy-ifN6UzTCooAwXLM48YNMEqzIC8KqLISWAAT3DFrHEB8TpU-jEmdkG1AY4dji3wCcjuwKrJi_KOehOZXWQiQHUgBaBIgVPJc3DBKk-1MgdPrZtgLsL_kSimY2IN0mDyQp6txyWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخی مراد ویسی به مخاطبی که گفت باید حرم امام رضا هدف باشد: حساب آخوندها و امام رضا جداست، امام رضا اعتقاد قلبی میلیون‌ها ایرانی بوده و هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133723" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfDbVqRgrBuTwx2IYYWWTizQcBWHsXXaXjbQLjHLvjrRX4FWouXn2X1IJcRIxNRTMlOyLDedH3FKLqcwFxlF-IR58seM5Pi7ylfdLLxeCTIYwWhM_UynqorEGQRWOfdVS0mpTfDdqgIbRujAUhrZ3NG83-OtDcHWwHnxZ3XEB9tfo12afCoCjvVQMnuupXqpbFg6seQlE0rMK593QETidpiWjaIiOSYOPk5hR5H4EIQGIZZE0GKwzQbRVZ_Oj3fL9T-lNGfCSHGqiR99drJJhC1k8zSAw3yUKDX2F0JlpyeXrgGUZSTdbn5C2fEiQ0PXuPwPRvi0Yi4ePkPx8VRXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی، خواننده و آهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133722" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / رسانه عراقی از هدف قرار گرفتن شناورهای جنگی آمریکایی در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133721" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بقایی: لبنانی‌ها از جمله مقاومت لبنان، بهتر از هرکسی می‌توانند درباره سلاح حزب‌الله تصمیم بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133720" target="_blank">📅 13:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/گروه‌های مسلح وابسته به عربستان در یمن: صبرمان تمام شده و به نفوذ ایران و حوثی‌ها در حریم هوایی یمن پاسخ خواهیم داد
🔴
با تمام امکانات موجود در برابر هواپیماهای ایرانی که به سمت فرودگاه صنعا می‌روند، درس خوبی خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133719" target="_blank">📅 13:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: انتظار ما از دوستان عمانی این بود که در صیانت از امنیت و حاکمیت ملی هر دو کشور ساحلی تنگه همکاری لازم را داشته باشند
🔴
ما خود را ملزم می‌دانیم که تدابیر لازم را برای جلوگیری از تکرار فجایعی که موجب حمله به ایران و ایجاد ناامنی در منطقه شد، اتخاذ کنیم
🔴
برای کسی تصمیم نمی‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133718" target="_blank">📅 13:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سه ضلعی مرگ
‼️
🔴
پوتین، نتانیاهو، تندروها
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133717" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_WzLg-tK-FegzVwSaE0MzeccQEQs3KsDOOOucvggTHZv0XsY9hO3QRCXhv3r2FavJGqP8zNFmObieqVQIzYakhuQItfve-yHeBl0h_y78miDojONzHijYTxt7hPEs7xSDb8bXmc5NTZvysAXdjdPjWqkgVPJFZTsMIPkMAcaryXXALj4kYZVnptIOhWYbsZWnOQpmNOWA6kOZb91nMIgUmSxQwwVC1IWhBTN9aESo6-IA9WbCSWXSxD4IAFNgcVrOFLybI0CfIBuLDdLGhXt8DwhlVJG9O_VtT-rRW4PQiZB8MBfgwtw1lDE8g7YT_hfBSBbELMv1HBwJFVeq9Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار از زمان آغاز جنگ داخلی سوریه، کشتی‌های جنگی نیروی دریایی ترکیه از بندر لاذقیه سوریه بازدید کرده‌اند.
🔴
وزارت دفاع ترکیه اعلام کرد که فرمانده نیروی دریایی ترکیه در جریان این بازدید در کشتی TCG استانبول حضور دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133716" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8cbaf417.mp4?token=P1WKBMiYs3oif5lSuFGuRWSK2brYWhvfua1KcKZoBwNorvobEqICuOfUA0xRNf4Nx9VPT2XrVM7k3lxzlhbaQXIT93u3wD6qAaIGjKZ0VHSRwo8ZeKgaXOo8GDdY1LLDZxX3LZyrWjZhIX_GKIz7jEk_c8VfmNpwRKtyWLp2TFj4dSuHc31SCjLEQvAtfUT84WLWO-SEejMV7_Wo7Q91j-ANCSnvnQ7z4Tp8sOgnkCs_zsKxZMtJb9obYFb7TUEw049tnVhklbB4I0UEIJBueQLCsIQRKuPAZZgzpWMuL5_mBZZnuifIyNRWhgUp9VAWru74HTPoL5Ptjt81ZoCbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8cbaf417.mp4?token=P1WKBMiYs3oif5lSuFGuRWSK2brYWhvfua1KcKZoBwNorvobEqICuOfUA0xRNf4Nx9VPT2XrVM7k3lxzlhbaQXIT93u3wD6qAaIGjKZ0VHSRwo8ZeKgaXOo8GDdY1LLDZxX3LZyrWjZhIX_GKIz7jEk_c8VfmNpwRKtyWLp2TFj4dSuHc31SCjLEQvAtfUT84WLWO-SEejMV7_Wo7Q91j-ANCSnvnQ7z4Tp8sOgnkCs_zsKxZMtJb9obYFb7TUEw049tnVhklbB4I0UEIJBueQLCsIQRKuPAZZgzpWMuL5_mBZZnuifIyNRWhgUp9VAWru74HTPoL5Ptjt81ZoCbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی حمله های اوکراین به زیرساختای روسیه، صف های بسیار طولانی بنزین و دعواهای جالبی تو جایگاه های روسیه دیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133715" target="_blank">📅 13:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1010c6d.mp4?token=WkaHStxJCn5NLPNX5qDex8Np_W0CrVspcjU-3lhbvph8et3aHHSGG-hJ0dMSN3Ohx-ONw5NkJnOgrn74yzG0iE8VoC9VjbNmIivdVVuS5R8D2LuKjqkYcZmzHS7lXOwA-h7RjXDQJETeS1F3FbbJBkaLmG46sUQmR9TyHS7dnnWn4QEmYbRM4yUTeFGqvU35I-GDJra2qakGueEb-iadwi0Yl6Sst0W4Zz5b5nZ5FQ1yqabddh3QSXZT63TRiWylNxjVhQNlLQje4oDR4LIqW-QqbuQbLx-WeWqriwsB4DK9SZANlL4PG7rbMtEcU_7ZL1VQroBHyGhWWTbZPoZ20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1010c6d.mp4?token=WkaHStxJCn5NLPNX5qDex8Np_W0CrVspcjU-3lhbvph8et3aHHSGG-hJ0dMSN3Ohx-ONw5NkJnOgrn74yzG0iE8VoC9VjbNmIivdVVuS5R8D2LuKjqkYcZmzHS7lXOwA-h7RjXDQJETeS1F3FbbJBkaLmG46sUQmR9TyHS7dnnWn4QEmYbRM4yUTeFGqvU35I-GDJra2qakGueEb-iadwi0Yl6Sst0W4Zz5b5nZ5FQ1yqabddh3QSXZT63TRiWylNxjVhQNlLQje4oDR4LIqW-QqbuQbLx-WeWqriwsB4DK9SZANlL4PG7rbMtEcU_7ZL1VQroBHyGhWWTbZPoZ20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های اوکراینی گزارش دادند که یک پالایشگاه بزرگ نفت در شهر سیزران روسیه هدف حمله پهپادی شبانه قرار گرفت.
🔴
به نقل از «کی‌یف ایندیپندنت»، این پالایشگاه در ۸۰۰ کیلومتری مرز اوکراین واقع شده و در پی این حمله، آتش‌سوزی رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133714" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دستور پزشکیان درباره طلب ۴ میلیارد یورویی تامین‌کنندگان کالاهای اساسی
🔴
با پیگیری اتاق بازرگانی تهران، رئیس‌ جمهور دستور رسیدگی به مطالبات ۴.۰۷ میلیارد یورویی تامین‌کنندگان کالاهای اساسی را داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133713" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / به گزارش برخی منابع: شلیک موشک‌های کروز از جزیرهٔ قشم به سوی کشتی‌ها و ناوهای جنگی آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133712" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYctIdcyL3OAI74pyfDxMJXwTlA2bs8FmZGwio3dzJ9aAXhLj33NG4MKSw8r168uR5hZV0-QFyWptaoo64gqOob6eL8eN57aALfI7tqUo14BAivfBxgyW17wChAMa-LdP2OshSPsYL9ESP3lCQbHIietOwyQPPF2n42OH4cojNm9i0QqqngzU1G5VqzxiuBrmSQizvNY9Yh-OzEfpnoq69WKBJcd7QhuSCbLQvG89pQVXFtZEv18Jfon6NehYmx3RFfWT4E1uWxnB0BOHpr1HnAK476XjoADC0SAxh5upHk3K8VEAVLSmMn0lxJLt7jm-QE6ggvsBgoHbZioeJF_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWfSz78ApxhZHXgNkbJgISS4fQ2nJOU9wp24Tj3liaWUfqbcmWRdmXT0f7LSvuSeu5M0jRdcMLWhPpsRDy4g8Xee714ErqfbTBneIcWhr35NvhoMg4GtgbRMtYvJ1EkYsPS-BW9ZEkhFabelQnlNcljLOr3D4NNt8ci6z1Ix2nnf1bGiFa9P23RfzR7O2vbM_959Q5fzb8skoJyUxCleTKYVwOCltWdy4Wme4dTFTeVSwa76k9KReskLmOxa86PT5vN-FcXnbfASE8YyqRANPD77DrHj_DDjw_lmd-xK_ZwQyWdkef6tlC3QjS3fr3FUEwbmr-P0P5hE2HWS4Q85xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تانکر ترکرز:  در حالی که برخی از رسانه‌ها از وقوع آتش‌سوزی در جزیره خارگ خبر داده‌اند، بررسی تصاویر ماهواره‌ای نشان می‌دهد که افزایش حرارت مشاهده‌شده نه ناشی از حملات آمریکا بلکه نتیجه‌ی مشعل‌سوزیِ معمول و برنامه‌ریزی‌شده‌ی گاز در تأسیسات نفتی این جزیره است که نسبت به اوایل ژانویه ۲۰۲۶ تغییری نکرده است.
🔴
بدین ترتیب، گمانه‌زنی درباره‌ی حمله به زیرساخت‌های نفتی خارگ تأیید نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133710" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c8802cbe.mp4?token=ESlTAh-4SwH_EtCVXO9OwN7-aBYCRcOaZbmoCfbj0PbZDqC5wXULuuXE9hg6_qe1Pu_BtQnapn0A1vPqdckGcYMGG-gMI2F2kaUfNZFjU5FKYajiAJT3z7xYWMkgdzpOtgYflbqC0dB_7mnrfX24UeSzuozxHdn-lhcKpUHdjgxdP1_EaPJXdBeGOQUTcOVKYnfmz9b9LcAexSMtU8IM14PWGxVt4lvN918N5r8N5sDZrsZFmj3sYJSEw1kj9GQIjppg6CfiAR8BeWVQJutuFpCj4zST192Pen054t36W6ygy3MDMBOFDBOtncRFtNjEjMAEwTFfDmXRRXdnnFH3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c8802cbe.mp4?token=ESlTAh-4SwH_EtCVXO9OwN7-aBYCRcOaZbmoCfbj0PbZDqC5wXULuuXE9hg6_qe1Pu_BtQnapn0A1vPqdckGcYMGG-gMI2F2kaUfNZFjU5FKYajiAJT3z7xYWMkgdzpOtgYflbqC0dB_7mnrfX24UeSzuozxHdn-lhcKpUHdjgxdP1_EaPJXdBeGOQUTcOVKYnfmz9b9LcAexSMtU8IM14PWGxVt4lvN918N5r8N5sDZrsZFmj3sYJSEw1kj9GQIjppg6CfiAR8BeWVQJutuFpCj4zST192Pen054t36W6ygy3MDMBOFDBOtncRFtNjEjMAEwTFfDmXRRXdnnFH3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده پیشین سنتکام در گفتگوی دیروز CBS News درباره برنامه تصرف جزیره خارک گفت و آن را هدفی دانست که باید در برنامه ارتش بررسی شود تا دست آمریکا در مذاکرات بازتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133709" target="_blank">📅 13:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مهر: شنیده شدن صدای انفجارهایی در حوالی بندرعباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133707" target="_blank">📅 13:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :  تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133706" target="_blank">📅 13:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به پایگاه شکاری بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133705" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
توزیع کارت ورود به جلسه داوطلبان آزمون کارشناسی ارشد سال ۱۴۰۵ از طریق سایت سازمان سنجش آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133704" target="_blank">📅 12:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی حزب آزادی کردستان:
ایران صبح امروز با سه پهپاد به مقرهای ما در استان اربیل در شمال عراق حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133703" target="_blank">📅 12:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به پایگاه شکاری بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133702" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Nw1ilR4agGG96nHnTfty7KwVeDkbmGgCDL2j2pmNMKomh9-x5exNcCQd4u7pKNVPDi2NxZdK9ZciNJc9fa8jb9MvrFN-NQ79XHLgVd3KZjhgzwJM3_ThfgwR36_tI4xBApyiA_X7dBPFD8fTvNjQpuSAk4-hffUdHsBUTkfLmCkn2JRWMzJ9cEc5hVFIAMo7hPxCLN_SlnpdUwKwDWS5bV341GKUDt6VOxyuqhV-sPBfIQaADqy4vHo3MbvN9KVqqpL8mIanmh9lM6juC22KO1qbAa8-uFzuzi3m9Pq-msEf6p0Bl-dhfYANe104zYpzHkcy_1-FyNNaOv1x-_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش بورس به زیر ۵ میلیون
🔴
شاخص کل بورس در پایان معاملات امروز با ریزش ۸۹ هزار واحدی به ۴ میلیون و ۹۶۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133701" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
علی‌اف: باکو با جدیت در حال بررسی خروج از شورای اروپا است
🔴
رئیس‌جمهور جمهوری آذربایجان امروز گفت که باکو با جدیت در حال بررسی روند خروج از شورای اروپا است که پس از تنش‌های اخیر میان باکو و این نهاد اروپایی در سال ۲۰۲۴ کلید خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133700" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d0b613f7.mp4?token=Xg12ziz0Ye2qWlNPa3SF-cQ7_ylJoCYuhcv_iaXkrHBx7fufZoLv7k9w-IqjKYYxIesmxe8sbkmFx9bxMTqxTcS0AUM7WoIWve359i4_pKAXCWaWET2pRYBbulvDixDp3zVtEzOmzzOWfiyG9zisQxXeVH7DAVmNQAbQlOOxrKA5DTfWIC5H_1wHaDlE-FkIKALvtKVM7kCiGID7edn3zXKa909uZXZ9BUP-mebArBMyFOmPZT9DT-HK9I-U5PcBMUMd0itdnKV7XiG5LtqUFp4BdrDiCmCZ1qh4NqRSL-eEd5HoQ6d34fcWj3LBKvJqyMa5gIrbQrtRoN97fRcVjoSxslscxSu2d0msOYcJSee1e0N0AVI1rQEk3EGMOOJxXZ_aFCpd15GKbpRFNTeDQM3hKRRbdIJ4LYZmRiE9EbCNw7qrdB5jEW4y_2kMkW6QVl0k8zS8VhNysC40avtKzDQt5vX2FiGxMm1CraFAQlCfay2mekLpITPS9LdhtT5sJxlBaCwb0fqxAAM_0JoiqsZVnHcPdMM-hxDjQRO8Swk_AgT7RNvQ8QNtrHrmfbSB_yEwgUZyzh0EOlmq-efBmVwMLzbSREPrUnNTNg7HySy-E5Y1hTI8_Wn4p58te08VmksAgMEkHYQTwIwHXQeoZUN9AMwp5BJ2-iW_Ry15GO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d0b613f7.mp4?token=Xg12ziz0Ye2qWlNPa3SF-cQ7_ylJoCYuhcv_iaXkrHBx7fufZoLv7k9w-IqjKYYxIesmxe8sbkmFx9bxMTqxTcS0AUM7WoIWve359i4_pKAXCWaWET2pRYBbulvDixDp3zVtEzOmzzOWfiyG9zisQxXeVH7DAVmNQAbQlOOxrKA5DTfWIC5H_1wHaDlE-FkIKALvtKVM7kCiGID7edn3zXKa909uZXZ9BUP-mebArBMyFOmPZT9DT-HK9I-U5PcBMUMd0itdnKV7XiG5LtqUFp4BdrDiCmCZ1qh4NqRSL-eEd5HoQ6d34fcWj3LBKvJqyMa5gIrbQrtRoN97fRcVjoSxslscxSu2d0msOYcJSee1e0N0AVI1rQEk3EGMOOJxXZ_aFCpd15GKbpRFNTeDQM3hKRRbdIJ4LYZmRiE9EbCNw7qrdB5jEW4y_2kMkW6QVl0k8zS8VhNysC40avtKzDQt5vX2FiGxMm1CraFAQlCfay2mekLpITPS9LdhtT5sJxlBaCwb0fqxAAM_0JoiqsZVnHcPdMM-hxDjQRO8Swk_AgT7RNvQ8QNtrHrmfbSB_yEwgUZyzh0EOlmq-efBmVwMLzbSREPrUnNTNg7HySy-E5Y1hTI8_Wn4p58te08VmksAgMEkHYQTwIwHXQeoZUN9AMwp5BJ2-iW_Ry15GO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب وارد شده به یک واحد زرهی از تیپ 63 ارتش اوکراین توسط یک بمب FAB-3000 در منطقه کیف
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133699" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هاآرتص: در گفت‌وگوهای محرمانه در داخل نهادهای امنیتی اسرائیل، نگرانی‌ها درباره ماهیت دور کنونی تنش میان آمریکا و ایران رو به افزایش است
🔴
در اسرائیل این احساس وجود دارد که امریکا دیگر همان میزان قاطعیت و اصرار گذشته را درباره برنامه هسته‌ای ایران نشان نمی‌دهد و دور فعلی درگیری‌ها عمدتاً بر باز نگه داشتن تنگه هرمز متمرکز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133698" target="_blank">📅 12:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دلار در تهران از 180 هزار تومان عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133697" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
