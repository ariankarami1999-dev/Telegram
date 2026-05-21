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
<img src="https://cdn4.telesco.pe/file/iHZPG5sPno5UTzTIzyfbUkDA4CvB7eTIXAWUQBEuy_4yEmCK0E76BzJEs9GEi4reO8e0DL7z79awUBObbBJhmqyJpwlUNEv4FdwAQVP1thMNPgNIRzvrMoyBD885duh58vTTrQ9bpj2PImrUfsP8y7WxiwKSUOwMhOczUSlz1INwUBPdC3Z-vvjEsnvjB-ajimLSYyCuHjiNR4Nz0AnN3oexb3qFtrGfhaptYvsDomVAfc1M4Ezm9Ln_EAsq0s6_lIt2PO7x92GtUJgA0kf5yKf2wyHOls_yBJVwRfaoYwq7FbM-0abprQJhXshwu13wLNlc-X8rX7nk4Pde4jHFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 200K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 22:24:13</div>
<hr>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4yGsyvptFLNMWGOl4v9acUO6qHC-hpSPttlwkQV2kTNVejJ-RveOkEWWjxp0PPnIupEnyRoZEkWDU7qZvPUnCNVee0BD8CzjKeVbybwF4GahjqyxesuitIzJ1tuZqgcjtYB2EJVk6jxjxD9h_aeAtGouJ8JKtQ6UvPS6fD1SLbRrhnVsW8xxGRypKtvWq3TF_N_Wq0bIekeE8yEzCSsjx4zrDs_asB4CIkZpsCveBPuW3l8zOXpq-WjtMi3dzlbuzs_3Lqi-wpD-elMWGkE5cmSxErD22IzMX_jyszM7epnppfcMtrdotxl3zxqw0vRGcFux9GllPKNeVvgYNBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
آفر مجموعه سوآن وی پی ان: ( علیرضا )
⭕️
مخاطبینی که 10 گیگ کانفیگ از ما تهیه کنند گیگی 185 هزار تومان براشون حساب خواهد شد.
⭕️
و مخاطبینی که 20 گیگ تهیه کنند، گیگی 177 تومن براشون حساب خواهد شد.
جهت خرید به آیدی زیر پیام بدین
👇
(
@alireza_mosve
. )
⚡️
𝑪𝒉𝒂𝒏𝒏𝒆𝒍
➡️
@vpnswan</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6J1Wbytal29L_FmGPKtA1th7RJ8g1vI8LQQI805zQI5oQNVsAlINsC_d20YmiS0nI1TYR4tqVRK1-V3eg7e2lIQ_ce1B7lCm0JPHmtlp1ypvA3QBFnAmSHiwelCImc-Fo8VL8ItYsJscKCIHhz1RncU6VpbNM719uD-xbSWtsjI8PwcVVFPp6BhgX29Nb3UgGSmr839OhhbP_iLfpNThMO17d2G6cZK7ey6teNfZq6jjq7wpeE9E_ymTfuRCXkMZqzKObfyio1Mq7EX8ldtr9UNDrXjRuvhkwNi417FWEyG10OPHx7Ti09xmQCDIPv7O-ksdLKy3i_Vbc3i2mh2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuvaL50hQz029fHOw8BvuWiGKprXQoMLEQ_XrW_e8rl5GsmSt7Oemkt9xtjD-CLQ9MyYD8LB5DiQShhDroQjxf-ZnHmM2HZ5i1sVeNmkaDtsPawSEC7syxg9orI0Segb0l4Tpi4DuWEdVOdXU4dp00PGWtddcpA6tDQ_O0g8-CSMTG8WuiZMKgWKuO8dSmweuZrKHtDj0iU_NfFLgzN6VPiXrknNCSlVbwgfQHPyp_Z7M8ieFo-0z1f-n5uYtdgg2Brj4NmXvoLUQIxwj4xvzpiWQ3WGNIZvsnn9IzvHy3meWFhHzSRsXgnV9K3Qtcuy8aOpXql6SzdL57VizU-rwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Agp60mS3lijaB8GFLTcYL4mbQVXM713VQ2iBV4oQCTjeMudxYu91vdJi7TJZ_jH4YEUuZD3xSsfBd_KW7x_lboyY_TgeGmCzcJXqc8ims9txd_04Q8VQ7cYq1TohAkUXkOXfptswJ4kjbLgQGGXdrrtQcSRuIHiht9MIrP3rB-K1u8WcwfMqeYUJjj2Ke2LH6_VJCJgKcJA7uPl4CmQGb9M8X5aMotOm8d1CCeB67vCgMNQjJBNbhyKKdVAEsZAM0ZSB9ISxCNG3o5wC1J2GxgqZlVxi3mavkJZ4ClhZXGlw99KIupUgVGE4ToSVry7ITGLlvzSOe_n7xD47-7uVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r31
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/persiana_Soccer/22212" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqqQ_ouYSkKg2MXRo0bFyy6Momh5OKP6n-9Yy_fOJU6YZU1SZ5IJXQ6MYblEmCEGIBmK5jGiEQr2eZpwoZQYVP_aygYbsjywaf917JpJDNLIFuZa6jJ39benD4ibInAyHrWEJ9h9ajjnJ_D1Kzs1J5iNgHoukJbn6DfwBxX31x20VdWsCEt8A5564n819BhElVsjWjbAAsowzdpG5ohYCfg3PqesKU3MD98emwIGYKkFBsD5hB12hcDv74wY_H8S6fb5N4CBRb9FVbhxT75YA-3D9rjyhWB2Z7yv5TJiWkeN9PAfNGjBmNj2Y-tYI8OEyS9m5NV70-fzZYlazyhiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsJ9ZhBpJiV4G5f3rlk4MbYvUl60ITqt7J1RAFAsTMDpeGpy7isF0QF-QIcyx_jX7-_Jk8MTgHZ-uk75NGa-HBRidZNBivuS-fxTM7FReaslZJialScVuflWAefzfrEDI-5ZMLYuiX8XbervNAqO7S7ApbwgFs4YwGse2sXnb2CrFncUawWP52E3A7D8NFaqWEIUQzN5qdQbsjNImm3gjV5rYehKav-ZoRlN7-g0bMzyRj3usWO0bUtl_GFJPdJqfGPyM2tQjAc2gj4lAG4H5ypnyZURsKpSM242dZqWbHhzPPJBRwIr9AiGhHlIiiKnmBQyIXjc_SydmXHTXxR5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYwoNAkZmSlOv-mjQ0sKZiEIGBPPM9aQRL2kNCoElekUpIA3YPT_Ktx4DQHi_8zdiwNmysd8Egrw6XXbgLdnga04ds3hEaYzST9oaIRHFkbnJ0A8dIF95I9IOXXmM4jbjQUHLPvuGuFi0i1pl8DMhnw_kJlHKvKA-UbzOF-XEd47qSLWjn5t6S4qLVLAR9eyMfdgiR9QnaSBiAJMDF7QVgd8mTTSUd1mV6zwF9c5mQTHmEY8vu-joX_Sl8h7z2XfkPaBfgUGPY945VcXgSu8M7TC-Dd5gk5nwoBuJJZk5YvlAk4lSpELyw2oqH5_oRofIW7y5w9hA6rIW580DVEB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چنل ما برای اوناییه که فوتبالو نفس میکشن
📹
خبرای لحظه‌ای تحلیل، حاشیه، نقل‌وانتقالات
🟨
مهم‌ترین اتفاقای ورزشی پوشش داده می‌شه
🥅
یه منبع‌کامل و قابل‌اعتماد دقیقا همین‌جاست
▫️
https://t.me/+XdSZ8OmU62QwYTU0</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQKikkMnYymvvQ8DaykMmT-qnOT4HwhZwk8JEQPLZLXHOM5eev3h6Xumi8vfzKFPVX8BserfnvzpjCiZ9YDzWj4FlrGaoOd1qvyDOxIfyGgbM-dgujKKCLJMF1pbtwrRDINgieVnyBym1MmyNhYxcnvq_feZ7ACiaMxzBkCLf7NEcHKJzPoVX0w9Md9EUbwrdUfKYxoSkQEUFt7-ZJm_xerqlhLPgi9ICXJVv0Cz4pWtM6Cm4A4J53ACgxbE49GIiKizq8jKbyuqemDe3K1kzN6D7e1pwKwQHuFJutsT6HWr0nnXYo8-AGmo71LifiE6YQOfG9Gfkjxt-nuLS_pfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJwLasdgcIA5NBEpOhkOqwCcMz8kAEMLW0qvw_I-0DqhL1z_U5OgrM-BW_rlc-032YDaFyRmsIE5wmwXlufFo-gSkMvMBR1rcvwrNXCOdWuho0EmfkbYmoWkXyNm1lOF4I0dIf65xaib-rAn0_rHpuDtvQF17F7yeUGs40srWgh-WcoLdjNSohfXt4YrvLwUnVSNhLM3NAR6deYlPN0MkbLIghXRq2XUxavkmz96IiTKBJ-dnpPIrbKjmIGksDcKT82ErXyewYGaDqpVEcY7X87PP6jUqpa1X3nCRMryYtcliPcHrGTZN3i7xaTik36s9Nfibc0wMiPUNqf0_P6Zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0CCFXfTepsOWaOO9cGSRa9vT4pJcCd12ZRQsziTysnlXyqICl9OAJKQ6LFRb77gSQLYFoPM6VyXG0UUHMm1ZIZv31aIwaRPQAmqk7XfEtOzwJk4fdXa8SCBctRBruSAA9ImhoNbhIgjTG4WKhF0XilxMcdl_loi6rH9sn1HuR9QD-k1eiV1mpx-yFR9Ydp6uoqzJYwH2LyXwFhs5FuYHVuzse6zkmeDcREaEFYPi6lnjsL-CaYfWXD6R0Mg7xXjRE6whXtJMvzQ0JRIlbu8nq1eenLk6z_LHRpcodrkWFSSZ0m-lmKmTJ8HON-sD1G15yi-oMVIU_CvoHhU8awqBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=g5UICj1x8dEhXF6c-hddF2gAAKCsO66GnQfRQYW2qtFqCYDxtMoKgDw3a_F5jmaGC-PB5b-SY3n9XdSJAcOEq-cXioBH2rT2NAG6FBTFNlNnfmYvHc-UotxjahMnRLOymeWfkNTtrXerTiZko67Jn5vjN9JJBfIZ-92RqHeWe5JWephc-HfbWCGfnPA88xmmjGcmP8Pn23n_TNeseL7_5L10uP84H64NprfUZs6dn7nlYGxdWLZB0BW3eT6I0UF1CDMBFNXl4zFG9-SgNK_lejtJD9YRSl65v5BYrjKR2HpvQbyXX78oBhk5F_KVaEw2lScgqLywyESm5POpQKCN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=g5UICj1x8dEhXF6c-hddF2gAAKCsO66GnQfRQYW2qtFqCYDxtMoKgDw3a_F5jmaGC-PB5b-SY3n9XdSJAcOEq-cXioBH2rT2NAG6FBTFNlNnfmYvHc-UotxjahMnRLOymeWfkNTtrXerTiZko67Jn5vjN9JJBfIZ-92RqHeWe5JWephc-HfbWCGfnPA88xmmjGcmP8Pn23n_TNeseL7_5L10uP84H64NprfUZs6dn7nlYGxdWLZB0BW3eT6I0UF1CDMBFNXl4zFG9-SgNK_lejtJD9YRSl65v5BYrjKR2HpvQbyXX78oBhk5F_KVaEw2lScgqLywyESm5POpQKCN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHeIlOfTFz4wR2ljE-0B5VnSfGiXzWE_I9jOtnp7vHQK0PQURspy43lcu-g35VbplNHFDQ3qzTBQlX1L4zJ5iWcEo_pDdwREk5OSuC59Pgz3XjL0M3_lMCG8Dj_pgSa2k9FwoO5YTWiMJcgxL38SnZhErsUBlpGiwt_anzfLSJtGeyhAoHI1s90g75M8cbENDDBvLuo1xLOrMd4y2qRxBdStFjWLZMbaD3bUzwl3Oltf3G8kKOWO4p4Qdu1T1QhHLOiVJ2S-wO46vBUri-Ygr1y_53Vc7E3pdrlu9e00yZpukBDITUzZ450jnQmVvsT9r55o9cLbesQD5ER735ST7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvSepJ3eCFDJC0OuxzbN9q610oTJ2lTKkss656liw9lHX8yk387dHNa2CxlbknE6aKUleUaGgQP063JVct4KgRjJlqoziI3ibW1YuLmgeAWtzsJzT7J3jfqPJyOyK-3UjfmmmH24gl_fToXuksjwlgPKyGbt2L7GD7acXY8y2Gi2g5yVKxz2x6f69Y-9qxrJoJS-fHHdpTicelyvM2mbwD1DBkXog2S8lWxD2Krgd0scK45MkCARTK1IEZckdQSPFivnhW78Iwrx_6MW-6dzGBTt1bRHOUSAJ9V8gCgX4wMe5yos2QjGR6muhoynh_3Hm4nRh0I7lEtM5f8sJnmR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0XbjV7C2Vhf50gPJ7dhaSTNxQcwBDGIKtCn2RO8zAcWSWCqU-jfVlwGrFN3rqz-1sNM024EdDt9mRH9Zh8Ah4fpEsV1i7paZ4MojAJ1I0s3o7hOLihwP1bBcy2GDWcH6L0Vaaeb_VLhJhKHcpnFMFpyX3de89NW7XJqne4CjKV8GaDGuoebmXuX2TWHrL8zB66ZAHSzU26ovKYRk1DmvI1OUOeuiDQKdiBmORDhO9GHFN_zJzFxNlruhh7Q8lAmGP3QAgqSnbBRuvyt623bKsozVKyVuC0l6GXfJG0-e4v6Ch_ZC9gAHcdYCXjNST7JTUf2dTxUVwghfr8MlJz2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhsoAgDC9utop5FVjgoix9OKpr5qJDBgVLbMzQer6wWqvwN0ZO558eKfkVSla46U6G6XjOUNmgUnd-fYjAgyq37GSL0j-cuNwIiq5O09J5S8F8CP-a9lDT0xdI81UMuCy8McVz-ONDTxATNhssVrCa5cXs5-X2FRg--Quadff6UNrg0VL444zTV9ADzXKLOFphnrScrlyH5NJKOMDw4TaLRccaA69Mivs2Yu7gc5cZTVglS5JXJLd7PELBq080f300uFFdjavxpnTrP5J2vnDtZdTfvfI6ABgSynDePtGKRi3CxbinfqtSsR7-BW5TRUAgr8oefpUHpuQy-DoR79nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCtYbUPUjjYfwaxzfQW17GnUtSLokG4uWjQ-WsgktmY9eE_850HhZHNW7H_yr-Jlc1LILRDdnXETJxXgrzWDZTPIOZaaDKiWWxcfWBNb3lzvV4RbnLkq-yQ0hy04eK1J86E5IU3lGwu9AuUgtI6ZhGQ-x96QarW_HHBuBEEnJxciZHytfsXQrQ5qgggFmCTaBl9qfmab1HvhdWgN66M8F0ZN56VYEqF3sacm81jLkIi8gM513XkcdWja1kecgzdh-2V2OJ3VgUhj2AFlFIYxf3Li6kdohEUS9xmcAvvZWrqre12--ungU2ZgJ1143miS-bU381VcS-XpjkwA7Vz5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo2U381k8RacnMdCf7Snq67dDgliSeoIVooMQlXHH9mwXRRvlwjZqvriHy8wpA-hKaTdfpdJ5pvP5saKy2BdIyYAV-qwDpquC9c6OkXK27yMMnEjqAqf2jvEf1nXesfQpd4qFmfCWDsGSjYFwNGTiFbdNCb2e4V1lUFf-QTvWKHyxW1yVZGARk7v0GF-9MUNlXZJ5RGTICrVL30MnTMlUJb7i3UT9OlirESLQ2fFHrYOCznQ9Y1iJQIBBMSr3YYiw8Ad2RRzxSinzJMeRQPYLckO3Z---kLk-gRJKiimMc1m-fMWALTAXIJ87AR3stYCKk6yHFmzTJupn1XIS5t3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmdAcPfljIessnZgdqdGENkydi1NUV_bZ0iO_CsetGG8khxThr4iz0aMU2igUECq_DOvx55FDBTkm9tNNG8DjjB-zSY-_aI5FD2J3qK8rPsM4dl230wayHrs8QnwXcCeKdKuoW4j85cW3NLJkIbaTvxaz5qAoez58tPTpcdQpaB0L1m8WH_Hrk4hJNY_vSlOdsr209tkEzi44aie5V30uDdgZIXbY--c3HwlsjDolh9LXKgMJPcBPPFuwg_pg_4T7emvHGaVpbtz91_lSTUtHgIDiTBOVveUIp6K76dw_8W5XOgJEmZoaCl1kdljaOYKunWR5b5eWh-SEyssbLTtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnhj_gNBXkE9QVjQc1HV6LDRN4cCN4mw_COizkJmCbs0USTJHX-D85T5QXn-SnhKNHpysKOCjbN1boGhuFzZRsRkm0VFUIQ0NZg_U7FP845zPGvmzDFEAoV6cI_uixHunHhV4DJjLTYaiwGUqWeYogslFzSohqmuxpdppwgsqZ9XuKaJOgRbb7fRf8Yc87qouZMjaj7qNF4YnVdqW8ubfbs_zTLQzsMowbQO11ZjkK8H16pQ0TPWHAcKVDaTwum0qXnDfzVbYhy1ERDYHaG7Fz3oDhb6MoLJYGp6_B7vjRUdp9wOn1I4VeF0PDG7tpkAPJzOy1R09Drboe-lOezWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8irEBSi24CzFKH1x0D0XWcm_B4-P3PfNNh-s0EYd0BNTtbRZIM4Be9R1hMB--0vMpdbljJ0cDR210XMIHi4a3iDBmT7x0oA3xalyt-VKRqZ6nDx1yq1F9Gn5apK8iCV85dyHCvUF3HSBpCT7jXGTqE2zDggyPKljXRxNk3ytVN_X74a9a-Zu-yG7VXgph5G-HsWj1eerGR1qei4x1KWF1SJ7XSR27xTLfm509m8U7qM9b_sHIyw5IAqInI4y-MPShhY9rA4OfeWdWvbTr67cdboOBbgJWU2EJCnHupEIXe8UsTY1cwAciQv7Vk1hCNfEOE2cvYoOpaGRz72m4QhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_0PI0dOX7-zaI4QdPd5hcHxBte2wrhPa-EZr69GhtxGqYNFQ3wGL8wzJhwv5gXw1e_eT8NUfhru_8PBcWUXYQvZ3hgJcwdqBGs2MWTm-_DpfYKNZLBwvhMIQHehh2lWb8fb5ZKdZ8jDlXx2p9_BizeuGzZA285B8kOw1wifCqG4Am5PrnIPJqJ3KPW63DQf21pjB_EH4yLa2BbFERFose6I7UWotfdksd2dFr-56cTYEl8mgyakekKsG6g6IxNaoAqF3CpTRzq9JVG_qNWVhTt16MYWWubbGcPLTyxdboYP1UpFZQ-JcETyr9SVpoZELv-7c4keLRQS3JncCAxh-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flJSNH9yebNS69hUdHSDXLsyFTe8aHZsdSJsOVxyqTlb-TxOwfiYAkLZmOsd0DE8vQBflcPBcl_vtp5o9OxbzCvSWGyGVyGRg9ID_xRrjOwlFpQ0tP7nS-Ax19K1rHw8Tsi0Ov-Q7jArXu7JqPemYH9x7YDp5qmIS2cbPUw3ogY32u9upzOcfdt311zahjPQw7_xq9CvEpfyi0tUEvLa0r8fOUEHG1tcHOJlwcpskVgSs3nXN4LuVmdoy4nSu1KyQEbbt9ev7ma9ngQYweUDI4Wl7-Xg6DK3IyCAJ-cs6feWOXZ_LdAh_BqwQiHAUSjXH13URsbgU9fjFgKdMG7DfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=G_W9HuD97oE6n3eJcPFG9MaVX9Y9PqGBEMVaqnru38sdQ_8bIDlNGqW30yCjlgTYT1ev0WeQHYm9ouP-Hmbp5iN6u7UqcSbSN_7f1GWsDKjl4cW2j7zyEYLf1zRMNPBInRH9Lf3GM_s17HVoowlF-Wd4X_AXufL0RUUkXU5381GiHjdc97SBpK_h6gcmkTuNcoY93iUr1w4jkBdeQy16ntsxGmfVCauC6j0-57NeQTxWMsZ6G9qlv1bpGDqEjCuBsVTduPUwauApIiAABydjd_uXuHVnYNEdMuj-Dgr1PWtu161w-E5EKSp_iWz4o9gu1XRhkDAcAUnCkMOuiz5Cvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=G_W9HuD97oE6n3eJcPFG9MaVX9Y9PqGBEMVaqnru38sdQ_8bIDlNGqW30yCjlgTYT1ev0WeQHYm9ouP-Hmbp5iN6u7UqcSbSN_7f1GWsDKjl4cW2j7zyEYLf1zRMNPBInRH9Lf3GM_s17HVoowlF-Wd4X_AXufL0RUUkXU5381GiHjdc97SBpK_h6gcmkTuNcoY93iUr1w4jkBdeQy16ntsxGmfVCauC6j0-57NeQTxWMsZ6G9qlv1bpGDqEjCuBsVTduPUwauApIiAABydjd_uXuHVnYNEdMuj-Dgr1PWtu161w-E5EKSp_iWz4o9gu1XRhkDAcAUnCkMOuiz5Cvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQnDM-fH3drWn4opf2J-pBEBHz3JfwVtWdoXhuLxXo1alTSL-G5i-LvO9jCs3t9NOoURMLfyV3k7WQ3TKoMJo207kkPS2Et0dpp8qSD-l4rPMACvbdELYkkN7g30pxCoH_Se07onsBis7aYFDzCX8oCBIwDI23i9vtwVhHcab7o7vG26GDRMzsM9Ou9O293vO5sxY20ZkPn-vTAgUOYdRQ9OjZa0mLrJOfdFmVpp1R2nabQ4qcPd0eU49jgdo9AqRB9_zbFTJvKiGC-NdS1qERtgYkY4urPTBfd6ro8lRyw7QoQUOsNcD7hIu1f68W329WZh7K8Y3tfQFO49cQtgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4N8v4XmPL75fU1L5wqOi7Wj3l8XR9Ra_Y_o9h2f7elu2zODtg1MMyFe0397mFZl07e1P01csivxk5UbZJNl4GVRjG8lMo8g1NSELCqnNpA0WQew770pXX1GtKMM2gVAjS9uXTTZDbopdKdWie8UsoyXx_4n0J3tTXZWCHxwbqdfCBpyJDGbA7PCmkt1J1ksQRonbPQYsoTVO9mmtg60kxDeqhS-yBXTLhNByHQ5iOnRbKlv3FR65ZzIUvqu6TKvXEIoR8sZslxk64TLlJp-CKXvhI1Aec17plS4InoVp19gS-qTDHAJxvDcrr5OrghYb0Zn3nvo6uo6pra3sdumaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE-FnrXuI_WU7AWbcH7gad9Y5ywPI3b0_svR9bvb831a1CMGk5A4o92LbSROfmhPgvk68jmhuHXbRAt3q7hwvlywl4DmWOT9JJax8ZwQHbeRpfySv10XpJ8679ETt3J6nOrnF1HLc8Jqvhunj6NnP5mR8Pn9-U6xNogJHfiej8YGkce5APlb4CkQVDS7TI4hiZG6DdWCBQVLeMr2FjBZha2YfHh2MxzlIsgBpV48arSvt-5xeCI4cF-xyWPTUAZYYajO5XLnzOe5RN48rNuysK0wAvXpH3Vm1G6Vr7pVL-OzcAicOv4LwNfYI-GI2qkzbIe6BTdfYZmoQcmlg2bILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPOxQnmbh9jYEU8DnCSUd4werD2sCZRr1XNM4B4s8WOfx_NNrdMkFsDNK67By2OeDxGx4GnR_RdnQQUyjFVoSUHap2qCBAuKlCc31GYltowJ6pBTHx7AVXqwzKAUQrufRL1MXet6cXRWroryeRrf55Pho7holcd6umCI2sl_AT2ylMUqesUa6US95nlK_5S8Ooob5g6a1CrNkMIksWiwRAzOzqZs_zvzmKkPwwwIERUkIBGZItUyuUFFVHN0uUR9ZUMqYtQL0PiQ7s9Ea1kNDuSJd_8jZApJeG-9D668zPsXBFybWzd2N4ZJ007TevnVy0LpiHotvfmeUZmlWKmzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEShLQS8N8mznenYGs1qF6DgcJ4Vra-7KaALv9GH0ONgKC4-Hp-Ma-6axDlE9d1DTP0P-bipYTAvCpydNTwaD0zhtKaqtBlP-ElasRy-70XjpDs4Yzq0pbn98SAbcUL1m7a3KswX2cU6t5R-3FDfigmHWi3Jgjcj1qoESjAZ9RJ87KFR0ssWSFWzjIUelrGU6iwUdTq-5ZzpOLKzsdvkWcyqNmlsWbhx6SB_2j1XW6SfONQKC1Dzdbkmlcgn9b1tVNdhFnvYbLbgI5ilNLgAJ3K1WaxaotaH-5GO6gd0u0Bry1iGSYns-FGqzk4PXq_a4jDyrhlxqO9DczIpxDGgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEoe9Loz7K8N0tvME1PsRcj8KZK2IpZ4wXWhCQukfTC3zooP_M4GaLZk7K2GPi34HwsBsTZnUpFuRS4HtR1mtkZpMGegmhHyJBLeQRc6VkfXSC82QgzrwuLj9l2rJGpNO2XS6j400IqaJ4CPJ_V58zHEz25raBSsPrU55cRWIH3jY6iDIZzgOGhu5fqxnKkf0B8pWR1oZuuzl5XfWNEfKEVXcVzJNUAbplvuPl_4FNDpUpKt8zVaJb3ahcsK3JKwvONAf1NfYJW6URbsuHa2AxWKWGXHYgMPq-b5eWo1FBtfnrnbMelYx7PeqUgln6KdvuJMevTLKf8zIKomNojORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BktiwsiD0mZKpWKhqNyNdk9_UdP_WjXFQdn7dZH3ejYTqukPAHu0931fJWKHoJXF7EHMZahc-ubPmp2ekmv0UIJZNY9vMO8T3EWuvAW-shwEJAS9MIiaE0NQIQds0QPqmZj9XInrODO8nsWXQIXHfw6d8pQybwPqZfHf7Y9xLb1H9iag6IFJLKQKYS7dPPIEH9MBMMHHE7KkEYLieOVNPkD6g_rKuGWJ68wmlE35I8o1c2QOmCqBRg5NQBezeNf13i44h1MOk99gxhA7fdxG7e1X1pSkT_VPg73K7gDW2Xvh_YOocd74KVqNd6TJ-T_HToclQmC1AZtKoA3xEbCZtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHEzG5IT1pAIf9wZkHlIpFAJbfIgPc9iPxMg_54Fe9nbjaAa2kbleAV_CAsP2CnFEe2kP0u0sPjrock-4poFJCCH5w_5FYdPlFRWJbOgZD3Iu7zDZCFofeJu8H61BlsglHBiIC-pR_MKaN04Xkn4WeEXQ76wp7rEiMK-7DWSqxAfazwUnc4vEpTqKIzX2ri5moeaevBRQDIzRD0v_HIS2Svvw_6OGauv3KjR0x-NVgD7fGF6gt6MVZb3kUOOLClh7Rr4IfuzDcznCn8A5Miv96tNFzBegE7VkNffGC12Aaey-z1cr2N8VW3hlWk-72AwA1wImqQFHd3TYynJ_VsUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFEylT3RhO-swYu-OWFQpd0gVAL_p-XpQUL5ljG7WmEB3Pttwm0TwU2wr9y0iRrh3CISugsxCvIxRsdS9YS5z-C3I4cUoUdIZxH_vmNYgKGuaDAdOhjpaZ891bwam7jY0xeS5fHQua7bJbeMgYI5rl55A62wlMpIZzPMPpfP1JI0FUd1DKJ5nLLaWynN6X7fgGtpBzaEF6DQ7OuZGu8OUW8TQbV-IfVZ7mEOOt6L723_IQFuZpHeRbuZsFSjv_FY-DqLjEDxRFEaoYhTeNcWi4RhBw23H9W1Awl7TDDx7KvS7ImidaBUVcJvTbT_GPLJ51hAnjV156RF8iaq8R_nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0QkVhcF2gPcvJIlxX0c575CI4VNDcS-2ZB-HWz83MUohObRiNOBICPSK2rl8Two4U4lXc4gTUTLRSrPOP8xJLUX1_hkMD23FrlSKluQxdajBFMedWfof0bFI7UwRH586KVnKPmAKTR-7Bgp_sfGoMX5AZoSjzTtkMo2Xb_dgBsmYymnQtI5ba3B509xMCIRTkAovWSeLHeUXAg81FPa-Y7mF9D6ihOHhzd5piiD4I122AAecjedMLHROSKdxd14sEBCa0hYeK_0kMF-9ThV1Dx8SJn0QHdTqSbyjPkxx2YC9t7XoeOFSXvhS84cSTj1iP0QKM7mro8qEHrmJDFIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=RvcONAEaz8PB9Tyl6eDyzmoGbw4x4dOgUdQQYZSZnagKmBJxEaH64vyRn13LN5YwJXMCd95oR9FvH_B084n9EMqdn4hD90yqExVCgfcjquwhHMRSJQb7p9_Ng4bN9WTXMfta_hU-GXCSyQD8kyqws9ZgIGCX2O2Xd1fM5_mLsDr2E4MImWZmaDL3qP-kSNGkbP7ry_JwDc1vFPx56dSiLsYKUWKZ9obbyhChfHAve997EC5slaihHDnBWjHBz5LJuEybdE2Nf_FfyjTYI8mF8DYLFoHDeCz-v6K1IYwKKdOJziJwyR1vlLDO6CehTYBye50H-jjyQiPaSF0Kp0BHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=RvcONAEaz8PB9Tyl6eDyzmoGbw4x4dOgUdQQYZSZnagKmBJxEaH64vyRn13LN5YwJXMCd95oR9FvH_B084n9EMqdn4hD90yqExVCgfcjquwhHMRSJQb7p9_Ng4bN9WTXMfta_hU-GXCSyQD8kyqws9ZgIGCX2O2Xd1fM5_mLsDr2E4MImWZmaDL3qP-kSNGkbP7ry_JwDc1vFPx56dSiLsYKUWKZ9obbyhChfHAve997EC5slaihHDnBWjHBz5LJuEybdE2Nf_FfyjTYI8mF8DYLFoHDeCz-v6K1IYwKKdOJziJwyR1vlLDO6CehTYBye50H-jjyQiPaSF0Kp0BHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=QqROGAZWE_XJ-mYJKaStV9g9Jl3B1xR2iBS8cWvC7Di8Z-lPEzrv5wBEMCck4GF0GA650L94nmquCNQvaKP3ZAdG0o-MzUWt7VsxW3cSIXEL4gWaj0tZ0m5eaN8Z5-0rNjM7VrhBeorEa7_P_UXKURjY2Iob1RPGYK4XdePe_EbhGsUYegMybdZvjhABFut5uMqPeCSNk1fOaKgKZTw9RMDwbbVJFthHpLGvFKtuWT_A_OF1LtTTaAJAZIX78Yo1PAWFK-n2-WtajMQ6i55JM2GeRtTIn_1moUJkJoVSgXRTk_wh87OOSFaf2iZDakcejerrMiDZzBzKuvPa5LzILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=QqROGAZWE_XJ-mYJKaStV9g9Jl3B1xR2iBS8cWvC7Di8Z-lPEzrv5wBEMCck4GF0GA650L94nmquCNQvaKP3ZAdG0o-MzUWt7VsxW3cSIXEL4gWaj0tZ0m5eaN8Z5-0rNjM7VrhBeorEa7_P_UXKURjY2Iob1RPGYK4XdePe_EbhGsUYegMybdZvjhABFut5uMqPeCSNk1fOaKgKZTw9RMDwbbVJFthHpLGvFKtuWT_A_OF1LtTTaAJAZIX78Yo1PAWFK-n2-WtajMQ6i55JM2GeRtTIn_1moUJkJoVSgXRTk_wh87OOSFaf2iZDakcejerrMiDZzBzKuvPa5LzILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgYirVYpRYlR3O-L6sc5tbQM41dXhXg7JW4kdU6HWs9gR4aMmEWy7DrJWLliV5GFSLJKW0UZrLcG-XuyqJDcZ6pGvjorVcj-fMsSGB8hh3x7Wzkin94IZxZVOpPzX-Wpv7LFHDV_Oaz63aOEe8oxTkAxueykm2s1yenrtxrcoeqY-c_O-9ALgaXeyIefVWBt92pWcbY1V_pz3G0ZKMMLRX0n9qoQkVoOBCxatQ6S43h4GJjANstNPE5MAcqSgFlicGKCJS-pcXwGfVFI_7C_JPFSxrh7g4ZM4buBLF-mZo_XLt3G2bcjT-aC9unnEiBPJH3De_ib13RyWSDColqrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEam-B4F-GQCRV3JXEMbzPtVfYuW8Rk_OB3s5VRe_zgSBur4NZfb-psP-9kXR66lytYTzGV1zYh4cheZAiN46mj-e3likm2k5vhn4oNt-sAvtEL47u9Q1-rsPqahCurKLYy9Uiyyb2SrusfNu3M2fOaz6h99npx22_Tqparon-xRpxKFj02TA6UwUBg8v1JzTG0lPZ3PKz0T6ZG6sFkER1Ps97iPN5OhumU7JLIgemfn6xTtm90Ipnos0lLCZPmXWklC3IsDmT02WktaHWoLzPtiruxGMP-M4Iwv8EqSYCQh6YswON6AXxM9JzcS7JS3_WjiLsHJwVs428xWxpYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4VOp5EPaJj0RY1-TN12IavXiK5TG7W7Vb5K4-kssfW58eef7p-CFo6qQm0N5-C4vIrqKpMTW7HCv3H0C20sX9aULgz6ExdIIU6OwuItIWSAntc91cFlyHcbfkhCGkqX_CioNJ5zkhdb1Ivg8Ox7n2Up1LZR3dJdmvu21HQr4R1OfA-Js05aoe9pwt1uP8RlwBoYgL3ec6KhR86JnLbOD4HeK5SFgDV0z7QPo2y6eL6IiGHZPtBSaFMuxQ_2FzS8r_Ve-m8y56N5cCkX6SGkpgme5Wk8C-sMaoz6gC2JFpr2PBC-DMLkAfLAWVP8n2tiQHsrt3uSCMmLrfzOOlvVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgJTVl44UQ6-7YMhG93p73KXZIiLVUE5OvGg_XVhe7CDLvlpwtVQVx3npWd07xsmnd5fu-HJDpTeyN47yJo_wq81OY0hexmSpFWrNaNUpg5s4-rwN1RY87NLOTR9L72QCO46AZJ7WrwWE_diCYih21agHRFPyfRpqkeD_usqLR4b1_FrJIAna61SvQQN7n8a9VZhuZWSrrWNDjYnn-exuP87JhfRNJC4YUuqvISTx6b3SGdbbCh_KXzLME2MylCdSq_dmv6-y3AVtRhhveBq3KPjr1O2QuXcgRUVNIR9hcptO_Tyl3Q26OlQ2tRF6zhWsKCnFBP8bPQFOv70CozsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Rln7ZGMSGvw_-csnStWrnd7rJiQh795pqDUuEfWIroNd0VvSCsLdSnPE2lG41axPDqUNLvZxv37C89XM17kXX3F-TkPc7Sfwfq4Y6nOTT19fc5jKUxdQPJoYuMI8ROpNoI0M5mlvktkIgZA75jPBQNJo4WDrfgVRueLRk6gV151XcNcTuFSg39rc5Zb04dhLcDkcjLmvg_0b563C5t9GWGkkhaikBBv1t1pptI8SmDuyCc_IlfsTn28zun5fgEs3ChM-9wYO0PuXBgttSqNxPdqJg2BN9VDKG7HbkBRLWlwE0OphTpXorxG_aiqmd50d0axyZgSEV9tRGbMsVRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtnpnQp2slC7HkBRfvmZO8ItCJJjYS_o3vpOj6-YGFTLThAnYDFFCqJRRr-RoZJvfrWRzhJ_Cuxmn4PskoeLwNb1BeGT0Eom0rQWqp6aywuEfPEHEcHqVqv8glVMAYBQgONTaIHO7c-LXkqZYbkZaTcD2E42qM3yZRfV5t2xONy8C_Ni11zbgMpMnTt6QOPCv2V-h-G6X1HspedMKDXX-bc3pkY49NUKC-QiiEsrQVS0oNnQQExfu5MLoT11-jF151lYx4ndX1GGdb6qcBge6xXHHy3bwFZNqtxX0HhajSWSxThFnKqyf8V2alrDcvzvo3hZuhvY5RT7stQLT2X7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNo3qpo-N9iIUyiBnnTZYnKK9FxjRWx7l9cLnmKxqCGsR37jXXSM1lAYxYoyf4WIRXzz5Ft83aztatdeo6t6o-jPCH5JT60WwzzQVrvpqGEGH7HyxYS6T1TTWbNN3DZV29AgvEjRYjE_SX_SVeh9coa9RdOqZ4NW_kSniBEhHY827Bts5NYslnQ1sGFl-rixQ6wejLneoBkemXyBLP8gIInPaPrqvnQurTQ4mx42wP-NVwGUFIuATLr8KjC31DQ3XjOJBND60IYVn6FCgvrTxSmkUPTvznn6DINs69Sxsbo9faUYfOkiZeBlIBH2bhPEwz2Qs-QlH2MO9oOWIYDQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OipbDlOIN2ztV8cOeMABmpFpt_Vl2uddwK9cqsznS1mBtvyNXA2k2MpeSqe2UHga5m36YQ8NejQITM2GB9boxyqHUN47hWQdvolNQcIZ0UeGMbkDpYELatwq8agPKlwjru270GqPOsLo7MFMzfG6n54s2POg-qXataxvH91Q42ea4JwqUQnpmKPPqGtrFMCxMjHuVpznSect21KoJln7SlA9mRoFZ3zWCW6jmLovLTubkl2_SD6Fi5An0QXRSeFUCioVEGEU21mcbztck16QascvE4OJvIdmEI3MhXt6E0K8k_7uqPMflwt21Du3KyfWfQKhxxxpN9rtT5uRuz_buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z06XccoZBuuNyx5geDdIpWYYiuQ1zRj_LURDwjzeFNaTBk616DcrHY_YzvWYnQ0-LAnEQnqdmnGbnwh_vShD9nOTKEOdOx49kEV5-P_8E-E4Pl6Rofyc9DZ5qnIiu5gQavoEaZ4_KQ2K6qPoa0n0aQXI1aw2mNZPFruIlSTxPmAQbkLm8_i2vPnmfoJNoKM1GS6xU6LvjVs8B_3ympPql3NdEO7eWcrU06Mj9HsSPso0En2L9_sFf5dS8PXnMbYKXEvD-ok_hWGu3BvQR62BOJhd6VERo_XPhsOy9hZnwXe5P1ElOxpgNC5L8xFDbOVAJK53omY9Lslbs9tk4hBSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFBtHS5PWFzUDn5cJfLIGfnH0W2BJ0-izYspsA3Ff8UDwnKI6ge5UgqQjLcLaQbPUnSpLoPwwfNhs4nULqBVJ9tOHyJZN6kURY2DQZAmAEWWcshqPdCAzpj9B0Q0q0Aak3xi7nFDYJ9uf7VfNDNY03u-w9yfzmDvSFlxB50llcwb9tMVPBT5kgEycB2CppqOhIUQ5CMfNt8J9es-nIwquxXiGM5zlpR6HJjQMkG8QgwaOmGxQRH_gjZpwLOT71DwT_UurrN_2B5q7EVg4NhuF--MQo-L6HEl6PfWP73eUjCngr5gZhgOX-9ffJAEA4pZrXA_3xwuGd68qUzaSiYd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRlpCdA7bNNdUFneUQ4UfbPSR1ylhWswr7J9sVdfhts206gW8W_g-nNCzUsD8stbbHiacNopNbKixhP-JwR9mA1R-gdH13D9-dHUdkoidCSBbl7scOWZkgogNr5um0taSsqZoVPbMnjpYhqI5d2jCaHieNqGMS5g0BG0jB9eLhoTS1UkIITsanSNkozhSjNRsfmP0xKCIGSmsCPDQz0019LfM8C5PXkDJmEPM_sZmdLa8x5OHuaDBzwVtCUgmjdkuFeDGROgVRuPSNqH2WIBwhtd18k4O9GG6lffAxLAl_mYGuBBtyrU4IODJ1EWoZJdmSEOfcxn6eUmAmirQb35Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm3JB3jagXWIiSx9YXYVBRjHvKjcW5Z3rrMKqsCY_9wMWFp5OO8VWilD3GC3GH5eLc0oOZMClprNqdq07TezjooU8X5dJqcfywj0kIQc3HzbIj169RdJlexyuCIOZPohS7UaPv4UKKFIaY4q_RMTaJDGzN3dPNGjDQTPIIhcvbxRNxWsWQem1yXP9MFpJhO0nyAQPREDQUQFwWizIMrlbkD5dbDxzaGVy6rfFt-2p8NJYmtsFlJeNFUdXdDeH3qWJ3OQm2qc1DXs1O1A2qTx2e-bpJA8NYMoHjTpg9WmsI1eQq6f9ogC1AHxVD6FSXMnppCC5vWGo9YGHm2ePymWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyZUoYM700x2zLA4yyzFCcbfRc9BeEbZHAK8pQhk3NAQ4YbKriyXIB0Ufbz6_qPGP_jz6xJ68x9nAwnsvltedAPShMZvEOBQb1smHzS2IwVj-Sk95PciGJiYygNYZ7qywai6nRRfHd56WMfiKIsnFFH8e-LOcFfl_1auBjt-XDck4otakfxZmSJH72AN7-3ZTNh1tchV1dsbsPzCt4NXthrsRdf8XUq6UWmLHfjk7LCUvMcTR3zU1CKMKoPM9LpopOfJXv_XOgRZZH-nQiYM-9wg4NM0QHp2Z86Jnp9A_ZM-71k65kIbFLx7l2oML9-NPot7mqwlq6k81ZmyYKq5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjlGxKCPnH9kFDjiWcvpUTXiqz2VGMn7PW7Q85ph3qh-6T6Edy_J36AIntqirZO3_bpA4FuWuyu0pltZcDe4ez0JY3_pp4D_5BXAg946emnL1CHoDFgaOQkNmqK9uad-FxIdhpln3U-rWSoe0wsqkQWF-j94VG4f2ndLrz85dArF_-4qcifjeYnvtmgsZgZg7aEWcTKtqXzS8R1OOkSYAmg6OTBkbC_ELD3iLayDA9tnLOUHUqFCu3DSN6ijD9FmYmKFwf_KxMkceba9ViVEJZopXyPHk7xVVxG4QIyUMrTtcOLqaFYg5jWWGJV5L6jKbWbv3fVdHj4z-0KxdzZucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5IX1yLsI1sYz7ah2d-sq00DOzSI63Xi-8tsGRj-ih73ZkFfXFgUaB2uVuF3di1NR_kxZDqiYj29D3LS7ibUxYMYuIduySDaY8Jj9BgA4CdUfPvgG2Hy8_8VNG78C5Iv7wTvftVtX2PTbbMhZX1rtsRjYawZH9aSwnfMZ7SrxQynP4wfOhUHasn-so5JJZqjIjtT7gVf3wkTKfTeRmG7boATk9hvn4sS-bbKCksvXVBcGMeEhluE5EeKRjlyllGB7iXZyLx2ZcvdlCT-tS1KqpmyfFKlitPCWLilOXACUiiz7_W9SA-Yr3mPf1Q-xjeamEMi09TKlJQTi1vCTGxLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQbyns0etMiSFdU0b9V5gLYmhy3PtfJZcaUUVM9Q_47NfUZm4QyFLE7elfKANFK-_eMdQ1NB0opmZmNMx8cEbwteGQJuqELIxUlrc-Vy_D-HeMemSorDV3znWBkoU00zCTH1kb9h7wAqSenDgG_PMlUtZHo0F_xYmKF27VrLmxQc2BMvWoTGOT1APlaTkiCMTNY38_D-3Hh1_fU0lIlP-FOUp66x6s7RdDO3j57LzCuXfgbcq0FP_78jjX3jQYwubMFICD3WjGs0dOl5j7p_GtMF_iwq61JWo9y0sc01_Ux566Q2QMz_EAyvXF8EH8bjYc5cGEbFtuX9-QuSoqV40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArkLwc0TgnAP0a3D3K4LHISERMSTvYoqCMn4GCdmMPvUyok-_ykUk1S1CatXeDEB_B7UWgRVfJU3wG4bUN_teDOq03T05OM5-yP_uoKFrAsha54GFWHTKwsqWFyghJxgK1wSRhbjZDC5bP3et9Jnn3apIGc7K8rcAsQ0FgdwViBLqQOWvXXnl4EgGKx9aHK-b8qyqUowVV9Ewu4LDR2RsWXfV-X60cUXxFjPuOWeNy7QKEL0nhD87aNDEH8MwbStzedBcWRni14t3EfU5rlV0i0qNLFqGNmMxt4f_UKycMVT5Yg5gLqFlFDV_SBezsawj15KrV_upbXzHCrZgQf3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3aghZa0uEkb81zQQ7LT0UexKzzGvwSW3RUKIKfnEr3BPVGAZM2SeRskRObdFKk1aRmgJE78Rk8SofX6A4p0KgEx2NlIejxunR3JnM4H7F9UA43ZUCthIyuAXdFqmweG5ZkaUggG4HbB8ZOZxtN-p0WPkZgwo_p0w_lQy03gtfcfOOAvj0bZ5bXClyLaXOty3_t3bO8TAshEvjo-L14Ow2xUcAfGblxPBBKlztz9b-U41psWpqFBfJoGIsXkZX1rg2XWktyJ4BqdQF-k7husEn8DtMagap8vrtdLa4mayuIojhU604Hky6BClqSfiwPXLeJ5M054g8D_eNMzEacLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD_Cek9TWqrQu7XK0Qk4P0YOmWIQz9GX_X6vCJPs44xI_6-QWADc0hPsLRZOhmJWwkdvcToTzwr6chIdMS1WQht9WHLrHSlrUjPA_wibF9v7Kz51iFjrFTPGR1Y3Xd6SN-YTX5JMOmU8jdASbf9IupySINr3Rf1ZxXw8I6YKYBXY4d20PhbOHPmT7T07fsSXaV7sC_61vfSn_Zz6IWvQqQpugIZoHFcN3UZEoIGwiqnOPg-eAkEhWJK3aPdLiLjlVQCqk_MeWH3IdT_pHlzauW9Af9cg1lJmBs30ZyeRa3pZYnCp_f97NHbzCm_7t2-6qJNe5sEZFvbyrPdvjLY20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrGiy5u8LoLomcDsDL_Z3w28pH9gk89yEBssUy8npTXIoyiX3eeHq25TaM-NFP85YflpK3Lijte4Ym3iafjD76zuMKPCMMrh6rrQ-pGuhvDDULq0Nhte8KMyg8mAdB43o91eJCv7zhpzhPs_5iSDE5i-BncXKO0zGQEwnM9K0XYa6xSvkEWfxn1-S1VGUYGrOGOACgtRFkJvTSfXPPuwy0mh1xL2shF7ZMSUhpolFtrLCPMdOYZuJMLAhspO05l9BkU20va6v-pfQ5HsstUJuPRxuankWMVZ0ppCZ1nNgugi8hsktq_GcpsJgDg_geAflx7GEyLJYVW8sMCBzr2aFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxRh2retsbuPK5bGdSXE6D39N48z-HaqSPDhPm7A077Fvc_rRX7ce9FEC0vb4yLEG3163jal-PcGvYhM4gfh7R8_aNHL0eq7mTNIgFtfQKBkHY6OYusJeP14FJOd9Dw-vjY70jM2ckCSmD07f7icFSjcYo8rTe7PpqJcqqlMoN4OR2UN3vdmBZoVEIUct2YCS83G-9XJUGdCPB5McVOGmDRwLh75em_o3ajvHY7dUf9McrHl3feO8XdxarnAXsT_uA0wXcNPGPvKO3lBN87M6-xfVUOJeVba9rBxrHo30qx7ExMYaAYa9V4WUph1z1tRg2XeU2u6wErgHhOm6aH7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUWwSSF2af4eDTJdpSoVOM6ycqsedtwR1XkEal1009gc6Z83yjfi0xrvxFSW-5_hdgE0K8YhlWwA1LLisJPcEZLXZ8ZcgNkQUia1ORP2X99w98ZuW_4RjmEiwYNV7BscN5VrYWUEOjo1ge4E6M200DaEvGl5Bx5aeEj4LzK_qKORQEi24UgtCS2y71MTVYz9HnJZXCG_vOa0Yrr19gn5i_LS5_-gWRJdQQ4AHM93dfcpYsLXkEZ7cN_JmJiQXnEQoO3NvI3h7ms_2Zq6RhuUkAMgrpOveIGN2Hxt6E-SsBt0W4PF2rzsEVg2Ms5NynmbUuDoN2qft904jJjCt78z2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJriJfnc5H-AOIlJp5AsJhqNEwoOSArccF3v4sQU6KYRYRSg3xogqmqYLnOXGyBW-f7pXqm0hq7Tv_vcKPZQfqPsr8E0fAN93FXzb2u4yEk7lA76glHFFMFtwVQS8qCUX5c9SYJPuzNNzl23LjU45VqwWD2j27ditv9kc1p_biLZCi1SLS9lw7A1qsKqt0z3hZFNgsEZDOD0te3S7EVPU3SZstDX6JTfygVTZb6A8B_4-ohOnc9nwoCtr6aMDwIK8JuZcDvRd280EQCis0S5JI_Iq3tCHqtJ-Yhfu4R4EblO3RmpIrdeVpq-4Pw5gMQkQlQbsaRdHrK6GPB10lb89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L25lRPxxFMZf7Iswk_5xlLPRtWMjLuJmt2ieHqEb_ITgao0y9mKmt004UpV0z8FxvjbxttswrHvETXk40vxCOuNRrVSvKy9WQHuzQm6saZN6g76jW75q04kNof-5exIpfQD5As2ihv5DHn3TUmoLt17umcrRvzMyrZ6mVrLIzGYJxRifbiFW6OSvkPbzN4KCpKDm0_FjrQj0-I1_lQZHGIw4r3n3MypfToMma-p__zakj4coOWVUG8M9fi44mS55xJlYhpDZQlWzyO4hapIEJZtjgRJi0JRG2VzCR1AGuaDS5cLhbT5G8htr-UU7ye_Gclzbe82FRazS4Egi5Tk-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9kyMrhHnlijDQuGLAsJbpKdxgVdip62CP1IZn3VuOCH3hsQULvRvQJy8TIuhGsdPvxzSa_HL3YtaTYtxi35GTnRhIJ3FQRSBpx1gxGEPyLk87oUF321rsr1nHBRnEZUdd5xFqH2Q7Hv-Jmqo64eEDSa6JXI191TNnTdf6tNzKn7tFkWyGCeyAXy6M8AbI7SkPDTnCSFmyAz2mO9-iTHdqVFvlai8l8fWFFLWi-TPIzuyIhBW-__d9zk98xQgebnKXbAapPZqaVJXgY2ImJhKJSojb9Klz4J8fdb8CQQ-cmUZH8EYNQZjhiWacmNRpzVjoeNMrHKtIkkMY-d39gxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSywRPGPHNr3pMfiztAV6NcVr_RphibuXvVWTJ37G0O6uJ4f87MygCnLj6ANdYqq4tW7DiQwUMBDBt4GagSqRVParZnDQUZ5Hv4Ynn5HTlC9-mJAPcwOGR4_BKHNBJR_rw3faG8UHzXGfqKcx9s4o-Z2bVuInaXWEQYmpzF6CfKB3JBULc7MbxVoiKhcwc3fgE_jJG92yga2onsT5s9HbJgmtmbO2ZB_jeFtwUtGCWjWYR0bq0D_1VWU0UQuM9TRANaGb_EBvn7GQeGe8rUo_9KgCbPtwCAr8Kg2MBHM28yLH_wO_APNjh2GqbbT_uDdE3Ux_6RoiWW3kQzgAwQFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUooZmp0CAKz7GCYIPcINUETMa3r7KNFQIb734Izu2ngk3i4lRxg2GLGZ22K-U0Bq0JZ4Bc1kHJmo22qF1H7ePEQrAGtSZa4GZFZhlKIlRmkKkkaOoGT1XTvaBO75myVpaCCVAQkteTE8Or5NjEixFmFLz9sAEQW8XDhqjCq87i34A-N64oupKRUjwidxVt4mze_q_t8IjQqGG8zeL5eNPKKV4bvH49in5WBTWzLJH1etkwY5YiF8jRvpjGshsKpLR4X-G1jPMgsLh-U3Dvk172D1eP39cdHw7OpaHkq30C9MAYl00Rv5QdILFnwHSEKcH_q5pHD4YPgMp4JPxRKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbpyXrbBQqytwDKuvFfT26fEgWggmBipRc_zbzTtNAkT-CReot7en_77tslJVZVHOq0owATg-OwOh-IILV-sT7cNxvPAmhtFuCypeRlTEyjbXiyhEqCndOCE6m059SMPgs4hOuqXxg66B5sKKql0rZVCnBKz1AjmtpxkpS_WS5hCjtccWCxiVlUOPivjtGmFPrBAJ232liHhNYKo38cB25Q3Y8A6pbKx1vRsJ_5WgelXNBW0FAXgnw4_JwgBLEruRCXD2Uk5R8l1BkT0CgnPkERE0kLzJsfCmACJF267YK9cVaPLt1NP0I557su0PK_Qt6N0594UVzGpNIESt5u1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=v5yOCYWvJfZ1XKktULFj4JFTa-xuYUCNaSN7s-Ia7S0IubvFHZ3Vs6hJI671TZ9xzzKApVt08K4b8vcSzGeTZZCUeoz14KIpKRR__5CxzMQgGO2qF08ASrBq9PcSR5djKTeYsQz6GjO1VGhk0lOFln-ajZdRAgpsVNhH8yIaaURBfjOEqHNhk-d1U3aTy1n9fQxXspMlh4uSLNw3q9NY0vcoaZCadq6OZveK7obUT3heTodv3E86eBZuRiPW_xz8Q6H4xPK-sIJOl_9sRk6w1ALZy5nTnId9B9vaKPWmSovuZM9cLFOazqmUCw5v91tcdpz7ip9K71wRWfz6ijRVXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=v5yOCYWvJfZ1XKktULFj4JFTa-xuYUCNaSN7s-Ia7S0IubvFHZ3Vs6hJI671TZ9xzzKApVt08K4b8vcSzGeTZZCUeoz14KIpKRR__5CxzMQgGO2qF08ASrBq9PcSR5djKTeYsQz6GjO1VGhk0lOFln-ajZdRAgpsVNhH8yIaaURBfjOEqHNhk-d1U3aTy1n9fQxXspMlh4uSLNw3q9NY0vcoaZCadq6OZveK7obUT3heTodv3E86eBZuRiPW_xz8Q6H4xPK-sIJOl_9sRk6w1ALZy5nTnId9B9vaKPWmSovuZM9cLFOazqmUCw5v91tcdpz7ip9K71wRWfz6ijRVXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI5Wz6z59kmNzsA4WxrMl8nLbZUHpck5awEG1n9o9OF_mZGjAOmC9z4bnHfHwz8sYFZBEniIU7Y0HQhmXPSiqnZhKI2MsSO9q1IRsOajh2uzmO1YrdbOEucUMGDOJjseqswiO_7UMVc9NxRseCVypoPJzaESUCMb64KcriDxd7b62a6Rpeg137_uIQevQdV5rq7Y80DAdVgv9NpEnKCEFcTchi5Xv_J0jPYBOQOAlhYotYM4XKMIT7VSq9pYE8o8Z4GZfTlwgMZzjLQuh3jy8vo5TJtbpfDUhJWAK-GHjVBgPDL1MtTbAl9BDtFqLwsszPgNtr4eg6tSglDagX1ZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvKY1Mo14lm9oDHkqKPM_GX7NDcsuu72hvN65dA7AsEcCpSkic8RKur1duoGMra1ZgANm4bNJfYCKwKygkUQ2bGXvy0kEPEdRcBi3wutXlgt9A-Tqh76HYf7QE8Y7tDBdctGzE6Goay4iaj1T9Qq5hys37EH4C-e-joSEW7RGrvQv9nk7jvPKKdDc7f30DNBe2Zmi0LQJ-cq-W0Z3mTJKKyuTS4r3Njjjfecf1RzQ0qhxBJBjyw9L4tg0F9Sd0SvexT70f7w8FleVn48ycgBZRqKb-MspgDLekqEJTTRTbY3gTVF9EB5l2rsbBSu9eOsotT9pe1gexTNnaKEmolUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1x6qxnwDgQNvHhTv05jVK8FpNmEpsx7zbkNse_SjqN8kinVBf6GuvUlfS0_XaitcdpfQyzLy8GomY51wM7pfy2K4_Wk7s_nUQYfpvkAtgYWoiinzKdv9TaZUAPYJYHxZcZdsA17HJ8NwOGwxWVmuReebZBt1vDKE4CC9V3ZKamleAZht3jcmmfSZRTmd8plPiD1seQ7zskJVJ5HTeoWb2-Ic0hhLAuWUaTcfvM_pipNbHEolHRKUmulffOKcaL__CfXVVjQsj4dMTrIy269854xQ--buyT8nm_ZsjPPx1-mturVd2z0nFrA8ItNe3FFWh2shOr2kKrvqZYG7CiheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHeBml289VES4nvXvvgzY-pGy7MnHwWSJa48xfLLEVvUCbt8YIBOLhe2Q6SjmmmXfSzgnHcfDhxjyry3Q2KKAPhiTxfsful4Ve8H-VyJExjpocxWIgFqtOclM0t_167S20U_y1jr5URQzTckovOd9JXuwe4tAuSNPK4r7-WAvUWKBdXpv-XEosFwsRsbnKD_conFyAaWbqXkMeTRZbNKrFJByJzTm0L0HFkuQa6iAnfEmvqtP8okeLjewx6_rvbVkhCd3tkzSbHbk9-HYaZwon__T38voTC4KUtnGqgVhp7YNijNtQrx7x8xpdyTvk5F_WszYs10DhNTA3NosJjh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-sF3Yv3RJGX3rdgeNSL_CBGTUlqj39nGaHCI2hLVMOXpkuuv2MG8nThvzomJkQ7Gu3zSBNV0oCacNkDDXYm3pxo4ZkRZOHo5nEoMOSxJ4PGZ9EG9nKSvUNUgzWrF1TFuHGXsNslna6yEE0ZMbC7LE9K1KXeicIK3vG1usz-PglDGoWr0Lx9q1AqgM-BoQfcJBEswE4-5vtRckkdh-Y4QDZh8jy2Je_aAzfkyhZXsH23dwRZ9ODf2nbBWS_B_Kk0X1w87SvDLe1vZCIQ9bFUOBAkjk8V0jc40CyPZaeFtEndxCkOXvusYDzZg0LXLFNNGRqqi81Y8mRV5t_fRqemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1YFFAMWJo-0xew6TPxeEcI-tzkc1AW0JF5OQQxuLnM7LcxClhtauw-1pzfOS_VQAdn0rmE7w50LAgoYoATWRQR0FbkF1S0m4MpvqsfdPs5GgX9UOV2X0hcN2ZXjnp5I4s2lNwdGCUyaPSaz5mrsAcJXA93XEhsIaiLE-WWuNHN0F52BoSqV3O9Kmxfath1TWQXGB8IodwT8PPVkCGyLeaIHZvN0-7WtyUmUR0dQL5yowhpMgLlvTOoKOqa-iHJrWeGXbKAZAQAV_-TqH-huZI-RPfyPBJ9wz8CWTKl3N4hHJiopTGo-Q5ZWoRJeqc2t8iszy65c0FiEbGqx4wTzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t59PfQFUkzozyF2mHSnDX2YWMh89R1zrUv09aYHeWUSmnbUtExeTSxN0mcEcblMWaPMkq8wea-gQN3O81siXmzD8EBtC7Fxk3fG37UU7ObMbuvGli3v-UPhYvgfY4GS6KfB9mw_Uaofh7UJbT5mWsLyg9B8oHKsgcJJUHieg0VHTyPdNuMQ_QQNav2A_qL4-Rf5uRE91Mzz4EFbTl9qa0UXa-eqK9d4Q51GDsXcrUxpWNf3y2Pgn2taGP5tCcrskfSyZXj5MMhSsQvswQQhKQvlW3_cDAMOzovO_WZY1Bw-u_BwvjcMmVF_WI_nKzFioB7hVessmVuuF0tdjnMXCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsAGbgqh8Qwk2-3ILpvLA_8kRTN4gUd2aglygw7wX9f2AZNxkkQ8whWrbBoNPOXfERT_BBRiz7i3dMvAYSd2Nbn8JF10mun8tl8nom4xhp_i4_bgp0xxSMQkBni_oOrkTpBrqyUFmEHQ-9Byx3dzvxOqyb46nUvs6mQP36jyICRrVWUuo9GEH8P3JlT5Vbu2pc24pN6g4Wpa9qpzdOoAbBMzLR2y3fn9kcFzjjo2RUPgbSU9t9JaX0Hh7UKB1c6IAnsb1ag4PJ1-ClBJABJduUJt-4XcFAGmRMV8cxMGfgCi3dimMcHq5fWE5Pm3bFxvmC4YrLrcy7C4ZczkkdTjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=u3DcDD3ghvBzNQQZuIwNl5_wMDgzbp2cq0RF9736wbLtA_NiwN_JkPyhprO0i1FuE7-3uMmUYAxC_6Y7WaTsSZLWe_l1HvwOaSAr_HyAoivhlhGz4Atx_54o40eOW8w3MkXKBuBMEMeru3lfY1kpDGvNQwQBi9_3pbILFBHLz8voMHv9nDHOXUoECMQKS-_MKuHyiaKDI21lXsZLQKsLLp32r72ikiL8mOvqONf1bOQu2xraQxjFJB9X7T18YsXx9WiC1d3SXYp2uenkzA0BQUvl81exCVd_ZwvKycTKnA_xVYfBdDE8-mdwt0DXQGO2WgUzVSFsROCUnGkoqdqnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=u3DcDD3ghvBzNQQZuIwNl5_wMDgzbp2cq0RF9736wbLtA_NiwN_JkPyhprO0i1FuE7-3uMmUYAxC_6Y7WaTsSZLWe_l1HvwOaSAr_HyAoivhlhGz4Atx_54o40eOW8w3MkXKBuBMEMeru3lfY1kpDGvNQwQBi9_3pbILFBHLz8voMHv9nDHOXUoECMQKS-_MKuHyiaKDI21lXsZLQKsLLp32r72ikiL8mOvqONf1bOQu2xraQxjFJB9X7T18YsXx9WiC1d3SXYp2uenkzA0BQUvl81exCVd_ZwvKycTKnA_xVYfBdDE8-mdwt0DXQGO2WgUzVSFsROCUnGkoqdqnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmiNEE4duMuGfoT8mlPIxiT9F9w5sSUaMZT2AGXqRgQu753sISW7Dq5iS6eh6uICgyUiMd9iImKMm-B1QJ9rpfU1DWorbSiVPin09PDXiwmRTEEVFtsSzHozn-XLm07NgsA8YAX4o-pOzMPw4seXU3KbizeuMhjySFVSbONzn8Qu42ofHACSVHTTyAkT2SavRLUE7E6Oenh0Daz1EFIgTHAdMVn-yfUYxJKozO_kF0mKu7kaR7tL2VV7MOwJlXp8l9MFgJr-lKTUedw9lsjRUnnOfYM2rJiNWmIhifrMjmxtgMXU1kb1050e-2euNG9YME7apIa5y9DnqkfSOYe9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMmYOjvYOWGVM_CVQHBSPLYEmR8v3dwRgWPY8NDmaVRHfIE6S49fO2JSC-62IvSi_c7tk5BDzLlGj1Z6VNu5apXr13VD_pDprugk8oHfFRq6zpbSmY3I_-lGv8ug5_6JVYWWXwm1_d-WyOKJ1oU5kB1w8KezgR2Db3UJuNTY1Eduwx2JoYtgdB1eWLVEttCLJB37_GRbNLH5AwlecdIldYu6vKmh4Otzi0FFoBG1TEPumD_RM7iX8vNcQI9B5xqGEvVPEO_qpwrvQZUyCvA3sbuvwYqxy1KPEjdW7oBd8ROMG-e2uLXL_b3JH5sJKcunSTVKyxDeCFSoeHlya1nsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ZoeNh52CSykiUS6jZy5RwWs_0Z6iTgMf7GgrIFU9FgdPuGTa49TlMpy1IFCZkIree05hfpyhEFFbOJ1f70pyj250BBFWncQe7py5LEt6arT4__HvGbLGiwUhHSnM-ADehSXvajtw0GjXqs9aZ0PIED39lFM8wrPay6H3vyYbbL8Coz58BpiKOQNNj025dMRwsMb-fWDgW34zsWmmUQmf_1pdHtRYVFuAmfdCrvYy0caDQbtSW7vPGblaYYAo_VGT0nmZ3wZ9MHe3MxtzDEOKj-IwIXM-tQ56WxkvqwtofwaBBH3f44xnhUwkn6dlVyBaKMB3SrcYtX8IulupE-RIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ZoeNh52CSykiUS6jZy5RwWs_0Z6iTgMf7GgrIFU9FgdPuGTa49TlMpy1IFCZkIree05hfpyhEFFbOJ1f70pyj250BBFWncQe7py5LEt6arT4__HvGbLGiwUhHSnM-ADehSXvajtw0GjXqs9aZ0PIED39lFM8wrPay6H3vyYbbL8Coz58BpiKOQNNj025dMRwsMb-fWDgW34zsWmmUQmf_1pdHtRYVFuAmfdCrvYy0caDQbtSW7vPGblaYYAo_VGT0nmZ3wZ9MHe3MxtzDEOKj-IwIXM-tQ56WxkvqwtofwaBBH3f44xnhUwkn6dlVyBaKMB3SrcYtX8IulupE-RIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUkZ1CoGYdtQnPNxxJZfHOB3JLdf1E59v0pHtXXX_p_T0jv06WjzohM47IDAXo_Zu3RGm_fnHQSP30EeraHZAj7RVrHVO857yWejCo3urNU8NKUSbsalx-yHJYKP9KoCHLn7z2RrNQvyEk5vbX2wZOuclp6ucGXAa-1-QOyCSXHexXIMP0ZDkzqY9dcfhtR8NQSD1k50ddw0m3OpIOqIswM2q3dNHhnsB_YWz8ASFHPqDWHgzBuE0lb1DftL4iPQQ-DOF_7xO1trQ0KWrj2MBFunpBYa9BehP8ruYLnNJn64TS2i-5VA4eF3ZNbdFAp2hZKv4B4CDd37aj4PiDUXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nmYMyfQ2p23qonX-esWsHfp7wbM_8fP1pI-7FrFnO0XLS9Ts0lFPMKeM2MMZ2YG-5skJnLf0p-JPbySOBWYc9hTYzqRzroJUdKf6vnLkhUTZtiaOogFUGUYEp3C8z651rAr8NyFS2zl8jrbF_iaPn4A7wXJ0fmBiVc0Sv7a_U3KNT6ln3YOX8w77oE4PFE-ZQGFiAWA66Gu84GlUZcg2zJ-60yhOS_kNW3qu4dXPuw5F7RGXNQmXYYNcmRfUR6yxJIEPgft8LvXKCGTlfuq97c41avM47FC1DOlqxeQfZrBlZlfft-D9A1WeUyQ92ohVJ6HgCuz1H_pyIZIdBhU1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQf_a3xenHGt3dFJyPdZhEP1Klf_UCxrQX0fa7VwGT_zHMNcLVhIStloZCYiWpp6ymjEbFXVITQQQkb8D5QbwszL20tMmGi_xVxyKWokBUthpSZghRZ_b8Xqq4ZM0KrbE1ugVh5cUYeJUCd8iJXT23WFIzhdB8nrLrpIPEio_iDL0p7v-hc-N6BtUj3bIGUOT3rOm1AESOCWmS4WpBY8qcPzxSSvBsWfUQm9UUgWEHoKvA0WwInfp20t_qt9i3x0kdH2d9Q5VMMn6mtLLdDJ2EtYiWjzPhYNKPXDhWwtMjjCLwW8dIvXpWG2whSq9wIsnnCGYjLjNlVZ819SVSIg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN2tH5xA5RPfgBNOpL5mGvHC9yIEOAnhihglzMMnw4bu033TG0M1V1yfdTLeyGVGzaiEB_BvjNjrjcEu1y4eLl06Hb6DBNfCfQLFEZKWNQvHHVvLY8qM-KOzaZKEf-9tI3F0Qu2gCrPuUpSR9kRhEzsKj_xk5I8bw43zK2EQTd7udcRZ8czy10eXJLnGwwE1fySYwWQORWHK7MWZEX6eFvEetM2NJvb7q9U61z91uF-_piA-ceET7FcAgIV_r3mGzVZN3TBXTnNQw1i9Oqhm0FqQCfTnk7AG0SkRdJkoVlhL4pVbkFFmVAn94m9bYTteA-Pt6xzXLjzloT2jlhRuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfI98nqN-a24yS8Ymp1IN-OOaLpe5-sY8uRRbmZ0L1gtYMvkGfbFDw8pC52sn1UaKsZv134wzJxj-zCBD-Mzxq7kuj8UqNbg6hfYGPjw6hvuOEt7DVR90aBs6l_0KnX9RFFvUC7V2eWA3FafMcN3wYW_yCXlNb2AvasbN_Xp1DZoZPc9l0qEt4tKDfrLQ1-565dHK5ACRRdBxGAczbP7WdcVkcNwsqHcn0iGbFP3Cc4RhLse8kwiVV5zRNwpYJOkldkQmiUjOul_rrtMjszfgKw9lKRYbrdKuhd8bzyew8GpA7TDLSJfH-b5UXoDyNYoC-pSGi1q_O8QP0SdS_DCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utKE9BbzuyKMHaYte6DEgct6VmQXtnmUiGkUQeJ_LZiRFWe157SQmfgIhTHGjftojXR_pAgQnarztANoBnnEQyqaiDF2taiXrmpP88yXd3r3Q93_rlT3NNmlHYNbX7BxB800vNzwel923P-9Mz0FX63Mkj435H1mVb2YHbBOPptRkVOH3exE0G4Mjt1gFDbWONtD_TOy2BqUvRJ1y3TWQO0vIjr_BrmJs_Se2z9rtzBmxhH-YkU24-X7nljMyjAIU0ZhztvApnU8OHvxRoS5p0JE090Yqguc91_s9Ax30ucpKklvwumyN9U_H9CHaWCJIfZL16lI56CrBVhkLcr7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwJyKtaxixjWKju8qJo1eyJeBn6S5hXsg0p47xVFmSO91NU9G_92w8-lkpkQlreM-fBUAlcrbVGwdfwMtLTELhCCrWlKENfSwkJFQuHdYu4a4W2CIK13yjzr0lccI_RIBDG5r71Lz_iL8yXT5vPSIMwc9y1O7BZd92NxgM9BYkwgJ2NR7W6UPCH_tr4q4vFyQcOJ1_RdYyyfEBBiDyYVhflwRyYXN9M6Lq_qbXjEUtJLHl-ZGJ3h5aHz7M4byfQcCSl_CapaKQM_wNGPl-rDun6mi1q-3MMx0POFmeRAQRX226UQ0qm0wWhxvrJpCCe-5G35xHjlEucu6qEo-ctaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM4Quih3yX4717XmFnwcJWQ_oYj3-zDiw3OLUfHUU4hvxAGJ-gxvW5WRodoraxRWqm0dYO8Ab7UfGSLA8dGrIrApHEx9jbQvSPrajy58JUpMeqrpwXatTwfJcFsq_0n7eT8prm5840an9PWSSvSbxz73rUVkuZhv39pNxAcWSHYcGHgWZ-PXuROQPe0w-cD2WbK2VrDBvBVbZrJnpA3R9HB4-rhHKGuT95ct__WFS02Z-6Pgxlk1D1tptlvoo_IyLn_dxN1fkzjdbkRL9v3xxYlUTVtg-WKn6rxI8VSR9H2A7flWDe3is6F9hYmRw2dyv-7uSaEgg3vcf1pVqyHchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyBITnQs0C3KqKXsLMp4ua33BYRCqlYzdt2vS7nJOBf7fV1vTI9jdhA1ms1ke8h8w4bhu7R4zpbctB0MVnCraCjeTN3bNSwchP_L5PNIkkhjVrAy6y0Ook6C0GWk-7hIaij6Adtd7bw0zvQDARAHhnF3YoD2xXUhnLEEplXy8vlhJm1yYlal-JNBjCabQteaJhOzC_VPv-aK-kacrBrpCXltocnGS1RY-DEp8HfHTt5IUN9PHRwkVY49wDzUa1d9BWsXI9FyM0j_9mVwcEMAAIIPVSWtxfajtcYdHM7DYbWQXeAte0tBpmf-GeKsPGrPbV99Wt6duqYonyM28vZTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdkNh9d1EhBa-dLG_qW4FJg7EzFngpEHKMYAyChcKEkGmEdQlagsGTmHcDj7KwxkWSNHCSFTvKjCGCUjjexUtfaGnsvv_oopi-4sFPohcOcCPRIdkzmo_A3se8Q_vM7-GeDHdyTGkT8ftUUaeZTXdiCzP1IoeGdsCHQOMPfguSBnh-kzopPDYraPLI9y55Zd2tJRqd41sXjofQGkbQc_O-8Va0wKCF-S0bC3Pnat7QYlgXuqphRK3mqSJCHaiNNtvF0x0yQyG-bCzK2e2UFQtiWqly4hyCSDhRMFkBRNMzVgEfOnWJw3rk3gsp4gWGlxmdpcKjCYNw12Qg1u7iGgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntbVJHnJBvUB3CvJkCRF6Ups9iLjr6-aga6n0XmMcxfBI3ses1Lln29d_8oT_GUiBaS_3X1w854K8IMKpamTGcpQiUNYd_xy7Eb7BHbNstdn1wnQG0bIf99EYh2m-xDWwmLOOHskr1z7RqbCcWkZzYcQ68YGFru6CfUsR30zM0afZK4u-NeNY8uCTlW8QDxRgNfrsTe_AVyZHU8bwjVEGHppNbAJ-dYVnAhaitPACGox1TjgR5W91JhYmOCyAfYmBJNpz6wekSOXidaCT7RX3IDahuuBrHfDGkfYG_eCMDynI1fkrRsf6a30Ickn3EvD1BLI3I0OdyKMUehBpooVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
