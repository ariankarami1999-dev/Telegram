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
<img src="https://cdn4.telesco.pe/file/jA0K8baJmMmMnPAfSP4H0MiMvLrasszTqdjZK5FYaHDGOOxHBYPwS88mWIkKOR9-cK3bJJJoMstjYhcz7s0r0l9PkuF6EuHXNwB9KXAp1SalohM8fj_Q8bSCu1KQaSxvKD2R_PeoluWq78D8rLBkU0T6m8AGo10pPdD6zoI-EgaqSA_LtMREWJpPr88mvxUaMnj6nN_OBZoBx8oUMr9OZeeubnPKo0lBXrHfERNrh_SMEVxNrMfXu9gvJfwqi8vD06YLx-piszm5F5hyZYy2bUqBMR7lKf8x9NMjYdKZxc3RYrYAld704pLKb4BjEgaOt1HC62tm3tG4U_o8HYK0qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 110K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 23:00:44</div>
<hr>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKYqgh1QM4KBwE4qlApLz3M4OKw2C2t_Qjju19fs-0q9RnP4tLn6H4ijm27QgVrj7hde1-n0rpctI8Y1rcrNJajY-RJBwrTks1ld-Mm86eX-mkToKkW6E421KcbFQWQDOCVgeOCNDjOZR7lwKkJGw-MVL1XzuEcwcmHhJe0yBx9kzSLdyg4gmzO6EEpMp9UAypnyuV_s1PMbXMsLL1S35bFxdseeEFf-oHHBraxQswyIMUesC9AYDHw0M42fR9SgvzqV1-cAkR4f03X3Wlyih-n5GNgNLruB_NERS4FyFOLSZeacYqvYnKUxjH4syFFM0TFTJTAvPO9USTAX7_yTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehp-GWeYkLyLx81OyQMaKX1JxwcnZNZULO94GIIoPVb2OhWIvmQASvHmtIuND8d6BCw-h8MV7o3IeI5Yp4ZQz-ZHjgwpE80nt6947iZ0CUO7r1qDhHf4qLzw4Vw_-EoE9bU77VUd9twUkN79kKBqdx6mx4nZDnR9l0_3kiGVHHkM-4Az5x7Fh0QVZn2UUm2ZY0clWy_wQOVOzkCiYlWneuUSIIMvQnOZ1GnJKJy30_CzJkewmipH7FWJeNKddxW6aP8KlbiIDceC0lSvbE5KxvbTz0_P_tpV_8JnwhN-hP9f-yYonNHjg9oYm8N0S5PNHSfY0lXm5emuwTvd17wQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qu2XJKhCzdj-F9eu6LF-9FknqtYx5hw1ilL3hB5_6AQP2zqp1M6B-tS4fcWlOYnqGzSkZsHvKYUdMFTyZrYhvTWNzgFmTqYXRV5hpNJ_mhrvoGvBuZnn73xhu4lhyZWtYc6aEJugBMtEEzXpus-wCAPX4vLvgQBpkjA150AaGs4eoQuYuK7WcUe50YRfuoLbETj583AmO-8u-uRCwLb17SWkdilMPmVE6Oz1sf9S5K5PxBRdASSwj2XDID2uE1R3H5DAC4S6EWCx19aYrYgMbnF9J1fPjMOa6-wryN-bNFlxO8S9s_Tvb7_GI-e5W7oKKVMEeUUvhydXE0hw4sEXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-O0QuWigpruDFjh3UUzD-qk3DP-g3UFQl30MB5TxcBvfVo1cwuX_v7mzGLYxEjHm_S36zRfgRVnHlUhaxxhnFxsMpSyW8yS1e_6R74aAshLaWh8CVIB3mezowWo9NmCm1wVsvdiaUD5cIihW1SA8w-NMHDmwMcR51OJVdkb44fJbjnN_h7tvj3xnFSiSdploHAi4Dim-z_KT9jzTvHAUhGlK6n_s26tJal5OoMiI5hHBUfQmkX4_TI9p_c9xPLU3OLd8KUdWDmvfWAiWHe1KspSLxuDKEiQs09JJ8h1jLQdYoRDM4PxDjgpGRTjFhaFQiQgWyWgO_p6yPY-Vn2fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOQYGUII_C8KrED11cqdF92WAhDC3304dl8vZcFJz565oDSfE7FLf149WCJCI_ppJfYGEUGqZ0yN55638UQ3RavFm3mPTA-Q7fllyhJydQ7H5T8QdGG3uoKoAYw4dpUitW_-vNHz681b2LrAGxFksgdhj07xk6GvSqzmGfjQGhoLRI6mjLfGaTPV3b4woXNTMRD5qF1OF05SDOdac8o-wrtbX-WYxsF_I39OaZ71V_XX9S7cyyeAQgvZIIYMe8uqYeNuJGXmcxIXCTkshy1RprHVvFD5J0m8Sjtw6IYQPLitjzAyB4OXbu8KnKEN9UCy2ok8H2O5fFlczYMzTxXTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYiGxKxeuH8giuR2sBPwQl_-ODryehO_bVq1HnFFrf5zA3vZsee1B2pV_WtLzOHH6DZOgFSrFQDqGLJonMoqDYEvlkxRskVo5lmErHDAjK8ZgsRXJe3eBIoYD_coLJ584ah5Bj0ZcJM95hg3cQvA9w4FWlkXmXsWb3JfP19Q56Sm-zyAUb4xLDZGtZA1Rwd6_4SUNaLLCM8cB81hQqvzh9nbcs4B0jdPfjx1TH0_kkBj9zNrsX42ixGJcxn8SF29bX4oHwr_PdI5Yj4ivJmJLY2QJw6wxReyd5Kf2os9xHMRYpHmbK8Y8lkqgUoBncBURLLKCmYtd2LuAdo1CFQRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSWR8pwup2w9baJFdEILpUSt6j0G9gYMhCIoRIq6nxAYTNwQQuwtuWgV5A9zoi4EibyMMV5tC0NoM_HoO1T3BTCE0-E2mrYrtXHh1cKShWUbAKIVI5JRumpmrH_jvFFHawLyouDIl_8QUt0_99rJxbTiJx4E89yG_zq2NKO0RQgs15RDyhIV6ncZLQyyebrVOGyW7jIoQkHT8EZZ7K2iV8XN2RKAYkF087G0jUlS3nA7c4t25_Yk0FZte8eVU-lXfXsOqBVdgZCGMcb0wcKC1R0u1_KsVrrkUbaF8BnIjj1Ck59GUGUulmKd60d9bcNzW3Pmn-lgykuciKKFE7csjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh77uiDscwS5cFtxaX2vW6VHB4BwhI3-BY_7Pcnv4MHZO8HO3YKOp8hj-RQblogz3TjPXUe4GO9LG36H2W_n1x_LUqULZmBwVkiJVuYEHDM6FCFw82xtjt5CSiRbZKHuLFxxcTLoznjdrMHRtgtaFtLPgPdp0R9_Tr9qkuPQJg2HWAih2EIhrnmA-RurdL6tVxz3M2R1LVGfNNDjujKanHIhKo5u5bcSTCpYowa5Om8K6DrgF24d9ZrW8c9_wbRMT_r8VRldq66MSzXj3aA8iZWMDaqkSZF5sqpXLRQz6m7fLJGWhjPy08QILLmJTzLBOJdIn4Ntktimx87AwltJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsXG0WlGe3znJbIqCF_brXEoPVyBT2lzLNyxUd8gsnPJZ-cICprOAoYb7OJLvlyRKQQwQWDoIS90bf2z3vyUdKFI9_12q8FbYpFL4SV5Sha-N_Nd2yIzio5Y0WTE-wxmdfe9Qod5bGTG5iHotjVEV67DhPTx6x5euwub1XvY8RPGaXqGkbC0gjR0Ug1dHqzjYicNc1JCo20aF3_73H72cBJt_E2d8SxiKbaEyWmiaqnUZY4N9e2qZf09GOU-MIsgZRvlJUttZLAuXX1ut0xGL6e3_EXAggbPlCphKEjor4KwFN_AFmag-Vk1S5JnvhBpoBfd8WOe1bXS3vVoROriXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrDuqbNKLXhqc_lrNr75EoRL8zoozDnj40LIESNF1I3yOIGihs8UG_GOWHcmna531c8Dc7HZdc8xScUrJ15MthMrIRntZiVaOVhzV1RSdv-JC3k9aWKE1w5X6Bz33IDy5eCjITCxS7WlsjGhqRmoHNcBfnBhOw42Oe_ME8ltCc01MkNu7239lW1_MCWfpPdUF4buJyqlPM3amg5aqGK3diov9bpgnTJargefKsJv0Z4w5qoYNIOikCWIixFlhT4ROakV4cUbE-BbDy6TjJ2Fl3WOwK3vW95TujRHMDMZnzNl2UAIfOdTKVxxei8_suOrUOLn6mXF4PqOevaKOiWp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=v3s4Id1rbelrwmG1Q31k43-B3OMgvRcZsVUgU7srl5xi8UhN3I8vcRdGJr3dGNkyH8ubKGZnB7czs4A_X-4QLd8p76hssnKy9J9_2wnMPZl2Ob3kxiyvN2nI586BT-5i8-FZwTBuUCIh8Fr8uJQptd_O8pkHZWfD-zQYSqGxvli6GsViyxgWJRa5HA60_oGdVbUs_rLty1xZRszVBQlKPkx3n9t7AE-EvWfI_E9nD7-T8VB6hKcmxZbM4rtNRMW4fWMyNTQuxddqxyLqk4rArF6WFetVQyF7FK5-RQtJOirZXOsUVNYlu5W-scDluPTMyfWrJTinyZoC_XPZ2TZQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=v3s4Id1rbelrwmG1Q31k43-B3OMgvRcZsVUgU7srl5xi8UhN3I8vcRdGJr3dGNkyH8ubKGZnB7czs4A_X-4QLd8p76hssnKy9J9_2wnMPZl2Ob3kxiyvN2nI586BT-5i8-FZwTBuUCIh8Fr8uJQptd_O8pkHZWfD-zQYSqGxvli6GsViyxgWJRa5HA60_oGdVbUs_rLty1xZRszVBQlKPkx3n9t7AE-EvWfI_E9nD7-T8VB6hKcmxZbM4rtNRMW4fWMyNTQuxddqxyLqk4rArF6WFetVQyF7FK5-RQtJOirZXOsUVNYlu5W-scDluPTMyfWrJTinyZoC_XPZ2TZQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=OaxpapX2nt0pKAgUgZSknNTD9SxwGS2ApTMlnNyP6WbGBg0_bppM_KsN3Z5plItBB7FZlozNlMPReeK3l_k4ipDBaZcnyAHUYwfuHbSxYiwAm0Pe661kYVItmrsplrtBIxco6YVAmlRgchsTG4dvpJ4-MD1nMXkkS6q9ujj6cIbOu8AYEubQKgTYD6kHbIkQU8jPf80R7leL0Ou0gAFAbRi5g0H6GMsWorP7H2Fd3kA4H3Hz1LSqt1FdVfPLQIVtopgHsfsf6Q4sa5U0RLcEOC6__kQl8qkJCICaOFo01zhDbbughvOPt5V2Yd81zSEk9h67D3Zj_AS8AWOglNHRzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=OaxpapX2nt0pKAgUgZSknNTD9SxwGS2ApTMlnNyP6WbGBg0_bppM_KsN3Z5plItBB7FZlozNlMPReeK3l_k4ipDBaZcnyAHUYwfuHbSxYiwAm0Pe661kYVItmrsplrtBIxco6YVAmlRgchsTG4dvpJ4-MD1nMXkkS6q9ujj6cIbOu8AYEubQKgTYD6kHbIkQU8jPf80R7leL0Ou0gAFAbRi5g0H6GMsWorP7H2Fd3kA4H3Hz1LSqt1FdVfPLQIVtopgHsfsf6Q4sa5U0RLcEOC6__kQl8qkJCICaOFo01zhDbbughvOPt5V2Yd81zSEk9h67D3Zj_AS8AWOglNHRzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Km5m59qKE_yiLqz4sRGuvYIfGuLC1GiRfJBYF2kuWvQuNn-dhApkL3bH0cTzFMAUxsYhDgCOjHLFGtogqPonUobStF_axS3RP_AhosKLPVux3ytyBK9y-_lv951m9_DMOtSz4gUTicpZuSo2XAy8NeH5qEi9-dUxYqsv21HpJ4_zPHW88hM1C_wBnS7amodKzwvzsSR9f7vnaZLYkB-4aSJh2z8u3tH_A1WkwmSuNzjV0gkhTotHyzorcDsQnzIPJLBQ1SDqgHgsvRjTKrXmk_I1ErjnQtEpVG0KTWS0qFOmam3ZrjavuMmHkDNNDN-SpDSNrk_iHrjMLYrDQbP22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Km5m59qKE_yiLqz4sRGuvYIfGuLC1GiRfJBYF2kuWvQuNn-dhApkL3bH0cTzFMAUxsYhDgCOjHLFGtogqPonUobStF_axS3RP_AhosKLPVux3ytyBK9y-_lv951m9_DMOtSz4gUTicpZuSo2XAy8NeH5qEi9-dUxYqsv21HpJ4_zPHW88hM1C_wBnS7amodKzwvzsSR9f7vnaZLYkB-4aSJh2z8u3tH_A1WkwmSuNzjV0gkhTotHyzorcDsQnzIPJLBQ1SDqgHgsvRjTKrXmk_I1ErjnQtEpVG0KTWS0qFOmam3ZrjavuMmHkDNNDN-SpDSNrk_iHrjMLYrDQbP22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=uq_H-lirsj6z5cpLNd7hPwM-ZBAHqIxDnnHweBDaPhL0Tghxtgst6QqYPQ-WMaTl3p1ppLaMVfcFzzDGm77XVSJQjVK7u6sCJjn8kPiOG8IB44Q-3a985hCZzdT6Fw3Xx0NU7tVnK37SBX1esilLxGI18lhY6mMHP4zbWJKDJRXuXBpd-hZThw8_tRniKcmJz832jXvzQ9_VIzDS9pm6bT49l-JEPpelB5Fmlu2o0caimID8qsnQfRcdDboDAR1Ls-39owkw6Fw3hM6yc7QUti40VAUa7fItB290k6CahWxZKwZ5lc_u4n8WmSg2cgBUstXL8MTf-J4L-71TaZSO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=uq_H-lirsj6z5cpLNd7hPwM-ZBAHqIxDnnHweBDaPhL0Tghxtgst6QqYPQ-WMaTl3p1ppLaMVfcFzzDGm77XVSJQjVK7u6sCJjn8kPiOG8IB44Q-3a985hCZzdT6Fw3Xx0NU7tVnK37SBX1esilLxGI18lhY6mMHP4zbWJKDJRXuXBpd-hZThw8_tRniKcmJz832jXvzQ9_VIzDS9pm6bT49l-JEPpelB5Fmlu2o0caimID8qsnQfRcdDboDAR1Ls-39owkw6Fw3hM6yc7QUti40VAUa7fItB290k6CahWxZKwZ5lc_u4n8WmSg2cgBUstXL8MTf-J4L-71TaZSO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftuj7Ss8llM2-a_uLn2KbTI3zjZxxtKo9uak75OJ366KC3C1NKn4SwdOVpf2fTgriCP86bKnFsT_MMv3ZxYeldTEjnW39huBTznT5hIe6KGmRMVfqACZe6ZuSURdmsCbFWbks3gv7BZf_P365Qxr6oQQdWzCdX6xrtO2-mcacAl6xUPVm9tTwauMt5Hp9H4l02hFpsMdtYO6WRpRYALiDsQKjoc1pxeMe37KjanJx5U9dSAFq_TypRSNTFM5EtSKMIRL6wEhJufwx1aQSQEcLIb2P_KsfLqQWBz310lCr_7nS3yPCinq4OLb5D-1PbVbsS6cfrawChr2wcmI9GEfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=vmstx-Cab60FrjOKgvRPWuNpQKaHTPEHI93WKS0KDvSUb-0ZLz0RsVpY8Ri70xKq8kxc0doFbEDwPZ8BYGr_1ql_v5r4TuNfEFjcLh271Gro0QVQ8T1opAiTHd5XHr8f8pJ-84sAbZg0uAwTCGUoTPinaD12V8rOkf_NLYBtDX9KWe1X4wLqHCn5kuNtRfL88WUcIC65I-TARXwulpiQuY7Mp85Y_PcGMBr0YY6nhReyO18ueIcgo1Qj7kGyLoz3TTk8o329gk3qX5ekuHOp8RqNkUxgtLnBuyHO_UPYy1wfREZcPR8qkPJmvYHA3yGWtt9evgbknn-gBwqkd3GCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=vmstx-Cab60FrjOKgvRPWuNpQKaHTPEHI93WKS0KDvSUb-0ZLz0RsVpY8Ri70xKq8kxc0doFbEDwPZ8BYGr_1ql_v5r4TuNfEFjcLh271Gro0QVQ8T1opAiTHd5XHr8f8pJ-84sAbZg0uAwTCGUoTPinaD12V8rOkf_NLYBtDX9KWe1X4wLqHCn5kuNtRfL88WUcIC65I-TARXwulpiQuY7Mp85Y_PcGMBr0YY6nhReyO18ueIcgo1Qj7kGyLoz3TTk8o329gk3qX5ekuHOp8RqNkUxgtLnBuyHO_UPYy1wfREZcPR8qkPJmvYHA3yGWtt9evgbknn-gBwqkd3GCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZLrAZvkZ2gVG_dnMIqkOWqmYuE-G0lMNeG3GBsaigCGhspTnzxuTtI54l872-2Gq9kvkocrLZTFmxBgpQXkhWhKNmGV8V-ep_7wH7WtuTJG-QKsKREawx_Y88BGf524bVgORogcoZ-zv6_Pyi4pQhBaucSeH8I17rmjlGKE8BCuHJzJd1k6aDL1xOHqjMq1Ub4SSq5I8x9REwxGeS9GZ_Q39jHcuCdiSuhzdB0sOlrnuW9kIO0AkxonpU7AhX8rKlCLfjUigpfgBx38lZ-QjdKl42zRohwWyxKOvxfALXlGa10pMKilIMKdHbCrwb3Oqyi1IbH1nSIgMaoyB-34XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=R_CY673zIH8lQJ68EN3h66CRgZ5ILlFjQSR9cYLU9-nXw-dZLmKg43MX46boTyVEtM6SnisawreIp_7T1xZ3e3YVhxLJOzUizQYbP5TTTvcHRJIlpeb7-hITczcQ8eOfgLFNPyTN6DtyNsaPZsGwwUHBlerbU8qRKy79pDjG7eCVU4rK-xmJm7By9Ukscm4rkr-X0gbJlFzlCyyo-LW8HQpMZu2-YakociU1JjueG0qchYdoe1bCGSwU2JI7XuXKOUNsm1mBuqMGR-be4vRtEmoW04mNiqa3yqL2a6-RQ_9nQ52OYe4ob-Cld1MnYQjyKu3FhlsYW2V-KbEqBO7heA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=R_CY673zIH8lQJ68EN3h66CRgZ5ILlFjQSR9cYLU9-nXw-dZLmKg43MX46boTyVEtM6SnisawreIp_7T1xZ3e3YVhxLJOzUizQYbP5TTTvcHRJIlpeb7-hITczcQ8eOfgLFNPyTN6DtyNsaPZsGwwUHBlerbU8qRKy79pDjG7eCVU4rK-xmJm7By9Ukscm4rkr-X0gbJlFzlCyyo-LW8HQpMZu2-YakociU1JjueG0qchYdoe1bCGSwU2JI7XuXKOUNsm1mBuqMGR-be4vRtEmoW04mNiqa3yqL2a6-RQ_9nQ52OYe4ob-Cld1MnYQjyKu3FhlsYW2V-KbEqBO7heA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=kQUVxqgLkpJhiO6IGqDwFWmQIu_hH6J93IP5IZMKzZmWMUyZFcwgLWsrnSBbiaVRPv-8P8dorHcOqqtQlGkzn7XyKBxsd8LqRxdQ7RMevisLjfy0YJPIAmu4DPv5QVVY7628ffufvQYPmBwZisjX6P7JR6sm1up2fCIurljNR5X2JxQPPcjEtnjxdZwp6Xb_mVVY89tqS07TJRxKS-5SgLsFzSf3hJA9Xm5AJBsmejx5ItKr7-1lAlCVv5MYQGP9NobAmOGQw1FoyTAKHGfZto4eLRKZ0Nq3fFqjQH5uQ26Cp3qQRB63QyaXI8u3pWG7TURTFubtKiKMyK4bBIkM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=kQUVxqgLkpJhiO6IGqDwFWmQIu_hH6J93IP5IZMKzZmWMUyZFcwgLWsrnSBbiaVRPv-8P8dorHcOqqtQlGkzn7XyKBxsd8LqRxdQ7RMevisLjfy0YJPIAmu4DPv5QVVY7628ffufvQYPmBwZisjX6P7JR6sm1up2fCIurljNR5X2JxQPPcjEtnjxdZwp6Xb_mVVY89tqS07TJRxKS-5SgLsFzSf3hJA9Xm5AJBsmejx5ItKr7-1lAlCVv5MYQGP9NobAmOGQw1FoyTAKHGfZto4eLRKZ0Nq3fFqjQH5uQ26Cp3qQRB63QyaXI8u3pWG7TURTFubtKiKMyK4bBIkM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=NMm9Knb0v4rhMHp5t0SiQT2hl4EjKPa3wyHsoWPXB8Nw_L3DqwErXlV6dEmbEEBRQTMdJDt2XauxuSiO_wlf9f8c0xv4ZM1cJRRZnLaORBsqXD-FD5tt6ZxvFiPFcsMKhIBcZe6qXUVahTGjhmT1yeVKboUti1-869HmBqtM7pqfuWGZbTUuWIlXu4y4doAz1bbVHTTI9A-tfnJA7iU-WitsuPTplAc9uuMyjc5EZBIv-MKcQ-LdlafnTZHopL8Fnfs0cTekF43IKk_-u8VfHZe7oQPrKgHH_WZyspjppkw5oH2cWqVEE6xQxU3TpCBw73WuqoB6W6L4BOGzQtgeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=NMm9Knb0v4rhMHp5t0SiQT2hl4EjKPa3wyHsoWPXB8Nw_L3DqwErXlV6dEmbEEBRQTMdJDt2XauxuSiO_wlf9f8c0xv4ZM1cJRRZnLaORBsqXD-FD5tt6ZxvFiPFcsMKhIBcZe6qXUVahTGjhmT1yeVKboUti1-869HmBqtM7pqfuWGZbTUuWIlXu4y4doAz1bbVHTTI9A-tfnJA7iU-WitsuPTplAc9uuMyjc5EZBIv-MKcQ-LdlafnTZHopL8Fnfs0cTekF43IKk_-u8VfHZe7oQPrKgHH_WZyspjppkw5oH2cWqVEE6xQxU3TpCBw73WuqoB6W6L4BOGzQtgeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=YRHFIeUuXZev7fAQWTI_wPO5bQ6FaNGnREV6hft8b9lg-t4GbO-wmCPSpW-nh3xkI95dChqRb3UjyBJ736MdWLlrU6sckhF23G-e64SMCm7NOkO8IbXdSA4sMxzHJgwxBEJO_S9WXcJ-bDj3OJXisoogeLbIksbZlrhwii1ItH5l0MSsONooekHs13C4ATE9RDJGTyNw9yrBRfJ6_ku7LMb0UFmVwwb_ZnQA3T40KgPUvpjYFz17t5zJVCBgRR-ZicoLy1mofmZuXWMAF2bc2vBf1jqkXAr-oVrfIC9iej3XaZH7ZpP38_lMFomjd29-V3wpzlxtznWXj8krInMLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=YRHFIeUuXZev7fAQWTI_wPO5bQ6FaNGnREV6hft8b9lg-t4GbO-wmCPSpW-nh3xkI95dChqRb3UjyBJ736MdWLlrU6sckhF23G-e64SMCm7NOkO8IbXdSA4sMxzHJgwxBEJO_S9WXcJ-bDj3OJXisoogeLbIksbZlrhwii1ItH5l0MSsONooekHs13C4ATE9RDJGTyNw9yrBRfJ6_ku7LMb0UFmVwwb_ZnQA3T40KgPUvpjYFz17t5zJVCBgRR-ZicoLy1mofmZuXWMAF2bc2vBf1jqkXAr-oVrfIC9iej3XaZH7ZpP38_lMFomjd29-V3wpzlxtznWXj8krInMLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=rZUAtQLt2FpHmXfnwrBgOG51FH9geWty9YbIvCD6LfIEX-Dnn0VxYVC7fkrmtLvyM9rgEhAQ1iX82ut052z7CJ783vuIS_QwWWnKSKU0kQCVaWIlZmEnMolu9l7-_wlgXoHi-Vz02A2wpVApIx9MuM8URh7uq3RJFy9hyA4KIKYUAsOR2VQnwA0jbzOVJHj4V-YsEN8yQnB8VUPGmuYrdgmNmv7HalrdDKR1R6wkm0M2pMGJ1_pd-Xo_rJkXcXoR5y70t6HrueFuKWrgpNHGWeAAa8SH-3s6tLWBDs2neNeqJxKLWLY1np1rcB7i6FMjasfgUibWYrb8EXufWu2Dbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=rZUAtQLt2FpHmXfnwrBgOG51FH9geWty9YbIvCD6LfIEX-Dnn0VxYVC7fkrmtLvyM9rgEhAQ1iX82ut052z7CJ783vuIS_QwWWnKSKU0kQCVaWIlZmEnMolu9l7-_wlgXoHi-Vz02A2wpVApIx9MuM8URh7uq3RJFy9hyA4KIKYUAsOR2VQnwA0jbzOVJHj4V-YsEN8yQnB8VUPGmuYrdgmNmv7HalrdDKR1R6wkm0M2pMGJ1_pd-Xo_rJkXcXoR5y70t6HrueFuKWrgpNHGWeAAa8SH-3s6tLWBDs2neNeqJxKLWLY1np1rcB7i6FMjasfgUibWYrb8EXufWu2Dbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=IWsGk9jtosJd17lUijJC7OVM9vznpUDPv4bCU4oHDNxBX2HdQG1X-Y2fIotNqsd6_z_954dK0CV-aacznSXKKjIe0j0Z2s9m7GoByJQ_5V8tl2leoc5X1h-rQQYalTWDJICOC2romnYzzNW0TokTVJt6mMvq5_iWm9FNJEJuqLc4g8SonIAR6xiVszJ2lceYqzZQ7ark1uQrY3SOa6dodyh4sXDc2lyvvueZ6jtBBqN8cwWaI1entkt8lBKKasR2RwECw3W2J8WAxR3fluLF9u8ISA6joxAPaayrgc7klTDmVMaTYbeMT_TzU00_xbIPFLnnMGT4U4u4jIvwSRsCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=IWsGk9jtosJd17lUijJC7OVM9vznpUDPv4bCU4oHDNxBX2HdQG1X-Y2fIotNqsd6_z_954dK0CV-aacznSXKKjIe0j0Z2s9m7GoByJQ_5V8tl2leoc5X1h-rQQYalTWDJICOC2romnYzzNW0TokTVJt6mMvq5_iWm9FNJEJuqLc4g8SonIAR6xiVszJ2lceYqzZQ7ark1uQrY3SOa6dodyh4sXDc2lyvvueZ6jtBBqN8cwWaI1entkt8lBKKasR2RwECw3W2J8WAxR3fluLF9u8ISA6joxAPaayrgc7klTDmVMaTYbeMT_TzU00_xbIPFLnnMGT4U4u4jIvwSRsCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC816z1daWmtP5nyMBZa6wnmh6fdSydft3OGHyl7Mrt7nZWoOrbrsCA5s_xHbc95LKibJK8OVyVkuP7cS3Qoz-p7iXQgRkIHK9sHK5ctKRd86D7nQGcgWGh1_7YPAdLkiawe2NpNMnnQS1i9EhYgG01ZK2I7FhmYNbT9jT14QC9ZOzxIh6xRPH9s3FDkQvtuLf_FD9p4UaQzIhC68DdCWcWDsyPhhJoF0SMuvFncRY75d7Qllilr3mZmtwW96apHylHRdIfO3K-8C7dHdzYQHSEF8rmkLpSLt8_tFV44rEJ5UbBBJgmy9nOra6QazkYwwNBEsvT7BOou_rYHUJh_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enTe5VPLP4Raq0WxYXJkOBpC7N0SGClKzZSMFtu2n79IbsUKkVcLv0uRvSqmxVPilqc3mxxaai5cdTytPDLB_mGi8KRAPCbior9yCA0tdrpxy4rufgJ4s5WjyYlsFE-OW2aqI4UUd1z0I4fqyaujWonPOKXb9VlO6aLMP92c3NrQwBNgueXTbDh_F-41V1s5DbB2utKDczhNyMQVTeTkCXuTF_LjhQp9Ilnm_MIOgfPDaniCZQ63Tfgd4DRsJdmJGUN6MT9CXA3bYPyIxXpUg6UDN1lMQW5rtF0HHCtzjN7qilUqg8kRoYbUFTAwZ4Sdgdxh5brQvg6N11sNhAixmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=tb5d3Qn97dTy6inh67M_icgKvBv-nLgNWSKkTUwxQrtvVRM2tahWCZziQx9wStYPJ44sV7G3Zac-9UGm0pFlEh6X9-YJ1XUFIMMS8JIC5Js-T6fUHP5RRlEkON5PGgn9VDZPsAHNwx7pGIaNeAMJ8fYwWqt9SELbvAhjT1NlKyV0c-qLUAlubHdG9RNcKWkPNQQCQzEt3F7TV2xzaKX4v6myI0vdasnOWHAj-XxrvsSckvyJaNUCN9rESeHZwmu9NCRS0kwlNctuhds-T-NLIva_LSPI0qXD0JIycXPPt5Q3LhpySml4Ele3HJNfdPsW799MaXvUtLgd1KKLI6sa4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=tb5d3Qn97dTy6inh67M_icgKvBv-nLgNWSKkTUwxQrtvVRM2tahWCZziQx9wStYPJ44sV7G3Zac-9UGm0pFlEh6X9-YJ1XUFIMMS8JIC5Js-T6fUHP5RRlEkON5PGgn9VDZPsAHNwx7pGIaNeAMJ8fYwWqt9SELbvAhjT1NlKyV0c-qLUAlubHdG9RNcKWkPNQQCQzEt3F7TV2xzaKX4v6myI0vdasnOWHAj-XxrvsSckvyJaNUCN9rESeHZwmu9NCRS0kwlNctuhds-T-NLIva_LSPI0qXD0JIycXPPt5Q3LhpySml4Ele3HJNfdPsW799MaXvUtLgd1KKLI6sa4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=ogwmIUI50WfcIQLZYuqRyqUDT4MFPa2xF7wn8atiC6iFfRHgN4mCyxJDd69AvhaQ98ECGtG-YyCEDsb5uqbkR3YpJrhGwz5JQ29tMdxCPB6B8gTOml6ut-5IbvWWmKl1ur1lDNh_PJ5_o1ITndUi3Fs-HkQTGgnrxv0Jdd0RkpS7lZw_JaWRWMlWPJjeV3QrfHlbmi4ldJ2TGXdm1sJyttg_eM0Tosj2Aa0be-BWQFloA0zgUlpbCCYTfvikgJPipEiwFwxrFPXgJQX0ARgPW-xerz8w1OOeptzRUeTC_sjxYUnMfENhuwcX34U7bbzBHZzcB0Ofa0AKqu8yPaVWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=ogwmIUI50WfcIQLZYuqRyqUDT4MFPa2xF7wn8atiC6iFfRHgN4mCyxJDd69AvhaQ98ECGtG-YyCEDsb5uqbkR3YpJrhGwz5JQ29tMdxCPB6B8gTOml6ut-5IbvWWmKl1ur1lDNh_PJ5_o1ITndUi3Fs-HkQTGgnrxv0Jdd0RkpS7lZw_JaWRWMlWPJjeV3QrfHlbmi4ldJ2TGXdm1sJyttg_eM0Tosj2Aa0be-BWQFloA0zgUlpbCCYTfvikgJPipEiwFwxrFPXgJQX0ARgPW-xerz8w1OOeptzRUeTC_sjxYUnMfENhuwcX34U7bbzBHZzcB0Ofa0AKqu8yPaVWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=ke-2-oxfCNo1kl9phAXIk90wC0qfmoXLxMpuHu2D0svXXaLblpfgOSSeExBVWQwFDzz-jZ2490Tze0Y0PXhRxWRCqqNu4lMKTn1dvrE1DeVidm4s_-cQ9_IzD-HNaoxbUWN37Gk3GNXXOSxMZvQKUNm24Wr6Nr8EIFkfE7WG7tqvWfJIcIaa_UcXRdpGO09_ELqO6ILCIM5jadwqMTnkUKQmpkrfahTPkFMfTYco7eW3iV3TWYRAP778m4b3wlU-VVSJHaQFkJdgjXWY0GVMvq_6PKR4Hbk-5dHRyhz3HBB--Fi6nmeLRHTp8HavuPG7jClCSRR1-4o02hoXxx1V1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=ke-2-oxfCNo1kl9phAXIk90wC0qfmoXLxMpuHu2D0svXXaLblpfgOSSeExBVWQwFDzz-jZ2490Tze0Y0PXhRxWRCqqNu4lMKTn1dvrE1DeVidm4s_-cQ9_IzD-HNaoxbUWN37Gk3GNXXOSxMZvQKUNm24Wr6Nr8EIFkfE7WG7tqvWfJIcIaa_UcXRdpGO09_ELqO6ILCIM5jadwqMTnkUKQmpkrfahTPkFMfTYco7eW3iV3TWYRAP778m4b3wlU-VVSJHaQFkJdgjXWY0GVMvq_6PKR4Hbk-5dHRyhz3HBB--Fi6nmeLRHTp8HavuPG7jClCSRR1-4o02hoXxx1V1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Ensgi8uaeIxp1sRxDzXk3FUH3GB8aJunSaT1eueQRAYMtBHiDE3eoFc723Zs1XOqzELx4Njdadr1cqpf88M62iVG_BrBphmQR9BDjPqYxJlgRQ4jToScMmP9GQKWEV-i4aomu9xmzTJ8c3V-F2hWyk_UgufMugUa5w_FM7cCnrWf2Sfn3G07tKJJ3qbsPUvdwrpA_U7v7V4Qi4_Tsx_F234lCB3GYXnuguR9r1dib-y3aL3xF-oZGoEyL9ZDBDZxoIEElcWhG_Ep1BK0-_pH6h5ZdDXqoeFOk8gIbIBAbTV9SQvL2N-KxZj2DWzeRoGQJZLgr2115jfbIHPyKVC5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Ensgi8uaeIxp1sRxDzXk3FUH3GB8aJunSaT1eueQRAYMtBHiDE3eoFc723Zs1XOqzELx4Njdadr1cqpf88M62iVG_BrBphmQR9BDjPqYxJlgRQ4jToScMmP9GQKWEV-i4aomu9xmzTJ8c3V-F2hWyk_UgufMugUa5w_FM7cCnrWf2Sfn3G07tKJJ3qbsPUvdwrpA_U7v7V4Qi4_Tsx_F234lCB3GYXnuguR9r1dib-y3aL3xF-oZGoEyL9ZDBDZxoIEElcWhG_Ep1BK0-_pH6h5ZdDXqoeFOk8gIbIBAbTV9SQvL2N-KxZj2DWzeRoGQJZLgr2115jfbIHPyKVC5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=EGgf1N8bZVME30y9vHkMG4DiAK4Lt87Mp1PHwGbwejM1r41AgW2Fcq1zUQtQ4Cs_eHoyKISa1mN_0xr0wq9YSl95SQgH9YrO5gZ_6T5BerE_dZxjEpGDaj-zmo1TZ3Z7lS2kNlPEiDyaz9mMQ9RiE3dnvi8T5723K8DZMUc1_WUvNwoHKeKmSdaZZcABg60LzYQvXPO4pWtPDbYnJpEWSHXw8ZOrQj0z69kIAUYF6prqynbwyKeJHOZKBYGjYsUkofCoKnBxvTrFyo_N3fbnLywKKT2jh_MGC-CeyMhAHgoNIFgArg8p5kg-x5OezFI5dKOt9PqyQo1nhpZ3zeLQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=EGgf1N8bZVME30y9vHkMG4DiAK4Lt87Mp1PHwGbwejM1r41AgW2Fcq1zUQtQ4Cs_eHoyKISa1mN_0xr0wq9YSl95SQgH9YrO5gZ_6T5BerE_dZxjEpGDaj-zmo1TZ3Z7lS2kNlPEiDyaz9mMQ9RiE3dnvi8T5723K8DZMUc1_WUvNwoHKeKmSdaZZcABg60LzYQvXPO4pWtPDbYnJpEWSHXw8ZOrQj0z69kIAUYF6prqynbwyKeJHOZKBYGjYsUkofCoKnBxvTrFyo_N3fbnLywKKT2jh_MGC-CeyMhAHgoNIFgArg8p5kg-x5OezFI5dKOt9PqyQo1nhpZ3zeLQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=kzWgsjhXBPbb2xZ7KYb4BMtFvaYgrFzZmiFhjMP0fnvIxZV87_z1LESzvwPoTmUwjpHtF5WByEcreOsdIA6kBQVLpXOHb1lFZFEtyrw0fNBLjCFcfx_vkN63LSyoynrOzb2zkRKWBRktWoRijJR97D6pXuTQsovKPvEvmN3noq1TSPMwWQX_7jcc6gSt7OIn5t78rBmtbEBVl0ik7WHSyC2F8mtOsTTjcBk0vKr3sOgpOC6YJ-T4c_VwOWen2lMRmZ1Wr_3F2AcA-NHkbtWQLtGj82neVfQL5R7F5Kipcffm9yvHt2vf5IcT_DGrxKK1mAy0qzzE14VyePbQOEVMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=kzWgsjhXBPbb2xZ7KYb4BMtFvaYgrFzZmiFhjMP0fnvIxZV87_z1LESzvwPoTmUwjpHtF5WByEcreOsdIA6kBQVLpXOHb1lFZFEtyrw0fNBLjCFcfx_vkN63LSyoynrOzb2zkRKWBRktWoRijJR97D6pXuTQsovKPvEvmN3noq1TSPMwWQX_7jcc6gSt7OIn5t78rBmtbEBVl0ik7WHSyC2F8mtOsTTjcBk0vKr3sOgpOC6YJ-T4c_VwOWen2lMRmZ1Wr_3F2AcA-NHkbtWQLtGj82neVfQL5R7F5Kipcffm9yvHt2vf5IcT_DGrxKK1mAy0qzzE14VyePbQOEVMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=efrOiZ3PtiPi1JIfz1X7kj8HC_a-Gk9_YgfAyQEl2LmmeQrghFQk4LviwNEhGB7W5ZYikFjgIIlyOxu70mCgZNxjou62aUSvSBzrrwSkMHrc0m-MpiK-MzrZ7yu8Hj2ejHQunhxRP9RCvQZBw14DF9i2c-zF8-WrIkislwE48DRV7pR-N3z04sN6Z9FjTHDc43R3W8cc4Gz1s50HJyCsir8oo0KjU_Mj6XS8QbO4ZiQF_S45KU3hgza3GU694ktiaWIX3GKWF5li_X0uE3VYWOp5Jr8H9Dnn-3wX6BIrnBeeQWpjrzpd8SH0tIe8g6DCry2wuu1BAjLWi5WuB5OSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=efrOiZ3PtiPi1JIfz1X7kj8HC_a-Gk9_YgfAyQEl2LmmeQrghFQk4LviwNEhGB7W5ZYikFjgIIlyOxu70mCgZNxjou62aUSvSBzrrwSkMHrc0m-MpiK-MzrZ7yu8Hj2ejHQunhxRP9RCvQZBw14DF9i2c-zF8-WrIkislwE48DRV7pR-N3z04sN6Z9FjTHDc43R3W8cc4Gz1s50HJyCsir8oo0KjU_Mj6XS8QbO4ZiQF_S45KU3hgza3GU694ktiaWIX3GKWF5li_X0uE3VYWOp5Jr8H9Dnn-3wX6BIrnBeeQWpjrzpd8SH0tIe8g6DCry2wuu1BAjLWi5WuB5OSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=BE543j1g_2taxn3bXPgcNn-jQt0LMW4yVnf2qY2BsuIDg5aNSutdpdROBJZULos82qcskiNdNMZMzpS8zXVCqtz-nNhX349P4-4J0xtSPaYCXFCVQkEDN8f5-XJVXt4sBeEf_tPnuiQZ9aI5KYVw6IVxv_gwQYxDPPKpfDidCxMUOe3XN9v1bx_0GhWOMPqwSaljd02ZYZyC4-w6ymSrSObB4DlrhrkgZ-PXXy9mODn1nlXkGNcVmaK_kVz-kASDBd4hIefLUgq5z_EhLwEmtoeK081oGJModbDSnaRIdDhwILBV6jcilFLFDRQ8KHNTVCyX6K5nBpo8KR0IFAeCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=BE543j1g_2taxn3bXPgcNn-jQt0LMW4yVnf2qY2BsuIDg5aNSutdpdROBJZULos82qcskiNdNMZMzpS8zXVCqtz-nNhX349P4-4J0xtSPaYCXFCVQkEDN8f5-XJVXt4sBeEf_tPnuiQZ9aI5KYVw6IVxv_gwQYxDPPKpfDidCxMUOe3XN9v1bx_0GhWOMPqwSaljd02ZYZyC4-w6ymSrSObB4DlrhrkgZ-PXXy9mODn1nlXkGNcVmaK_kVz-kASDBd4hIefLUgq5z_EhLwEmtoeK081oGJModbDSnaRIdDhwILBV6jcilFLFDRQ8KHNTVCyX6K5nBpo8KR0IFAeCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=DTD-MLNWO0woOe0_sCE2a_al2BaWcam1KETTPDBIH8ntdf1GMy0JRVaIrLaVQ_Q23moSzC_NimUb3FP0xl4FtbVYQHgVLbMnW5DFZEdQZ1jKcQsihX_qIH-UXmAvgbmngD8AufHcDjh8A-_O2HNYHxOmhnF7UVGbwPSmyMwWTBQMZKfrieFpQD7El15_ZV5EXgHoExPGhWRpO82rPK_nJbeNqCOxAeYh2KzrcS-WEEJnlsPv5Cb4LDz_YNHOIJKMyGEgB8IpdOnYZ47lxEYUVZ7O8XGSHD9FTAD4AZ5x-6dAcke_FhgYa15SG2CuOT4fWq6GFDsNafSi098mLaJJBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=DTD-MLNWO0woOe0_sCE2a_al2BaWcam1KETTPDBIH8ntdf1GMy0JRVaIrLaVQ_Q23moSzC_NimUb3FP0xl4FtbVYQHgVLbMnW5DFZEdQZ1jKcQsihX_qIH-UXmAvgbmngD8AufHcDjh8A-_O2HNYHxOmhnF7UVGbwPSmyMwWTBQMZKfrieFpQD7El15_ZV5EXgHoExPGhWRpO82rPK_nJbeNqCOxAeYh2KzrcS-WEEJnlsPv5Cb4LDz_YNHOIJKMyGEgB8IpdOnYZ47lxEYUVZ7O8XGSHD9FTAD4AZ5x-6dAcke_FhgYa15SG2CuOT4fWq6GFDsNafSi098mLaJJBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=BQ_RGT9Du78fTwmXrPMx6GVeVUkPO22UvVaERl8qZCFaINHblNCylxD5Q-xOGZg_IlZN2OXKTHo5jgNjQvJepETNnZDvTyhytOA6d5C4GJoRx1I3Nse04vJhae5cGDi_cd_qWcfDpy5TaTCV7VkyLw26KXHy8OoOB9dlCKCEHmE_yYVWp0QBIHC2hU8rLFQw2gAtDZtDtpOULHnhcLM12L7tcdmmr8umDVM74MOqPqlE2N91ACLJNaPezsx2c2JRNZ6oxQ0isiG6tlc_Sr5HGcF8hoGr9s7QRv6_7RZGNKZP8SuVJCrJnKKjLGnwLOHeSVv25DgUejXgn3sci8k5zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=BQ_RGT9Du78fTwmXrPMx6GVeVUkPO22UvVaERl8qZCFaINHblNCylxD5Q-xOGZg_IlZN2OXKTHo5jgNjQvJepETNnZDvTyhytOA6d5C4GJoRx1I3Nse04vJhae5cGDi_cd_qWcfDpy5TaTCV7VkyLw26KXHy8OoOB9dlCKCEHmE_yYVWp0QBIHC2hU8rLFQw2gAtDZtDtpOULHnhcLM12L7tcdmmr8umDVM74MOqPqlE2N91ACLJNaPezsx2c2JRNZ6oxQ0isiG6tlc_Sr5HGcF8hoGr9s7QRv6_7RZGNKZP8SuVJCrJnKKjLGnwLOHeSVv25DgUejXgn3sci8k5zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnNMzo55puXpGaOjTBcCbpYFRmiZmMiGRfNBa36zyAMPZ-HUrreD7ySueScLLl8l7JikftKQZag_MFnmLBqgm5AVNfbndPws3oNnos1nf4okJNnYySiEvh5YtUnt4875rSHybD7OxSt4Cm-eDjV3BukDZhcamojnQ-sMIDPRyTyZkyoanKStSzXIev24A32ZYtil0hqBoz1JxYkXq0EFoTSGSDqY78Fr9qIYeNg9a5ERr7XSxvSeVzAh-JzSuAUUbqfuUykluRU0FJbMeP7mMpgaRG7kgoFV-KdZ2wq7eEojjG3AKPC6NVzfB6BBd7rwKV1LDE_rlo-hXHYpsGEKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDnHMWMnuM_FqwIfJADDBaQfWAIqZfiReXlIS_XNLeEtahVaFO6Zx0AD-X1qZWWFQ9mDebO3i4OnZoI-YB_mS3cPQgPJLSVp7q2Ge3RIS2Qac2-8qL8mjm4_Z5C8xNvpcGmuyodFO82zhYcm3KpeS4rIdh-wBY3BtLGuvqV1h2NRkLpmCwkMXNw_CMa1KFarUkuVwyJv3-V8N_2hI2sIJe0u7_FBWmcRpYKtxyd26QYFD2A5FmedJdYxYVhMbttjsyyhFReuw2ZLRMfTxX6UDotpnd-oA37ycmGTfMsxgQP0CON3r5MpuvrOOX3pSTwcEN8_2J9RDrTOmrTRga3bqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=YoC1ZEoqMuigx2RNfwkZ7EHuuyNsjNNkZ9lvIuETMH0WdfPHP7cW_OJciQ9wBpsjiNeZNfw5U7rrNNe3gvKe5ZklvjrvxHyJe2HQfVBUtxD-U-yFx1DPKckSgpm0i75wt6klPY8rxlGYfO0U_CzonTYXpr9OTGB4IfEW1mH6jxHUs-88BsOkcEqMHMLADbhMh7CvUa-DeXRKl9nbFYLLNlT1gFIHEpQPlEMWF-bxaAcOaFKVeU0IcNKnjme_4JJpTdtoLMHKYd3sMIuMHuYRYYqgXHJgJy51NhJi528kaZwqUpJulAjHmGijQuF2OWZpVdxEE2Td3n_YAJfywAQUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=YoC1ZEoqMuigx2RNfwkZ7EHuuyNsjNNkZ9lvIuETMH0WdfPHP7cW_OJciQ9wBpsjiNeZNfw5U7rrNNe3gvKe5ZklvjrvxHyJe2HQfVBUtxD-U-yFx1DPKckSgpm0i75wt6klPY8rxlGYfO0U_CzonTYXpr9OTGB4IfEW1mH6jxHUs-88BsOkcEqMHMLADbhMh7CvUa-DeXRKl9nbFYLLNlT1gFIHEpQPlEMWF-bxaAcOaFKVeU0IcNKnjme_4JJpTdtoLMHKYd3sMIuMHuYRYYqgXHJgJy51NhJi528kaZwqUpJulAjHmGijQuF2OWZpVdxEE2Td3n_YAJfywAQUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=nr6WG5dgZfWjLitsMiZCOtGJCwYb1Z-i75doiUP7V5KDW98DNMOwABqCAhnfvygzmUxwzRU-QV6Wlb3n7947nVn-lEZx0RB5Coc4xEiMX9TSSwoYk920NDWlGUygqWfhkhJQUg09vFtDZK90C08Qr3eaUlBRI7ZZde3LjFbWj06qLkIaBmYQ5gxKkJSIjrl7iGRlQcnA23OUzsXBkg-XDC31T6M8MYtqAojNl_iX8taNDM-JIO3cau92ahg_BBxr6c7oSO-N9X-GIpm1UAfNGQ_I5an1XM3UuhTQT6exS2RV9xMLubhwQbTsVftATZLCbsTMiD1T5BwSbsJiMHonig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=nr6WG5dgZfWjLitsMiZCOtGJCwYb1Z-i75doiUP7V5KDW98DNMOwABqCAhnfvygzmUxwzRU-QV6Wlb3n7947nVn-lEZx0RB5Coc4xEiMX9TSSwoYk920NDWlGUygqWfhkhJQUg09vFtDZK90C08Qr3eaUlBRI7ZZde3LjFbWj06qLkIaBmYQ5gxKkJSIjrl7iGRlQcnA23OUzsXBkg-XDC31T6M8MYtqAojNl_iX8taNDM-JIO3cau92ahg_BBxr6c7oSO-N9X-GIpm1UAfNGQ_I5an1XM3UuhTQT6exS2RV9xMLubhwQbTsVftATZLCbsTMiD1T5BwSbsJiMHonig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=Vf-QfMBhsWwerEP2bvpHejNIgfft_KE688IEADpAzTW6ARDcfmkmhaFHmGAcder8VQEP5ghK7q7gQGjolt5J8duMSz_FimTq9446AQOw5yGZ1dHkWITtZgqAdRhLYCNjET8ngqzPItnqNrbRflcHBeIyl3jJAKdCtbZ00R4dd7e5RtovlczTay4riA8TNjolWUAq6yAbCSYEDJBFvfH8ipRBsvgbgRyv4fTlvsiXb66Hj6MOwPShjq-FCp-7u8bMUfxPxmbPtAMsF-YSd6EaW5NaDKC_ZHGXjBqKW69HcIpws8rieUVlq1RT0JIuC_OLL-6CNbgeJRxjHDD75s0CvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=Vf-QfMBhsWwerEP2bvpHejNIgfft_KE688IEADpAzTW6ARDcfmkmhaFHmGAcder8VQEP5ghK7q7gQGjolt5J8duMSz_FimTq9446AQOw5yGZ1dHkWITtZgqAdRhLYCNjET8ngqzPItnqNrbRflcHBeIyl3jJAKdCtbZ00R4dd7e5RtovlczTay4riA8TNjolWUAq6yAbCSYEDJBFvfH8ipRBsvgbgRyv4fTlvsiXb66Hj6MOwPShjq-FCp-7u8bMUfxPxmbPtAMsF-YSd6EaW5NaDKC_ZHGXjBqKW69HcIpws8rieUVlq1RT0JIuC_OLL-6CNbgeJRxjHDD75s0CvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=ENjFXTDKRrnTRAqY0QChIMWvb3bmKs32-ujbg3ku7UhAmU5CFv0tOMcfsUn0IZJcAPOjZAVdM3vlxxBMF6SIQtV_l4VrDEFQodFnNtjjCFz2Gfxmp55R4Zl4tOBCJLBRTxVT1cHwOpYX4LrcY8Z9DQcHxR38jAxyh0BZudsXlRTivN9JsCP3JDO1MChEihH1UcUocYn948jUI3FxvezRMOEcaBCf5mSONnaiOjM9CRb80knijwtjH2tO8Ip0puKg_dFega13Sntw7xufrf139gGAgage9n6GGO4BuSqIcjxDT-8fYNS0iahp4yEwSVRB6fGrONhhnDtSGYYn9QrF5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=ENjFXTDKRrnTRAqY0QChIMWvb3bmKs32-ujbg3ku7UhAmU5CFv0tOMcfsUn0IZJcAPOjZAVdM3vlxxBMF6SIQtV_l4VrDEFQodFnNtjjCFz2Gfxmp55R4Zl4tOBCJLBRTxVT1cHwOpYX4LrcY8Z9DQcHxR38jAxyh0BZudsXlRTivN9JsCP3JDO1MChEihH1UcUocYn948jUI3FxvezRMOEcaBCf5mSONnaiOjM9CRb80knijwtjH2tO8Ip0puKg_dFega13Sntw7xufrf139gGAgage9n6GGO4BuSqIcjxDT-8fYNS0iahp4yEwSVRB6fGrONhhnDtSGYYn9QrF5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=owof1k58E-haXYvtQECoORQruYCzEajHkGetW_YIwKiaYRy1X-Xh9NGAVdM1sw8OFb5tqU-ZJVQupQU3EO-tlDYVZFzKMtw_0DT_k4KoTkgqloR18YFzVAxjLyn8BCPd_kz3zCidAwMMvKFHkXTqxZpysAAOKs6aZm4yY8vnHdaTsmIyjxoGrEBJvzh4cHLDsco5YJFYIKxBr5sWkhXR65ySjw3TZ7h4GLkdOvnydBYEztR1kq_udB9K3BCvKrwd5EhxVNmG4wqQUMGv5hzyVlwXoOqNWIm-w3E6rTjQDGQoiHFX41OauB2hr4DaQlIIWQvE1k7E8Ph3e5opAToGJkAmHBZpxoYfWaFfYWseLwPUUJAyr-MpZCqeAx_5Wz6_m0wGqO3uEZGiuFGzMRgK67VZ5E9Rn2_6QbBl-fJaEtq6c2IkQavw1cY1hFe-H1mwlZKlrFZqJ45Ws5j2z1Iw_x73naqMD8FusKLdxckREzReY9s71k_sH0JUHw1Vqy28V63t_jpLHVqvbY4kP_vL5M5udzfscLOs4YD4rNuP68V1gm7CRyGL3FbvXUh4HjV22wmWuW7FOy9y1V5QndpXtypxxyEcmxI82fUh5Ues3HbYNPp-HZQfpjoootfIe17_ctPU-e4EXzqo7V4JPucWQB0VhF0yCxOefMOfAUNI8H0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=owof1k58E-haXYvtQECoORQruYCzEajHkGetW_YIwKiaYRy1X-Xh9NGAVdM1sw8OFb5tqU-ZJVQupQU3EO-tlDYVZFzKMtw_0DT_k4KoTkgqloR18YFzVAxjLyn8BCPd_kz3zCidAwMMvKFHkXTqxZpysAAOKs6aZm4yY8vnHdaTsmIyjxoGrEBJvzh4cHLDsco5YJFYIKxBr5sWkhXR65ySjw3TZ7h4GLkdOvnydBYEztR1kq_udB9K3BCvKrwd5EhxVNmG4wqQUMGv5hzyVlwXoOqNWIm-w3E6rTjQDGQoiHFX41OauB2hr4DaQlIIWQvE1k7E8Ph3e5opAToGJkAmHBZpxoYfWaFfYWseLwPUUJAyr-MpZCqeAx_5Wz6_m0wGqO3uEZGiuFGzMRgK67VZ5E9Rn2_6QbBl-fJaEtq6c2IkQavw1cY1hFe-H1mwlZKlrFZqJ45Ws5j2z1Iw_x73naqMD8FusKLdxckREzReY9s71k_sH0JUHw1Vqy28V63t_jpLHVqvbY4kP_vL5M5udzfscLOs4YD4rNuP68V1gm7CRyGL3FbvXUh4HjV22wmWuW7FOy9y1V5QndpXtypxxyEcmxI82fUh5Ues3HbYNPp-HZQfpjoootfIe17_ctPU-e4EXzqo7V4JPucWQB0VhF0yCxOefMOfAUNI8H0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=nAFyMQW7f8Zxfl6d-m78bIGrTjsfJcFGUolqcxbCoKKmnxsQGYsJt5zBZFpYwjZgCJ31DfkXcqsuBofV8drIQcjQkMVrnZBsNBOpfa4erwy_O1nQyBGMGGEM1PNTX1yM9S-N-h4vmv3hT7YOTvC35J35cXxIDyR06OvrX1R1zaK28n2VsVDOOPejtmpqg0TiAG0few4BDcAMew1WSb8DV0z_oMJbKgqV7XR-zMsVqnXojAo1Yt0fa6zrGUDnfipaBDp-UBH7-5YKsbEQI27mHRm6nEHFJD9Q7mWWBeU1xwDXuwBnvaa4igumYsTNeDZBT4bYn9GOMprQBUanEMGUOWaSUVh6k0xZn_Mfk4fE3ZADalSSmiRO73tATi6-s8gnKTyScP-_RKNv6FrusehVRkpXJE_LuKdFIK8lsYuY3KGyLO7tvZW0sw3XnD4Se9JfjWAAqBii7NwQAwBgfIJSv7tkGrzkaNgW6TFcWbY3uGI578uxjR703fBpa1u8fmzRzPMB_nkOQozKAJlyi34SeNWY7h3OFDZ0gXEm806fEyScpPFdmsPR9CVfwlKMFl9_AjrV6DtQxisMBG0f50CbDCFzJuIwLDFv8W1vUf1lPjYmKE4XfVPKx3uLMWYU37JwY-rXq87STXYtM2VQKnvu-uzwg5RjGH-n2q5AVTUftYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=nAFyMQW7f8Zxfl6d-m78bIGrTjsfJcFGUolqcxbCoKKmnxsQGYsJt5zBZFpYwjZgCJ31DfkXcqsuBofV8drIQcjQkMVrnZBsNBOpfa4erwy_O1nQyBGMGGEM1PNTX1yM9S-N-h4vmv3hT7YOTvC35J35cXxIDyR06OvrX1R1zaK28n2VsVDOOPejtmpqg0TiAG0few4BDcAMew1WSb8DV0z_oMJbKgqV7XR-zMsVqnXojAo1Yt0fa6zrGUDnfipaBDp-UBH7-5YKsbEQI27mHRm6nEHFJD9Q7mWWBeU1xwDXuwBnvaa4igumYsTNeDZBT4bYn9GOMprQBUanEMGUOWaSUVh6k0xZn_Mfk4fE3ZADalSSmiRO73tATi6-s8gnKTyScP-_RKNv6FrusehVRkpXJE_LuKdFIK8lsYuY3KGyLO7tvZW0sw3XnD4Se9JfjWAAqBii7NwQAwBgfIJSv7tkGrzkaNgW6TFcWbY3uGI578uxjR703fBpa1u8fmzRzPMB_nkOQozKAJlyi34SeNWY7h3OFDZ0gXEm806fEyScpPFdmsPR9CVfwlKMFl9_AjrV6DtQxisMBG0f50CbDCFzJuIwLDFv8W1vUf1lPjYmKE4XfVPKx3uLMWYU37JwY-rXq87STXYtM2VQKnvu-uzwg5RjGH-n2q5AVTUftYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=d7rNqncChgcutDeTMO7mSowApgLJd973Wzy5tGVRJUlFQCDHcY3nbBNNE2mFFP3dIMAH8I4pL6SvhDjvmm9gvkyhwW-L6B1UvmU3oHCMUpKpizJBGQhmvV1yr2Ck70qMDdnj4lliymGUHVfFGavwfybIBZCCNIZmnU6EmxmZ5hvIYYMIDdbfthXrTDztq4ynC6hSLpy1xuu3ytP7Zg2KVT3HrBXot47x-7rZQ4tcSBzh4j_ERP2ZNpBEKm76Bwg206ji6MewlPMh2D1RDsJ1FjmaHBSH2WTqDq4gKdHdg_1Cf7nSvamRo1u47dzll2h81omOIYcpvc3n8gKeDymhXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=d7rNqncChgcutDeTMO7mSowApgLJd973Wzy5tGVRJUlFQCDHcY3nbBNNE2mFFP3dIMAH8I4pL6SvhDjvmm9gvkyhwW-L6B1UvmU3oHCMUpKpizJBGQhmvV1yr2Ck70qMDdnj4lliymGUHVfFGavwfybIBZCCNIZmnU6EmxmZ5hvIYYMIDdbfthXrTDztq4ynC6hSLpy1xuu3ytP7Zg2KVT3HrBXot47x-7rZQ4tcSBzh4j_ERP2ZNpBEKm76Bwg206ji6MewlPMh2D1RDsJ1FjmaHBSH2WTqDq4gKdHdg_1Cf7nSvamRo1u47dzll2h81omOIYcpvc3n8gKeDymhXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=AXdlHSMGsbEd9O0wqdK6BBGp8hzZ7JoPu5CvueahvGAZX9JFYaDjisL2ZAY0tq4rwIuBAo2K9iZiJmJwav8TwU87RqefuVtWI1OCiw30Q-lzd9a1cSuzHxCMlBH9yGFGnx93pYkadWyzJFb5N26FRyGpRj5-2z6Gri2jRL7mrDpLXBWIhQbIULIQYneeXCOjUJ8XlZE5hqt-zFPr3nUQZScJCn0Pyfit-d7HEOW5vsEDLzrOjo0d4icbRyp6YHPJzWw6MqRAZ9UT71cZvZAD4BTudLUrrT3B0Uq-_2pELkglsEKeInXx50BERqDhMzLXnzdSWWmwmJl6q9W4JHXGOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=AXdlHSMGsbEd9O0wqdK6BBGp8hzZ7JoPu5CvueahvGAZX9JFYaDjisL2ZAY0tq4rwIuBAo2K9iZiJmJwav8TwU87RqefuVtWI1OCiw30Q-lzd9a1cSuzHxCMlBH9yGFGnx93pYkadWyzJFb5N26FRyGpRj5-2z6Gri2jRL7mrDpLXBWIhQbIULIQYneeXCOjUJ8XlZE5hqt-zFPr3nUQZScJCn0Pyfit-d7HEOW5vsEDLzrOjo0d4icbRyp6YHPJzWw6MqRAZ9UT71cZvZAD4BTudLUrrT3B0Uq-_2pELkglsEKeInXx50BERqDhMzLXnzdSWWmwmJl6q9W4JHXGOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=RJrtqQxw1pkJvke4R_Ckls-WqJYAUnhDgCsRm1oJ0sAbdBMBx_l1KIcE9GY3LAKf6-UowpYP4sByh9oBvOrE75g-CC6_Te8LpP7d7RthQgbFQOEoiT3qxqBPylX4l2S-HfIY2y2O6uW-_26WlM5wf4vfdU63546AZS9RUHU2PyFzAHqATUUy8JoIYArOlGZMtjjchnJNepDhL-m4_CbmHCA_w0BVcJpPjr26iC_98Zi5LrifMKis2-ZHiatxDos6r9DLQrw3OEpp9SxwORFBhHvIALAHwVZX_8ARtFk-CaiGpXgVREKRS5KcdBY9hH8u3Uth6MSFI0Q8yIB_Q6ChZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=RJrtqQxw1pkJvke4R_Ckls-WqJYAUnhDgCsRm1oJ0sAbdBMBx_l1KIcE9GY3LAKf6-UowpYP4sByh9oBvOrE75g-CC6_Te8LpP7d7RthQgbFQOEoiT3qxqBPylX4l2S-HfIY2y2O6uW-_26WlM5wf4vfdU63546AZS9RUHU2PyFzAHqATUUy8JoIYArOlGZMtjjchnJNepDhL-m4_CbmHCA_w0BVcJpPjr26iC_98Zi5LrifMKis2-ZHiatxDos6r9DLQrw3OEpp9SxwORFBhHvIALAHwVZX_8ARtFk-CaiGpXgVREKRS5KcdBY9hH8u3Uth6MSFI0Q8yIB_Q6ChZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=ftldZq3nSh5JlFFE5el22dNH0YWe5tQyPmlQv54RwpwQDYld5AVCeCa_zBOnnhZk-J7Ie3sGf8ZIZnszwxWtascuPSj_LqqttqJ2FnFXuABP83albUjkBCtcZMfhj0IOuDd-pzDu2ubTtSxiBUQt9-z6vXzb4apMlqolXHz73ItCybup2sdcTkRXwQB3aSGM6iPo5cpFJ0F6CEno3mjAKXdsYqv8tbSBsDrjh3CUn08X_7vvupDCkc7PwooHtNdVaros8U06geJPpmumQ0a9JpGMyMqQ4yfPTY1_NKT8PTpC-r4ZttPM1o77sdtUJc7zq0Aa3KgAZ9SCrgbBxuRvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=ftldZq3nSh5JlFFE5el22dNH0YWe5tQyPmlQv54RwpwQDYld5AVCeCa_zBOnnhZk-J7Ie3sGf8ZIZnszwxWtascuPSj_LqqttqJ2FnFXuABP83albUjkBCtcZMfhj0IOuDd-pzDu2ubTtSxiBUQt9-z6vXzb4apMlqolXHz73ItCybup2sdcTkRXwQB3aSGM6iPo5cpFJ0F6CEno3mjAKXdsYqv8tbSBsDrjh3CUn08X_7vvupDCkc7PwooHtNdVaros8U06geJPpmumQ0a9JpGMyMqQ4yfPTY1_NKT8PTpC-r4ZttPM1o77sdtUJc7zq0Aa3KgAZ9SCrgbBxuRvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=LK8t1Pg3TvwHlqST8NIhOL6f__eBZMsEcNSCAivPABEjmUeuqsY6sLTydE52SRuYnNa2PRBOS8gF-QGN5WR5Z-68_pddKU6rogtYqOJHOhYfXd_fdlLXr3tdMCBK0ge8aNi91uaEByjZplhWpOFP6dkZYobbviGBbJw9EJUjHz7dC2UhrrUIYsYwLb6A_CvHn8jCXEXvlwJdFikZEYVmBMOmzriVcYoC_cAlEXkMLaXDAHzVfdfOUOVllGhbKjJ_JE7a5CFB2JrvRkg-IWNLuW62YfcuMLOQGjyT3CzU6HiP-cGdf-fJNJTYoidLU6CpvTGji2E-U1AdBf__F7dY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=LK8t1Pg3TvwHlqST8NIhOL6f__eBZMsEcNSCAivPABEjmUeuqsY6sLTydE52SRuYnNa2PRBOS8gF-QGN5WR5Z-68_pddKU6rogtYqOJHOhYfXd_fdlLXr3tdMCBK0ge8aNi91uaEByjZplhWpOFP6dkZYobbviGBbJw9EJUjHz7dC2UhrrUIYsYwLb6A_CvHn8jCXEXvlwJdFikZEYVmBMOmzriVcYoC_cAlEXkMLaXDAHzVfdfOUOVllGhbKjJ_JE7a5CFB2JrvRkg-IWNLuW62YfcuMLOQGjyT3CzU6HiP-cGdf-fJNJTYoidLU6CpvTGji2E-U1AdBf__F7dY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=mgVYqXCF48qOO4AKjM75dnUf2m7h1WiBjbu168xKJdXkvQgLhfzQtnCTS5RnKtCDxKiOAYABk2KKg3ztm6C4CU5G7jAUIsOrFRNVSNiKZFawvp4hdadVnZycsRXSVcomc_c8KsushHCX_Nbix4O8Zz3x4YydynRAvB76DjdpyYcvlgcpaX3C8UyQVF5rdHNVscvPWlQgz1rf34PkPNN3anM_g755KFLC7yPtWolsDwSXDz84rYKZXS1S7rfHWxX2-bpKypSsZGP204KlXxF5Z8P6x96mkb19em3FmZBrmlgokNbWv1KGrIA3r62Icmmlk6A0DG1AQSGXgFHBAFQmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=mgVYqXCF48qOO4AKjM75dnUf2m7h1WiBjbu168xKJdXkvQgLhfzQtnCTS5RnKtCDxKiOAYABk2KKg3ztm6C4CU5G7jAUIsOrFRNVSNiKZFawvp4hdadVnZycsRXSVcomc_c8KsushHCX_Nbix4O8Zz3x4YydynRAvB76DjdpyYcvlgcpaX3C8UyQVF5rdHNVscvPWlQgz1rf34PkPNN3anM_g755KFLC7yPtWolsDwSXDz84rYKZXS1S7rfHWxX2-bpKypSsZGP204KlXxF5Z8P6x96mkb19em3FmZBrmlgokNbWv1KGrIA3r62Icmmlk6A0DG1AQSGXgFHBAFQmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqpFfWgEjJkFj7LQvRADA579saIsew-zs3mYH3EvCEt91mAHwofaeXNMi5XbEtmTcFyToieYBAN3YCr0HcrB0TaEANcUsvGt06KoyBWPQ_3NRMdU00U7yW6CNxSTckDdKuDNUqBXerm_fMMwRvsPLFMFa2k7b3alveEY26Q1LPIOkrZPMw2jE6kphr0ibsl6ejAlXcrOdR-IeRkTKjLZMh6UNY0IbsG_glcJXgkQdKyl-K0jucH6JEnvtzupKYR97hcKdukjeEmnlNQ9oFMd1CyQpklg2zpXyxEvuHVEAt8Tz6CnCILAK5opos06_4rmwXQI73dqjWSlaIFirDQoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA043Az3_APueKWa4QeVoJZHae8c6GA57korLbbfGSGZYlPAghFG9gR4-mwmDs0tzKk3duWt54zbDU80k1EPlsL9eyDoxQuULNN91i7VEua1WCH7fz4J7BsBRd-EiiYzuoQ4-vo0whRUi1s9giB9sFlEcx7G_j-L-PrGQcIvOWce83ll_O041uhs7uz3jK_qZqFe-Tw5TY0pw2vuoFcsON_e_RVyNwCIE1kv59ITpN1d2Zb2gj8N1leh0LNxCHhkpscCwUL4TZjTCy6K8Ledzfs6-MeuxvyaNA_StvokJ_yonoIHcgf5fVsPl8WW_OXIMXwYa3y1cyiEA0hbpn9B0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFfn_Vojr5OeSlAHb060Z4k1fY_4nOpMDDlfUHKzOM4jRb0CrhNck-oFq-56Pp2iMxaxLVMl692yJaBX4HgPnTi6ElHvCjmvLPLTqoWJXIMHo5xDhvSAZNWYl47Rhun3aHAamh639YeRTyQQdU0IYG5KB1KNk6Ec4bGGBVs8VltAEl-Gqxc8nCGZH49K1bltyf8Q-0z0f4bsbZ2VmqZtQ4icILAEygYFqn_HLmkB99NG-vcAQ8t1XB5EN1nfBleiahR6zXjR7kB42-9InW9xoYy15LwfdAKFp7ul2mcxM6cFZmyfhy_bSJ8OEr2LeGFWLVOTgZoJjckX1NzV05QKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGytvM5YlSmNTSYk9s6qkf0yeNpUganL2eVfYn7Bg_2JBwSeXTrStxRjtAp25SeHnG6VkyTvFwhbcURnxZlxQRbOMB_3EEu5uXPo3dCsA1qyvO-VxikcJexGGlAesIhFku2KgN8iuBdw_w7XRKlaiW91MG5y_k1dwVpoZAL8tbRVL_gDofjUgAK6tl-5ufFTVW7W79JT-cGlAnQyFw08iSJl2qPHf1IMk5EiBjq5v7ugZXoImJ2n25LgAnhyesHXjfNFL-svnI_GGKIeKzcmalQl6ZJ4zJPUt8ooQOzufNp1nD7hs0-uxn5LsF7Vjz--vpAQhhFpNbMvmErkMriGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=R0M4VkxYmpSXH6NbnQu6ZFh2wpBUAgJcquo87o0XW1l6PwdkOSocEMk-bvyz5wgjFwBLvuBN2TKawZF5XVg4kd7fF5a-OrkntGkz2AFEgssWENqrHjLdlfOE7nxN7uVEynmPOoeRiZGBhP2BBgLqp6A4KuPXNtFYSFSDXs9bZ661VeSr5nGkk0Vgr-nQQ0EhKyBvrESzutmhXbHVfiWm2AJQBF1zMiG_6t8v5QuTO4oEnL2OWNYVbBCrbowx-OdelrWVnN-oCmGENRcDkzzpEUo50HOtdQo9y32cNzx3UllYi4PEzCfIpJ7LpuSrM3YNQt17Flm7rYoDtIsVKM_QZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=R0M4VkxYmpSXH6NbnQu6ZFh2wpBUAgJcquo87o0XW1l6PwdkOSocEMk-bvyz5wgjFwBLvuBN2TKawZF5XVg4kd7fF5a-OrkntGkz2AFEgssWENqrHjLdlfOE7nxN7uVEynmPOoeRiZGBhP2BBgLqp6A4KuPXNtFYSFSDXs9bZ661VeSr5nGkk0Vgr-nQQ0EhKyBvrESzutmhXbHVfiWm2AJQBF1zMiG_6t8v5QuTO4oEnL2OWNYVbBCrbowx-OdelrWVnN-oCmGENRcDkzzpEUo50HOtdQo9y32cNzx3UllYi4PEzCfIpJ7LpuSrM3YNQt17Flm7rYoDtIsVKM_QZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=WOkiK7iU5SMh0J5mOY9GHnbU3pfzrIHCvnx7zwqXNQk13PKx2-zKIA2APrBTrMktpJ84g9hwihrZ5Q-DAM1VRnlb06qZZvcdVUuaVq3lKFbs4eISYQ_FRPJFvG952MAXcnQXqvFbbWvTuPOqr7kpSegViHWK46DSsu3kAntkjZtYhNMUuPX3E9YNCgMuuGZatTHoqrGmN0xRalYg2gcLNppPd3uAxbRROnaasEzDK90c9S3TYdGvxSQ9d49H28g0KC-LvCA3b3XY5thCwUL2i1kSq-7r4-lyl1Qw_dy-CHgYQRLnzCc70zHf32OIpjqWLH8fl81AfLBNTYUCB0bqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=WOkiK7iU5SMh0J5mOY9GHnbU3pfzrIHCvnx7zwqXNQk13PKx2-zKIA2APrBTrMktpJ84g9hwihrZ5Q-DAM1VRnlb06qZZvcdVUuaVq3lKFbs4eISYQ_FRPJFvG952MAXcnQXqvFbbWvTuPOqr7kpSegViHWK46DSsu3kAntkjZtYhNMUuPX3E9YNCgMuuGZatTHoqrGmN0xRalYg2gcLNppPd3uAxbRROnaasEzDK90c9S3TYdGvxSQ9d49H28g0KC-LvCA3b3XY5thCwUL2i1kSq-7r4-lyl1Qw_dy-CHgYQRLnzCc70zHf32OIpjqWLH8fl81AfLBNTYUCB0bqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=m8SbkUoUNMktuwD45hev7Ij6JFIA9855FlJ8SpwWi0tzENYhiOHsyVeUq2_CABdpnnUSofzo73unhCNARYZbfg60c3jopgm5-cbJcbCwb6OIoRYKkvpwvopQFZn8csV7XHiPVz_vclirtwPR9WETwLj5p8QbgWnTlDQTa3EhEJsbOsav7_25O_IXnl5mW5Iv95PCp1QyTWf3k3GOYCEFArYN68xOG7WmfzMXsj_8mr_DQtxytVEYmfUuor9S4dVG1ALTrJWWWjl01QpiEYh4hzKllM9RLpH_AJ_r6VMciT7OLmLDU23TCnwAyzOlhlrtboRcWLwcCPIdqmpuTV89ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=m8SbkUoUNMktuwD45hev7Ij6JFIA9855FlJ8SpwWi0tzENYhiOHsyVeUq2_CABdpnnUSofzo73unhCNARYZbfg60c3jopgm5-cbJcbCwb6OIoRYKkvpwvopQFZn8csV7XHiPVz_vclirtwPR9WETwLj5p8QbgWnTlDQTa3EhEJsbOsav7_25O_IXnl5mW5Iv95PCp1QyTWf3k3GOYCEFArYN68xOG7WmfzMXsj_8mr_DQtxytVEYmfUuor9S4dVG1ALTrJWWWjl01QpiEYh4hzKllM9RLpH_AJ_r6VMciT7OLmLDU23TCnwAyzOlhlrtboRcWLwcCPIdqmpuTV89ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCrSK9koGXXJPnh9HYlGE99jawBLGk9enow2hm7Ymme0eDXrj2IESKuJkrHjKehe5mov7j-VuxJ-pL046UQHfN6SbdP05fvp-cRUYppP2740vi_Mo8otpiFoMezxERvJJg2OR7TzyYldbsehEN4o6CL4tH_bYdBmgaR4f9jL7zVhWFicuImZBA8l7Z3-59N3jiLIi-FxUn49NQq97ZEM-iWb9ZJUFLxomyckduVuB3k3FoqlQ8lVlV_Ej8Vt04kk7E_-_nqh2UZUguzyBnV61QgsSbOcUIfLvN5LBBPBRRYTljKPfgpp7b0CiGm6kIiSEj_E6srqJWjSJ3GIIsGt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=Jo7S-uMRpNHleL3E-MDOl5hcAOB8aSHDi6q00UfbnQZFXoWPJsAAbBQqqHEFJ0NIBhQ6Zp7UMmS_Q0r01mSg-a5ePJvAOOAtBhuEcdj4S3zjRJJ8FWrFqgikslzW9KqJTHCMH45q2l_XlwfU-gyOpZwMeVTD9HqfAHirbVx47oTth4z6EmwSlt1ghvS4AAcjFiHMLB1YZvHOQUwyLfCjdlGiQUkhRBwsCKN0AypXyLqRqIebjc8jnIeApwILIVDJOkvFaxZAg4f3Rzmpi30DwISyoIMB0dRJAJdh32jBAsf6KPWXg65xxi_PdW7O9xaHYDJmxZHS9pFleavxgeyCeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=Jo7S-uMRpNHleL3E-MDOl5hcAOB8aSHDi6q00UfbnQZFXoWPJsAAbBQqqHEFJ0NIBhQ6Zp7UMmS_Q0r01mSg-a5ePJvAOOAtBhuEcdj4S3zjRJJ8FWrFqgikslzW9KqJTHCMH45q2l_XlwfU-gyOpZwMeVTD9HqfAHirbVx47oTth4z6EmwSlt1ghvS4AAcjFiHMLB1YZvHOQUwyLfCjdlGiQUkhRBwsCKN0AypXyLqRqIebjc8jnIeApwILIVDJOkvFaxZAg4f3Rzmpi30DwISyoIMB0dRJAJdh32jBAsf6KPWXg65xxi_PdW7O9xaHYDJmxZHS9pFleavxgeyCeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=FWK0YYp7nZo9C_TF4ttGnQ8tibVXPSMoyvEoLYcQOsoQOJjULtV9LzKFP6wA165iLLNsjjd9Br_c-L6ezpirWXEv4VBFNq_b3c327twnd6UTPO2dvMk_ZhCn_5Cc7ve_rFyhbUlXYJFiTaqpqNZhHCFQdmyGV9GVy2f3CQ4_2sBTxSfIrSGPxTpNA79JADsDkSyPXt0nMX11bhkY68L0BV9AogUCA3v5u7kk2TFL4ViuOkd7o7brpmqDqav_AnhQ355eKZg2CrMmdm9sLvXwxK1snDtqJXPcYwUxFPyva6BiX8T0LINFGCKrVLn95qFTKlhewmgEQDsNoYpn5WX-Eq7hWbd-ykuif6lN2a6LkVycyk3Ta_9uyH-EjbhA9DSjn0Tk5F_-hXQVDuGaO_7rl_kDfLtR8iJmltpH3Ha0qnNNpfQ7etD8UbOJRCn2c9BDE9G7N8OYDvpCag7nAU89wBur7aQnw1sXAk-cJe_os6x-fKhPbGRWMU24LwPKZwNuDmH2X1lOTT4Ed4oy4E7AxdVRxHs0Dm3zMg9_8bdFzK3tuO8Vd3OR4wjqAtWFWJDUSwQDliammUPCSB2dMGDtHYeuPnUXx0PirsH_6FD2uSLnWlgeBk5q2KSio6i280P0ceYv7fct85lmktBGtQbqWpXQuAvBeNL38nssBegwYsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=FWK0YYp7nZo9C_TF4ttGnQ8tibVXPSMoyvEoLYcQOsoQOJjULtV9LzKFP6wA165iLLNsjjd9Br_c-L6ezpirWXEv4VBFNq_b3c327twnd6UTPO2dvMk_ZhCn_5Cc7ve_rFyhbUlXYJFiTaqpqNZhHCFQdmyGV9GVy2f3CQ4_2sBTxSfIrSGPxTpNA79JADsDkSyPXt0nMX11bhkY68L0BV9AogUCA3v5u7kk2TFL4ViuOkd7o7brpmqDqav_AnhQ355eKZg2CrMmdm9sLvXwxK1snDtqJXPcYwUxFPyva6BiX8T0LINFGCKrVLn95qFTKlhewmgEQDsNoYpn5WX-Eq7hWbd-ykuif6lN2a6LkVycyk3Ta_9uyH-EjbhA9DSjn0Tk5F_-hXQVDuGaO_7rl_kDfLtR8iJmltpH3Ha0qnNNpfQ7etD8UbOJRCn2c9BDE9G7N8OYDvpCag7nAU89wBur7aQnw1sXAk-cJe_os6x-fKhPbGRWMU24LwPKZwNuDmH2X1lOTT4Ed4oy4E7AxdVRxHs0Dm3zMg9_8bdFzK3tuO8Vd3OR4wjqAtWFWJDUSwQDliammUPCSB2dMGDtHYeuPnUXx0PirsH_6FD2uSLnWlgeBk5q2KSio6i280P0ceYv7fct85lmktBGtQbqWpXQuAvBeNL38nssBegwYsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUdqQHe2ItRq0MMy3WNnvgqgLwFjFi5-wrSSeUAPvab2xevzv2_T9BrQX2ENhSw_wKsnNnE4nFUvewkgsRaqkjRyr7ktGRJqQmqBre771Cl4UBIl_r5cOR7mT0oYXIYOH6qcwhHc0cp68rBIC0oV-P9mAKs_EXsxW1KwgIlw-JiWZdc1xSmWgfOO9tLvFjfJXCDiOmwuEesAZc4GTOscADBYm1-FP0Nzm4hc2MK3zJ8SF-1oGCkKLxnWgxSYlkzuPsN_VQEpVzhHsPMAPj6LDib5Agzskr7ji7DfbwW2sAGyEe8WsOzMnDDDT9wXA89hYE4TuqcOaqcx-342-YZ2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=ReFOL92Iplzo8tJapUuC48xSGHF9Pih19TtwHKQ7c_En2SihOGYlB2u2I200sRAefLhkbqLyU8sapiwyfKkVu7HZHseHTcnLtJwhmOgi---1LmixB3_JJQK21KM87fk_eK-lV5X4nqsAE_XJddFJMXdwSC93noxZN17pijSpljnfc-iYr1gGij08QU1-ABo-BGlh2ajTl32OwIReXhzEa4NhrPAXvLgHlhx9rL4bdUSZ7G4GnKYEKONX9c6O7iVD1xa_lStUmOroW_1JRbpHZGZNrXY_t_V9ufsjwLPtaFhuJlRghC7KUcLoCAPxBjqyRrpwK3mhRGVbIacQVC_iOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=ReFOL92Iplzo8tJapUuC48xSGHF9Pih19TtwHKQ7c_En2SihOGYlB2u2I200sRAefLhkbqLyU8sapiwyfKkVu7HZHseHTcnLtJwhmOgi---1LmixB3_JJQK21KM87fk_eK-lV5X4nqsAE_XJddFJMXdwSC93noxZN17pijSpljnfc-iYr1gGij08QU1-ABo-BGlh2ajTl32OwIReXhzEa4NhrPAXvLgHlhx9rL4bdUSZ7G4GnKYEKONX9c6O7iVD1xa_lStUmOroW_1JRbpHZGZNrXY_t_V9ufsjwLPtaFhuJlRghC7KUcLoCAPxBjqyRrpwK3mhRGVbIacQVC_iOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP8IslkrhphBEjzuy5e1whLAcn8CK4vKsROlLmyWDPfZUo7UECITH17ex1LVrQ5ZeXkaxWdxuSm6ipRBl237dBT6VRFEkMweretvXD4E3LEqRd_aMsO-GnbGOK4AYVyf_qDzhocBhinf12wznuN0g9KdKNx-ma7XGIXBTE19Tz8pqbOFWz-lUZLN_iQnmG_iucIMkEmrbjPr5Ex6-guTmnzGvMeM6vTB6sRVitcN-bUiZlV4Iy5hAIGSrsW_EsBDskA1h6kcFRFE8AVyj1bRWgqjzSClEND_qIvIZFJvNpl8UNcEClUihJD31UWufc0Xjb1t7DUq7HhBGew1fvUTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZAVFE_I7ETFm10eKAd6x_d4zQgZyKj57etATtR_aG6AU55uKTlmo2-cvFvC55WIz9g6oZepgGAV4-Lgodk25B5anTCPohuVBH1MzM-ZHoAkwI-pVwbslHR91HuNbzr2mWMZ_BTjFvT-69q4xlOdaWmErJ9uwGGq682PiZq4g5MEGgAumZYfbPJKyp4A0gm_AGnaD7_RBPl5nYNwVZn4QaeHPPan8iaCtrTKkCTDU4FDAd2oJsn07oEfLX_ZUCfiHQyeh25dd-2qPYmWemhMXUVnG782QUNo-xZXTL05XTjuiWRWFXYpM-rWUyuElrwDLT6Ai40iYlcEYo6zQE0MLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt3V7Qbj03vtplNvHFDUG-rfoUgUEtRlGYKOkvgZnJ5L1CMqV39ZtiFGjLuQvqrjDAEKtvG0SnqBzj7-nC-bykbv77ZXUnTMPLbPOc15zko5yVqDmBZmFRua_8PGWg-oAQl8wIC-iNlyS5IzwuIU8nrifBNDmcD6cszg7YrSlvNoSAUbdEMp4oQuAlUS2sblM6hbpkOLszIDUuEBTzCQcEnaHLrRjmAjEdLhEj6Ry2FsT0V8SNu65jO3j-W1sQXldc6bwcsfV8qFR11hfHJa9iuwAYohXmngRdYMirqy-hZrmwDde8QNyrlmRL9nJyklUaQ3sfwE0jOWOg3Lcmp0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=v462w1cE7GK-RdbtMtzQuK2TJ1GLjEckj_5sMIwLB4g90Ar0m2NYXGMs9ecjSc_MUgxO01lTzNsAeY2xCYvCb4_Xb7azs2wdis_H7bTeuCibcM5pvAVXjamTSUptgY6g0YH0q_acYUzlK0ObffuD64u52DsuzI3NxcVXyhpbGl0YDERR-z4WlseY5UBkejqfwOlERAEOFMqnvx5yuvNy3SpjCkPOeYZHI9JnLKkIYrupViQLVocU0MqDMJR2qTsgPiPKat74PSN9qqqaQMKzukfBQ31HN4nW-Z3P9jUBgUIJxOFWaBH4gjMQpXoVpmgqfvP5xJ3_XHW4v_e3A0IIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=v462w1cE7GK-RdbtMtzQuK2TJ1GLjEckj_5sMIwLB4g90Ar0m2NYXGMs9ecjSc_MUgxO01lTzNsAeY2xCYvCb4_Xb7azs2wdis_H7bTeuCibcM5pvAVXjamTSUptgY6g0YH0q_acYUzlK0ObffuD64u52DsuzI3NxcVXyhpbGl0YDERR-z4WlseY5UBkejqfwOlERAEOFMqnvx5yuvNy3SpjCkPOeYZHI9JnLKkIYrupViQLVocU0MqDMJR2qTsgPiPKat74PSN9qqqaQMKzukfBQ31HN4nW-Z3P9jUBgUIJxOFWaBH4gjMQpXoVpmgqfvP5xJ3_XHW4v_e3A0IIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=omKGyjnkuFwohK8oj6iaki12ZUles5BrwWMV2ZTBMatnTHh3MRj4NEhfeEBKZYS2Q1qxk2mkcVSdnys8PObZlvtsjt7KTK_tRB5RYodrG3d_yae4O7ClOpPC8iMK3uPWd_xnmKJMYL5Ko0u5FkCTIW3By27fxuwXc-amDBB8kYKhoqwjg-BvaCy9r7wT4QT4RdnmxhDIXA2ZwF9qKwpwzC70wi7daSWpuiHonsngCZ1HhC9yhsRFSTuCctkIqI_XwDzZMiSG89oydB7s4A3zDCQ2MdJhgnANI586NITr-FJJPL2us5SkVix7Y2OcaAtGobyDVIEvc4ri7ay6gIn1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=omKGyjnkuFwohK8oj6iaki12ZUles5BrwWMV2ZTBMatnTHh3MRj4NEhfeEBKZYS2Q1qxk2mkcVSdnys8PObZlvtsjt7KTK_tRB5RYodrG3d_yae4O7ClOpPC8iMK3uPWd_xnmKJMYL5Ko0u5FkCTIW3By27fxuwXc-amDBB8kYKhoqwjg-BvaCy9r7wT4QT4RdnmxhDIXA2ZwF9qKwpwzC70wi7daSWpuiHonsngCZ1HhC9yhsRFSTuCctkIqI_XwDzZMiSG89oydB7s4A3zDCQ2MdJhgnANI586NITr-FJJPL2us5SkVix7Y2OcaAtGobyDVIEvc4ri7ay6gIn1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=IZYYPIAqy4k2yzUivChyktACEluxK6l8h7-dLk12wLURTEbkk69_rZ2BRN4ItkkdIxoLFLXSPID9AlVNH_YwqSPvMzYsAOZNcFrqnc_GZvhX3MjxQtvlfrPNh_yRI7yaYz6JQAKoEAyKiT98nma02BAnjIUUdegzgaQWXV4Nehyo_aLm8cxUMKpVHzDJg_f36RGMAlXQFbFKbioYC6hleEZt4p0z-CC5YkArUVVmj7nipY73Dh9Xcqat-h56Fr3l7o1747F59biGMLDCCu3YPXhGs5U3V3A1pOZsTFqziSQVLkJKSTyw2_YrJYf2UiToW_ZIr39vTdiZc1kz6x9scoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=IZYYPIAqy4k2yzUivChyktACEluxK6l8h7-dLk12wLURTEbkk69_rZ2BRN4ItkkdIxoLFLXSPID9AlVNH_YwqSPvMzYsAOZNcFrqnc_GZvhX3MjxQtvlfrPNh_yRI7yaYz6JQAKoEAyKiT98nma02BAnjIUUdegzgaQWXV4Nehyo_aLm8cxUMKpVHzDJg_f36RGMAlXQFbFKbioYC6hleEZt4p0z-CC5YkArUVVmj7nipY73Dh9Xcqat-h56Fr3l7o1747F59biGMLDCCu3YPXhGs5U3V3A1pOZsTFqziSQVLkJKSTyw2_YrJYf2UiToW_ZIr39vTdiZc1kz6x9scoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=SVgLsnfXRXCOHJXgdBK19EAxym2V01Dm5waIQ1rwqFzHO87ZX8nsGdgUPiJIPP5j3bWI-SgPdctc5ieqak77Cg0k6RcI7GMKiPq0KNhZB-uJ3rLakybqecbt1RAKkWBmaX9kPEaNpstMsDgtv6dvS-BGVa_kTfx5gi9QvPXS4UsSK-qZt8ijDTumbJSD3eOSgVIKPE0SKvWhxNYNKvhSCtUHUyMkQ28ALnBvdjiYwLPrdjo0nlmxX3CedU6Z8Sn3oQgTnmsabww_um-EwlegBzb_C5y75L7oFwjEjgODYF-4UKYdUvoK_NyWU6S8ErB7i0tFJqQ2xc-I9-A6awt-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=SVgLsnfXRXCOHJXgdBK19EAxym2V01Dm5waIQ1rwqFzHO87ZX8nsGdgUPiJIPP5j3bWI-SgPdctc5ieqak77Cg0k6RcI7GMKiPq0KNhZB-uJ3rLakybqecbt1RAKkWBmaX9kPEaNpstMsDgtv6dvS-BGVa_kTfx5gi9QvPXS4UsSK-qZt8ijDTumbJSD3eOSgVIKPE0SKvWhxNYNKvhSCtUHUyMkQ28ALnBvdjiYwLPrdjo0nlmxX3CedU6Z8Sn3oQgTnmsabww_um-EwlegBzb_C5y75L7oFwjEjgODYF-4UKYdUvoK_NyWU6S8ErB7i0tFJqQ2xc-I9-A6awt-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
