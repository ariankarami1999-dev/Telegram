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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 315K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuEvkyq826BJjrbpUtG_FDdx6p0-mvU_3Tg_CVwGdee6bvUbJk_Gkn_Nh95k4EPSkByrq2hGON8ev2FXQA19SZwxfK8lYJY1v-o0qlRkB-qlBDSKhnTucC2ZLZ8sg3RcfoXLc0fzhPH2wFVI5-F8KrONVkjfXoMnM1uR0h0i2Yn9d1IjtZT4IxuvOQoaSd5orp4aEY8w1h-pHLxCX6QVkZyYRKTMOn9nTwa_71nY3inNU-lolJbUemTPUaH9klA_xsMywKH4KWJhglJ1S_UUX3GjDn9eGz2f4Vr50_KxTmraUfH0CNZS1Rsj4wmxE0Gzgpfe5o_nhwdegAONLHskoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roo-JRyO0F8lCahydBzk5JFeKXcOW6jex-I52oivVRZd3TtzUEJp3Tw23vRtKJYiAKRdPZ0dyiFqmANihFt3kBAWflOfVGA1d69uB_ewe_HUtu4zlfUCgg1kc9dn5V9WqTVodBBfVHiWhWVDmEFM5OP8Sqx_GVqS2YRtLqXELhfQEQmpUggQCWZWUatA8zdMhFQtRmjepYDek6IWICiQ5uWQlNpwQSPvjIbj5E0ayp1NwY1R8Mc8soJvzgvjsMCwZKjcCSvyeYHNOVyKugXK2EvwRvIyUOl8gIRnV5egYEmBN3Hg97bwiPHGNxMdUr-c7Vl_IISUrqQ5nNP_zTjweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV97mUvuBGNDuhqrHCVFx3Q9USCv78RywBJvJGTxqfEaOUaSwIQigj6euHDe_kf5h3NgnM5qXeg3MJw1QGcZjxRQGD3VTqU-cgUd5EC1CGHCl2IqKJHf56RZUa4VxylJuCV5XcVqjO9BrNTyXQ-VAQ6DntGE37Uc9l09B1VTeITsFAZHHmeU0sg_oefj70WH0rjhZU0dWV1JnC2Lb3x6prgjLj81Xb9piBNUaBZY5EzVtofgKZ8OMzuO9etof0ZVsB02MFDDZy-YGjY-muQQPXyCJc3N7OPN-lHd1BEpD-5qzILS8vtq0Snm0fqtXOoXpWfPHqFPyuSOQsi3QWMtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab_dq4oCteske_wVVqmcV64T9zMxK485luf7aptUznfunATrz8Ig92on5lkywbiZLogtgU7wuqGOgDqafNOL3ba32sE3ExT-3iIgYGiZq1mTNuAjOrFX_d_4-Elt0gM8uDLOOWTlY99bLnTg4Wfy6oJDulFdye-qr9sxxjUWMIfCpagPVwkZXfkhi1q97fbz10hvMWUTGgqU26hnrfy88tEHKZT01v-yXXNg7EnHnJPDjHvC3wpAdy5N3IIzhFWu9m2mBcnk7bnoEG84xlqq0sU2foadWVUm4pFvwEDUrA9Ol5aQ6U7756c_kV1KbQgjSGKWvC01K5Sso4mtm8CiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZW4EIAPGtMBAJdk60RAjxDsm5Knc57yhWEhh10EvH6BgVhKNpW7CZGk2KUFP4gRjafWdf3f2E0ODcKH10VM6Gk_EQ6y0hO5cdP49FCCt9ESzLOe8WW1t_opWSSRsPxIRekG-fNQjtHct84CjDsnkTWMyvtNutV9cnxXm7taLSRcpYscjzglRI026bRPdI0IhVdSJy6eTMUQ41uFmZ36bgPj9VOfnEAmcnwbxzO54QEzFdNojSNba3Pxwq_s6sOS0cqRYv8i40mgBzBLWOkXL4NQgE2wfoSh0bFmxVIZG94_6KTG7j2JNUh8XqOSu9F1LuDysURw7ilu3VEZOLdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDws9Ln96Sj8HbuXvbEQQDKx1rHLtYVcgR_DkyoajcSiqTD7ZG4TD9jQKaTCt1zvIiM9EluBYUP20PIjWtvGlVQnwV1AmQhAtrQpuYqIyjiQ8bsnxfzwIk1L7VpjnmpyjhuQebL4W_qqodsj1WcB0kJIkhJlW3YyMnnttvnwlwUDXd_KSmY5UVN5BYC5kP8uHcnCce_G4LNkCfkK2LyU42_LSfNlDlJlY97Sn7ZkL_R5N4rk1XCMLyw6rDuK4FVUWPzYUOKzVFU0kkXoCup4fQSbBOxNnHI8IVzGnkYn6t91RXjWOkr97OueI5cWy36Otk4YHa0KcsKYogphHyiCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yso_zKFB_RI_aUW2k2rtA1Z5Nd7dkQJ_bgk48DNbnW8IbvOemmiWNBSI-RGlr6AF6SfObEdUoiRCpims7BNhUUYT4j2V-S_O0mX5sWI-ejPDur-hNatUZI5K7thQuM6QRnPmN2eLfwt0oH4l3vmHAluOdA_RdDMkQMXQJOs1nHYQOhoGrjVJgEFtdM8gSOkZfZDMlROGfjpbxy1TKwmVEg3xDFA-Jq6NcDeGgONNSPKVNHUMrpDt-3uJDVHgjHcy_zWxEQJMTbao7XG4H7e4YIezZBheLVL77Foak5Dynd85_Ntj3FyZu5JBHDWgf7YcZ0ETrJvqsBzJ-toN0x-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=k62wvJXr2VFACmC1Nc2KNvt7XraUxkPEYux5CLlw417ulD_WXYFvF-0eDUksntN0Hex8H3yx3v6oaPyTPIcb-fO0PUbShCEIB2V9NiF1DFfplxPTRBSrzxDc88cTM5Zqs8V5-yXlohSGzp7ipXeX3o3wh6kBSaB3VUAWMQk_MlN1gbgE-J9hj5O-826meScycP6jTvnw5AFSodueNkTm4Ary-ec-MwKgBLcLd2W26KEHZfvs8ASWp6L_qmLJVgEploBAYbqIdi2QoFs2qFVkAz_Bm4lZX88LgVM0maWsL8JG2WN0KWwaDEnf5j1Fw-UO2mLkMN-rXuMibo3Ok1Qmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tCVLWRMK8GStN0BGfi7hbOq7TudBOuTDxrFkxaNVVoomFkx-B3JHe1nvaCDzcT1OnSJVN1fV5jT8YPA3lKHuZFAuWReh2iyCMyz4r45pIWuRsarQ951xUCwQDdccAE_FOxz6QJUh1KIV-RKLRfr4O15nzw8hzBacNW8BAL-TCdXXXRecQcwJeswWP5t46rhZfmITRmkfkON_YbkAkDDQWOgnKSWy02kF8Fq0XEGsPyC3k2I-PKmJoK5ZSzowwDeAgWs39alpLcRB0mWIqjFQzmK4P5DkiNPeIpN9vCZfvy_5PENh-_vBXJZIXL5Ouo9ugp7rkRpkEdVyiG4iTAwdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
🎁
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز 3
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24225" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=i-mHdhIKqr-vZXrbRJfrhFoCTRA0cK0Pzua3LEQtH3y_6J4ofyPRgENRBG4HFrc_oRIN91bc52ccRn2SjEgckAOq-HDaCU_Qq7aFWbdVNG1Hx5EkUfTZ8gduupESj4Nh6IzcohKz26jnNTVfiWFGGVuM015XTa7zngTHqpix8tEVRME_FisnNCCm3fwHtef7JvWVHRqh5nPRXPtSmTKr5BMZWp-EDuogkOVNTLdA5BY57TdCr_JcdyLRZKWfnlTMvqwUuf600KneaNpBq_pMnC6RddymdvNpCEki66d7YRdadbpB0jg8lJFr5kDWJGJgWm5WV9vJold4g_OYo6fxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8GrtOrmmygCDvXfbFSknnmOjzHcmCo3piyQoo5D4l4gr1-ZZQ6owHGtKj5uSfywAnm18D3D_P-nF1t7rqESbOm6AToq_6tTD_vKbaZBbjEXzFD5Vmv7hpUziNJpGESI5-yykAGXtg2gGh5RTkPNNmyE3klVLiY7EL0lhAuJ0ga7Ih8zK_m6lOkJSKFvt99X7yssdtZMiYc9m48i0zi8nDM6tl8tuk68TU3TtHGW_N-llVuROJHiAM09F5L1J1s-yT1Vztw8kYi19KUgJWhk4rF20a5bCXxHsaKYr11_1cFQg-1KNhnb8D5bWaxaMeBol-wze3PjivZs1UAj9FGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpj57wUDhukG5myY9N-7mFR6CI9M7r0pqypDGFArMTQDZ_f3wNGOCNS8tfs1KYSI40WjLSsZvNk0rYRdyIqcBfBhxI8xkKgr4WNbqEE8mjIFzq3pqbfR9wuo_9mENU19oOWJTU69u86oCLZ_XxiJRGUknNMzDaM3L6p8CPGGnzRo4FX20fdMDXM06SWwCB1nquiTYNzHwckmy7eH5zSZerJCGeR9c9Hu_o0WbKOvgVKEXMYBOyL5P9-SEhXd3ORNlQYRhlUMb9ZH3i7JrdWpUc6eXLKVjxRjvZDzLMF15PeGFBaU9i4GDAtO74nst5vkmuTOCXKge_EmaOL4MFjEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoXiUonUqq7Tw5x7Qv4NHCJ5b9AvXv-G5y0t6snTZKxJp40Gw2fC9Yf2w6Wu_ldSbJsIcxyzhGznTXvEEd94RPVF3e6L3m_kVKNawF16pLJgZmkT8f-Nyh4bWapXP9BXxgk8mmnjkQspzDYk0tNdL0V4q1cdr42Q7yoEjjdgeV9A9uuFSXsmZFlYePi6NpC7QFFavY5ttvvlwnJO2J8_TRKhhVbhdmq7aBjzToliKoTGxD0wQiHUszDFb0TD2DRvg2utn55PZb5d2cWqYI-KtV5BOWDkaD-adAgQvmBqD1BD5DmfIULtUJcra5f4OzSACL1PH1Yn0vIW-jdDuSD2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZpHEBQ8Lj4YNuGvBLWQda8JoOwjnigYObl4VPA7vZ76G9viBF467gAwFsXKfezTDGA_lzDYPFG77dcjcFHWV7Y0mM29tMN2Nd2Y0Rx3wuArSV7eBmcWBMCnbkvw_LjL4qMPMLNljes8_2kLhxBv2lLVy4Hm_xMKg-h7Jw9Jx6kopRnePXOCkT-rcckiY9fITQWnoGS8i_MXpXBOnKy2swl2jNi1DwvguAL8a99IsMgy65wp8BY6OK3ZffUR5YNdGLxO6qi2g6h7juOKBGWTSyzdesn4ZHspwcvlPFZhhLX14PTLaQpaDiFuaOJFe56RnU63iCw8HPDEfBfK3JGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZAsBT8e8tKq7xca5aLd4R_k4YOU18nd4rusKnqHN3INSt9tZIqvksWkLKSIw47KUD8rg0r1LgymgmjBra-6Nx5mct8qyhOJqmV27atl8Yl2R_8-zQygLUl9SXwKnuXDEsOT9jDYjp3_jq_TyBn1TlKlwvcmjgQTOWQTLk--aU0LB-zZGTwy2OgnkHnMqiUQrvAlrTMh0djV1EaJu3n0omISefrsnI8DWuSxws3MWmBuM_2j1DQZJVn_-1G750axnb-84xbttWOb5Vpkyn7cYhnoxdm1EXmo9Q2rNTpsFgNYoOoIYjZvK615-csjHUEHjv2qRhkzrKUHqfV8KMubSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0kWPW5LJKzNWzi0gjx0MitJQvu-dQ5DRPjKXJLnu0FZ3htpQlO8gYGODfe58Cs7q6Gz8aPpFxjMqo0VKXyLNLYfRdocG77zcZnR-wiIjKfXKSvTES_eoRq93bw57dQ8LORFGKtUt4jfo_lIlLET9zgJGZ8HwVVPwPcyDy4INY0Lc-6yJO8i_jRSmaO_WLk4OZqS_bixaBL6GUjWkPAajaa6wWUaDHt_FZI06G3cgeV-s_8Z-RfUc8n5ENG72_hSrUI4GGJfHJ5BIVAQVKmxtq1-m7peYNsM15Z6GcbHVJZxkbV1yxUwPHvpa861ySIsr22HDeI0Fr7bGYOwxUtM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgCAQ-wPtJxCvjn1_lgeQWMr7i5tEV3iCENyORXAXR4ZRo4hldWltUa2iPV7Nh7EKcavYRdb2yKZOGNTW2bhGqgdhAEBCra7K8uwK4cBSUVdmTem1CXUbv5i8xPoYK2xPQUUYCyj4cCtWlNCYLRpjvmgUiT4iOpaBPpgfNjVPMTsI_6tkOpNk8UR19ARunP6eLBchposmQ1-QVkIj56nMcq0cFCmtKzqrDaQsVlboRmsRq1GdrSIHXtB5hOZrizyd5S1KGxbdzlQofELPd9FffcqmdDWdtv9Ebnqx2qXCMb42b8hC03aORW1hBynF6bDcJea2u6qtH1sDA7l3MGCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbI1WHaTqhYNt2Dm8bsuy_fBi_gx9G9vxCGirUbXTzzzDq_ozpSrfCw69VTMiNzy8MQHBeIvgvCzSg17nxQEeN5vUID5dGSYFLga5JPsJLDGKp3YY8ph8_i65z-OwEZ9z70yXrS26rtW6unBFfHxj6rX2S8vVIPvkiKkxqiHawlXdLtiqzXNhf1grPouuDolNs14JRCpWjBseUEwLq6NIQOFCBwK5QJYb0GFQggX9aO5TJgPVrnSoy3lYq7hTTEMA1_9NSngKny-BFB0J7kggVeqQpia14dlV7u_Kk6AEl9cbwredlLSDn9YZPyEflRyZnOQ731MD1UJXzaIyaeNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_FV4DWPlzNX5NY0K1OankD44Cr88eC6QsDlZEbtx0IVTFo5kpTNVV1OnuJa_Hb_JcmDPzXCjk9GqFxhFjdlB-AwPMysYmbsi8RKCDCahEB1s7dom84UJ0SIjUk3-IifYpLCI-upmM7redMDrBJWR3gjk-hS29fhhXjrneW3Z6eTLO8tMxYOpfk2jH1Znq3BeAT14UKQ97q0YvZjTBUjmT1r0VxGFbiV-OMurI0TWrCAUWe4bZ-Q9vVVxZEQg0iPJVy0zq1T4jPTCgUvjhZrMDDIwADxER_1c8otaTV90tpHFuGvN7mlVcwYVUGC6nxMGJktyQ4ZBrBPAiu8DpkTuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFXCZFagW1CX8tl2caZiJhgUQyx2tubYEauQvyVFrtmvyT32w7I5Z_CIX83nh3gN3yVQha1nnXy1575CcyOmtlcfYvJ1UyzuhLlh3CiY6IHYlpuuIFULz3N4BLW8LQ34Vump_6xUZi2DaCwzrMhv1cAJbdp-Cj-jMuUbhCA7igSdJOQiDn8zN5-K2Xdxg9IRfaF6SAlqrHpXX0bFs9Kiwv7eJG9HaFwDw19a45hYfWz3Q-tULUDoERIkeYAR_hHMaFa8AnlINBWk8Bteu2MOQzBuJ0aamt_xXubL6orx8nA_hiIPd_G9t6LNHcv8uz89d3hiWBS2W1vMbFvzBp9FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbk0q_hkmFCfA8IgnjreQYfK3BgXyaCwMF_aDqUC2-mLF4i6P3vcfpwL8lDDQOrGKiCesOs3iunfWSc0X0Uhh3tRRueW70X_Rkygf6J3mLI0SIUCbfCM_aQiHVS7uTVMk_dC4OAV1pQ6Wa9IKPWXRy89zSAy1VB1wR-fMQ0f5lGkNZcvDifePoYm-zisCoSJYSP5AiIW4OPL7PmoGhUxMivAzK3FQFIAn0AJtJxt7gqOS-gMOSkLwWJJ0SUoDf5sP2EwiBshZ5vWWvHS6bw_DJdphipB0LPTBYo6Y11qKovPd9qKebjYhfNxBEDO37zlOwqUknor1o51wCjiXb2QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHU7uzk-fxyo5Vvgs3i8LxYllApVw-tYQ8jGt_G5tGLySlZb9FB73pX96Vyo-sqQ1wn_c28HKoDjXx9cQ752gHB4i0pUjyMaql3i7_s8TtPs_mmSs9vMKtepq0QsglpP3rpAdPn0ofpWVOmBzivOMr2QlOfxK9ys5LipWuaDm8tWLfUd0EIbNLQzOb4LKGZ1Qdn94v1VllCp_vDmjUrbBeS_lE4DMXl2SYNwVbkXI9d03kRnpln1FyXJOFI_uLerHMqLcbUxHkDIzycHliKwzqkSprdy7Ux9tNd9Q2s0cx7IeGeWsO-bWfuWj8k8PI_jA70GxfaiDlwEWC5MPlZIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT5E-AvDtKGFuIVoSAT00RjF-w6Nct6vruop2YqcqFnX809yXxHtPSqaWTSwxkAKkUMARTronu0pj9Yi5K2nG2Js_TZEreOPKwTRoJE_OtVUjFdSzynpTxxSdprpWlDc5JoLGnBrmUpZtHOrPI9rmzGlz6-Y7jPO1P3i7sgqToI3mqeXNtPYQKWJjUP3X22GP50pl9R-dbWCRvjtEYH5FvTrr4A21asY2Iou0NbDpz2TWbgKDmQ1YFmqxBfM8kTt1mkJEGqIAxHHaavJQskfVIutYF-_wPeb7eNNGXhekpLTOlv69xd2DrHAMGLetbNjDvwJ1GBtzBlka4-D4dX1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT3xU9e2Vi-1MrNKKREBXYTWE3xGNa18IN1lPyt5wvnt29Sv8YfFXSfej4yWo8eI54B9IXsuhUbDlZswEnJKKQu3yclxb3m-YEKGTwvrDzlfSQqO7ugo6aeyjScEeK_MHd2aAgiOXjtu9n1urskzSxO5aD7yJNCUYkuoGitqpf_3xlO0b7RCvKDuHuTeOyVP-QHh1KcXtvLF970Q_VLII4by8frycMKtLvfIfpYH-mDuRhcwBQiOTM9gXJ6RcwUO9YWcXBWJAg_YCy0573SkMV4UYdW_p2ul5NJwZXpv8NXCNbqcjduEuViCRnQgnr5oxjcBxoHFigWWAmo-vT50-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=BeHr4jdzDHcFoQdrrKlCB2hP9rsYNsIJAOuNQ2RJBLK2ZRboFehzclBdIk0u8hKW5eBbB7ZA5daL5pC-WUYIfoNhLmZYWUmfQrAq7O3VqPzpL23ev33XnBUsMHS5T_dfnWbAAR7zOVUf_Wf00zpiSR5b-43z3ptf08jUaPGzSve2EuTG9tDJegt2eVMsdOHw_MHYCJ-Xc6OaNY3k0OD1sMLzhC9vbuojKWUgeh5ZpLLQE4w6gIp5v59M0Bz0GpMmO5duxAAdMaotjA9yaIg__z80O0bV5GvqnDBJlbKbnhnFJuQCO-1Yog8suL2a85lQ12Fww_JdGQe5VkGWNHtigg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=BeHr4jdzDHcFoQdrrKlCB2hP9rsYNsIJAOuNQ2RJBLK2ZRboFehzclBdIk0u8hKW5eBbB7ZA5daL5pC-WUYIfoNhLmZYWUmfQrAq7O3VqPzpL23ev33XnBUsMHS5T_dfnWbAAR7zOVUf_Wf00zpiSR5b-43z3ptf08jUaPGzSve2EuTG9tDJegt2eVMsdOHw_MHYCJ-Xc6OaNY3k0OD1sMLzhC9vbuojKWUgeh5ZpLLQE4w6gIp5v59M0Bz0GpMmO5duxAAdMaotjA9yaIg__z80O0bV5GvqnDBJlbKbnhnFJuQCO-1Yog8suL2a85lQ12Fww_JdGQe5VkGWNHtigg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=IpBIME00sgklUb1L0QQPOtvWnDErWpG8q-XsgW3DgZNSmg--hNlcKsiMnv-crqfHG_jiRPupIXbUGrl4OJt_5Ppfd8EwVaaoZnPaWSUuSMXy6m4LvrzhPHNKyjDJdHJ7DMoMtdp7XAk_wo22TiJxykOBSncmqZ8YcQb7EZvnGUUqDPCUyTobOLdGnaboAnVWucUvxYmm5tNH7NCpCjRLJSjd_U1w1ausscW3x-ogrrI88XjSeg3v4WVz9eqyxljGu10aNX8BslymVGlcVbRA95hMr1CytFQepwXqeokAUNt4MkdChTID3StlmmHCHX90MYWdAp2cWJ-FZtC0sm4iGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyVpxY-f-Nix80VJpiVwWLAlbui7Z6A6WR-E1iNnXPCmvQd42FHFLH8ENzI3_fFGFZbt9TbsE9ihEURp_g8i74jdlQ0uaWGWwuu3UeSBQVVLjKi-1Ed06MMNRry0wjXPEjU4P8-sDCMDSu5hgg65GxJhXiIbIxb-VD8IuuaxnFOX1lxkuinvhtsxiGQovz_0fiByUnGwSNZm27aHR2CQdQb2ZPuBCL_xqWfCoesAMZgOAsSEAZbBk4NuB057LrHsxyMUIlNKeYBarFhX8XOE-aie4Oi6kID5DZGBSRRlXPuGCXCtTfKg2Ao0Eply0mLgjfEnzUFAa5B4jwR36PfBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kadub8rLVAzcMdqQPVDOCYtGsHDiq4QeQnD-01dF4afT7qoDLlJzZaG-jk21sYPaV3cBNBR8jCvx0hGm7lUxAxBsdkpp3PDMTUZaZJqomKR5f5HvUdLqQlqnQrL9yZLMNHC9SBAkPk3WveUJq_aqpvv64l78dZLdGRnVNy3kY9YTnKGaGeK5wONsBPKlYITM7FP-tCy8RctL1hTaCdXbaGmyHd4XexwHW2BVFhj0QPUysqsNnHYOC8y8WbPGoP66ltsFlgn5kOZtkb9YXndn4ytlG_q7nyG4xwxFKDbE2ilEBcGKr264DbC3NZe602Kafcs2yK_s1jHD_eImCBZdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azC7gtryPOWI5CoGkTdym2kOT33i2_V6mqbi6o_dZUwiEq8kON0XiNikSIuy96pL3eTrZX2SNO9l5GqZy_wsRlmarpJRuWEjBWDWErFXFMmqWlla6DKNh-svD7mgxnXQvV3YR41IJb7mvePG-FbqqbRP01Cp4LJIjixbIrX9T5S_hjmyC6FAzNd8OQYmBVmtHD5pmfEjrVoUyIIfL1MiazdLbFnDPQi6aoI7x-4GGvfIF6yLRZepc_b6FK9QNud9cZpxcZa7xPBcA7-khSJSN6ecAMC-z1SvyCSEHMnHZjRvUauDG9N-oNxQmkjBwN9kPGv-OonJRZeVtZj-Eyu__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMq8fTS0qgBOmtGiXOTbDuU8W6svCfjfQgXalCAgSd2onGo38OKeEzJT9_pHTX9yRwHgMKEv8d0hKn889UZcrOMN-r48gb7N2riIUJl60mfOZFmvPSZ6gfmuqmTPiwkMAUiRs8lL1ZbC_sCBLO_J_-fxWQz0YQ1R1uxcUvH7_W8hUe8IoURHyvc7k1aIEc-Hr706agyJyfrrHKshNsGLHPxBEi7EoHNrTAA1wl5EbCGux3jc-qCd8upRiYQu2pLlH_KXP7p8Lj1HeV8FVSiL0CxZ4uW5xx05NsdcjU4My2zaxGSHDKKtS0tCMPbYq_NXSoLbhKG7oTB3o4FsAlX8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=ocXe0Y2G6D7pzv1jo1irB2ZIHGedGgHLepO15g4oJsnhgC8P21BKx0qWaJuCjeZK3rG5rV1PcDpho8GWRiwSSC9d-T6tliJ7cHo2oUmrb2PRefb8Wv6ynZIYXIimo-Moy-Ys2HmHpuwdHzl5MG_aAR-0lDXto4pEEvEBJbPF6smgWb2mYlqgDbCOrmMjAqZAQVWAn8xRr4p2mnySWy_HcidUmyOzhO_FjTG3IDbI7OGFzMDgGut6JqgaX84RzuUAlj6I6Os1uZi8zpQJ5SEtOs2pUyDwV_tYafY1uAzpHcMxJyM1-Qo_-OdEe9PRuXvi2-TKQbT3X8sliEx-ZbRxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=ocXe0Y2G6D7pzv1jo1irB2ZIHGedGgHLepO15g4oJsnhgC8P21BKx0qWaJuCjeZK3rG5rV1PcDpho8GWRiwSSC9d-T6tliJ7cHo2oUmrb2PRefb8Wv6ynZIYXIimo-Moy-Ys2HmHpuwdHzl5MG_aAR-0lDXto4pEEvEBJbPF6smgWb2mYlqgDbCOrmMjAqZAQVWAn8xRr4p2mnySWy_HcidUmyOzhO_FjTG3IDbI7OGFzMDgGut6JqgaX84RzuUAlj6I6Os1uZi8zpQJ5SEtOs2pUyDwV_tYafY1uAzpHcMxJyM1-Qo_-OdEe9PRuXvi2-TKQbT3X8sliEx-ZbRxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIsVfwQn6AIqMGSKqe6f_MKPT50gIZM4sfdOWdjNoerZ8mff9O2uX3xf2WpXaWgLw2-uU0aq7k_tJE2z7I9Se84kpbumT2_2Q5Vgsm_NK7Ib2TYe3Vl6poAb--FeeqV5talqPro4GvvXQZtw3flBaorBU137gAhIwptxwpkuiDBp21EHsYtivs1DWy3rUUVdhEEBYOb0qSktwqe7ZxDuGTSbFTQOTDAKAgRMW66vkhtzA9FmJh1De0QBsvd9dZr2jGSVViN4oI6BuVDTMGBU88ltSIszEnuCW1XL_3ppk_QL3ylGrVudT39hh1uzZa9hIyWKrCRB-kBKEKQ3JAYqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=F3Hu3mdaJ-HnZjP_AR7XkLhSgICTB4SdWE3kobRm0KbXafXSHKswsvpt2t_g9RBknLBXuM4J1Eyduwo5wUkk7_RdwWC-MYbOXugv4shmUNMT-Swresogxc9WgCWex59ucy4OOPW5xRdyZQ0X3ZlfpCLz57DGK-kXEZwKzMkethzDpKLlDUz0FVUlMdJzpGd0OkEg-nbhpSwsk4HSbuozCaU4xhAXVmHEtLn5OtucAjHN7uxJsWbaGqoZsNo-ytVULNbf0r56-7Sz2rOj4QDB7NyL6Ei2Zv9gDTYuLw8UltglxUwxwQ_to9lUvkqNNcTHR65nQ53qrrHzftVeXVSPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=F3Hu3mdaJ-HnZjP_AR7XkLhSgICTB4SdWE3kobRm0KbXafXSHKswsvpt2t_g9RBknLBXuM4J1Eyduwo5wUkk7_RdwWC-MYbOXugv4shmUNMT-Swresogxc9WgCWex59ucy4OOPW5xRdyZQ0X3ZlfpCLz57DGK-kXEZwKzMkethzDpKLlDUz0FVUlMdJzpGd0OkEg-nbhpSwsk4HSbuozCaU4xhAXVmHEtLn5OtucAjHN7uxJsWbaGqoZsNo-ytVULNbf0r56-7Sz2rOj4QDB7NyL6Ei2Zv9gDTYuLw8UltglxUwxwQ_to9lUvkqNNcTHR65nQ53qrrHzftVeXVSPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPvXn6HHl5boZqipksHw2L--DCJqypAQwplcqy1ILUfNnOnCltFMuelEqnZvn1k_0vL3fp_lFY0fC_jnwibxP-GmAWzU9MlX4iiSh8xD5zXdjff3nbQ-tzcXdHuEFMUWJGuO90BIHlTXQU3o1k1vk_nRwu_A9AEBaPmHgPGpm4vV4Ml271UdsFrFmOaq6I76SA9jnNKLi8n8JKet8Xhrddp6WHwzqND4-wKfSkCf5689mRrgnInsU10C2S5XjJGCR1ReF2zngI0TUPhfgzAQhtz6JzzJaFXeEs-6n_UIwDAJ8KAL_HlZlHCnnwwUghng7ujobkjsqFH88SJymjaWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=VA2ZKD72HyZ9d9_IdA6alEBLFmYiQeABBTvU-mudeOXeETpIBtAeHrytlRUjGlAYLhhheCsVoc-ojSiPyNdpEf6QSqH8iNOabsdG1VEx0G-WqST33q4vDcL8Sn62cdBVGezNZO-04vjk6XnxKCJ3a7KYrTWzhU6K-PIlwd8ap2E_8YfVqJlDk_vzKAgwfJ0hQZz-iYSnUyWJF7dSb6PGIWAoLw1LUCOamj0e44EPCPMX7r6VFpudLEvMaGzCPJDhXZYx3uR73QkSXqFpvcaJhI72tngHs-dHOu9cGcrjsIDHM3w8_OvScfTtoJKJ8C3bzCa0ApFnu68jqNOtXbEWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=VA2ZKD72HyZ9d9_IdA6alEBLFmYiQeABBTvU-mudeOXeETpIBtAeHrytlRUjGlAYLhhheCsVoc-ojSiPyNdpEf6QSqH8iNOabsdG1VEx0G-WqST33q4vDcL8Sn62cdBVGezNZO-04vjk6XnxKCJ3a7KYrTWzhU6K-PIlwd8ap2E_8YfVqJlDk_vzKAgwfJ0hQZz-iYSnUyWJF7dSb6PGIWAoLw1LUCOamj0e44EPCPMX7r6VFpudLEvMaGzCPJDhXZYx3uR73QkSXqFpvcaJhI72tngHs-dHOu9cGcrjsIDHM3w8_OvScfTtoJKJ8C3bzCa0ApFnu68jqNOtXbEWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yllf0_JiGgQZ1NPViuA0DarAd0uWwe6FJZpKvukPCW99e9H45YcprXJ9EKwTaMeUm8iGU3iy914UOYPUJsfYGVZ0OqcRfoG3s-ymKn3wvm7_OmCQ6CXAAvcRL0Uw46YOe-ceg1SomnGt_C7mftcul88T7DF3jz6peQdvv41ssWdHvftSoOZxhD95vWaCoMCRIL4l68PJrB1KKlG4352VtwAgbswAs9IhveO9zvl2mzU4S7OSBRe7HuZnUjSHrTGIXLH43mqV68lGAnqnYEXq2D7Axw-uhm0MB6omZJxZ3vkjRBVZX-gIKbXW6pNnfHmDWtFf0OpE3FrCH64CJgUVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=IpXqUTk9063SVXB2Plj4a-E3HEvTwfu6kSUOWANMlnVTjS7A6Y7PGphwCdGGy2kgbLmqW3TKHiMqYaqYwvNZfdBRIGsKjkdeCkVn5rSjZS4JPOb-f2VmPdr2oUoQiAnAWHIHactCyyOZvvualIoLtt2NXK3Qh7dPfBEjdn8eV-P_0a0DHZyggNrlTkmL_Wl9HlLuCx2oPl5V-Fu0p-7ZU13rUPksKNvQDVbaoPjbxzQwi8mc1HkX5rUErhNt7skv80BPJBdcgZSLYcPDWruA9U6S4DyoR2qX63c4_YWnoPEn9gEHztOdpfvpaHc6o3imrQlP91cnEniuzXVnQ19SVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=IpXqUTk9063SVXB2Plj4a-E3HEvTwfu6kSUOWANMlnVTjS7A6Y7PGphwCdGGy2kgbLmqW3TKHiMqYaqYwvNZfdBRIGsKjkdeCkVn5rSjZS4JPOb-f2VmPdr2oUoQiAnAWHIHactCyyOZvvualIoLtt2NXK3Qh7dPfBEjdn8eV-P_0a0DHZyggNrlTkmL_Wl9HlLuCx2oPl5V-Fu0p-7ZU13rUPksKNvQDVbaoPjbxzQwi8mc1HkX5rUErhNt7skv80BPJBdcgZSLYcPDWruA9U6S4DyoR2qX63c4_YWnoPEn9gEHztOdpfvpaHc6o3imrQlP91cnEniuzXVnQ19SVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=HJCzL7hVdQOWJjDBjkw_FQ3SJVXiTFT8fus5cFr-UG9fqxwlxk6evW5LAz_8iYWTO_BVuE10hukLZL4-B2XqHccDNLlfJmpXnBuJYKU2CHP4o5amSmWcYqPy48pmWk498xFyf3G4dmZIQA_3zhFHQSqKcmt0xWmPcuwYW9oUsZlvtS_YQF-q4skY_6st98Ulvq4lXHk6SuUnSVIyZ-__zvgdSo5XRvA1Z36nTTRKTymuTP3rrf2wIeBg9tHJ5TGoWVrBc5MOAL82-mX8Hx7nsUEyPDN7mjsMFFBYBvgKohfI_uuyp5aSRtC1YoIAeQnIb57EUi6qlmXRHgg7PyCtjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=HJCzL7hVdQOWJjDBjkw_FQ3SJVXiTFT8fus5cFr-UG9fqxwlxk6evW5LAz_8iYWTO_BVuE10hukLZL4-B2XqHccDNLlfJmpXnBuJYKU2CHP4o5amSmWcYqPy48pmWk498xFyf3G4dmZIQA_3zhFHQSqKcmt0xWmPcuwYW9oUsZlvtS_YQF-q4skY_6st98Ulvq4lXHk6SuUnSVIyZ-__zvgdSo5XRvA1Z36nTTRKTymuTP3rrf2wIeBg9tHJ5TGoWVrBc5MOAL82-mX8Hx7nsUEyPDN7mjsMFFBYBvgKohfI_uuyp5aSRtC1YoIAeQnIb57EUi6qlmXRHgg7PyCtjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwVWG1QcBoqR1YTzuhfg-NSstHxFwHyMrQIkFsicqMPyRuPmgNfNvtNJMIxY8U0ApApr-uLmsUCzp7OzrWsdX2dmpN_6HfuOY-Z8fklPRFHFa8oy2L0HTmMpokomAxfmGOttSXxisl-m0Y-GZ4xHrYaCU9aYUgfAgRKmfPbCLS9wEceDNnh8sc2Hg4pyBExeLoC0jyqJp_FR9UOQjFn8oENnakhL9EDat0a7dYRAqgSlDFsPId8pjtB-SI44gNPLdPM7HIIq0SGWTFlW8oiUCE8JiMeNUQVjCQZsqaKpPaoyZ9RVb0tv1t4EsQHq450k-JchZiGSbfkB6YokhJasaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKAon3g-DHrvamiSd3ef6VOaMGBE7RzYb2-sf8WRk-VBaPulf1lAfLXESQ7ChdM_u9tjrkG7r17BCAMXO4c3rJN5BGHWbGSqAdEmy_qtd0mLKn5pqLnfzdE-d3l3FuE5b_tZUuJTM4I-gONwpqXhQX2gGDWGk7SWvs4t-8nBKLYgKPgsvvq9cbY-nO7m5EBlLOfnnHjYqlXv1cneQRfvh-BJJ2DSNVjwtDWtnI4jA7tZ5xaElbqOHQ0G4aR7cQyA25Ides6lnoFB_DSz3ob8ADPLebSzVvNwX8uU89SPNAok1AaIa5vAAgdySDqw6VkNXe3dHvEYMwgqeQ1EPbxiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeNufXcTuGLVn-SmNYtyY4jQpl-cBeEUGbqzhZ2Rm817TiWKM4VHqmAeN3zHNk7tlkxqvJrKs2vq6d0yaHNRc5-j6xGNjRv8q8auYF3iMgosI4wqWj59-EFWP1JSIeZHlsz9n4ezyiXsTvhpY39685i7kiUzNItnBRVD1j4cTXEWpBch9MTN2x2kOiw0isPQ_mP3s9PX_XoiN5v9ex8NpZ2zF6_iNj50DdR6aF_xBZFHizXzIUqLxy09J2xregCC3blrheIMkHPW7zKyPLG3BAnibu5emZ1dup6Wn7K5xEtg6vw6ngB8S5jd135CtxKwJZXDdrfWfudX9c4H44C0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSOGhzkJCinN_IJ5-nccEs6tmoXwcQ0orpmrAZSYAXSaqm6zy4GrFcb8wTpS_RY38-0tsW5I4pSB7_NSLqtSOCohJesBZHwC3TJ8_ukc0prSIA3D4h6pUjb5xumouWrlvwFiSDK4-6Bz3JF_xBTVkh0VcM0OfkgqqI9KItZ6-vK_QiATurZSNvUhcrLeJ3A4DbzOfG2NKCXrlNT2mbOsC9i_SS2AM9254F78bmWZSdtIGigsnXcUpK_IerRWYqOvOysj60Zd4EN67PyW0cW279ve-7Yj1mZYI9nBgWGq_kM9C8e_5ujk4COvYzzLl5Gc1arJgR_P1lJElVRPm32Omw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFVBHoMC-801W4NBJD-maLgWXtctAj-lSqT6t4Qbui-F8LFBldkuHKXeiDAftW412IO4OH3VFihwYk1xnD8MFtjpSRgZvOnIG-v-7bsUuY0MAIB_xITOThbxl0SeXe5nAZEnlMwH47kTsW9by-qG-SrggQaSvLtiaK_U4RieOARE1fvpnrxX8aje2hYnj86RlVBF0ythwdQqa-4C37-V5U1ldFk44a5p9Wtto7ItJmNNrz2QMKOnG_qccV3Gr8qQTdBBEM8et0xdPhXwX62VPrEmvIwOml2YP46O15h0WptaYrsBP9EocVzzvJWeDeNdZoIbPgafgYiOR0zq5SUocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsEbos6Owz9y9_nVlpn5e-cpujursdCawdd3xbWZJtnMjKc_0II-4OLb5IwUZiCafURdZZ9YDrmbme4vTjlWpvodXRZMXkW4mgpi72AptzPfTSCYaw6WYhR3L1a5zGaOSbZmHm6am5xi_nJg8v_gr3X3PWHTqqZjZ6xSoidiOw91hkmTNYG-xxmsKA0c_kojyoItlEnUUWASUFLX7wz7IM6acH8DoKB1aDWyuYQN3Aw4RVL7ZbXqQhwNEg8Hs50Qz7Aj10zg20vWh3hiu0jgKn-bnbLiOpMk1-_BHkZdrjGZHJIZO5WJod2OXa-RMHWgPOjP8R_hmheA5DGI0VV2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNmsUIB5uDf-OODULVQ5hUju9hlhet7K3gmBAa0WJeDicnDOa7HwK-CRWOWMLLm2XZLMg-UsrWSRrEr6QFZKKSEjF394ptPL9fmY1KeqdlYeQnobgWk8xXUt_rwIjABg1ev4J5C69xThH7mMjaWqmg1shlQ_MHYa5fjomLyt2BmMeJbh42b1NApaXw9Ld2YquqxZEmraolNUX8Dx12704YgP26wq7DCPMSaqsoQo2Wcjy3rhp1J2_uPP0EoHHUeXhFOtLSpv3tD1biXvK5ycGr-5gvy5jJa68tKpT4UTYu0-8vWyczY99qGUF4g1qw7esK3gxEev9iuT90LQauepvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5X9b_2yAwK7X_dwkl1McPmOhRqTCA6p0iOnWXIyJJBQUHA6H2I-fW4YnrmNPeSZ7twHt5C972GMXO5KDSDuJt939-0Pe9INTc1dEoGu2x-Wki__h99KuiFxNilnaaKZoSXI4OOvjZdPvVlKGz0NShPglN11hh8turK_5k9ve9HgsxdnoIVzEC9x58kpRl7whivjQ3sZ-idQ7DdxZ69sAu_ULDpdpZvCbE8MQwhgMl9AoPMv1RS-ZqWEVCeSEKVPjJ4vBzzDKwjAUIhefnDWfvhCzNZeUxHWcSeVFAqJCXyTtGuX8hS3nm1Q5fI2TNiEU0e1nI6IcvVAeAndMVKDpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-qc-N-fOgHHEaX11dycRJlrgxXcLnHFQgIRAIXFmpAauIACdj7xDocikqE6cgIjjYcLquoK-WgMWYeDVvJjmB8b4RqvpxHDFYBCp_Zy-pl3-yKEguYdMzOHTRCuTmQvJ2oFPbkxMIfNVo3zuEEAkbrdCTiLdhY1zetoex9dM4S8DCnA0GmCsVbznE34Xu1h5sB2DeetgvEHG8cTgc5aIor2WqIwMkiyoMk2ncRtWKMJAWkaEWuTK086fY5jEamctVMYaY2kSq1K6VdpED3DHUEpvkl3_aUG4G7bZLe0YxqQDW5pl3D-2Q2Y4NmPDo5uAzb4ao_zGkTBuW9xxOpxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLEQaE6CsxR_6nzHzbK934pyWrlexj4Y0idq-z0f2klTPhtQ3LEi5QzCNqumvr0jyPUqxyJoGiVP0fsbK-cmz1OgJVWXk1hZrx3cB1DwoM6UMWLmAuishGMKIg979nyr-SaPulYdhhSgh-yDfeY4HZ0GJgCyhZIo8wG91lqVfVgu0ZgjVLjptjRSd02l26gwG1FO9rs0cahe-99C-lCt3UGpCD8O0rqfqdvCzYhrXiQF7xiqtXimvgKTIGVupm12OXtEdA4JlHGyxdzuj2G3VVyUB-iUSL1G65MCTsNh9WytMfCIFH3w39pXEW0m_BFdMGNfT9u_Au4NT38Rs7ndUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL5cunOdH7EUH-4fHEVQZpzcYMEnTdyJnbamgbYaUB_7Tz0Nm_2Z9xduhkPtuswTLHtevAM_kKgHbI6jh6c3--tiu3LKFqFomWWEP1jofyI3Kh8sblmf3RUVrHeygxO68Cx26AkoJJv8Q48b7-s3wlFket_HXF_Dg6LVfQ2f4NSEsZuhmAhC64h_2XhFC8CU5cni-OGEOcRiwbVLlO9slXF7iduosYWtkVV_ij0dI7g4ncyXoyOVH-1OYMrHt9Je2guIWonRUY78Bg3MQSc6L1Rf3UdMYznmcV711yUl2adnXprrBDHfGjephWI8nR_DDGxdUuC6NX-_4zU5UN8DLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNDe7fNw21arX4TiEXKWJ-789Yg9PDrIS_PoYneMnblfFnCgTjTSWXprR4lmMIxJEwQZ0DuIf_e_fjqteYY0kIeEHfdMLc33WJX1_kkoJhjoxmOsFqE0jGgHBj4ejdIW08T5xF6UPvw7910KRCRJ9n5yRDI35kO1NfUvXfdKPRhOsx8NhdgaE8lXJ8TQguwHJ7ipR943BtWs0R87LhhzfrZGgPco-IrKSKc47Ii5sNRgj6iThNr-3RCBGboUql3Tp7DuOgdQvzZWA9KQcCXXKYtR2hwvoUBe7hN4si9E0NdGpQkh3fEe09Tjn_HE9hu1PTGb0UJFqH0U0HpsMa8Htg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOuRMcON5FVndCOGT4Pz4x7kYI_Eu_Ap_deC2qFKSLCmT74Kp2ZWi9snkN4YxbQJaZawAeh3VLwqiSrjggfY7qpApKGiMEIxkuyURTvJ6a4YF_LUhEBoc4sFW8fP4FXRxnMjty_t0woWBsH9S5l6Y5HhKUA73WHCpXkYTKn9_I-2Sn8SjkR7V2LRbXcf5Qq1Mg0B4E6sEpwUapk_BYewR2qY9QTCfJeyfXtXgxRB_WnEzmXfdgkCHZVfUQAFGo2EpJlcl6Au9Zfc7xF6ywXLMri1yJuIg-F9Y7mX9erSPJLD5Pn_r3LFN_9_QitHkr6pYJ7ji6E-qkMvVSdzj2UD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=IIARAktEpasm1WIzQwbrJVb-2Z-J0s1qLX6Kg8e82zRaGDNFJPveRUvkaoPhAWQR3qS4U3iN1alugVNTC6vA5UMyt8ma-NifbdEtrqyvB6AAtdHKYkypk_oHRpYvTn9EOqt356YTHhC2v04ztGrQOv4UvxWO6dbD3mMv4LlX0k-I6TqIt2-OP0KJ2kbpzLa0PTrLwn7KBu_q8ZpMojzSvj5XQx7hdcEkKwJaVKnmXXuPsHgof2QlF8tiCu-TCZ3axQ3tiW8sCOFedq6HAESZoFerPGtb6NMTtXyWpTcduhHvMUgdOPJxVsezcixLojHPzHSmUwdOSJe6LU7HKIVrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=IIARAktEpasm1WIzQwbrJVb-2Z-J0s1qLX6Kg8e82zRaGDNFJPveRUvkaoPhAWQR3qS4U3iN1alugVNTC6vA5UMyt8ma-NifbdEtrqyvB6AAtdHKYkypk_oHRpYvTn9EOqt356YTHhC2v04ztGrQOv4UvxWO6dbD3mMv4LlX0k-I6TqIt2-OP0KJ2kbpzLa0PTrLwn7KBu_q8ZpMojzSvj5XQx7hdcEkKwJaVKnmXXuPsHgof2QlF8tiCu-TCZ3axQ3tiW8sCOFedq6HAESZoFerPGtb6NMTtXyWpTcduhHvMUgdOPJxVsezcixLojHPzHSmUwdOSJe6LU7HKIVrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO3X0MvO-5iuiuAmG1W9yu86DvzWcQ7rfUopVVEfMfEJoeqqHBQdbOaVZjr3UeDJHlpDetNXj3LwmtFMmKXyi664m5wcv4aS_hGmwGX28FB1I4LWCzHQZvxlANPMVPJNRQ-SFfEKEt5l5qndxy2UYlw_aecR9H9mE-Ms1WSB3UsaCaZH0jf0uzZpIPCx3JGBR_c8lXeb-0uXTi8Xs96_rYY-q3h2LY90gj8qZmnh6cqJ5vWVGnE_mnp3xhP-VYZFvhvGqcj5Y79FdQt6pvmVYU604oROLfuk2ocZw-2qZt84Qn-kl3CUiWQV9S032YpkuHvQlTujxqFe9v4y6PiMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=b9rECfDelzWP3dAL7qdmF3jr9BbwTK1AwfSTtJU6ivX35phnqOMW-pUAQDLgR5AbnPBASrqOm79ZXyMP7mPd2m6F8ft0jtfdT3WDdNwJ-wET_MOh1o6zIxMB8PlGP67mCbv2lVYKCHB2MdWyglX5eMXZv_j6itDQQd3E-F1jo5OZlg7ZRI77GqCqvOjgYEy3DHG-esi2hyjvA85uh5ti9G3oifZhkMESYNxbxIx5Fh0A7dH7jWHUF6Dtk0feZtLV3N0OBNIenXMHS227P68VIQIfz04xJS0vuRnRfg_Qp2dhMOhx4LGD3FORLH7TJrxisq3PpPmNPwsAWCbgQJQk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=b9rECfDelzWP3dAL7qdmF3jr9BbwTK1AwfSTtJU6ivX35phnqOMW-pUAQDLgR5AbnPBASrqOm79ZXyMP7mPd2m6F8ft0jtfdT3WDdNwJ-wET_MOh1o6zIxMB8PlGP67mCbv2lVYKCHB2MdWyglX5eMXZv_j6itDQQd3E-F1jo5OZlg7ZRI77GqCqvOjgYEy3DHG-esi2hyjvA85uh5ti9G3oifZhkMESYNxbxIx5Fh0A7dH7jWHUF6Dtk0feZtLV3N0OBNIenXMHS227P68VIQIfz04xJS0vuRnRfg_Qp2dhMOhx4LGD3FORLH7TJrxisq3PpPmNPwsAWCbgQJQk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSvu1bpJGij-IQ9CZMazzMK6u7QW7THg52InTRyJWacI9SiSb7QKD3eG5L6hQtiRbzndWnghzI7l--wNhQH2yk3Z7fd5TrNYMGnyd450u74n4ZX3nQKlbO67KBC-fY-k8fXrZkVPR8HGADmD4BHuFTrNYPZxE2KqfdXt9-2GfLmfFQyhNZ7bj20sd7ZoWzCqvBDEL44FOz8uNSPLM_RDFVsxmFmgII394HEFDQn_45F9zKklPTFA72iPb9pswa8UjYYzraa4s6C4bF3fgw0K3bLyHMAGRQBooe5QVgqnMVDMn7JySs-c1EFFhwV0UZRahJg5VLAEv4EJx9tqEaLzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=YmsG9uQnLyulp7c4TEjRHoiiay4pTqEzs6VTaaHG2_eMayf3kreSacbHb9cB-DcKk5K8CesxyIPN3k19muIfjf6K4co_BwhzcI1QqRaExwjmOybzQx7rQYhcXQvL8oieYPvhg3oP6URiuuo6TGtMQMVOB0mOPE329Sp4FnUugYrOuiSEEyMsFwv2bhmVVFTInnjGYOQBdGNbfLGZjDJK6c9391kt5ALfLnKCCSh7wNqpgzdKrT_ty82A8juOGXiXFi1phzrFzCE5r612vRg5bz3k9wxHtwEcUyq3yKUCKjk6BEqF0dvi72MC1eAMVvzryYIfb2NJy01pFFxKInnVsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=YmsG9uQnLyulp7c4TEjRHoiiay4pTqEzs6VTaaHG2_eMayf3kreSacbHb9cB-DcKk5K8CesxyIPN3k19muIfjf6K4co_BwhzcI1QqRaExwjmOybzQx7rQYhcXQvL8oieYPvhg3oP6URiuuo6TGtMQMVOB0mOPE329Sp4FnUugYrOuiSEEyMsFwv2bhmVVFTInnjGYOQBdGNbfLGZjDJK6c9391kt5ALfLnKCCSh7wNqpgzdKrT_ty82A8juOGXiXFi1phzrFzCE5r612vRg5bz3k9wxHtwEcUyq3yKUCKjk6BEqF0dvi72MC1eAMVvzryYIfb2NJy01pFFxKInnVsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKBeaOIC590sfvSFVjpNksuO00hBbwdPmEMVav5mPYjxQwJD99I_AANmM7kZVnb6oVC8J1TL-erFyEVlgb_j-1Z_MPh_tyOkLBtZSBn20U1fzw7x2KO_NrGfo_3dJlANG15GVybPT6D5aJkVX0QSAhYxzRIU3JYLF_14KoLo9sR6tShBJ0s7yXcbyIwnr4U7XplGkoBkz-SN21vf6NN75Eb93cJbDxk7gPcJQvJ2T8UhpioeEJJD3rqeju6nveAimAunMxEZqjNSl0qHtOnMqA8Aed6pmUSrMF34dMWsti-LrPWR-do-p3Oz_8FL2pvaESVx4yzXHZbnHJvLl3IsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFuhww_fXsMLUg1CVxj7PLmpxHoV6rXfAtLNHLO42rqgx_QXwjtN2prIS0MiWrJM8rPb_awdWRouNKI6AUfntf80Z3fIlAX3ul46e0tMImVBVzTBL978F2dCtIqkvZk45GBKctUCOIFqf0mZWGbG-IXi3e_wNye8d3dVK67dOQOSL0QF22rEn5_OESLge06ZOrfYQJuPT3vY0LuEfrTjABtZh00J66tDjlkXCdrPxTlGv0HaTp_g-OSgAEkH6ccPb3Xau0n24PWcdwVLe7-A6LpePRYvgU9XR4O2Y5y55OLfzMF1KDeDqZAan7lUVQikv9r5hm4_9wQ5FxBbGvXOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=qa_nYGlnv6sEZAYXYYVbOQr-l7dSHPtAyc14ppnn4p8vqPRCseP3JpEwFADilTF0T0Iq5Dn-9EVi_EdMNPkfvOjaouAWSoMsTtS-NBiJzox7wVRqJW4TO_NRPjvFSNfZGENG-vXmRnKlwlfb0w7gyxOeWf7AR8hVnvim5S6PqHZRQ_2Y3kSx3_z2snEUxesjxPnbJOlbkm9H1VAVsle5O060LOHhhg6K3W17WxwMa3mtS4sR39ghwP_BrT-WGaLZUBVzFxclNOef1gIt-_wo3AGeC89hHbnS2et4-P-B5eCyDR-q8PyLC0i8dKucDXTzDMyGA7yktXcthewcm9MaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=qa_nYGlnv6sEZAYXYYVbOQr-l7dSHPtAyc14ppnn4p8vqPRCseP3JpEwFADilTF0T0Iq5Dn-9EVi_EdMNPkfvOjaouAWSoMsTtS-NBiJzox7wVRqJW4TO_NRPjvFSNfZGENG-vXmRnKlwlfb0w7gyxOeWf7AR8hVnvim5S6PqHZRQ_2Y3kSx3_z2snEUxesjxPnbJOlbkm9H1VAVsle5O060LOHhhg6K3W17WxwMa3mtS4sR39ghwP_BrT-WGaLZUBVzFxclNOef1gIt-_wo3AGeC89hHbnS2et4-P-B5eCyDR-q8PyLC0i8dKucDXTzDMyGA7yktXcthewcm9MaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtJCrATrKDc0Q7eIa_8AQ9lynd8MU7jgKvfF41Nx_K2YrnV2JKCj6UWBtJCL9FbSIDwIFYSSxrvvXdKYECbvky-GW2Eig0uX50mPgfApf6YGQkJZKil-Rori6-gSNsAI9jd6X5e7lErqfHVbixs9RVojdksjiFWwRdw3vkwX72zKBrPAk5sFujw84n75yUXbwGz_xnXCnj4mAv7TNZCgjUjHK3LY3YBxAphHTGEQiW9y2VD1P2lJ6JKjATkMtm-o3WDwQlBuczK8C2XEKJchwTqb-gpLktWvJGDGOiODLE7hqTMk5OirQztILVrEL7mJFv_jRoXS8xDUN8gP8AHibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=AdVto72LfI3dtlhefwtOSYemtw96eZ0Wuq-nxXQk_AnbpjLUk2gkXdLOMGf_Rx2Hoj5K_lLwwFGjKDfkLhhEHYn_f-pdRQVWBnCBbY217lgsyZ-uYH7lkC7Xg8fXrt99ZOQIGfJEpi1jjVZJ2Y34KQEJrMxf3PWTcTnNgpSYXhC_xX6I516s6u9VAnFRprFCTMkZgqVCuuLfL8hFf-2lhtOPgB4lzRNpi3QwoP3709Dg3_2bDzmmQLz4PSTnKJuweB421MOTFdQA2Arlcu5Jb9Z6w8FBYCbtSDs4sJ-MH68ukIlNyqhRo36u9Jo0TQxgZYBCK4adVE7MiermsTwEiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=AdVto72LfI3dtlhefwtOSYemtw96eZ0Wuq-nxXQk_AnbpjLUk2gkXdLOMGf_Rx2Hoj5K_lLwwFGjKDfkLhhEHYn_f-pdRQVWBnCBbY217lgsyZ-uYH7lkC7Xg8fXrt99ZOQIGfJEpi1jjVZJ2Y34KQEJrMxf3PWTcTnNgpSYXhC_xX6I516s6u9VAnFRprFCTMkZgqVCuuLfL8hFf-2lhtOPgB4lzRNpi3QwoP3709Dg3_2bDzmmQLz4PSTnKJuweB421MOTFdQA2Arlcu5Jb9Z6w8FBYCbtSDs4sJ-MH68ukIlNyqhRo36u9Jo0TQxgZYBCK4adVE7MiermsTwEiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE4LcwiXk0fYraeegUzwrONz1iNiI-1NyEDMAz_7WSkqv6jwD4CRmMwHSRcMzL4ChIMwa_Z-VH5IRGSY6M7WzpKI9TbITMsiFC1uDmgFR9QOSUIiFr18fYgAr2SzD6cJ6jSCaF-3U4DHyAZyPOTPhMKrjk--fpw5O62gjbEWyODf3RGRPEEc5v_F8V1fH6JMLlK6aBacQKFl6Jk1kloC_opHhG4vLo-QLMwjVpsIq8-JsW2X6XcfBf1X74a2fB8TlQDTqKx1YbrPA1dgotvtHtuKsi6koKIWjsz-VlMqwKUgA7DHUyhCEcM87HRKxK7XpOfXfm4WbJ_azJkLVRoQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx2s0TyZadQuFcG_HJpMCyJBC0lJmrZkCoHkivFDALteK7_hhrfKbIeiFvsgAQzGfIf3ryYv_c5NYQAYNJ-4AstK7yNfDBKuvB9K7UUMg-zt4n4TZ-io0Yq8bdgISxzNZ75CDD0gHL3qHtDtpn0Kc5X68KQV0E1YhSVj-TEwD-vUV5pHGNFGiJjr-e5WAiBpXC--auh_vj5EYJXZAmUKakcL3etpX1A5d9jvfpsfGBeJ1peEMT2znaf1qKCtzw15rXW1ZnNkkco2ZASpl08DM52gpelrV-Mx_JGwKq1nqAPGx15XrZDQD_3UZqid-M_nvuLHxqj9OXmBSKX8RNkdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJcenh6_sOgKw0TugeUCYlL5ykFmdPU4tclmtpaPfMOEtvnx46PRAHPmkq1tv5Ael0yGDaAUWZcdudZHIU2YRChXB0YYwjIgRvxZqL0smp8OeSEZlwppCv9DkUG5_OL2rF7rOrhKeQtM95YPM5pXpNZMjyVMkR3ObYUHrhpelRfUnEEMUtIkPXWvBVkWyhRNNVJfYVj3agMsYvVcEhyW31CCXd5919oCs0wW69iUO7yrkPcTWgzaHmC5FyHloZkCSTW65HSarFgzcgsG7jZREX8nkY6vMiDDO2i9tb8VlqMsUFFf0lTd2nt4dZAQapXFWjuJDSY4FJ6qii0NhvEKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW9o3y04_g0SyT3EczTBMoBqBWdnnF4vnrUCuSNlOtswCQUFzwMIqhRRlhYUEsfSr3y4k0d4t7Y5T3Oy68b2tuOLZInD9Ls1Ucqg5ZSU6blRp_axh8VJn2gO7skmn-g9c4nK33c5aP67G5M9ef8l_jSPNUnu5EgOBLg5IndtUdcUI6y2WpgqKE9QgMnnG3Rj3_noGZcVool09yErU3rbrPbM50ZcxQuZPHfbdG7mve1BAJktq2o70aDjv5xjsKN7WR-YKcgXDfhwywJ3nLvGtubrzybUyHbWdH9zdchybtpJ2nqpawb8skADK3mROYGQuXLH_BqHxT0skGHjnuDi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0_RQNInUMa1vZcWaceDG8IPQXdC97s3ISWMSXRuieUvZCNj4OsTqDpq0SyClgp-4I0-Ce8Bm98kGWwyEuziWKadY7y0_IuiROsGyZXcTd54v9CLG8kCCFPzu2ifZSCd0wEx-7FDHfkEdoYtYNcBe_SuJPIIIvNF0y6ZBaUTTrS7TmTv9ha21yStxskkOZtxYJn9DYcdYpuPHyHXGRK64PVxASMJeIgt0qhhP1zRDKP7wwp842QAmAPcNlFY-iVHye_WPOZ3h_E60Dca3UoCn0K9uOxKtRBhGwXz34jNhTo-TtZ6aIoOVIeSGgN_4VigL7HqVlBkHAaMxYpRZZQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpf2jlEo4_PmdYIh7uD3LLC4Bfi6wPCuIkQrcysCzgPy34NwuIn9sekQHgHLA0Nd7WyXaqoJCSew9hIC049quElqXWVnbtT53d2dE2evLCI_8WidsfhkZfllumSYPGxgmAdRH517QRKsd1iHy-4Eqz48gmbWo_EBhT8cKsBMaQ4DIwQuA2U4DdxEua9Q3gAgTgqDfJb9thq0Vxxdf1fR3bMzDVFtK-W1hCjbBdspP0iYKvz5iiPIsAcKfvp6jZh1e2IeK05cxSWJDrXN5J62mDeXyOQpXfW2f0jmAt8vKE4AsQtY8uJD2nfpPN0kXRGFpKW0SY6Z4JwTTozjDX-fJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrCgDOyjftH8cWwzQYBnNL33Wu8iI9OjshUDQSS4Zj9SFZ1mUjcuAfkDB23-E79QEatVNE02QkNpDNtXri71vGPY1J4vikUflZ3UyLo8ud2qkeX6Gm-G-jB7gkNL6uc1PdEBMbEGsH91IQbdIjRFkcbFyT6AYkx1RY9YoVZxXPMmnn2IQUDE2FF7EYygQapAHZG8ZaQsCx_4GM95yL-2EYVno50orD7rd3p7PBVe50ZGADCM2VmWnVXo3F9lJIA3o0NXsqY2nVg_Vr0XLtKkCvTquOrqeW7zDGCj2DXfp5oqk7jPIjgMIN5QLYi7doJecWZB-KvyfngkEbrjEJcRpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E433M5l6AG-mnxj6ekECC0HxccfuxOIwB04Fdkkr49WVJxGLL1QuWrLCSVGO5rueayMkwPScybmxwp_xQfXSUoOwFhDl640buKe9wv4w3hHCkPzoo5zjgC4Y_SLP-OX7vEJ5d3gglrKOPu9XaSLiueYdK5SqROxa0lAgdWt4JHohxwtMBwYw2IYzqhkXCvgkRRaCNZMl076jpY5n02UuyRm1AVvYTgmYmC256OCaCw9I_8SRWwN76zDWcmZVy9WaoZ0karg7t1bzvkL6ptUC3Rd61AXv1xrgs3Tc22JoqqLb0hJTbtvmrWWrzaCE8rXzFPd9VH6pAv9hsWKr5if4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=i8LL1-DPLdGisKAqCJ8AhdSbiwFRBrmXRwmMCgKtEJ-MkfUuuE3CaklZ16O_Ryb6GPlXNQSXKGp4PbmOjkaPcF2UcWEsq-Fur4rYDxqnYQx8cpBIBKpY5AWfAWx2Icsbs2DxFYJdoI6HLL8ol6hRgBQlpklU39eu06hD_Js4cCWqYQ9Mt5ItYgyUZYT8WVdvgm4rAB6CerC7jsPSWmcM4GlnCehw7dg8SPulXG_zJ1whV9iyomkwIGvzqERxteZaxx-59qFS6d83eIxtko68naV2E2nYuN3MzOL4idWSlKTzRtpITd16qnLL-umsBeNbQ-qsgyY3zrjQyVG6-S6akw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=i8LL1-DPLdGisKAqCJ8AhdSbiwFRBrmXRwmMCgKtEJ-MkfUuuE3CaklZ16O_Ryb6GPlXNQSXKGp4PbmOjkaPcF2UcWEsq-Fur4rYDxqnYQx8cpBIBKpY5AWfAWx2Icsbs2DxFYJdoI6HLL8ol6hRgBQlpklU39eu06hD_Js4cCWqYQ9Mt5ItYgyUZYT8WVdvgm4rAB6CerC7jsPSWmcM4GlnCehw7dg8SPulXG_zJ1whV9iyomkwIGvzqERxteZaxx-59qFS6d83eIxtko68naV2E2nYuN3MzOL4idWSlKTzRtpITd16qnLL-umsBeNbQ-qsgyY3zrjQyVG6-S6akw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDBt99M2yk0Qt3bGiWqNyNhxCdhd8dmxIQ9xxSiA0SQQaxNWbXMn40CAn_40_IcusuIMIQTcM8yQKRWx_QxmP2wmVOR1aQ6KFI7Jsh92R66dGhwgC6zF1IDqqeVnCqleISu29w3JguFZbAWRu9tYy_nKPKDIFalmiHhbP4t35hOmx-YSPXEfcptPoyBfADzCaLSdx7Y2ktUr5LIBp2v_6KF0gDy5pO162h263v-oEF1xgPmvGNk5FGkQAj9TMHjG5Hg21qwWjympgc84DhaNLM5OoRFJ73jWbVfLvCGDKsJUIcjXYyZ3ofgVcCAat5fvdmXNZLY2eKWdeQELLvdggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=kceq3SM2tRuRYN3WeJKF52h2dng36v559wfQ-JazfKHZ3kp1ysKKcH05AYv89O5ro3F1yZx3ew9hYNwSAr8zTvWFfc8eWGP29_c-schzjU51NaXcJ8l09DcpQI7pyf7WdCQ3L4so1z1g3PWK7_rwE3ox7qmqaFsrjoBv_gZl1ZWFgWeQBeHIQKGQHclYWlaQvMSmmawniGOD0VSlP7fc9Ov1fbk-gHmVF_MTQ97eghyQo6sJsJ1fLYrfQebL3vSDnD5TW2UPtj7GtmeGTt9-e-Sq-c4M0sPKXAR-ZZ6xrSvtkj8nyKfXGpJzFjRLPzoL56U7nMtwGtT-GUcQVXDgyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=kceq3SM2tRuRYN3WeJKF52h2dng36v559wfQ-JazfKHZ3kp1ysKKcH05AYv89O5ro3F1yZx3ew9hYNwSAr8zTvWFfc8eWGP29_c-schzjU51NaXcJ8l09DcpQI7pyf7WdCQ3L4so1z1g3PWK7_rwE3ox7qmqaFsrjoBv_gZl1ZWFgWeQBeHIQKGQHclYWlaQvMSmmawniGOD0VSlP7fc9Ov1fbk-gHmVF_MTQ97eghyQo6sJsJ1fLYrfQebL3vSDnD5TW2UPtj7GtmeGTt9-e-Sq-c4M0sPKXAR-ZZ6xrSvtkj8nyKfXGpJzFjRLPzoL56U7nMtwGtT-GUcQVXDgyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=TxZvimVEhPa0Pj3_5vbrPl2UytK5EElHQUOeGKP3jsVEbHGq274jpvN_lL4Wia5XFF724-KbFpS5qobOwcBxnVbx45ETZN9RjhQKz5eP85owGqChJpnDA7cKdr0PZs89o22jAI2kUUk1I-Vz56Tq3DU8_Q9W06SqlDzAIJ4z7HmulCU_3I23HDp4cLv24j1VE_cusSvZo1m-rYd-tDyIW6bzs4hHfRgNw_JLtdIlu-pCsoNO6vvrgrdBvSXPbJx5ONPxl0aOmiZE17UDP6M4zqemTfSJb_wIM7zxPBJflQunTuqUdwYgNbb1JGb3dHc_W9_veVMfx-YQvsvVzUZldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=TxZvimVEhPa0Pj3_5vbrPl2UytK5EElHQUOeGKP3jsVEbHGq274jpvN_lL4Wia5XFF724-KbFpS5qobOwcBxnVbx45ETZN9RjhQKz5eP85owGqChJpnDA7cKdr0PZs89o22jAI2kUUk1I-Vz56Tq3DU8_Q9W06SqlDzAIJ4z7HmulCU_3I23HDp4cLv24j1VE_cusSvZo1m-rYd-tDyIW6bzs4hHfRgNw_JLtdIlu-pCsoNO6vvrgrdBvSXPbJx5ONPxl0aOmiZE17UDP6M4zqemTfSJb_wIM7zxPBJflQunTuqUdwYgNbb1JGb3dHc_W9_veVMfx-YQvsvVzUZldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=kab9WeThtqPVdskP7ZY2VcmkUlypxxtBQkGo47c2IuWJGlHlWjQQ087UzfIHjo_7wzNT-rD5csQahzsfHEsZv6YDNgcWIcDFBFZKw4vfKQrM7FhqQKAlfPIzMqs4OuFASX4Q1NCceww1ya2D3hGvfVOkfvdGS85aVy5DmEWBQ3kktMf7sH2OdnE4pBczISkW1KOijSXnocA0kIhIZZglD-5GoIge7TtIoE_arEkKYYTMOBNBmFYHSx85wgvvvlvA-Wz7ZDO9etQI9ql9oARHjrEGbNNSIfKo659lihaNV9Do1Cvn6Wgq-CEDIh5Gfchw_5qy0za1QED36q9uZffs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=kab9WeThtqPVdskP7ZY2VcmkUlypxxtBQkGo47c2IuWJGlHlWjQQ087UzfIHjo_7wzNT-rD5csQahzsfHEsZv6YDNgcWIcDFBFZKw4vfKQrM7FhqQKAlfPIzMqs4OuFASX4Q1NCceww1ya2D3hGvfVOkfvdGS85aVy5DmEWBQ3kktMf7sH2OdnE4pBczISkW1KOijSXnocA0kIhIZZglD-5GoIge7TtIoE_arEkKYYTMOBNBmFYHSx85wgvvvlvA-Wz7ZDO9etQI9ql9oARHjrEGbNNSIfKo659lihaNV9Do1Cvn6Wgq-CEDIh5Gfchw_5qy0za1QED36q9uZffs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOM_poC3EcBai1OgGDItV6I6P0gEx2RNYIHPgwDFQc7boqnRRbpJO0fBBc9m7rY0iTNWqSwI0HNjXF4MT_HQXJQL0qVy8KDvXApfnMIBDsdB_8-jgwpXDlNf_Qy-88j4KR884kbd7I06bpo-00y4BTkWtvRMStu60N0oN1K_Rh45vE76bOpJ7dVkRbH5PUArxGfVDzzgx4DDZv9QLTV7l-8Zg79EpvN3064XdHjHn9ub5XVhIrAf76sD3EUXdjM9QIYfXuO7v7cLIboyJdGfkSMF410Vp65SaLaTIO00TWBsgh7uAt3KVf3YilyYzrRVWyk7PYzm7y2n_ie5Mrue2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzMsjEz54AZv9pjlR4ZntiSawEXxwXixS-MsqXqrTXUVVDRgcUOfQfTqgiki3Pwr2KWyaOKlzEBOT7GO6BAAGsqhy4IQUrLtVtmxOf5-GIN92QOUYRXtumn3N8YvWVkmUVrZkh5cBZmZn2b7pLAWcbRm8dzlpJwz92WysjCR4FBVqp_62WX6yEvbrs20RQJP8RdNUu6Yx29VQye_9kW8NhOM0XTCvXYQ0S6YcnI5T1G3_7AGfrZgUuGYL2YzLwvDjndzV7oUmztEHXnFvSjT7l5HBtWVuc_FKm_57W6pau8SbeR-7zrLgte0LfRwO8cNoLtSnCaFumBYbo2ty-sQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWqtsIMROTiW4sLFF38ex3hqkNesWL6xQZbTkITsqGjdlL9moa3l0yrNcipOy-QW1KqLAtHsspFMhwM2lh3Ts1Nuk41_PG0F3_tYfz4aMl2PDbi1T3skmwWnUbbdxvcLV0V4hso9MP_8XFf9-o88EzTLNknjnFN3uau15jh2zUQm4jGy7frLKNPxJ5TLx284joXbVwNbx9n4r4_9l7-i3x8ETruhlYno0FwD-NlYrwStHiPJDIJDEAWGunqjbzMdcbHXn9rFf7uTVx7LGL05s2L_HgHpsViUNu3MVR8oA1HL4Fib8Vrg4FvnJ50cgSXDEOkzhdQFig-K3AJbAYHnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDcD0u2MPIUKM0KDSNTv4VjysmGPe9QWv5OCCiJWKNHeAxfgUn2knBeeuw4Jq45T2tY8jfkZIcmdCRO3Xl2IjAlRR6I5Miic0RKc7c5CTYqKdIK62iDzv8aTYi-HSZYa4j362XSzLUg93a7E2hueYvY6oT7NeZ-lJjBtcb7wk6yWV--EqG7bcxr8_UHsrp4lyCrhAGSoaMazLjpQ4YKjmLdhAPBoE0r695QYTeqHQ5KM_mtvO_PujQD2EEuLWNhYS0zi9jODu-wE8lf13vkkvyFjZ1-Za0-WFwYSI_l9AXTA_bRYUDDh-65B8t7AZ-rqbYtqn4qSK7QHMPBKQJVFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Be_Sq_6OcekjNQpxRIHeS_3OuKf1RwIdur6yNDd9SWi6fJZzBhWmwduKrpSeJjDRYDxRE3PXHcsMWabrgKRnB4ERZw6imC3qoJSucf0pS6PcpE2aG3KSYHCvlmfkM7s0X3Z5Iww9HnZPqF3I5j2y3HsyzbfliSxZefReglDmxMIVuAhKLR3kD5WG9Z-y6-HuAPfzzpxvQMXtldv9pFcgv4rsQWK-8phCZn-WeQpFVR5yaaXu3RQ_NJKgmkuvdWqPdzzFgq8tvuOry9RM2yDfAtReMp9cl2E-PkPQCOoEDLfmsflMqA7ssjum-hcy1UH8vadbIkxCSziGkHSEdPOHGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyk-GbPUALlg0Tiz4ui3h2VEBi_15WV4o52eLLCrnwOhj-MVy8uk0-a28pHGIMQPqEZE1Wqvn89tzeX1-Nk9xYLOixJYqv5KHNYm_FRYVoDifJ11N8M61qnsYDOwmYxXZSXsfZeGpRjOUCDKPhbizHgJ1Rt76JOhOfabw5fFZURmWCAp7iLrRiZ4kPzkqoc9ykEOT1UD71ZHD_qZHMWp-9PijmhR12EMQZpKkNWXcDVhQ2PQhZgnb9WOaUn5u0t0MYyDEI0rCgReg88tnQ0RZT0q_aPl4YtIOwURi_nv13aTZUmRY-P2BQXeJCX1oN0VtCJEP5QYO0n3M02SI4hWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=SVwmQ5DxpHWK_ElnIMNXW2O53_1YT8HEBfrQEkn20XRZ4mCj1MVVMkNacY_vCVgwboZaCEdzf3f1TmpVohgppYmDnMyy-mctiy__NVGalldfLnRHd_172j9ulVRMoaxjsWFgbhZGsCmRCHtChSsYsOS1LM1HCTDXl6yGj0z7PwGWryfHepFpjajkNF9OHMOmuRV-6tl6aeuOx0IO-L2fMf0gDvSYP5d317AZgbW62HES7TwYvh9BE7DN_HjB2pI_w3N6Sh0BJEZOSbMCPzU98CmudeAfIvQPOuf8LQUFsB8yF8wl9qqV8vAcEhDxAggEMCqfrfipYsRIfi3Tn6KdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=SVwmQ5DxpHWK_ElnIMNXW2O53_1YT8HEBfrQEkn20XRZ4mCj1MVVMkNacY_vCVgwboZaCEdzf3f1TmpVohgppYmDnMyy-mctiy__NVGalldfLnRHd_172j9ulVRMoaxjsWFgbhZGsCmRCHtChSsYsOS1LM1HCTDXl6yGj0z7PwGWryfHepFpjajkNF9OHMOmuRV-6tl6aeuOx0IO-L2fMf0gDvSYP5d317AZgbW62HES7TwYvh9BE7DN_HjB2pI_w3N6Sh0BJEZOSbMCPzU98CmudeAfIvQPOuf8LQUFsB8yF8wl9qqV8vAcEhDxAggEMCqfrfipYsRIfi3Tn6KdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBPlpisTvHpgonRNMWbcOG0WhOVbW6ua5GzHfTN9QLPgJBSsf8i5YiNw96T5o3cmc7VeNxdFQ2iTeplarayRoJ9WPsa7ebhuruS61ArJo-OqeyeNOKzGx60B5WGo3pgVYtyWdF72vnovbIW25l1oIO2XgvfwQzuJIj5NQom3OqkiIOii1joRn2K1MoonveHfIkI6U5vO4hhaBeyZDNf0Hnfweuusb1PSNZKsBt4seEa3GvRql9sgGc6jyXCf7NdRp1n8gtKb5FOOEAyb7A-j6yQRdhkLsQqY39LI_DlVE4UivJuojJeoFBgGPxdFxH5WZTcJHw1ly6Yp6hUS3mfLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCLyK2ipca-P367c9XZtlBSJuZ2ghLZi8rfNI9nqjMfSIe06m8iLaOL4pmtEtF1WOKqw0SAYrKjpadCF6Uu9rkzXMD6tMPXpqwwsLphPurrIna-CjSHN2RxGE3xTloRpcvWF8soud503m39nZE89HQ5NOneazdPiPN-XGMbdY5SIaI-51LejkJ593NYm_hswS4EssiGGg6lCmZCj6RBntWxZaq2D6p1dJP9tlajEI9FxWmgCV2O07IKoXCosAM0Qvy7vtkrmGgOJUhXkYLdIZpWEN5m7RIbWiIYi2O9BaF3ojV99djEtXB22BeZhdwJ4_lnG4bCJUUx7Yv6LeDwI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMnqYWjg693JbR9XmlTCq_4leKKlf3OIbzeGXZr70OWKSKypawzwFEMrAP_Rwz23nwMRopVEx-jR4bEb80wA4r9FEM_QW28ptwhJl9NY5HOYvWz43SVPR8m7Hb-IES3F0Lz41TCKyC_Odv-8wh8UTg0bEbMQ3Wwg8Ek-2rWRahkbPB2EzUmew22ZQuvJ4um1VMT1kpbH-BBLY2KTCNSvEnQC-HU304s2s7tZtdU8jjWASn2gXAgmjCffOEk39WCeUymNzNpYpW9gzyfRHrLs9jXO1CWqYu-BnhXy8g4HiPADjL3wYmHLh0QIiBUjxzVc1THR3sIyWddJohyyGHUEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGtMMd2o5cbQRvrpiCB07ALRLKsHrLJw0mJVsFn3yCwjKVTyhWKXpIIOTT8sBFngXFGlmJ1aTijwqVW-AQ3xc_J5doZRUCAz7Q3SgvdsmPW9gjXUSRKSoWvYRWmAvk37KkkzqZd6gQqoTpKATDrgsg6lgSakDQex8ijS9UHiIMKN06mAVnNvdWRpws4J1N-rc4KrfNdyJ-RMqofsmUjjPlQ_Isdd4dy7aMYnPR5NAIm6MrsvZUDuI8QYrzW4GYJqHUZICpFu_P67nmT8J_qQSkzyMtayyE_UvXRXGQchaq5toZ8fdRMwfSssWnhTzGlD1_qAZiYewqYGWlXb90Zilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZKkaEaVRDT3eRR_EqbxrwpE-_UG6zyEm4MZTpUgeO1iWJXsqbRi2eNoPpfAIAAHVjvIkV-YiRDMafRgNP1fG9iQ8907j_l_2EQbJezVw_H27bY2CvruN6xAuu4gW1i_27VXC_HJQbgeJuNGbGPwViA-C773uEicBu-Nw9j8ox7jUA5Kg9v_KZGuup3XmlX9FyJvU95PWLFsdDRoHoxxnNG8AyxSX6J1H4FAFjKA8Rccfl26umWZKgCwKGZurBPBOQriLHz_QC5U6FONZe6UbMINvoRwA5L3C9MSJAYXZGG8wHEWBKKyvH8TAUPvES7Wbteiopp3dC5uLCcFDAbE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2IejRxGfjBfBLNAlryefAnVpRY7ZrwU6OwMX1yswoL0qlxlgXuS2Jb-WvAs5J9WXqcBRA-WDdzPkOT6L0XWCqC-f-xPhBuW0wtOxRFbX_LMqObsgZIaawtXcYvOc7dwRKobOPgjBjT9LnJ2CQMTJsDTGVtP1VYZE_ZxUYb-dk6QIcJIuO-fOV6wLXLAwF9b441QORHPtxcunS2gn9VWV8qodNlqalfX1LDRqjdXibXkpw55KiJF4355LfnnIVw9TIpUa1e4HfxWVzF1vc56QXWksUu1rUK5lhOD5-FCSL4yI-qYsUzfc6h1tfocRncypIqMhXTuiYeA2Yd4JBA_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=OkM3aXiyGLFn8ZwFbKqfdvA4-KVvvM2i3neJc2nA2ZdJdLjmj9Q6TBxAQz9bwjuEGZBWqhKgZDk43Ytv_VubK8G9YRjMWXPAtVkfCvspVZCitvZat5t68qxnQrC6FQB-XP1Oo68SZ6AJInvg6uBBFCV-WK-FWKIsHvVU1pt7khlFd5k23H9pFvBn5mnTh5q0BPaUyemXY-y-1-d86exIQHXE8aoaU4Sn0WEoJ5sg4j5pE-RGpAcbeHrReY368MC4tYSrNRrLkxaGUTaN18cXFJTNmu6ZQRtmB_QMCU9_5eeHopc31jQCvG9DzK5lAyWVBqj1y9iYUzwTwnEJ2daTWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=OkM3aXiyGLFn8ZwFbKqfdvA4-KVvvM2i3neJc2nA2ZdJdLjmj9Q6TBxAQz9bwjuEGZBWqhKgZDk43Ytv_VubK8G9YRjMWXPAtVkfCvspVZCitvZat5t68qxnQrC6FQB-XP1Oo68SZ6AJInvg6uBBFCV-WK-FWKIsHvVU1pt7khlFd5k23H9pFvBn5mnTh5q0BPaUyemXY-y-1-d86exIQHXE8aoaU4Sn0WEoJ5sg4j5pE-RGpAcbeHrReY368MC4tYSrNRrLkxaGUTaN18cXFJTNmu6ZQRtmB_QMCU9_5eeHopc31jQCvG9DzK5lAyWVBqj1y9iYUzwTwnEJ2daTWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvn4wJG5_mlI0wdU3H2ClUPy_p3wHacj7wFBfG29noTI-crWPF9T_8TZ4tW12aaPMKozFEaoJY1UQNP79Q_SXrAYFAIboPbro-QSAc_Xr_I5x3TdentnNL2Il6B0Idj6vplbXfAgwPpQUtFcyFfkNeKD9mBqG-3ap50Wk4MJWJ3j2HjgEEafgZIHUWw0hSkCgUQKHwBX6gKLAmkrwdONjkHvgJkYiL7yiy-mcMmItnVKCMni8XerFL0mkVWdoZ8dpKy7R2Vl2_LRIpuP0bhFmZUXWu5e51mNwRNQvZQXwqw_t7VxlWuhOc19Yay8T0ex8VMCbYkZ5py9YH1UW3Aczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P44U2kFoH8bpTmBg3UY7IQwD4IpDH0T8LtaRZJDwagKTALkCseSlTd2IY1AZaV0mf6_zYvB5kFNFNjQAjJ_EC4Ynl6pshlc4e-qFBG6LDf8NyYUAUN8r-jHNJnQeTLU0HMcr57U7_i_caGGisDAVX7u604Slm9sVXT9c-aYTEcFggiAXPIDeS5QHAWBrNOlS5g3NoIe09gWdgZ3uP6FcpdCgZsEieRQpO5KBzK8jUT3iVc0zhYqRzxebOVDUkE-16scfr06vs8v3frHVKQpWLijqxCpLz-VHK0Okq3455MSTwfLkZ51HzXjH0k5ofnIH571TNE7lel0zO44hRyvTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKgy5iI1vjefKQgV7JlLZxx8mY7UlhCGXRGthYvLe1zjRbJ0ZzlHLa7KwWNWnEXqhwhOeN-73PTomQBuUGN0QSTZYO7aY7O8KQXHRmfU-ScJX2fXgWs-CvTpyvDihCvWy6zMdhLbALlFKFIHJ7j5nSVVHvRscJHpB97MA8eiS1IyJBm4Jmw2hgBjjkrXUCOk4ptnJJL8ZEgMk2m8TBut9OE-V2I69NOV3ETXrHR3YGrsqX5-ryr59SfpkIQ8_R0ucgSQxiYysUVb1S-Fv6r4NQrqPtk9cgo5ouaD3SQB6BrOgoamWtDGj_QcH_75BKLhpPVoulFLVyYdxYZ54gPoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=b0bIx41TQNQVeMGKZh95HME2ql2DdKMsD_8r2bHfMJtrQnPgOUKDCU7ZD4ILk-BC4rn803FHZ39XdKdx8LgdwUylFP55h9RwMWUI9q9YAyoxJGK7pjAQ54tCmvjmzMBadGuobIIo39yY2GdXSBH6Ko8z9FQ05cLwWLI_G6U2-p5JWVTyjc_BMES8dAI9JK-3sLr0YwRAYL0gZvbeOx0N1x0wKiEakhcm9r3R5mlz2yjDxT72twqPxnz4QEooXOSf6zsi7kt39MYzqBVggGblzAH4OaoCxd5Gep_5sXk-1WmDi4-i6Wwdm0Wz7fsMCYqPRAfIvehqh_pvW1zHPMXnJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=b0bIx41TQNQVeMGKZh95HME2ql2DdKMsD_8r2bHfMJtrQnPgOUKDCU7ZD4ILk-BC4rn803FHZ39XdKdx8LgdwUylFP55h9RwMWUI9q9YAyoxJGK7pjAQ54tCmvjmzMBadGuobIIo39yY2GdXSBH6Ko8z9FQ05cLwWLI_G6U2-p5JWVTyjc_BMES8dAI9JK-3sLr0YwRAYL0gZvbeOx0N1x0wKiEakhcm9r3R5mlz2yjDxT72twqPxnz4QEooXOSf6zsi7kt39MYzqBVggGblzAH4OaoCxd5Gep_5sXk-1WmDi4-i6Wwdm0Wz7fsMCYqPRAfIvehqh_pvW1zHPMXnJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2ZIXOnefTa46x0KO_f12r5FnK6WEhPFw9tlscso37Ts9YzhOMuAeINDnjiFD6HR6HOy3SXeN7EIRbP2jC7Dv3yutjANHmU9E_J313OSAbBXfxJjoa_goJwlkLwnJV5xtMNr_KaBzvZe9YaLj-sBBGc5k5pVak-nXONbaqIsZ2rhMB3695o4pzbV61_4V7yXk85Kvqy7dwp4m57YBboG3liMrxiUR_Xo0zcwm48ylvBs3bVL7o2eUq2sLmkB2nThDTiAqeOlY9_VOYI3XmtFHhfBLAhE6xKmHnh6FPSsNAZjnsPpedlpnVyfwZkFlSdRbhq2t8L3ZMSdeJ-y_-twiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWsUlHHEUbW_q8vCrNJJmsA_-tNQatDXu7vmPk9IYFGpGm2lREvEmyokwtlpvvv_PQamVvu8GqWBqTmxzkPQ_HQYZKj0_RZxqQLxeL_qKadyTpXTqT5ok7SfxgTSY_3e9U4yTjVQRSVyDuN0Z7NiPhmzTfdumHoXYaeoGG2HxakdvvUblHI7lsmBCK2qxdRiAdkeoRLkT2jBThskdOiJ6AZxejbNlXZLWBgZziuPfYmXSi-kMdI033P9cbqbQVbZo0Z5nz70UZaGtKgLsae4KvrWXoOCZEK510Y5iwm6txaLn_Ojec4LXGWnlEz-AKZ0XW1hl6d30CSTNi7SQPwyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF6eQNgZANsRxCYi0fweT0IjK74-SXlj7eJBwKP6tmHnXcoQKxG9LoVCJG4jfIBK7zVyk65ChimQHKv-AqkVgcxV-xYlJa9Lqc58o3s_JQ-g4sHqvg_yypBaWDIkBiqCTTrhgAqdp7Jv_dwwjbGlGXGYmCK9Go1TbWYp2AGSZJzCTF11jQjKhD-0qvdwT4HrFyREfYW2EodvlRXIvzMfSSssAo2uXX2yfwfVOyOpGLEiNHqRfFkLL-PUyAvHMgXhjA3iPiHdURHUF2fTjk8ANLKhGrIUiWjMHoEkp_0r4REqmXq8Qp85WzuHVZR4REAipD2uPfo1VA3s6b-A1cZ-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcbd9eWK1IqkG-WpiN5aB-hM2RR_33w68nVKEKz7bvblsoGe7rZZyke4e8R0niid1VdoECY5SBp1DxWsHMxUz_ailOSxMRf-_pvZTGCMW2y4FgjsM7uabBLjrkx-oylrk9WuwFl21G3HZ0QwpWzjhB59f1VEAq48J8LvXfGEIqj9-MFvDqDkUvey2wotkRbpCU9X7HKUXIsw5Ih0IxsybjKxdhPoc7R3NCAc63-NPaW3q5zH2QvJ-ya6SM8itCgd8eEQAugT3-Gah5u0yRv0Zwsjfpt07tkG9V8ETtPxeR14gz-rlthDZzgNTaKIOmtFO3WPAu_LJLmxn5AQRzsxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4PKfUiVyxEPHzxnDEUiNygF7ts6iGlOC0D5FNsA9v4SHq4Fm2CJk9i1jgg8S3uaHJbwrXU3WPSBRZRcg60iQjdr4DSspMpEhZlEEiICG1chwsdJ1_ENcREuH67hlXD6_1E-8UiSnBd9dH7QTjR6Cb_iVcE3UcMADQ2igxoYkyFdqlWp0PoYn-qJvmWINbUw-ycAXcospMjHaeboxUT3iVM5lVZ9aypQT71i8BHIttcrXgzGQITSd8mlT3pRnvw8GPETnhYgdWD8RU409CeSD00YaQNA0BARh8eOgoib2RbNAvlZyWBG2IeRTIGXuJ1MexvIbEDV4BqAwSjlAT2y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgdPDhBsnCIkpxHLPD5nTAVep7CcR5J-u7CskPR7Jx-UGrkPVKZZXZkz-34fokIjdFYwZLfO6nvetgV_680Sxw8EbvBUl_k-knbCa7eiCFKjsPekIIe2CP6W-5QuIU9dXRtDjr0Qx3fByk30-62iFREviRGSCE_9fdWUtm3tvb12pVV3hh4KastSRGU7e0J0_xKYUwSyfFBTrgQ8X2u3Mt1R1ZAe1-uTlVybnwog5xkeUAC-hyzxKCK88Ws7bjNEGcFHPTVk1huZyWwuTRQCQb8r9WwvwLyouza0GZ36aC7AiQROIilPPEv8Kf5EqPkwfjchHLbWgV0z905oqoczxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=MbWvZ-u7lA2s8jHYWhxVdci6a4BgRSkasnSvS4hFWvXejXgNyLPU7o1sYhrBvCjmYxKUM5CUCe_AlBJDirvUth_xju1k4gT-tmLpGum498cZeGCE-Osvo0on_v8dE0zqX9SQyhj077LrUfGCeW_FTotmtN7Q0FK04abl0GXP5d3ckVEN4svfiCMenpDHq5h-CePWTnBpXYiKQ4baZTy2jO_2kQ8Xa61KheGQ1LMC_ZxXpZM5U6foxPvTEOEVJmEMl5CLiMPVN4bCrChAZePU_KfKbWPHM4CReb8xVNh4gMX7WT0VGdB90iizvfguzovZzSxWtjTP48C6nxQWhT_Bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=MbWvZ-u7lA2s8jHYWhxVdci6a4BgRSkasnSvS4hFWvXejXgNyLPU7o1sYhrBvCjmYxKUM5CUCe_AlBJDirvUth_xju1k4gT-tmLpGum498cZeGCE-Osvo0on_v8dE0zqX9SQyhj077LrUfGCeW_FTotmtN7Q0FK04abl0GXP5d3ckVEN4svfiCMenpDHq5h-CePWTnBpXYiKQ4baZTy2jO_2kQ8Xa61KheGQ1LMC_ZxXpZM5U6foxPvTEOEVJmEMl5CLiMPVN4bCrChAZePU_KfKbWPHM4CReb8xVNh4gMX7WT0VGdB90iizvfguzovZzSxWtjTP48C6nxQWhT_Bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_EaQoM-5YU2dukIGImqclhDgC2Rcoc5alNRsQfrMI4e6oCYSbW6khMZOT6_aWMpHYmvybdB-tLUeoT2dGVCaEUJkFTZ80IL12MV61iL--j3uM1834et7nqfluap8UxBRfu6w3A1tkC8OsdksXvWbb_lX06oxJpHzGBppD9K4RJptQ4oW2rLc0G-fBHl6BI99UvY5n-FqPmoJsQid2i6GWC4W7HaT2_AlhJgtv0-pNgXJB0jKu4RUckAUeEPU8u6hZVAstEQHxIEd6WT_jcz5wKbPAsimWFAm1SWQZC9JSaScg8iOVjvq7joFMkBLoaNcM3X59-n8Cddkn-qcadEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
