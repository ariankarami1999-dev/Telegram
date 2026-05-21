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
<p>@persiana_Soccer • 👥 201K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6J1Wbytal29L_FmGPKtA1th7RJ8g1vI8LQQI805zQI5oQNVsAlINsC_d20YmiS0nI1TYR4tqVRK1-V3eg7e2lIQ_ce1B7lCm0JPHmtlp1ypvA3QBFnAmSHiwelCImc-Fo8VL8ItYsJscKCIHhz1RncU6VpbNM719uD-xbSWtsjI8PwcVVFPp6BhgX29Nb3UgGSmr839OhhbP_iLfpNThMO17d2G6cZK7ey6teNfZq6jjq7wpeE9E_ymTfuRCXkMZqzKObfyio1Mq7EX8ldtr9UNDrXjRuvhkwNi417FWEyG10OPHx7Ti09xmQCDIPv7O-ksdLKy3i_Vbc3i2mh2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuvaL50hQz029fHOw8BvuWiGKprXQoMLEQ_XrW_e8rl5GsmSt7Oemkt9xtjD-CLQ9MyYD8LB5DiQShhDroQjxf-ZnHmM2HZ5i1sVeNmkaDtsPawSEC7syxg9orI0Segb0l4Tpi4DuWEdVOdXU4dp00PGWtddcpA6tDQ_O0g8-CSMTG8WuiZMKgWKuO8dSmweuZrKHtDj0iU_NfFLgzN6VPiXrknNCSlVbwgfQHPyp_Z7M8ieFo-0z1f-n5uYtdgg2Brj4NmXvoLUQIxwj4xvzpiWQ3WGNIZvsnn9IzvHy3meWFhHzSRsXgnV9K3Qtcuy8aOpXql6SzdL57VizU-rwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/persiana_Soccer/22212" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqqQ_ouYSkKg2MXRo0bFyy6Momh5OKP6n-9Yy_fOJU6YZU1SZ5IJXQ6MYblEmCEGIBmK5jGiEQr2eZpwoZQYVP_aygYbsjywaf917JpJDNLIFuZa6jJ39benD4ibInAyHrWEJ9h9ajjnJ_D1Kzs1J5iNgHoukJbn6DfwBxX31x20VdWsCEt8A5564n819BhElVsjWjbAAsowzdpG5ohYCfg3PqesKU3MD98emwIGYKkFBsD5hB12hcDv74wY_H8S6fb5N4CBRb9FVbhxT75YA-3D9rjyhWB2Z7yv5TJiWkeN9PAfNGjBmNj2Y-tYI8OEyS9m5NV70-fzZYlazyhiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsJ9ZhBpJiV4G5f3rlk4MbYvUl60ITqt7J1RAFAsTMDpeGpy7isF0QF-QIcyx_jX7-_Jk8MTgHZ-uk75NGa-HBRidZNBivuS-fxTM7FReaslZJialScVuflWAefzfrEDI-5ZMLYuiX8XbervNAqO7S7ApbwgFs4YwGse2sXnb2CrFncUawWP52E3A7D8NFaqWEIUQzN5qdQbsjNImm3gjV5rYehKav-ZoRlN7-g0bMzyRj3usWO0bUtl_GFJPdJqfGPyM2tQjAc2gj4lAG4H5ypnyZURsKpSM242dZqWbHhzPPJBRwIr9AiGhHlIiiKnmBQyIXjc_SydmXHTXxR5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRxCcWGezD6nf0KR6pKAC3ScpkpcJkgIBdhK5ZJPdM99kp8coOd21NLMLLCzt5mkbGFTEKokuw6GbWehPaFBf62bnSh6rqM2zDBhlKJ7d00zyv7WOk3RubsdDJ9QBsWOXRlIKfIjl9oWgjNwrTP6RSDcp-x4FxuTbhJBepnivgwsTCOT8VGnqLM0iiyLFiot39FGXqjTw9f36w99kN_SgQ27DkqU-R3DsrZJUZ5rxx6EHtxiuQETyam-Q4upkParSpOZJ4u91I28SyVIzFgOOumzillUEn4GNLpf_S30kiFE_glRukaksamAafMOmOdwW4FxlZ7DzvidoL8hnvQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOqj5SfJwQNcqYMr6OnT4cezIl4cGikU6ntyyC6nYb5BgZ2csDdxbVa77-0M6crmMWYx43zmwnMFfEohjATBNhUoY8Xyy0OutCLnAWtMyJG2c3w7VRXxRzByR70IptS3UtSFM4UtYQ_d_rOfFRJkvGaP63rwsT62HLRLCuLBmqb3oRCX9_kio2EijI2s2f76pmKigiX8wRxXX_clx31xtlZ-_CvjYNcmo1cxdTT1Zk8QTnSPyHCIGr-_R7C8Ay_w_f_Q1PcmNUNnCUXE9V8H6ClZXWkrSAuPV976MY0-g_vE4UhnngRc0dTjbLOREGvwMkGhpfhfhcA03yOJiowDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdxLx5hzevnX_wfbzRu6ztRUiqtOm6OvD4WYr4Xx378sJJi3ecjzeIi3_OxjJ6bM0beQRvsxuYRuijZaJu-J0ydz1bKDxN2oEChhMqXy46EHw_qVxH1as8ye8VqfLQATsW0dSBMxB6Ly8VPqlDxU_2Oq-SqYefjU8hnGKD3g1SNIyLIsf0TNZfYPGzEN8FbqADUFKNuzw9RtE5V3xh4bRiFD-rbNCrs1_Oy89jwAyZ2zdt_vPBBIolvCy8f-gGdiEAzxQXFzPO8hp0RLaPKYofzJ0IFSRPPfv8EnJVHlWV6ChQIGtuqsys-Y3c8dqEvOkynJASUtG7JhNKqIHYZvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lP0yx0hhl1ztyHrt9ERWKOumwuin6RVET6YKmxscGey6ZBgGyhuk_9TsiImH5VVt7b9bUmmFOpSTSuppPdmptY4nRydDyop2xnKyPLCUJwZrFgpeh2Gpx_SESoRdokALd7RAzKu7WOchzRle5tPBEQgcksLIKmFD-uw9EDYpAk_Zjm6_w8smaCjUhKu6Ou91ck0lxZKqnjPgfGqJxwHpoX4JiHhZzCbLADEWRYuw4abRRllZvO_NqOpVwTUvw4RqCe-xR6YTO21rsNcRgBsxea2BogV05m_LBgxEozVIQneHJCIznOO0jSzCmJ8aQrCJ7yiIcKaPgWFICVapC236Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgtw0tmeZ50w_RNkj9yBzKYmRTYgoRtSvP2Dp0WPmwxhVXmYIf3Xg1BMDbhQgLb1sgi6kljkb8Qjo5JZNH_ThV9ZYr0J9mlgQhDa_i8_rriSTHuad6XJQd6yJwzu0nJk1oDf8p03Fpa94j-r4jpqzpqakISuD_m2MVZueyEayWflHFVZzAKsMvrUhXDTpnNoElqVu82w_8PginJTwpW6KwI19DfDlw-FphdOuwPl3-beq6_WbBsaxkROWcOI7sMlvyaaKkq8vldPvZopYZwoYc-uwZHV0YoFLuEzYMHfem4gznz5MwlcRn9kXJhDN8H8Y4YlBQXSaW2-a79ra6acJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=fVnvWR5NX39hpUOehW6WEAVe20KTPjWjXMFiWtDI54JnSlX1bmGiPofiU2QXAyQLV9w7qmgJOdJUHxF3Uxwjr0LVdOfyJW4qnaQqddWRRCrSk-ZB3_z059mf2r5mnseEJv8hqZDsLcHcHJH7tYWGGY9BtdFMFvKDA9k0xbEDpBPXkyb9ZwLjDWBBgdvxN3cUEaXO6wuUMoHpuCKYNQZwNE1UsHnhV-3Fy-xkhAm_bIXm3wkyYVDv-wRu7s2cgkgFr87uZPpNXcI_IoaKvyZy1UuGiSlAHPMVESrqaIwD8bblPebyJbAspVH3g0veMZguq884rJpY6EjK7fV9vX2Erw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=fVnvWR5NX39hpUOehW6WEAVe20KTPjWjXMFiWtDI54JnSlX1bmGiPofiU2QXAyQLV9w7qmgJOdJUHxF3Uxwjr0LVdOfyJW4qnaQqddWRRCrSk-ZB3_z059mf2r5mnseEJv8hqZDsLcHcHJH7tYWGGY9BtdFMFvKDA9k0xbEDpBPXkyb9ZwLjDWBBgdvxN3cUEaXO6wuUMoHpuCKYNQZwNE1UsHnhV-3Fy-xkhAm_bIXm3wkyYVDv-wRu7s2cgkgFr87uZPpNXcI_IoaKvyZy1UuGiSlAHPMVESrqaIwD8bblPebyJbAspVH3g0veMZguq884rJpY6EjK7fV9vX2Erw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceoGJv0ojutbhZ_2zF0TVaYus1enO-qRE8nJTmBQZnevPOj7WcjJPKaaMjySA-xxGvZcDfsDh5Eg3AfIKXHNyWRsa6Z5zgg4mkSP2tjH_AYnay-teksMdmuf7N2Onne3Vdv2eCCTIR0hCyyLw2kxzdWMgpIF7SUaSwyvdew3rXj8hB9w6jfgQ4ycus_kLpM3JOxJX1NOdXuL7nIEetzUV125AB37k177R3W5Gj5Q1mQhT8NMde0ltrcSkEL1re7q9e4YWcDuD2UU7aV7ZzgmRd2-V-RP7IGklSg6V-BnYh_Jp3mw3HnYQ2faLVHglWFAR-SentGgx1SXanhcU3Lkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHJx1Dediu6MdSYdI4jsHb4Ds_oupN8MCDIm6sPE46FDprDCezQvuPYpcB2FyvSj3wRAIJpqDIN0MocHQ055ica4sThtbhkX8kRRlz-5tZZXOsfq4yxvn_ptLdNWxsf3sv198Sw3ZxQJwiC2YNlrFjfyuxf1wqrqym236xRStvaqQYgSDn4IMLO80aVRcxcVtT3OMOma26CF42Nr4bzIU48CvYK5Zj0jgMdFCyvSNzWA2eaQNnfi-EX5M6TzlOhNn1umZQrTNhWxwArWRPlANMmaI3NEK1EJJfF9cRkgw8FW4hagscgjjbZLGRH-QJt3wBusA4A0k6WKH9fN9MhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTfibFsOiycFQADE1io6mAMJ82hPK5u3iQ8ia0p2x6qWuXdDyJH5eaT9pN2PgWLPFQ-ZIxjT3qMvd84Yo1Abx4Gg3o6MR38hf4fv6vjkNadXl5ZytMKWZfn1BZUEmgZgexyftzCHf7Loc54YrxBsbk3sle-FG_TmxTVbmJ9bZBhwqCbg8khkEwq2uM2rZjYCnPROIBb7MsNixObAkzu2wWKKHe9w2HNFEYRE1OtpAQKYKEKCC7pfBjfYqPXRoXwKIIBISghFQ1jo3mukbTyTs62lggBRQEE1k6HA78YsCWanzRGXHSAios6NjhD8Gi71Thk6vQbahrya46k4AWhkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kivu3qeL2aErgEqQj2f_mltsyDlrf5DvlQq3FAdorWMG_nOc8UQOa8SbMFp3g5qy6bcTEUdVKnpbGEMW0IjN0xfjY-VdgO6VTODZbfOV3uSyT-quEsprBlDEGYbaRYdr7uYwyw41h5NWWOy-9RlHGZAWQOPsdvkAT728ckL6qo5hCZCCUjCKOQUD_jTpOu7ifpIvixDdbDRVUV0lUccvYwBPj22PZDeK3eIl-cvqKlSvgSm3RG7srWeBtLnSOxIPp_s_SJFJaOAlie7VGv2--C3RyVB-O_Fu3z29bvYJFHtnuUPKM5qe5-kBX2x1eZyZIINwli2QYjJQIkr58NWNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntWT2jgziyTQ4d_66k0Stj6XP0MwzOVPMkrAmfAivp09NhiRQoBqBy9N6lc6Y9KRD8qhWvRIhpy-bSkD5ZkRZW5q1ifLfihwTTWi5OLqXWvGCyVKYU2suA4cT6NSMkVuF_DVCsaHM2zgXf8j-I30_1VK6VaxHZX6pAY23KQXc3b-kqXW-P-8ZVKVi8UQraXRw_RPuLKc4xCHFDLHw-3cadrE-4mNN54Op-cIiXzWxaZr1-N169JqmwnMPSG4p8F3tiums-fwmUXgZw4eSJsvYYw8DSqK7EYMIpe7HlEKacvgewUMMxcnZJ0dlqFByhfWwDDn3oRs2a_p4V1lM5q8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAMuFcyOace0VG3FdSseQLZyN82S8ukvkWo-SSG7nelNrjrnjIvTQPzKtJpnSIvADr4wW-X0kn5Port5rvrnJRT7oNnRSnLcZiTMC35HGlUL8xxUYy_E9aF-2sTu_zApqP-iPmw0F9vfHIXLn_kn6BOickjAc1r308C4xMhIaY9ZWfHEMUBYFqScOmiuXo46kyuRmDD1KqOmw5Do_OYJbPaL8Y_oZS0Iah5fhf4b3hlsfK3cqliRqfuV1kG-ew-R7Dvk-pfwph9fQlDecFfcqC0QXwbaWbEhuNmaeEFr1B7yemXMk198f8FQV0cx4CEMRC7_iUYV7FF6MASFmNtSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_PkDSHOW9zeRMw4ewPj7wQ4gN_sXS6VDyrI0EuwI-t8Bbe1M-iZCxlyZy6nSnC28LruWxIWVMfDdAY9EyZ_njic8CxufOh3KuG_S0ESCyne2dxQdAPCfa_xPE1Yhq-grs-szrD6myEaAInI-G_0Sy890onK6sEkMtetVGDN_6aSia3I28jQies9O2gSkMFgLq6tZAYWkvwR_qFpWriFO6WXz6w1MvrZd7WgCZr8HR5W3X3usyxQOsQIHHi8eaxUfoQ5afe_K_beKit_76HFXyheE97hS2qqkf3JddZoQxVneOm8HpGwVXvM4rEbp0TsPIWmyjrWp5CUEN9gY4I7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwux93A2rCIMYoWLeMZ25KE657UFBLVXn_euMBGwOCqQKCghS9CTNtinsbzpwNfsNUUagtiXUljvy7WvsiJhL4u2mq4cIff7Yd9kWB3rOmNJkbRsUZqne0ja92spsRSmEhI0yQLTUu-ivek_qL6wELEFY8Z9athPjJrKk45YNIGnHKiUJmyFap6MJ-BINcvBry5SIHzmSbH-jxUHrLf7HC7mAnAi_08cdMcV3Nfg3t8J0CZTsxVscbiktfOXSFMFTXL0yGuNWxm_gO5BtmHd5IDAq0y1LEcb8_PlzzLdMH2KLFYlo06pkrt2PRHN6ThThSAqVHG09_E1-QT3uCtoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDDHZhyWDLKZz_wQkY6Ysecjw6X99acgmLly1FtIqbTvcgzUS46LgfvxF99sJgWTutNtdK2ViSGVn0E2A_BQ6-sXm1hZHU1tTM9vvILWEzUyQwRpZik2YVxwbt4-MpQL8iMmwNlUUa7VhjBmD0ND-oVjzpUTfGsYGIDRkSnGQCIIpgmGF0Q2yjPxWnXJviFrgW1LGo9GNHKycVmKyBmmG9NuFf2oljFmZPQg6ZzArs32dPRGBmKnjr9FpN4edytFM8qEVpOBGvBqj0YfQLSyPItewcJhCIYgi266wazYjwU2Nb4LeaTlBpA2uR4YDlyR4ZPlNAFaHazR3kkWt2-kSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8VtO9S3v2s-Sl-Pp4yU2jNTEQ0q-BInRfyresdPVOZlRiwSAgbszzBw1kfK2sXtMuniVJF15fVaHA9WevDsdDCT20yTgv4FheTCnD6SK0sDFzoH5UgFMHcmobZlzJ-k8kGLKV1UbC63IeCGtbcLc8kmXcRzqUoaoDutfs8inS1iX4jGL28nhwleBGq2d6bGBjPWx4jv4P2niyvLjukFb8dLsaiaQyaDM1ZlpJeXenCN4wd9sAHXG3mE8ixKrz_YX40EDdyC5ggjTqQ7iQaR7vid2Rl8H0JvnzXw97ebTbuOaZN1iZIwwHba3yBH7eVP7RWFkC3jD6H7XWr6P0Ex_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLuqtT0YBC3zGkq0ITMFfC34EE4ewduJGAENVTxg-l8ZzFk-8xso97PQRGgSR85Hy_jbT2E17ODVyfDEnHQkMcTHU37-CKRuzYT7yL9-y0J5XoTau1ibUIaoxe29nzXE37BDKxoXseFIcFy_pFPqm9Xs44arWz6mUMVaTClPHSGg5ApDOI1FVG7zojpcHFYr5oBjAnK4IEQCTy3ey2U5_glzOl1vRIIa8lfI22RptdcSXqAZHNOYLhpRCvfjaLvskMXW8m1tNWfWJSFa-gwUFBSqQuot2EXULLQud6p7qREtHI412ZGJK98c2pGoJRCgnT6oURtof2IP0e-nLjI9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=vm9WQMb0a3qBSjHDnzGZqiibN4my6oabnoA1HqTClNg20qDj3jJROj_9IkA64QdJ9hS2eZi1SsKSC5_DXT82hgINqehJNgvxNjbxUOVkpN99FxFxEd5u9D5GzArAdK8KGqzS5bgMwA3puWIxWqbXLPaIzVIRDdBHpsQA08LWf9yVY1HanTVS25ndencbbZPfs6wAEo52HtsrTG-m52paUFSnsRLcRRqDdYjDdAiOYdUisCjEat-2LNfO_XKs2afcfhzrB9LSfjxhOKfam4N3aX7zqRezAIRd_t8Hts225vsvAnMyGiy3ArR5ls-TbbXc3unGq29vnEv26W_ixznkCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=vm9WQMb0a3qBSjHDnzGZqiibN4my6oabnoA1HqTClNg20qDj3jJROj_9IkA64QdJ9hS2eZi1SsKSC5_DXT82hgINqehJNgvxNjbxUOVkpN99FxFxEd5u9D5GzArAdK8KGqzS5bgMwA3puWIxWqbXLPaIzVIRDdBHpsQA08LWf9yVY1HanTVS25ndencbbZPfs6wAEo52HtsrTG-m52paUFSnsRLcRRqDdYjDdAiOYdUisCjEat-2LNfO_XKs2afcfhzrB9LSfjxhOKfam4N3aX7zqRezAIRd_t8Hts225vsvAnMyGiy3ArR5ls-TbbXc3unGq29vnEv26W_ixznkCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKDA_Akyse7UQ3bTJefHnwVO3NiEG6Ym2IBW7Z43wrqSvMbhDx6eWS8q7kGvv9vYInGBYR6e2jcnIEowdn2dK_302jsgNRmZ_faR6_LHVZMKGcOkwazfFEzOyvOgpW5fB2qussLU8sjfPAgIsZSk0zqoSA8ws9W89FVwckbKqw-7kneggueZz7urSJSjjHoVhX-UfG2DREIn7-6oeghWEd-DkeVPQmPOKUF7RuHkDl0WaSXG4pR5Mjz3iorWMIUak-nUY0cDBd8jWG469hHLYjhd9ZsSBNmM6Pg-hLqa2c4LzIBNIiXElOATUS6ksY4l0KeEP5nbXxVXV6enEX1PSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlaoRJc4M0spKsIl2TrEyOkATYPDUXG5kQOUnHk6o7dutgKaC_i69Re83sosrwI53PzhFYIzfFRsCARxM09QEf5guOKDlJfLOZ_z2A25vPYrtp5KGQNOu27LZ9XdrCJDb3jmpSUMl8OAiboBau5IjjiQQ2TR6KehTbbkEy88lOANESQPmJ-haoBzc7eGxGYL2f6x4IHzLxh9OFmkaaSs7LQRw9q8Juy5sIxhW5idKsWVO1Ae_zDCZ-1rHGzdSz0Say25hPTGaRNBYNTaM1H6M886XzJ6Pk0MXJ9YMlukkolnF7v75evDl_OpeZvOEkbDfEpq1FFuzFQsU8IR2thWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhrx6ULrq859uQw_lwup0w74FAQpvB_5kZHvqECiixcmmg33bNPwxA6OfnYriKX6GLKAa-oyF3OyW4Sjug24WrgwF2X1fuK0QgFh4Efj4hH_BSo2NSgBk7uB_PRrwGglTF3OI8wOULHQiGvyEsliYyD8FMA-mI5sLKQrVl7cOaWIHyfgctqKOhf18Vb5bOFHWZiLBbqKbBHf_nKKOPnBnbm6p0qLUlzLcP_Gfu_IaS41qE09gl6tpT9GcUoCbHQ0YTuyFxk7qBUhOjGI6kNshgqAM8VIIV-la5UCITX1Fbu0F4PeG4IresbFRJjaEYhP-WiaW6rvN3vAo5UwRQ22CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naSy5ZAy9Nz3UN2tOwVLiHEsp1QKgOu316uUayl_DPU4PGpJ1psAZ5HtLkWmuLf2HaopfU0ti6DYze0TcMGjUKWZXcPXQC9xc9k5ApFjVWCmELwlJfY0H_SifeZ_irGj78L7qZBMMp4iVfjnaiCh_s2ds5nE7me3WApNWDq_LQo6UJ5JXpcyausOzStGM0HtnNjG4lq5pIlqNH5CfYylDO7yadPtrhkv8QAHcf-AVijcENPkrIgs-ADmLUz-yXlQd3lJrl7e88WC8Itu748rdsxJf857-LhYOXuX39VLO0yG7KqUayab7um2lMGc2a-oZsg5uKPms7FbEEYhQToO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erlET-q2RGpgri2v9iKFAysrgpZZ6OU_6A-02XKj1MfzB2OQgP2BKvZDFxai43W1eIlXkKA_UwjqvxfDpOOzON8vuxirecyF917RKS248-WNhPSL1h2WssBmcl-xvwcTV0NiXzL1HKuVVOQv0ljVY-8sdwU3qztGbkDwa3etvVNit9DnE4MKoUp7Ly-bbJvC1np06SFhjY4WB6bRXENrVJhBhZOifJhbjvSzZHCcoYuT_hHXOdR-NjfrR9VyT-QIqwrzmCMHt3X1gyADmwg98tJRRGLFk_j83bry0MVtL3EnRfGHwBFk_0h47-OZs1Vqo7gqyEc_seVBJ8uVw-vPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF-lb9wVBRYDSreoe_FdqHofdmSnz7o4zpfT6Wm8mqpYS7UU3DiJSvBEopGXvBgy3eGjeyUam-MIi-Lw4ebWssrPWOVlusVDxE4hDVIcxMG2Q5DLCsmdSGDHRvgpWf2GzqfPLgFFMDmMp9M8nnEwCk3m4emlhzu1t-L74uGYdeCpzaVfvIpkeWJGK9wfAtVyxvkRJwMkl-gnPlUili8Q2IODit2N28Wkeujpn1Di8723uiK4PLf1kQSDfCQ0Hp8NcHjU1JbvMT89AiCp15mihazuNK5pmrmcPuLHbf0znJ1bpqhqCr60HGGDq8Lz146Rpp1jbud3dStVINFWZm6vEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm1smOXdYZzl7DI34bKFGU-HprXwD1eCK7uhZf_z80-_xJEuwC8qIrjozLybFgYJYBVeiv4ozJroW_J-Etk2bNCxs8h-vI0HypxNFu3QDYz7gwYpZxhzvPPBYwGr-8X74q9e5pcY1b_lIs-rZtgSyc3JqXK3anrwpwgIipoLYys2udaNi3arxKiTdTlqyLEOBvWVd-TwYo5UD-cxInUPKWd-R15KzQvnPlLmDcqj0cEtQQ20o0C_opErtARaDu6iFyGi9BQrM3QOstNTIqyY-DKSICXUikdcCluJnVxbZFEmTsR7fhz5UJyOjw9uqa7JxjDkn22NnuZPPTpFhwyuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHM_EB43dl4Kcy8zh-mTtOGYXf1YuEsihBoWgNktRFwQE4_76aSjdLn0u8DnzR5zbaDlPeUFbLeyFgqG_xmhBZw8kzuAFkf5ccVyzbYEwL9BAY9p5AA_W6Db0YKciq_lGn42fqAsIfahAPvty0ZJeUrdaT-V3M-vU5e1cCjwQ0XB8RiWY-fydPQ5EUN5ZN2_EmTvpx3HL0lL96auxliuOxiSBJE6pnD7XeZBMJ7Rg9RA7LUJl0lrCzVkugr5W6ZixBHPTlhWvoWTLPyBDOtKPtx2lPDTf1IdvyF2AyIrfhIYB1yCO6HocW25VVxokRv0WUDclgHJyJ4sEaDLimdkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJsvbXdY12m4mRe6xUgAmHiLwZyuFN62GvkqbYJRmOH07HhlvUpHCS7LHjN7u8cXJI6UK2Wh34zCtFBV9wpZtiDOU0yprUH-veDinP0613gLqZmNpxKZ6CZf-Mfnre77jnrqSYMHuVyUgFXP78dYv1m_KMZIzb73oJ-LP_NexpAIgXTDSJ1sEQqjZNqChoKtFleptEtOGngcF5hm9waw3j9LraOfi5s36GNa9EVjQ1aSXkrEU96I17KYSvI6r5zRMNjSmnI9pY4WVw8OLIqhllmlQQGkK-9p-sVjvhPrR7G-VvW8oP-2YMY52mzJ5WcQWHof5h0tLEeF7g6toFisCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=JbtlKWxixxGflDZzrO17ZmGnxTueVCw4o6hid2AI7_wVPrWQoh95ykXM-nBR3CUVF4EvM89di5wLL08YBI6hYhsockX-qdxeEiP21zfQY-ulZ5bLPfiRGCv5f1VCl2PRo4AICBMmjxH0JteoqiDP43G1GNuUmmax-LNJoild4876CnIjw9HEUUeG_hbAt_G8ci7fCtOGJucufwnEtKVCEZbPn-E7wrsHfgONJ_h18wRsfBOaLbEi1Atg3bO2JfUzGVVD-vZlpz0IXA0vaQrnCqXTFTM2aHGpWpRK8_NcryZqYqf4jVfOz5EzKxNXOA5ndkvqSUhhGdmhSxbqTdC0Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=JbtlKWxixxGflDZzrO17ZmGnxTueVCw4o6hid2AI7_wVPrWQoh95ykXM-nBR3CUVF4EvM89di5wLL08YBI6hYhsockX-qdxeEiP21zfQY-ulZ5bLPfiRGCv5f1VCl2PRo4AICBMmjxH0JteoqiDP43G1GNuUmmax-LNJoild4876CnIjw9HEUUeG_hbAt_G8ci7fCtOGJucufwnEtKVCEZbPn-E7wrsHfgONJ_h18wRsfBOaLbEi1Atg3bO2JfUzGVVD-vZlpz0IXA0vaQrnCqXTFTM2aHGpWpRK8_NcryZqYqf4jVfOz5EzKxNXOA5ndkvqSUhhGdmhSxbqTdC0Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=Wu-AGBQ2Fx2YcYK8cIKaTBYKYFUrKY9ZP7m6FpUYTztPEc1lx7kB19LZ6tdwT7GAQU_koK2XicBmFb5RqmZTP4ZH0UsXqUqqwaOve1TQBJWl0Pl_4gM5Pq0sJIcxWGzzvn0fFq8AoZHTSUVneq42IouUxKksQ-nBvaLq82nQ42e-6u3QcPeMwBpGH0zg0cjkYFpfTkp7DBGbETM-ueJhbSIloYultEl6bQS4aabHIg5ZsHqcwqDoSMEoxq8zpjYm-tQ7Q9DP3my8DcYTeNSSaa7igp7vWoUJgX7nZ6c_GOHIEIhQBc-uGOeIJXjIing7ENbJdpSlPNI7zqMhrFfHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=Wu-AGBQ2Fx2YcYK8cIKaTBYKYFUrKY9ZP7m6FpUYTztPEc1lx7kB19LZ6tdwT7GAQU_koK2XicBmFb5RqmZTP4ZH0UsXqUqqwaOve1TQBJWl0Pl_4gM5Pq0sJIcxWGzzvn0fFq8AoZHTSUVneq42IouUxKksQ-nBvaLq82nQ42e-6u3QcPeMwBpGH0zg0cjkYFpfTkp7DBGbETM-ueJhbSIloYultEl6bQS4aabHIg5ZsHqcwqDoSMEoxq8zpjYm-tQ7Q9DP3my8DcYTeNSSaa7igp7vWoUJgX7nZ6c_GOHIEIhQBc-uGOeIJXjIing7ENbJdpSlPNI7zqMhrFfHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEN736NobADJGNNvSxoCBT39QIEz-SC53OMCPT6gOiQXXOZJwr30PsTrZRNUgLuaRl5Q3BYbaG2ghi-rycZOAx-ONuVVcpwbBfQnTlf40LwqDSKKm0fwsN5bsfVqbyNMELod9jleG1Lj_6yJ319jhictuBx_cmjbYYJkt-SLF_tIY4SjZ6HNJayu5DjHL0gFLRKdB5t0C2NmcRZ934Pp1SNjWVTPa7MwdLVwY2WXLyeLv_Hspy9TrOarZrJ8dxcBpqtUNh9TOqI9bxx4xf5HvpU9FywQTbBLbE3OtF8iIrhdltfaBVJL8lS7HJKHgmm3RqxrcgGxKc4bX-2Rsf-QKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MScKo2BkcTFsjFrxhQC6RqaAW-e9qIRI6vnVSXuCL9bzCKGDzeZjDYeaspLoLwpdnxhkf1K8Z9LWNBO1WLbuJVyF0EtEWQ0J7P2oA7tvTAOXGrx5OiaA91rgS6wmRD_NiYxYjl2fZ1RcBs6A-pR7Uyy7lwQ0o1u_KSANnMdcUBVt5lMFNpD2bddRs8P-9-doXLx28opxWQl2kOLgUvF-S0E0LiaTPPqSfvVkr68Iyk82ghE6UIr_bL-Jfe7bN9hDtUHb3nRqwY3zjbPgj6rgIFLcCv3QsKDyYBt2sWfZMSlypxYuYaupYVmN3sGrF9vxrCaXgvznBwJdsIRIlnRPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqp9rPAmRXLAx4ZXNvelO0PSYMj1Zj_EHVummiHWYLbOehbqZt1gc3ns_st6xAAKeC_SAKcrQ_5pDUCpKa-X-w1fo8urtGDKUmSgRxK-_BXKH1nhhbc0geILnANkqtR94AoLEh2cKyrTAuqDFWILI01iL_87xXAy_IkOGCO4DA8YSoAsut9XMyTQQw1oNX-pEuNHOB56Oq5v_o7sln6FtF8Qursmewafsd92uRc_DAgWnk7yfMHVRAMYQfl7rb4cgA-chzVHb60CL1u3r8nXzAUwab18Q4qYHQaOg-6JvpocbnZaAh5BPVPQ6usTkjs4phjoBMIt2AX6g0sdDtfdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlEYiySdFPGftXQvR168AiFM6HAr15hB6L5zbq1-KUPJLmZhYQ9dPjbDsxqRFD8-bBHthHDy6xujB7g1JsXuEzLa13O0ilXkW3AzhuVXbz15W1TwxStUhWP2hTKSE8rIi-zh4jtf-OR4O_vXzbWfqVpzSil1upFOfrbBP8irkWZ-ELIdfyPYL0KeNXQ8kNBDQx3GZdFrk2pZupmE31yl4h7fTEiBbZEGJKyNCw97d_qrmduEmEWWU1uif95CK4bzFFD0eFatjb2i292z7vZhOwj58poqwajhr_KD7cGKuHRmd6OeXhbVplEQbGZLLpeIR7K7csq-MncfJjie9Klt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnfYw6cGiaA3FXfUXWhcCD6kYmdkDff1S2wWwgTltpHMJ8yd_07IzRcBqG7XUEtm1uXDOaIgGm7LlzpSeu_DXKf_g-RI7QTtgIUo7soOceeV3zcTIxWeJjXUghUZnjqyWwb0oMol90jP1eILSzqlT15DhkqL4_CE1HJqtC6JF4sQDV8eweGHIPlB6yBqJV1Iu6Bbsr4JD3JPQF3yY7ar-81BbYVDORvH8QE8zjYWm6Z7fhlLUmYTlhZiU6FH8RWnV9dITxncqfOa36nuKQWvTVY7eOpE5p9mzKNaltT4RTlJwp-LontB0M4VCYEwM5z9uCaZvXwVsdik5_vBHl4KoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_8wOSjVXRoE-yuYSHgQhQbeHVtRlcdWF-7w5vD8D6s3KKtvU2cjFmTxmJNZuVOYkbULcQgB0s8BPHTBng-MEmWaarwhB71Ft1TYTBMZAZ6cV6xbqX_xLn6Yyi3kJbtb8eQ4Sn3ojGpUumRGF7RZs-86a7LMOeONhlxjHQUrYIkzxpAjSI8LBUWYHfRTqKdmenqTLLLQw5qf9EC0D9bhqapRhBMDMkkpnKcely-iJew39PXAmH1IAL-LBkCJ9UmhtoEHYOaxaYuoaxMqrfTwCovP75NnwVYPgKin6gBB0a6Webp3TWOQIQlhsfXuIiuKrpzKpRZH8rUcAyklTBOAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF2kS_WWoZItse1VevC8c7g0310MLraLEqle01p4hjgZQ2428OfRb-FLo519Sxxg-I68YLrx0cl7FVabk6UHZEF3SnwvRHTjcrOaQEoSDrqnKhk_YHQhSA4k4F5mwNrU4TcUn2VyuIpbS37nQiZvIyfrHkL-DzprKNMOPHYgK12fdTto7enu8X1DP3bogcKjR5yoCOhdIaMnUPiYbEUUKyA5WbgOT7v1NFSKXZOcH4WnI8y4-Mah9DqRZQzk8o082jf0lJwHVSlgjBIMloepygl38wFQE7chADhsJoAQ3IF1vK6vW3bYCqF3XTmXxcTa8v5vGM9NIG9muVcwA4P1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBld0CvoR13qyUYVT9C8Yu-O7pzXNcjN6pktTLOKOIGgPnCbq3ZqaOmvpte35SQzvwY-O4sKSOUG8dIMh-qg3P1zkzfFQeDW03FJmngVbWAHKPYZazey435N5eH_BzlgidmyCMdMvn1S7l7-zDvmy577uF-uY7PdqTLe_dHrSyV1405-XyEWcRKk-ZiUbpe6mnqxYrgCxl4wN3-kFCzF_ytWZVsgrbuBSSpjkl65yQorCEoQS_LGtk2W9YivWXl3xfwKwcpBN6L4bRlJIqIyRiUujMdauOS62K1SPw6gPbjutGrVwLgrh_P4mg1mO3ood_Qku6qffIVKXBjViXPNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZOcZ8E8v_ihwyf0D_BlwS7gYfdlDx0SO409Mcp5Lauz2g7IZ0jwtuyKTn_3ukWYSbpkP_oFUoJvG6to3CjVi8r0yfQF6aTiKca_-a6dmHeAMHKO-5Lk9q-5lMvq6s-88bsJj31Wkrx2PYHRxmZW8wj2ZpHUGxztY9q612lpyhDxANZWRqb12F3vErZcBHb-F691qlrnNhjCNvs8_3zM7xSxSFTAzBDAcKPDWMZQmeheIof0nmSxc-cbrh94wU5YkMC6aw_miW-l2ADFQUuKfleNLeWz69xE0F2Pi7pWol4r3BNHm3hpT1wQa0CQm9wb-iVem-hOli3ESKh2yqiz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJoskpKcr2yMOIKvopjPajRlYqwiCHHXIuVm1TbBST1Mj3TLHsgfm1-BbZqKgN6xYvdAVeDEcRLsUTz4jKO6SIBSRZMXWOYjY1xcZbMhupdm2dwuPIxmBu-yNqj1AMXPmSlqKIRVWEPax3Nx6XJ1tkU59t-sdvMUNzkGDxxD_1QheOdkGLEXXcv7yvlUxx0V76Yn0GsUxR0pUSABPgzgGeT3Xq9WPUVhyIvT27ERgLZROgyt9MU9tsvbDOlnlLD6Fq3eiYglNkHmM5UHpEos3179dgiVXfR4Tzj9EYhJ0V7LP-e-tXEBYgTqReG0qAhC3Rn5zFYme4GZ_I5EtCDpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2XZGzhvmeGDJ_uc3Ws-LApA2RTeu6-8a23hv9m2W_X52_bANzMee7oqs-EcQDcRF5THVgtVeHZFlj0l0Keu_-Fz9WXLvfDlBBSDjnn6WiFpkjy9hsuI7YRpqsLwXU6Gbtp9BU21X6mZu5HjxVFpvoL3jzKC8nVi1m-OzlgSh4oCdKNVdm_x3w_9Bj16llC2cqskS_1jC027VVTYDf-GHdfOgDF6sBmgf27_MDya3W6OdETFHOHPPApxp-nrYkQX9vgn7jNzuCFXyjeBaTOJjoSBVDWhe5CgYOhy1QjFDXRfzX6kg5DlSXeT2avYWoPJ7HVsMWptSapLZtz0Y3_FvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhYMhlFF2QKk9_x440vF1frMTPBoOa24kXMzVk9hQMrR7eiuMGENLWJjZrszuvnhnrbm-1PuHzAlc64DQo16nvr_gPNFevMR2-uiCPF86miI3ycawr26MWBTTIgf5RWAZdVZnxBDLsC3Npl8i7YwwAuuynRr9oAfhIEDOnqiM0tGtD6C1EVzl4xR52cz2f8IrUMVAsdX2FRPKT8O10xb_TAUNeGydn1Tgoq-qfKffMRX2oVHt9Z79CqXPjk8pQJaBDh01l3trErfd6RJ19VUAze0KqS1rnkGmzfyhwhcrI3YbLySR68fUo0HSuWETpKGdEszQfh8owH_gyG59TUV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9f6X8KNw494Hszm--XaxQ6-SpggsUbPBPj_PzfoHudSx0t-W5iNJkaFu-Ru7_toCs6tPphh626SYVeCrimwJ9r22W4lGtKBA4GpYhanzTrxtGsxjCDurQY3Xny_4cHm_ftiEE6ifsa5ZV4OQ7IQODqZoTB4ItZyeK3LmpkqHKD2PAUViuAK2QPmBsHi19gkakEtTGJRM7gahfj_XWoEbM13fhDlH45if5ZO7L8vDxSQjQXht3EZAOZBH835FDP4j5tCuk5HkdJpfuiOtYnb4_6Qi_Hi9tB2i-_DvKBtSX4pTjel_aHGQlu1VGU9SIL6baTFdqvc0sCrBUUNVKeTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM65zBTwzsNOvg3SJFtdQlsHL6m_qKAUHSIjIKkgg_3R1BDWnJcwS_L3_g0wBAyU1s8E1lY1X7VWH54_cXT1nlTIIzphDg6OeoJ8Gy4C2BaUCCnigbgTAVR5770KTse5WPT0UL2YddVVTQ8tvigWFIxizJZlONL_kZJTFqvQKqQfOjMxbuOrOM1Z1CZzwVeb0dV0Jk9RGwcHSviry-ZetgMP9_wgq8KJfG--KHjH5vW0rujHdIwg-LOK2jSoFMV4hQQ-g0GrsW_PRxz-_0Yt5i4Yce8vL0fStY2RAZJlyaWOxeiAMyrAuy0Rs52Q3Mr09sVdYGJrn4gF5tpV0V6aNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKSsrjP1qFUUPNy-XeK5ciTScSvcgAivO87RUKK4woLHz2drwYvmadAuWO1n6Zy_pVUyUX3E_9D-6l9EkAronbp3R9fXCeLFs65XVJLipH2aXjEHuom4Dvdy0XxztBd6XGG-0Q0fFy50RkVvgxLIp8FuWzlV834S6Rnj2iwP1Q1p4qggxZOTLPl7a6ztbG8tcNBe_zU93lLBEBMqQINKcQAmaAecRoNZNc7sHjhcno743XUMCtsWhKwg058gmZm6hAk6D2Mu0jba0HR9Z_QK_lT6G1mE8JD1NP2FYycR8vZz5f15ULAtEEwsV4J8jLVgCnlOQs0Xkk1upjYVkDa6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHil86J0-FXGxjvB8BIru90uLrjEud5NMz5vD2Hs1R7TL-h-NBQCtTpbyANKmWwZbiakY8atPv_ucx-XnssyUeB5hYcOZlpih1QdHiYRG75RfqqA6EoFpCFh15Cmg6GFitZM7DYWVRLZm--bIB7YcUXHAdS6x6TI85v6ByXmuQOH1NiZSqklgPxWxVWOzAD2BdP_8pQS98zYY7FUY-P8aPRYK5KtM0321_wBq3GkGFaWBxek2JXNdvQ1yxSH2tDjmPCeozE0paKQJVm-j2BLPV6C8iiLepp_DS7oIJ4w3WSrVBFHfBgIUus4LCY5nzBEWILiXoho_gmsT6WUU4KJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOB8Puv2F30TFjc9OJ64QdKgytKqbK682ccxsTuU6geylYgaVBLRBO5kCQUu0ePwGGmmEKN5g-ySHH0_wIbQ3oKqJ7ohUJrmwqeDekfXZxPtCAfh_Gy0q9yQKrPK6eLopvt_Tve5odc285i9xgX6ynFoaDuOLgfbMYnCGHtxYe1b6nN2U3DJQDyRrLN8rMdDcgiHXN4S8jN_nzDDk6QjZT1ncZ6f0Wc_EyVtgM0B3Dok0QJkZQC4bBOEC9SZr6VhCsksJph5WvAv1wtp69o5-MyGokGlPdamBG__wKTbWp1kclCnao6xpPD-nOKJjOgPetdC1fi5bmkuebNsTvg7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSeJj0E-9qjwusXavmL9iqP_XqFZ2gDj6mrZp5JG3wU_-8-d6tJ-Hr9G7icd57FtwtZT6wR8ZwZNnHz89qX1KKlpQWRoiSYvld4oDfNUg76ta0bWdoMJtP05P5b2tt8wJSgDCa_etTLOfFnwkEpWm0KGg7r_TACu2x7qkXHJdBGlTdb-KLbndno-7Y9tIL9ePw8u9HoBelqec4LX3W_iRuNa-T_tryFU-oP5IR8hlVF2jxuXOpsHBLS7o6JbfsGYp6mw0advYUXsm30HWuK6RKQ8LrFtuAgbDHMd0m67RBmZE_-hhnEKYP1Q4as7l-EY4vzVw8U0QrCoDYqgyZ45NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFQQl8RXfhLXYv_H3hNwjwV8pQnxXGW36VpeM4mqfRLmiED28omJnvjJXpcYDMojusbJexlLt8VPnvJLWYM-cSvVoEFfcEHJD-LfftHPKShSDeounmYPtPzBnMWtUbJdm9Ix-l_LYvJqWQzgE3CjqeUTsnaCrFcZn8lsOp4h8maaWvpqPQ3L54Umf1b66aE90B-sVGgvdMhlKHkptyNgSranx03BvWriV3w-a8t6XiQDPI1Q5czqspMj7XcoHSQIoWYXSEq8XBEZmoYxLDwChYoWGd8r1ATAtwA7tXd_jBRIyRx6BCtfX6MZTpaYwF9_kDQQ-UJeQqjTGN08JE1HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqBgnrLj_ZrP6J3nDb1GUzQvaEYKwpLwNtWRmEpIVsvldzMvRvvHjzF0I83DuNy48_EQEsyCLPi0QlSRqO0daHSGizYwK1VoEvmalQ-EvQ2zRW_Lo87A2YXuISbhX9HMqAAjWzbFbDLFXrxOWQ9Co6XRDNReJAHL6yXbGdaLNP8UfLZKaJTkp1MlznIN9XlbdmZc03DMe5maWFzoouhbULhkRO-zoVewxkZZe34iU8p4k6_qM206bW_9oqdzihy3H2KNrX3XdRlQXH1pLoEnIY9fn9VmRaumzYiTZ6fmlgktrUU8_hBGnZw0TXFDdaOYJ7Y9YOJzfSAy0Ox7ehAyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRbuTLcw3wAVIqJFYyy5l0Whwmx73TxKl3TBthE9cxG350tVwEndLkXFTPl3k1ZUu_INalb5Lfn8NCtr6OwB9W92iDPOMoDMy9KFNDCv16CF3PEa494ode4sHP5jpHO7LrOp69ZTLXU-AaeYVqTrgik07ronlE8MPF7WQcsGC9A1o3xM3oobdGcCTJpLWlgTd8_fMXYmWBR4JDMF77Vwd3sUQuqGWynAtdeuINvZeDA3J9OSkxnku0wVT---A6rNFEstFOOvUxAGbYICveAqiUFih79RkCpqs05HHzVc18blLScXFty2rmsiCGI0cmLM1DX3t6BKx9NH8B3fYjP4_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwG6snMMLnTk30THEWdrom4SggR1P3m_2uLdWa6Ank8BsWYOKBRcHBeiNI6HWpfV6pLh7rcTyA5Gn4PMIlUyxYKJbvDjL_CP9fOf3mM4n7kAeimtgTz96kw4_i0LkiBsdwu-cmTwaw7vRMAu0NKWkTclfmaEqUk1oSS_JrUWJXujRqPHrBK2zQTKg_kOnQSX4Ns0tGhJc0ZyVKgEeCiHAR6StPxvWRxmkWXBZiuhOe3l0EIhjiMUpO5CIfSOnlvlySh_HnpVd3qT6Uotk_s36UjVFoFfXGy3983oNjHxhmNbBCW5X1GLIIxnHsuP2049_CXp6R1PoBQZgTIaUuyppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc87B12eJbrvNhA7itF3Rynp8sbMkTknAmDrzjRn-zXR7-f1zyYUhfAeh0UMhWkPnlK8Dd1L1Xsj8L2KOskxb6-rPB-Jn4iHdjLH8pV8WYymzEtti4ZnZAHEyW62UvWos3fV9jZnbIBNXdmfQII7TOr4JiRpHmkY4yb9jtcIN1--n1iKypC8eIxlMRO22Xlj2Srz4dEOqgnu7i-R6PzD8knYrR1tCA9h6uJTX9hJKu-YPtvKWOMPMD4tEtwAfwNZSIHOC9NYiEIBu2CeVnfyoTBH2RSX2X07Elx2QFl58yG3msXmkXj4dVsTyHIT7C0HwMjgvsTeWtQ0NLBHXSLK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsOMvkMGTkHn9aucQDMQ-KOGl_93x3NtKxX_hAWEdN6cQuIhC6QmdFoOxUnm_ssdlyeBUlKahpm3vd_3P4C4uNmCbjK8wMpPzdGse_J1cPIndzYXvKi-63p_fuwIfiDvW4d1mIuDLaFOgms6USGBYOAzcEEWGH5FsEuQzmOh6jZfnKHMPteWAOq78WNWRly6TL3RxaEQimJh-6M9QBctAbYV7fuHrCBwAXP1nOqELpr1qPcpOi0IW6mCDbKlkhV27f474MBer-VRKfClEM7CDFk3ipvTqBrmMIpC5DQO_f-dVLSWse0ibyfpY8WNB8yZruRdI_GYehBBhoCgKcvDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTFbQnKGKf4wkR1QeOg62-kJNr1s76XKWVfsj-Ne_pkQWrKuK-BwW_62JUA3TQyl_GYB2k7r3WnY60QeigM5Bejv2b8nw2iNr8yDYyKesHM8c3IlpHCTv6OVm9xMk9fncVwwsWGxDKgP7w3nAA_b2KKkZ7bLFnVctQfbBA3p0pHUmsRMdt4MMkf6GfwrhOZvJED2Yg3Yqq6TauzlIIF2ZECMRe6WYbeOsQSTLHvEWhiP7BVbNKocka7KvJRaedOpqLeKIloiuIa-00h3bJGVDEC0TbiyhGJo_KrrG5HEY-cMpHXnEyEJ078LFXTMfuwwHyOIkaB9Ins-cEROPDfmew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLwI7Msm35zA0p4idAeKj_2z0WKaD9glsfthsnjuMQ-wRFgJxSmB6DnWrJdUInn3V9SQC7bc41PYlNLsAP7ekn4CksksS9IskUmSn2uWGZ_u9WMbhL2m1wl57UJJvWEStkarrvpvNwdOQrIprwR9y6nWyHFwQFGfe_EqEilrOYXH97bQ1CmXtvSVyaxl_zE4N5ADgWSw0Q7nOG6daFyiqHkMy7zmyaXeb1pkW1LWWUSKEpielG6ZTQ4_bSVh8Mqf6hhtm_JZ0vqmJUNHZLlA930NAsdMhiibvIYpLawS9Gbf-eAPPgGl1jiwrzjAeSe8M0IhSAtNUjFH2-nE9WXE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tuemti--fVFQBJiFlhYJ5jl9A43GW1qQFnTIF_BuLx5qelbtWh19ZLCnNeo2spufE1jHSP1N6OfD8DUZ3p4kH_GWngxpTvyWWOanFXVsLQ3r67FDHdL-181w5IIy9Dlx4qLxRC59Cxii9jINtIViqdpcvrMkt3DyWJhqyQ0qJ53XCizcLeAiIYn5tswMXVV4Hxm2E6KywPRsVRCAIlhgRYka33acnH_5bgfqoJmDHFhz-5yj69V7CkO717Jn4RPGe2UleRubqiqNkFh8mr7t6SdcSW84IQDwgFk090Gbucd6Nhz_wPT4bCdBitGcKis0HRh-KHJ1g6nU57G2OAO5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMujnVdtQLfUBNzYD5u9-a_TcCCh3v2VezyF9mBSHuBVWgKZ4LF7kAaFVktrUVziypr732v6IpaQ7p2HowHyJlJBz2BwDYl8WcckF50tFWhZ2-VYLffn-zOOS-_H4AauBz9W9AdTrbqogSGRgSKVB_m3-VBbZQ2HPiSDD7UjrAp_DFyWYgCk8xvArPEnG6s2nFUPUl4oyZTHOBuTY4D7yWE5UCXw7WBR6KXKdwuCkXhWdmT6ctdizfs4RGBsf-NDAczlj_ucL_o3AQ2E3PS19SvaSkhD0XtDTQiFKjrlWzZ2BiiqGN0VIH4vCxSVmKjGk4sLifi7Exaa6pMcYNz4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jN8TFgXpFjuGADPmmdTrnXFYRZAdvcvDfa7hRzeUnUsdMrqasOGPGrgCNslYT-SP3UVzKVtV5rpLdutOvL_4DiZ69R4XwAlXXbdScJxHbB4-LVagRDA2JgelSjyiYIyAESBAmeaXcx5Q1qI4Nn9rvGr15rjYOqfvp6qeef4TdG4o3aLDJ1P4zPu2VIEcrHOBx_GTJA6NDyqmUWMajho5K849fGZnferfmQ5IWah5IUXfbUEXdYqRh52LIq8jzYi05Rz4A3arkD-Nlwh3FQmvX4zeIxSFQSIK170lT4YZMMjTxUuH7trc0sZwAfS9864Wh3wE0qPlCkOyL9_fCsXQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jN8TFgXpFjuGADPmmdTrnXFYRZAdvcvDfa7hRzeUnUsdMrqasOGPGrgCNslYT-SP3UVzKVtV5rpLdutOvL_4DiZ69R4XwAlXXbdScJxHbB4-LVagRDA2JgelSjyiYIyAESBAmeaXcx5Q1qI4Nn9rvGr15rjYOqfvp6qeef4TdG4o3aLDJ1P4zPu2VIEcrHOBx_GTJA6NDyqmUWMajho5K849fGZnferfmQ5IWah5IUXfbUEXdYqRh52LIq8jzYi05Rz4A3arkD-Nlwh3FQmvX4zeIxSFQSIK170lT4YZMMjTxUuH7trc0sZwAfS9864Wh3wE0qPlCkOyL9_fCsXQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exMUAOsCahtUcQb1oCfEKgzzHIUN0h1U3DfjfbB3i37qCwkS5N_oodityY5GVB3sF6GMXX7d0pC-mJxkd4ov5xsqbof4UI4Ktmv1ahqAalJJZK9R1jB3UZhkY9M_yBJoCgg_pGu8wfVA4t9FG8BgjOa6YR4ChehMtHJCQooZDpdugNLODlVBYs2-s6VAgJW1xF5Zo0rMxQonbtk19RI4U0ZT_dV9_TLhu2I11FiZWJtw8OOQBDo4vVWBCgWSiBIl0jJwd36Q9qgNyk7aMqHPpDCkD8ti0NuVSgKCsLhxWVEc3Cn7vdpr-pR1WbasfsgvAu3CXQGv585Np4ARZK2KCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUYSzaItRVfT4H-Ui086HI5RtWuthtUoyuXiAw8b_ZVii_tqFSk1x-ohbjmm9CVjatPOlb9Ot9cmDFetuiL_5NHJn5X8qzb6qY5iEkra4buNA0_mi8j5gHO75EG-38mkzCsnv-gC3jS01DDGnzNvoumEJUTyWOdX8KgOGleOg227a0u_YD7RCTMXgjPqhqbSa_oJBdUlIf-kgT87lgDdUuagZYkejF6okbZzzDZGCRcbXcdzk04F1IAIVHUdYI-4Ok5yOXWeTaErj62CM13qyqZ2O2DdFhUPujFg0ZjBTrTRyYAk3EZviSSJQcKFKMeFeat3NgdSP_DwC6cVkYlVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjNySQYGnjE5hn2Esv9w4eCtFAgVW42u9o0B6DqkMx2PmqX9Z_dk8Q3uEt-VEOndh7G5QaeOV7K1cE4rR5jmWapUh1kUrv7He1Tfw4HqQx1wj-2DysDsSHb5S-ueD_FlYPI0dlFFs0hel8QQSc7D_Q6Y1Ys9cypM0SrpBqvDBFD7NriS9n4oDirxi9bGsVQryNUFjFJqqCVl3ONRKJCj2bHsC0zm0FBOPGfskb2ghlHdSfAJR5h7xjK-9kdLrpU97W_GGBeIyd1rAd2bFH067AnAzRU3aY6REK2YkJtia9Kvot5vf-zLlpjeceH2YyO9nlgoDblMysZeB7fKOxrnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utiZD-BR2x0SejGe49OBXx_uUwfPAQaU7aQqMm_6e2CsMxAima4kmzYD6K646S8vd4l25SntME6q2n_8RCteFZmCh82WmS0qmjpl8gEbJD2yunyssIKmRCWG4HrRIlpDWOdPP9ygGzhfBeuPpNuMKS0ZEWsy_DOqYqCApH6BD1IXKcprnENjc0F9Cd5LrfXT3t_tpOgw-u-ngwL0ajeFN53w0-dPFc4Q1l8UCgcSL0mq6cYIEaeQY7LAuweP2rRIt8Y4lp0eX-vjQYogtEL0wEGmo-cpq6iFbxEtY7g5Le971nJ8AiltRzxBV3ofqWjg6q60KG0vbD7igtPaYyCxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl_2ZNqkbvwOMUbCCcVBqEC_M3hsQv6Ew4mWl4GItK7fF54TfADeGP_efNAO7zaRhWfgy-x6gEcQ2_ooBagZT1gMCHy6reuvpi6WVgJmZOclY-i-nVBFDb3DU5wsqM4ZR2PinsQFxk9ud8e6aZR_K92nt9Bvh1NmxEluoWNgevLP0_rlmdNYRchfYrii6yKFD956cJA9aMPvThli3LRT38zvQfHfIlRU0pO_klSbtNqv6PHYpX4ioAsFHFBtwFKU0EJX3N_fnnIgqXxDJIjatCVw3KsIgUMtZzIY5LzNIP-purcSg79Y3hLYMBlp29a9WrrGmLSnBjwnSl1saQcgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-SCZvVd8EIt36r_TbNZHndlv1c_eDHBFOViAoDcUxXGiuwZK0vWpLR4e9YyMyZBxlMGeMIbxPFWBIzq3YiLO8hpf1P3muAYCehwHntLAzn6VEz4yac1X12Cd6l8Li_UkUQkJlp5KJn-FAQE54Fh8kF_yuG1_ahWa3JBIKspqtnWoYsDUl-yB5m7_DmpzH1Zli6ABOx1o-vlpIxSRb32DQ7UKtLz0UROZpgR915in9VZTFM3DNMRhJrU4nSIRJscQq3kb7daDVpNV1GBSEl0iMY37zmlefLsYaxaX40RfvfKnbv8t-psu986NAiX3OX-ZZOFgoxeg612WbI131EiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFBJN5Ly-rtyUJzO9Llef-ES4PYcPA-GX_rNfqBwjrYlomgPBCJS7IRu20Kr0vG6PaFVN4lXgNwryFLBn27R7c78FXpgw4KB5GK6Z9JOCXlUZdCFZOUHABGfnKdWMvCYr3CdBQMW9Qex1xO4g6g8ublkU-kyLdAKYfZnW97Lx0_MuxYCm9ndi9yvQ1Kdmgz6MGOixwWH9Coh2qwR19S_w9SaxmokuUZHREvvVSC5frmRcoI0OatwtabaPYNlYLN0OGBRzxtVPdnWx78d-zVOryqMoTHZvH8H5-CH6yp9I96qh3PD8TvpjRutBJrse4CBlwgicqNjSk3-J5mrPldQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIVEU7C7IfIFU_n8WwdtnoFEl83gSYu3O5ojhjnlOIorKhE5nN0wnKIcYTstjlq3n6qTvJA6nW5Lmv2zR0J6XnzDGv5vLBJNC9QyYpeCu7JcUOGW_ZMRbEqxssePX6pVBSJ6pTjG081ZYFQws9ZNi7CzkTAzKtjiWDsiZA4sBAG6ce2A9tp31fMie6nCXI5UG6YgQ6j3GfZynf6g85IVZSM8SDSStplXL8vuYLr8Rl1clnNE3YySvwh7FzKvsjH1E54nB00_FT9iTn_gqvKRtxoSJdaS4au_viflFGZ4d0eE96w6Ho0mNng8saSRuld3p04MPrZNfKbSyi1vOE7L_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=pI8DlDzvXLnaa_QGgS6M95UWMv0Vlxv3RQcQNwQUVMYeKjvo1yzzsbUIoir94pMOuHdtYfdtCuDh1XcOED2nDIn-tzPX41Ffjuv6DRPk_pN7Jd29XcUebgsEd04oXNga9Tq5k6WFDqhVBeXYETO2uoOEcOxwkUUq1xN7LOINcurIEokHhpNFWeRbXQ-Obpg7b_Kx1qphtfcEfjtY-NiZQ05ULuZnu_yIzL_nuETxPXbVoA16FQWU-V12SLrkum8tU9xw3JrUpta2oMgYKH0AFf23Y5tdoqk5t2bdouCW_Higf_nF56YNV3cdTUr_OHMSuj_QVZmH4RgkrO2Ti0_SRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=pI8DlDzvXLnaa_QGgS6M95UWMv0Vlxv3RQcQNwQUVMYeKjvo1yzzsbUIoir94pMOuHdtYfdtCuDh1XcOED2nDIn-tzPX41Ffjuv6DRPk_pN7Jd29XcUebgsEd04oXNga9Tq5k6WFDqhVBeXYETO2uoOEcOxwkUUq1xN7LOINcurIEokHhpNFWeRbXQ-Obpg7b_Kx1qphtfcEfjtY-NiZQ05ULuZnu_yIzL_nuETxPXbVoA16FQWU-V12SLrkum8tU9xw3JrUpta2oMgYKH0AFf23Y5tdoqk5t2bdouCW_Higf_nF56YNV3cdTUr_OHMSuj_QVZmH4RgkrO2Ti0_SRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LisWBV1uooqx9W6EekY8VtEu0tSFzCGNpHJ0gjs4OY_DglOgEp9-woJ3OYrE6rwFrBxGpiADCCFRktS8H-sdSdYew2G1_BSOHrN7pzEDWgPHG2cHeH5btRtkwCmN-f6gwjjPKDjUFPBYAWNoNsnEXvnGAAfTWamzIkxUe00n40EFBBYkeHrXaM4opFNxnpwhubjsH9n_B6hUXq-D0815i4Al9KQEs5_fNKxs7j4JUGBe0M6yhUqwRAZQlDS5j11ho6BUPMZloN-YrjWLsXZRDwIeZ7N4LXl5WNB0HIL_M5RYVbgdoBLegGxMHlhqrVLhjcQC3EGOZWTSdzHGGFaj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czsTLBRa6i3bOfhRcr7hMar_WKJSZRpPPU2uHMD24J-_Dh56FyD4stU6YnjT8ZcelEHv3p5nLwZmhEbFDk-Ubfbp2UUQxI8oF5zZFrrMbI9kbV65cgigSsndHA0fozF_qK7xyjgToXIZzwxzwW5pP6Rwh28lIrxZME2zZ4UTffdYATLmu-Uo2y6SM7ie1DDPB2fD4JhHv8_vePvVuzqD-BrXd311rz2nsNIvNxHrdUFdnQfLvutOrLyQfKYBhIzQMqIk7S7P4-DW2s5G2GPxSEx2-uaQMEZ9v7EyV4z5QrXtyXBt7rZDduu467kk2QAR5COUrWNRmSBEEEbbT3mzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=btWMHcW22ByurTYyeYDH56hrUcPuElLsbRh53h73vL_PbjFTyVy9Ocu4_UDfGgkbP7zbNW-O0nWPjZqnFv_DLaeVHfAoL1Th6EQ4hksPztZ9gAc7h4Ttp9MvHkseW_d9DVswULTzvtDu-mjq-M0BY-FQotITCO9WdXwBpGq0IUQ4CaZfB-hwK8X6VIxrR8jvG8CT4SfHCgSYK8ezYA_q053l4Qvhr9CNtCD9y5CeYFp_wDwoZRf6GQGDKbt42xcb6ZxCXk3VIqus-eAdKb_-GQ0XXoH2mcEl5bQ6eZfg9j3NQ-tnL5trmkKTkfv09ykxZ-j_gj3gLq5mQnW9jMW4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=btWMHcW22ByurTYyeYDH56hrUcPuElLsbRh53h73vL_PbjFTyVy9Ocu4_UDfGgkbP7zbNW-O0nWPjZqnFv_DLaeVHfAoL1Th6EQ4hksPztZ9gAc7h4Ttp9MvHkseW_d9DVswULTzvtDu-mjq-M0BY-FQotITCO9WdXwBpGq0IUQ4CaZfB-hwK8X6VIxrR8jvG8CT4SfHCgSYK8ezYA_q053l4Qvhr9CNtCD9y5CeYFp_wDwoZRf6GQGDKbt42xcb6ZxCXk3VIqus-eAdKb_-GQ0XXoH2mcEl5bQ6eZfg9j3NQ-tnL5trmkKTkfv09ykxZ-j_gj3gLq5mQnW9jMW4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9h-0ac9nT_sLvfRi4iHPk7hs_GKbq8qMdskg57mN4HvaN9d90yTU7UL_zfYURgwRzkYZiKcGV1nxVbrK4Wumkcj2N5G5cVfFTQ7GM65h7rti4fPLKA6WMTqZlUfTjQ8vM6kdoKtCjeeE0Nlju5sn0uhvqc62B1yJRrlpl9acfXObqxKDQrqTOQ7LWi9aUvgjX1h5aOYfwoczbTCHLyyRw2ziVD6faUTM2a3_9npJFb0JnN5t_irti7l2IUqg2iRkNThnixmqf0cXzIomKO24XSNymw7tDsG04XP8vZfc_EOjtpmWq7UGYfQbquMkwSmMRvk3CUxwAXEDXOyKjs2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aAHDVXW6gEBGYd-HG-xCakvv04M3ToZ90gpEWp7QJ-lSTSzOvLsak1SqBYmd7uYC03IJCyFBMR81Bi3pnJQ0uiCJQvmAIgSsENtGpLgoJR9_oksGzqOlnlJLdI2hzCKdnSP69r6SfNMhERFngnk326eUsQ2UBo_bq7L4cnYbKVL8r3Tn__R8Bo6lKvJfl7cFoveZ6UCRHI8J8VThVHoENl8hPu1O-jxOaxN1BuKjCauM26-J5ro7hTXUvv5g-NUjeLUmGBli4We7XWn9to4iX-mu2ctoR9mx3Pc9LtYP-YYSMj4tI77_LViCoUNZbVaFmECTu8kNJlWGg92RMONXMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-BOuXLF4rK-xBdJ1xotZAsfyP1hc27oEhN1smViT3JWcHqqhvdkpboyqLek32SnjRUOLaoVPJnWbNWdLxoXiB-hYjxIw9WLRgWaj_sU_bk9UUUZWEf_8jjcJFxRjMySowYOK6C9Hr25oeo1cMxj6vZsf8kym-NDTEVJzGNCf7vcEJpl11Oyh5aW1hzElaJ4IJoKVCe0UOTUaT8NIgj8pIpyAg6PLGr8bAAya-OWfYZhKsf5OMODLk8jbV8FVa1B5Uf5H1izZ2N3jfwY7gkr1IHiou5dREhQnUhjPg_aeS4S8fkE3hMvjqxaermFHsEc0yqYZYJQWgFpHQVhu_o3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxZyD0mn5ULkSCsay-LojuXee8mVtOC6A0PhRM02AWJUq-wFNc4LJhJ4JBuXkyTIqV3khzhrv8-lQs795rWszRDwme31WiulDU10xyAKW8Onmr2osXyRS4mif5ZgVnUrAc0fAl_b3gy_pvBIqEmaJvtpB3HXLS0rppFw1lbgGAjuxGIalAlHMITFMi-mHcR2go8fucMlyvVBzYUWX2xE1zYtOFtmq6Q9HML10S29uo1EUnXdQoLa8Y1NJQFMydgi6TCX1IOO3J8-lsWTBHawcD89XNEHe_59g1sGpL2Kg2CPtclWveAMwyJYYGCmF_HHQ3nmUHPtSRpHq2L_t9_hHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kC40HRYm_EC5QsdQBjJoD19pA0ByW3w59ZyKBv1Wxt5iXxjbw_rg9aHt8UenW28gPPatMF_wa3Chzq0TIYbIMw5r-VnL0DiIm6zEsqSnj6AWJLVfLQmWrC-dOkFyr1wKqV9fCWJsVbYuSpWx9cRETpeC-z18Su2AbLN8KB-SrTiEVsskVy8PixwyihYueaoZRLTo8877Ix3nn4Yzk8eDbCf8RcElVwpUTfK5DH6BukImf5DqJ5nc4qrmq15GcFjiyb38eco56RdLmDVl51UnAZo7BspMvkYYPv3MnuDsV_VbhYz_hJQCHL_Rjan0JUwctG3afBuw2Y5riAu1oxXXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrEmeL6MWeqlgmfstjsx3J4y-9APX1By51LdF0FsTPCkZaV2OlnlfgYvk1M1al2yj07uGW3X3q4VSlv52CNmxVdLRmTMwMBPKz3EH_crCeo5PamJeynyPwbdqUtubnkhwGuDqzkurCyAhgPlNuP5mLx-H9fJOAjL1ki6qTsev6f6Y_ONIoTuzxh1De4M0c49S554_gzzD1KrHpfKwT3Gkfo7TGiwzGfYuJJmr0IDn8HLKgYeLzhfLaPc4_bLwLCLPBCHuZyxRSDzMBqY3Ps4FNakYrRbBkmeiUw1ubHqpgiphsbkWUuwbYOKgRKCZSynZW1ZZAnyh75MDdz8PKnYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmdD2aKDb-NwbnwAPnP3-cHFMBEQ7iMrTD88p3EhRC7BNjAL_D4jiqszUQmA0KAmVmnjsWblEDiwFW2VAUnuDCxbySsbFw3GwPb8tozCwpp77wfvyT0yXCIWeQWsKgeph3yzuVXHtAxODEX0lUYq5asjxeRrdYukAL-tenC8XOhWcADi3jRJKqSWSb9iDR4-9jSo6plrx51X6CzdG-6eIP3gcZFKeWpwpBXcs_0WziXStVKlYt6ZD8ikFrfduYHP37lBUO8-1DR0q_M32D2vv_iBAO-ETZayzmZqyFGt1mT9quhEvJBbvXNk1WKtqik3ihhpZ5vPkchmb6O5-yFgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANqVUtVWeE-XQdXpYnooYwgnXVq18_cjClPOVY2GuiU8tXszBL6rYWE0jMToqb3EfxA-Xb6ZzifmsVsm7Z_H51hq1-L_dWS4bpPe_GLh8ejUzNkNAY_C9qFqDR4P7zReo9O7pVPjwF_4N5opOx_DsqCCOF4XpaozGohqrqmSQot-OLlGHYcLS4At34322Lmx7f0kJYI0tk4sb88HO0VT5qJWtT5CwjOh6dZiORFLo6E1r5yC9VplULjmLAM90VqA0l5m4cQfjFcVajyYiZV3B35kn2MY9a3fyNAFAh2IrfSXc0P_zZS9XpwAyeaM8dzR3K862rwpCR59nWDbwWz5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgTmZFOPBIW44RGxHw5NYrxJXeqrdRzT2CYuPJ9swWxMBMLzuZn0o7WMs94ILEUodR3DwuxFjtdArIMqLJWiyUVa3OBpkO4qG6r80tPlckSdi6kHfXNvNFUz8L46OkmPqu-Pq7X_AkWFbgtDaVQpy5QUgLRzXfGdw5eo89uJ7XEO43_hrxSbukRiiFppPKD6HUBW2mi8WeJA2ogk3WSnybrfF_EOuJZlzGoTr2AwZ5G-TSaluD749hkDyr_RcZcHzACcpWXDPWfH7nPrXWPeVxj1TX0iRlQaTEx0IKh4s_3P-zJERtiNYebSWCu15ww07W_cqmidWSgI9vEpDVY-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-9kcJnprmuf45Qr20Hwvuq_wgp7F-9-zQcq4ol3oqfGmPb_yfQ-_LTn0sBUpOrFaiULKrg7bJC0YWsc9xl-70Kk_T937ML2qfTgAM4omCnrdNGI_qDFr46OrwF5RpYjYzMarN4Er5XxoSpWzQ8NwRqUx4wJmwPwtKkySguzRJSM-fJe7-tld0e9wSXbxIScIqzow6lHjnW7NAYR_YQ6pLLyCkF5EXocgLawDMa1xpBT5EbcTfaXmSC-YsTEV6M0zMEFBa4UfTnsH_j0Bi8hgg25SipzG_i49YhMbCN8iObcghm6EGUXzEceFbchOaWZyw9_EdKSbppft_jCLGmtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnXXnq3cEBRtVs7MJJb1A3GecbB6fQ4ApkDJsQPji7VYSgZ3x7ruHPWsWkFRp8dCO9TBwlnFs6fPHSuy7FwSLZyE7p6JQZtZqsmy4Hv6N9ZIZ9zvgAnVjMdKQBvhDdenfT7LvDqE1nxdF0h0JE175kmT6LkULrGathUwdKQIsGt22k7LoFIhUghAlXGZWyBzjT3u8d5KbhU4j2xS0WJX-xs0aMTUnKdXWBxfGh8sN88RFTQtulSdFyIP9yVz04qq98fl5iHQrE4a76Kw1SqJttTXoHfG4ADKzbzl647IS_8QhTh9AA7TvAYhGNacGZr0HEM567bjzyJV6ZA6n-AV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvzliIUW33FtrBtWOn6yq8Yom5zFRRa1F68HcLfH3TugOLKLsiIF0eRweE5YIYmxVVJO54Yhrwx5Vox6yFim_XjdlJWpFCfJQyw26atgmGVq5mgs5gsSOHbn3u7YCMEBCiRQpXFuD9jJ-GOa6MWdueyqdulgyklHiUlxXQFesL_R6cqfYkKfgqz4j1YcqxXXaJ4G_8d872TxzBbVdrou1_UoAP2SOviaAeqgamevFsG-8XRWphW9HQWPuEaYL5lsoxn-fi_-H1uVdDHoPGDf1qgxU2CggirrsqaFpfAh8uv84AmgHByPhV3cR6fJgX4Q46CX0sYXiqWkBmBXN1eiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lntJX3wMKI8w5NB8h6bmdJjpDo30oJufAMT0O8utKs-9O3ZQXnB7IV6cPRPBRBxtQdHkXuNxZk-eOFhmsmmI4SrOCFQa22qEzUA1KvOTX3zRTm1AQ5vlMUoK8Z7gFmqqcRcwiiWLh_YyaqEvToOjqvh7ZPgeZPehtoalgkvDohm6doskHOO6C2b-UKU511fRIcxAYP5uNa67RwcPGbuhAosvbwmtJmabraiJt84B0PZjXXtEriLRnLn-wTvNky7ZdML_UDekmMwYiB4mXMoMYdVN-0FcvVrwgwyoq6fy4Vg1GUibW4lzYPx6-niTmpc6rvzOFmEhDqyofcFa0hLzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB3Gah5BiAfrwsYVesUUCXAlNKB44b9vzpNL7u2zGum55ux2jIzwQmI_4dTgtSLnoH4eeDrCSu91oR1mwzZAzYpCLNk6500szxVd0SWjUW5PDoPqYXrMi-ir4oFG6QdpJeifcQRcp0Oh2LgqhyBD73yua6S8A1sHcNUcgFDjFJ8bnGsKDYUVXMPp19qSKXDzCheY0t5_q0EnrnQ0G1HqlGAMGNsj4NaV6KIJXaj8rTzMqVcti7bZR-bntlg655QGNzGAOapeXUyyJwa9Squg69byU_GdRan9oYVbRXGNZ4SMVU06DQ-3Q9ZS5pvoCEA3qUvOwWeydbki2C_y4B_49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=NzD6b3GYoKGDU-_0fFIs6babVAJmtkiVahluNym4j2y8rv3uvlT-t7aZOg_5sdu3dmn3kUf9ZtKfc6v9tpPZCWQwE7-ElaC8FvqcEUCMONd3dNr9iA93iiUdysbpUl0m2sDjRy1UlPU-DMCgHAzk2C1R2Ymb49nR-kqwdKxizJEXKKI1CKSNnsh2uIIr5CL_ybZFw1KDqdRqoo7WtyltI1X-sszOSsCPDcUpHCQIyMte6Gulw1VSSe3YemFATX3fK9_cBP6a0CRVl9RQ23L2XrOPO5uQdHx-kTl-DlzzjTw8wcIJEuy2Y7WbSFJH7OrUJV5RdnZXPM3OsiYBdTguUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=NzD6b3GYoKGDU-_0fFIs6babVAJmtkiVahluNym4j2y8rv3uvlT-t7aZOg_5sdu3dmn3kUf9ZtKfc6v9tpPZCWQwE7-ElaC8FvqcEUCMONd3dNr9iA93iiUdysbpUl0m2sDjRy1UlPU-DMCgHAzk2C1R2Ymb49nR-kqwdKxizJEXKKI1CKSNnsh2uIIr5CL_ybZFw1KDqdRqoo7WtyltI1X-sszOSsCPDcUpHCQIyMte6Gulw1VSSe3YemFATX3fK9_cBP6a0CRVl9RQ23L2XrOPO5uQdHx-kTl-DlzzjTw8wcIJEuy2Y7WbSFJH7OrUJV5RdnZXPM3OsiYBdTguUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWBBm8rPpiNO9LF3EufVSFDw9XXenSW63dT1DYLLdR8jQ33j5zSEHYaHl7nthrYX_vks9k0sxaupxRqwB7QSp4g1-nngFh1_2xoVn264B3C5Hvn50AACTSx7GABC576dE0FRGIdEcnpd9egITFW3oj_SSfDQFPnH1b_rKxSAULQTDBg7lnDtDBC3_9NfgWyNyNkRaRqDemXmU8gdW1ml0Jma5BaUcP-viTCvCL1kAnO7axBFc4TOAhBrXWkC1gtY6xbDKbxRCj0FQzuaVw00NrjzO8eLM34d-GU1VHv_mlCPUC9B9CvlD-ZiWiSMXEC3CYgx5h9sf2iFn-A4jTCcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF_c8l0zyf90gaCtwr75-hq5xAb33NZkBFdaSF1sIcRp4ZVhmAG3r1gERxsjVKA-aOJkoxjwUpJcPg0DH-hj5bv-1rP3DBIl9kTdIskcC61knc44_VQe5_w-tu99Stmih-N2p0WFP_SWT4RbccaDxWsDOqRMDLTVxQdJ8zm418X4loEopD44uhHlCgI4A61XWe2J5E6rTN0yxD8IYxLJZV4Rjz7K5xdtK6vB7T5Q6IkJ_fuDk12ufAtgzzMK9SzsU1e6oI_yPFZYc-4-GzZpE5SFYsMkhhmWmTShj0xcI8ZfHKj9OixYv2YEBCBQWjZ5KvBfEs08kQ2rOuSPfPkZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
