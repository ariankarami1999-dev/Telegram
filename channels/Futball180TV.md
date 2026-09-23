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
<img src="https://cdn5.telesco.pe/file/Ea51rqoYYKdDhSbQGqDh9u9M7e6EALwsRwsWS0-UrwH7TET7HZpN9iHY2VJzlWKBcBMpR_WvLonOZuuUSSiJ4spYe86oMqCYYhx69vL2WNQbSOVObdfjks7SAWpmUvbuJ_8UgElFj4cKEg0lrQSeSx_7H4Ku3JXvP5XCsUtPGgoziMKYAGx_gTUquQzdoR3UjyTx2FMQap5vbjBQOoaqbthsSt4TIGA10l9DVhZ_cHKE5x58Ti6gI0JjYr3__wbT8QkeL3C-eeFW30J5jnfmOQ1-qpngYgBKt70jWejVSrWX9eYM4cLtQTByMrgmc4jwKa4BBbkmHxa4I00DHhxH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 403K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1cBvc3WMr7s-Vel_4SghPzCxkm-NhjU-7jVoDk2ypFsaXVvc-0_T5QcNECKLJHIjb5KncQvHasjk7Na3gokyZcuTZru4Oo_l_VIVQFB1K0lXSv4dplZuCAhm68tvsvSZeYk_VuGD03M7QqF1v0OaOjezArl2XPZlWYrEPl9B4qS4roBqf061_6SqdimH-ECJXZGZmXmfbR0ueT-C6SNwCnO8m_32diXPhkO-ctmyhX61BJDzCD5bZ8SPuyHSkfd1cLkpXxl0dHL2oihpZE1lO2AST_TPZ7WdRq230hpEEH6OUm5YTO14bifT0Lc6C_phRPac5nmIEEBdmB9D9K7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHIiUhZy5s6ZhEEOzkCZv611ej7A6KTuid1n6-6kfmOdF-MZVF0kjpy8XHVMQiXJbv-3jNa51oNxX6bb-3hBJHgm-3Cb3DhbnhYvCpjJ5ONJwiLIcu5ACEx9ZUit69ZSyKhNoDrqWi1Q0iJGeekrTM4OwJtFy3UvR6m4y3-LUDO_QrhYEdtibUYFg3gv2W9on23zwqPH0yTJfmi7FNOD1ZP5ml7L7SMlGaWh2EoPHOpnY0KfenB9JJ8E5aOaIa6kb980DNuw2DrDuCdsp3w4JTtICL21OLc2kjwXtDrPoLeOFlRSFDO3NENsBK9orQq4izn6yeBJKZcOd_2pUo3d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=cXU88wVJW4avzwgP_qam21LQWXb9f-MJbdjP2E4uFU3g6pS7_e6Lb4lqF6DIdgu1WoKQsn9n01sxmDOJn8hfG3mwzTspAyTOSbyJDeFQAl-Zzb3-Hh1wpWgeLfnxtUYRBd9_-RjKhipCSxf1yWTqXMwzYBJm5w5Et2qP5gPpcKKRwutgOX0KWl8s1GQkLsXE9Ic2NAN7tEdP5sR9k-NzufCY4cDM0onIUiGjFL7ULdPCHyX2pI3M-S72H34FPKCJmF9q7PA7cHeRY2S62hbHCdIH2ejLhduqu1mEC9xubleNTqvKLK_NSR5AjFoFmZHke6i75lzm3XMcoYx33Phun0KDc78COthRAu-xuMDryb_AF05EsQY5J8rtdsH93ILu_c5iPE5qOEOmQCWkgnUDs_rZyP6MOQIpn4iBE6V25Y8rhaxc5ieEMro8l2Fz3_kwAiQ-7Nm0mPz8fXNLR27Qx8W3xo7CGjcQfI5vzcKwT3MtWAaZxuspytBr6jhJaBvUfVMOuPdwDembO3oxyij8g_cxdxRcVmdH5sB8uSq4QgQlQQktk3niB3QSpnp3a2ngCi7vTfbAh5j8rUmaA_h9sp-yd0hsXNgQdTr4HaFd74tTm8h6QgLDMn50g9BPa1J0AY4lKmKjFqWkRIf2rrlYxoWoYgF40nhthvhSe3B0mLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=cXU88wVJW4avzwgP_qam21LQWXb9f-MJbdjP2E4uFU3g6pS7_e6Lb4lqF6DIdgu1WoKQsn9n01sxmDOJn8hfG3mwzTspAyTOSbyJDeFQAl-Zzb3-Hh1wpWgeLfnxtUYRBd9_-RjKhipCSxf1yWTqXMwzYBJm5w5Et2qP5gPpcKKRwutgOX0KWl8s1GQkLsXE9Ic2NAN7tEdP5sR9k-NzufCY4cDM0onIUiGjFL7ULdPCHyX2pI3M-S72H34FPKCJmF9q7PA7cHeRY2S62hbHCdIH2ejLhduqu1mEC9xubleNTqvKLK_NSR5AjFoFmZHke6i75lzm3XMcoYx33Phun0KDc78COthRAu-xuMDryb_AF05EsQY5J8rtdsH93ILu_c5iPE5qOEOmQCWkgnUDs_rZyP6MOQIpn4iBE6V25Y8rhaxc5ieEMro8l2Fz3_kwAiQ-7Nm0mPz8fXNLR27Qx8W3xo7CGjcQfI5vzcKwT3MtWAaZxuspytBr6jhJaBvUfVMOuPdwDembO3oxyij8g_cxdxRcVmdH5sB8uSq4QgQlQQktk3niB3QSpnp3a2ngCi7vTfbAh5j8rUmaA_h9sp-yd0hsXNgQdTr4HaFd74tTm8h6QgLDMn50g9BPa1J0AY4lKmKjFqWkRIf2rrlYxoWoYgF40nhthvhSe3B0mLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=S9onsa8zXd-4bjzsPMqQLNLPDMSZnhhZZTE4Yl-1u41BfpttzSdgRjxPM4kPt7RmzBEyPwWAYGCQOchsnNHDs4Gi8xMAFM8cfoUlcqb2z7m6kwXjWXkoyrQTzPaq59PhNJ8Xz2NKEQrEC5pAN4jYzgZJSqrNge27ayhJ9nsEy3fWThympuspFGE-i8Q78pH-6KZeUuHeioWQy8J7Yi3HoqqYOzaDVSaKsKZC0ZoLqdMJOb4DyLtF0K8M_-pDAP6os4wGgVSJCfgGPq_wW11hxr2Cs0rbcn8-zuJ9dhEM90GXZZMXLhedyWFajuskYCyd8AnDhXes3YpMwvIm9w8FIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=S9onsa8zXd-4bjzsPMqQLNLPDMSZnhhZZTE4Yl-1u41BfpttzSdgRjxPM4kPt7RmzBEyPwWAYGCQOchsnNHDs4Gi8xMAFM8cfoUlcqb2z7m6kwXjWXkoyrQTzPaq59PhNJ8Xz2NKEQrEC5pAN4jYzgZJSqrNge27ayhJ9nsEy3fWThympuspFGE-i8Q78pH-6KZeUuHeioWQy8J7Yi3HoqqYOzaDVSaKsKZC0ZoLqdMJOb4DyLtF0K8M_-pDAP6os4wGgVSJCfgGPq_wW11hxr2Cs0rbcn8-zuJ9dhEM90GXZZMXLhedyWFajuskYCyd8AnDhXes3YpMwvIm9w8FIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/107146" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qme8j5G4gj82nLAKijHZHDT0a6HqjJuZU9p5F1NQu923yntPiyQdwO705GqrwG5yQgtVQnQVm-_7gS_osUQEBxsJRKgY1XfHU31BcOwTOHuRJ19rylcvJpZ_eCoYofa2k0zXnFrsBV3Zb2uxC9I69ESj6fqoSj3ndgfIrjvI9qcnrlqFHl71EyV6elRLS2JKSyU-Hem4T7RnbZ8uF3WAuW8Br7Pv-8uEN6YRkavwJ5xrlac_qCNkUUXfQSb0TvENIc4CzoICb0L0sWfVl-rjFTrp7JsIKDTSp3_DQJpBPoe-mF0gb2Q1hG5yCgqak2uhtJ-Xo1luIlLY3gI4qDCnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/107145" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=sxQwOO5aS6bfGOomGpLCDBSFhJFDdALZmxxPWEUk4e6btYGcQZg7xbedLpfONIUiWMyfeBJB2UItOAMnXvSx6LuXtzfIEAvSxZKLLjQSF81IBhuPWlLEOYEBzsZwOBB7AR4q3mZx7pdbiwfD5DA-MDBD5IFcjXoOfAcIErU7_hciNubLpBXMz4B8O3Ngbf6m1AeNCuAyKMOXcL4700U4Yk0d7E0oC-cfl8Vlr-chDuQPEmP7gVVfUrZt3bY5vV7zU4KQCCHH2JfoE7yLgCU3QyIoUVygy8ajGiHnkCWwN_1fgQ5K5f_KhI7l2YiDFLd8OMYBJKcsjodcMHyurDdO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=sxQwOO5aS6bfGOomGpLCDBSFhJFDdALZmxxPWEUk4e6btYGcQZg7xbedLpfONIUiWMyfeBJB2UItOAMnXvSx6LuXtzfIEAvSxZKLLjQSF81IBhuPWlLEOYEBzsZwOBB7AR4q3mZx7pdbiwfD5DA-MDBD5IFcjXoOfAcIErU7_hciNubLpBXMz4B8O3Ngbf6m1AeNCuAyKMOXcL4700U4Yk0d7E0oC-cfl8Vlr-chDuQPEmP7gVVfUrZt3bY5vV7zU4KQCCHH2JfoE7yLgCU3QyIoUVygy8ajGiHnkCWwN_1fgQ5K5f_KhI7l2YiDFLd8OMYBJKcsjodcMHyurDdO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=rUlAD4Ysf7e2IfW3AvCiOgR2Sz65ovcGHMNx4r31GK4szMkp1A1Qpv7Qqv7BReRAcs_BBe5dTMuyg_Nu9PKasHWH8m-4kP4O2b0pKAGJt6IBZuCMqMJ8QP7G_-gja8mQBxxAh9se0_Gq6eQeBVfZQHa5s4Sxu3rh82Jl4Ytxf4nmctdcWL0ig996DZJX1URgLkc5xy6wXPF9uIU7gROmfL8ErpGeR0VZ0cLzYJpGFklrjqmm6zg-tN5NcZ6MrQ8abejQA1-LfL--zxw67gfGiCMtWbfFYQLTlO4CFlubzQeK0i2HDvgcI-jYPg4FiR79lUeZr1dyMAa4RFU-yqwqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=rUlAD4Ysf7e2IfW3AvCiOgR2Sz65ovcGHMNx4r31GK4szMkp1A1Qpv7Qqv7BReRAcs_BBe5dTMuyg_Nu9PKasHWH8m-4kP4O2b0pKAGJt6IBZuCMqMJ8QP7G_-gja8mQBxxAh9se0_Gq6eQeBVfZQHa5s4Sxu3rh82Jl4Ytxf4nmctdcWL0ig996DZJX1URgLkc5xy6wXPF9uIU7gROmfL8ErpGeR0VZ0cLzYJpGFklrjqmm6zg-tN5NcZ6MrQ8abejQA1-LfL--zxw67gfGiCMtWbfFYQLTlO4CFlubzQeK0i2HDvgcI-jYPg4FiR79lUeZr1dyMAa4RFU-yqwqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMVg75fFjdSpGS3dJ6DPYfCcp7F_MfqP3VRMDkCh2KaB_j07ji-F6FNEps7WecsIVv8urtxs-WOBsDmcxKKbCfX74MXD0qUJc11tkRo5YsL90dVWj2xDgIMtxMeEBad6OJzg9BDhhRA48kS5Bb3E52aXx9UyIrb5EJQLm4o74xDtjQ2JeKxgMXYmg8TPVbTGO8miwGI7kY412YwPKK0FvTZsBmVtarE8YWMsW7nyfw5SsK6ys5NEEdYoPRpoUOovKzm2NNrC3AgZMWw0ttY6B6bbXLG1o1BheNgiDBFokXl22K-O6JiRtpGQjczqbc217ubPHVBYcEyLe6qySIh_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfXnz_S-lcdaKTtT6dnZQIqE0RKktG7GLcR_4tKrN8p1E_de3LJGBTP_D9vKwDrDTaEQya1KtN7R1MWWvkUl8vejmOX3m9JVPVMtQPwYs8pyD0gmJQcEJ846E1DU_Lrq7YUyZkEgdAU5DkF70VWsVmcS8OtN5RqPvQO_3ST96MGFlskJOisYZ81LAA6gPmOEf0dhbu1iOxLyai9TF2QMlLKouAb8zAJawnX6j5xQt4tLGTIjT-mJgSZlEdAAG74Lktq2E2qrU8sXta7AwRgzw0MvKiZOyYO38NO44qUK___h_8MFJWCRqzENXIpC5e_CetGJLSEncS_dpVqt41Zg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=fzgW1jgN7tex502XUMz0OMEbAaMp0HXVHlrUu3cgBhZK2JpMZ5-0C0mmBYkZaTpzgXAlU4CNJfMrfcgQJuU5TlYZVNCiEHFO_X4Vl4pUCCcCe6W_c3lt-wyooHeLQ3CoJzRRB7WmjCT9QSB95YQPqdD9tmsSsGd_irIZe4Ix8rFVL4nildbNnhs94ZvCXsLppwbAGUkAB1-w6b8i2IfQ4v-WeoZ1V8E6eaUi9DK8FCvM8oHul4U7wE5AmKCXVWTacN0AsnRgGNJB5xw0tUj0LzNPkW5ls2DGnh523lph4t1R44lCNAT-OVFZSWy_HJJDcwJCmk-xjmAwfqNb2HJCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=fzgW1jgN7tex502XUMz0OMEbAaMp0HXVHlrUu3cgBhZK2JpMZ5-0C0mmBYkZaTpzgXAlU4CNJfMrfcgQJuU5TlYZVNCiEHFO_X4Vl4pUCCcCe6W_c3lt-wyooHeLQ3CoJzRRB7WmjCT9QSB95YQPqdD9tmsSsGd_irIZe4Ix8rFVL4nildbNnhs94ZvCXsLppwbAGUkAB1-w6b8i2IfQ4v-WeoZ1V8E6eaUi9DK8FCvM8oHul4U7wE5AmKCXVWTacN0AsnRgGNJB5xw0tUj0LzNPkW5ls2DGnh523lph4t1R44lCNAT-OVFZSWy_HJJDcwJCmk-xjmAwfqNb2HJCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=JmWeROaan1jK-OVUCLuGYfsAzHUBEhFy814dj0T43gcku2Dhq2FLC6qLuBlG_lIF-6vljPCe__LYtpjnkd7WitD7qZ29b0QqgmJVJQFhQ6Hv9Pkwlqhm9IikJjWksWen65gzh2geNM8A4GkAKo60S0kqgHXh3KBJ6RO-d4KiM8iRdLCEnFzQ5YiSCJx3sNcaKtFAmDnvBC5vsoa4kt4gn4ylPvq1lX4lxMwye6lGr96cWV-O294mAkomN3p8yciF79WjSAVp1AZmx_vL0Qu_sw30tUd0caYolWcMOQefjrwB9VNtgTL8LDzjxXMFJb8EZbgl1yyY5eWEa-KwZ3_bv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=JmWeROaan1jK-OVUCLuGYfsAzHUBEhFy814dj0T43gcku2Dhq2FLC6qLuBlG_lIF-6vljPCe__LYtpjnkd7WitD7qZ29b0QqgmJVJQFhQ6Hv9Pkwlqhm9IikJjWksWen65gzh2geNM8A4GkAKo60S0kqgHXh3KBJ6RO-d4KiM8iRdLCEnFzQ5YiSCJx3sNcaKtFAmDnvBC5vsoa4kt4gn4ylPvq1lX4lxMwye6lGr96cWV-O294mAkomN3p8yciF79WjSAVp1AZmx_vL0Qu_sw30tUd0caYolWcMOQefjrwB9VNtgTL8LDzjxXMFJb8EZbgl1yyY5eWEa-KwZ3_bv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=qEcgXhq9E-0ew5qlQkPiLUmbEy7-xPX6jELVV868zju9k9rMFFWzEeHfJGoRtKBskM46WtY06r07h_M78lIb5nhf-4HVawXQF6z8s9X5oiS5cOHg9YnjPGLRPbY26FeutjIhMuPdhoRjaG6Jj6l6IplXQpGLse5SyhZuLXiBBWN17RJ5weIvkxkIXM9S3l9ouDNnmblfOcFxZV7pcvXXdVweYqkTYJAKIZ1zdWyBZ2JB5BnRbRfrBFNcJdg5AIgeDiCN8lYZ5ozGDtx5vknBkw9tQFrMlPJLx3YIw18bpqFrHCmDCoEL-s1AMdSKu_1U_vhHAlx9ysZOOcd_vK6RlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=qEcgXhq9E-0ew5qlQkPiLUmbEy7-xPX6jELVV868zju9k9rMFFWzEeHfJGoRtKBskM46WtY06r07h_M78lIb5nhf-4HVawXQF6z8s9X5oiS5cOHg9YnjPGLRPbY26FeutjIhMuPdhoRjaG6Jj6l6IplXQpGLse5SyhZuLXiBBWN17RJ5weIvkxkIXM9S3l9ouDNnmblfOcFxZV7pcvXXdVweYqkTYJAKIZ1zdWyBZ2JB5BnRbRfrBFNcJdg5AIgeDiCN8lYZ5ozGDtx5vknBkw9tQFrMlPJLx3YIw18bpqFrHCmDCoEL-s1AMdSKu_1U_vhHAlx9ysZOOcd_vK6RlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=HxjO8DuXiESqNtsKKILg_RWGX4JXw-gBM8jtfknTCguF-L5z2O6skI0w0UpBUBuF_iQkRHhFM06CN-N9m8VuoO10lTE4DdN_84vGmTyrkhe9RpNSvYUCTKmV8y3yllbvsk57WN3arGcDlHCCNenbDVuoBC1V18ZpEFib45-ORVgxdTkOjsdz0BC5CB5ELLHWnvEcnJ8qfFvgX67lN1H5WJ3xf6eX6xzhCdyG0VwEutm3KdJ-p-of1XU59FNZNIo9Ce6DHXYLJzT68Cy_P8TDPuPQXckilVdPT4ZUkaa2p0_0Axqitg8lKHyAxUBPHdBZNYW6K-KNy-v3SNZRDMOpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=HxjO8DuXiESqNtsKKILg_RWGX4JXw-gBM8jtfknTCguF-L5z2O6skI0w0UpBUBuF_iQkRHhFM06CN-N9m8VuoO10lTE4DdN_84vGmTyrkhe9RpNSvYUCTKmV8y3yllbvsk57WN3arGcDlHCCNenbDVuoBC1V18ZpEFib45-ORVgxdTkOjsdz0BC5CB5ELLHWnvEcnJ8qfFvgX67lN1H5WJ3xf6eX6xzhCdyG0VwEutm3KdJ-p-of1XU59FNZNIo9Ce6DHXYLJzT68Cy_P8TDPuPQXckilVdPT4ZUkaa2p0_0Axqitg8lKHyAxUBPHdBZNYW6K-KNy-v3SNZRDMOpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=ZLtOQyALGf9qz6eTnaTIPH07jcBcEkjheNJILOVZn2stxK_ZmNzL0dH79ZahBGqetKkyU-oKfEcAacXfDRcett4lkzgL56y_vSJVxseQVtz0x05CQZqAz50IAtU59_JxjxSUZGoZlUYqgMUgYLr4elUVAPrTOeS29epjbDE86G_pLv4xy5v5aqNRDOFz4htvPEd52YMKQyUWGkvcsvOflS0ETaAt6uzzxZbUp4F_bcNj77HmErn5NAmVT43FXsDoJx4tRm7jASbPSp45aEyIGmQN_hC0nVMZh15lWcU6_-FmIN6nJ71WeuUDJ4srdI1Bs7boMg0Eu0y9A43_AmthwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=ZLtOQyALGf9qz6eTnaTIPH07jcBcEkjheNJILOVZn2stxK_ZmNzL0dH79ZahBGqetKkyU-oKfEcAacXfDRcett4lkzgL56y_vSJVxseQVtz0x05CQZqAz50IAtU59_JxjxSUZGoZlUYqgMUgYLr4elUVAPrTOeS29epjbDE86G_pLv4xy5v5aqNRDOFz4htvPEd52YMKQyUWGkvcsvOflS0ETaAt6uzzxZbUp4F_bcNj77HmErn5NAmVT43FXsDoJx4tRm7jASbPSp45aEyIGmQN_hC0nVMZh15lWcU6_-FmIN6nJ71WeuUDJ4srdI1Bs7boMg0Eu0y9A43_AmthwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWKkO8Hv-kl_4Rbgl4MiPpV-Z_wkWXKLZ0CQdYS3CrKR24Kv3UnY4lS6xkM_onry4PokQjPkDALf-Y_pmUp9sFNx4Iz9cLLJTux6GBmG3YHZ4uV_YNylpL4ez3KcbxRI16OvCweoPW1PLg6OBByIgPitQgDlGnfRhnyeXmcdWWj2K6MV_54zaL04ppXY4vE0dnTngpu4xUZghCcFfX9rPPYjG15l29M5h-F8ieBSpUkbcb8dv30ug3exHXUclfcssgrmBhwhjfe5yy8Ki8MgWAfVcZGtwgkitstQt7AYqZWM1VBuivvCYJ8K1jUtQ-oVsvtWgruhTVJw9BiEoMJU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=e0Jp0KuKuAw7CtvkXJqiBm6H24PFV6DyVGDeAQczAUzRBxFhZ6eQa-Z9ThY3HkcFl9vXjxYDeXidlBbEZD8vWDO2qyP4BIEGTBZJmJGEHj3H-2eW9cjBBV0zYQiNBQBr1NLc_KGU8qatEEqGYB93JRgRSzUMU4gHx0aajaoOWcxjfS5XxpGIulCMmVsEJSIa3ZfQ7IxTUZfm-ZD3uKcLyDt--VHLC1CJ5p8zdlt6zGy4nLHauCvyT0tXwTHBVD5pO-sL59WwB38xibjluI5zXzhlPO80Cqg7oQuPk64ZA-jDly-OVIkUrKBW7bmPDxT15aYxaPaotOQbDaa_s4mF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=e0Jp0KuKuAw7CtvkXJqiBm6H24PFV6DyVGDeAQczAUzRBxFhZ6eQa-Z9ThY3HkcFl9vXjxYDeXidlBbEZD8vWDO2qyP4BIEGTBZJmJGEHj3H-2eW9cjBBV0zYQiNBQBr1NLc_KGU8qatEEqGYB93JRgRSzUMU4gHx0aajaoOWcxjfS5XxpGIulCMmVsEJSIa3ZfQ7IxTUZfm-ZD3uKcLyDt--VHLC1CJ5p8zdlt6zGy4nLHauCvyT0tXwTHBVD5pO-sL59WwB38xibjluI5zXzhlPO80Cqg7oQuPk64ZA-jDly-OVIkUrKBW7bmPDxT15aYxaPaotOQbDaa_s4mF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107130" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJkykgZD7lKoYgdBaBydWHPODaP6JpivLi_uRlqrZZlxOdrr14NibOpfzPzFMQV6rwqM6Qa23h7QkUIRaHnlx0aSkS1flKpixFExbfme7jh7Ig8uNM1GBa2QevvtIH8rZxnxAG78Lx3LU2uAIYmwuTrBss68xY0DDzUalLE1bBO8g8twFS8r2piMJnWyWcSd5xim8Mf0KOYWcE-vBlmWU6H4M_OJRwo8FDicdG5lJXUwwrB3VM4wg1iZvDmzIgaZIR2hbP4S-K09DG83tVmcntcc5Bw6VDP000hj20Z3zLnonbB9AUOARqWyX_u2cX2axK09dcOLWZhNU7VBiyaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107129" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQG5qQ4q5vls4gs5A5he1Rk4yu5xpZ2st1KLfJvNZbmpgQqeKQfvXdGJo3bZ0jtRhtwj1ixclwmO4NQ9hKudnrEzosc38a7GXgUw-JSdbPurYAe-0Ck1MJY0n_HN_0wSfhKcVQVcPSHSpf0cETrNFL1Q3JW3kvmVCHqxXiG1hTXJIVfVWHBhK87_pyFAzvtSCSy9nWqsrplrJuuqhrRt1Ls9kmGdusKpAmadoDUTTAQ4CqT4ixQMer9iry_mGH9aACVnINeVz16MrDHvB-E_bmnhhhkdGVjQmsSidd_NeSoAUIam-OVwb89fmW9CMQf0w6yrztEs2jbTwSI7ojLv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1QrcQqkdUcv7mjKfL1Jkus-0-gKds8d_RKfC-lan_2MWjnLuVO1W2y2ZW_e2mU1j4b0dFjpL3knSEqkMcsaxsHhBVj3pRY0HPJCbQzegzT-X4-dJAaqjVAYa4HJKqKJggw1pbPgm8DEH0Fgy-eJnATZBVgnZXUWrqQT8RTYmzrhbr7jFT3ZlzN4P_cQrGfBM22fNttS-_Pa92v-wxpan3neiyT9uiPmad_dDsLpSez_w2n-oxs_qpInzOLselbfJldjBQZRynHLvub8JxFNAAUgWziWS3fBAh4Z8UJmTYL95gDQv4Lvqw8rOGnd_HoCto1d0FP-zXyj72A5NEzNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHIj7TfGLD4AkaVF_nPN1eTsCydoF8Q3SWJ5fd8cqKI8oXPDwIFGnsqt7W4u6bI1cQ2_mcpK7p0-RSnrL81YHaxxsg9DBUxS5f5FV-RHZ8B3IYGyUNFMii9YZdUIXOnkhsCIjZ7qWMJipC6Or-xfqbT7-AmK81Q8XfmJA-pWroL5He0NswaiwOQFeqpAmfKXSX09GsepesYSvS6JGTvhcUjkXEymMtPPrlt89G_O8bzSQZO45FkcP_6-igK0wXXwgnjaav19_ZXFYOJgFUDP2N57DiQNMu12v2tJpSq6n7ZpNSorPsYlxuzyocyodjou5kdES_qgyeMhS4BsC9oT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bDqGH15T-XKPIzjWQcsk77qkvno1gSi6DRoQtDMJAtKfwhN7x9fKA5ktBElBuStoBYyzlUDZDleNlOJoV7rda3Ws_jMKhwSff3wLOOOycmu0sa1_u4Ga0x-ImWL9RcG2l-Zkj_7yuwwdKRHmQMIBj1v-Td4c64071uwZnMrpSVxBQFo5bYO-PoiMqGOw--KlhC9grjtyj66qLFnb5I6iZ8YsOW4Om66x8bG_vmBAWahNJOALaseEHG4JWYyny-qI8a7YXi5lQhfqvRLhzwpoxWGF8IKa1LTv6j4KYc5kCxA26hqZDRWI0S1rHhCmXAqmPR67NW1SiuqDUmzTDJS6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=bDqGH15T-XKPIzjWQcsk77qkvno1gSi6DRoQtDMJAtKfwhN7x9fKA5ktBElBuStoBYyzlUDZDleNlOJoV7rda3Ws_jMKhwSff3wLOOOycmu0sa1_u4Ga0x-ImWL9RcG2l-Zkj_7yuwwdKRHmQMIBj1v-Td4c64071uwZnMrpSVxBQFo5bYO-PoiMqGOw--KlhC9grjtyj66qLFnb5I6iZ8YsOW4Om66x8bG_vmBAWahNJOALaseEHG4JWYyny-qI8a7YXi5lQhfqvRLhzwpoxWGF8IKa1LTv6j4KYc5kCxA26hqZDRWI0S1rHhCmXAqmPR67NW1SiuqDUmzTDJS6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=TlSVQAz2HrEzTk2i5prHdtWrToVycX6-F-PfzLHXI9QHpoxPknRGdDe4HKDiWJ8_lzRMCcG0DGmk1t6Obkbdtf6rLMBR_1Y1qaUzCo12lUhYDRATRynSfH4R3a7iWfVSHKyFdygLPE5Yf_s-JGMb9NMu0VcOgJixwxDbxETp6fXWVXQJwu04Bly9YqvSw1lmLsGCkktUr42mvym_qy_w-rYQm-vHv016hqa9wUX_hddFEsRQK4OEwfvBHm48X8AKPe7rn5foXjlBw_sPM9sswTxlogM5meCUV3vM5A43eCv0CWlXapelpBHI1UjYiXEdwYCTOQL8Grtl9ZYzrRq3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=TlSVQAz2HrEzTk2i5prHdtWrToVycX6-F-PfzLHXI9QHpoxPknRGdDe4HKDiWJ8_lzRMCcG0DGmk1t6Obkbdtf6rLMBR_1Y1qaUzCo12lUhYDRATRynSfH4R3a7iWfVSHKyFdygLPE5Yf_s-JGMb9NMu0VcOgJixwxDbxETp6fXWVXQJwu04Bly9YqvSw1lmLsGCkktUr42mvym_qy_w-rYQm-vHv016hqa9wUX_hddFEsRQK4OEwfvBHm48X8AKPe7rn5foXjlBw_sPM9sswTxlogM5meCUV3vM5A43eCv0CWlXapelpBHI1UjYiXEdwYCTOQL8Grtl9ZYzrRq3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=qEVlkgYbdayQ1OiPun7Y-alsfM0uGa5ZezRVefVg6kDeUstZsjLjf360-0LDm6hw2o0d7rNKhR2-GyfBt6Tb8w6a8bKJF_vjt3EKW8EGfjLtdCDFTQJxsgqmSyKQ9six70NXdIYWU1CRAZke20NDuZCfSET3Xog5bHZp4_7AfuEBtQqYGRFE9RKmMI5LpOWvg4SrWTjeuuoIBYhzU9Ci5GaztRRvoagAG0qUtk4ZNXlqpxaxHvkTTFBqKlBLUa0PcihBuZFuodYmoySrkZZFsH5se4t4s4n811O4NWyxAxnZcf1I1WrP1mP_qf96wMCQOxBoEBRT1-RuBIUFGJrnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=qEVlkgYbdayQ1OiPun7Y-alsfM0uGa5ZezRVefVg6kDeUstZsjLjf360-0LDm6hw2o0d7rNKhR2-GyfBt6Tb8w6a8bKJF_vjt3EKW8EGfjLtdCDFTQJxsgqmSyKQ9six70NXdIYWU1CRAZke20NDuZCfSET3Xog5bHZp4_7AfuEBtQqYGRFE9RKmMI5LpOWvg4SrWTjeuuoIBYhzU9Ci5GaztRRvoagAG0qUtk4ZNXlqpxaxHvkTTFBqKlBLUa0PcihBuZFuodYmoySrkZZFsH5se4t4s4n811O4NWyxAxnZcf1I1WrP1mP_qf96wMCQOxBoEBRT1-RuBIUFGJrnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=eR92BCmug5eVtKOmu5BLNY5emq3lHNNENxfQnyrCiX6H2dSroAGHQCi78V4bU3tM0CHEZb5PyuD5ErapSAPCfo0B2HJplgQc4Y7CqQRrK1hamBb9EChELLGqzO8fWSBz6s5_NAAqxbtLP_Yg1LGba7LfBuR_2fuQNtw7YVQbvWnGVZxyiyR0Y4WdPYTJMhZ0o-D5GLXK4tQRh1_UTjtqpX7UFY11PMszK8-aqUnZ6eBpPN8ndTMa7fcOjesKP-yHdWV9fLHXXaVN_N_eEWdxcfbilLGsGhF2L5fyXypiTs4a8YPuAe0_HMZFBUvIZf_M06zEtkZwXJbsOVUSwiZbXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=eR92BCmug5eVtKOmu5BLNY5emq3lHNNENxfQnyrCiX6H2dSroAGHQCi78V4bU3tM0CHEZb5PyuD5ErapSAPCfo0B2HJplgQc4Y7CqQRrK1hamBb9EChELLGqzO8fWSBz6s5_NAAqxbtLP_Yg1LGba7LfBuR_2fuQNtw7YVQbvWnGVZxyiyR0Y4WdPYTJMhZ0o-D5GLXK4tQRh1_UTjtqpX7UFY11PMszK8-aqUnZ6eBpPN8ndTMa7fcOjesKP-yHdWV9fLHXXaVN_N_eEWdxcfbilLGsGhF2L5fyXypiTs4a8YPuAe0_HMZFBUvIZf_M06zEtkZwXJbsOVUSwiZbXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOKCXLmGNxq_5Vdnw_2hqlstWOS9Zju9xSJ1_hc2w3MdIUpGmCDoooCaFTTbgX54giNfFSi5f0B9TK9aYZ8u8IF7XUPGhJGLLAnVV9WD_gJTQaQS3tKoH4NFdebVB3PRLKDXThRKzv-7keDoRapJleqao06hcYkDAX05tS2XH9_7MI-xIcwnaowb9nyaq4b5aZyaaCvxnPx3oaYCNQH5u_nuzm4P7ffFHdhRorl2G4Onvar9xDDCMHZ2Rzr_irF6VkYJyjtx37X8FAYB7EcsXqp-y5NiFhjXPejucLodHH2uUsges59-n9bbPIuriJ65h7Xep0bm4nOQTn7-GrSnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiB3scoQjTeAmWB8NrYqm-h5qBSdR9iohkXA6EazK70OXokUJQqB9yA-P9Z1O1QXec0DQEVJEknR6PXu0inqvPPDq9_nE16fVxF4R2w_gN02DGxUEnkHDnYcFitLiB4jWAQE8aH4HFE26st0JJeVdxLh_S70E5rNwgWq0nwaj7rq2OnC73vOgD6ibsL_9n1ciIl0KJf_ds99l4EFiV5p0196lLstxABNEMVFXpaijEFvOyUiDrR_XA4RTo_28P57l56h7BfivasepeIV8Fr-Mx2DJF0em5xaaHsV2FzvuysiIVJjRgr2H9v8YJLbCw4K5l5LQAqF7HCNkRBdQzOJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocGTV_2zloGhXjzXmBgA1RFQtYsVsydXJsG_P8Wt_bk7BqNtrHvvuw2tGcJLu6Gc2OSAd3rubyBY2qjl4GBBsYE7BRnYFOQSDmwgYf_y8jh_SN7WEGeBeeFTs28V-qcMUhEKmS9yVp2n890IiGQkZMu8uAbVlIkR6A4Mwg5S7S_e3C8iG9AX0LSxp3929xH31TSbg-Z_uWNiSSGczDoSUKSYmj7-BGHQZw0wDEQoOELwcoPqiCTLNKJK0gyv89MVy6plPrglSHIzq1YbER9LesrASdhTTVCXUQEVaua_JgxIJ8o3AXCpaWcx6QJZ3hhIYyBqA-1ifwgWHLmNjWRX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvin1MBSNjselkuQy0SvJvMxzYZ26QCj__o_Szov0HRjb3vODi4Rgr4fGIqm3TBchNLx2QGfEc9NxZIzLtoKp3N-sfjzAL0TPEuwFtV6umhvHXmv779oTp44C0NuTwzGRyqDFoV__FnWMTD_dpdY60bbXFne1rldrwCz10gBS4bHbLj_vk_2lqxNzXWtc5V260GKJ0OPRtwVZtr2UIrRawizlXrod2Wk8aBkHW_anui2cmYigL1oZQfRJULqyH77YQuuhOk1ARp9I1rOt5mJmkz9PJliHr5vr172Tr_iXC9oKup491P_TCqtvUVb0uXGgW1vfx9LsWW1vNRCRMhapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a29oajhSbkSrelgw66WvRT3LOXbf-lHoBNNagwcLO01UlC7zaHpG18zl2csd8n6mLM5olPbjdp4wLlIzkwwinAXAjKWAjO3otpGZw1QOZh8LzPVN0D_QQcfs32_5EhfxoyzjO_jk0c8HJeT01dAQD4TgPDofS0eyjEldWMJJP-DG4x1TCRI_j4vTvyF3y_Xv4vDrLkSw8X7RoDIAZVxUbg7T20jr_OWNeg-yFXPsCIlUhcz3xyE26YruwxpE14zspJGw743hPmYk6XmfO5DYHPP_shpu4Q44zAV54kK-eSfUOlUQvNjLN9hdFG5KiRca0spThXWxE-fbdbTYuVLfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1yn0lD3Vb145FN8xomL3DA_cC7pYFuGsVwjytvpwwzD0JsZS04BF9lFpQRYIntLcEIfHwySchpbD3shaXD-FoVD66g-CI7xmXbyYVXTRcUzfm4lJLpv9Gi8P6PLquPRe0Arx2lvomOgNRl6MmX5TxW_RS9kdqHpRJvD6kowtQeHatJJgqFsadD2A0LFzsCDLjsw0LsF4DA0-DnHxnmCi_3VVAsyvTr-rw3fNrp4rQrchX8EH71DZjn5hLDJht1y-YqlpQtLNbp3m47n4OkktloHsfIbg_JCJRgcVm2D34XDQh1Bqsvg4Bqxz5o1ZbuElEJlqEIGCRvvhW6-3qaS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQh2GPJbbmjna71ytebtQQQzOGhW-0KXM6bvKgQhK5rEr8Qy4uqlEiD5ADpdCI2YIIRBflbbRSl-5OFQ9CwiyYZutqBPLZiLRQJdT7QzuePs7OjD5vqL7KY-Ozub7GT0nFMbiGJMK4enr0LiI8spiLg-F9sLW1YJJl9HRtUhLNtjSK7z_gyR5eZwMzedowzQQ5rScdECPQ_inZ2m3XP0nNoSUdr4PLBfakw7ZbamxWqVJq9eumxWFfe9KOG5cYJbQNBhfJnP0epswUcPBGbtrxZiWo9IIjtkuSdgJg_GWmGcGIut0zUV7qOi8BhyGDA1tqclWdciZkaD-DC0XLK1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=Wa3Lp426gwdW7wMbmtnMENCZoz3ATbYmgFReouaMSKt7BmiuDBGdY1MU8aZNL0dxuci2_02sjTqqjGYMWO26SKl7WMbpQxXnUS8gle6VNA0g9fIki6Zhtei2h8DDKmOAV5cKk5cxIIAvPtQVjrfOLeEWvMN3jry34inLzBsqP0AsnFbzfqshOQsoni_o3vkeuEKmrvXqBHYF67jAamTXbkiz0D9YdXwzl5Fx1mDjNntZezSZz5Fa6-Z3qt0GHwCRKqoBZAgeo77PZIIuKukPWdxreSX2kGOg1oSS-6YI3DEAuvucc2Kj6k2K8a2cig51nMwu_DmHW29vYrMfaSP2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=Wa3Lp426gwdW7wMbmtnMENCZoz3ATbYmgFReouaMSKt7BmiuDBGdY1MU8aZNL0dxuci2_02sjTqqjGYMWO26SKl7WMbpQxXnUS8gle6VNA0g9fIki6Zhtei2h8DDKmOAV5cKk5cxIIAvPtQVjrfOLeEWvMN3jry34inLzBsqP0AsnFbzfqshOQsoni_o3vkeuEKmrvXqBHYF67jAamTXbkiz0D9YdXwzl5Fx1mDjNntZezSZz5Fa6-Z3qt0GHwCRKqoBZAgeo77PZIIuKukPWdxreSX2kGOg1oSS-6YI3DEAuvucc2Kj6k2K8a2cig51nMwu_DmHW29vYrMfaSP2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دیدنی تیم فوتبال الکترونیک ایران به حریف ژاپنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107108" target="_blank">📅 11:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcZwqwg4VzZvmK_5z1WitwS-ncBnM8ayg-83iBcF-iJWAtMlN5q4M048u6PMnMsc6qmP3Etv5gSEJwKgQInK58F82zCR1V1nKFN-g-onBUWl76uK3VeG4g25-vDvsh4Y8Rn9Y9mx735UzJ52IOo-Xy6sG5nsWlWtYIhkHiIUZqYWaqeqTl7QKsDCm9MgvQirn_-F2vn6U22pWFvuKZDNR8jStM_Uzb4TKqcl-MC2T7qwksW_fW6K7PnEr0EewsNXbZlxSRSavKCMjKeYfomItnLmotlQEQSu3c80CeS0veuHGaYgw83rYayBs5q0izmz53R2AiAggSjhtDbK2umQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107107" target="_blank">📅 10:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFFjfiEqb5NToyvnk3MC-qMlQtn6f_YWipnD2leyLO8-eNXUzt82UtZUadp6rvMk6KkK7C4Plgk9hkc-y4psMCfJ2y1yw0T88dbPgv-wJ2eatB158ZWUZvGD-qPFkpS3tsobD4YYrgGUKo3uTPVoJgeTQl2rn5bo3aTTfWn7SR8Yuw0UOud4v9ODtVh_ug2W_uwcPQ1Tsa2viC6XM42ddx1nIeqIYWvo0Bu34pITB76j24I3gEAQ0gP7-s3VdfuiEfXRI51QJwbDc_0jyUnlR0BAI-rL5HXdBlNw9LWBfwbnZKoOBLssGgfviQiDg-oJ2w-rBhhrWeiNOc3uemdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107106" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYEKPTNTj84Dpwe-hPtt-sRPf0TWHeQppQEOeSgAmZE8b28RscNO-TL7tIHH_4gHvo1VxcXNkL4SQtWuq8I7LNsXitBP5A-zgp6hh-Oquo08QSoI5dmiRIiSG1xefDUvS479cAvN42PkMzjbR17L-VJLoZQce_WQb0IAUWv3oD5ao8tYFJR80WffyC_uQSqWb0HgSQExFzv9W2QRRyBM2hrce6g6yJFg24yg6xVUtGCH3pMyIxBjxbtmSGEdGpGlZe5wJyA9hWJJVnBf1Nyt2lhPxjgh0rS5U5g9TKe2nJVMeRNW0a7b4GBJfM85jAlgTt4NF_m6vPSWPNuH-YueqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107105" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم کره شمالی به ایران توسط چونگ سونگ(68)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107104" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگگلگل چهارم کره‌شمالی
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107103" target="_blank">📅 10:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=cjxax8XxWdlsKAuj8JoH7LAEkA8PrIYUJ2VKrx-BRXGtAiC8fNuu5kkf1UrFNVSmTdOkGcYmp6KJXkRbBKmTUlykoFig8819DOUr-bqbZtCgekd8b27dsBAea1v0cYVs5FcHeiBAdlV9dXFQuhTzobrtfOW8_QdculfEB1rKbfxJTgdKv4QCLXp8M6OLEscbhtYBtWLhd71ZhlJHEqtmX__vOHsiQBE0d_U5mGjpC3soDNbw_rn4e_YxgPc811UuJy72o-Hy9Nhh8vj-4DGdAkVvxktNoOomKVAoJIE7Ys2XabGNWGUJFQnNYKWlijX2i0jAZUqkQGVYbcnhI5-FUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=cjxax8XxWdlsKAuj8JoH7LAEkA8PrIYUJ2VKrx-BRXGtAiC8fNuu5kkf1UrFNVSmTdOkGcYmp6KJXkRbBKmTUlykoFig8819DOUr-bqbZtCgekd8b27dsBAea1v0cYVs5FcHeiBAdlV9dXFQuhTzobrtfOW8_QdculfEB1rKbfxJTgdKv4QCLXp8M6OLEscbhtYBtWLhd71ZhlJHEqtmX__vOHsiQBE0d_U5mGjpC3soDNbw_rn4e_YxgPc811UuJy72o-Hy9Nhh8vj-4DGdAkVvxktNoOomKVAoJIE7Ys2XabGNWGUJFQnNYKWlijX2i0jAZUqkQGVYbcnhI5-FUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل دوم امید کره شمالی | را میونگ سونگ '44 امید ایران 1 - امید کره شمالی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107102" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23009325d2.mp4?token=j1Tkxx6laJ9MOP7uImLeyikBER8Ud5B69EKv6kNJPOAEwKTGm1-MGCgVN7SVZ1eQ9URuW2Ka69zHXnxbsotKbGIOJOb_fxgMQDbDlEHQAAJjUdqUEMZVFQNDEpn4D5a70ejE229mDB9jz7JyBLGA2bMWhVH0w-FDvkyhCf7Bgr0YW_i-W3HTSqkuU-clgvfIyxF_mfkfp1Q9shVUENhVzKs_EODWyvhvOEpVT35mHJHZroDdq6b2NZ7eB2vTZEGNxDWRLyqM22bL1RxgU_NHc4ZeErbxuCmKvNqQHe5wE7khXTNMwHBfUH_UG4Zrib94X3s-eJC3LfPstRz_RZfOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23009325d2.mp4?token=j1Tkxx6laJ9MOP7uImLeyikBER8Ud5B69EKv6kNJPOAEwKTGm1-MGCgVN7SVZ1eQ9URuW2Ka69zHXnxbsotKbGIOJOb_fxgMQDbDlEHQAAJjUdqUEMZVFQNDEpn4D5a70ejE229mDB9jz7JyBLGA2bMWhVH0w-FDvkyhCf7Bgr0YW_i-W3HTSqkuU-clgvfIyxF_mfkfp1Q9shVUENhVzKs_EODWyvhvOEpVT35mHJHZroDdq6b2NZ7eB2vTZEGNxDWRLyqM22bL1RxgU_NHc4ZeErbxuCmKvNqQHe5wE7khXTNMwHBfUH_UG4Zrib94X3s-eJC3LfPstRz_RZfOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41 امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107101" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=c-pPd5VM7VoHpyotcsKmQNv7r5HPrvZQZ4ZmnSfc-hgJm8uZU58IC9mwXs8ROazeR2B45jCbU3r1ZZHHvV0AnceeTNfpLu466-wkUutPr97uba2Vlg2RWE87P9g_Ume7Mz920m6RV4cEl1SYQ2jobsyurEqU4XGfDUmqe0tuzNNf57SUuLC4ikglKU2InMwAd-ZdEHwTs-IIbiU4W1weTz4cppLHyGz1KX_mXgPBC_wSjOEvyRfSu-Ia6YL8UqG0KyJ5-qflqXN8QYNppkdzv_FxBXqwJRBxAwwSlk5pYm9qivzdGr4VM-w-F-5P8aLUeWAC6hLCE7q-yeLg6z3bAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=c-pPd5VM7VoHpyotcsKmQNv7r5HPrvZQZ4ZmnSfc-hgJm8uZU58IC9mwXs8ROazeR2B45jCbU3r1ZZHHvV0AnceeTNfpLu466-wkUutPr97uba2Vlg2RWE87P9g_Ume7Mz920m6RV4cEl1SYQ2jobsyurEqU4XGfDUmqe0tuzNNf57SUuLC4ikglKU2InMwAd-ZdEHwTs-IIbiU4W1weTz4cppLHyGz1KX_mXgPBC_wSjOEvyRfSu-Ia6YL8UqG0KyJ5-qflqXN8QYNppkdzv_FxBXqwJRBxAwwSlk5pYm9qivzdGr4VM-w-F-5P8aLUeWAC6hLCE7q-yeLg6z3bAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41
امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107100" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=mQEhQ3NWiWhLNJBKL2xXtJphKB62HYxqWvY-3mEM6wsAZpcheYgUySHhizekAYnxJ6kuIKfWTp6pZZGkee3lmlsOqHbNtxkWf4VMGbXxiWiSu_OrB_VMmBW0eRUOU-wtrnx7amsixP1onSMmpl3MnvlOsdlzr8I7RZeig3ZVeH_ukwahDzYuiGb12AaYa6_Tl08x17aemGSxFFv0SMf6CzDHX67p7qtMFXIT2KePVrVD5za7xx7x-FSvMd_SilEoAIBlR9_JxIWfbZS2URjiHWlQfQwbN2KcbQyjQRdMPV38AdF09A2m4GNmUvCLQGeT4v0dTmiPy6O5NsnG1FqeTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=mQEhQ3NWiWhLNJBKL2xXtJphKB62HYxqWvY-3mEM6wsAZpcheYgUySHhizekAYnxJ6kuIKfWTp6pZZGkee3lmlsOqHbNtxkWf4VMGbXxiWiSu_OrB_VMmBW0eRUOU-wtrnx7amsixP1onSMmpl3MnvlOsdlzr8I7RZeig3ZVeH_ukwahDzYuiGb12AaYa6_Tl08x17aemGSxFFv0SMf6CzDHX67p7qtMFXIT2KePVrVD5za7xx7x-FSvMd_SilEoAIBlR9_JxIWfbZS2URjiHWlQfQwbN2KcbQyjQRdMPV38AdF09A2m4GNmUvCLQGeT4v0dTmiPy6O5NsnG1FqeTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول ایران به کره‌شمالی توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107098" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=YX7A1xnEas3t-GHZF0F2av7fU77j7_oXvXFdSXE0ie6bCcB4n4xfdmVg19_CDw5wm-idub8QHN9XhgDRy8_kfjeSfKXSNDFGOSaFz1PyMr25YoXlWOttjMNwsVnHDeMBPQve-K769BN_ThoLQGDG_0KSfKaK6nloknr4-lJvAtnZj93Jc1K6sBdV0uxNkoyYBjdZ68iaP3fkX3Yc6Ng8ZfvTYiu5NALAYDkcHeEJ2xG3DVC0NKOtPVVNay3kpEkaFznc7W7xteHDhB0CzlMVckQgSfzJ6w2id-f-66jpG8715zG1Bdbs_I6V4Vs4ZdOkdtqGo9mSPBn5BJTMgNhw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=YX7A1xnEas3t-GHZF0F2av7fU77j7_oXvXFdSXE0ie6bCcB4n4xfdmVg19_CDw5wm-idub8QHN9XhgDRy8_kfjeSfKXSNDFGOSaFz1PyMr25YoXlWOttjMNwsVnHDeMBPQve-K769BN_ThoLQGDG_0KSfKaK6nloknr4-lJvAtnZj93Jc1K6sBdV0uxNkoyYBjdZ68iaP3fkX3Yc6Ng8ZfvTYiu5NALAYDkcHeEJ2xG3DVC0NKOtPVVNay3kpEkaFznc7W7xteHDhB0CzlMVckQgSfzJ6w2id-f-66jpG8715zG1Bdbs_I6V4Vs4ZdOkdtqGo9mSPBn5BJTMgNhw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
دلقک‌ترین استاد کسخل در تاریخ سرزمین ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107097" target="_blank">📅 09:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=Bvj9PlzT37mOLhpgi0bkDroRCyw930OqXS49EhUyOOCIE9YP_4Ju48PGApKf4ad4ngJmMK9cAxXl_m2HJb85oJLXRlWe9l4mgc1kIYPAusMEmoJjyiZA6Izpj455XTYAUHwul2V3sRsmmmH1u2JrekKlwJZdVm9QO-Tjf5h3jCmFoqS7DlwyWVGlfzmen7OeoktJCGDcEBOTUfm5RNRRe58jJ7OJ0Djdx2zGkv_P2tDC2AwsC0EI-BT0Xfpx5tRPh3Xgz_ddEhp3KiwZKdWHoQIMgu1gm6uOSE5oVvr6_F-SF17JsPV5s1Qg2ZkzQ_nZbwDclb0Xe-Vw7kyfTTts6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=Bvj9PlzT37mOLhpgi0bkDroRCyw930OqXS49EhUyOOCIE9YP_4Ju48PGApKf4ad4ngJmMK9cAxXl_m2HJb85oJLXRlWe9l4mgc1kIYPAusMEmoJjyiZA6Izpj455XTYAUHwul2V3sRsmmmH1u2JrekKlwJZdVm9QO-Tjf5h3jCmFoqS7DlwyWVGlfzmen7OeoktJCGDcEBOTUfm5RNRRe58jJ7OJ0Djdx2zGkv_P2tDC2AwsC0EI-BT0Xfpx5tRPh3Xgz_ddEhp3KiwZKdWHoQIMgu1gm6uOSE5oVvr6_F-SF17JsPV5s1Qg2ZkzQ_nZbwDclb0Xe-Vw7kyfTTts6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هیچکس نباید قهرمان شود؛ خیابانی: فصل گذشته باید از تاریخچه حذف شود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107096" target="_blank">📅 09:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE_ZBbG_bHQDc8vjwMx1h3wjYXMTT3Rk3M5o1lWxSM2fOnR1oOe39XZyWn2BI-df4DlCqmK3rrM0I5or1CqRixekNJ_LwGHFI-dFm_LERqG7Vbrv1iNd1SKkQ3USmyu3xjuy434ymKuzgDjzQT9boa_7DA-kj8-y1XGniuh72iQFPIAsk1KijqTAmufxkqeltTvu9HzQBwZwkwJQxPIT8zjk2oD_LjwvIZtPIA6OdRqlqVG9bYG_suu2LBkh9KJYOT7P1cVUi15VTHoL_1V29HRGKiJRXJLGFC-ZW5hLULxjgEFcbmr9bnmdAFeMEWyEqK_bZyYvIPKTLc2fkpH3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOwOmcZSSYABVDHHJrIK3yQ4iGPt-R9b_TzoWQfKEg1SApiYpKS0Yhy8dkmjPtuUNK_D77SeVvOWZ4r8PXVuPCbi5A1q5Q9QhGwXAhi7lU064MzlQDSBqbnMQO29ZF64ioOpDDXT6XjyvdcyPq-UbMHF1y-_RIO7TFoJ23iHIDWPhv1sDnK4aEOnUZ_zp5ARcEzvG_cRIF-r8uckRvfJCk7HDRGuQETJu3O63NgHtNzYDyXj4GrBcdrmYg94R4PFJQZYs-ReT2cxhDFZ85xfyCkAfNmokSaYUb06GNwAM8s0Z19SdkfmYkWUsr6qaioAr_Zrrb9Rh3bxpby1USZ38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcyeXS4Y9Pk5JrCrnSLRlvSiApC-winNgzJbOV1YIFzrV96-ow3MOKWSKTlrySlX6VNm882T6FMnjDMbhoH3eNMHZlvCEL_5N2sWSu-vHFrg64mY2NWEee13wUcdlG_ptJU97_iFcTeVV5USqviebwOHh9OeTQsoqhx7AfV1CYIaqmidYGRJM9x2eskAVqeYJVl3Drv2R7gnKGbwnfqsj5LvNeXoQerKVkSg3FhMpx-OwxAxoeQWdW6g-AFWftijU8-R7yWOg9-f_N93pfOfQyKIhMNMPp8crt-pJCp1WAsMu5tb5IOsBrb8GO0fchS0W-4KVAS523Wo1CxDZGYjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیفو سکسی عربستانی‌ها برای بازی فرداشب با کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107091" target="_blank">📅 00:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107090">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca-F6KdPPwUMxCRmhpSl3SB5dhVVAswMasFjknhgj-AYHJ0j-zfT_yF3QlPQ6_U5xzsYIlfN89O5kweZStqvkRj00nVywg00cmq2IcIR8WLNJNsarpjntFwnJQWLraMEwo9sJSzxjo0bvdM3MLEk6VT0tNYMKwxc8dAnFFZqThYhB1shx6MFI-G97fKtcG8hjQGhmGvrtvbHnRdDMESt01S7mxi0Z7UrN8rzGaRAePrTtoNMbOKfb5aS3p7S33xAt4HCHBie-_Mtg0QWaHJYZSpYSE2G24mMrlXjyn4ZreHI15rSkWQyE8piBuvUOkLvYQ0KdeBluZc902mdTJUkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
عراقچی و ویتکاف در حاشیه نشست امروز سازمان‌ملل با هم دیدار کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107090" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107089">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP7GYxe3EjqzU_7SYu4QsBbRKpt_Z5reDqlx1n1ZBVSncRe7HuQHYiB5Ya9gcf_ZsXN1QUfqT-E42wEhfTSmTlq2XvIz8EzqkW2PMRjGmdWABPDe0I_LJH9zUdLtej_VcJ2tYzE7IoZsh-_McDovR9VxfkwXLjOsuzlBKMwzi8UUnR5U_Gx1hgZ334V-10a_zYSobrA8hUBFvdQWL9QQ4C9LZMGKm3PoGrCdvqWnY3rRUSeMjLkCLm2uIKZYyOwmU_dzWMIv7oXSUEGb3m99VGW69-sV2EeszfQEjhDgYhDm4glt3PDez4cViuaafCk4arBhIKRbWjc49LYKlLq3FnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP7GYxe3EjqzU_7SYu4QsBbRKpt_Z5reDqlx1n1ZBVSncRe7HuQHYiB5Ya9gcf_ZsXN1QUfqT-E42wEhfTSmTlq2XvIz8EzqkW2PMRjGmdWABPDe0I_LJH9zUdLtej_VcJ2tYzE7IoZsh-_McDovR9VxfkwXLjOsuzlBKMwzi8UUnR5U_Gx1hgZ334V-10a_zYSobrA8hUBFvdQWL9QQ4C9LZMGKm3PoGrCdvqWnY3rRUSeMjLkCLm2uIKZYyOwmU_dzWMIv7oXSUEGb3m99VGW69-sV2EeszfQEjhDgYhDm4glt3PDez4cViuaafCk4arBhIKRbWjc49LYKlLq3FnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
اولین تمرین خروس‌ها زیر نظر زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107089" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=tDsEzMlVyV69unu6E9VJYF3_-xU-V3kshLjds6iKmi7YxDnRtjiLgaiVQwVrXm1rbDV6f5SBaXO2iCR9nqW8aI7hcAPrTnUKUFXraDP65XNSDcWmRWLyTnfhbcpOegbaX4WucujRtbQ-zk1VU2MjPi-zsEmUQqcD7CGcM_LkfvNLSWIKFn-M7WJgenO9vASRt3_WL_5kFbiKR6A3gyk7vvJpJNkm2-twyS71IB_fHPn-N1ceYtLhzrH0IuJpJFr3GLwyKeKouazrc4PIWTRfAfP4DPB_LTbTEk615uX64irdywV7Y30Sbh9WWWAY5oXxNAz2tyqJ90JBec6w-gMYg14KgH-ggVQDyBh6jv5jALUHaPejooh7LLju303GN29ssWS3LGHs3Lwv7lQKnrYGOF6rGwLUtMYK94YOGAjb1_PJhXqSc1s92Rzdl_aIjqdMPRCoNWb6WkC5iRSSJoB3IklUjZZwXkiV9ZMG4VeRJEyLbN4Ee5bqcqZthLbrFhU5TgNoK8FPQ7aAC6sY-OTilXBtbLk6jLhboDfRXfY0h6WmEbOWENlgX6CnEzxgrgqbg_dKTXgzqT7S1kf-7Xb3xdE1x-OpMpR23-FM-m7aEPu35UivhlfQnX71H9W9jI-WWm9BNDRnQhGptIJyHfe5bcS05ZG8zVr0XZZT3Uv4BNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=tDsEzMlVyV69unu6E9VJYF3_-xU-V3kshLjds6iKmi7YxDnRtjiLgaiVQwVrXm1rbDV6f5SBaXO2iCR9nqW8aI7hcAPrTnUKUFXraDP65XNSDcWmRWLyTnfhbcpOegbaX4WucujRtbQ-zk1VU2MjPi-zsEmUQqcD7CGcM_LkfvNLSWIKFn-M7WJgenO9vASRt3_WL_5kFbiKR6A3gyk7vvJpJNkm2-twyS71IB_fHPn-N1ceYtLhzrH0IuJpJFr3GLwyKeKouazrc4PIWTRfAfP4DPB_LTbTEk615uX64irdywV7Y30Sbh9WWWAY5oXxNAz2tyqJ90JBec6w-gMYg14KgH-ggVQDyBh6jv5jALUHaPejooh7LLju303GN29ssWS3LGHs3Lwv7lQKnrYGOF6rGwLUtMYK94YOGAjb1_PJhXqSc1s92Rzdl_aIjqdMPRCoNWb6WkC5iRSSJoB3IklUjZZwXkiV9ZMG4VeRJEyLbN4Ee5bqcqZthLbrFhU5TgNoK8FPQ7aAC6sY-OTilXBtbLk6jLhboDfRXfY0h6WmEbOWENlgX6CnEzxgrgqbg_dKTXgzqT7S1kf-7Xb3xdE1x-OpMpR23-FM-m7aEPu35UivhlfQnX71H9W9jI-WWm9BNDRnQhGptIJyHfe5bcS05ZG8zVr0XZZT3Uv4BNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQCPt2V8U-i7DPwoP4dth4lW0Sup4N7duJUxf8PxdG7K8jTV6yQiPUYyUEHC4tx4pUQj2blew53PeBYBROLHLtPlW0V8du4A7OybV3zGi4VosSRH-Yk-ff9fx4t_1jikIFteqMoq1TbJNBd1xhO6CLFG5tJf2QUmf6zvFaknw-XMlJ5F4WjiFaDbkTUF2NkGwbLwic-nx3Hxi7i8yjvKMX5qHUhaziWIhVD0R5J__dPbhoMIdnazWL3hN5yZuelAJQd4ATK_ujS8q1E8DmALo4W4fxppg74dWmBnRwD3i9m_NjXEQ-6R-VYbMEv7ZUS5L0drwPRYG0kkvtXnz2yqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=TRv27G_d7Yj-igNEd4XtcdNPFF9fwaQOQOA8ZQQcFojNDOswvaHrY78dEIMzp1XD-tF9-NomzBe_MYjagWwxSdUdHtCfNpFClez79huoQiyHZmNJmEO3XQEBTgfnkn6dYOOCt99c_c0-aaCkNfXIn5VOOFcsEi2S4LLmj64Zjjtq9nXqJ21MbAg7SWBqTi6sZh1W-vXvKDbxjWdYMbTNlgNsjeWtGYrO6Ih7cPtHLK6bsYnYJjVoQMqIlCFCaOKApjXnT9zMPLkSzJWklCK19wO7-wfT2ASz00ocLUV2QLE7t4dnt7-weCAz0FG2EIjs-VCYmasl4Q4n0i4A6mIwjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=TRv27G_d7Yj-igNEd4XtcdNPFF9fwaQOQOA8ZQQcFojNDOswvaHrY78dEIMzp1XD-tF9-NomzBe_MYjagWwxSdUdHtCfNpFClez79huoQiyHZmNJmEO3XQEBTgfnkn6dYOOCt99c_c0-aaCkNfXIn5VOOFcsEi2S4LLmj64Zjjtq9nXqJ21MbAg7SWBqTi6sZh1W-vXvKDbxjWdYMbTNlgNsjeWtGYrO6Ih7cPtHLK6bsYnYJjVoQMqIlCFCaOKApjXnT9zMPLkSzJWklCK19wO7-wfT2ASz00ocLUV2QLE7t4dnt7-weCAz0FG2EIjs-VCYmasl4Q4n0i4A6mIwjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=iB4Hj620Wnys26ps8sXWAuRM16FsV07BzQzVUOi8aTj_2aT6VZxUo5jQ6vIo26J32RPwxo5b3Ui8R8gCKP8BMC2Ojd3DHAc-zKEce8KpPdRxbAt10g7MTnSkEEjxkuhGCulz2-qfzngokTRA-w2BXzIeBHNwAkkSwUfR1D5-vrIokC8hKJ231ynY9Ov6AryKBFQcgzdSkMVoJKlAPWpG5lH6k5nJpPvo4S6KUGAsed2AcdaAdSpVWfTI6V5UGmei6py-caa1cQRcrZ8Fwfn-uVFZxLipV7axLVnVI17dG2zxZGrkSL4u0mGyka3u90ByKiEc8pluoN1y6NQJ1nmk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=iB4Hj620Wnys26ps8sXWAuRM16FsV07BzQzVUOi8aTj_2aT6VZxUo5jQ6vIo26J32RPwxo5b3Ui8R8gCKP8BMC2Ojd3DHAc-zKEce8KpPdRxbAt10g7MTnSkEEjxkuhGCulz2-qfzngokTRA-w2BXzIeBHNwAkkSwUfR1D5-vrIokC8hKJ231ynY9Ov6AryKBFQcgzdSkMVoJKlAPWpG5lH6k5nJpPvo4S6KUGAsed2AcdaAdSpVWfTI6V5UGmei6py-caa1cQRcrZ8Fwfn-uVFZxLipV7axLVnVI17dG2zxZGrkSL4u0mGyka3u90ByKiEc8pluoN1y6NQJ1nmk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=KPuRNZGllF4xdREZwNMivWlUYCDEWThbQUgMdQBswQNWC__uyHObebNQvy4X7ayxTGLi0fxs3LmuOKVjSh37cgTwnw5vY6PdG35RlmCX3C7jVRRGvIfzJfUQgBWh1uR02LldBdkRsVh9B1-sYReWM10kh-VFoDFgSmYPo5LqXTJ-1Pfr20As4KNUNnpGmvSkkbHkgDgawl7ALfXKghE-F968gUv2o738K1IIDhhWysNMzROjhA7CMAkmvXe5UC553O3krF6513iUewaopoisv4XqiwGJvklhi-K6kWzP2RpM15muKjdnwaP03Z7utP8s2dVczF2-bEi6PMYyJs2BDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=KPuRNZGllF4xdREZwNMivWlUYCDEWThbQUgMdQBswQNWC__uyHObebNQvy4X7ayxTGLi0fxs3LmuOKVjSh37cgTwnw5vY6PdG35RlmCX3C7jVRRGvIfzJfUQgBWh1uR02LldBdkRsVh9B1-sYReWM10kh-VFoDFgSmYPo5LqXTJ-1Pfr20As4KNUNnpGmvSkkbHkgDgawl7ALfXKghE-F968gUv2o738K1IIDhhWysNMzROjhA7CMAkmvXe5UC553O3krF6513iUewaopoisv4XqiwGJvklhi-K6kWzP2RpM15muKjdnwaP03Z7utP8s2dVczF2-bEi6PMYyJs2BDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=NYbfxw8LNyTVN7_SURyNYRcH_vwjxQnuZZu8wL3iREELdXK47xZ6HEAX6BN-uBTJ4iIxKmTqOVf5CDACfTVM-hz3CvrKMvXRPnKKCuvQUbd_JYoD4hAP-W2tIYhgpecrWXQNhl_YqyOvtYmXUv45ikrVmb5oyCVKPlFQTTk0kEcN5jZpia5atG7uR8SPFP1VTOLL32iqosICAlPGGu3ykDt2CULNJnSGa46_hAWdCsNBz-fDYSuIqeBRvvRXszhKv1WFK3Occ56AaYpPMQzSYBAoNDA-ejjkO_v-eDPezGIoNDkjXxzXnFQXUtpiTrjJyemdbY7zVWL1WlSS3_8oEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=NYbfxw8LNyTVN7_SURyNYRcH_vwjxQnuZZu8wL3iREELdXK47xZ6HEAX6BN-uBTJ4iIxKmTqOVf5CDACfTVM-hz3CvrKMvXRPnKKCuvQUbd_JYoD4hAP-W2tIYhgpecrWXQNhl_YqyOvtYmXUv45ikrVmb5oyCVKPlFQTTk0kEcN5jZpia5atG7uR8SPFP1VTOLL32iqosICAlPGGu3ykDt2CULNJnSGa46_hAWdCsNBz-fDYSuIqeBRvvRXszhKv1WFK3Occ56AaYpPMQzSYBAoNDA-ejjkO_v-eDPezGIoNDkjXxzXnFQXUtpiTrjJyemdbY7zVWL1WlSS3_8oEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=Oox-krJ3Qhi0Mmg5pQy6x1BerQcDoccJMmxsZNAPmFYhA02PcfCUga-7fEd3VDiGWzeq65tRH0Rq9vdpIK7sVdDrouj9eIfuo4soEC4caTv4sLv3v-qoGIKy-_EyYbYKTYcIhRqaOaKRvXSLiBplriGqtXrzJEqS_ccZnWnW-RU4zGsH-Vj-DWBhrlmvJBNExkYfZaVK6yof2Lh3QyZ-AJanwPFZ0QZDZgHpGWhQRLVu2Z9mJddafPKpqopgvfbEccELhj0JxSioZAvk3A2WDeyh_WKk75N_6yLPuuo4BTlgPgg6NNPprExtwV-V-2GQoO1BC0Oxiy34_ASWyywkug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=Oox-krJ3Qhi0Mmg5pQy6x1BerQcDoccJMmxsZNAPmFYhA02PcfCUga-7fEd3VDiGWzeq65tRH0Rq9vdpIK7sVdDrouj9eIfuo4soEC4caTv4sLv3v-qoGIKy-_EyYbYKTYcIhRqaOaKRvXSLiBplriGqtXrzJEqS_ccZnWnW-RU4zGsH-Vj-DWBhrlmvJBNExkYfZaVK6yof2Lh3QyZ-AJanwPFZ0QZDZgHpGWhQRLVu2Z9mJddafPKpqopgvfbEccELhj0JxSioZAvk3A2WDeyh_WKk75N_6yLPuuo4BTlgPgg6NNPprExtwV-V-2GQoO1BC0Oxiy34_ASWyywkug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=HNqWZJ58WgSui_jhSgyAkAZKiA9ZWNy_w19quv72Qv0AwIYwyDQIvtC0J7S2CVa8nnT1bRfvKaWKjsUyTJhBKVlicfJs_4MdElvZS3xYzy7-MGSvynB_Rp_ETgkkw7CH0kNrhfAlOsg6Yj4Pn1Bynr_-7qlr_tEdAprZ9sU3Bm8stHrdVdtTQzbnKZlASDbikODokHWJ2lDVFu4WwU4bwy5kE7OdY3Hgl9_YlnRpxQ0TzAW1WNhlWZTz1j0zFXEMvOqkKsjG50AHeTx1dj-j06tRUJIeuM4dNkWlMrqvoyN5fbaNOLPHWZmy3vI6AxwqXj0VVMkl0FMjW2xAv1WnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=HNqWZJ58WgSui_jhSgyAkAZKiA9ZWNy_w19quv72Qv0AwIYwyDQIvtC0J7S2CVa8nnT1bRfvKaWKjsUyTJhBKVlicfJs_4MdElvZS3xYzy7-MGSvynB_Rp_ETgkkw7CH0kNrhfAlOsg6Yj4Pn1Bynr_-7qlr_tEdAprZ9sU3Bm8stHrdVdtTQzbnKZlASDbikODokHWJ2lDVFu4WwU4bwy5kE7OdY3Hgl9_YlnRpxQ0TzAW1WNhlWZTz1j0zFXEMvOqkKsjG50AHeTx1dj-j06tRUJIeuM4dNkWlMrqvoyN5fbaNOLPHWZmy3vI6AxwqXj0VVMkl0FMjW2xAv1WnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=sDr_ye4pYTOE7PTP00HLIM9bWR9zx4GXGLSYIreYP22xrLY2AKDa61PlWGBk_QxUVCWLjXcFHTHHJOzANnQ2U3Jv16qpHX9W75qdg1ChEcc6HGDKQ00nXTO6UlceYAbXfNUGjTvfs9X8cOhTuEl8-oRPM2cok3PicsO1g1J5BLwrJhuvcd0tEJ2ctezj7jhfRlGc7--FYSy_IywJbiP_XQKx5OSQunWHh_sghWYAdSmVWI6TZnrmtle1zlje-IWhVolefeqSWO5rfxOlQdHkiE6a3-pZ73rxG7enBY-S7UWwjBHgXu6sRJpsjZOcARVzbX7f-DHioM_abWQb7XzMKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=sDr_ye4pYTOE7PTP00HLIM9bWR9zx4GXGLSYIreYP22xrLY2AKDa61PlWGBk_QxUVCWLjXcFHTHHJOzANnQ2U3Jv16qpHX9W75qdg1ChEcc6HGDKQ00nXTO6UlceYAbXfNUGjTvfs9X8cOhTuEl8-oRPM2cok3PicsO1g1J5BLwrJhuvcd0tEJ2ctezj7jhfRlGc7--FYSy_IywJbiP_XQKx5OSQunWHh_sghWYAdSmVWI6TZnrmtle1zlje-IWhVolefeqSWO5rfxOlQdHkiE6a3-pZ73rxG7enBY-S7UWwjBHgXu6sRJpsjZOcARVzbX7f-DHioM_abWQb7XzMKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=M2ANA2rpDClfOQkZhCqZlcRb85xRRSno0TaTZRUtTATo6sjnNIYjA2hFP_pg_goJaoE85-lHWSt7-EwaXhIpklHiMFNhmpC4D7MMtvpNBAA3oLCC3SFgDvlYFU3ytZZcXTA844SRTScn4TJOVb6WoxnzewTqiJiNvyAr3H27ppSwqa29h5PeTkfRWZjJWRYqvFg28UGBdKTAdBGiqjFkjaRmyuHT8aGe_-AMjKV5StMOv-bRHVeGw_kVRjs0OTsMCL8iwQT_qhu6mvWRfsieGP-Q_qF7b5UW4bUF73scez7FiDrwb-eByOLiU6S37_gFMpb6LJr-mhcscQHegUjAMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=M2ANA2rpDClfOQkZhCqZlcRb85xRRSno0TaTZRUtTATo6sjnNIYjA2hFP_pg_goJaoE85-lHWSt7-EwaXhIpklHiMFNhmpC4D7MMtvpNBAA3oLCC3SFgDvlYFU3ytZZcXTA844SRTScn4TJOVb6WoxnzewTqiJiNvyAr3H27ppSwqa29h5PeTkfRWZjJWRYqvFg28UGBdKTAdBGiqjFkjaRmyuHT8aGe_-AMjKV5StMOv-bRHVeGw_kVRjs0OTsMCL8iwQT_qhu6mvWRfsieGP-Q_qF7b5UW4bUF73scez7FiDrwb-eByOLiU6S37_gFMpb6LJr-mhcscQHegUjAMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhWf8fH6kr-cHyZAhjQoqaGNRrdnimzjnp0CVbIulfRhenOb0GQKUtf4Xlv4mgNiLe5CHdRyAMM87_-3UmH0KWBWEH9BirCtAe2L24p7NONf7z1L7zsYssvtOkIkYTveRX0LMAAy2edrYjebBJhw4tyZ4bItrFLzU4M2o1JilTHe_Sjw-ILRra4AYLgLeMIdmu_HRotg401gB_tRhW59JJUN6eghSQUmVDzPFp20o59ma9M92sUvpMndLIWp_yUqhKsPohjFh2-yYzddg2b-USZM6x9kMk-xOsTNJdor8Jzaw1qVdLojdze-M3eJ8oi-4kTDD861hGC_4D9gzw5dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajGB3FVf-n8j4QCmINmh6buQsxYzz0Fgc0PpGcfxxbIfKq9nJ06BxoewA7evTv-4TApAjRbUxPhJQC5yCVZCqr3OvyPlNi5lve45w78s21f5cbn3zyAq0iMSIMBLgSHG5maQVG_uXggRBqqn9QFA1TBG__8CRJ8bXfY2IiMbbWubi1uWJiGy8BXVwMJmLYkTYpvm-C1M4iqW5p0eDmMLamx_7yYM6BypfWE5tPYMAbBBUcNtmp8Nev8hKOK3nlmb5IpNJoCpdDPWKfq_f0VkhB3BHsyxVTp5-7yKALod8ldSnVbtqYcxxVLfCF1czHarjSnv-516RqiBtFQvByXefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGkoUBMy7h-RNMAmjDOqml-dr95PnpI7iypLcD5qlR84tzBlGaOBjTZipCE3DSUxxgqrmDq2oh9uC--usfB57QUL_yTex9bEl1wbOrFtb7CsAUam2GZSW5h81HgEBd7ZSJFvsjNhAEZ-sdVwEDlQ7vN89Tjy4Ko1QfG9sgQdkFSE1Rw6OLbBzkJ40ACe9-C09yPqWujbxRNq4I1p-9kN7exUdy7KOvrSbc6HuO0j-ERGJLllsLt0FwH28g-jLVvXGij6UzPSf57O-Vt7b_H6V7Z5byt6GUs46Bv499TSzzSOrt4Ps7oTPbEsQVGSIFrTWDHYMZGknEAopobH0CMxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=KVKGFBdZ5AwoceTTn6DpAIbBbUQ6QUZgxLXga9NsXjT8aixF4yKd4NZlmC0QYejOq-XY56xGSMfSMgmPAZIMppO5knDhNfgIKeJTx1kojTlOq3R2jxFakxFPTn6U6fBGzas_33at8GiKV1RLQt3VF1-PxAq3tbJkpytuPBBXhUL7pZdRIyjZfqPoGDmyr3yT_eMT-ckGY_qlZPsnQTG_KcvFCHeeolhuadFr1_8ClVKtUlUhPH7h7TiDJE0tRFyPuH8vb6p2tLM1yLArlC47K1BVt8VKicYPMuIfVXcR7vPGTsJXSEGaM-nFh0Z_jsjZDLWWp80IuAKNK8TAW5zvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=KVKGFBdZ5AwoceTTn6DpAIbBbUQ6QUZgxLXga9NsXjT8aixF4yKd4NZlmC0QYejOq-XY56xGSMfSMgmPAZIMppO5knDhNfgIKeJTx1kojTlOq3R2jxFakxFPTn6U6fBGzas_33at8GiKV1RLQt3VF1-PxAq3tbJkpytuPBBXhUL7pZdRIyjZfqPoGDmyr3yT_eMT-ckGY_qlZPsnQTG_KcvFCHeeolhuadFr1_8ClVKtUlUhPH7h7TiDJE0tRFyPuH8vb6p2tLM1yLArlC47K1BVt8VKicYPMuIfVXcR7vPGTsJXSEGaM-nFh0Z_jsjZDLWWp80IuAKNK8TAW5zvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JffHaE-ddTBAeIHiw66cFsV2fg-jvtYT6VwNJloaM8DIsMKLAMuJkN-jBCBpOzTVbg2nSGoQq3hGwDHuVJin_eiz-ISvJsGUmj6YMaqEfvOGwDiPJh5x1SGgDRCeLSIZygKzFosb_hlU0JCx9_J1z7dGMrTkuF4mhzJ-OWO5ivPB7Din1ynYDcUn4adB9tjWG0KV0peKTOTjlqpmbe9qAUEgWcoeADjejly9JuQGG3Do2nxkKmh3TSVH95VklyhyIEKERk7Zdg-IbSW_fa8GWvubDldw11jGgX6F_zmskrkUUrl5WojZcIxrEybyuiQZ10GlFPYxZBKpEmXY0AVkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnYthSlqD_U3Is-BZnZQxcBZBQ8zsMHNi4jkfWpwykcooZ1d2aEydUJADjiwvLK-vFgjrbzGcVvMLRBlYmwWdHLRUrz3pk2nlJLhWQQX5PvTQ_i1syFufKBr9r3vot-mlr7t-1gw-E0zJmJ5-pErMJWrLA3SJWOOwpnOUSWddgqOIDd18tN5nTaWxjkkg4EsA5e6O39a4pKouBRGVsly2tFlGPHyRS3kqAWpLdcOWvXbYShIr9H_ccxwImfPyToHCc3XyQsb244qEw7gsoF8WUxGSPC6lzyMfgj3gcBbE597MxJ1x-_YNyt7sy085ftc1FPvmTjU72OZdOInXEuAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJLV8PODX_jrx_uCJqzPmAZrOk2XOj_3ISKLTjXzn81nWkBsOKVWlVrI_VPPYpaAa2z16ukYfCxbJtbzk6LBRQqQUxJpJasFBR60OMmP2BC6ovAiYDE4Y2Zqkm3BLNVz0jqPOXNi5mM-a4cePvsuWTl6yrFk3ceIy82qigl3r3G6oE7PtlWF0gkDwm_0YQmXJiI03YYHtLe8_u1J1sO5haiZHV2QepdMc0NrLMWzaCi41IlTqSftE37unTR-oVQzPm5jnFvaempyFkD1na1PC17BISNQJxi5Ov09pqQL9nIWW9aEpliWtJW73ybvrzdQVRE6bwl6Wf5sEBocOBP-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q27umpnoDwZk9DVe3yp2QZbXy_lJRvQaiK0Vevn4Nf42MDW9N76BNnCSJPkU7mCio6-qV1_RboXnOjWnDS4nm0GaLngKRZhKFXb_b_kUvOPBzgBgGvs8t3FLIbCCN_XRo2hDKj86shKC1QufkInv5aAu4xwqgjK7Lg4PVX3ODXOWxi7xbjpOqpXAg8Ps831pqBFw6Wt-yBhUae1tqVkDbdhyQr3866urxQ9mAloR4nf28qo2qnesZsQIDLM9Prx7hNSJaAb0D-gTlWtgkQA-OdHAKGvz3M6ZqPMMevx7bXfsM1jzBCm2u7qgjeiFNd6hNuFu1ct96HcC5tukY_kgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftAlc36hG4rKQG1CbLOOlxtHGgHDcj8MNiP0CQkm7gr65ckbZHVI0QGxlvsrZfG4RmGjAUf_hSAD3HBqls46mmO972QfOQ8BYroeIIOt04LtNXgi3WnVO83NQ5zROWi9V3q8bSDH0In-qYnLGzLO3Ek4dg2yHYUP5laQlRNHXEb3l37DnmPnvAQ8x5EZvUQBoML313ipTfEprNy8nE81wPMGYe7jBAQgKSMntJWGIrA5QG-UQvPQ2Y9ROZQ0hch5YTslzaAH2qZrJqzpdFH5BJLtGAyhBCZG3D6omnbYDoqDrHQwAljVMPnAnAbSAOm59jP8-bbgutn3-HvZo0-guA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=gBhj1bMWeAOOLfZMGXMoum5edV6aUumkh6_Koq857bTahIG_4oSN12IZhNHUYNjtEsxxjgc-g9sHOMzKWcQtSqNZrUi8F1QGBhLrF78eulN1mZ21m4WwUBByasDtXVD5M4kx_X-A1iYmQoB-Zmv0Fu3bQQ4M3bgCiDrD83kqbMglNRLRsSVlNB4lfpA3FPEQaIhpZLDVs5k4A0aMNMtZ_1OlKOc1aqdU2bn-vB2mGZ35zZZd85rsB8IgnsV8RvML_muz5B7iLhkyA8nw3ouxJjoaBQs-_P2NDkYTg1xT-yko-Xta73ItZZvbdsf9knE5AnvbNYvIMbhLOJXRagIQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=gBhj1bMWeAOOLfZMGXMoum5edV6aUumkh6_Koq857bTahIG_4oSN12IZhNHUYNjtEsxxjgc-g9sHOMzKWcQtSqNZrUi8F1QGBhLrF78eulN1mZ21m4WwUBByasDtXVD5M4kx_X-A1iYmQoB-Zmv0Fu3bQQ4M3bgCiDrD83kqbMglNRLRsSVlNB4lfpA3FPEQaIhpZLDVs5k4A0aMNMtZ_1OlKOc1aqdU2bn-vB2mGZ35zZZd85rsB8IgnsV8RvML_muz5B7iLhkyA8nw3ouxJjoaBQs-_P2NDkYTg1xT-yko-Xta73ItZZvbdsf9knE5AnvbNYvIMbhLOJXRagIQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=tW_J4unkOSO1s80R9KJskjTlQwOUJ6mVILWxBRXYXEWvoW1LtC4czYzNdUb9mTJjoCF30vKp4wiNHxdGxbE-Ghs5N8gPY1uwqlbIr0TvT-fPB8pUMjvlPjqY0b8djUfpkxmMNEDcaWF9c-7Ovq6BXysTxtiMOqM2LyM-NdZPSES0oqVhXJp384I6lEPInJtDKejJyUHenY8PUpk8SOj5Hd9vLBB3kwYFbIo7EK455CZ2lwa1x0ZoIcU0xcISBWGKdzhdYIQJ4TZ99ALCy55nuCdhwhVT5o-U8n3JjsUP9uvgC6QL5m_E9e1htFTmOUmb9pOUVEtFpqeOp7IySK6GVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=tW_J4unkOSO1s80R9KJskjTlQwOUJ6mVILWxBRXYXEWvoW1LtC4czYzNdUb9mTJjoCF30vKp4wiNHxdGxbE-Ghs5N8gPY1uwqlbIr0TvT-fPB8pUMjvlPjqY0b8djUfpkxmMNEDcaWF9c-7Ovq6BXysTxtiMOqM2LyM-NdZPSES0oqVhXJp384I6lEPInJtDKejJyUHenY8PUpk8SOj5Hd9vLBB3kwYFbIo7EK455CZ2lwa1x0ZoIcU0xcISBWGKdzhdYIQJ4TZ99ALCy55nuCdhwhVT5o-U8n3JjsUP9uvgC6QL5m_E9e1htFTmOUmb9pOUVEtFpqeOp7IySK6GVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=nUTbVdIh8HQxjICzxi0VueiZoDqOjq0wwLNGxKsBpiBADL_IJH12ACOu4eLBgO1aVVKx1Eu0_6cCVMOrl2lPBPS_Cm1M3W6Uuvb83bet-Vnz1ljSi0_m3ilkQKfDoSrjU7ZtD9_ptMCQL795xcv32OxiCRPJWpD4ho_bfi8VzKtzBQdRKBhaRUEHs1mXL9HyPlXq7ifAuxfkJr8MB8PZnY6YGO7I6MeU7TEfM3dBBbV2mVek0Y7MuC5rD30YM6hYpOepES6kYNe7LGTv91VmGNf1IbrZjSxfXsA12XUUl0k_prK9N_YckK2U4C5yFBFAEsFGpmlWq2M6QsTNcOYWBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=nUTbVdIh8HQxjICzxi0VueiZoDqOjq0wwLNGxKsBpiBADL_IJH12ACOu4eLBgO1aVVKx1Eu0_6cCVMOrl2lPBPS_Cm1M3W6Uuvb83bet-Vnz1ljSi0_m3ilkQKfDoSrjU7ZtD9_ptMCQL795xcv32OxiCRPJWpD4ho_bfi8VzKtzBQdRKBhaRUEHs1mXL9HyPlXq7ifAuxfkJr8MB8PZnY6YGO7I6MeU7TEfM3dBBbV2mVek0Y7MuC5rD30YM6hYpOepES6kYNe7LGTv91VmGNf1IbrZjSxfXsA12XUUl0k_prK9N_YckK2U4C5yFBFAEsFGpmlWq2M6QsTNcOYWBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=D0X63fTo5oxzx2I5mhz9-dhhISXfy98pQRFrr8ydkPa0I2pATTnMgnF5pLmHh6yPRFYYzE6tTPnretM0XX1WouY52BFcnImX2_z_3y6rb-LKz9M7V9s5NKQ0JYMLhmiFC5kBqbQaze2xt3pL3zvrNrmIocrqD6iaZmYufDFAoAqJvnOqFq9X0QgGlltjusxJx3vY9jBiHqvBru6CWgN04kMfdph_7kzv4DhBWbSqHg433GtJ_zPn30J28vJ6Tn8YKneZxB9ZsXwo3aapZAAplMmjGEa88Plecj5cJIOGQz8Zo11wNxbnlSkpKcxiKt3V0Gkg_6ED1oQcUAWEAS30yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=D0X63fTo5oxzx2I5mhz9-dhhISXfy98pQRFrr8ydkPa0I2pATTnMgnF5pLmHh6yPRFYYzE6tTPnretM0XX1WouY52BFcnImX2_z_3y6rb-LKz9M7V9s5NKQ0JYMLhmiFC5kBqbQaze2xt3pL3zvrNrmIocrqD6iaZmYufDFAoAqJvnOqFq9X0QgGlltjusxJx3vY9jBiHqvBru6CWgN04kMfdph_7kzv4DhBWbSqHg433GtJ_zPn30J28vJ6Tn8YKneZxB9ZsXwo3aapZAAplMmjGEa88Plecj5cJIOGQz8Zo11wNxbnlSkpKcxiKt3V0Gkg_6ED1oQcUAWEAS30yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=VDW-PjwRaY6dMudTurRoJuogEu8hhLuNeN37hLvGSUkL_TSpQUOAsB4M4lj_5CgZIQ4b6E4fmTDOZN_13zrlCai1Swp_90oZ0YwywYmpdJtnk1GKeJX_ya9Zk3sAT371hnY994j5BwzL3aI1C27-Ilg0a0GthVUUxcLs8FoGDY-OUUiET6LOfBA-2TiLk681NfDuO9jWjahv0nwTu92pYByJ3F1J0UX-XU9Dcp03zwvdxeXEPf56Yr5-et2LTOSowihlFSiS1dAZFZUtmQvllEv3ToBh_LiEKg_sQ28g88lB-7--8AKEXK-WO3pxrB5JP-swM8mkUF1AbVxWWXaQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=VDW-PjwRaY6dMudTurRoJuogEu8hhLuNeN37hLvGSUkL_TSpQUOAsB4M4lj_5CgZIQ4b6E4fmTDOZN_13zrlCai1Swp_90oZ0YwywYmpdJtnk1GKeJX_ya9Zk3sAT371hnY994j5BwzL3aI1C27-Ilg0a0GthVUUxcLs8FoGDY-OUUiET6LOfBA-2TiLk681NfDuO9jWjahv0nwTu92pYByJ3F1J0UX-XU9Dcp03zwvdxeXEPf56Yr5-et2LTOSowihlFSiS1dAZFZUtmQvllEv3ToBh_LiEKg_sQ28g88lB-7--8AKEXK-WO3pxrB5JP-swM8mkUF1AbVxWWXaQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=v9lxOqAQLgl1BJE_GdCgiBWn5wtB4XVho7IHEHZ48w4Vpd3bdFIcAnvrU3KZHFL0ICkuu6n2ndiiA0RTnKrIyaG7MqblQ4nna5ZmwrXqR1o4NsHwTkqPH1qMgrHcN6tQLdtmGjETb2f4wf6J5gxAWjxB_Ha4r-R9yLM08i74BdcoUvKtN1LIXMl4Qj0oDseVWEpBQ5xfAYRQh4xIFpyj8EKekrRXU1FNpFDbKdND8mCVE8oGWHhFsXCh7Wdg_SuOFyKg1BkdmVavi5Vji4YYzTX98q_GP65MlkkeZulo57n1p95egSaP3wgOwmvz7O_q1Umx0ewdE3d7DLFmMTUshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=v9lxOqAQLgl1BJE_GdCgiBWn5wtB4XVho7IHEHZ48w4Vpd3bdFIcAnvrU3KZHFL0ICkuu6n2ndiiA0RTnKrIyaG7MqblQ4nna5ZmwrXqR1o4NsHwTkqPH1qMgrHcN6tQLdtmGjETb2f4wf6J5gxAWjxB_Ha4r-R9yLM08i74BdcoUvKtN1LIXMl4Qj0oDseVWEpBQ5xfAYRQh4xIFpyj8EKekrRXU1FNpFDbKdND8mCVE8oGWHhFsXCh7Wdg_SuOFyKg1BkdmVavi5Vji4YYzTX98q_GP65MlkkeZulo57n1p95egSaP3wgOwmvz7O_q1Umx0ewdE3d7DLFmMTUshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=AXmSCBIFk95ZTc7vTnQkDOS8gf2tGT92abxa0V5ghguNNeBh-kB98oMdPbqj8QVO5M-982eFF-2R9prjOUpuzRz1QkLXphyyE5XwAXWg0Vuok16zymzbYxPYTtNxmrpXrWuGgK9aJtet8zyOgtcHXn2p9CwsBb8ATjiXhMMxk_Na021T3cssLBjZ-7n2sMFMaN5sZmNHby2JAXJdh8OK2WRPi63x5_KgkduVENmH2OlYzcqWyyfbI0boTp0FFiCh3Usm7KhwpzjrvafqkB_w39a0G3EzjjiX2uuZ_Qnn3h7mvZjaV_7bxThPNxZ6QGjLvykgC5ReiWCXYsL3XZeM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=AXmSCBIFk95ZTc7vTnQkDOS8gf2tGT92abxa0V5ghguNNeBh-kB98oMdPbqj8QVO5M-982eFF-2R9prjOUpuzRz1QkLXphyyE5XwAXWg0Vuok16zymzbYxPYTtNxmrpXrWuGgK9aJtet8zyOgtcHXn2p9CwsBb8ATjiXhMMxk_Na021T3cssLBjZ-7n2sMFMaN5sZmNHby2JAXJdh8OK2WRPi63x5_KgkduVENmH2OlYzcqWyyfbI0boTp0FFiCh3Usm7KhwpzjrvafqkB_w39a0G3EzjjiX2uuZ_Qnn3h7mvZjaV_7bxThPNxZ6QGjLvykgC5ReiWCXYsL3XZeM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCrTH5DgY4S_khiwFMhB1s25i5aVN5xp6A2NY2KcK46DPnLTHs6iXEcHmE5Myde-0kNK5DdTb79lEXc7VK3jYhI-14lZ_nCHPq6nYz9P4hnXc8mEQYIAmyxmfjf41dzZjtHlhGCqHYvonhvjdmPo86DfaHP4t2wnDinMomzYW43Eitl9zyL-9ZECFbIwerSjwzpBfvkBpIAd7h4dym44SJtzdABxItGsWGFlmU9LWKDtweyliRgFadsbexHZOssb1teXGCjvLHsm4-yBrQuDmQlaYHdOnwnZvADLoF9tRcC4lEBeYcuaxVDAkmkGto7HyQKiikA-tGjovxg9xFPbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8IE6H9RDYhOOn2QKlOXERC6cKGr7_1unUVDVedbEnmaBgojP7_fWIVHmPfnuJl8Pi6UI1M9pacQbCUXYadyPf4KwgAJMUCHgo7YB0ncWKmgi4B2AOe7cjLuZp6uyacv0kzaqKg2j0IBLk1DIexB03b3DiZ--cU5Q8Nfrl2kwZpn0uoa5d2YzlhCxsG7oJXT_Z_XhBCCgGdZ32ijE8lEkANxp8b4_wqHvpdjwYUVWnuPYC1PMDwGav5ZbvjM5PFKcr_MqeLjGff7RXie8rE1NvfQYoSIXyMAFf34zJfultLWJYzgWip5VuaMa9HtBJ2BUf9eOVPLwlYM_EgrDjbugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=uTPB760WQ_4E8S6Il06J9zxwMuFeM8XD7nrOAlMzCvkA_MSy9F_aZgPVx8EFZLA7PuyWxy5xmtvIbRwoGDv7e05lVRkjXxXMabAhnxvrOE0xj2vw_n80peQXmLIyhSf2h9ihfKJyhDq1nMKhcQymrQvI4rh8Oq5276laHWS69yH3lVWwvkdUW4Qy9nN3R9nWyGYfkTjxQMaMLiyMsoTi2NTCHQ8MR8voqr9JMPau_KSRDeT_5XcuYIxvGSTckynGX1AF_Vnccx7WOV2qO9dj0D3cEHVuLFObv3GptT9b8OqJb17ktAAUl19xePNuCSb-ppqTAR05WyjVRkMMoOakYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=uTPB760WQ_4E8S6Il06J9zxwMuFeM8XD7nrOAlMzCvkA_MSy9F_aZgPVx8EFZLA7PuyWxy5xmtvIbRwoGDv7e05lVRkjXxXMabAhnxvrOE0xj2vw_n80peQXmLIyhSf2h9ihfKJyhDq1nMKhcQymrQvI4rh8Oq5276laHWS69yH3lVWwvkdUW4Qy9nN3R9nWyGYfkTjxQMaMLiyMsoTi2NTCHQ8MR8voqr9JMPau_KSRDeT_5XcuYIxvGSTckynGX1AF_Vnccx7WOV2qO9dj0D3cEHVuLFObv3GptT9b8OqJb17ktAAUl19xePNuCSb-ppqTAR05WyjVRkMMoOakYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=KLYJ7tp8HxmaLwRke8E0F-8TLg5ORlY9FKSgPopy2MNEB2Q0ewzMERJg2e1_Yx8jsrsByvKmX35Nw6LT4_uzg3jK_0cDC8a8yUHFl_en8J6mHlO0UO2P5RHvNm2JarI33SUoMJcEKolAvMZUqATISJDZetl5U35ARO5RFkmePyZEk3WWhE1f5qzhWbP6bcnAqU_0v_2gV_e82f1GXr_c55SQeC3CD9Sl6j3bcu3lK1qaBtNFEckj1PfJ9cLpbrxWu42_Tp9b_l3lC1IUvprRiZbWNFk3rRj58EtJ49WU-pLGPli5e52qpxrhW_Tkwag8KJykS1Rg0SXXfURQCTbqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=KLYJ7tp8HxmaLwRke8E0F-8TLg5ORlY9FKSgPopy2MNEB2Q0ewzMERJg2e1_Yx8jsrsByvKmX35Nw6LT4_uzg3jK_0cDC8a8yUHFl_en8J6mHlO0UO2P5RHvNm2JarI33SUoMJcEKolAvMZUqATISJDZetl5U35ARO5RFkmePyZEk3WWhE1f5qzhWbP6bcnAqU_0v_2gV_e82f1GXr_c55SQeC3CD9Sl6j3bcu3lK1qaBtNFEckj1PfJ9cLpbrxWu42_Tp9b_l3lC1IUvprRiZbWNFk3rRj58EtJ49WU-pLGPli5e52qpxrhW_Tkwag8KJykS1Rg0SXXfURQCTbqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSuTE7BZUhcWZzxC9D4ZeK3RGtj4vbtmDKPwJnsESDrLfVCj2LXQ5ZumXerX5iYPWrzWjK8q_5uI1tAe81A61DTwChkvjF7afwHJSjBS8T1JBWhASuxMUIqQ4sbkzWZGQqUiAc0GmZaHluEoGg4u_Fu18yFlo5SlobIGHQKcCY6uAkn7_shQlL9Fwnuiv39awEF7qwtk2HL7ZddeGfUcQYgDRlQo_YSudIk_R94UbjCy6TQZ9h8dCjd8FlIZqpgkaHL9Zszjr--OiGGsNS08qXKibg1xr4cvq5YmshJXf8gnl582iD5-o199zpMPhtwc6g2PRHLz2X7lpvkUBa1pcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKJ4iBxZweRqFWEVEsJFVM-dk_fcGOtkZHNU_2XaD-BsjBvQVKu48RVX8Mvw7eWabAJi43g5EBzGzmEx3g5EyxrMfC6uBaofgzsJrS8LJ5axcicdQ5BybLhEPaN0-ZSeWvT1_NdRBqOSndTuev3Or-OaB-goqbA4t62lAS3nm1imNi7mshmuOJFuaFvgesJRhGrh4VwdL86yaJVHqxoPCAnofKz9vEwzzsuCi0QgtZGn_QEg07zqQgZi-ng7wq1V9QPSKabDMlmHNUNG74Tq92hz7yRxRlbwyECqFJFt7CGMV1fORONsCX1Z0ln90q6FvcufccABzQ99LwevXFGL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=vmrTx6V1mObBPG4fnfRaS-EXRL1d-199C_F_vioY0mXRUiITHPWxk_RZjBprbj0leJZKRfF0K42N8qNfjsWyC2WQrQESWrfGApY2lNs8nuAGtahPkVcCThJSGplYBRh6ReBeH4pqkR0CTcSx0o8M0YPEiN2Kd6WdXkLpS7En5R_HPVjCk8_UiOZx9rfRIJiXi-bTLLTgAc0gjWVbYs0KaXYHZWoaa6CZ_MDDv9bY6OaWz3x30W9zdyWvH_01lm3Qm_YjmXTAJmrMsfyfelCT05GrTRZhVZA-TTnZxQs9wzlNL7oRhl13nOwYtHZpEXD1c7Ttkf4cQVQjhy1jgTsPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=vmrTx6V1mObBPG4fnfRaS-EXRL1d-199C_F_vioY0mXRUiITHPWxk_RZjBprbj0leJZKRfF0K42N8qNfjsWyC2WQrQESWrfGApY2lNs8nuAGtahPkVcCThJSGplYBRh6ReBeH4pqkR0CTcSx0o8M0YPEiN2Kd6WdXkLpS7En5R_HPVjCk8_UiOZx9rfRIJiXi-bTLLTgAc0gjWVbYs0KaXYHZWoaa6CZ_MDDv9bY6OaWz3x30W9zdyWvH_01lm3Qm_YjmXTAJmrMsfyfelCT05GrTRZhVZA-TTnZxQs9wzlNL7oRhl13nOwYtHZpEXD1c7Ttkf4cQVQjhy1jgTsPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
