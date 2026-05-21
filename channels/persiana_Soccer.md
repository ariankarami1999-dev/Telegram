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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6J1Wbytal29L_FmGPKtA1th7RJ8g1vI8LQQI805zQI5oQNVsAlINsC_d20YmiS0nI1TYR4tqVRK1-V3eg7e2lIQ_ce1B7lCm0JPHmtlp1ypvA3QBFnAmSHiwelCImc-Fo8VL8ItYsJscKCIHhz1RncU6VpbNM719uD-xbSWtsjI8PwcVVFPp6BhgX29Nb3UgGSmr839OhhbP_iLfpNThMO17d2G6cZK7ey6teNfZq6jjq7wpeE9E_ymTfuRCXkMZqzKObfyio1Mq7EX8ldtr9UNDrXjRuvhkwNi417FWEyG10OPHx7Ti09xmQCDIPv7O-ksdLKy3i_Vbc3i2mh2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuvaL50hQz029fHOw8BvuWiGKprXQoMLEQ_XrW_e8rl5GsmSt7Oemkt9xtjD-CLQ9MyYD8LB5DiQShhDroQjxf-ZnHmM2HZ5i1sVeNmkaDtsPawSEC7syxg9orI0Segb0l4Tpi4DuWEdVOdXU4dp00PGWtddcpA6tDQ_O0g8-CSMTG8WuiZMKgWKuO8dSmweuZrKHtDj0iU_NfFLgzN6VPiXrknNCSlVbwgfQHPyp_Z7M8ieFo-0z1f-n5uYtdgg2Brj4NmXvoLUQIxwj4xvzpiWQ3WGNIZvsnn9IzvHy3meWFhHzSRsXgnV9K3Qtcuy8aOpXql6SzdL57VizU-rwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/persiana_Soccer/22212" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqqQ_ouYSkKg2MXRo0bFyy6Momh5OKP6n-9Yy_fOJU6YZU1SZ5IJXQ6MYblEmCEGIBmK5jGiEQr2eZpwoZQYVP_aygYbsjywaf917JpJDNLIFuZa6jJ39benD4ibInAyHrWEJ9h9ajjnJ_D1Kzs1J5iNgHoukJbn6DfwBxX31x20VdWsCEt8A5564n819BhElVsjWjbAAsowzdpG5ohYCfg3PqesKU3MD98emwIGYKkFBsD5hB12hcDv74wY_H8S6fb5N4CBRb9FVbhxT75YA-3D9rjyhWB2Z7yv5TJiWkeN9PAfNGjBmNj2Y-tYI8OEyS9m5NV70-fzZYlazyhiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsJ9ZhBpJiV4G5f3rlk4MbYvUl60ITqt7J1RAFAsTMDpeGpy7isF0QF-QIcyx_jX7-_Jk8MTgHZ-uk75NGa-HBRidZNBivuS-fxTM7FReaslZJialScVuflWAefzfrEDI-5ZMLYuiX8XbervNAqO7S7ApbwgFs4YwGse2sXnb2CrFncUawWP52E3A7D8NFaqWEIUQzN5qdQbsjNImm3gjV5rYehKav-ZoRlN7-g0bMzyRj3usWO0bUtl_GFJPdJqfGPyM2tQjAc2gj4lAG4H5ypnyZURsKpSM242dZqWbHhzPPJBRwIr9AiGhHlIiiKnmBQyIXjc_SydmXHTXxR5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJwLasdgcIA5NBEpOhkOqwCcMz8kAEMLW0qvw_I-0DqhL1z_U5OgrM-BW_rlc-032YDaFyRmsIE5wmwXlufFo-gSkMvMBR1rcvwrNXCOdWuho0EmfkbYmoWkXyNm1lOF4I0dIf65xaib-rAn0_rHpuDtvQF17F7yeUGs40srWgh-WcoLdjNSohfXt4YrvLwUnVSNhLM3NAR6deYlPN0MkbLIghXRq2XUxavkmz96IiTKBJ-dnpPIrbKjmIGksDcKT82ErXyewYGaDqpVEcY7X87PP6jUqpa1X3nCRMryYtcliPcHrGTZN3i7xaTik36s9Nfibc0wMiPUNqf0_P6Zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0CCFXfTepsOWaOO9cGSRa9vT4pJcCd12ZRQsziTysnlXyqICl9OAJKQ6LFRb77gSQLYFoPM6VyXG0UUHMm1ZIZv31aIwaRPQAmqk7XfEtOzwJk4fdXa8SCBctRBruSAA9ImhoNbhIgjTG4WKhF0XilxMcdl_loi6rH9sn1HuR9QD-k1eiV1mpx-yFR9Ydp6uoqzJYwH2LyXwFhs5FuYHVuzse6zkmeDcREaEFYPi6lnjsL-CaYfWXD6R0Mg7xXjRE6whXtJMvzQ0JRIlbu8nq1eenLk6z_LHRpcodrkWFSSZ0m-lmKmTJ8HON-sD1G15yi-oMVIU_CvoHhU8awqBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=v4MKrG9dNCYh50c6qkHwV_P8dzV9A2dy1G_WHqECNQR77ql45it2KCGPqQ3Ywijn8g9byvMpVyCCkc2u01pUbkGp-tUzCvKjVc1AStUtEoI_pGdFJG2l3uZM3uDOq8X1LCCCosIitOKjESZ8ouoHUMw55XHUTUdqaK1Kcf5QQRZI-lPCJILSoDOY_KKj9ZsC-agOJJcJCjhv1pkYKFy0HlF3ZAHW2T9aPKozpLXq4pMBCwJMafMWgy6p4b1x4k7EPGoyrYRyFIeyMcUw8waCh9tGUPAwVQQwnxaCSpe_RFNf3ZtpdcwNfzwkE573ApXrjAuVX9RuR2j0wxelzwevLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=v4MKrG9dNCYh50c6qkHwV_P8dzV9A2dy1G_WHqECNQR77ql45it2KCGPqQ3Ywijn8g9byvMpVyCCkc2u01pUbkGp-tUzCvKjVc1AStUtEoI_pGdFJG2l3uZM3uDOq8X1LCCCosIitOKjESZ8ouoHUMw55XHUTUdqaK1Kcf5QQRZI-lPCJILSoDOY_KKj9ZsC-agOJJcJCjhv1pkYKFy0HlF3ZAHW2T9aPKozpLXq4pMBCwJMafMWgy6p4b1x4k7EPGoyrYRyFIeyMcUw8waCh9tGUPAwVQQwnxaCSpe_RFNf3ZtpdcwNfzwkE573ApXrjAuVX9RuR2j0wxelzwevLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObTejb3H5dSIgKqWNewNZGiNDykp4YAS-CNnCT85ZgRSXVvca9jVIpzbhjuMG1L-jFtsCrgyKW20_25Vo82kavwdPml3A99OzQXDv2UJ-Cl0cewVwVzh9ypQy1tVKb8vJ0WZe8hAsGF1esMZwah2klNU4wKkXv9pB6UCMiboUzK2wOQX8fxGLXt-wbfHhpsDy0bMqQkxT0nMphAW5XdfCo6jF9Agydi1lcBa2HE4HNxtSXGeEN31fzkwC9vnSLWHtRUWU5rSlAGvxQh56HBCBTPcqUpU4cRTBnLXrvcgNZe8T1L2VJ7H5Is0yN0sxwW2lgZQdGBEi0vUhm6uS3n-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHJx1Dediu6MdSYdI4jsHb4Ds_oupN8MCDIm6sPE46FDprDCezQvuPYpcB2FyvSj3wRAIJpqDIN0MocHQ055ica4sThtbhkX8kRRlz-5tZZXOsfq4yxvn_ptLdNWxsf3sv198Sw3ZxQJwiC2YNlrFjfyuxf1wqrqym236xRStvaqQYgSDn4IMLO80aVRcxcVtT3OMOma26CF42Nr4bzIU48CvYK5Zj0jgMdFCyvSNzWA2eaQNnfi-EX5M6TzlOhNn1umZQrTNhWxwArWRPlANMmaI3NEK1EJJfF9cRkgw8FW4hagscgjjbZLGRH-QJt3wBusA4A0k6WKH9fN9MhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTfibFsOiycFQADE1io6mAMJ82hPK5u3iQ8ia0p2x6qWuXdDyJH5eaT9pN2PgWLPFQ-ZIxjT3qMvd84Yo1Abx4Gg3o6MR38hf4fv6vjkNadXl5ZytMKWZfn1BZUEmgZgexyftzCHf7Loc54YrxBsbk3sle-FG_TmxTVbmJ9bZBhwqCbg8khkEwq2uM2rZjYCnPROIBb7MsNixObAkzu2wWKKHe9w2HNFEYRE1OtpAQKYKEKCC7pfBjfYqPXRoXwKIIBISghFQ1jo3mukbTyTs62lggBRQEE1k6HA78YsCWanzRGXHSAios6NjhD8Gi71Thk6vQbahrya46k4AWhkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kivu3qeL2aErgEqQj2f_mltsyDlrf5DvlQq3FAdorWMG_nOc8UQOa8SbMFp3g5qy6bcTEUdVKnpbGEMW0IjN0xfjY-VdgO6VTODZbfOV3uSyT-quEsprBlDEGYbaRYdr7uYwyw41h5NWWOy-9RlHGZAWQOPsdvkAT728ckL6qo5hCZCCUjCKOQUD_jTpOu7ifpIvixDdbDRVUV0lUccvYwBPj22PZDeK3eIl-cvqKlSvgSm3RG7srWeBtLnSOxIPp_s_SJFJaOAlie7VGv2--C3RyVB-O_Fu3z29bvYJFHtnuUPKM5qe5-kBX2x1eZyZIINwli2QYjJQIkr58NWNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntWT2jgziyTQ4d_66k0Stj6XP0MwzOVPMkrAmfAivp09NhiRQoBqBy9N6lc6Y9KRD8qhWvRIhpy-bSkD5ZkRZW5q1ifLfihwTTWi5OLqXWvGCyVKYU2suA4cT6NSMkVuF_DVCsaHM2zgXf8j-I30_1VK6VaxHZX6pAY23KQXc3b-kqXW-P-8ZVKVi8UQraXRw_RPuLKc4xCHFDLHw-3cadrE-4mNN54Op-cIiXzWxaZr1-N169JqmwnMPSG4p8F3tiums-fwmUXgZw4eSJsvYYw8DSqK7EYMIpe7HlEKacvgewUMMxcnZJ0dlqFByhfWwDDn3oRs2a_p4V1lM5q8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAMuFcyOace0VG3FdSseQLZyN82S8ukvkWo-SSG7nelNrjrnjIvTQPzKtJpnSIvADr4wW-X0kn5Port5rvrnJRT7oNnRSnLcZiTMC35HGlUL8xxUYy_E9aF-2sTu_zApqP-iPmw0F9vfHIXLn_kn6BOickjAc1r308C4xMhIaY9ZWfHEMUBYFqScOmiuXo46kyuRmDD1KqOmw5Do_OYJbPaL8Y_oZS0Iah5fhf4b3hlsfK3cqliRqfuV1kG-ew-R7Dvk-pfwph9fQlDecFfcqC0QXwbaWbEhuNmaeEFr1B7yemXMk198f8FQV0cx4CEMRC7_iUYV7FF6MASFmNtSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_PkDSHOW9zeRMw4ewPj7wQ4gN_sXS6VDyrI0EuwI-t8Bbe1M-iZCxlyZy6nSnC28LruWxIWVMfDdAY9EyZ_njic8CxufOh3KuG_S0ESCyne2dxQdAPCfa_xPE1Yhq-grs-szrD6myEaAInI-G_0Sy890onK6sEkMtetVGDN_6aSia3I28jQies9O2gSkMFgLq6tZAYWkvwR_qFpWriFO6WXz6w1MvrZd7WgCZr8HR5W3X3usyxQOsQIHHi8eaxUfoQ5afe_K_beKit_76HFXyheE97hS2qqkf3JddZoQxVneOm8HpGwVXvM4rEbp0TsPIWmyjrWp5CUEN9gY4I7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRMmu6MVesucVJ-wKZtizJW3J_61nOboPoUmtlD9t3QpCNgHBGM1O2NDG4RNQ2OKDEGz4hhEiRQJpLdfCHPJZCpUTVWbySBF1SbMp945FWub-MjKYOQ9MJ8Y2GN_onsPZkZQeoCt54uVh3yXNgUcXkqmN47tNTRNULXfY1n4wPIgxZtPaojAewQRRT57GOKZ0cK3wtkZ9OgN5GSQNnssd_SkVJYR2oU3jAJoZ5jrjPUrcIRJMskWhkxhR9OBFry3-9qr4HgSBtcG45umJro6wvuYKuN6UbaHAXd1Bk2WB5XHOZ6XpolGVqiREVcPxeWdyVfm7JzD_qQpkQLyJPzpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDDHZhyWDLKZz_wQkY6Ysecjw6X99acgmLly1FtIqbTvcgzUS46LgfvxF99sJgWTutNtdK2ViSGVn0E2A_BQ6-sXm1hZHU1tTM9vvILWEzUyQwRpZik2YVxwbt4-MpQL8iMmwNlUUa7VhjBmD0ND-oVjzpUTfGsYGIDRkSnGQCIIpgmGF0Q2yjPxWnXJviFrgW1LGo9GNHKycVmKyBmmG9NuFf2oljFmZPQg6ZzArs32dPRGBmKnjr9FpN4edytFM8qEVpOBGvBqj0YfQLSyPItewcJhCIYgi266wazYjwU2Nb4LeaTlBpA2uR4YDlyR4ZPlNAFaHazR3kkWt2-kSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8VtO9S3v2s-Sl-Pp4yU2jNTEQ0q-BInRfyresdPVOZlRiwSAgbszzBw1kfK2sXtMuniVJF15fVaHA9WevDsdDCT20yTgv4FheTCnD6SK0sDFzoH5UgFMHcmobZlzJ-k8kGLKV1UbC63IeCGtbcLc8kmXcRzqUoaoDutfs8inS1iX4jGL28nhwleBGq2d6bGBjPWx4jv4P2niyvLjukFb8dLsaiaQyaDM1ZlpJeXenCN4wd9sAHXG3mE8ixKrz_YX40EDdyC5ggjTqQ7iQaR7vid2Rl8H0JvnzXw97ebTbuOaZN1iZIwwHba3yBH7eVP7RWFkC3jD6H7XWr6P0Ex_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLuqtT0YBC3zGkq0ITMFfC34EE4ewduJGAENVTxg-l8ZzFk-8xso97PQRGgSR85Hy_jbT2E17ODVyfDEnHQkMcTHU37-CKRuzYT7yL9-y0J5XoTau1ibUIaoxe29nzXE37BDKxoXseFIcFy_pFPqm9Xs44arWz6mUMVaTClPHSGg5ApDOI1FVG7zojpcHFYr5oBjAnK4IEQCTy3ey2U5_glzOl1vRIIa8lfI22RptdcSXqAZHNOYLhpRCvfjaLvskMXW8m1tNWfWJSFa-gwUFBSqQuot2EXULLQud6p7qREtHI412ZGJK98c2pGoJRCgnT6oURtof2IP0e-nLjI9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=vm9WQMb0a3qBSjHDnzGZqiibN4my6oabnoA1HqTClNg20qDj3jJROj_9IkA64QdJ9hS2eZi1SsKSC5_DXT82hgINqehJNgvxNjbxUOVkpN99FxFxEd5u9D5GzArAdK8KGqzS5bgMwA3puWIxWqbXLPaIzVIRDdBHpsQA08LWf9yVY1HanTVS25ndencbbZPfs6wAEo52HtsrTG-m52paUFSnsRLcRRqDdYjDdAiOYdUisCjEat-2LNfO_XKs2afcfhzrB9LSfjxhOKfam4N3aX7zqRezAIRd_t8Hts225vsvAnMyGiy3ArR5ls-TbbXc3unGq29vnEv26W_ixznkCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=vm9WQMb0a3qBSjHDnzGZqiibN4my6oabnoA1HqTClNg20qDj3jJROj_9IkA64QdJ9hS2eZi1SsKSC5_DXT82hgINqehJNgvxNjbxUOVkpN99FxFxEd5u9D5GzArAdK8KGqzS5bgMwA3puWIxWqbXLPaIzVIRDdBHpsQA08LWf9yVY1HanTVS25ndencbbZPfs6wAEo52HtsrTG-m52paUFSnsRLcRRqDdYjDdAiOYdUisCjEat-2LNfO_XKs2afcfhzrB9LSfjxhOKfam4N3aX7zqRezAIRd_t8Hts225vsvAnMyGiy3ArR5ls-TbbXc3unGq29vnEv26W_ixznkCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKDA_Akyse7UQ3bTJefHnwVO3NiEG6Ym2IBW7Z43wrqSvMbhDx6eWS8q7kGvv9vYInGBYR6e2jcnIEowdn2dK_302jsgNRmZ_faR6_LHVZMKGcOkwazfFEzOyvOgpW5fB2qussLU8sjfPAgIsZSk0zqoSA8ws9W89FVwckbKqw-7kneggueZz7urSJSjjHoVhX-UfG2DREIn7-6oeghWEd-DkeVPQmPOKUF7RuHkDl0WaSXG4pR5Mjz3iorWMIUak-nUY0cDBd8jWG469hHLYjhd9ZsSBNmM6Pg-hLqa2c4LzIBNIiXElOATUS6ksY4l0KeEP5nbXxVXV6enEX1PSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlaoRJc4M0spKsIl2TrEyOkATYPDUXG5kQOUnHk6o7dutgKaC_i69Re83sosrwI53PzhFYIzfFRsCARxM09QEf5guOKDlJfLOZ_z2A25vPYrtp5KGQNOu27LZ9XdrCJDb3jmpSUMl8OAiboBau5IjjiQQ2TR6KehTbbkEy88lOANESQPmJ-haoBzc7eGxGYL2f6x4IHzLxh9OFmkaaSs7LQRw9q8Juy5sIxhW5idKsWVO1Ae_zDCZ-1rHGzdSz0Say25hPTGaRNBYNTaM1H6M886XzJ6Pk0MXJ9YMlukkolnF7v75evDl_OpeZvOEkbDfEpq1FFuzFQsU8IR2thWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhrx6ULrq859uQw_lwup0w74FAQpvB_5kZHvqECiixcmmg33bNPwxA6OfnYriKX6GLKAa-oyF3OyW4Sjug24WrgwF2X1fuK0QgFh4Efj4hH_BSo2NSgBk7uB_PRrwGglTF3OI8wOULHQiGvyEsliYyD8FMA-mI5sLKQrVl7cOaWIHyfgctqKOhf18Vb5bOFHWZiLBbqKbBHf_nKKOPnBnbm6p0qLUlzLcP_Gfu_IaS41qE09gl6tpT9GcUoCbHQ0YTuyFxk7qBUhOjGI6kNshgqAM8VIIV-la5UCITX1Fbu0F4PeG4IresbFRJjaEYhP-WiaW6rvN3vAo5UwRQ22CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naSy5ZAy9Nz3UN2tOwVLiHEsp1QKgOu316uUayl_DPU4PGpJ1psAZ5HtLkWmuLf2HaopfU0ti6DYze0TcMGjUKWZXcPXQC9xc9k5ApFjVWCmELwlJfY0H_SifeZ_irGj78L7qZBMMp4iVfjnaiCh_s2ds5nE7me3WApNWDq_LQo6UJ5JXpcyausOzStGM0HtnNjG4lq5pIlqNH5CfYylDO7yadPtrhkv8QAHcf-AVijcENPkrIgs-ADmLUz-yXlQd3lJrl7e88WC8Itu748rdsxJf857-LhYOXuX39VLO0yG7KqUayab7um2lMGc2a-oZsg5uKPms7FbEEYhQToO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TszEaqRVx4kUT0z41L6JdotFuzkLTdPOCCZTl_SVE4jTC7DEPLT1M44ugYKd-6waMHZK0beROFMxFwQ3HUpzqOTrbBvct1SDYaEKB8L5XIxxF8ZyyvAcarXhgGHOLszRDdR2eL9jLK5VlDdc6HTE9O8WoRakXr4GhQHKuPris1cI4Fm0B9qOcQaynpsUkqlsK7-wI75h5QDTsLB2HPc4Xf3HNrO455xBJcDxmdy0RWysJJHhlxvXvKleTwQ9wGSdy529NOuZ18X1uGgGJuHRRGLvOI_3vxRcxvS9B_rhqRRbbdjznbFYjY8sDg0xG9XQwP8qdNdP7XSESlcPPc9gDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6RPQKJ_eG_6qfQ6YaTs5u5s1W8rU-UTLlZ1dHkYvWgo9IInUxbUKS8cutooZJ6ThgzqtqnjzrVewdXXZKT-NHOJOarOur8XJ2rQM84bhiSRTKGFuYXCNXM2B2Sq4j_P8MqkX725dEawiMWGnS7vxE1e4tyUQBBD_Q3BXGNiTDwH9VPorQit-yB2Nr9jAQjd0rZBaAwERkfLfWPXWyR1p28fqSdJfbVCv0ZRW2awvUJS9u5crkEz8IIP9R3FWzTg-c8nCMtaJwzWSvWGvam6xASljs0kDVSHymrodSzjuXNZGl2V8koJ7SDiTo9TayAv0KLWUNDkJduahqpBJAJJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7Dq16k2OEVd7K2yaQjtcWxAhyGEPpyV2_SGLdWZuCMmy5rtlueYsBV2XTRiRrdNyaHsPdU-qvbtwr13xdwnhWlYMVFGtA7hTWBeWA4SAvTB-JpH7DfAD6GXZG0aFuPHe7-OK0ZYxZBJ-8uuXHQgHBpy4rr8AjSVUzS7PCZGDoZ5pYKePSEkExBsundND0vdaxFcld9z7DLw9ESsacESVNd3g4LHmYbOtzUbvcG8LPYWhvLuL_qtMxlRFLn6x4QMOEFn7vY8VI0TWPyD0q7O3TQkA9bpdbDqkpwgt-s78T5QefkhlsUuD-i9nhpFj-ZvYfKHwOZMm8oDfApCivhUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGPB9f2yYVw4Hrg076v85J044F-WuSvgh9yrfQ2tcWpJGGgFbeos_ABcbPD3oQ-LE3Fo3EVMHUMfhik9WLWV4fFY2ebsLDcGjRYZdJpMDFDkIt3T1Zbmg0981g1qeUv8TqOgxgnOiXPoxOZ9_-z9XGfYgAifkDNXpK3io8d5Ly9G0KzH-nvFK1n6Jjzb84bs8rZDKEsV05HWwyAbN0_FBriRVskQivgADjZHgmtJ8qlIL4-nPGI3i_qZos1ZqE5yNaa26laiVcpjNZdYDHy4-1HqPMhsbsmN4lRYxDoDMxfL_GF72fNF_rpgAvbS0tJ81ft_JCVXoGuGoHfCpQajRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmAUwly35vVmnrfg0RA8nwYjlR_I59ch1D-qRRrhJNStHQ69BbehNDx8hdD1JNNRQmtUJM7_clhyuSKidqOmkdN_6x_9qmn4kGKYzPoa5Y47IM38EgLNWvPohmVgMXyXAsb0Za061U0vTgs42NCDY_xZDAXR77lnqpV3n5DtjmIV9_TJF4EyEz77znve3ABY_DnitpAXyVEWieq0ghOskR0BSY31LwwSGKmf5pPf7Sye0HnvTshs_hBc9G11n6IXMqKGJVLn2XJsJI3yiZ_8x5AMSAf5wPwG_NdxWK7e_2XHVD6FwGQK7sNxIasHgpx04jXPBRv0q8kRJpDblQoahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyrPB5q7QshtDMKI9eSzohdLSh_jUHjy_kw5FsjEqoXXnrgwzbscLU-Lz0TL7f6VOzYDPGfAW2u0i9f_R3MbTXumZmmM9lEdRJuKlcsgw1oURp8-TeWIMeS53y9janjP4N3gRL76kp1EiX_PV1KL1TY5CQmGh9VMJf-La5JGP0VzlzunOC0Nww63wUXqsZybDSx1G-19gAPaD-NPvZgOQuExIMIoUUdzQh4Xk1PrI_cjZb-JWk2TEOCMxaJLv3kDE2w_SNmqiUBZctpJ_Kuno0SIkoWXwtwGBS7n3G7OWV-1YPct-okPnvaZmzR--4bNwqBOUOowlyPw3eVyZvtvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=BTjBrZ-qHNGueTMM1v9M1MNMdyY-GmeKFGriLEmcBzp8TBSK5PpWCB7Nyv1Pbrz3K0beBrwh1MgO27Dee3VzEJnq-gmWEqTZWSywZOg36CUI1-ghUofhNIL8nXamNOpx_Kn_CE04xz_S5-Xkkhn7b_9G9c62yGenRRc05zFi1Yk_jjr1xozWT4ZQMwUCSPnPVC79_6kVoOyntVosuG2uyA7Jjyyn8SSCfJtgl2zTHmFFpgp9P7cLNpnXEmrEa_TwNm-9rgBBAHyBrGVv4i1_J9pCcP_FLQzHHgb94_iI5fi2Wl8Qn0lF1HB7mHBqbTZYerb8x-jpH6K9zfWa_kxT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=BTjBrZ-qHNGueTMM1v9M1MNMdyY-GmeKFGriLEmcBzp8TBSK5PpWCB7Nyv1Pbrz3K0beBrwh1MgO27Dee3VzEJnq-gmWEqTZWSywZOg36CUI1-ghUofhNIL8nXamNOpx_Kn_CE04xz_S5-Xkkhn7b_9G9c62yGenRRc05zFi1Yk_jjr1xozWT4ZQMwUCSPnPVC79_6kVoOyntVosuG2uyA7Jjyyn8SSCfJtgl2zTHmFFpgp9P7cLNpnXEmrEa_TwNm-9rgBBAHyBrGVv4i1_J9pCcP_FLQzHHgb94_iI5fi2Wl8Qn0lF1HB7mHBqbTZYerb8x-jpH6K9zfWa_kxT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=DJAojEKVsxyiWbTOtmag89_efH-B0B5PDADhAlfMx5daTWZs6uq-Nxm-Jddq57_BVpkmCSLypf5jeUVIFi47pcw25DEqQ1fll83DkxYamYtFc27J036WLWSek1qqjboFRb6hvpwWQyIbJ1exCMNANLit9dROeG1NLAJDnyjXz8zPwO2DJM_N6v1WvZsnKJi0_Omw70GyJLlcyB9jquEF1dZrxT0ZPRfGwBsfhDgtQ8NZbFFYiZ5SpxOuZDVAvF9s4XaaJJ81PSQiJKD7_CqGDZUGoa-8y5dfyluFYhKjW944YLutRpQM32aFh83FgTFOK50r8r0n62frPJxnqykzRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=DJAojEKVsxyiWbTOtmag89_efH-B0B5PDADhAlfMx5daTWZs6uq-Nxm-Jddq57_BVpkmCSLypf5jeUVIFi47pcw25DEqQ1fll83DkxYamYtFc27J036WLWSek1qqjboFRb6hvpwWQyIbJ1exCMNANLit9dROeG1NLAJDnyjXz8zPwO2DJM_N6v1WvZsnKJi0_Omw70GyJLlcyB9jquEF1dZrxT0ZPRfGwBsfhDgtQ8NZbFFYiZ5SpxOuZDVAvF9s4XaaJJ81PSQiJKD7_CqGDZUGoa-8y5dfyluFYhKjW944YLutRpQM32aFh83FgTFOK50r8r0n62frPJxnqykzRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3VhjaDHST-HeqetbFxO8KNBmDwDu2uSIn95wWQhrokK_ZHiA10sJ1bAaXWG5eolEA9RyNbHcoqN1kO_K7P-pknMMdaLLPqzRb37mCCiX4AinDZ9OkRfW90L46rCHevUkHKcl_MehezA182_30cn2n_5sJZPYIUjCPLxU98K6_1wx21UwGftfMK7GQERTo5uCcwNYUHDumEuhDtkE2s6DjuwajG91oAf5i84KPBFZbu_PYqjYFbvMC_SPJ1zsSiRXh_SgtOs4Eep3YucpZ9svebokfnPAoaU6_nHZEjuVg-hZfkUmdBEPuOxu99NrVJpofZTQd2A_c_nzicaFRvMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxmXlT6WTXoLxkmE5L2avtaFV3K4_IDhDMAo4jN_DtciQDv5g6sSB7OHVLDE6JS4cEWrJ_XSpjEpDuT0JAw_Gvr8ol-sgH5gPnrtD-5z_p9Of0rXBc8s23yz0VcP45pkBXwiU1_2cjkUGNXfKS9LIHF3iXHqunxJ2UISaT3AL3rms92VuRv55ddEXcwO7flkyo1MPYRvaIdovbk8fb4wdTEUZZeIytxZP6oYeHDTGSo61TvNVVoy6Sd9AnpcV_BZojO0J4rXCy86Eo_UHovKSiJdO7jxl31iD9QoSThlw48Qp6LbXYnSF3GD4tHJanKpN5Zd7cPvAJwCfUqjQfnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le6lLRNnP6wJNf6HI7ir9TxlY8Qesw5f6UwuAn7HWgLkwSG4au72Ozpa0kZUBknv_NAgfdjc1iTGjNZ9RVTr3D0yBAYKLvpM-JwZ9vYjUsjF-4JrB6AkYOPlMTFK1JAHFobZkUnw8G3JzRvU3hBkQ6ZZ3aJKrgT7-aiQ52DNi-VHDsMvW1Z-eCsA1D2g3U-bR-pAwLVaR0JovstSCbQX_bwKpVG75f8eDVWbxICUnUaNU-RLsMPr5gUO8hsamnGYNQh1NwKQFUju3MzOXWirZceI4mMCAj2Iox6cqVUTMLHOrgF1roATEuWAWPhazBziEK1B_8BahPEc_E-Q_NiAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLKYMY_l9ZmOmhGyEA9rceSi1xP7lCI1VkSV6SHGyguv3YHa5nAdm7fNFC8JUe6aK6oxSBwsFh2wNKCI9aOyhZioEQ52gdPVNzOKQBTIFrk10oSefghqk4kqMqfZAOD5LLXPVdMViYi9nh6MM4HOY5LJAeBxjpLxm4pMHe3ljnmaHgbmXEm_ToN06pDwkocN_j8ujone-dwglDETGdkuwlpO8mW63qTeia1wvAyhgOUR4E9JVshe8BCx5v0bV_CmkTeqCU7TYK5HkToxNzY2XX52P8s47jN0vzG2rmhV-mIE5O9RjA8DuB-oHiD7u8HXDNhZfqbejjQxiG9oQOoJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohiyN0DyzKgsErJOERjBBVc4gA_El2VCT_GNDNptU-WRqRsodHqobA9MwJLr2qgMB33DHNlaqMDnIqiHBpHT5lHWsupPdaZ04H2aIbNQM5d2Cc0S-0IL7kZ1J7nOz23EskyQblSr3sJH7uMy9V_wBJhlss9MYzCTeyO6YHfSSsdiCVrId8GlOu_GsmVW4aMeXiBBqO_I6jfiAiYGHnEMVjulJNM_0NFlUuF2NGUQwUh4AItQFySY15Po9KSfbFpYD6dHBRWXTeXmoqDPeZ_j9jHrysW--TRWCuFYaSrv6-ciCPMlpi7ma1_Un5y6XgwaOLUTZ3E_d__JCcpc-0I4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFL4B7eP9turO1baEVrgeUqgLyrviFTK4qnEMutMS7FGP3yCHLGVRU9-h22Jz77sPjBW2N2r79XLpAvUWiAV-DfNmGqMiTRfJrlPx-Q18WBS1D6CUJKbFf9WgK_aymKloInpOTnrqLZVorulQKPzCunlgszXO0_TD_D6Xx06ehavESQwIjiLVd-vHZOMBuwRc-15veXCk4bCU5qTFfx0sAl5IHUsrnB9TkcunQTAZa1a2nsPDpnfYxbxQZGrnEhHBiH_FQ4Af8w6Dp5VTf9wSnUCLN9DfmfVIyf-VpgLd8xy-5yPKe7P7Cya6Fx5wcnDBZsZ9fXZPJtrUMIPPspWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RViis4PSUlqaCcR34wilmGlhA_NEJ-k-jsxygMPCehnCktJP-SpHPYiG7m-F5FsV_VXDuy7wb0Hbp9JbchnzNcu9IEFKzfIcFLizCuwlLtkYQUxiJrxudFjuJXKxaX5zxLZdHGoblufgaU-MUMEDNMYwoJS0meY_betSivDAZfKN-0j8UTdkO61rN_7a_ugON_UC73aGA6BM651w0AomTJ4ojwDNzzC-onqGdg_Cujpn94s9T6tXmW6MPdsuBVuDtKyAP190Khg-rACTT0qtuMePPeh6cZND4EaJVtUmT9BPDOC1zzyQ18LpmKScEpXgqsLrOA2hYlONVGJIUlU1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfVYDCFuX02-oRRrGq3jucsdNSVLD7QeF6dT8kJNhAJycuJqD5JXG7xQzUfbWGJUVypwq86H9EIqLtddZb6sTC0KAG_vslwZrPH0ZOi3v3HG2I3Khh1ugMJqfYPkVI7w3vbK-XBPPPYjGYTf2S3DSjyFT2_pgEPbumFwNi-4zN0ECU-jFWQvfQ8RlrroP67YqdBplEKHrbeBWlE-_UqM5IAPUZabJKQpDivWXoXPmx52_18lJRnxQZmYmAP9lKB8G3_NLwgPNNWQG3j3ert_N8vk25dIKsiwGldxIEppZuejjPExA1Y9G5JLI9XCFaG-pJJ-CQZ-BUhMTJvzvh-amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PptoitjMngDa3iEZiRa-eculHRjCfpfO6XlOIMg3qVVl_lZf7MW-cIfjo8BTTnwZ_roWuzJpLipAVbeKHNUc1NPGTexn8o4kgkguHzsljqu0xF4xLojBXd1RhWs32dYZL6rqECJ2WKOy04mvoj_cva_ARftoZpsXN9qEzLilglpSMQcjILs_kNi8GaFj5gLYTXp_hIymAJ0lahy-X3jrTcrT24yHWXtklVOa869SxmvWjoTZv2RXTb--ICDug5Y9NNEi_65xzE65Buq1VsCw0SDnv4yetBoblQMN67qmF8D-jEWhwI-F5vFSA3xFs7BOUlNCMGHpIEOqVmASJOL56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tgr3iQepbRaoi4SpDSkmVxRngR9Td9DIMjz2c52L7Vzqxp-SYkEeetQD-jx5yhEYsEJMQU2DwSz1ug8rIFDlyaWe7V7DVnCn_amOHctVkfTt3uErr2xeB7rgBppznwqXAp6FftB3-JmF69U5sAdfxBkrEwv-KlOySTUoZBKRu52mm4WzajhtQlBaxKHQeGf_IRM4hs2nopHmiqYV9NQ2hu2kg8YJ1X-RihhocKXP1mwAnJfwCAquJLEHYsBc88Xr03DP8yiisp922nBpDv3l6nKNCjbjrFdDsl5YlKSN-124FLYo58mOYNUJBIfChFqbYoqloOQkAtWT5biy7ni4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2f9pg5gzjszI-hVn8V9FH4cn05tZPLRqlz7tfoJp0MTnrZc7FzvP4Xk5vTUlPmVeeA2jwESBrJgM0gisS4GAm_xVeYBj0XDg2PN59WLwuK8q8HH8Irj36oYwGuVd1eKfgzRVHCHtLDOSQ59IlDpNoAQ1JsoGOX6XJhvSPeYSilEfQO6LVq1eUUSnXf1Cj9LGIW9o0IgeQdo3JHWFV0j19SYGdOvirYeEOa5pQHwr1huvrkP-7tfD1ur03ikRCaDtSUhKby2LYW9o1p-2eXIkaHik-QFZDWMedwd8CLNtKwSNzXe2pIo1jNbxL0y4Y_hBHPWgNyxMjZHNQkhw4aieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2AS3vbA1CZrdmwMOHsAJ5EBlTBiBS2HYdWVZSGLOX562d4b5FBvhNoVaPCcHH6iMx_gJ0fl9UOvm6COyYTr_TbgdbOgnuzfuUJ7AQD-hObCtger8hsQnyzD8PTacwJm9B7vFgX4LU58OnCVRL-gYA3jXooGk4CgM8fcvfA1rZe6Wq_xVDW-NupZCROH9pQ4CCQVB_spp6r_FQ2T9S-s_uFisPKZlsKPaTu9efyfNrQKakX4WJpdSljE2LyZqIC9_v6HGteoHt85YpGANzZwQPUHlhq7Y0ZLXyAph0RXmCzkBjyVFFeESx-QySbQrZanwhU22vwVcb5SdF5SyuXFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlySJNIY6Jt9VaJbK5Z_W6w1kFgP1iRrF0fvtoN6vySBkK1xGucD_Vc5HYvu1IM5tqPUf2vaNRU8qMoNgpGTWxW1PHgg8INL_pcB6n9pnqV2RE6kpb5FYBr-Y0EPRvpOUGc-3u2squXVEi3w7DsYdfc-Q1N8oEQGJth14CEH865mPmHF5EwGHBirwDYR6suQCBk_tV15xVSbkP3kevKheWZSF_TcbDjM1u0526vxBry_C2itvcrfBso1Q4AZmkZzFaf5l_nfYY0CJTECCfGbnUYktS1yYH7ePIGrRRHyqromFQMeCyxiZkfgry8kvOFb7lZIRtJTnsdtqJUOH3YVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlS7t39da0xh_KwdtyWFmmP1TrZWR-JzInnR27I7uru362P7Vcx9169slBvFeu1-BMFYrJe4rPYWJ-CWOsptXmRp-G3-dBreX4q5nG1D7Dh2g2hmeT9-XfWJv3I4j2hHSvqQaOVGFDb1NvVBSaTPB6gnCexbskmR3Ycc_eSnAfloDSqPVUPFYnJ60ePHHhVSUi3DRjjMqUbrCgNtLPRER5zgks66fZFN5Z0VSmyp9rYqvQtcSUm_bF2YMklyw1det7-lKo-1Cz0Um7UzwrtIfHKmw2nHOG6fTc-UslahTgs7JrRvOU-J0D7LEPS5POHs2OOI2AzI7v67_0UZV9In4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv156OjQVNF_2e2RgS51h6Kglj0LMqr_KAnciHvpJQOv0MkKQQXQHf8H3w78n1MItyobdAQPjaZ-nI90cLql-bx2tjGV-SAle2pYUWG6MNwCmtP1flQboeCg8aCNqm3YI9WX6pUIiKNA_TzfKhsxqyoMIsxurr1Yvc-7XiPDQe6NFHGktlDaTH4jURUPsP1k8UioZkN82wWJ4oO79ODpD8z6MilXcOTU5DfGKzCkuJE6YPF0sk4-Ix9D1nbblBOWVCxw5vgScJ1p3WRRFPRzrXJB-28bATNLaje8uhcyRctjwoPlC4ZBdnNEmJJhgNDJCecVgmzvXqPw_3LJhmFS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGhXZ2zm9IyYIYyISi_qYy--aHC7sygKLMH29fYsobCf8UJK59cbrNn5c4MllE6BqK7E_XysbK81yws356RpNJBKmlSSgLsKanLPCx5bYq4rgWvTyQtFl81Dlm38WNzanpskwjTA6CjZPIK14QofOWkiGoSLwz8m27rrkqJBtEQ5frreBL6pZzbk7OXDPVg2qPWCVnrSC4w-BK0nuVPRKXU_uX8b2KWa3rOrzeHP7UopxvD_GEARXtCvWW89TxKstM3oq-6r2bXFcQby2sMpRDukkLlpIVNbsehgkHh2GQB7QknnnrNAbLMH13CQo9UJjEYw3YBjRdwJzCiGB5MRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMzr2UYPLVfTcOUcvGRbtTc3vZ6tBtpMOY4mX8TGdyNoNo9zcslFLrcHIIra9JyqRFtqI4clieNW9CajmO9iNJHnod9UbJd9WaT35EffesAxc1GwC6JQC8kFJ4-O288N-PtepjLFoQvkCKqrygMVjzcpoQno5O8uRXJSpbqG4lPuf1reIB-nw58R-hUEayRYKLAoxVTD5cRENLKID9dQTEQbzEXYuNCLNwMOGWhP90kGJvv-yKHSOidMTt8F3_E51vooxcjX6djc-WhWRINwHBOUbcH-eROaNEwy4qfFKPJyRz57u_6SMW1TrE0iSxRLn9Zxnt-NfCVX67W7fkUBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urIcPOtRAVpj-rhu2ngjuDaZhrrPIlB4NrF6a08924FT9lkXLxBe13oqyhKBMZe92fDq_c9XXhUisNhUnRR2gnDW2YNM8Nx6BBL3eMUIgSHiGZfTr3wYAjJrzf_6WJoQ1pJiZZTeLD-_x17GCHu3zw-A-S5gqzNfcbzmtoUEYrV5SaMwFGIECjd3IOdDGCGuZfHoL-vkpN-rsyimA9MTg1skTMarlWk-bAsWbyko084RPf2OBZYcT6C5V48MpllGRIasdaVEgXGLFteIATNOOGCNXyFZQgaIPIv8u6KzhrjfnwDB-CDNFQX1Uvy4j9-FM_Yt8wfTQYRVTe0IK8lqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs-hMra1JP0JcK0H1MSmFQapxn_0zC975FNSGZu_65hJVUFKmcIAFjUxawV7gAKXKgIuD1CZ0Sjm59qpEFmJbq2tSipgdwV3grHFGLtpuisn0hAqVANTM-1wSK_l2hQ72835bub9lCZu_rVTLEjeoAvcuQNY2Y0bMj2rRZuWaIUtiNg0nmpY6IZVqkRmWlyKzSOSsZNo35cqJZlUVOTf4clXJVPTxHapLmJ6L_CRv2VKCu_CKF0jnKxJrULGte9LstL02Tn09HHtzOeglXypogsY4J5aRrrEW2AovPIqiLiu5QIak4iqSkOBLory7GKSjl1_8C3ldAEDMVMUlONurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6ompjjrvkf57keEmoaxWxw06R4CTBFVd1CVu2nnFduHhpE-5psLwijB6feEFqh8A8IBeraoVcEJPOWVlCWuLi3d3eF3TM7DYs_K-4AZdLVvWL4ZWRujxpRDZwMWUwGNR9nCYrGDauNIfiQ3fDzWap3-Gx4RAKq3dNjxTNhM_mZYRADhPPSzKMstGPNxyNCuvJw_T9mC_p-XxQd4okvC0kpC1qNQPktEC1mrPeVjBmYtpKONh_Wc1UDdxkfOwxbzEu9ZzgcoDsl0QaDfMIM5BKfRNSeIld8k9YGcoWKZ9VIVoHUeKRD76qw4BS6gRbhKiHDdqJSEi2eVI5XOHHAeUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fixeyuIYqWja9c2p6d5K8c6vD0zIMPxgdvGX9FqjZEZO5pmHHcTVREpjecgyJr5M9Zwvk9_eu14rcBkRyaqnUS7jmGg2YsFY21iT0DBfztMxrhvZng3efnmjT0v8d7tydbeOFJx1tTdVm4W02LVJ9JWagzd4eSzihtvCh0d_GFrvdKKmpdSLxYe5iupk7EEpJaD-WWrNdF4wvzdA4BnD9v2hCS1DCisWSBYPU7HkLlWpV71YIc3AA8SMXPKSBHSQMebN-7SJXueHIt3uX7So-UqnH2cFyY0gDO5y0zD3230wtIBE5eokoyzRvqbsHWyyCT9EczviFRpNPyLkqyeoNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln4mw_37II9bSRh490alQ_YXwNHb8nA7RGLsmrZEOBIQGL5w5dyVFvWjq4KE14WllAhPgYxbA00zY5HstJLA5uzjJabwAvUJitECctkShmfy5IeT5yrI9PFrYRfgopvzomE0bt-lmuX4UpNVqjC7hOFLv2FnFH4nlO5KIW4BqiZdYzhn61QnZIh_EgekN2XmNLTwUxGz3TJDtaMQCnfkQE4viogARbnVDbNcoGVHr_TbyehzxOwJeu5fyGZpxzGVmofckrv4eFTqj0Ec7reetaSsFNPm6gdshOHQ5JZMtzbeyxo7tfCmObt9fNj7SHPLifWpdkpc8dyNfM9V100_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGCSNw5ZNCExvXWR_QLFVIyduLOZvIWS_RyPHaL10QEXt79A2nhMs-sgjshuyCXh99t_HOmr6JVZYV27qiHFCJmaYbWs8gFaeP90s6jO8HLp7TAS8gCZeLADcdOgUaO_yQd1C0UCGSj1J6dX0cJpBUj6uSvBy4lf9OmvPRdrbgUcUZsYpzPK46N4Hr71ORWBt5HDLwgWpM-ABfOlS11c3y77z7neDOBC8ZK7ked09QzGQI8ECN8BAqBByXjUGX9vfbEPYuGxrlPRiR0pf0JjgImEpmFWo0lcZ_yiDNWCHV7VRs4Yv94FvLu02ubPp45VG_4KxoPg5hLouvkZCHKyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiyAt2L_yJEySG3Q9quB9Z4zsfOx6P8gcGm2YZWI9rxsFUe9LJvCdVNP3pXeP67_pQP2k7xYfVNzAoz1G5q_xkQGdLHZ8q_hpbm1h4WL5KOPGY7_HWjclhpeIDQpxXwZoihrVjIcsgH2PVaVpICbWdp2XPnheG8U5FtNwZBFeqVcdIfB04GnZv7syDkIl4vmj_4_TJrnCl7QLRGJzkKz5OxJ6zgLFQYlTc-ygrqUfx_fbyeNjbAGrecpAQTenLY21ETKTQCFDfHCyUDVbN-KL4bwSxsJk3vmM1QhjcgHf_GhayluUBFxjIZBK444nmzVGv0YgsbGdzaWsQ4h8uaGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-haVhZ2LRTYFx9rVS-RVYGK68jxn8GtZknFGhv9uPFhPhVmGhF-rbiJJ8_7P-OEKZ9mK-4nIEwjaOzB_ROUiWRaAbyNgQqyGlQrWwQZQ3d-lo3k-eVpEUP2OOKB-EeDeIxSF1czC2gTQeFSlXEENbYy9InHy3LBUbG0PEnsq9ydRy1wNTdKCIikIS1LyOSgR4JrJcrJJm80xJT50w_-7dd1Kz48lvuhceHv_0TPFu9rcjgSzTO0gwl-nVMzSe-VO9Wwyfchrcl2XPWNjqGfTPMMFacMVKlay6G1ENvQ9R9HKpzpa859gkA1dsPMImEeg0llQjxWnyCQ1z0C1mfUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLwI7Msm35zA0p4idAeKj_2z0WKaD9glsfthsnjuMQ-wRFgJxSmB6DnWrJdUInn3V9SQC7bc41PYlNLsAP7ekn4CksksS9IskUmSn2uWGZ_u9WMbhL2m1wl57UJJvWEStkarrvpvNwdOQrIprwR9y6nWyHFwQFGfe_EqEilrOYXH97bQ1CmXtvSVyaxl_zE4N5ADgWSw0Q7nOG6daFyiqHkMy7zmyaXeb1pkW1LWWUSKEpielG6ZTQ4_bSVh8Mqf6hhtm_JZ0vqmJUNHZLlA930NAsdMhiibvIYpLawS9Gbf-eAPPgGl1jiwrzjAeSe8M0IhSAtNUjFH2-nE9WXE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUeg9W6ZKGOVVzP8WG0vzlHE-M1mBiAS7r4QceoC0ayZrzNfu7F7d8a7UlIkCwSRu4_NWAFMNwwy_cYJUKBL1jByq8cyHaLK-rGE_HsL1SEsaerfL8Eol-hPnFmFmZk4swdQ1xhZBXbSQMmB3PzL3zipWKarFebKavh9688ms8-pPcXpG-AD0Fz9XN4yO-AzkFJ7PUyLHpW8qj3F41bNN9mh6lD89KHF3-W2b_6eaeOSY3Lg125ugnHDfMbVNNHYppPWDTRqy2_cF65dhUuJTvynHiJbIa58LANxNC0UQBA2p4ELuNSaicvsKSVVHWl6ORmT7UDcEBv4uOLU-MAuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZfuJiptX_FXI-9ojoLmlEmTe09KRb7CDmaO12LgO4ejv7FDfYEUYWtleye-n3rjJUwbCkf0064Jjm8MYK4NdeN6FRZcc0Bk4VLTmXUJuHy9WtHSP45enuM5FaL6jAdfiLqwDB4cJgox1V1K4thAQYqR-fC7vPZDMNiGehlho44w-Ao9vTxvfWgAnzpjETFTHo5A3M2qiAndGIvOK9ZH2KiRANuSJkXFSUbM7qJEyIQY3uKYMwhsjNmSJ01KbxEJqTs9SFEZ3MRGnOKUvhhhjdhIAiKWXW8xSYs6yQU3mG4KmSRMGFsXcj1LObpWL6O6TR7PxfHrccE_Sqes1CLRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=tSl0095KoUEy7OoFHYBFgiMSveXkFs5oMk8zZ6CDGa6TMNOdjk4pcgmx5LqdFCr4cmaKjw0cvO30WCORHHntOtv_ncgH1C5EelDbHx0PdiF8hGWiaKSBN-1NfHm-mGxr4Ffj_18CbAiOLqCQuiSiptBUqAcGxYoibhTtPxyNk7uynsO4Fh8MPs0g2dbLy1zOIi5iJ7ryhRwWEW3-Xs7qZ4g3870MrjEMMJS4ZBo5SeaviypTAy4aZ4HX-JUWNNfza8CAnX1Uw86Ep_st47dlQo-P8ygFKA9qDoxl4LvuoR7XO4GlpO1QReGPJp2bIzmLrDLpittSI32FP6opUDu2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=tSl0095KoUEy7OoFHYBFgiMSveXkFs5oMk8zZ6CDGa6TMNOdjk4pcgmx5LqdFCr4cmaKjw0cvO30WCORHHntOtv_ncgH1C5EelDbHx0PdiF8hGWiaKSBN-1NfHm-mGxr4Ffj_18CbAiOLqCQuiSiptBUqAcGxYoibhTtPxyNk7uynsO4Fh8MPs0g2dbLy1zOIi5iJ7ryhRwWEW3-Xs7qZ4g3870MrjEMMJS4ZBo5SeaviypTAy4aZ4HX-JUWNNfza8CAnX1Uw86Ep_st47dlQo-P8ygFKA9qDoxl4LvuoR7XO4GlpO1QReGPJp2bIzmLrDLpittSI32FP6opUDu2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2whvZj0dyQ_qlLmQCC1VGFAtjTz1hbk18a4ESKkgtdRq2Zz1D44A1A-gtAT9Dcv2Hto9QBUfo1vGs8rrbgGdLQdvv1a2LK-jUWkiLvp2umsC08UloOIL2ccg6_cpE5H-qmXdn9mivJjRqnKu3J_j57lrRGK4bxa8aLcga-31Ckyvg27BwXwLILd_QKTzZjkUxYeKfQY4k7CnFIW0Vk9zo8PHpve_1FzDSNN_FW2qRMre7U7oFvbFx0UqlXF0IE3sPmdG77mbyZlJFuD6Q10NotGAOLkqOgMueFssqhSueKIHmlRlNwX8l04O6RuxeVUXQLkpmoCdWWDHXsQcX4J1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQTt0NrfeQQsnjbEdcNhy7gdf8_RjZ46hwxmGBceClCTIIGseT6fw1WpovY4-qlKs-LaM9rKzIhwnwCLa65ASlhuCQF08pYAYa7axIrV7-xLk8P1xIVYYyFuhJQOB3Pfawq0DX8NgMExf2hijLSb_1sMq6tzepzWPASOXCAtFAT3pldkG6JpbcRNzZ6Yox0Gh5_G6aCh4YlR5SjWL2GYmKr6mpDPdaMPjYjAdJkDZBXKhkYsE-EWvT3KqAXCUimV8-_3QzVQSN3fz9kTq0twECeWIxlsKpo66PZZ6dIKR5AK9i0tUyjq1lIyJ4RVOpWbwdETUmiDz5vB_Dfqd1jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjNySQYGnjE5hn2Esv9w4eCtFAgVW42u9o0B6DqkMx2PmqX9Z_dk8Q3uEt-VEOndh7G5QaeOV7K1cE4rR5jmWapUh1kUrv7He1Tfw4HqQx1wj-2DysDsSHb5S-ueD_FlYPI0dlFFs0hel8QQSc7D_Q6Y1Ys9cypM0SrpBqvDBFD7NriS9n4oDirxi9bGsVQryNUFjFJqqCVl3ONRKJCj2bHsC0zm0FBOPGfskb2ghlHdSfAJR5h7xjK-9kdLrpU97W_GGBeIyd1rAd2bFH067AnAzRU3aY6REK2YkJtia9Kvot5vf-zLlpjeceH2YyO9nlgoDblMysZeB7fKOxrnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utiZD-BR2x0SejGe49OBXx_uUwfPAQaU7aQqMm_6e2CsMxAima4kmzYD6K646S8vd4l25SntME6q2n_8RCteFZmCh82WmS0qmjpl8gEbJD2yunyssIKmRCWG4HrRIlpDWOdPP9ygGzhfBeuPpNuMKS0ZEWsy_DOqYqCApH6BD1IXKcprnENjc0F9Cd5LrfXT3t_tpOgw-u-ngwL0ajeFN53w0-dPFc4Q1l8UCgcSL0mq6cYIEaeQY7LAuweP2rRIt8Y4lp0eX-vjQYogtEL0wEGmo-cpq6iFbxEtY7g5Le971nJ8AiltRzxBV3ofqWjg6q60KG0vbD7igtPaYyCxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT-WPfRrYHPvsfz-x03zvcoFb696kPiu60c-SMJzTrIya0WD6ozyQT1s6XOeiCBvCOVYpuKjQPbb8hQtmSYgQahiN7_1D1tZyS9Fk9WSf4b-yHaA_moBuMlAIYqt4KbA359yT72A5L-MUrDH8B_O36rhWiYJpBm7dg6cMWbJyKywpyZ-dZsM-CC_hhaYlLxNMco58o11Nd7s5KhehUicEYDBMDAKb0TYIgIJ6dZWMxQXGVpnCZBr1ARLsg6WbrCywHdy4yX91-OXWjYnRn4rEIBFyqNBrf1p2ywqiZmJEShJl7Sh_401gskWqZLCoe_VEq-Ev3rnDlENovoUGR7dVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We1pBINEjGuw3HlIwkh9joSX0kYMlQ8Ue2CpTtlb2SM5qKi3daR47Z7UBDomtXnhurM9ymENaoiu6F7PplW0UciQ0af9XqVnj1kWNWEtmTbcqL5vd4BhgYNUyNMTDY5fDH6G_rkxbmjZ24Kxarj1bEYW-6Ao44SZnTLZVCObJ7C06PV0UBMBgC9nVlWJpWqiUzMu-BkFJ-0dB5VlgaOxmhB0vnJsjttgkcdvVo5TRCICWfu9wtX_JuXrofqDpAsXh-zqxmh6hTj1iFHHUwTusoKtiZgImM8R1D26iogjdFmOq9fQm_Y7dWwaYxASPDA1SsEufrE0PZNjayNOufRhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQnaCs7YPaeWenV5CRBcAwUSn-WRJAkfF7x4Va6A4DCYbr5QX7l1bTmWKfeK_nhuOfIF1qzQN-uV1iRD_6H2HG-H8xyV9lUXXLzPf-oP_X0PCo2DiWLEOKJOhu5ukKRFMMN0n6vN8XlkXAt0t42v9fcP8mOmL7e0-Ol8gg6W9809TGDgqA-W51ff46epoXxKl4s8MwSiUsT_KpDD4V_gHrJZdv0YJNEPH_11LROVdpqMWZAFHq2VlPsmA1TAe-imFv2xzMqMM0W04uvKRWfmrmatjViCVzaCJMx_FpIssb-P0UkKboJu1DCKrmt0cHmrAVIp_Od09gt8tKg4UmmSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq4saoNR1gxOoCGJN2JpghWTbuPDbKiUZaIGo4r6Z3L6oKoj67D4BOjlpk0sEWSEbYhtRQPze1DXh0O-E83YPNv4-_B5CLfp_OWZy2subltznbWMk6mqwL92JOIalC-4r5yUqrHjaFE9EOSimJr-HRsYdu6k66xrKRoymkO7C8HZ4SVKtbs4kxBSh1rP9EcREWRXgmsoREoLUUHcElzq-is-vd8Zv05oVFOyYiRBrUu6rpVtjbgV0osyM7Iw3obiQmFZ-K1Ub5yxN1IohsblbMntpPfl7hRB8vPWItLCfHcttCEiGH6o5Xt-0ndX0bRKM-xMLmJqelepI64i3Nk36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=OZM4a0YQmtLY39MNvh2TJC53FBbQFsvc2_4kqXnjXyA5FC4-s11kOx9Fpfm-4IbhT2-CzWpZPwPMI5ukBS2ioTmb9M-wyPB5lD-a0pyW5DIm5ctZdI8v0a4p0dphJuXA76aIToI0O2IARZBlyJl7oKCk4C01J-gTnFX0ekf50fh7I9dAA-g0n56pD5T4gMefxk_QsfsCf-HxpII2WpH-zUx3VnKsdiQDSATNF1dAprcqsJiQ5Sdk8n-es85N-pFpvC5lJ8IhZMKTccw47xs4TBaOCnu7eub0XykxMivBKEfUEw8vWfKcptnwYD4DxqI0Y1l54nSv7AxITe-eeFX2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=OZM4a0YQmtLY39MNvh2TJC53FBbQFsvc2_4kqXnjXyA5FC4-s11kOx9Fpfm-4IbhT2-CzWpZPwPMI5ukBS2ioTmb9M-wyPB5lD-a0pyW5DIm5ctZdI8v0a4p0dphJuXA76aIToI0O2IARZBlyJl7oKCk4C01J-gTnFX0ekf50fh7I9dAA-g0n56pD5T4gMefxk_QsfsCf-HxpII2WpH-zUx3VnKsdiQDSATNF1dAprcqsJiQ5Sdk8n-es85N-pFpvC5lJ8IhZMKTccw47xs4TBaOCnu7eub0XykxMivBKEfUEw8vWfKcptnwYD4DxqI0Y1l54nSv7AxITe-eeFX2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMQLCl3hQMIkVqqInFTFXfzlT9bjCIq-hYK1Di8LdFduzsDJ6ryMwYGKjPGfgGMwCtv1ApvNDwVvNkkaUxKwx1VM23SAKTjfXInk3CWZm4yykRhMQQoebgzQoz_3d3v-sQGWbh99-gFzhi1y2lukRMG80Gn2qwPZlanEpaAYV7ly6anUCsv6DvjPkWzQQ_oM1sHmZVIFMPnPdkVKEwJlCwWAFpV4sCkzdPyrg_Z-93P-5GbkG0KgrKWuNQpv9wqimXfTuCsVPdNKxSQ9KPGGoWiVyD59XRCmBeahM14RNNye3eiwhEZLFdt162SIixOsDgh-X3iowjPz5ux8DiVptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J46SvtTJx6Ds-fYs6gn7Ut8TN7jvonCKZxktLlE8VNtZAfqRnEP5Oj-FCBdtvuTSVUdC4bTRBAUVcHERCp-wKGrqYOhf7QpZox9gOBk1OVjtAycuOCmus274_WwXcdj59tdTP2ZYW1ATcVM4NUT5NUoxlOgHzce8oquzYhlFl_P6RzMyoohI9_7cvt4-M_DH5tyWZ262TvbzrzATl_IlEuL6nHkhPSFSusL4l5CDAw6cMq_PebU6yPFeWG-AYw5R1EEctlcmLnQu_CMpyZXylfccl-3Hj7AdyAZL8HRDsXkRAqxTsOtR5vQgpfKpWgtW-8QWuyVde3TW57XY6qeDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=NUdMJCKcZWQ_0YNaWz45eKuJsQN8xsdEAWX-aNReSoqdWi06Mmz6f3TZeqP9B94N0eRg1STmg2g1l0uPWFRZiTR58w-8JnNHk9rcWET30tcU5G5u1NdyiRUzpuu2I0UQCt9qUNtZKAFlo4Py31qE7eQP3Hr9LSi1TGTJUw27WKiZJL3sEmTkHaFJK9bwhEltAzNAv9NKg_HysIPNHvUE4P-MWaQRvj-f_k9RjjYS71tBUeNqe6JxAzUhDjVvu2JQ-4kSNzfxXfebEezt3KnpAS_860E_FsYyXFGfw0-A1bbhUJXS2BK2KQioS_v7Vi0xc6LKqN1BbMIhtElmRecwvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=NUdMJCKcZWQ_0YNaWz45eKuJsQN8xsdEAWX-aNReSoqdWi06Mmz6f3TZeqP9B94N0eRg1STmg2g1l0uPWFRZiTR58w-8JnNHk9rcWET30tcU5G5u1NdyiRUzpuu2I0UQCt9qUNtZKAFlo4Py31qE7eQP3Hr9LSi1TGTJUw27WKiZJL3sEmTkHaFJK9bwhEltAzNAv9NKg_HysIPNHvUE4P-MWaQRvj-f_k9RjjYS71tBUeNqe6JxAzUhDjVvu2JQ-4kSNzfxXfebEezt3KnpAS_860E_FsYyXFGfw0-A1bbhUJXS2BK2KQioS_v7Vi0xc6LKqN1BbMIhtElmRecwvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwsIHrxcdRl-blflOJ-nFwMH3JcmpqAM2e3_gO7_gIX7HQFpNSsNe3hi9WUzW0xODs8LAWtrNm5Nc0KmHBBVYojuMKrkv1KXXHi7mzCQaxMLIDTH1DR-XYMSuFzSWKhA7FBCnvaeykjmCVlsv8XhgpDlA7ym_A2iBezynBBzCUdtNQLWoroPQgdtoh4OmqIHpAT1lluss_JtmbJfalpqtoQh8Oe4hv_L2EBY846uiA-40cd4bKPJ0O7Auewz2ipJLJy8Qc6QwysDjZ_U4E1v4y-ACtZwtml6yLACFgKZ0YtM0BNlEiTIaQDxvzg3Xiexk6znEhj3o7J-LEZ0Id_TKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MZjvZvjAPbbz1jPvXGDU27qxjvDOAqTkAwZz2dg0dRVUXUgOHyMAlM4TE2kjRUbW38DI-PyEvnbRdNZVdcGXMw9lhXnIMz2daax0LmSLaU1JWj_Fb-o6cfFxagsMofjvooGyb6zG2u5EQSjEWc-qq8xKQ0QzyA-FBvsSRH2-E7yyB_Oh_PA5hb9j6a4EpxtbCWJaf52-HYVaWb4xhpkt7Rcm4ZYDrwJfk6xX7PKKswobMZbRwCua7WUdR0eHW8Fja9oFyPZglRwiNPn0feF2BTv3mprwCoUhMRfxpqeKZOOooDdzuufd4Sf3m6lqX-fGuGo-M-1NtDgjG2X25rJroQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCvn2JmKFrtlXm-My7ozAMJwuMGo3JC0VhIy5lP8VAqTGLlxWlOEjh8POXnduDG7ssOkWoE__Db7JunSyqSGmHegQej7mCee-J3QGJIcc4ockZ3cEZHXf2BUqpDm_w9RdRt_Du27-DT3AP53o-fvArwU6P5MorCqKGBte6s82UeHLI5Hsxg3yzopqU1kKEKMbGhBSywraifpnJiNuHZYoBAOru-4wdt7TeKfw1NzaHHshXSl5MzznaVWQ-0nNvPFZmm5tKYDN1lNOMHxbzohrk1AzSQOIj-YI-RldFWEgOKqW_C3eCXZh96-Wq4NX1MSEh4_INZnmhtNV1GknvoUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLmI6-qy5Tlb7-Rzv93_SvzPZ1AAXaW57rBFSJ7ZwHSL75VneHWmHpqRxYiwABtgvfze0PwfhKPZn0w9p6wNy5gkFavxiRjsw7MuDLYmsRmE5JQI6KbCFSyCP3R_Nt_OgSmAqPtWPXezzTIlszsEoF5nIyTjYjdHnHoKHqE1INTjXLa9tDbXxtIBLUu8QQphVAbXE8fiuSD6IsXULcg-axCfoGIkCIsu9efY2ZqVCeUsF97gBpDxInXfWDU7KYwg7Xamzbddbz-00ZTg55GhUrMdjcaVZBREG4eYVBEAQDfg_LtXMPeS2FJgZt8kAeSpP5bTR6kyV2gL3m76w1FYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkK4DGzUN9CZ-RaKrhRBBVhZpSUEkMPZDSjtoZ5o8L0GJiehDCpoXNmMsT3EaOOEcchHM3rW8IJX9B7k_2dpKKCbhggJDfgNv6XDV7Wob9TPz0dM0jO6RM0Kcle3rZKFPB2Zr4iuSwH6OY8A9gGVvmd9EBnwyzfWNK5yCFO6-2IAQHMiTEGYQ10R2v3tL3ffD0dJtVJT-2j4kDh9LscyR89Z3EJvBY49ohsa3bWIs_HPvv91UifO-VGZsnXFwIgoTfAsHiDRUy3Pdvygt2CW5ucv3rElX8tpYlWFhYKrt9HNvGc7rPMqjzFkD_Q5i0iY2sFgKdexIJNsT8wCuJ1o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXKm3bCv-VrzZ9yJLOkNbZb6nQlLrQEGvP4tml1ydHhrrSVxrZCuwKD05jB0OnDaK7SK7_rgCgY56nQgYIO7YTj165DNlYhRvrsrlgDT3LY1835pNzV2WM9xlhngTCD4Ox1YI_kD7rc8tlzrlHP5uHyoibuH7CQNK86DGA-KjXuY4iv-5D3yFB4EuuwuCDzeqz20IcXNAURzbBAtvv6klRqckA4oBoOXXGSTKk9wA1_g8gpZ58s9uyjrCW_CiHAKFBk7gxg_NKBhszkMA6aJvVNvL3h_KxeKrHezd86ZmAwAvUlJgiLxfkr66P2p4UskwaHKLovD9o2Taa5fknbibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhIAU8qKO7XAM7Yh8GC1OqP-ZV8qunv3zoUpYxrxRy9WFPxg1s4h-PRebpuxanhHY1lnPI47pDFSp37M_BkaYrnJf0IqXBfx6lMS4_1CDrGufItSY_KGIJ-HSUCEgq3SFrFqNvgKdfJck5XEseEkOE7m1voqSKHy8_78j0IU8ARQkbgm6O_-g4IdYMJBkD-gDxW-HGR9BTd6X8RROgjmmlq4HD2W0ZYdrHTPn8XAUYbPOdf_A4fcjX13Wzhr6y2Ba3_fhqn5Mp_MbhQwktH7xraomm8J5A9Ctn6rm38QMTh2K6NOzwG4WKryVL6gPNIFV2DQsDYVn-8iDk_zPJ6jMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSVfsRX8iuzXw_xZ49WISuP6zhn414n_f8qVJK4kveuceSrE_6tDRu5VAhLK2DB0BN7g83dLlNHQJJlbzE0H8QYx2Dnfbe2TOM5g2roBA-JnhSw46H887Qmnixeezp_bklQv15xdrB-3sIcwjcAM7f89IgfWpTuCfLIh-eJg6fzaxPcWxzBxyU9TwU-bPqAGYoCwHp2p1nVabSOZQ8YRiqlkqQJn0Txr2O6HFoXK9KePRQTYiHEM56l0Ym3pWHlIj-kE3x0s8ZEmTVcQb0GgSsD2WbAo4SOHR0ZKJlKC-hh-Mr5v-KhXxWUnMhgsrNcRnrgkfoADZ-bCBAqleE5wQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z64dzIlknqenLxNHtyWZ3abQHCykDPlisWgBx4zlslEtrNnD-LKV3VR51LJdTo7fgMoP-r66NBNhAbiGzb61fZ2oIMg4ItcXd7oWeG_-18i0FGe3NKbu6OPFR85S5t5NvOcu-7pTpLmwA7UIG8EVqEqNTCDCRT0fygPrOY3uSxZUZRbr6l20nxlMp5NK9nuLuhUneqT6jTgLS-dQdfRWCZvjqvpoLZkDwFy6tUvJK2rLw9GZJl4gc8hQweEeM4MoVZOYC-9HJws5xNMqXvXUihcHYRT9XNe2z8Zvh4wjtx2TbU3ZukIu-dQN-sfNXlONgnETt6dFo9HMTkEjym0YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3LjxwBS5SnMd3LjFOldA7ZnS1uxTO1GccOE_pxYC-6SJgs-p11xbx330xpClXvjKaQL2RRtIvA4RnWzVEgPFpbHJIcq2XhUG2q8jnkfdFHEnFFIxs-VaDPNxfRo1Gu8W5IcujCxCqbeAtznxDD6MAXxU4XCEgFckkcoXRJszUFKeUNVnlWs2qpn4gcHpRMxKPjinhOxBhQ8trW-kdNjZQ4MsCjaxUFp9FIyzBwF9u8x8qsPapwm9FOpYqywMlSfX7WDmuh5jt6-TbGZ9fZPJLkaGp1R0elSabz9Io7tU3A59OgNa6QCUt344REmH0TghsBhN7-b3-3JCTL50zgMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsHirNf1-78eJJplhoDKALWSVVwnjzB-0iZyX8YWdGJxBtX284rFkLXAaMr_yuAzg2ypaNeOZNKO9I1NYZh1p08u-pAiQ9cKu2pT2vqMCs83BX2SS8UpArGpn6LRO-1Q2tEctIsCufD1WmeDVrFWQAnRqPvj7MKw5MHwQyl8JRE7hfubRdbCarcKcfj_8-N0nwmfjiTm1J5SGvYuJFooZ9QfOCxaCcUlQe05wTTo-AzdPg7pwxxJOT32YD3PiIhvTjCL8Uasg1rq6vjIh1ffChmXYBZiUE6cNbwelsQrDtCqyWiDaz2EAfnq8mwArmIh59lI-Uey9_JRLZumci9jRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maXepCLItHUkhoDdW65Sxm9ulsJvt9FdRhUFVqqVW_efPPwdaiOwerxMnYnLvUyInyWBlO9Nn8zMFeJRKCF9QWz60B_2BnZNbjiG1Zwl1mpg3tPj2myBDYaIQboyH7NInYH8TFv_lwJt3S6neJgn7EZ66MIw5Uck7BR2zWIfD4LUl3_pSbfPL6UbSkQV0b9egEtvXKjLS6jOO8iYM1n8gFvoDtOWzS7CE1YDDrcKtG0abgc63uyj5KobrK9ahCZ_wrAqIbXYPSZ_NSw_di9sjRO44NBzENEuSmhN4Izk7T6jpjYe-Ts7bfnN3IRGY6XexwFDhnN5FY0Tp06p7J3B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRfr_yxAwgRx81kx20T0arfjOQbJZBvt5AD5O45XisdGsNjatUGztiKofVFqe46QDXHzG8pFNal32sEFcUJC-mnQgeYSxtm3DGeSTTbmE8blBa99oV2JMIBhNHJD7Q5KZmjnriUeL5WHWS_4FkPxDl1wKKjTXjq9Nbkv3KiepAHvvhSzq9SAyNo7M4FFVQhbq7t0JFslw1PKh8cX4IXjUmA_5GgcusE3VS6JhwY8kMZ3cDAQmJ72iIun94_LcPS-F9e6eDDwLEsA-I6z6v3SRJ4qDDMTYNDuUqUYK4Au4mQsSnd2palEtLA_msyc-rCcgwFQIuBmk2u3pUaMYnZ_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRGOj9wpSr3mDXlhkT-gB7B5Q_smYi9UtuCzTcovJEndPCuJ3E5lfXWlItzmiuMWaiYQhkBNSU8Is3fiFARcOs5958rkELEKXv6Omsw3p9FJBmRUxHUtxpidcXIoEokWVNkj-IhL5Qi7Uz891uBFUSxy_P77dM5883Khxj42HLKCvrf-fXiw8cTxJktv5-CZe-JHNlL20YyCCM_lNtDFPZLMAdBJOEk7W03wQV5SFFmWmuC3TJlm0ZhcxIFxtw1pwlBGjwC-dG84fBC6B83hr4MWHahVSwzpyQTyJHFHZPTn-EozqD3AwC4gdaBU-NJ5hxfXddGXn0bwn65IY7e9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
