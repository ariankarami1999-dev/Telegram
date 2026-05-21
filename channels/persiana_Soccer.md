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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 20:07:52</div>
<hr>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6J1Wbytal29L_FmGPKtA1th7RJ8g1vI8LQQI805zQI5oQNVsAlINsC_d20YmiS0nI1TYR4tqVRK1-V3eg7e2lIQ_ce1B7lCm0JPHmtlp1ypvA3QBFnAmSHiwelCImc-Fo8VL8ItYsJscKCIHhz1RncU6VpbNM719uD-xbSWtsjI8PwcVVFPp6BhgX29Nb3UgGSmr839OhhbP_iLfpNThMO17d2G6cZK7ey6teNfZq6jjq7wpeE9E_ymTfuRCXkMZqzKObfyio1Mq7EX8ldtr9UNDrXjRuvhkwNi417FWEyG10OPHx7Ti09xmQCDIPv7O-ksdLKy3i_Vbc3i2mh2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuvaL50hQz029fHOw8BvuWiGKprXQoMLEQ_XrW_e8rl5GsmSt7Oemkt9xtjD-CLQ9MyYD8LB5DiQShhDroQjxf-ZnHmM2HZ5i1sVeNmkaDtsPawSEC7syxg9orI0Segb0l4Tpi4DuWEdVOdXU4dp00PGWtddcpA6tDQ_O0g8-CSMTG8WuiZMKgWKuO8dSmweuZrKHtDj0iU_NfFLgzN6VPiXrknNCSlVbwgfQHPyp_Z7M8ieFo-0z1f-n5uYtdgg2Brj4NmXvoLUQIxwj4xvzpiWQ3WGNIZvsnn9IzvHy3meWFhHzSRsXgnV9K3Qtcuy8aOpXql6SzdL57VizU-rwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/persiana_Soccer/22212" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqqQ_ouYSkKg2MXRo0bFyy6Momh5OKP6n-9Yy_fOJU6YZU1SZ5IJXQ6MYblEmCEGIBmK5jGiEQr2eZpwoZQYVP_aygYbsjywaf917JpJDNLIFuZa6jJ39benD4ibInAyHrWEJ9h9ajjnJ_D1Kzs1J5iNgHoukJbn6DfwBxX31x20VdWsCEt8A5564n819BhElVsjWjbAAsowzdpG5ohYCfg3PqesKU3MD98emwIGYKkFBsD5hB12hcDv74wY_H8S6fb5N4CBRb9FVbhxT75YA-3D9rjyhWB2Z7yv5TJiWkeN9PAfNGjBmNj2Y-tYI8OEyS9m5NV70-fzZYlazyhiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsJ9ZhBpJiV4G5f3rlk4MbYvUl60ITqt7J1RAFAsTMDpeGpy7isF0QF-QIcyx_jX7-_Jk8MTgHZ-uk75NGa-HBRidZNBivuS-fxTM7FReaslZJialScVuflWAefzfrEDI-5ZMLYuiX8XbervNAqO7S7ApbwgFs4YwGse2sXnb2CrFncUawWP52E3A7D8NFaqWEIUQzN5qdQbsjNImm3gjV5rYehKav-ZoRlN7-g0bMzyRj3usWO0bUtl_GFJPdJqfGPyM2tQjAc2gj4lAG4H5ypnyZURsKpSM242dZqWbHhzPPJBRwIr9AiGhHlIiiKnmBQyIXjc_SydmXHTXxR5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJwLasdgcIA5NBEpOhkOqwCcMz8kAEMLW0qvw_I-0DqhL1z_U5OgrM-BW_rlc-032YDaFyRmsIE5wmwXlufFo-gSkMvMBR1rcvwrNXCOdWuho0EmfkbYmoWkXyNm1lOF4I0dIf65xaib-rAn0_rHpuDtvQF17F7yeUGs40srWgh-WcoLdjNSohfXt4YrvLwUnVSNhLM3NAR6deYlPN0MkbLIghXRq2XUxavkmz96IiTKBJ-dnpPIrbKjmIGksDcKT82ErXyewYGaDqpVEcY7X87PP6jUqpa1X3nCRMryYtcliPcHrGTZN3i7xaTik36s9Nfibc0wMiPUNqf0_P6Zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0CCFXfTepsOWaOO9cGSRa9vT4pJcCd12ZRQsziTysnlXyqICl9OAJKQ6LFRb77gSQLYFoPM6VyXG0UUHMm1ZIZv31aIwaRPQAmqk7XfEtOzwJk4fdXa8SCBctRBruSAA9ImhoNbhIgjTG4WKhF0XilxMcdl_loi6rH9sn1HuR9QD-k1eiV1mpx-yFR9Ydp6uoqzJYwH2LyXwFhs5FuYHVuzse6zkmeDcREaEFYPi6lnjsL-CaYfWXD6R0Mg7xXjRE6whXtJMvzQ0JRIlbu8nq1eenLk6z_LHRpcodrkWFSSZ0m-lmKmTJ8HON-sD1G15yi-oMVIU_CvoHhU8awqBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHeIlOfTFz4wR2ljE-0B5VnSfGiXzWE_I9jOtnp7vHQK0PQURspy43lcu-g35VbplNHFDQ3qzTBQlX1L4zJ5iWcEo_pDdwREk5OSuC59Pgz3XjL0M3_lMCG8Dj_pgSa2k9FwoO5YTWiMJcgxL38SnZhErsUBlpGiwt_anzfLSJtGeyhAoHI1s90g75M8cbENDDBvLuo1xLOrMd4y2qRxBdStFjWLZMbaD3bUzwl3Oltf3G8kKOWO4p4Qdu1T1QhHLOiVJ2S-wO46vBUri-Ygr1y_53Vc7E3pdrlu9e00yZpukBDITUzZ450jnQmVvsT9r55o9cLbesQD5ER735ST7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvSepJ3eCFDJC0OuxzbN9q610oTJ2lTKkss656liw9lHX8yk387dHNa2CxlbknE6aKUleUaGgQP063JVct4KgRjJlqoziI3ibW1YuLmgeAWtzsJzT7J3jfqPJyOyK-3UjfmmmH24gl_fToXuksjwlgPKyGbt2L7GD7acXY8y2Gi2g5yVKxz2x6f69Y-9qxrJoJS-fHHdpTicelyvM2mbwD1DBkXog2S8lWxD2Krgd0scK45MkCARTK1IEZckdQSPFivnhW78Iwrx_6MW-6dzGBTt1bRHOUSAJ9V8gCgX4wMe5yos2QjGR6muhoynh_3Hm4nRh0I7lEtM5f8sJnmR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0XbjV7C2Vhf50gPJ7dhaSTNxQcwBDGIKtCn2RO8zAcWSWCqU-jfVlwGrFN3rqz-1sNM024EdDt9mRH9Zh8Ah4fpEsV1i7paZ4MojAJ1I0s3o7hOLihwP1bBcy2GDWcH6L0Vaaeb_VLhJhKHcpnFMFpyX3de89NW7XJqne4CjKV8GaDGuoebmXuX2TWHrL8zB66ZAHSzU26ovKYRk1DmvI1OUOeuiDQKdiBmORDhO9GHFN_zJzFxNlruhh7Q8lAmGP3QAgqSnbBRuvyt623bKsozVKyVuC0l6GXfJG0-e4v6Ch_ZC9gAHcdYCXjNST7JTUf2dTxUVwghfr8MlJz2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhsoAgDC9utop5FVjgoix9OKpr5qJDBgVLbMzQer6wWqvwN0ZO558eKfkVSla46U6G6XjOUNmgUnd-fYjAgyq37GSL0j-cuNwIiq5O09J5S8F8CP-a9lDT0xdI81UMuCy8McVz-ONDTxATNhssVrCa5cXs5-X2FRg--Quadff6UNrg0VL444zTV9ADzXKLOFphnrScrlyH5NJKOMDw4TaLRccaA69Mivs2Yu7gc5cZTVglS5JXJLd7PELBq080f300uFFdjavxpnTrP5J2vnDtZdTfvfI6ABgSynDePtGKRi3CxbinfqtSsR7-BW5TRUAgr8oefpUHpuQy-DoR79nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCtYbUPUjjYfwaxzfQW17GnUtSLokG4uWjQ-WsgktmY9eE_850HhZHNW7H_yr-Jlc1LILRDdnXETJxXgrzWDZTPIOZaaDKiWWxcfWBNb3lzvV4RbnLkq-yQ0hy04eK1J86E5IU3lGwu9AuUgtI6ZhGQ-x96QarW_HHBuBEEnJxciZHytfsXQrQ5qgggFmCTaBl9qfmab1HvhdWgN66M8F0ZN56VYEqF3sacm81jLkIi8gM513XkcdWja1kecgzdh-2V2OJ3VgUhj2AFlFIYxf3Li6kdohEUS9xmcAvvZWrqre12--ungU2ZgJ1143miS-bU381VcS-XpjkwA7Vz5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo2U381k8RacnMdCf7Snq67dDgliSeoIVooMQlXHH9mwXRRvlwjZqvriHy8wpA-hKaTdfpdJ5pvP5saKy2BdIyYAV-qwDpquC9c6OkXK27yMMnEjqAqf2jvEf1nXesfQpd4qFmfCWDsGSjYFwNGTiFbdNCb2e4V1lUFf-QTvWKHyxW1yVZGARk7v0GF-9MUNlXZJ5RGTICrVL30MnTMlUJb7i3UT9OlirESLQ2fFHrYOCznQ9Y1iJQIBBMSr3YYiw8Ad2RRzxSinzJMeRQPYLckO3Z---kLk-gRJKiimMc1m-fMWALTAXIJ87AR3stYCKk6yHFmzTJupn1XIS5t3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmdAcPfljIessnZgdqdGENkydi1NUV_bZ0iO_CsetGG8khxThr4iz0aMU2igUECq_DOvx55FDBTkm9tNNG8DjjB-zSY-_aI5FD2J3qK8rPsM4dl230wayHrs8QnwXcCeKdKuoW4j85cW3NLJkIbaTvxaz5qAoez58tPTpcdQpaB0L1m8WH_Hrk4hJNY_vSlOdsr209tkEzi44aie5V30uDdgZIXbY--c3HwlsjDolh9LXKgMJPcBPPFuwg_pg_4T7emvHGaVpbtz91_lSTUtHgIDiTBOVveUIp6K76dw_8W5XOgJEmZoaCl1kdljaOYKunWR5b5eWh-SEyssbLTtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnhj_gNBXkE9QVjQc1HV6LDRN4cCN4mw_COizkJmCbs0USTJHX-D85T5QXn-SnhKNHpysKOCjbN1boGhuFzZRsRkm0VFUIQ0NZg_U7FP845zPGvmzDFEAoV6cI_uixHunHhV4DJjLTYaiwGUqWeYogslFzSohqmuxpdppwgsqZ9XuKaJOgRbb7fRf8Yc87qouZMjaj7qNF4YnVdqW8ubfbs_zTLQzsMowbQO11ZjkK8H16pQ0TPWHAcKVDaTwum0qXnDfzVbYhy1ERDYHaG7Fz3oDhb6MoLJYGp6_B7vjRUdp9wOn1I4VeF0PDG7tpkAPJzOy1R09Drboe-lOezWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8irEBSi24CzFKH1x0D0XWcm_B4-P3PfNNh-s0EYd0BNTtbRZIM4Be9R1hMB--0vMpdbljJ0cDR210XMIHi4a3iDBmT7x0oA3xalyt-VKRqZ6nDx1yq1F9Gn5apK8iCV85dyHCvUF3HSBpCT7jXGTqE2zDggyPKljXRxNk3ytVN_X74a9a-Zu-yG7VXgph5G-HsWj1eerGR1qei4x1KWF1SJ7XSR27xTLfm509m8U7qM9b_sHIyw5IAqInI4y-MPShhY9rA4OfeWdWvbTr67cdboOBbgJWU2EJCnHupEIXe8UsTY1cwAciQv7Vk1hCNfEOE2cvYoOpaGRz72m4QhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_0PI0dOX7-zaI4QdPd5hcHxBte2wrhPa-EZr69GhtxGqYNFQ3wGL8wzJhwv5gXw1e_eT8NUfhru_8PBcWUXYQvZ3hgJcwdqBGs2MWTm-_DpfYKNZLBwvhMIQHehh2lWb8fb5ZKdZ8jDlXx2p9_BizeuGzZA285B8kOw1wifCqG4Am5PrnIPJqJ3KPW63DQf21pjB_EH4yLa2BbFERFose6I7UWotfdksd2dFr-56cTYEl8mgyakekKsG6g6IxNaoAqF3CpTRzq9JVG_qNWVhTt16MYWWubbGcPLTyxdboYP1UpFZQ-JcETyr9SVpoZELv-7c4keLRQS3JncCAxh-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flJSNH9yebNS69hUdHSDXLsyFTe8aHZsdSJsOVxyqTlb-TxOwfiYAkLZmOsd0DE8vQBflcPBcl_vtp5o9OxbzCvSWGyGVyGRg9ID_xRrjOwlFpQ0tP7nS-Ax19K1rHw8Tsi0Ov-Q7jArXu7JqPemYH9x7YDp5qmIS2cbPUw3ogY32u9upzOcfdt311zahjPQw7_xq9CvEpfyi0tUEvLa0r8fOUEHG1tcHOJlwcpskVgSs3nXN4LuVmdoy4nSu1KyQEbbt9ev7ma9ngQYweUDI4Wl7-Xg6DK3IyCAJ-cs6feWOXZ_LdAh_BqwQiHAUSjXH13URsbgU9fjFgKdMG7DfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=G_W9HuD97oE6n3eJcPFG9MaVX9Y9PqGBEMVaqnru38sdQ_8bIDlNGqW30yCjlgTYT1ev0WeQHYm9ouP-Hmbp5iN6u7UqcSbSN_7f1GWsDKjl4cW2j7zyEYLf1zRMNPBInRH9Lf3GM_s17HVoowlF-Wd4X_AXufL0RUUkXU5381GiHjdc97SBpK_h6gcmkTuNcoY93iUr1w4jkBdeQy16ntsxGmfVCauC6j0-57NeQTxWMsZ6G9qlv1bpGDqEjCuBsVTduPUwauApIiAABydjd_uXuHVnYNEdMuj-Dgr1PWtu161w-E5EKSp_iWz4o9gu1XRhkDAcAUnCkMOuiz5Cvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=G_W9HuD97oE6n3eJcPFG9MaVX9Y9PqGBEMVaqnru38sdQ_8bIDlNGqW30yCjlgTYT1ev0WeQHYm9ouP-Hmbp5iN6u7UqcSbSN_7f1GWsDKjl4cW2j7zyEYLf1zRMNPBInRH9Lf3GM_s17HVoowlF-Wd4X_AXufL0RUUkXU5381GiHjdc97SBpK_h6gcmkTuNcoY93iUr1w4jkBdeQy16ntsxGmfVCauC6j0-57NeQTxWMsZ6G9qlv1bpGDqEjCuBsVTduPUwauApIiAABydjd_uXuHVnYNEdMuj-Dgr1PWtu161w-E5EKSp_iWz4o9gu1XRhkDAcAUnCkMOuiz5Cvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQnDM-fH3drWn4opf2J-pBEBHz3JfwVtWdoXhuLxXo1alTSL-G5i-LvO9jCs3t9NOoURMLfyV3k7WQ3TKoMJo207kkPS2Et0dpp8qSD-l4rPMACvbdELYkkN7g30pxCoH_Se07onsBis7aYFDzCX8oCBIwDI23i9vtwVhHcab7o7vG26GDRMzsM9Ou9O293vO5sxY20ZkPn-vTAgUOYdRQ9OjZa0mLrJOfdFmVpp1R2nabQ4qcPd0eU49jgdo9AqRB9_zbFTJvKiGC-NdS1qERtgYkY4urPTBfd6ro8lRyw7QoQUOsNcD7hIu1f68W329WZh7K8Y3tfQFO49cQtgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4N8v4XmPL75fU1L5wqOi7Wj3l8XR9Ra_Y_o9h2f7elu2zODtg1MMyFe0397mFZl07e1P01csivxk5UbZJNl4GVRjG8lMo8g1NSELCqnNpA0WQew770pXX1GtKMM2gVAjS9uXTTZDbopdKdWie8UsoyXx_4n0J3tTXZWCHxwbqdfCBpyJDGbA7PCmkt1J1ksQRonbPQYsoTVO9mmtg60kxDeqhS-yBXTLhNByHQ5iOnRbKlv3FR65ZzIUvqu6TKvXEIoR8sZslxk64TLlJp-CKXvhI1Aec17plS4InoVp19gS-qTDHAJxvDcrr5OrghYb0Zn3nvo6uo6pra3sdumaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE-FnrXuI_WU7AWbcH7gad9Y5ywPI3b0_svR9bvb831a1CMGk5A4o92LbSROfmhPgvk68jmhuHXbRAt3q7hwvlywl4DmWOT9JJax8ZwQHbeRpfySv10XpJ8679ETt3J6nOrnF1HLc8Jqvhunj6NnP5mR8Pn9-U6xNogJHfiej8YGkce5APlb4CkQVDS7TI4hiZG6DdWCBQVLeMr2FjBZha2YfHh2MxzlIsgBpV48arSvt-5xeCI4cF-xyWPTUAZYYajO5XLnzOe5RN48rNuysK0wAvXpH3Vm1G6Vr7pVL-OzcAicOv4LwNfYI-GI2qkzbIe6BTdfYZmoQcmlg2bILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPOxQnmbh9jYEU8DnCSUd4werD2sCZRr1XNM4B4s8WOfx_NNrdMkFsDNK67By2OeDxGx4GnR_RdnQQUyjFVoSUHap2qCBAuKlCc31GYltowJ6pBTHx7AVXqwzKAUQrufRL1MXet6cXRWroryeRrf55Pho7holcd6umCI2sl_AT2ylMUqesUa6US95nlK_5S8Ooob5g6a1CrNkMIksWiwRAzOzqZs_zvzmKkPwwwIERUkIBGZItUyuUFFVHN0uUR9ZUMqYtQL0PiQ7s9Ea1kNDuSJd_8jZApJeG-9D668zPsXBFybWzd2N4ZJ007TevnVy0LpiHotvfmeUZmlWKmzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEoe9Loz7K8N0tvME1PsRcj8KZK2IpZ4wXWhCQukfTC3zooP_M4GaLZk7K2GPi34HwsBsTZnUpFuRS4HtR1mtkZpMGegmhHyJBLeQRc6VkfXSC82QgzrwuLj9l2rJGpNO2XS6j400IqaJ4CPJ_V58zHEz25raBSsPrU55cRWIH3jY6iDIZzgOGhu5fqxnKkf0B8pWR1oZuuzl5XfWNEfKEVXcVzJNUAbplvuPl_4FNDpUpKt8zVaJb3ahcsK3JKwvONAf1NfYJW6URbsuHa2AxWKWGXHYgMPq-b5eWo1FBtfnrnbMelYx7PeqUgln6KdvuJMevTLKf8zIKomNojORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWUGBtN3i2Lys7svm-beegnTnu2coaINAQ4CB4-r4MjhRTWq_wHXeLzMGURt2ePuLSABUJVi4qdUCG2XGd8rDja8A3_GYsZXamodtgRm2Iw19yEj6PCga2oIBI1_rXABIK5bgGczJEKS9lEnOQOcy6u6BJv6hc7cD0ySqwA0sCzvTVVWVElhQOCddaikPzJ9sAF01aE82KC9lRU9K3KxFsGBVjfRX-OTOphEmwUAWkv6pP_eya3u0k-wX8ew4zx2K8i1Pj0urR0R-DVZ0EErAz9yJWX1GT4eF3vYEo2onIcwwkhEA15y4kb-ExpD5vbeW07KZ1L5hU-O9_pdvGKqvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuXeS67rtTVTteahsEiXvg4SR5VUDeUH__0Dz6TXHJUwmW8NzEjxYp2julZRSWdlDinzWqFToBNY6ceFXLFF8WYpP5AFZJO8ipHbaQxLNBoyUagPWIkhiEIgcGx81rEUpe1e5W-n7OLBXqvA_qoBuXHoh0NAeUcz5SDgYDfyFhdhnObw8BCm5yjcIc6065nPcvf-thRA4ig8bg5A8D1poCtP4xa_JcrpW67ApsIGATwLheOliZJJglCyZxPWdfR7o-MlfNYij1LKyYRZo-46FQD_GkIPi9KO6LyKBElNThAqM9b695sABiDwMXIsRqD1RtME9PU4RlenB8P9m8Hh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF72XrKFbssyQxvl8QU0VeHIltT_hTrMQD1SeFXBxVlV1XvVZI2DazDTWSvW_povFylpHK4ChaRKbAEfDGs-HP9YMq_m4kGjsJpub3wa2uYOQfdfltUj0xY3QC693HHGO0RaaPkM-4Ucr21S2xlBE4zjKg8hAWt4DnsRXbnMepBonRcgg-_wwEZbR6qQ9NF05poesoKKOi0hdxiVzbka7eqBD5wy-0fShOmlsJlGfhBqUPolxfbG1-fLrWkKWDQ7NYCIw7uJyHT_P7Mdnh9lpce-X02oQcrFvs7QhqWCI8WFUsCkYMTO_wvUQ-VHVxWaUJuxRRKH0oM2oNg-Zw6HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0QkVhcF2gPcvJIlxX0c575CI4VNDcS-2ZB-HWz83MUohObRiNOBICPSK2rl8Two4U4lXc4gTUTLRSrPOP8xJLUX1_hkMD23FrlSKluQxdajBFMedWfof0bFI7UwRH586KVnKPmAKTR-7Bgp_sfGoMX5AZoSjzTtkMo2Xb_dgBsmYymnQtI5ba3B509xMCIRTkAovWSeLHeUXAg81FPa-Y7mF9D6ihOHhzd5piiD4I122AAecjedMLHROSKdxd14sEBCa0hYeK_0kMF-9ThV1Dx8SJn0QHdTqSbyjPkxx2YC9t7XoeOFSXvhS84cSTj1iP0QKM7mro8qEHrmJDFIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=D8b3KXq_tpie_KI03UTSfOKZVoLVUz-UulVfjXw0jdf0MW0f9J5oYrOgdukX0_DUJMqlghNVO6evgx4S_bbqYK0Vll85lpIvhnuDUrvMYsJB-hp_4PaRgsLZWtp83rf2R8zEFqtfTq3w-uZ5MyZrD6xi9lY3HKhCH6w9eYygsdHIw8yvf1rqOwHcU38-WrVs9hFslj6Mj2N9VC74LznaH9W7Uk6BVDVyYh6xAqyGoFEFU59ou9GOrYJKcBPeVnDunaDmysb_ISoDI3jfLBZixXapUTWMBr8bCCdibS7UmKCtzmfoo4n2Hy62XdM-Fl-2_ct3mj6dhFhZv97Izl5C3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=D8b3KXq_tpie_KI03UTSfOKZVoLVUz-UulVfjXw0jdf0MW0f9J5oYrOgdukX0_DUJMqlghNVO6evgx4S_bbqYK0Vll85lpIvhnuDUrvMYsJB-hp_4PaRgsLZWtp83rf2R8zEFqtfTq3w-uZ5MyZrD6xi9lY3HKhCH6w9eYygsdHIw8yvf1rqOwHcU38-WrVs9hFslj6Mj2N9VC74LznaH9W7Uk6BVDVyYh6xAqyGoFEFU59ou9GOrYJKcBPeVnDunaDmysb_ISoDI3jfLBZixXapUTWMBr8bCCdibS7UmKCtzmfoo4n2Hy62XdM-Fl-2_ct3mj6dhFhZv97Izl5C3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=AGsNZ1C9nixS9DWNLIKoBIxP8qu3cpmhZ972w76KQobpjs38SdioXC3vgGea6IJ0zANubHZUb29Uv9ZUhE2sqYjEm0egG7wN4pPt78aDDCxQ_5V8ivSyS1rhJy-AdtBmonJ-x4bIbEPkTYbNGsVWJxgBSAvgXj0HIdGv0CNZFuhsTxxIYYwdHL6ScCiRfKGzbbT6Nvkjbjyg-weGRwKikykEYmTI5BTkC6xRwz3C1c3FKqAOh5AuFEQK3LQfxfySFJv3DDnF4l8QBR8CchyyRUmhtmcSfWgfmG7d-OOI476q1xZY4owJyoEyKRq-aIVoIiatfciFxMbfTw0sbbUBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=AGsNZ1C9nixS9DWNLIKoBIxP8qu3cpmhZ972w76KQobpjs38SdioXC3vgGea6IJ0zANubHZUb29Uv9ZUhE2sqYjEm0egG7wN4pPt78aDDCxQ_5V8ivSyS1rhJy-AdtBmonJ-x4bIbEPkTYbNGsVWJxgBSAvgXj0HIdGv0CNZFuhsTxxIYYwdHL6ScCiRfKGzbbT6Nvkjbjyg-weGRwKikykEYmTI5BTkC6xRwz3C1c3FKqAOh5AuFEQK3LQfxfySFJv3DDnF4l8QBR8CchyyRUmhtmcSfWgfmG7d-OOI476q1xZY4owJyoEyKRq-aIVoIiatfciFxMbfTw0sbbUBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy7H2jeWFFbLVx_CZHwdnXdwL_pWKnou5KKO0XLqt2gLj7j2jhZL-SqbCT1VdCC2EA1_NZgERokelJL6qp96kh0L09sphcheNL3SO1W_tWuDQJ0ZU1ULo7mqkIbMvOiSYyQZD4cP_O-4jTG_ekzi--em0kUEGthoBAYFqAYB7a_48ZUAJl42WCbNC0j0yz8TeCFVx1LCEc_MuV3-xHuUPs9XbGMN8uMwlwDrXzD-BlFoqEBhcdRcgvm_BPSNj-oHlmizlUTX1fDfDoWsWvNpriBfx3xkMowAlf5x6PrzVP8nbk63A6x5D4cgarK9Qj6Tt1LN1TQWonWXDtkdUK3lXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEam-B4F-GQCRV3JXEMbzPtVfYuW8Rk_OB3s5VRe_zgSBur4NZfb-psP-9kXR66lytYTzGV1zYh4cheZAiN46mj-e3likm2k5vhn4oNt-sAvtEL47u9Q1-rsPqahCurKLYy9Uiyyb2SrusfNu3M2fOaz6h99npx22_Tqparon-xRpxKFj02TA6UwUBg8v1JzTG0lPZ3PKz0T6ZG6sFkER1Ps97iPN5OhumU7JLIgemfn6xTtm90Ipnos0lLCZPmXWklC3IsDmT02WktaHWoLzPtiruxGMP-M4Iwv8EqSYCQh6YswON6AXxM9JzcS7JS3_WjiLsHJwVs428xWxpYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4VOp5EPaJj0RY1-TN12IavXiK5TG7W7Vb5K4-kssfW58eef7p-CFo6qQm0N5-C4vIrqKpMTW7HCv3H0C20sX9aULgz6ExdIIU6OwuItIWSAntc91cFlyHcbfkhCGkqX_CioNJ5zkhdb1Ivg8Ox7n2Up1LZR3dJdmvu21HQr4R1OfA-Js05aoe9pwt1uP8RlwBoYgL3ec6KhR86JnLbOD4HeK5SFgDV0z7QPo2y6eL6IiGHZPtBSaFMuxQ_2FzS8r_Ve-m8y56N5cCkX6SGkpgme5Wk8C-sMaoz6gC2JFpr2PBC-DMLkAfLAWVP8n2tiQHsrt3uSCMmLrfzOOlvVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJjFfu3Fuj29zAh1hWHvJZPTfYtEqTOaS70idvZtceHK3GaHD4Gio35O-5ZHRoV6b4d1sEFKpHTT3IvWyWdOXOIzAV8dPWH6XdyuX22lDJRyDWsRDVKptr6PTPU38ZLJ8ZIJaMe1bQ3bJ5I0FPlbvVFE-YVy0k6OKQOQ9bFkfThJuQUnZP_koWaSQH2H0OxMTnywJjv9RWM0-eGqwQWpluG87eNHrH1dKKrkSg66N7B-AUwqO2PFE7IyFy9eY_4fXDUJ9aJt61xSU5MALJ0QG77F5I_Krx647nYO-4eJhuj3VbemodVV7Jow4kaQq5Zeq8V2SdM9N_bkWoAnI6gd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Rln7ZGMSGvw_-csnStWrnd7rJiQh795pqDUuEfWIroNd0VvSCsLdSnPE2lG41axPDqUNLvZxv37C89XM17kXX3F-TkPc7Sfwfq4Y6nOTT19fc5jKUxdQPJoYuMI8ROpNoI0M5mlvktkIgZA75jPBQNJo4WDrfgVRueLRk6gV151XcNcTuFSg39rc5Zb04dhLcDkcjLmvg_0b563C5t9GWGkkhaikBBv1t1pptI8SmDuyCc_IlfsTn28zun5fgEs3ChM-9wYO0PuXBgttSqNxPdqJg2BN9VDKG7HbkBRLWlwE0OphTpXorxG_aiqmd50d0axyZgSEV9tRGbMsVRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtnpnQp2slC7HkBRfvmZO8ItCJJjYS_o3vpOj6-YGFTLThAnYDFFCqJRRr-RoZJvfrWRzhJ_Cuxmn4PskoeLwNb1BeGT0Eom0rQWqp6aywuEfPEHEcHqVqv8glVMAYBQgONTaIHO7c-LXkqZYbkZaTcD2E42qM3yZRfV5t2xONy8C_Ni11zbgMpMnTt6QOPCv2V-h-G6X1HspedMKDXX-bc3pkY49NUKC-QiiEsrQVS0oNnQQExfu5MLoT11-jF151lYx4ndX1GGdb6qcBge6xXHHy3bwFZNqtxX0HhajSWSxThFnKqyf8V2alrDcvzvo3hZuhvY5RT7stQLT2X7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTwW0BMvcoPFXfIRbMqRKl59witDCUCMI4TgHrHGC5OHxd2T1tJbPGmTrmUd9MJDQijQrq93hEVnUiNyPRVbIKLNjPOORVGsMlw3MdAn-p0w74sLXyN-dtfSM780GvkgJzhPbf7Bbiqnv6bxzmkF_DrIaKWfObbUY6oGuio5_7cI1MHj6_X2YCeFUGiL6pHT1uvGF3wJPYro4NvvYfjV7_u0e82j7_GWtu9FsO7kdI4vIGnHgzt0d-nCtSViuI8mQQQvJGSWfXWNVTNqRRtdIGmPMe6VZ0fmLpmThFi5iuQutGnCgoVbfkCLnk22l19Osmj41S_pTBgSwB_JI4vwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OipbDlOIN2ztV8cOeMABmpFpt_Vl2uddwK9cqsznS1mBtvyNXA2k2MpeSqe2UHga5m36YQ8NejQITM2GB9boxyqHUN47hWQdvolNQcIZ0UeGMbkDpYELatwq8agPKlwjru270GqPOsLo7MFMzfG6n54s2POg-qXataxvH91Q42ea4JwqUQnpmKPPqGtrFMCxMjHuVpznSect21KoJln7SlA9mRoFZ3zWCW6jmLovLTubkl2_SD6Fi5An0QXRSeFUCioVEGEU21mcbztck16QascvE4OJvIdmEI3MhXt6E0K8k_7uqPMflwt21Du3KyfWfQKhxxxpN9rtT5uRuz_buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z06XccoZBuuNyx5geDdIpWYYiuQ1zRj_LURDwjzeFNaTBk616DcrHY_YzvWYnQ0-LAnEQnqdmnGbnwh_vShD9nOTKEOdOx49kEV5-P_8E-E4Pl6Rofyc9DZ5qnIiu5gQavoEaZ4_KQ2K6qPoa0n0aQXI1aw2mNZPFruIlSTxPmAQbkLm8_i2vPnmfoJNoKM1GS6xU6LvjVs8B_3ympPql3NdEO7eWcrU06Mj9HsSPso0En2L9_sFf5dS8PXnMbYKXEvD-ok_hWGu3BvQR62BOJhd6VERo_XPhsOy9hZnwXe5P1ElOxpgNC5L8xFDbOVAJK53omY9Lslbs9tk4hBSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_t66pAjiYHaI6hW201pX7jVWNspCeSG2Z27jl8NHzBfGlhR2TgM7FB3EauMHWsTy8NUBxL28j3ZZ6PdR-f94LTgGIL4Hk7gmJ0tcHsPb613F2ThhVH50V7z_iKtsoWzRFkcAAqzRSel0zV4y7SnyZ-KAM4wWBgRFuP-UPkL4dxetU-9DSy0-RqNpuB4oUJbW71qdRdfv8e3jOYw32hvQn2Cz2nCKa0Ij6y1EAEdw6gfyY4tJj3ozp81XxrT6RD_lUx3tKxuw2QJ3nKGPAkZgFdaVwEWw3J7xLVkkXcovMIq0RCYFlFyXDb3Zq8xC6VHBww6SgYABJxOuMKy5H82nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrT8zKxkYsRtWT77udPJwalqBwraAPDqeKR-XqDHtr1SKA2WhVuzORn4KOD9fP4qZeNWsYlhn6bjHUdPogvaGZOHA8AAmKQ_Nu2YnE1yyRMWeHqODBBCW8JyDWUpW9QEo7_kKvquBhtEkDe2Q1RQsOJgzkVT8-0dZHQsc_Ld0Kzl_KHy8K_o7sHS3L-cs3VevgAN_NValhcf4UMCTfiiPqb46EwNLLu7oGPPvm37ngJO4PEnc2ABtT0GZMgcJQirbzb9SdvAgp44CNo40i-70eU2H0jeKpX2hQz6EHZQt8f2GkMuuicHBm2oXWXJ2MPzazF0LbBcP2U3b7v1Qc9-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2-J1HnVIOHGHKOyTD9B_B8r6fNLUrMgylTw8RHSZN5bTL8r8FHyTvVw4OEjSgDf4uUbnwEUehnwFnOYZOkxuhwNZKdqM300FUfUdjWvPEeRn1knX0BPdcwdcF1HlxuWBNTpshgZeCm4qdTcfSbcAUNY9R4J4UI2EUXFMSHS9dd9vRpTob1Z1zFxIc5DzvHTCuVDYB2tIPipomQNu0Vns4lsTDuQDOlUpBo8G_4IosEPVxY0zboPBVZzP2ofzxXDy0PAjxHnJQUrrrO2NTwnMODWWTJrVpDtitQ4eujPVd7QpU5TbCukjl7YDChADhtsu61CvBoGuZwKMAfyke1SCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjvcjL5PeUtKrkQa4CodXfSkuY5xx0pew95x1H92EjfkZ_OSgHaL4AwUSrmip21b7FagDma1uskR0_M9b5XUQ3vuYI7GaSjKVYYSxiuvPqZabNBbs1BiDgnG48ycfyfpzubkbGz0PVOcdQadcrJsClhCsfnvb8Xn_X0_YCZN55x0JVmdVeyGfXqv82-LSpmvxGXE7PyYEu-MMBRuRTjc718tPci3Zj8is0Vsets8-2mDyHWZfuIf_1xtDN-jbf3yzxo8hy283Tp15UG6m3okMGrU1rYHfZ2R5JEQFYPbPVm3ul1KOSkaZMGXG5WayQTCsP2GDLGODlrQxMwPMRxzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvpc-QP6WQ5gMoptUyY_e-wnmfoy1WEjUEa9OuIdgJOYv8SGUH5s5TTghDBzC3LeVbQOL7sJosLAzQSMFig3xP_0idC_-oBFtR8Xl8SGakwStgP0qPyQUV7qSM1GhzA_4UD_LpV6ERPmZuxiTXiXePxJtQl3UJ15uEhrcMv23lOpCoJZ87LwxA2DV2mLmAXZvCg6-jCL5lf-Q1yjGgAQDOxl6G0auaIKy3tWC_bbVHePXYoJJ3sDK8GwCYQzR9g-J3lYSRrA6v77WCLRunIVmR8YDo2NrqSmmmQk5ZLKnXbQkYfRGDAdNTwiGC-YeWDVXeJbtMS5oXL2yZxsAyS9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFbG-1cJhRTWLJA8U_YX4XIZUc0Dk-g5f865r907PEDv8QYwKt9AsSWidiauREYImduBq93eDSDwRxGzIdbZMTE35ZY4xraUM2a48VdNop_kWr1FBRoEPkK-j7x-wr7t9gdfhQi2iY1Ni5FCE5YR0ZwR0U0gs_pa_xySeY6kdGGhBPUHYGZLQxSkNBTb_u9GRRFpnsNULa8DwxE1enE0M_I7K58nCfOV2c7ZLZ5pYqNeJCuGYIi97P4fjksfreNoUVqwPyH2rAb3QHZAarCj2vzytfGHzIz47GD2_DO9vJONWu4lVsnKMpJp8rS0VksnremC3ox8As4ZbJARepFUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XipP8TbjA_B9vl7jUxT_3dNvDPquLdU5HRzicxLhTe5PQvUCP9nSi7xhCRtqdrSQcCYAFlfE0ae5V_9iBw4lhUHuNEnarkcwRkCUdMbvdqwyDUNnSEBQxMTteCQhfnaNoMrBP-ZLIqiIbrPsvLJwNYHaFpXzNFaNc8bTlPl5fbnsyNCMQD4_CMohow7b5JF4sceypahIfCrObLOIq0OgpRBcpl2Q_iKalm3Gy_oNPjkOAorAAGCOEyzeWvZUWlGL-ayTWJ-H6xdhi0dsZRmN_2KJPICNMDlOb1mhIfEiK586CG1oIjopvcQVMIoyMjKElJfQ75OSyqgLXLeH9NwiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTJbR-LHG8PA14jYV8hTyQ1cWRBSzJpVtdSBHnZuTw1aMZPUx3XTwd26iNmB_Gec6MOLSs2YHW5KPtj4GR-OkdrOT_wiXP4j8Eq5XB-VhvcMcuVdpotr7c8l5mbm-NvlR8ArVsXDVy-fanGYwfAqlNRiKEY0DW4NDXKdmM5_U9BStrTKBXBr39dvT1nRmA8bCR46yo2Q9stKTNYlOEUWwEjjpy4t9gAcORddYWWeReEcyHyDPeh1-6KXy3RHAZuCH4iit_jFQM3idYdIIQmzT5YFVtGB5fC7h4mqHEljbaxkkagrBran-HN3yG_wQvX4hYtt3w8NJEQMjUi6mN0LxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2gF_H6R15uPXm8c-7iIiBW22dp4eGsL2gegiiQreVMtGgNy_4LZ7a2gyboYYJJjVtG0jextrDn4C-iQWURAUuZDgz8bv0_Gr_b-RAn5nTtc29faBf3O6NV1-9eoL583vPAknX8QGvlwNVfhexw8exkgX65m_uDBUql8dt277Sms9WtjSMFQZ54DjnBaoYNxyAoGDd97I3Dj2_9NdTk8Z2bJrgpunTvh1Z50TcUhM27FtUFGuGe4C2mY2Peb7MxbnXj_faxUFzWxnbUBvhq4zENOH30QF1JATXgB5qL1kF5Hzaxpnb1ExzxL77p3w-yNYvezBf9cY0MYEocVxADJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMhTyQJdCq3d_MyHfgc553s-bfMY3CnbczN0KcoDcxlHnP6H2BPKaO52g9kRQJmI7EzJfFpTEW5wFBD0dffeF-SwgkZ0RHS8_ZIWHWIvaoiNwaVrZhmSr6LQGAGYDQRLUSXLPIbaOxflcHPVIaGrLvO5zEl1puJom4IKi4AljXr_qNrOzYOsGouA3Kx77GVl_8cjIWRHuBjA6Rqq91bT3G5FJsxzKvwsO_QhyMa5vJ22rFUpE1K4nvCa4i-HWpgCkzXh0ah3-sLmDBnAPZO1mOXKAIbRYL5ds6h2qJMrrZEFdtJS7nXIRVev4pQkWQG9R1JzERBPapm3PfmjOKEltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuftp3vgbFYjum9Ct4wp3Hs1Am3ABTxeZigRdJj6fzmeso9FPLzd599qXFCdn1QAlbv2pk0cKF-nZ5Jm5WfZ0CAgQrVyqlZJXpzfMN08xmTvrkITlmCYdq_EhlDG4_6DY89FmENFN1m4_SKlcUNH0D3oVx4qUg8hmMX-yRIaVZd0DOlBIqWCRJVtOW91h8wW4gILYUXpzdlSnK-zrbGfeMdParbtRM2Jman1vbEmGI_5WP7vJmL0t8QpP4srGA_yjpqNqqTcpzt5rGgETOltgjhTZ-_jKDdh93uq7_B6DWevbsVzxTCUD9p-UbjXiz-v1KFBHcowZAzFKkV6bo5tSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oit0cYFH9TjZBq9ZoGR1IJQabqvAkSHYu0N-nvXbC8vXpmrl90-xOcOVsdX7eAHQjFjW2XWuX5epQ-qtdx-5WJLE1_QJEANnO5-VXHKSckcQuCoJJZ4S6bWwJUVAKZi65mQILwu0_RsvyBlNf47chyHIXHZQGlnN8J5GqHslvDSqHL75zHBqmbVYY1wz34Dg1C92d9tyLHtarYlYgfgg_xxOrZdNiAPLvx1gAcGBR-7uh2RsIREjyTLm0kdl9EOnn9EEmZs0agLPniOy9kE70Xe2E_bjvpa4Z9h-CRk8xmNJOY8ouUTZcooCVYx0_bjLOlifJndYIPSjIitdpyIgug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVeamoizurKKMXyMTG4Y9ljz0NQnus37B_q8_o24kq7-iMlnb-zAu9bHgcCVVx38mKulvbFQVdeCO2yn4uk-Am2DWir5CijTsa7GNZPzF4k3Gv6ZcQacgZ4YdnBnPJP0mOgE2_8nGEbk9WlLqED2zJeC9l4ygf3urYKd3mOrLNao_iGk2qjn04yc1g9wl6o0Mn8q8G2RJpGL-ZlrefgtUPCgxfF2r5BTMKNkstWnt4pOS0bBGLfF87JFytJOwjIzMXpqzWVAnRX-ZRNvYaGRStk7TkchAuMAPp69Dz8tsde3OkQxuy8kKYFlZgek9pfi9mo6LX_OSo9qFrJdKB5sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX-JAs1wVtikx80TkXVsZ2kiP-dYF0Ye8ICR4HUHEmR7s26exIdS4ranLxxNL9H6LK5jpcUEadU7TeTVpU0ndFJhSO5fMJ2_9iWptkLdkuwMeqmCaDNYykx5LODIWazDn8UyNTSF0F3r4-jj01G8abT984-yeC1j6CeV8T0gq90uSWH5RZGTEtUZtk4kpl9tGTzKPzLlqJUrhamZDFApB1gfQrmlhHnnaDhQjMC_S4OGkdg8mAE-RSwB-gcWcetj3HdJEOuDtVtNBoB_nDxf_JCjmE-Z82xqbHiVEI818U1pv10CY6zMqNudN1FAmM832v6DhXiQj4jZVYlkEcJbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMgkXq5GG0J2MRe9uBNpsxOd46EtILV0w3X1Aiuvykc76J6qDMysQ0dJ0p63OjpwYFTjNnnx2fWFK6v00UkzO6IefPppjmNUi7_uOFaA4HOwhwhyMorM2ZjXuVf6uofs1g1_QR1DEqn8RLSk0I8ycZQn72h4Is4mmrb0pqrGcDfcxWyXIoR7BxypYRrQz270RDn8KOvdxxjRZ9iICCPiK_pOgNyrKpOAajVKIruRm94d8BkKh5ltlOlmN8F3Eu_ssocDY0rYYOS-Imjdr2JWaQO4eymQ0YQx5-zKbwt2qdpjypDEzs6f9xSgp1a77C6ZR7xTKUcMQkmpEGiYjY3O9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBFsOUAtlPsI0IT9wzfJ-wVUiq0-KxfLWuJcDEO1L8Ma4ZhLdhVcNnRd_418iTSbblKdXDdPLU8p0JrkqkiTu-qyi5vBzA7xYVR-pvUWP8hFw58cSvjM2Z_NANWA8R8OYtccKaIgg20p5mw__UKv2RRjOMWbpFdZIeIu1TZZYQYltb-3Sh9V--F-apuy6dWEX1yA5gS1rhtGMuiAnY3rUwQfLePEYPurKcfvu2g1eaGhDRChCr1XxHRqi9LckqWd24hKvQUviJkppIe0weJcUTjqieWIBBRZuNPmDbkGkGW1T4r0tWWZTntfpfom-JbfOtt_LpTURu62KBXX8aAhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9uDmQuxV159xn2UM_nWzXqmbBzSBlAD-7JPL0c6Kp-siNGDkDkQevR1o_rWcgnmZeW0RSAiScxIcgt7x1MpNAfnSpuQbgjcr76ChM30YmI-LRvKSsr16IDrbnuIfarCD2TVpgVrLTQkjgkKrS0M8esSI_CJ_fTnCE0S9QJ5KlC9AhDoDnNRmdhEo2qpY0qXsmkIsFs_Qw3mH7Mz4jbYPZrpRfh_xT7vlCTvc5O8iFXcc-YNWBfSkOw8KGqlCCM8wH8Vbuzmuwq4vF4E9rSlTdKlXQHaoGkvFTyW2U0QsVc6FVU5JXJ0xQmgbScdChTKqGz28oqJoQ_j8aOTcy0WsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAep8JZcvi3u5vNr6cW-OcqZdV4j9PqzDqI9NdHqBpkvUYU49SUuCaQpuNbxjgVYH7N6AixGoPU9BXp0WhUJfZj2pC17WRP_4HV6aT2GJyc4g-vHzL_zXLIdZ2YlbTMPXtsi3rz1u0dFzTqXm0J2QYwxlMxfz9_7wCI6dYWB0FAjqpaaK7ucsi95WJ4jT9873km62HZadR9h5jVt3HtPKgNnZ0JE3xL3PNlNgKEamvqFjIMePH7eh4-TBtVL6PDHmFxMDVzoNJTHY0Ns8l6arpUtND9pi0uIMf7U9_ltcqHLA-kBx6jU1rrXqBrBO-GX4smGBWrgh80cHvJZLqW4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0nwh_P1JgJ67hIWpuF7zezk-ScJ9ljHeYW6iuht6DJdwupeaoXblV7D9vkrlTXWYDNIwyMHgvC2Ixm8B99tF7NSpu_Rt_JeKxX9-LLA0Ln4ARyqO0q8g4ZwrJu1LAGZU2FFjFoxLMTVpgQurjeyJfc2wM-MyhIpDtrqLpya6BfJGpV8WRPdlEKaSIF79ZFwIQtsQo5EZ4KclypwK2v2adzTMFAlpO7kyFozY0R_lPuquem1LNnBwbFIZ8AnSfhCFRrX0etaJdt6-yhmP2pyaqLSmpTjIbK-3yXNID-gkUZA7f8hb_iWSopfBIkW-TkTYXQBGwF7mocF8LZR1dNrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=uTMu_zJzknsxCKubQdoukTWRKUOTZMKp8CEqD86u5ek0BgirphWQV0Hjq3SydQMser_do1_L6cRk9YPBkAmkucHiZ2kZ1Ijw_p90BgztGXGQCz4tszF_Y6w7bMMahmKRefSPDM10BTqoQAb4JDrrc9EE036B3_OeWCAplEEvenfKcWr2NDPoKuuLvS4vIsnBB9sSEv8CgWpCT3CZn7NmfYWZ34UrE3jWOXfJePHpasG2KYTL8ufF8ez8TtDbf5-1RBp1GvV4-ZAYHPJC7PGTxaggTnBJYhXf1D9azfotrYOvOoT9JGASHa4FiPHTNfuvAsq7FOpJJ-mCGTkO99QLIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=uTMu_zJzknsxCKubQdoukTWRKUOTZMKp8CEqD86u5ek0BgirphWQV0Hjq3SydQMser_do1_L6cRk9YPBkAmkucHiZ2kZ1Ijw_p90BgztGXGQCz4tszF_Y6w7bMMahmKRefSPDM10BTqoQAb4JDrrc9EE036B3_OeWCAplEEvenfKcWr2NDPoKuuLvS4vIsnBB9sSEv8CgWpCT3CZn7NmfYWZ34UrE3jWOXfJePHpasG2KYTL8ufF8ez8TtDbf5-1RBp1GvV4-ZAYHPJC7PGTxaggTnBJYhXf1D9azfotrYOvOoT9JGASHa4FiPHTNfuvAsq7FOpJJ-mCGTkO99QLIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfAhFHLyzJ07jxc_y1VgzC6riAu9mwUDDTwJwTVJ7MIAPUKVNttFdfzPSkXpDqavpWyaLPGhvxhYnZqQJtCbr5sVe1lRmmPJVuQcHf_L8ROLKOb48RO1mgJX8GZj6QZD_osmKex_KhOpxQinVOt5WCNSBMUvBGH8g0eLMB2X9gE1JoK8EWotHq6mSfub-CZhnCADTQCOFWUw3lhPK5aD9JakJeSNSm8c2yMKk-rAw3bC3j9IV7PdcSsyhcRpmHnho63bR0gH4G5vlrgOF-RjCZ_C1DreG1MBlaOFbbJjoMbJvVPAdCHkEst76qqh1mOxYPYm_DlZVyFvy3yOaB_8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slsbWx3SHJvhvwDVXoqHymJcmXxtArIQNxbhlvUAk7iZ1cGL_-ik97gZIqcnQnkf97Js0fa_uxrpDeJJM4V6EHDAX4MBJmJ559gjADlDVqSswIVc7XJi3aEFkjGPxs10HLfcbPsBdmUutNKrFJmJOKF-SEKQppLA_2Td742K50ajJ-hzchzjDwaQtoUj-K4-arvCFcBNGNNpuG8O1oYCzPHHmy1cI1ZgOaKBZ3Rndmue02iRkWqYXdHoPjOuW_cdrDv18KVXDOPkW1MHCuu1GvAOlxA84MsUBeVrYRntafUAW03z7YbwKLEwvkfTAaI6uZ4q8_sgaPXpac_Rq3V0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvlHJRzTFxjBbUUup9k6E2TDpDxklzPwQbNhhsfBlg8bCVTcaOvF5eVO2GuYNkVaI9CDgHziDUQqM40HRxonnKLhrLW7cBE0Sj1ZMZ1yrkYbPzTsoxrzQZo3QQB53rOt32N0oSwrE7wpwbDFNV0ioS4FXnJwa0qvEP8tXgHo15_13YI5Tx5mcnDDfhc9BYZtzxXpmjFZoENOcUCcbTOv-5kLik65KPJzclA5sMuvL_xxyQz2kFvSLce3-XlIXaVqeve5txgUEfAuk3KjO2YugYaFo4v8jfJReh-p6lHbbTa4clluP14cl4Lfx7gx2Umag3WTIfpmmcN3iXGqIFTt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhvWZDYodFBS0jotcYTKpE5Af-Bz58QWS2YP1jO9r0b1WWYLcUO686fQMuqLU71xh0lGo0DpYNle1Rv1jjalhtwk_jaTKm_DDFgOgVKMBuejUiqUPEKsFWC3J8971v5Zr4bHEhm-xbtIfyAN-V0Mk2CaPvEisrXZzBR0WjkSyrnRfQzXbLFVQOeKxwY9hoZj9ImsFpjUYIQxK7h8q2KrkalD6GpL2OOk4wklrsgXTeARo1nFyV1gNpMPVBwiAEKn4OesBS2jzznfhTD8kfogxwpNmYTpa6Eo5GX9k0q1Bi5rZ4xzs8g7DcTsn-wVm9AWR5s4O06paTpmHSUH26AAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dektmiQB_Y1GFWF0RpmSzvuMPejqNp-BQgUHuT3ADtcHCM9SAXQQErDeOUH9oNsBakbEcM6cIbxzIeBJ9CIfzKRWKHmc33psUP2RQ2fuwk2unrwE7y6aAAszczyoMB1F7MHYdtvDLSiYLtiKCcRFXfkv2I31auLxgfRDnSGvtdSYt2a59R7Qt8_k8KYVa7iXBvbse9fpDu3vA004RuR43qOrKX2I7l6ilua4aO7nVkTAtNQ6YzN9kt9Gb13V0PsfIuux9ihoSxwZw8ekf0zHBs3vCgDsxdk3ir4vdhS_WJs68LvXAhAOGEsxjpnK_RAIm6nzIZmfpZbzzhf8cxPMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZUNvtyymQEK0O2ZjmT8t5PWz9jMzRLFMofH87gcUqxbiztmgAVVlwAwpEli_v0wsp9XVC0tjyXQ5UFpMd22iRsIjCBtftbf0haFFMvHmhyDQby9A-n3sLGR7yZ7Ye1n1iEk8lQjKyjwK9nlVpTU5cTg8ApaJ1ehnzhrQqyTdU5F-WNprFjsCBuK9NkVVAwbVyUtSW_b8_64bB9sky9H0tyaB_SpphZRO_R4aOEd8BcW2V9-v7AJfYmDiIPP5nHpctojOxQeRAm6ysdbDv792PMMpQRyCdNtT2IbNlNiV5S4CQKP_-jpO-JaVbuJXjN5g183srCG2gSj-76vW2SSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzYUx-EvytN4VgbRi5AgC44hgICY4YYqjiVKyOVVXJ1Dkgqzgq6rpd5ZsHx8HthMK-TB0Tfmyp_f7CXV7qGHgFqYqik9eu7O7i026ey60wevkrhn2IBHD7xGQVv3QnMJEJ6_kHz_HmPYwOJVrQbcN_Ue4ipZkbBQqWfvj1X1Q5ueoMxWPZwkCDWb1FbzG3Js6u9sQ2Ege9qzS92UBm3ZqGeBX2wdELkea1x5oOKlyk5uV5Egh0Al8bm3s12vkp6cdyyht-DfjSQlgsL25CAcCNcrzn5lqQp5M1Reaq1-VpWGkie_cJ-tcOmwJDDhU2zw1rQb3eCnZfITyQsrVfK0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKKh7wnT5n4Of-a5zzOinAbihAa_ICP-_fB7qw23cSpABuONHBWeJvxaegrPq0s-dcb_GKJoWmKtdWcyx895V2dST6ACVroz3Dtbz0M3s2_B_NcDvoil0_4eh3C4HMhj6vL0mhVR_EFJQh__lippBMqWGu8yy6v0Pi1oExANkLsNuFrGHuL18MsnIoz1Qj4P0C_1WqLtKqIG0Akc1p2i2zDaQl8YTVWhiFWJxK88O6CPCU_UAXIS1G8Dj9vEgOCIVUMrFLFChBtOUj28470MrolO2jLrd-lNtzeg8Zl7-j2AMAO0G_HrPf2Ce9R6w4bKdkRKDQhMEp5EdLVkA8a1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=XB9m7TXCDFrTC9qGY4Cx7-KpfvWfimsUEYOFFV1ZWRNdsFK_sgYxkedSnyIleTUGAhHCGYftp6TsAfTI4qH60O-ZRuRooeCByIs-U8OD8dInRuwm05unIueqQGB38S9SzGY-xunXez8n7KEe0cbNZdLrgzVD_tdBchJ1rxQ8FYT73pI7rpsD3bTj84Wupfkm-aGUq78HyLEclOaVhTl8ZlD8j-84vm6MakE31eWTVvxlrAVtF08khQlFq2W9xcWWEBNizAXVdCjCXuw6QY04dR1Y07dxF6dnoA2WGvIns5k5aZKynzdX_2eomroFemSYKWTIVmOmXu088jSogpuE0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=XB9m7TXCDFrTC9qGY4Cx7-KpfvWfimsUEYOFFV1ZWRNdsFK_sgYxkedSnyIleTUGAhHCGYftp6TsAfTI4qH60O-ZRuRooeCByIs-U8OD8dInRuwm05unIueqQGB38S9SzGY-xunXez8n7KEe0cbNZdLrgzVD_tdBchJ1rxQ8FYT73pI7rpsD3bTj84Wupfkm-aGUq78HyLEclOaVhTl8ZlD8j-84vm6MakE31eWTVvxlrAVtF08khQlFq2W9xcWWEBNizAXVdCjCXuw6QY04dR1Y07dxF6dnoA2WGvIns5k5aZKynzdX_2eomroFemSYKWTIVmOmXu088jSogpuE0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALLeJdgGbI2HG4Ndi0ROXQhzXmiDdzz-4hWRyyMoD7UcPprGpvrYLlIvqwUKj8-H8SveQQUIImiixTAL_nvqClzA1jGxSWjRkc1rTXu0W39-W_BBAxL4vxOm7HFdSLHY7TmfpBOjoKMFqaYPEay9niGhqRX0L_fojbSnr-6mUgqNElt8PR7exXLe3Ex0e3ZWEsa2qlSN22x9Iw3-fnMEmu6jWbXEuWoBdap6DyNxhfGBSE7JjyeNh9ePzTxqsDTy5nUEu6ACYZvEOplDjVYOKn6WoTTiuu9j3pjL0ycNxAR-qmevrCpHJEteO38aoe-IscILLDDUAwI8ljOvOZC-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNJyEFTPSXs1tfqbX1XmnGDiW10aQzxGU-ew3b6Un9OpL1pIhn_Lt5QEdhtYXp_q3H2XOHXJYuFgQOn_or2msOygU7vrwYv-eu7Rhfat0oyD13LngyeWOfaCT4mlipmxV8ZxfHNsL5td_0_nWh71K6h_oRaTLXLk3BkGgyUAy6thwGlHwGhKSuBc-gcvAMxS5so2WjkzaTWtOmgqAs6awREKbnBTmSh5cVTbmT26NITOxuMKiFHXzjZF_-dsL0ONxTITAg3EDrPGF_-SxH7At-gMTv7qkti7CBHkuWFUp8diPn6YF2njm0dujqqfFBxXA1s9ISjrslD3jZgStyTSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=RqYv1UTfJlmGR7dLoJfBe3B0oVvhTFsjTnyQahJ3sPZxQMf_Zl1tDow_hqFm8Hq9lHe2yYY4cjtwPDfcIbAgW6B5jyD9tNvjU5t4wz9hK9DlFTmiaSu87C7xDBcFz3A3lDfZr7OW5Je8ltZKanqXxTi390nTk6YKRTy-OohPJMsVHYaAN5We-eYaW6wso77VrVzPCiS1GVwQvhoSdQRqoKJGBm3g_QebZD2mLmrmxDA2HGTc-DzTy6NauKcrOSYDDP7u2kQAXNtQ2CDyFOmZEwSYSurB9nTKpcjyPOOUcEYA2tqSiYkWLqNBt_45KCUVnB4cBxCsFzSBhxu_si2EKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=RqYv1UTfJlmGR7dLoJfBe3B0oVvhTFsjTnyQahJ3sPZxQMf_Zl1tDow_hqFm8Hq9lHe2yYY4cjtwPDfcIbAgW6B5jyD9tNvjU5t4wz9hK9DlFTmiaSu87C7xDBcFz3A3lDfZr7OW5Je8ltZKanqXxTi390nTk6YKRTy-OohPJMsVHYaAN5We-eYaW6wso77VrVzPCiS1GVwQvhoSdQRqoKJGBm3g_QebZD2mLmrmxDA2HGTc-DzTy6NauKcrOSYDDP7u2kQAXNtQ2CDyFOmZEwSYSurB9nTKpcjyPOOUcEYA2tqSiYkWLqNBt_45KCUVnB4cBxCsFzSBhxu_si2EKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_mjTFir7IecqtWXURazHOlaE0tQVCpzmSYPzwyomvhgHnCnC2Xc1kVvOdIt-e_THSwxyhxpvzrd_TmbFgMs-gGkaRv6FAlXXjzsZJ46b7qXrfTq_YckWcwB4GF8-RTgafOIvWbU08QlwFiPc-4JngESDGeUyPxeGj-VjupAxEcqHxJONKJLMKMlKtoW9pB9XHogz6yTabUdjxCWbtCVW-K9_VghbLRsiLhR1YmedjC1asSYlqerSm_LB-jnTCg13GvTJp8ttuqBE0eHvwDBuFGUzlYBrr9j5vFEiy-tYoJw0BYvRw2UwCLRkCOTbR3UoiAjguwp4mX4U-fIlW-y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/P7qreS6_esS_vmu1oooeTN445nvLoTTYrPJVR1TnXe8tdaAWty0ZnHEscA0b77IEkAH4tJLWQ3rYBSwgEy63fxxSOIykZzC-yXn6NZwb6qVi3HbX2b3AZmbHxMUteSk-V_xWoSk9oN8iJat--j8SJ2I8ncSUZG5a2kFQwcu85JyM4w_tjUcnGDfCr90uVCOMBvIda5Q7pJHndwJiKP_Rlmsr3o_f2hFdnyeJ7nUKMKj4M3KbUVihV2U3icRODbUIoEN3WPXtiG2ODvoCDtpiXj_nf9a75jCYEhGUL86_MFJiDo5PYjm3dTnq1zBusN8fnAtll2hKN8sxwiKULqT0BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaaCF8Ydib3TBh4NMzGEzCLQllak1i6nTd--PboP6LQ9wTGrXjEjJEEDtwY1sdGmHw6q9qgOzhNlXm581WbW3Ht_SOiu5VfXVQgUWQJ2ROuqM64moS80IbWiw7MJScf8HFaukdcVJtN9oIedqMIuZ9ziL2nuZ_14DyDlvLcs2F4Q70stefgcq7iwCv1sJ-XGCvO5cPQr7CsqVpWNmuqm6tHFQ1FFbaW0Z0ThcgfYL0U-w06Br5rtNkFPY6vD8FUTWba2ebs4W76CRu2kA1zGOnA24zANNOkd6sv_MfmlYPbvZafSQaknt7xAjYEUTFCR5qe1A9_1XcVfKN6qOnboTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDzbGuM8iAm_JGGHS9tzHVOQ1Fxru3nxraFaolsJuoYvmjXZ_rVyTT8Uv6A-TCJnDljr7HMEJxTwV996QJm-aPhBbU-HDOZbJWpxurY9ffpjNQ3Dxfio5trsTzUSRXGhrCwfxpYVRMTe4D-YkRrLNnuKqPX3oZhwWFWG_heTtERJlxi3g-73bOBPnuZ_kV0FP_stUUman4Ec8u7MoSC-PDrFbj8cfaoY78fmBuWOTfwLvCe-5WhgaTeIvmQ_7GW-XWI4zvIDETyiN4Wa7OQr5Sxbz4frpFxk-M_Mz2hMnnGZjE-Fi9a7NadzK6D-DnQl3gQV3E3p7VCK1LeNQzotWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdps2qO-g-1-ZmKU3KXhuXJWgWA6kj9dwxGexqlOiZO_zva76UpVsXPSMiQiBExs7zRKQDVTuwBcaYaLfgJQJU2DYKAFcVMpNJ9guHScrIhBPDWiDJDJIzsej-VFm1w5jkIulSFXg6RxJyP9vJO3kWaiwf0N7GaNqH21vmU_us03Ecoff7ZhIaGy0zZN7vEA3PGTPk17gFXD1AwyMYEAycQnf5gA1Cioh3a0O8LF5hTkbXNgC2tJbP00IvpW9iiNG2xRlqwFC65CPdrIjl7j4QFUO0d70b4RvUUZIwekH53ckE6tWkPK9zyW12mxmY5ffoEfQCk8hko_NKXJuXGPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBpHXhgX9Gld6fjzg8jsMoaXKVno2ulYUz9fb07w7eqLy5299y0bUm23tRg6wmETEGkq3oNE_bBnryL5OlNJvokPpI1G8dzOheJqfHaN5YEINNq4xyag2J0ICFCPyALs6HZIdBXYzz20Uft52LDhG6OydpmjuFgDuFdTzvPrNcvs085X0FwQ7O8GrFFb81nzQ7Vs5Vr9t3f3_lCT8Phd7Hf1UTBk8-ENKRl-KxTd0la9wxasCbcY7Aui7JTVNvnBMuC3ahjLERt3c9JIHl4HVKYkZET5kH5s6laZ-edsgTqBulL2zKjUsCAWgTvSqRdgtiZnsbCDkB_Vxb3xO2RM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUj0dE6frBc3V9BFtjoPvZpnKWwyNWs-w3jxyWlbR6Fu9dC-rJmgsCZixsmQxZkCdaEfzKevKMopsY9JzCWB7ftZXBwoMGiWA3ngoiQah623aFq_gKXX43jA_fPLkEJpFHz131ncW0N4D96bpwnKm5BGDYjoCA_LPK6pImQ6i6KCXSpz5HREYs2d9W7TiiARQCQwUZXuVKTgJo5h_lHxmAd5CliCMI6Wese13jHVc0Sf0v41Db9NWqnTN0irReaC_Nw_olGtgWuriqWNUsTzwwgb3yn1ckJC01Wdd2C2okhpXWHqUIwfstVT2WwFkIx8unvR6_l3BMrdxURgwBuTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCXqrKd-MaCq9XsQtd3sWuNQf_kSY84_3vxK2xa0Kp5JaT835ZBDf10h8q-7_Jw8Bd-yETTEwMoC6i-Nz-MJfCdHm8YZ9XktPfJzNZ0nZk9mHFHk0rOcPKxYL_1saaP6SFw2UGPmKxasV_FruB9SRLjrvJdx3xRPID-DuybFslEW9kThJyXLcXLFRjaFSheQvRgaPLufkuxfmDkUawd-V52F1XsmTdnSIW4kYFemeH7yoyPzULH__0bNLKCVMqmM3ToBN8_0rO7-65iJlMB1FCpbLa97nbznyIsRxrFodnW9Mn9frbjlbQEbTo6Bqi1zsbEpsmXcfN76-IShdsoaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnFJv_6HHJlGH1cTjlIba6q0TjSWu-fdKYRPEYCAsSixt-XvxsYtyte1OSHkaaauZ7rZB31cEoeTJXHbDqSmzKrZgYSyTFlJlK_6uTrLLqnm7zRtChEuxOkTxx-JlG1oao8-vOPg6XvR5ApBAnAma3i3tMN78mrmtKSYDuxkDkS8k13rqFibagAUfKxzSFi8l0AK59c-5xOc_52RTZDTu8N__Z18Hp1ELGNnHi-4wsVK-hr2worzqrrtXbpYHaDhEYrk7g23CodPdIvqDd0labvH7iY71BCRssSt1BD2HE16joscwvBB6QD3sjFxyKCceqNZZCwKvzdlMwUI8WPE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKBMWS7OQ79EU8bN815fwo763ly75hqGkg6ip1MfiEVdF0fEqtWx522OFuo47pHgdbwyFwHqTjlKatt7zLAAXKQWR-aQ6EgJQAk7OA8OQUjsKC_ypYaoSu8qMfcplC-cE578biLX5VNpUwvHm90OcDkFS9BRQ4_SANhF-aCscSkqCuMZFGkzf6TqXBvgNakEQ5DX45u-3SKUjPXTkFgrpod7pVKxLb_au6xlmuTqlPOxF0UkF7p_CW909nTikkNUm99vF1p83ZMhlCaR__EkeaK5Cv4u-CuKnhIk4OJOOmXvqUp_aPWc8RNpaXJU22aA0C_Wewy1KgghCy0mmAOKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pszIIxK3or5APzdee5zpsmuAY8lY57qkF-2FRpVgrC9uC8SjKthPqMWsX_QUijidV4Yj0U63mq8OssbyTjcyY1oyxGOZsPMJRErbD48lPpwQ5qHA4S4_yvB2neaYeEYX0_nbyXgi_grj3Ze06JWYMzfVET8uC-8v_xL17MQdBNfWcIPZ-SAtkLPOiwzdY-iVmKM4l4UddnVEvC8zdzeImkVwDDpZHGhojCWhANjQtYQPFNFYwhHJ_ocyq_yNFbi3MeSuS2-JelX9xgU1oHZa1HalohqyKsWtGH8B7lQvddVlI8uYBUNgZBIeqfB1jiVEjLc8mkmme7oGjCSekkQyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4ekBmQV_EtlXRb6Rlnu_7cq31rco-JZz-PY7ozHhIj01h3P_wLV-8mWXZpCJSiCtKfrC_aGyVbolXP5bPdlr_3vmIEbUYwrFyZXk_JGkCgQvW7b37WME98SUoSg8cTz8nkJprfuWoVcGV66SIYJ3OKcd_RcNHMzUTeVjTudregEhunFZJDRFz4rbbifVn-1c7k2BFwSv6cGaxQQyv2NOFBQZLTwY8o6Xg2bwC_L1aTY6HiDKb-bKjE7-9NTHlY5BRB-3oD-EwuHOwTLAeH0u6uHEvFXHneW_rj0yPaSZfnR2pW_UZhjcdusfisl2Ho8Dd9bLNgYaG6zYvhEN4jEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O915eOOY-gjZ-4q11a7sNFE8frp0k1FbeHBNkSKsUilJjUKKExe44vlyb37bfQygZBbdsOcmUSN1JGhlDevooiD1CXsgkxUowuwZMq4AYzQGB07c1ToFpIhJu_Ht3rlYbrgE6THqi86k5ocMjwPbQUWI_Qh6PqwNH7VA4pQ4QXgnSKrynwBReXem3Nm-dToaQ_wOI77uIJhYyrkvSnl2g8yybT09MMY7HJz7TvWERGxSJLNuaYYaA6LEeJd0OAhnpMunGbiEBu0EFUUKLWX_MHEkJFhoV5yOScovTV5XuBX0V567GNqT-s7HoPCZAC9M4dgHtU2cdzsFpTaxDcGMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
