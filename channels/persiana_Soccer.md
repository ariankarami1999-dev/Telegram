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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 177K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnEwhAVnVZuc6lbcDzZF9672pp29CGWbfyEipEKX1TCGt8X3MWgjRQ0eCQ4IOdPbIz4LvWpVElVtx71gKG6N_FOHQvSRQPax-rttDOTo2QQWh8zKvaZVmgyZ3FgIAoBIrlg2HsAz-4TOgjaRxXYK2o5xPqN3mO3DS16lwbvP7lz6riG7Fqhc4Po1sKHVz3yc9nNR6WxGg7lU5lN_YfBvyCrK8_ZBwm3cLfxsHTmg73oWBj90reSqxpURfIc0C_0PAN-8mLrAvAxyE5zqbVQfnsTJGrxbEZ0oAHzH0l8pROmQX0UAVi1TvuGLN5qrY8ImBb_JEW0B92jjSH0uWEOhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1v5OZnQS4kd0T9q9bFj56j61LWjSCpZ1dEl69NzYtMc2Czc83yt8D0Qt7k2-PuRSpR92JivXwWTmWRrdUUVz4WlnsIKhJ49jn6jl0fZn-3Zvzysm_S_xQLXwLI9cPk0BD_vs4spNxHm3c7YfD5FMD6hKpSFedOtg9uTKIU3aBBZze9Yb8qsoCfoBKYTIpH-8FnZX_o9CYadaqRJjW_IC1vkXeaUJOUWlcxlSt59F4NmtoM622DeMO4m3Ut-I9UPAn9eGxKUMGzL_SpXbCORzzG7coABeaIlmbZWkwVqsA0O4qGHjkmJW3sD1OZsfxa1AfwDonwPcCwV1WpjHFwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=TX25mho3aJW0abS340mcc1g9YCvrkxZxVm249OlpZwf_JXNtIYZRCRTJss2vquO7BifRtkixzhwVnZ1lTvTAZh-I5KCJkkX-AaU1Nn1zSIA5EeYXzYAV0Jqe2eI9x8vzr-hjUzv4nAJj5wPjLC2L16jnuLmgcR4AECbHPYcFeTpSQVn0aWr9PBITjfygkac8_ixnYAzriOEWtc9LHmeOxGlu4ucXws3HTkQuIplzt2UkVgsuoA4807ROSC269fOJtJM8cBzL0h0uXCgCzSj7sTH88WfDOEbis4LasYS6seqagRFxMWu550dVacwhKh_hb_WBxDnPJnnJKo3QOXCFRmQjjKFaN6dE2YIthxLxioz3IXK1d4olZshAffEXksL_rwCkU3TLMxpDVv00VbP9gUNbyaIvcqS4OuisDHZZHjoeIb4CltckaNfXK3j4bquMt54aYPjv2I6pzWCcehJZnHJ1LMZwaQW0NE_kM8aeLObycz-jxSyPcRkQYN7ELE5E8KHtIUFZNYRnCP24JHZFnEWoPH6yByO0JRJ2xDJSr1kBvj_maPuJqFTIEYqpmu_1JYo2HTkSJI9f651w7CQt1xbU3puLHAZlgk81hUFg_R0Wo0_4xbjCxsqlGvnX46GiteJ0_sxJ6TFTA7uIuPfuyX9tODjU_0mKTnSzUvQk-lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=TX25mho3aJW0abS340mcc1g9YCvrkxZxVm249OlpZwf_JXNtIYZRCRTJss2vquO7BifRtkixzhwVnZ1lTvTAZh-I5KCJkkX-AaU1Nn1zSIA5EeYXzYAV0Jqe2eI9x8vzr-hjUzv4nAJj5wPjLC2L16jnuLmgcR4AECbHPYcFeTpSQVn0aWr9PBITjfygkac8_ixnYAzriOEWtc9LHmeOxGlu4ucXws3HTkQuIplzt2UkVgsuoA4807ROSC269fOJtJM8cBzL0h0uXCgCzSj7sTH88WfDOEbis4LasYS6seqagRFxMWu550dVacwhKh_hb_WBxDnPJnnJKo3QOXCFRmQjjKFaN6dE2YIthxLxioz3IXK1d4olZshAffEXksL_rwCkU3TLMxpDVv00VbP9gUNbyaIvcqS4OuisDHZZHjoeIb4CltckaNfXK3j4bquMt54aYPjv2I6pzWCcehJZnHJ1LMZwaQW0NE_kM8aeLObycz-jxSyPcRkQYN7ELE5E8KHtIUFZNYRnCP24JHZFnEWoPH6yByO0JRJ2xDJSr1kBvj_maPuJqFTIEYqpmu_1JYo2HTkSJI9f651w7CQt1xbU3puLHAZlgk81hUFg_R0Wo0_4xbjCxsqlGvnX46GiteJ0_sxJ6TFTA7uIuPfuyX9tODjU_0mKTnSzUvQk-lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq_fRMdu25rW_DnO_kMF9a_nFTxHv6HqXnybki7gl07gfmbRHGnnb8Zytv9WPvfolWtquQByOg_i8amAez4Fs3y2Wfnc3AY_y9xOr-LoFEMDXDC0oaJC9dzpTrTUo51MGDXwEDEojTqCFVDRDcs3FX1RIbTiil0zesfxT6YAHGP7nTFOz3iWu872o3Vgl6HBzJpZ9EQgKpt4pqGk7sWLlPn-RdLxounOjU-IMnEFI-TNrSplgUF1SQenXqOLXY3SIeCsoPIbcdJiTLnoiTmD50fWkI0FfJBYD22sQGZvtwB-izmHkIUQLZpjUu2rqIGzGyqVb_wvA2mXi2yy7dfzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs1EnwjQRiPUhlGOBA_7KFfxDRJz_j5PZvwJzY39qgXhV83swW2DdtdL4tZlfntwFOt1uPGC2vqRCmVaBQEatPrzIzs0Lx2Oarx8rzcXbdtKzvr40u9rEdIwb0WYelelvRPkI8YrGm8u2i9j5RLWP7TbrfarWr1idji2QoQPAeJNdcqCCDEUGvT2UWcJj0faizQ8k_gmzz-56OWEr6t5DwtgA16jppvs48hbkIe4qkdfsmMK7Z45MGXUVFQSaRXbyUPqArd-2fNaMXRD-E2-jB7N8_loYH7aIwAP6LFDmPiJwRQS4An4IR7-0qjZ81IV-TFIMhLrJshbjwiHepp4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAn8vhCyXwnFuIuXaU3zcI2XlqBQQ4F01-koPHWciDC4WqjwzMFl_Kuu45DDMy7jsfppB2qS5ETJxZ4aAMsVeinb-cAHOrqXoQ2LVkOuCeZQOXni5SMtEDNHHxyNrW1EPAJlu-ypdLQO7fY0jRo8AGmnmTZ1QC5EO6PjiKcnefsc56KxQdlyFgtWwA4rgpgtB0Y9VIBMdeLtaQ0maGZjvRwsLfv6GycEdCXBFKepDg2-JqS_Wxt5Xtko-k7GtBu-3xYpab1QCmGeGKDKhlKwFs-0o7xzYWn6B3R5iSom0BeVH0avekZlogatBZf9MaY_8fP8-_0b45N-T6rKbYNq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaOHNvDT-Y-0KJhjWsgphlRduDHKEYxFqfEuz8dW4OmRGknGovcTmreZ6qwTwo9k3MJheS1TFNpUOGRTftYG1_IzCFvB9VKgjWBZgEaTOx0U2_fqZFHlNutEox7oeVudCcz-UC_Ay_c4J2fYROLZFKQvU5qSO7RnX6pliPrwWy4o63SIwqMW1F7J5_x3JN9OJxqe4n9LavKPZs8fBZC5Urv9Z3tD7VpU0CJhn9wDIKUJcYzLQyWoDFSGW5io3_wPdIZgIvnftXVRyZvidu0KIOqgPSCGnf3dBhyYRqJmwk2hhONp2CniW3Q9LirreKYzb2LzKSO903EB8PgP4_ADoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj2nx5i8PsC3_ZgmSW_PNF0jVGwL-TdsfV106GOsTCATCQnPRW0xwG-WzgyIuXOFJ1sIqEojMfVYZyivc6iercVci-waX123GdPDw--xqZvYsAhWMLvOZVNnLU2aKbJh0RMdviN7uLVbeGyvU1rg-jbj3Dy-U5YuRoBYQGmoLWfqZmAgzEw9tkIO5apyw4XNt31JH7QUqYfuZO2WUtOhkh5ygyRbhz06Od93hM8dbPMPDtUkqirxZ0BIwU1zseQCTmsFZ4ZWesZLSHo7I_tEmPb4dQOWvbMoKHqYHpN8zjmnYtskDLb1uSEDaPQbKqxltx0sla6X4p4rGloCOU1eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWLOSrbBMcT2kBZGR7N1hpOSyfZEgMOMTZB0VMp2VuaswgQC6w0iN0X-uLDKtLVZfWeCrx-ltZG2BiwnDt0ET0Q4OlBvHHhd9juKgmMWwcWqtdgcpFe1FPMlxNz5u9pE8lFbKFbgzngn0KRlqnRCV0j-dL89aPtvutdnc3q-uH1lyuk5-sL0j9SL9pSgJNyKWqKshTM16RmVg0CcZFAem2eh7BOPPsI5sAtzeulRuJ5X2UmJlTYWgY3Y1GHZRITVVpJXTohjv6N7g4zvh17imoRNPzKIbIFbzmdLPfp2VQq4vKHY5yae1oio24VHHVF4ziHhvc_huHKFj8ycJBR_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7zhLmB6tn14c0cGwfWW0MMWTfHbUu4dx2AzKZChs_Qy5OSbiwt1ofdmzAgYQoPpGtr8UbMvkFNpBnTDwV5jrwkA02900K6Ebdf6y4WGScSfOly4CQGaZANX5dqPjs4ryqe65_seRtyj1fMXagFybx75a5UUUfl1GwAq4FqVmFyg_DqVi_x1L0mN71laLViUsK17prLZ1kMmB1bodgP4x5_6aC08csgzdvkDldGti1H4OH_l3Tyld1EZzSZCTj7Jp9CYhHVV89zAC6ujMe3BkwWJP8eZrRDbfwrmmC1hHvTp8Dt7bnKC-_ewQbNh3xcxoAg5TtApjkKlRarQSIwFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GODitzD6X2KR28rcCFUdzGd5l5CRVASmL7GpPOksPfUFRMbjGDhHS5UwEYKYvPTh_sLlFfg1H0dASnCCvsE-FF8SSwUQ4GrOPxe-qDcDstdrW1kaX0PlybEDY_UjZvr58Q9hSslFqj2UbFKlvtSMHCQ91HyGsS11uccd5MOG2f-qrwChys4k_5AmY3RVLkeDkdhAJCuyrbM1UBIRaV5tUGaF7iLWM-8_TdHOdI9FkVNXzD77TJLHbgf0Q1vM1opAhrHqM9TiUXz9qu6_vIWz_7Iu5Gqb4syFOe-nbTjQpIlEWTnzB9_SX1zAGL1tVBIhUnJlg41BWeIp9wjr8ElrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTLrNrn5kg9rEQYHFjR1NUFBFKmgILwSWBUI6DYYXoVxwx-0LfkG2qjEO9CbO9xTb4c4yJlUINNJsPl_kR7Mz1CSDRrZSqSuips10Je2e7_La7vxmnvre220SBdDQkJr6z-L0lBI9e5mg9U8DXJr7B-wmqKv1O6G-YYsE82ZAz7HRCoa7rYBL3Y3DmjsE9WCwcOpYHqOhyvOtQLBYH0yqqcY3cQFjzXWiph_73j-XAU8T1Gqe_CDbqpjH6dZv98V7FsqYbQlPxdDGwcKA-sQTGxTzjTs6heWRhHHJMsh2jPDl3Q4gBTj_gKOqudCEUBbSPtA9liL2dUoygtAUKsfPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=CDYdGDR5uHwUZEkJE3MtO2TTPB1TSyZJ6GAi6RvI7VHk3D-3uLJJUsXjxLsPL37ahUDEuPl5OJhPHXjV6ZDMlIqcTWcJhSzjOHhBrcLyGCX0uyt_Ogatl8Og2HorJZF4v7ns86-l5K_MzbMU98AhL47iYl8orC30fZPGUOOawfyMIkhDExRVh57cnMtXxaPZkVgDAYJfmy15hIR3HgJTR8pckrbndiXXRD8ABO9kZw-EwAKmuRp066jxTdeQh_P0qqpd3jJNHZE0xLhFgmjBPbI_3z2olWEJfent-EFiqfrnDlXS1kpWAF6aQpJGnigCEJFshaZPmV_TmasEHoZJxIFrwUil_Wkufekk8VLfwJKalgVkbWB-6ikEHRDL761EZvKVBVoJ_vPoiiCTTB2ujmEaF2EfB7F84d3kAmPaoPfDXNdDapM9_xg74GWQY1OdbINaQ0BUMiWtL0IeSdzJhCNg-IyT0SjEKOECvuXocR1MCWWjs53ci85pHVwmvQG8TfqXc3nXGqZcsuTjGN0ZNvYKuBuITMuuumtkdNqfXC4n0fNMjFd1PvxXoI6v8ybf1CwESaduu5BcRpll0fLdtPu8KlJIMgXVnC6e5j_Qu1V9rl1tQHN-4wQnfWOPmNxuN8X4xkOT9VR9Zl5PBoYnpdPW5wBo7fk6AykVBnZ2Mbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsyvnmKD9wqQIKN0cBByW4g4qrBGAP7VY4vO-S-tWC41gU34Ymbuu8eOQHn3xPl-RkVV_ZKMQYjKZkXQrWuwO1qJRFIUzvZcYqQBHXjtK1dZe-_PPIJGgzVYUhQjx1BdkvkucBSr7xhbv5mkjskxV0jNW-2pcwz9DOUoM_tmZpcCBzc7E0CiNN6-gzk7nIXGSpDEHlqYMcvxhd4pFU_5JPpsVjj2H1QWYK7XTjmX-3h2xICYXtZHcWFAd2yzP29ba90sNrc3jrJXZpGWaNwC4__i5DXusrrGWFiJI5yF5HHg5Z1maxKqGPd3tZ_EK2QxvAV2ieXvAiURs56kGDBFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=g5Ml4JAU2qmeZFVeQLJRLHuAcAoTyoWEFvP3k6wNmW6o2x_nIKrv4P4NY0xal84BDtFRFhqUnMniz0kdOkTvS4AGSxUqMvj3JbutPwkY76j-GLrL-Nwj0Tri5LC-4a0fG1XhuUxEIuk-WpUleyRQnJtldwcO8Dko7j-2mIwIY8TVTkudSrHWnSV0Kjv1cY093DQVh3a-q8Udymos1BxjagPKLerIudvrebHOBc7vzaMb0IFFOz8GjyclI5pAG-p3CVGooN0wnk_F_rXWpXbM3B7HURg22YptPrIGhIsrea8kbL8hrG6tf6L1S6rxw5adpnGRlPnb1guQ9Ehfq7QOh1Q7TXFKrzfeW3TlYO2u_pbS5i70XAK3MSNouY1sxS5lfLmSaVF1MyfkkWyoThxsiJcXIFA0rfuhpGyfnnpS7t_h5D0tFv7lMW-SxuZk3HWeTsanmzJwrvZyZoH0hTGlg9njF4qr0UYuG6fxRN-vHWGr8nD1ISW2zcLgT3zk6q-DZcC-KnO2HGu4VxvzKvmbfFBoOfFH5SNIDrxZuqZMUWT1aMePZcgWoSqSkkjvDkZp90eI_ctAZsbZts3H1cpj4DUP7YxXGjcnHNGlqe-xYk1466vuZt3QT2DSh5sK8O-6j8cwttrxQGzJJvtMeD89bYGu9ZdyymgmlfusOY1xRK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=g5Ml4JAU2qmeZFVeQLJRLHuAcAoTyoWEFvP3k6wNmW6o2x_nIKrv4P4NY0xal84BDtFRFhqUnMniz0kdOkTvS4AGSxUqMvj3JbutPwkY76j-GLrL-Nwj0Tri5LC-4a0fG1XhuUxEIuk-WpUleyRQnJtldwcO8Dko7j-2mIwIY8TVTkudSrHWnSV0Kjv1cY093DQVh3a-q8Udymos1BxjagPKLerIudvrebHOBc7vzaMb0IFFOz8GjyclI5pAG-p3CVGooN0wnk_F_rXWpXbM3B7HURg22YptPrIGhIsrea8kbL8hrG6tf6L1S6rxw5adpnGRlPnb1guQ9Ehfq7QOh1Q7TXFKrzfeW3TlYO2u_pbS5i70XAK3MSNouY1sxS5lfLmSaVF1MyfkkWyoThxsiJcXIFA0rfuhpGyfnnpS7t_h5D0tFv7lMW-SxuZk3HWeTsanmzJwrvZyZoH0hTGlg9njF4qr0UYuG6fxRN-vHWGr8nD1ISW2zcLgT3zk6q-DZcC-KnO2HGu4VxvzKvmbfFBoOfFH5SNIDrxZuqZMUWT1aMePZcgWoSqSkkjvDkZp90eI_ctAZsbZts3H1cpj4DUP7YxXGjcnHNGlqe-xYk1466vuZt3QT2DSh5sK8O-6j8cwttrxQGzJJvtMeD89bYGu9ZdyymgmlfusOY1xRK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1dtHW8VMVFsF89PWJJU_RwtBAo0K8iEo5NK2bI2qnb5fE8tHa-9_u25r_xZ_RKdcs-MjaM6BNZZqV-m9xCsczxSRbP0kTCewANbk3WnSK35hfNH8Ws4-QmUkfTkyUfpRZ6cCQnPcqF1aQ7zLvVqUSPxHFjHRp502OoOWX1Kr6vNvu2Z7xrv_aIWu7i3rp7g3NrG_Mjhl11t94_7d7CnyoEZewgxmXRari7BVsi8o6hShQM6M8hHaDPpbzBhdLhtD_7ukFosFtiYwCyyv4V9u7h7oVmJXt-gJESMqUM5MlIkr7fci3yy5wMV7c_l2BJBsQSOL7D5UAvlFoI-B8fErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjKyGkH1w3cSDTVPVY5tPhu0P0mBlEV4svmTwSulYy-wbwNHQhm__-B-Ivy-SBiTilQ5008y7g_vtfJiI_NfVyaERD0gMM5lFoyy3x4m7BQX-cHPJAp-IjeTwtokr83b_A5Mfv_TG51G207DVXu6Vuyvw3X7vo_O61eXeINTdWGKeK8zsx4Zb7vmsRny2fg3kmZIVh0FDswGcB--kenbx2IOW8PeAwuXFlcq4KipovrkzxWvuX8q7F1mAF9P1sgJrmzsdYdNxtH2BWFvyPh-p8EEKVCq8PbeCjp9hSuoPzpwfVSQ8icehmD1xmPtzSBmvnZfbWnG_jyF080Ycldn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=PvU7tnK0RL83CMe61470-wk_-6DeFVeXN3Y_loAnSR9M7UC_sXSVuzHhirGB-SGpYPUoXbC1UHX6HjO1yYSSYRaVm8Hvox2k8BrND-Z6fdItheJt0YXG8slFdJV8IJpnWm__Xh3PenYhO13kTioVJc2RqO06HSt3Vm10P-0zPjs2YhOJ9dLxawSG6hs4EZHl_0UhDAxyHrzcVIt1ariiH6RN83UQmyOeZ6xr909h3ofZPdw7JslymkofPAtU9QR6fq0X-vYdyGoSA60tZX_KiBPVeO-InhUSRBKBqxic8x00gX5r6aaJPOGusXpQ-tddYqtu4koI870DjpH8qlD0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=PvU7tnK0RL83CMe61470-wk_-6DeFVeXN3Y_loAnSR9M7UC_sXSVuzHhirGB-SGpYPUoXbC1UHX6HjO1yYSSYRaVm8Hvox2k8BrND-Z6fdItheJt0YXG8slFdJV8IJpnWm__Xh3PenYhO13kTioVJc2RqO06HSt3Vm10P-0zPjs2YhOJ9dLxawSG6hs4EZHl_0UhDAxyHrzcVIt1ariiH6RN83UQmyOeZ6xr909h3ofZPdw7JslymkofPAtU9QR6fq0X-vYdyGoSA60tZX_KiBPVeO-InhUSRBKBqxic8x00gX5r6aaJPOGusXpQ-tddYqtu4koI870DjpH8qlD0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvTQA67cJr-m2v2QuE2OK-4yMCnwZujUKvQ8PK_f4IxJQ9Ig90fkYrzhLORfu_jX9J2nWZs12Mqfs6WbC6zLco8CgKx2ntUbrDstq8lhUB84AfXh58XbcPQgPOtrUAlezKrSPfF0XLQS6CPgrvXNV-mmqpjzLe9RY5y49KKZ_HCCC5zKbW0-o7FmbR-i5v6TJf61F1zk9sPksYlWJJTZIZoR2QZubFBcuX66lGqdFw_ANWxwa6QbCYkqfolzV_RP5oxBWYmg7-uN1oM4FjQj3kvObYWKY2Omezzqbv8AC5H-34ielCdyTVR4XIgap11wA5btt65WqM1bKwV4cnKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ZlrpQhxMUJB5XFS2eTgWwD1vZSMgsoV-5FtTIEtzCvO6pUn2wQwYMayCI3LQGFN2kkfFqxZF5oBP-41qfSWUgeRjIlkzBsoayWKJHAg6Elavfi5YIShUM6Ndm-Bwyr-prKXORscBzuAYX8zUczEcEHS03d75eMokuGNkyzAlWjgFV4-9MskCyiXuEdDPU0pdXJ6tZfsp3W9UAdW4xMCyWM0RHWMauOcDXorfXJk1xscYqv5WcOIo2oB_k0-vgMFi6XcH7-mis8TaxCZ82cQJ7yv7eVkJVlZpx1QzF6tfEnoLj5jHIpaVb5xhrmRiRItX47-Hv3ckMODC9v9P2jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4576fhAYUxv0_-4pRiJxIHEqRTUA5tqv7ad8uAI4XDNX8ch2yOTrOyXnYjNfqP9Lfx1XiM1FFKtRDxQjk3yRhml3N0GhrdXRy_uNovgEEiqU1aPEpg5tMuiDQW2bTnIGgAbcL3ey-ptJn11QbMLFSg765q5zJ6VAdCnQSWHDV6P1MdaNTPIL313fnMJbjThBv-0mEtmBV3FKbut6mE3fMRExm44ngqs71FlpBWuL78ZBEXbAsy8qNAcKtC07QgOLPPfqfgYTK1hv6ou6Cnv4TXzNh5WTySyqRqWc044EdbTtSL_GGxWYrshUG88y27CrNOIq97vB3NNtwuOaoaU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhpB1sWc1xYlWPXwGeFG49gWd6xB4TtXyCxlU5-l1R0EU5BSkE-129LuEB0vypQGO_7FPQGsY9x_wiBKy5PrkuShYpi6M-eAzyjJV-E6wnjAOto2z1uzLu2aPAs3tbKdYbzuNwitiyBb9H8PvZqLEVFgJAbe7UJCwpXnKv0yibN_8vnWNxSPfY-G5c3ftERnwS350jrVaNBqOo8K0uT_9pDHMFnqSC4sgsNjrmEw3ZzPIin4eruXX6BV9o-gchtq06EBP5chFVLWqBes0Lpt6CQQZ6TSRicBI0tKXJH0t1Zgamy5VTQ_t8NEuadUrCK-Xmy-ebrvdo0CQmAcKkOsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔑V2RAY-VPN🗝️ADMIN️</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiJlXQ2Nqtu7We7c3aexc6Ls10_FG6N5xDiiDb36liAS-huOBGuLCrQq1Q5SLlxrhV8_jUqujovEf6nQM_E_7H2y-6rHLK6ruejCwaMhOM9xT6NKBbBSli3XGMb84NCvgPbhA9YD5NGBnXOmSn5SCETNn7HQ8sWHIfkkw0RaRlByjIi9hrii9aM-lBJ87BF1RTCXvXyMMCqjSOvMcTXvzNaSKYA3eZVGTKEqtwrMmYaQ8HAQX-dcKUUgN3yR9nOY3Nb-jSC1PodQvobQ1hYtL_3PaWUpqEa5IAb-iEgq4YOZMb5MaEPYqsUifHf4WUyE4iD6xEx72XfDCd_pn4oRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
سرویس استارلینک واقعی
🎖️
💥
🔝
موقع جنگ بعدی،بلافاصله تموم سرورهای موجود در بازار قطع میشن پس جای معتبر خرید کنید
✅
✅
🥇
آی پی ثابت و واقعی استارلینک
🥈
پایداری تضمینی حتی در زمان جنگ
🥉
لینک ساب جهت
استعلام سرویس
✅
بدون ضریب با ضمانت عودت
➕
سرویس
تانل و استار موجود
✅
✅
معتبر هستن ما ازشون خرید میکنیم.بگین از طرف کانال پرشیانا هستین اولین خرید رو تخفیف میدن
·• ━━━━༺
🔗
༻━━━━ •·
🛫
Channel:
@vpn_artel
🕹️
🛡
admin:
@Make_server
·• ━━━━༺
🔗
༻━━━━ •·</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22627" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ax3W7fdpQ-zMR0HBfRmSjxd8QJjwhxZ84DPZ06fbtzgNsS4jxIopj4Y-hkZ8ftjw62c_i9kQ5KdWzND6zHCJf6Bv0h_ZOXkkWRPR0xf7CGLTaT5xpjYmIkBAFXplhtnWLFuUJakSTDwqMfhdl7Lrv9P9a0rQ_NNYXM_uLbSDAI9obSu2nw9E5H-qNLCSFHcT4M0ISU8DeKVxo95_clTmPcdonrd1aIUwwyp3CxZHnCmYf0i4JTHAleAXO8NRI1fU6NyciuXYoYEQ7OW0_QnwQ-fibHfCpd9Q_C8YRX-p59yzKuJtbScvSjyVKZSyWPLxaw53Jk_ZiRLD-sDF_Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZJzVAlZoJZzCgMpuAC4X3NfTMivdxdG_e6_9bHc_UTUPsmZzfruZslHNxhrsFSZe7fr1NRERJ7_S4Liw-lKMJ4zNNBz7DzmtNOIYFTGU1GGiko14_UlpYioILFVjfAwBC7YgVGAfEHcSkQccYRTSauZRgdsPTwIiz0AW1FqhUtjT5m61Fhk9fCQywfUtAfClA_IYSHHLIKLhX6bCVKEL2rgB-lHBb4NnXFS4etBSfkTjiFTO_CKYJ59zBAadwnp_5kFLnmBFdSQDVWY2fDOeuc5Bsn8p0MCj5v4y1TKUivzGsEimEu98WrdvfP46r0gW4ClAzS1WgItxDXitBbOgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvEixoTVmXQYg4uTjf_ndxVSZJnzKUAQ5Kx4IM_dx288bx5YOTFyEd2w2VsFqCyo__AvgzogAAXkhY1_QVjfErW7GVpKMMh3lhK3oZGsxr2vkJCAQaxIHJgTddzjgYGIWqrVANex-X-2WXC89yJSIDmRJfpWdRSjsKDsV5ZoWlWVsXvmIkYZsOD4htUkB5qpp2Wx9T6eXXqp8EK92NqGMvUBSaxG1w5jUkNy3FMJ6r5xn5mPiLFEHVcpp01RH9D3OVQNP4gO9vUuwjxsZs-OyS9W3JCD7sncerf-7oJPKBlC4h_XHq8Fu9-MVadRNf8scgUdd6R2SX4Jh6JwGRjnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVNsB-fNrSCzAXOWlPISA5S4YQXEpWr4f1ME0SS_XvwgEO-SRCMATIJ3--tBwHiYNOiVWqg827Qjvaqm2ys8Rn_itggZ5gAS4xgD7HsiHZeDWzJVndt_arsrqo8g34aa2KRTrDFyv0k9YSNzVZDtMh5XED_i0qBc79GNceIspV1XobQXPkT-ixNpHDj6_xLN7VaAQeKOrPogobIGjJXEzkd6OgPWvh1dCHL-DK-wnUOYrgBdR93k4Tyoi9VGS7FStVlTBNopLNAjNGdUrL5rWWuHaX_tdUm_Y5-6qKiRqf5VQdvzDDNGjrCdBN64Qn51ikOiHh4UAHuF0y_sZTXecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6P4e4sMLT2jqpnHE_7BAlNGAv8HsuqDHVen1zj7QnuUYoq_YvRA5Q-uoaAY9chY4mPHa0nyxS8HqnfwmSBiwQTAxsc-o6jeVZozWSmChoKqMSinLoWGF6Q10JJ5m_97Bil8W1YubdTcf634mhCcSYHtqmO9qFQhIZYPTxmYtHZ4z_vF5KzHnCJsEHe_EPOUtS_4Qs23KSPULgTltgSklSfMToP8yZAJeOLyftFBQQ48lkPIULDdeCXEIZT-GS36iZG_e-M2GrmK-RHoKViFhDbZw0NUXP11glKYaycVcpd0zvbeUAFmB-QH7rAuB8JemtOGNB15O1P_Eg-Fdsw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVBDLvOMun8BJmxklwXxFKc7G5d4nsJP1kaGC5Y5FS_961hwYPj79x407SXN8jWn5-PqgdqJ72FRgZi5hsRAv2V1qOyH3q6DEbNXEHWDBNr8AriamQE45v8N9CqqYrbB6m9YkJvrDovTpyd1o6YXRd02uip4WEV82-ixjGZ8vrJQ7q0VrnoPrT4yU45S-ENzS0OXBTWTmmM94SXJo5c05RF3Ky5kJ90kzHxpEd7smfY_c-8KnMk-mBJqFqVqao25eIj63ApGLc0_LdUm4ZWC6voBPpJgWgELQDUeD00_k9p_jW5GJuFYSuOM76H_l2N-VqWM6EskIvquzC-5UkZuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpkT1zhZdySiKQk8anZYSobG0fOlAejBtp_tBuf8sv1bsL2M3dsrIjd63mFPoWK5z0GvMi-XXehTXN6x3Z4rCemWJTk6ncFVMWMOsCkjMsqGid6LpggueOKEvQkHXhe8XwTQmv6c5cfwi70RhWmxk3Avx-Lkef3iL3jgAstmwcKUMScSOXJ1V5e0c-JGpAhaPxg9QOGfxfM8AHtiZrDijmue2NQdUvoUcNS9gP-qasZvhT0KVbOYB5yheBpVTUGY83US0wndlFVqH99MFNUT2CIvkjvRSyMcGbnjPalbzOEsKLcd3cSnVz8QCHrUmOwK1Q-EKI-_eQZIyweNf1Ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=RLNSuppTODzdFz4SIW9kn1iid2JwMq9LyFk2KbsJp3tdDZOBOFyuzU1DcPkouAxyMzC2oMVVYjSipbadn7iIYFTX3iFjEXGiyZQaGvOZMW1YX6S16iK8zcSdIEZhFBeEnL3aO46U3VCcx-0hg3m-sds-hvBQkug7faOEHpz8pCQZbkvBE0xUBAuvMo6GNIqF1HNnKY5YuiQAlwu2Qf2BuKlrQf7vNlK2b-OVJJ9QMKolBM2omUTZK5NrGAQcwWkZGjYuT45XGnii37MNwe1njFwz97GvqmN5oJguMQzrIrGjI_2-6tTzZvpZo7OPJ0nUsm3Cn6IVyeSKsxtqTdJ_-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=RLNSuppTODzdFz4SIW9kn1iid2JwMq9LyFk2KbsJp3tdDZOBOFyuzU1DcPkouAxyMzC2oMVVYjSipbadn7iIYFTX3iFjEXGiyZQaGvOZMW1YX6S16iK8zcSdIEZhFBeEnL3aO46U3VCcx-0hg3m-sds-hvBQkug7faOEHpz8pCQZbkvBE0xUBAuvMo6GNIqF1HNnKY5YuiQAlwu2Qf2BuKlrQf7vNlK2b-OVJJ9QMKolBM2omUTZK5NrGAQcwWkZGjYuT45XGnii37MNwe1njFwz97GvqmN5oJguMQzrIrGjI_2-6tTzZvpZo7OPJ0nUsm3Cn6IVyeSKsxtqTdJ_-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMPLy6_lEx6vC15_cfFK25mLjrPADM-x0O2ydNja6VaTR6Hgju6ulifKrcJkAH7ITAnNyLygpoYWFVCbSO_hqmrz0fXnv43POM1s9LGORkNfLUhzldt8t6yhEexjfzmfr01eiXgmvGplm2WDc7Q_KylN18a9L4VEF2J7_7hORDJ3t9-iOj5UwnQBF98Islo6PcDGdLgYGy2Tke-PXM1rGuWQZqI8dDn_vLejdiUwX6DWgp7QdrVTgYtvoWCyIsUB-xokwFfy9piJygLuiRvNIjyFnq7uJRV0MXpiCXGqOZKgMVnX5h6xgCLKaFbOS-tfMJiPvxuntcaiQxf4qRd51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=W5I3RphS6cHbo3BUffjtawHg9HrmAcavaPLhYZDsTQZdQ3X4mTvA5p-olta8D_SYYa8Tz_zz8fbBqxjk-F-JU6Tu_2I7ixZu4eoAcdNpzxMqV2ACE0kcCFrYyU-ceOosWiCPk_lDHMjNkk9EGWXsnf0Q0ESttguSE749TU-TQQGJbmKeWCs9EKay6YlkG1VqAtm4-rh22cisLbRo5wgq5sScheO1b9Qn5QGs4ocwvX4ETI2En04fR6kBNl8wWrjJtsphr6dEUZa3kZKK-__KOQJXmI_RyPT3cRv3ZKzsPNnp7RysUVyccydCsO5m4FvpgzQSZynGgEifbOb7vzZHNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=W5I3RphS6cHbo3BUffjtawHg9HrmAcavaPLhYZDsTQZdQ3X4mTvA5p-olta8D_SYYa8Tz_zz8fbBqxjk-F-JU6Tu_2I7ixZu4eoAcdNpzxMqV2ACE0kcCFrYyU-ceOosWiCPk_lDHMjNkk9EGWXsnf0Q0ESttguSE749TU-TQQGJbmKeWCs9EKay6YlkG1VqAtm4-rh22cisLbRo5wgq5sScheO1b9Qn5QGs4ocwvX4ETI2En04fR6kBNl8wWrjJtsphr6dEUZa3kZKK-__KOQJXmI_RyPT3cRv3ZKzsPNnp7RysUVyccydCsO5m4FvpgzQSZynGgEifbOb7vzZHNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnV7e5B5XFyspuQTtklCbixb0WYriKHY4JdYU_WXAT7mmTTRDHuBxkHgcX4DZlaVc7FilECHkGWuVL4s5kbZTAJl5SXey9krNfpWFCiQo1nBLCjP0d71pFwSgNI9VlTYUUMd90VTvi6FEZ1k1pHgV-7K554NarLI-QUzrAPyD2flnLQ-FtoLMvdIu9OC20Aa9WVFxFRhcAbRV844q-lrwUVBgeVBfROhxA2LfelFtavCSmzbl-m_ZMzKYxKN-ZFd-NfoGl6vU_Orxl9fNy76TbFdo9Rw7TvO5a6OweWTE0ldoxZUWvjnVdY7bVNvkOlAz541bcRQhAblEWbcWWApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=B1x_Gf-Z_PGPpqbwgpVezbn69DcZslKr7M4qOnCkVYvi3SXarKYx_Lu6U1gjfPQxRXRk9QRgwisRkbL7yiuFp6HXpbo_lRprUIowzUfiHM5tsH6Yq2jiLYCwphHrCzH1fflu5MRsHjU0i_YTlkHvx4lXko2AuYOHtxlSWQXt7kBiqeugW45beTaQnR1GHKtyKieRmtGKyjh1qwh_JgIdkNkaRxtnp488nGouPvzYgj31dt0F17SSq0SOqopLhU58hP7ikvA0RUfJfja8efCU2k-qGhII2rT9W8Nsg4w9-U8NUi1yK4gL_K7mYB6jF6wduIN3bbivSEJSQNyvMRRcPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=B1x_Gf-Z_PGPpqbwgpVezbn69DcZslKr7M4qOnCkVYvi3SXarKYx_Lu6U1gjfPQxRXRk9QRgwisRkbL7yiuFp6HXpbo_lRprUIowzUfiHM5tsH6Yq2jiLYCwphHrCzH1fflu5MRsHjU0i_YTlkHvx4lXko2AuYOHtxlSWQXt7kBiqeugW45beTaQnR1GHKtyKieRmtGKyjh1qwh_JgIdkNkaRxtnp488nGouPvzYgj31dt0F17SSq0SOqopLhU58hP7ikvA0RUfJfja8efCU2k-qGhII2rT9W8Nsg4w9-U8NUi1yK4gL_K7mYB6jF6wduIN3bbivSEJSQNyvMRRcPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjCgXEGwL0cxVl1UjbBeL45JH00BVtlQfQzDwvYjbxSO-ZxrVEDuPDH22JOElrX2lRSIjVwfJ6ZWAjJ5_eiEuRRyUAXIlxJbM0G18XpDD4uczL0xp56fxbb3e1kozq7txcbTZzATJ6WX8uha7dK0Jvxrj2AAiHkJ2mLKq_76IDlBLlI7ByH4gOtwzsxtHIVCr8bStWMHATiEBRoFL8ayssgSgwr70NaXrVD9w2zYny2xrByhgoNZcRj7pYSwS3R0uxivFP_F1fVicQEAhDZOUVGVKoxcq7zVQtoGyzAek_HOtyDxmNPLbjhJGZINnbH5Jk0DeVmjD0VhVXIxVn9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqs_wfc00utwucrjSZp1NLWbXYfP9LCIBpIvtWL3WHhIreil5IA4BNeLncr5Dra5iwwF_DGlO7S_w3AuW6rc07RFSPVjlm5hg-BoDPeW_OyScc4M3yYAAfN2WsYyCYRVE6I6kG4cFA1rNSF2nIU96qdGxta6-5EkhM1YjKETaKMkgMKJ6ZIjbnPRozMCildz0ZCk05INTWPOawrVJ0rFn03Dk38S2_tEoa3tI3lZCZQt03CCU3tNyM5ZEwA57GitxThN5azAfecEmWC3wsccigf4cWp6Ls7xLEpIYXBoB-DNxftl3CekRunEVr5T2qZINO3sJEabWBabpF2y37m4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilL9sAH4jZXNqcPQgPMj5bBljx3EQqzE8rslRThrmEHw1j2C_NKOz-iVqhFzvgC1qcIC72hSoBKFQDqrNWOBNIXkij0lkyyzdbiMfxyU3yIFiAdp9_5aSMYudFZs5V50IwoJSg2AcFU9G_NuN6USITdSH8P1tcFoNpmYmAZaMg5S-i54fdaTrlkOrf3pMAuwL5wxJf8l971tJa4c26nn88-aOgd2mYnbmQ9UTtR3erRWhBpfzVUggsQz2PtwhXIpr8QrrwkjWyRAaMC2uX_vppY5H4RGCD2EU7OFdDLrejh_qe_ah15198GZcHSWPfvUJ6k_5_G-1V_lb5IrQBe_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU4GYgPP1JaVsmISPk_khWNCBE1PRLUuyCRDxT9JjpkiSw-Wf3rzEqiWGa_8Cm9DG0DngIfth5xTdMIPDi25GFdJ-KjoyJs7HFkrBnOsnNk9pfClTVmQL90Asu0iAZIRJOytxySZdBfd6Eusdp2gL_pJxNQr2F7s6VaRoxraWUbNPjB7flkEkRNi7xt6c7KrOox2z0Us4p13VzZhEgHj_fWTRsgtiYFGxb0RiJUhHpADkStMa832Mp4RRginZFNObSqRPowK8tj0MfOJladMkRZGiOxA_CTXkYOioE4zeli-aY2h9uVQw7Eia-_k63UDyVd5ce99PmM8Rr4pxbxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dip2crMiWFBTlMNz-TVjOkkeeG7v8S8MndOHcr01_Gzp5JEk7JdwqbjUb_LZabwHIYuGzcvdpliF8GbOO0DK3bGEYtIisORHWtPSidiXjeV96J6A_liIYEAOKCuEQ9pjNWDate2l3Dl4caXVPkDq9AsYn3F91GKyJM7kbnJWcBAlS9FdS-MsdfgBQGQRDzfFCY0D4s8ruWVrWHZEDKA3Puup9a0T9tGbZ8ZQfDWhfE_LzkoL_kohJXXW4q07o2sBP2FKPS_xddpYnfBxYQrGlwNMEDRdVg4J9dZwNC0bc0pdJAWXVSm2Bis9a6uey7Jlq2cDIuT1WYRxJ2bi6Ppjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV_eKEbTbpOZ1U58PjNg_dD8YKubV1D0RprJ0PMrgEV58QTVqF_qeHjO0PNVy08s0F06GnV69A2mavCsenEhX9kahZp7-5zqvMdXl-WgKqSwn3AG1y7dttPcnqGx3jYQE0cqizA7UM3wtxFoa0MM6Rw9GzKrR5NJKw8V7wFn7qKpN22P6M7o_7cEF5e0Ar2_TApgeji4428T3766casjJXN6VE-giJkgpfVHM_vPAEJ-Rm_KxLuZ185OZXhTEK1RjVREhyHQmSCYMOyP5aGZrC6FS4Mmhtfph1f8eqWkBaU3-8XUj59wQLlNMs6w-uv2gcz21Zjoll2iolKCDpee2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDXj_JAbw6OtlwZr0Xf0ntkZ5dL38CgpjCAG-QDCix7Q-o0wo2yk6dZeDH-JXsPfOBbfz8kmcmQGPf3UJdzGAaTWtFxJfXMrrw_JBFlk563lS2HqPn6VIYpqqwxI-iznL8xddlpSfbhMmtF5puCQ-hPsJM67iH6TuDqqh2DdeCIecEvLKH-8lATyeNa4LUacMK1ZlET_NiKZ44r7N3tqGUrjU83PBlg47QDRrMNqE9Ega9ULvxHxbeUnftpxD7ahjtsyNR0arhwcdL_OzsobtQRbDp1jRfFNXU7MA92COQC3snQm2PTMeDrNLdKJWjX8O3P4CfQMICvUOe4qFAf_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfD6ezEUmstnKEH8WqRX1ZFgVXGG_J22QDpUInDFInDm1UcJrm_luN40od9t3wrdvziSXhA9Xys8y4maqwxlBGSoUjILTrwq0gQwbnIjMVzzAo4-N09z6hoW2k0Qgyt21I6tzPdL_sQzKLGnlCyqw5mipBbNwAjtk0r3CHS3gyTBShFeiAAQvmvAcDOeMCo0hPCUKgBwFjBc4BHaNR83fDFTgkNrAOTYCdqZZba9huOquKm2qbnb61rJ9xwgo3vEP_h56FXFgp0H-JUQHE9f-hdhTVF4kyKNPaVXoEJOzdjXioA6rECvLR-avjXDs1D-pHjwpiz1M0vAFnJY40l2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=UOvs6gFlnOGKc-MrBpkYU5l2vogD8Vmz5Zayeb5QuP4Tg__xzNH97RanCmMs52OtuZsUK3sz358p-MqclUxnmyfk-w-gQA8CcE8ivv1xQKgqBlOmU3Wmg9SbqWgco-me6sMPJ54ds3btvylWn8TnXxSCqTjvcK07iKuwT7SOSfedKtkKso2tHQmW8BE7NWhQB6dx39E_9IbbL2qSLkiOtLzXT3AHVwpUsN5-s8kcjUoOKU_Jy2P7AOrO4GsYYcnPOvPPk7_y82Y_pNOs9QOG4PPD724ESOUoxyKOf53ayNt5gnYyJfdCvCteAkxwkta-q3q5C2ojuPJz3yYl6KQ_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=UOvs6gFlnOGKc-MrBpkYU5l2vogD8Vmz5Zayeb5QuP4Tg__xzNH97RanCmMs52OtuZsUK3sz358p-MqclUxnmyfk-w-gQA8CcE8ivv1xQKgqBlOmU3Wmg9SbqWgco-me6sMPJ54ds3btvylWn8TnXxSCqTjvcK07iKuwT7SOSfedKtkKso2tHQmW8BE7NWhQB6dx39E_9IbbL2qSLkiOtLzXT3AHVwpUsN5-s8kcjUoOKU_Jy2P7AOrO4GsYYcnPOvPPk7_y82Y_pNOs9QOG4PPD724ESOUoxyKOf53ayNt5gnYyJfdCvCteAkxwkta-q3q5C2ojuPJz3yYl6KQ_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=Or9HEM1FW20yL8X0KnN5a4wzI7w0mtUR3ltxEI5rWY_gBtp39k5c5qqnV9AUvqzMwAtZ0-JH74XD10veIFhPDjRAK-ng6150gR4CYzI0vA1TCEtwbwJLdc7_4MGUn5Pe1nt3F2vEUpx2S2p_OeZqiKN4ucuDzYY9CKDV89FGYInSQ0feACHvmbKZWfMPLYe3AQGASHhKpqj19TqIrgLzZ0YXq4N2miiPUGFz92Z3g77DeIBuB0YkURdil_UQeR9gbi9CgzDwO3mZ51kAqjkIO5XRms1G50zCkW4uJvEaELkVdOLukMxJr38FtfUWFUTCQM4QL8tb6eHjm0pgSCcz1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=Or9HEM1FW20yL8X0KnN5a4wzI7w0mtUR3ltxEI5rWY_gBtp39k5c5qqnV9AUvqzMwAtZ0-JH74XD10veIFhPDjRAK-ng6150gR4CYzI0vA1TCEtwbwJLdc7_4MGUn5Pe1nt3F2vEUpx2S2p_OeZqiKN4ucuDzYY9CKDV89FGYInSQ0feACHvmbKZWfMPLYe3AQGASHhKpqj19TqIrgLzZ0YXq4N2miiPUGFz92Z3g77DeIBuB0YkURdil_UQeR9gbi9CgzDwO3mZ51kAqjkIO5XRms1G50zCkW4uJvEaELkVdOLukMxJr38FtfUWFUTCQM4QL8tb6eHjm0pgSCcz1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7bZ0IQoTEBLKFSt_ykPA7SSy7i-PQ56YtgSZ_dG7slQPJMz3Dxu1K9iT2nNBo54deKWKlUYsO6CnX09CKEEkBWV7T3XmFFjV2R9_Z3gWruvw5zUbqD-acCGMb_ALV5LLx1saKeUzglFS0kQod_JSg3ieGVHdZ4dU0OnsgW4fzYte_exf14FIoeHKJ0nljPF3KC6U4RVrQd41rHHy8_iwaKJloGS6c3bPmXAOWxxPdCVOoduGAYqQKZziw0Z-c1tYFhMMHt_XY93HDvjoNqWatNWM41m6GN_hhy9B3zqLFSvFpAEsihmbqLnWUzavn2XOxOKDlV3rsfrNNIRVMQnJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=cdVyvPQxwB30rTw8fq0ozCAlZZsmLeSX-MIatJ6k5lH71Xo97u7wJh_oFn_RhtiBt1TDwpjXvVJzDfgxGGzM0XEG5N9JN1mlOPHCEZ-dpXmAbqIGIN8F21FY74tUGyX4LKFA3IocfU2-o59o5RhUL-KLKixS4CjU420P_YAPPbgUsKDWPZh-PDtqpbvGIWxAibfu2T0LNVRhIX4F9EdMWdgczK4MZrYJOvHosxhbcl7gcVlQBBvHHJA6-KMJ0kRguy3WCe_-aFp3fgMxoG3BS-VRgcNj5w34CGVLNaVYKr5_YLjpGeI0ZwlxjtT-RL8ji09IKD0JPqXoBCt7aUaa_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=cdVyvPQxwB30rTw8fq0ozCAlZZsmLeSX-MIatJ6k5lH71Xo97u7wJh_oFn_RhtiBt1TDwpjXvVJzDfgxGGzM0XEG5N9JN1mlOPHCEZ-dpXmAbqIGIN8F21FY74tUGyX4LKFA3IocfU2-o59o5RhUL-KLKixS4CjU420P_YAPPbgUsKDWPZh-PDtqpbvGIWxAibfu2T0LNVRhIX4F9EdMWdgczK4MZrYJOvHosxhbcl7gcVlQBBvHHJA6-KMJ0kRguy3WCe_-aFp3fgMxoG3BS-VRgcNj5w34CGVLNaVYKr5_YLjpGeI0ZwlxjtT-RL8ji09IKD0JPqXoBCt7aUaa_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNrHUmNNZux4nCbv1b9fOdUMQM8Mr0IS63E_TNHgBV4blpKsKBkcbBc-lYDTls78Cgv_LJZWg3pEkuVm4gxKe6LhhkUWaFUVm4vyZ6Eb6JnWnUyGuo0Dq2R9LXFqDFcOVzZksqnT1tWIFBdOs5AWQf8NRBQPA_rlv7kNpxIHSwiDrVBLFt8oVL5dQTwlHews3rzrpRY6URUTNGUKoyXI9PTZq-rh-Svw84F4IirHmr0ohYZBN67qWs3VFZsU6waRV6moQJgYBP2rTBx5MmHcvymLMP8HLljPIB5MKJoIzSVFsVBzO_igI1Lka2Alm9-AsDSd4fLTrqdHknA06P4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0hi3h4e1Iay1L4hUN3h5ogAi72DtPshfGg_Blm5vRz1kVy8zYBbs5NA1m3pB8YrMJuqJOoUQTlnXsmYsOKGFrifgDw1z0C2rY7jpoSabwFKOlqwjsn7KqxN9qTLJ6wttmXZOvos-xJn8F7H9sRb05VrgKg4oq2MsOVz9KSnZyF1G9GNNFLWX2vd3wjFQ4bt2pD0QsJWWL-zsCScPWVpMuiI4t-7X7OOtksp4QCGNdRQTkDJ-LWWiN0Csh58jIHzhAeDYKtlJrnX00VBrR8qhkyOvUA3LmXmPEJGrpi6hCUQ-z8LO0fZXFgyrRKIQoRxrYmdekmjuDv00UumaaHweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=nhsRF4433Z2Guw6low1ClcrBrHOzjZ7I7aT16hIgSmKc_14P_W3IkE6sY3AicnefmkCZ29VFQHlQhDhf2VggYhCTgid0WYmooTlPQvkf5AmFj1UWfGL6wE6ToN93_YR4O2oIBN-p8qO_gC6aE0YbSYIRxcgtxcQKzYMOq_SAh3CIydiLLSQ58NAaoByocLAlzjCKgBmlMWgz07oxMq6QAYpStafbmQ_npyYYt256XCSRg_Rs0hIrf0Kg14luk4v8Si9iX4_ELLaRvc_obdklYgpIptOM1IK8P7wP81dp7I3q0BZvaD7WC2ISjx2z9cmJaA0lPr-bP8GFkJL8Ih01DGhvsVP8AClKRoS7mRZI6pDRz_GC5TG5x-PlPOBaQuywx7Zbmj8OYi5HeVdooI6eqqWKwLW7R75HXCldfDud7KL5r7LDA4nKgL96U94IXxn5kJJnx_RoMENF5sUiX7yMC46i0o0vMrn-nMoIqxO6z6zrqAcNk_bx-buUNjyb5HZr1IXuFo8Z-2zRaOronf-1UDBMIhz_cC2PbpKSUUTsWaVxTQnw1IR9OTM6RcUndMTfPLxVike4We4vX9Ul4TdOv6Rtr-VZweZetI8DABKBxzP1PLzW_f9hGtcMqAWIYL6QRjfyvJTeOvScy6C6D1aG-7j3CyAfORYov0c6h-DtDE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=nhsRF4433Z2Guw6low1ClcrBrHOzjZ7I7aT16hIgSmKc_14P_W3IkE6sY3AicnefmkCZ29VFQHlQhDhf2VggYhCTgid0WYmooTlPQvkf5AmFj1UWfGL6wE6ToN93_YR4O2oIBN-p8qO_gC6aE0YbSYIRxcgtxcQKzYMOq_SAh3CIydiLLSQ58NAaoByocLAlzjCKgBmlMWgz07oxMq6QAYpStafbmQ_npyYYt256XCSRg_Rs0hIrf0Kg14luk4v8Si9iX4_ELLaRvc_obdklYgpIptOM1IK8P7wP81dp7I3q0BZvaD7WC2ISjx2z9cmJaA0lPr-bP8GFkJL8Ih01DGhvsVP8AClKRoS7mRZI6pDRz_GC5TG5x-PlPOBaQuywx7Zbmj8OYi5HeVdooI6eqqWKwLW7R75HXCldfDud7KL5r7LDA4nKgL96U94IXxn5kJJnx_RoMENF5sUiX7yMC46i0o0vMrn-nMoIqxO6z6zrqAcNk_bx-buUNjyb5HZr1IXuFo8Z-2zRaOronf-1UDBMIhz_cC2PbpKSUUTsWaVxTQnw1IR9OTM6RcUndMTfPLxVike4We4vX9Ul4TdOv6Rtr-VZweZetI8DABKBxzP1PLzW_f9hGtcMqAWIYL6QRjfyvJTeOvScy6C6D1aG-7j3CyAfORYov0c6h-DtDE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9uaKzjVofRyvzQiYsp3UK5XH8k1hCdn__GIwwGL9g-0rTr1pA0ikqmxIzXx_rN2opcyWIb-UHEk_yg_VCKGbiAC1QlfdTUcol2O8ijsE__ZvUFqGkwsSR8wmzTCuMUZvnBe7o_4rke-nVarlEPi1X6Gi0Z9f4EIuWoid2h4UjIwyL26R5bbCMXxT_vP2QXAumzKlF3IbKx5qagpniYv8nRDMgk1VjVQYUlRBUJW64A35rZdGcx-QdoCyFoDrzx7YYei8YAaJo2MyUxvWXC75A1mzRSWP5vZPUnEPhEylNEMBonGNVvSXbOBVxWedHRmdphgyw1z-WgTmeCLavmcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6oQhPUrTe-VfuYYoEBjqPNupFyNwheSTMAllw3_UlVqbb4iuI8KU24WqctbiebR5QYRQIyROPSByexQSAWLGt8Q8cuY7SJzWBxl1lTSYe9orO7-QDa1hnDZ4VbYiFtvT4zHXs8_zYcNKeO7zEEalqIGz8LNDGncXFj3AjZfj2piavtUpPltRTxJK7V3cN4qEugLRBhTdsp7DY0aHFtUXQK-MFT-7oOapA-C3k41MRirSda3OkhGNoblwtbqbQ-u2DXP_CqlqCjGu-QmjmpRssepGaiVSb8E62WcjXVhMoSJB_RGM_OkG1sfzWCqOcT4UsPnqTC9Bmep20fT1gzh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOXbnyCR4PtIUFstpPiF36zKcxZK_4j5PfkZfvLlI-_DP3jx5dZrykzzZ9JUy3XPTLsIGSRpIT1Ss5sN50iga_R7d4R_2XRe9Q1Dd3-zVV8USUq7qhL2W_7uam1GzKGQP5PsU0VOsat0VUg1vFLv3zoBcM8MMumnEA6bV7qPeXNpWcQ1lCAzQdJzOa2DaZrZ2yQZ18AoHgApZsK93HEh50Z24fxeNksYEPPJqZC6FHqFdeD6Jk1hAoY-vlfkrreRUMZ_HPKZVNsJCFp_dOM9H5FMzfXlnx9wUk-PEyst4ZoDpUynbVGM3mRWkjpF0jDiGmaZg3tHSR_D7ONXAdgXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjYO4wtC1sLqz1i-Dq_ZYGAMJJvWkPk8uGsincmrB3rPo4stDuaWjyNtY2XuyTl3PehvrAhgB5UoGOjggx5cuGlpOHrBNZLvu9ViOfyIkllVYQ4yUPlsqbo_xrKWWBe315ZbyoiRYtR7OyO5oipxdk3OuhIHPEjJZiPdU6Lc2WC5BUub6Z4zf4uvNCdYQH-S3t6Nk3NijlR_26Vqg8MF4VSf_8ul2zReBuQjNd1ZYd_jR5oc4kNQqXsGHsDyXp0BcfHh0ypPYIj_FtqwLHV62jDZI0dtIIBYAuAvnn7FdJOP2ERmhm342re8-bM1vgYfGiQHTXnjyYpxJwvnEQnZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYGTh6hvcD-3KK2GtDQ3PedrvU_vz_08CUSNy8L0cU3x55t79-HolSyy8eJKyzT2-Vt6-5DsxkMR-Vukhp9J-vKEpjeJtqOu1muXQRkFeDeYYflQS0UBk1lp-UxLrwGGBUewIr-rbkNOH7PUOa2eH4tbAyKE7YZgv7bJFKcacTM1Dla7PSaq5q9QejlMjr9Y0n6IxJqVu0XG0VtZNq8OQOCxAYlDcpPSROh8vUnmaJOWdlk09FQSQHctNKCBsmx6UPFHJ05AzS3TubsZbzCG_xAc8WpmbMvG-ob5bBVczxojoquN9moMXXQckZeZtIrFMIdG5aUZqJD3DlhVL4n80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=patbZj-Wo5e6mw5DYJgalU2sM_Gwx0zkohs12eQ9KNBgA5z4iuMxQO769dwFeTMr_PUtiGvXm-TPnKN6gnAROSZBT2pW2C07SrxSLBtAaEer4gK0c-5F8OUT2-rUeOMdOb2mEymWpiA2GBScxFSDYnPKxMgjKbZioel4gfbHf6M011a6SfGyZcTwp_gyAv51l4Mn3MRjk57ZK0VONS2HmZp0okYBZlJsWKq81-8no4NDd9t5wwy1WS9QFyAqpJG7PcKhFmDBiT30BrEW5MVoklyaICRso1QUBBxAo9Wj8yRINYZebekmdF2_AG_nUD6YztjJj_HirGhXkIMPkLq1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=patbZj-Wo5e6mw5DYJgalU2sM_Gwx0zkohs12eQ9KNBgA5z4iuMxQO769dwFeTMr_PUtiGvXm-TPnKN6gnAROSZBT2pW2C07SrxSLBtAaEer4gK0c-5F8OUT2-rUeOMdOb2mEymWpiA2GBScxFSDYnPKxMgjKbZioel4gfbHf6M011a6SfGyZcTwp_gyAv51l4Mn3MRjk57ZK0VONS2HmZp0okYBZlJsWKq81-8no4NDd9t5wwy1WS9QFyAqpJG7PcKhFmDBiT30BrEW5MVoklyaICRso1QUBBxAo9Wj8yRINYZebekmdF2_AG_nUD6YztjJj_HirGhXkIMPkLq1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUyWKDbe40cn9tTUsFRNBo6qN489Mtm3D-wBJi3dZswe8F8UDICJcvSGCCVc_WEbvT85R5rRPieNKK-blBn-jigLFILomiE48kCyFQmJ1zOMRpUD-6HYg3jLpPdV0Ti4gYpRWaCsx8ULfBNZSb0B-oBIxeJXcR2t7s64Aw0yIWgEaeYrhANLCt-qh2lCiFD9R0Hv4rK7DdEUFUz8Neo7RB2rhKtIlKyuDTMjbrak_p6_v81aYV9ZmQS9hHDPnAv0EVavcx_r_LL8zZvcA-8Dslt4-UFmcKVD044miqcXjsdkmLp5qcScW0nAWQzmKiVxg2AobnW7x6NkAth0-zCAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=Mf0UPDll-2Z_eWeyZUgU6dm694GASH6971liih-EIKzoGRlsOR785BnsrQ4KzfHb7AXuJYLFFulLz7ABmmc4nia8Md8Ur1lbs4nFxO07T1szMJVEAz8ZIlcuDIIn80Eyk4cVBlaC0eJ-JWEguIojrWfAWonMMrAeeOAAaxCPm8ngMDmBGHeVrGQwhmTIA1CjzHiyE6AhD7hrfCT58YSfwF2ZLQmC2GqSKTVAM61kSfq9xdInpFZTtQwdplfGQ5MK2gGtlp3-AMWD0YaWf8SNMCsz08lHQtJ4M_cfSXqo90OtiUNI72JX5P1Ebz8BWaTZR9pCje41MF1rTrrU--i6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=Mf0UPDll-2Z_eWeyZUgU6dm694GASH6971liih-EIKzoGRlsOR785BnsrQ4KzfHb7AXuJYLFFulLz7ABmmc4nia8Md8Ur1lbs4nFxO07T1szMJVEAz8ZIlcuDIIn80Eyk4cVBlaC0eJ-JWEguIojrWfAWonMMrAeeOAAaxCPm8ngMDmBGHeVrGQwhmTIA1CjzHiyE6AhD7hrfCT58YSfwF2ZLQmC2GqSKTVAM61kSfq9xdInpFZTtQwdplfGQ5MK2gGtlp3-AMWD0YaWf8SNMCsz08lHQtJ4M_cfSXqo90OtiUNI72JX5P1Ebz8BWaTZR9pCje41MF1rTrrU--i6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6C_hMyEGU0sSzXSvmOX4CU5lqa8NfdyKZLq-olSun1usu0t_3arP7_CMIH6vV-3U5jX9OXaQ1hRWDDXOnkNADpMeGLf1WZB7vQtU36m2y0gTrxZ_hOMoqOZTngAQBFk682S3t6pnazFTs8PqNeUMqmCw_OWtS1hF0LeWdguZTBso4UWDwQmSWGqiPvevRuKV7aX6xsf9awaxUsD-KgD00GaANBhIGgFXzXZ2r08nyobychi5c2Qw-zLgjS8UU-CQVn_ypsP4Vc73WhQurDwd_ZchG3x_F7tBbWJCyiorJLqBnzYhzui31SVX9eezlldpZYzVZXE0OWhCWG7FwJHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvqfNm2TcQ1mY3rwSYz9v2Xt5odoaM5a4I7h8L_TCcbf_A5U59O33jsOBmL2JbWlLnEReXe0B4U_genvAI1V2MBVHcPk11xXj0MYNOXlagus_p_udMx45fGfTTsh8-KpUi_PS2mL_ESG4h7eCjDbjUDqH6NkDNWHxhA7UmlzvOkO3fkBDi5XSsrDIFh43FpV1DaRElosjKHRMquBF8E6n4xRdOwJyypV2lcDgSAELVA7XvOxxfE_0jnl3LYt7Xn6h9gp94LAv6mXKtYG5sIvcq5pcoZClP0O1oSJJkLDz2oS7L9BrwyULPBgEWUVlal_4hdQYwRCnWBSJ1qNCLYIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAzx0d1V_ssChQJYYIfmYUVfhjI5VBteKQ7ASIrNpFZPhgDPuRYS9jNbNFP0NcMIxG02M0y1767F4QBDeIOWyCnex6biscLhlhz3OlYHPTg6d75CNy_t26YJEUkpk41GpeBEzISue9wbhRMTnOJcdORDq4RH0043qkTxGu-Y-JMMWw9jz4fHDZdDbKBSBPv0MjiEaW5trcPTgYTbQNHHymCmRVFGOVMeC0-a5lru2ESBN1WEt_xBsWzGMYXN-KBJIOaxo7yOg31hjOJdbrpVizkwtadWQ-XtIDN2ZIarDOfBRhClVNOaIVvthI9oWlUl3ZhNwXbOjzu6GgRqLGobwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRvUO3G8-G6bQo9sIGb598vFLh-5cCoESB20VEf7RDM74tkfC-dqiG-KUi4TfuzgObn7V24ccXY94B2U_14ePmBJCncdNpWtOrL-cmAq1DjV6cddAvI_F8prpUBOWqu1weE2mCY6zGZvXRJUthpl5ne-GLv_OeT_gBD_U9RW80PzxyOwg_BwRX6R-N58AOsoiURZsD7Ggslzm-OVu5JkGzbPTNI8pxMVXbl-2TGZlOuXLn5dIMwXaI13Nllgm7uTvTazZuv2q9EhyZVGX-9zFUiCjYON-0fpFSFs6hh2ONYYc5EIu5otW35H4WsUm4KjXZmoXzjn3eWh0t3KAIjNdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkSHoR1tpsBB25VRixD7MgV-pQrIoUYDqfKp_MO8KpbxhfaBYhko7zL-Re6p3Wl5q4ImQc-VcBu4FaQUIUPmQrttTtGSYkTk4EHFZP3d-DMocaX2jc-fju1cTeTFM99V5VrmWx8hVfX4giAsyIzWHrlSKVNI4f_-k3D7qT_3IGl3I4kWIDqkbz-DhPOcKPcKDJkmWkl7Idfd5yQzmqBQvvLLa7viriC4Pg2UnI68eJ4EnG9JP6a_kdQFcir8hkAtcsCqYDkkMZZqiJZNWJIBtI_CPC70jTMs_RQg896SP6zuROASDzVYtLhArt8A9D-cwa-Pf-WbOPAYBDzcLkR4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=Z6QAeqBpefeAbXw9jEyIHji9pD-LNx3hjNm9D-SOW1OXZYZ0Bm95wxzmMqUwWUMTXxDUjXqdTse9VVSoHR329iYmfUtHrUI7jsdLzrxkyZJWxwlm-J7w3dwosIm2nJN9D2oXw11ETzpRfN35_dj9aY9NbQVQdadXfT607gEXBkMzOLjsIcsrbiV5aEvCO_KG-heV1v6jcknFVJIWiqdx6rm-4Z8RQp5_u96SPYfPzJJyZcYapgH4rT3Lzfd_xrdSdm0q6D9029PGr5l9P2hjiglPzdFLo4astfa6dr8odrCH64VSzCTdYFH4xsulpug-ssHYF7EQKKZX80JCLrZw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=Z6QAeqBpefeAbXw9jEyIHji9pD-LNx3hjNm9D-SOW1OXZYZ0Bm95wxzmMqUwWUMTXxDUjXqdTse9VVSoHR329iYmfUtHrUI7jsdLzrxkyZJWxwlm-J7w3dwosIm2nJN9D2oXw11ETzpRfN35_dj9aY9NbQVQdadXfT607gEXBkMzOLjsIcsrbiV5aEvCO_KG-heV1v6jcknFVJIWiqdx6rm-4Z8RQp5_u96SPYfPzJJyZcYapgH4rT3Lzfd_xrdSdm0q6D9029PGr5l9P2hjiglPzdFLo4astfa6dr8odrCH64VSzCTdYFH4xsulpug-ssHYF7EQKKZX80JCLrZw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ1foeRy8of8tq2eOET6wsl0JYSAnE8W3i8jZ8gTuF01fAu54EcpCnHQRltGBLcDDI4WUfVkdy4O0YT3onWm5VEQh6hk9I29nr8Y8mwn4rl7xx_P0qkGJfXSjSxSMZChqDak50-zVHlonVx2KaA5NEEuucZssjs9xev_MPsQ9VVYMTvNeO4Ht54Nh4YOzdox0UEMkjIHu5jopLlh54ujcjeuXmxMlApic-GyEszGaHVUbwJHsj5F7kSIyqetTxbaFxydRz_ZURlpEQ2x6eEXBzVN93DAdDBMUROD0tGvAsTdup25_GLxSgTwoQTn3wigwSVyuT-KRoRqdbSSO7n9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVfQb-9Vsq0tiuHQV82no0Jod1dNvEbJChAEZIZxSZmQavx3HLc-M6YpjAMyrmnua1c1rx8CnBAHmAde1dm3zGk1yHGY9JMxbRbKgFfrn7PYEBDnoEv1atCUc1fy1ZRqnQRNZ0NRlcMGcq8ZqHSbWYsoNU4hL1AtZeF22-XRMbhb0K0d2mayd3iwblZfzx3ho978moerT2-4QKzTWbU6xo7S9ICdp_V08fHEBjPVSY6lr4Qdb4AMBNOQeZhKXuoNWYMi-6c-qdWQPuDYrf9UQIZwslPfz11pn7HSMILfyF44uoEStDnEpUp6vsPANAfR4UeRsBn5f86pqn_rmFg_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMqk4lexUwzO8ssWjzERYOeNC6TdHsH803pYSm-LgVIPEZ4PyLzmNTMS5Q6qk85AMETh3j1F4KerNYgnx2nQGN1sKfx1iGUtE5__LaxZUnoevNrmIrAEUpdzUqas6bUW5X3iVzgZTZi-5Is2YvdOKT3rGghojTI_dN-j7jaCDplSv_IZdMgZ4OKdiD1N34NIjkoxqTF7VQexXYYAy73HoKSeahgNRVJqkc_RhcaImXcUOUn1r4rbI4y5b5GNk_L9j6JmTLGXp5ELlmzNMJ0XwTt93mD-0ZCa-gyUimTIqZq14Ba61zNU2NzFu8b0c9pnLZDHHAQzy0EcdW0__irdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=WzFBYJ_JmX0OIXRnwLSDhRBUekblC3TVDm48KB2XaYzymWYVk_-F1Jq-CtFUVElbx38yOu2aZ7gKAq7aVgSN2b-KjzPcJbzkbSHzVEZjdVgQiPDWcPNbVhB7wHO2r2WAKyrKb4qq-zyzvE8AUJZVoyMdtBUePxxiaW6ug3iXgfAXkas0nrhb3Uq8IB5XJRnWFiadYcG6-Fshv7DtB1-JvAsjMuxke6oXGOKdh_0mrvuNbGxza_EVpaSVuru6bJ13z5Q6kFzpqswJUpwIytvCw21VrY2PykEVz4fk-8eRFejs9oYYmTGNqeWAO-jc5YEA919Q-69ATLU2LfLDmXw1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=WzFBYJ_JmX0OIXRnwLSDhRBUekblC3TVDm48KB2XaYzymWYVk_-F1Jq-CtFUVElbx38yOu2aZ7gKAq7aVgSN2b-KjzPcJbzkbSHzVEZjdVgQiPDWcPNbVhB7wHO2r2WAKyrKb4qq-zyzvE8AUJZVoyMdtBUePxxiaW6ug3iXgfAXkas0nrhb3Uq8IB5XJRnWFiadYcG6-Fshv7DtB1-JvAsjMuxke6oXGOKdh_0mrvuNbGxza_EVpaSVuru6bJ13z5Q6kFzpqswJUpwIytvCw21VrY2PykEVz4fk-8eRFejs9oYYmTGNqeWAO-jc5YEA919Q-69ATLU2LfLDmXw1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4R6rhP0REPGz_GkOEZFaztKfSR7t_xgmLXKdzPI0stwc_tbwZhnyUrmadEqtHWnj1UPdGC4lOWSUH-lnm100kn4chBI0C4ybBQTV-oIdu49WfbOwWavkQkRnAsvb6cqrMwUUbBYwO8qZRR4jKn3VBF01_rR7dsmeKk-HC4-XXjgynUkrjwsQUxwqFLRJegoxAQ5bJJOOT_-hOATRhfXDxV9R8MML2JSaw1ZsUwehTjpnx8Rr3X4dExzTdcyXkBqLiiHL0wbH-lLJp412_5MFCkw9NPN2A7-Th4PMebCIiyaPsyom7xKYZABJWkDM_JZbNDGQy5gnf-jg3LIYiyNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHTpA4ggtASDyUQy63nyTTl-y_MQh20qy3Ya_MVhDHMyvlbcoFeSuFwG2fLqQ9Yd31FA2egWkrcXOFKaOfwkR99Kj3rJ_4_h1qmA94BpoI2_IS-Wj07izR7wObqqSJSlyIIf9Sv8UZkZBUo20awEKgl6Ig_Ql1xxvJYugUc6dPI2Q4mU-IDsqWFwW8K4D3_SbU-RHbz-8XGkseWhqazhVEFyOM8tWXiDbH5TmiC7SZWgVosqfw8BV-ImOB4SVUQkwZOlILEbabNVwtuY6zhZTS-rBF62qd-6LVihwHbAAW024Js-khcRpO5Cvp5ab5nxeVk5KMBdvXMenoaDemz6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nszIoPmc8p_x9tpCy55D0yr9DNKG_REuUCkfn9LmHFI9mLUcTZCSAJJkp-0gCN07qp0Fgsz9uTAoMbcbHI3mo0CeQA6vK40FA8uKGNgLdOgr23wHPkuwx1a8MQFPJACtq_xbLXiMPNtHw2sZk4JATS_PZZ_KirbtIoyy3k693dk3oGhiXqfzCkYtAIri6DMNTFMHGEViiJiSnByIvbA4Wlzi7JVMNBpL3SYsdttK2TtvhpVj8-wW0ZgZ9pfn1WN8IThAuXH0e0EyJKmikQCg3odBXwbKQqUnwZo5w0CLVegoDdRI99NTV7bZLVj0IULkKs_VAzaiQ7SY_v4BZYl62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7E8Uj_G4YiXq0Wn-WQ5aXdUouXZbet9G4SdpLe3LSZuegedhewFRJz8TMRCtq2ddO7pBWUW-gBYbvMnzDFrLPXZ7t73Pff0Vo8Zo7Lq1sku0TyepIFfh6GwP1X2yS80m9RYZ8G5LHnhy-qkmFSPSSX6Ej8qp0FKCMFyTxkQYUc6YkjDE3SH25lyO6U6Cq37PgzqBgNWhvl2MnWzQYTUgHFPdukzxuO9vcC0V0WGpjsp-_r_de2FsYb2TYcENgkHLf8qMyGuBZLCzVR8n-X9Z2Yj-G6kV-z21pkU39ce1_ZEbOGUByHOhR0fwPZge1m0AfDjgC_8wvWUcobyxYE0cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDf10rCkKFYjWIBB3vTEUWX5Qf-UkMv79UN481Aoe7mETBsvBpYnh-u9L55q_jSsVl6B3KJfLX1dT1cS8Kr6hjXSeT2jt0uyTp18ZvI7WwrcJI_kiQncRkG9ib5OeriFTXZO6szaK7Wo-jz4OZz_xWFCHPawUiLrBXHuYLkde0nCzgXO7rkGfxXsJcVmxSDN5q2crAZ9dMToyzl-KWl9WS4P4rT1N0tN6Gs5CeuCtkhZQyh1fUZ3vp0h0VWJiMXpDxDwuOAaXufRAyhs8AtzE1rC0m0GolN2ga0CkpfmfAuuJpYFJg2WgnSrO1xUktPU_NlbVz-BsTLm6s6RScIT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm5hwo9Mlp_NnmjmyFe9NMGZQzyaw_I5QL-2gkWTrZnhTktE9NL2K3_J4erU3-S7SXzFBxbHo_0Sq2AcwMhfpNfHWIc9B0iVM4ZDpozhz01fuISAn9X3R19uOp9dIyb_QQtimhr-3UMbpdaobfBNhHz9se6A-FPhRaHYIn-CVE1YRVLcPO1M0kFs8bY73HiWcG3wsroGOMgFRC4KJR4yEIUYoXxzdhTaf2kWz_mVhG98gDFCy2hcxqfrbQMP_p0SEz99bQWBx51q3Za0wdsdfKOReaPgj8lslJ5VV1LxOO-PygrXpffBBHB27zehLXSuToQ59w5CHprOhT1wQ44FIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSnpMV1YNzBcOHVHGjBK9u2n6nQDdIsjulrI0ErUWVxm_x1x8cFXCVR4J59g0sfFmqanKEy8cTJThuStY44BIuM0yvUhr-v162ZJfW05M-f1QU8LbbP_Em2FWCybirqQYbpKuumlVQJxgxP8_MFoTb9Euvw60mNSC2Nt3jGDZaSLRhqXtSkW204K1ad7LVNFDUjgOSlort-bLg3bTZES8g5P6WMTNh4HKvG0maoFFYBg8TzUX8BnKBaip-VkOcvueG78nfUvdF7DTrMkhqARzT12ElOwtcVZXEpU8O2t8o5RcFXdWYrPHRfBQF952r-hFZvS5P1ZwnVn-QuK4kPkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cImW-eA7rZJVz73rJt220PLXlCKaT899diwZ4gdolirtnW7IV6jiZ3d16pr1Hhu5VkYAcAVKwYcSfhkzLDebQdLetf8gzDc2sx_FnuAYAyuSNmF9IJD8hXYLarCSGPRwBjQWSPhX6V5MFaOLaIzCzotuB_QC8ySHoRHaUKgYj8MjG39mNYfJf48er5eKAJ6ItzuvzRbp5qApB5D0C81sxt2SLQUSnij1ql_bOGTta0tXeJkB2V46hdfcYL4aofUjayLuV2RtaYzaVnAy10PkXAlRjCO6b73hAnn4-ipi0ao-WfW1mUr8VvAdLRu3sjBPgWzuUm62kUrTSxMueXzHFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=EGhmECn5_3Ssy9fHMm4dZ8V5S3aZcI3VS-U1pOe3uuho89RjR0zWttUhZf5o_Hj7TjrT7DlYGXZcAOl6UUS2Msfi8m8be4kvoTjTSWiOsvTHQ2Mp51dEWH93m1sBBWSO0PgnsKpNohl5ngPJD33Kr6MlgMXnbJiSV2KHuqTVmeweVvI_pjshM0rmYu4SRtes7k2pw6JfWvKQXvm_B63sptMUR_Z-AHkXDBU3OzCYFYhU3jPa7qvV2h_kq1plrlMtWlSwjbsVCkEP_IhCDASJ49ABTFsUenYgI3HbnTMAPp8glH4RqmOZwsYs0XMdR157ZF5yDB9I0j6DqZxh4OobE4LqVBT4xFVVQNXjwc9GbHHMb-PwZmNhdXdtdF3YUzknc6eISlipkXhcPLW_30RcobL5PAJ_vrBS7jqLSxZnLqCQTAfJpnZnCnSrcLTUDRpdeBltopukF2HJ_NB-L_t3-Azo_pAZIaDNO_rskoZGSM9Kf27obILWfR68GU99s9xK8bMexRXzKDrehYoeqO-OONuzRRX6MVtOBQ8-VFM6A5SOR8FovzqFVkY6Kog6yz8sDSMiUi9Z57xucCf9PCK1XpKTB4Qu7tRaII6g95juMGpMVIwbh8i2ysywIA1MTQBxsWvkgV5PxV5B0ihKZMAFlnXVJ9qEt9ftlREySafDpVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=EGhmECn5_3Ssy9fHMm4dZ8V5S3aZcI3VS-U1pOe3uuho89RjR0zWttUhZf5o_Hj7TjrT7DlYGXZcAOl6UUS2Msfi8m8be4kvoTjTSWiOsvTHQ2Mp51dEWH93m1sBBWSO0PgnsKpNohl5ngPJD33Kr6MlgMXnbJiSV2KHuqTVmeweVvI_pjshM0rmYu4SRtes7k2pw6JfWvKQXvm_B63sptMUR_Z-AHkXDBU3OzCYFYhU3jPa7qvV2h_kq1plrlMtWlSwjbsVCkEP_IhCDASJ49ABTFsUenYgI3HbnTMAPp8glH4RqmOZwsYs0XMdR157ZF5yDB9I0j6DqZxh4OobE4LqVBT4xFVVQNXjwc9GbHHMb-PwZmNhdXdtdF3YUzknc6eISlipkXhcPLW_30RcobL5PAJ_vrBS7jqLSxZnLqCQTAfJpnZnCnSrcLTUDRpdeBltopukF2HJ_NB-L_t3-Azo_pAZIaDNO_rskoZGSM9Kf27obILWfR68GU99s9xK8bMexRXzKDrehYoeqO-OONuzRRX6MVtOBQ8-VFM6A5SOR8FovzqFVkY6Kog6yz8sDSMiUi9Z57xucCf9PCK1XpKTB4Qu7tRaII6g95juMGpMVIwbh8i2ysywIA1MTQBxsWvkgV5PxV5B0ihKZMAFlnXVJ9qEt9ftlREySafDpVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tztnHNcpvRPQIbLx_KH9x3_Uqb8yBzNDzDO9HJbIDoDtGer0xEIlTPciDnd4PqZq_EaApi74rWKumwhFpO6ZDLEJf5mUjxpUApeUafthNmFC1XAwXdetzwqAN8hGN3Kizl1SrJm_zxNO5ovNlN1T-E-DEVp1kWKq6UESAucz50J25Pia79T-kScB2Xm3XFDUzMhZw0ydxQ9PVqyHZBs_1bJSuEV-Zfwn1T1FRDydFyyr5IyDV99fbOsXQvCUHKnKl4-USa00g6BL8fJO_S5Kzy4AQ2S-AqDJWpsYDx0ciHAC07H8nIzF4lSRTxBNulT1_UWrlb3XHR9nttmyBltA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHoSN7UywlTD_2nirouFKCC2Y_PS16mzwQPmu3dojmfLxXLc07O1gVJ_3zM_kM1CWXr4oJT0QIWuzwpzCQwRvLQDqtPzVSbNVUOD17gGP-Ibo8wM44iBLysWzD54B9KIX4OCgY438YFB2hO8Yu5qEI2z_tcFJ1U8AMfmVRQQhGPmx-btCXcK44fZjoENPFGyjFASQECv72AKmXE0VgHacrswRQa7LUWD9jHbz8lnl5y73Uuk0mF5xM9tMn-KrwQ0Z590LvcAd6dCNY_3p8dYnJtxp68LKG7sSsHMaQBSO0h7AH2aW0NUaoJ3FdZ1aFns5e7G0SFkoiGgYUn_FEg9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfO9JVLMM-SrsdOCvCXpthfLucgTCaXJLASNquwGLolwE_ep1yucFIACjQoyTGP78RqlmY8JQp59agXY4ZTHHu2J4Wjon0llE-hi47PxMmPYbqE7TMON2tz29g88NUcT-u7Lv2Ig_Dfyfs_-egMutU8F9VFA2hxgo08cDIx-shTtK46ikn2rV-aGUMmTPfu3etdosl_pI_OTT0FSTzplnN5swgulAjhK66cDV9gjyD8t72IVpUgmopj6DQU4o9-f5fpYn_z03gdyoWQsZXdSDlv8qXvGgfXeyM5qfNHOBwK1-AhbifO8UeJcrmQoBz8pm8LRsg6owhipn6kDvHTY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W17FigIRDrcfn2Fo4uIHkJwKMaXwz7RjBHSvHi9G9efhhsHfUE4tv80QR1ce3kMldId5anA_o8ivEPVKeit33pm5jctnyvwjQOMDsp3zMBmWlHcJUnmTbHASHn8D4_9zwyYb1Vyw0XCljEe0QPLGh0vmdk4KtfTV37m5nv2yRVZ72biUKaw1fhil3bDEHDpm9a9v7VAGh0erK1Vo2S2EwwnCUaz-dz5hEpF95q9BqqQ6EfNnKif42Fxw1G7oTm7aE8SWufIe3oWR5U8ZYZAKX5UJq8HM6zkJA9njsMeJpOefW2bmedRZWcid_607dinh0Tdp__QByH_6hmlN2NEHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=B7EXLfY5z_ckNdBXqFecr6pQPqkN67N4zd3baYFgM7tRV0itUt6dY_6I8pdp6Xc7tczxcsqEzsOg1L2ebguGKuDxR8hOOAy30oFGjfsbrswRCSdSSEoJzHqp_-qUMwg7oP1ur4HkxWujU30X52e4L7ubCLlKuxzm_AfAfh61ees3VbMlpZ6Dl4wMEaJpU3bcRitG_lZ-V9fcgxJH4GSCMT9FXAgHeP8ajMO9sRNTacNV6yLkqkra0jnJPBUzToxRYnXq06glPRFueGp_0Fei0m_zDWbRYemxl7-vfQyQzXGxySUd9H7lRiyO36j1b83ZzXkM_9Zj1Zm_sDQtWk2UAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=B7EXLfY5z_ckNdBXqFecr6pQPqkN67N4zd3baYFgM7tRV0itUt6dY_6I8pdp6Xc7tczxcsqEzsOg1L2ebguGKuDxR8hOOAy30oFGjfsbrswRCSdSSEoJzHqp_-qUMwg7oP1ur4HkxWujU30X52e4L7ubCLlKuxzm_AfAfh61ees3VbMlpZ6Dl4wMEaJpU3bcRitG_lZ-V9fcgxJH4GSCMT9FXAgHeP8ajMO9sRNTacNV6yLkqkra0jnJPBUzToxRYnXq06glPRFueGp_0Fei0m_zDWbRYemxl7-vfQyQzXGxySUd9H7lRiyO36j1b83ZzXkM_9Zj1Zm_sDQtWk2UAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olHEPjziItSbaTHRbHCT6sxZFUIPMW2LV4M1_G5f3lkC0mt21cQZpcno36-IM2qypoTHh8UVYCwmx4W1Mc-fiPSaGEZX6BKZ3U-mRr1Z9pnhc_6URpmoSSgKgQJuVzK0sRWyrx5g853XXtqnItgtXfY2CTt36lZDfJuEPtKjHGC5KfOnyBMW8kkf7T7fbw80V7OCTfpIwjNLg035M2Q3zAiT7FXHuQVPLTqkNtp0xB01VjW6H7ul97uT9Jpx2VAqO92v3fLH_6WASUyeoLvSw-gWl9ROHLPYjewdpxqjj1s60H4Cw6re398q5ZQCWHB04jI86aqLuUVl-NZPk7o2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqpnKo2kjLwOPT1ihKIf7sw6lM4vSGcSsNQkWQj6FYWslE_tKqww5pOMm3F9FwT1JofjKQaukDs8MtVFVKc_dorXzFVFwiNKUXErQyzYeSEFDApPwfNRg5_xvd6EM4iB70c3219q7zcrH1gMt87y9oh2zBU0XBo_ePljXAbLi7M1rsAKgV19fGd0w11UYi-CLMAT2D-Esj_qFNNZLlrAWfAUcj8NIv94sLX4ona8Vh3EXUN1hjBqio2DarbFW9DhCu2tpvMFxPRlp532irefAlF4PvYXDKMfhIIZ5FqxsjeDjrKbKU74KyKXVil18eaD8PbhWvN6qw4TC7rDUCBTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E36lzMartqWjW_4gWMyWWPD3oT2hKqWYW4UGvuBcNAA2fQNXgZMF297IXoiF-mrx4cQacCpGaxyB4h3ysYdUyCQQd_DAIjpf76_lNeLewhPzLcnXlxeNfB4P4sbh1CB0s5CWRH1scyoTSenIBDHwyht5JdTSX2R3ZlxeUr178nc-hsUKssZOZmroZjBayRuvhwdThq5Xb_ccx_3KXgEflqwxF1L-jWEONvzDo4A1MFoL0bQXZkjhrH5sP7MY-0CEYj6LCAX2metSj2rt4Aazgv6tZeajYOhplEKeJBFJINJ09-OhnFW5h3KiSFtuWAV6U8lLNmAf2UCmrs9d2iCYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUEgnrERHWNEu6bI75PXFzz3hSp-COV27K4uGOsUCAZeyHiPdffQYUJlSlX8QuSPw2v6ydTpjHp-Zy9cq5prK5V1yfnvchmTB9xKdXRQ5MFaLHd196RYMRW50e3AHGAffbmDkVujY827gjFmy_zAX0puHgOU2wW2nVXwM6R3gJhzkVy9G3ia4x1gsHTknbS9adRn5kWaErETnckSh3RabisSsGTL4BvOCe9xI-wX7Lv24MqQelyt_3Qao8XggRpwYOcbYdmv4jk-njzY_tpHsIREd4JwXmniC9kdq4CLwSDb8fqle1DePCCWzqPPppA6FOLMuibfWNXGiewUsgCS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzLReR0qAiHk48eYYtsF_9qilxgKD99dXup2R_6r8iEbd8cWlclwspHpWhF8l_LbOt-LudUS9m_vSU6GvG1U4qQhO8EbyILzL39K5kjbml-b6Si3T6d86UBzkwo2sHzlJEKZ7a7SH4JaO7eGVM_0cA37D2vz12o-1V5gbL1tmb0s4xBxaiB_eq3rxeZw9a1jyoHr4CyiybKu_CF9GGWgB9FbHqXIBGVdD3-ANwpwNj5zM1HTzyKmQnicIbuHSoNiHU_TZSmi-YdHCSDsa5ri2Vd6XBBgD71RDl3fN7yhLcbH5ydn5Xt0B--jVWX8YrayeDYX8smK5-lTEnoV6hfU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfUbvf8VH_i5exgI-zUwaVmRPGoq65hVp2Ru7VosmpU750JvQrDSnOEau_aJwmoe2hEPrS_Xqb5f15w_veKinH_THK06MykDUs-VHDzdiey90WSe7uj6CImF_-i8_KQWFmHQDDpjKt_dZfLeKLcIO7DpaF9-j0YdSDjLUD3p93ZnitNJCZk0i2wBXY0hCJV6W2qvfkObPyuVU_uN3KgwUSWPJIg9Atm9GqKqrI34Lde2p7If3WwyZVT0c_enMOCHzqc4SCrCiIzT5-MMFPZJQMtTrhVRYqXyPEPjh_6haW-rKVyQJMe8JedNjPg5AXac4PtMpHonrLfJ8rYBzG-xkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtjF8nFkxIX1CFknDcAxgc1fF5CLOeOKH1wBGtBJMVxisBejZrIcaR56Q1kEcq0Q2VzrBkEMFvGTSo6hRprKBI80vVKvrOfjZqX9JmFpCICIJJpDEQrHUu34sq2Y9NgsAw-airV5ohkJweA5tBdmfPTCc1e2iEZGo6yVx5sJCq7NvMNoSw19mX0Ngw6B3KcvupRppFldz5sco6UFQYRcdD-GhSuElCqv6OpwAydzq8LRGS3r-6MsXjiOeIIuWla9fNTnqdbIEw7KN7teBhp-QY7YO4-eQ23GncDGlZwGOkVMbniJ3TpEtuvGVqgN3NTXA_xf4tp8o8A4XJixlLCc-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL-BCs7b8kuto9HCyEmf_-qftIocwMLK1VZ_26lGV2A8Vs_Jk_2-LqDM2d0z7LXP7XWxF5rqFSPRIswnu3tFijkqjZtkmW0eH7shNxX9MJwVpS3KfAJNWiltiPRfB61jfViQrVljExVmHCw5jpWYsvN22n3t84FoNNKiJePnTh37uQky8vBQyu0mSbpRsohlnb41d-L1eOcoQZ8C3KMws84BOY6yql_lXzwg4wIO1WQTq4h5Kq3VmTXCZME_EVOYeTh9ybM7YgEGCzVvtZx2M68nqksKjqy_5EAKUaiS0OIOelNdaDn1h8EgMA2wBxKsji7c61cQZEbfo68eqtVcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=NqBUqRtwF3yneAvQ2SquuufmHvU8iMIHTwGB5kMkcTEzZal1Xs1wOSjOspf4GBSTiQta0oY7f6FYYhwqP5rNDn00-5tCTWt1igNqPQRChQeCpcnjxs60Zo0bMoaz4aFgsKBCPx82UvQ7fMp7jfngmDfIBwktQFYnK9Q0PuK64S89JrCprTLO8vp261XsQPAoeUS9gtXPufrIztFvioryg2FXZJ9AEHo6v2HF-cR5Rr5b8SsnSlcOkDw4uaK1VT9Xu-N7MFbNrK5ir614Aky1Who56NmnnsO05Wr83DkHJjMpjutnzrKqCZzp9hn_Mfxc8ekuuCA68it6siR1hRvjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=NqBUqRtwF3yneAvQ2SquuufmHvU8iMIHTwGB5kMkcTEzZal1Xs1wOSjOspf4GBSTiQta0oY7f6FYYhwqP5rNDn00-5tCTWt1igNqPQRChQeCpcnjxs60Zo0bMoaz4aFgsKBCPx82UvQ7fMp7jfngmDfIBwktQFYnK9Q0PuK64S89JrCprTLO8vp261XsQPAoeUS9gtXPufrIztFvioryg2FXZJ9AEHo6v2HF-cR5Rr5b8SsnSlcOkDw4uaK1VT9Xu-N7MFbNrK5ir614Aky1Who56NmnnsO05Wr83DkHJjMpjutnzrKqCZzp9hn_Mfxc8ekuuCA68it6siR1hRvjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vStqkUTeaeWGxa6XhfYh7rgqY01Ib7krIzPVJ8AJO9SW1Dw6khxVuXeEc0z_xACusyECm0wCT2feu9bGAVkq9AUuTs4JONz6NestRgn7ETZQSUHwLN1NuD43jlICaGHOIaFTwDckTkIS567F8ppM6gYYpZ7l4_0LghubghHK9u83hk4U6GueKnyvR4bABR5XWSKdWPNAdqH6PeiGsHCiNcf6sN9a957KLNrtLWI921s_L59HT5D07R_o5lmk6aR2tEEzuDgu8iA1ufJeXufTaIJfFWYbMqKolgqEJLr4PwN17zPdfy2upqxXuMQ7pZqKLqHewynAjgrbpraWraiX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYzd3wbhc1VdIDs2B0WTi-6XooWSh9ZJG2N4XY7ABbYcngWlte7ALzJCY-AIaRcqzC4jmygcqmyHmM6KS2sFX2jULruqATjRTaLS6d1ed0xjcSi7OchY637WjZvVgNGQvgzrAsseInHEuAuflgEmeJpfs8jiFmMo0-Gle8J1-2PNL4_tb1QgLdsPbWOkWpNfw7_fBgXx9QNphFq21o76mGjFpVpAlyYmZQ4ZpLtDTThvZIjZ_xlmx8t9AkbO_-T26bYOk69sJ54apC7Ud8PNONS5ms2X8dMgpxwJLHbpRQ7ovhggaX_5RzZxiPzFAQkHaJXDwQ_stXrhYPtNylZqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gag7ADxMhV_SvSO4pDWRTnhskurYNz8_TOGPKrtBXOK0gxi_J0AQJLu-mkZXL51tKPkuBhjSctLWw95Hn741dkJjBTjA4Pa0ReyC_zYWRm6geqxgiR_RDhRO59j4h91iHiY4n65qcenJGLhO_8bOSiAxOGaLd_JN8T0kChEXsgG1uOrrkRsRdzJ18L7wIxNwHWEW7kHD3sEQMwr9Qu-jvbf4QdSNlbV_CAEYyVJyAhklqNCw0DYPGlxn4hki4lqSulkcsPjBifYepnfQyERtNF2zcHJY3B5DlzFsE52Me_5Z7wn47QQL1V3-_pYMZbzxssSBl6VCLqO85jNfFf4cZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XU4nlZMTevnDQ92gKRwS94j8KgofmX3pxd4XAy4g73FZdObfShFUYgTyRkU4S6YLT3ELkG_jYDZfYoWzv26OOh2_3qxodHjd_5KOCaWvd6WYEMVT1LlF2C7WYyoOndMQJij8HaFxbMRKFThtUOr2zaZf1Q2EqyeLVJniMqtxQ-7SRaKUETZu4LKarzPbiS_bSkaoeI1A1fKe_Kf6J8XoJer23YvM4CF4A7PjQu9hdGWzVMUmpDDaGEDD7R9Md8pHYsA82gLgCclYarC1aa755P11Jdv0wCGktzPujdpANGoyp4KyS2VEh3ankAwUT2yDRlSnRAS_kYVeV833wW8haBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XU4nlZMTevnDQ92gKRwS94j8KgofmX3pxd4XAy4g73FZdObfShFUYgTyRkU4S6YLT3ELkG_jYDZfYoWzv26OOh2_3qxodHjd_5KOCaWvd6WYEMVT1LlF2C7WYyoOndMQJij8HaFxbMRKFThtUOr2zaZf1Q2EqyeLVJniMqtxQ-7SRaKUETZu4LKarzPbiS_bSkaoeI1A1fKe_Kf6J8XoJer23YvM4CF4A7PjQu9hdGWzVMUmpDDaGEDD7R9Md8pHYsA82gLgCclYarC1aa755P11Jdv0wCGktzPujdpANGoyp4KyS2VEh3ankAwUT2yDRlSnRAS_kYVeV833wW8haBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=JJJ8l2CDDXugkCYRlNrllR48Fd-_BtFBMrzjPhCegQCwAJsehlzChSqixzwKzwEcxE6PIp1qPcmIn2LdPH6o_PAWwRl8qd69lWsObF5cxiUFMw2BHOVU4K0ZdI66R6hIn7xJSU2SAvANXwtwsB8ZbYh7gf8SGIew86IVhzuPGkFmPSwamMYduhZDosVg3PHdr0XZLx1ZmHQ7M7TntNS853R4PS5PQKxDQ_hLNikh0BXgYWsM4OqC57-96SqHE9UCEkel12xzse34G7-BIp91i5-co6sBayICRB5Bm9Q4SE9jOz59ZKrg8jd-j5-Xyj3q6lzjCwhOuApIzoIxFD7qpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=JJJ8l2CDDXugkCYRlNrllR48Fd-_BtFBMrzjPhCegQCwAJsehlzChSqixzwKzwEcxE6PIp1qPcmIn2LdPH6o_PAWwRl8qd69lWsObF5cxiUFMw2BHOVU4K0ZdI66R6hIn7xJSU2SAvANXwtwsB8ZbYh7gf8SGIew86IVhzuPGkFmPSwamMYduhZDosVg3PHdr0XZLx1ZmHQ7M7TntNS853R4PS5PQKxDQ_hLNikh0BXgYWsM4OqC57-96SqHE9UCEkel12xzse34G7-BIp91i5-co6sBayICRB5Bm9Q4SE9jOz59ZKrg8jd-j5-Xyj3q6lzjCwhOuApIzoIxFD7qpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=bX9vm8FbYB5YN-qjx6lFIgPHl_Lsx8RMVMCf09s2pIV-Q_eZ1AWeUKnt1TEVtfv6X3jt74bP_PvmUmeBKdkedZCurs5mWiyQUxLfX0-w_IJAJO8Kac1cUYA-qk4SfFx6VnPT6gm_lMv3_b84RR3FKdgACs-LTaliaZwUBp-unR_H9orobrXaV8Z24NE_FjpbBtkiOPpc-uzL_w5_qgHEpZSZg1c7-9xta5Eud49k-DSTlPZUfmz69B0udVke1VsWFrSg64iNWoJeNcjadzk2bhZUHDnSIMLoQHAa-3FaGQoO5qHBW_dNl-nphKnS6cyuyDQxxpFf_jHQQfXL-gMfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=bX9vm8FbYB5YN-qjx6lFIgPHl_Lsx8RMVMCf09s2pIV-Q_eZ1AWeUKnt1TEVtfv6X3jt74bP_PvmUmeBKdkedZCurs5mWiyQUxLfX0-w_IJAJO8Kac1cUYA-qk4SfFx6VnPT6gm_lMv3_b84RR3FKdgACs-LTaliaZwUBp-unR_H9orobrXaV8Z24NE_FjpbBtkiOPpc-uzL_w5_qgHEpZSZg1c7-9xta5Eud49k-DSTlPZUfmz69B0udVke1VsWFrSg64iNWoJeNcjadzk2bhZUHDnSIMLoQHAa-3FaGQoO5qHBW_dNl-nphKnS6cyuyDQxxpFf_jHQQfXL-gMfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
