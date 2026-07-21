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
<img src="https://cdn4.telesco.pe/file/EPGMXoQXrC5-5zhiPjRnRPVhKyYXdgUulr1Kg31fkBaIE_ko5ovv-ODSrSomEqmS7THtdKPpyVPFlnR_VdcBguP7wo80E4HU1aIFu7kfMHwDhLJg6Yg3Sy3B-OGj_r9Kg6e_RITf5xalzLvvgojXaf9o9Q33rfiqxT2Yn6VFfcDRZayd4d1YjTPv0Irsn-ZjxgOKcCfgIvAYRaTmcdBJ8gmgb6EOqfXFsNalBYIIRN9IGB3Y8eb6qiLZ4iJrc6mq7Ge_cOSlEnKWwUWghcA7SakPR92ZJfY2Po7Gc5vm_71ug_f4jHYMfip22aNOAkpShy5pa-Nmn5LXSAD51nhnMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-136360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffxZQvHMpaCPVwJ0gZlP6uP3CwohlhksnPp77ogL8UvLl9WydNc8xBeeK56aWJkV5at-CEvGO52f5tpXwcyp5lvB9Es9OELmEQZwTYdk6pPIVtOZgb8h1Nh08L4WO5OJczVM9knmxlOiKvSqrMjVcLoY0vo0KgEgYUmjmrHWb0_Ifpt650AJ3_AhxCjDvNv4yo5L0DkortD_JwLyLXynICJ8fcJi9xPqtiOWsLpPKfifmFXwy359z3gWAlLVCnKjN-Ok3AoaildiMRD4oiHS0fi3YLpYD49iyYgM3beXCXjJyOkrkMYJxMblzswb6iNpzskXqll5U6XDNE5BXpcGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCd22JOGrBrOqDuL1hHYJ2dqG85t4siW-5Q2_GZziqimCCQdZKXIGCPV53s-23Zw3V-9Hjnd-i51kBWJtbf86LX_0uiTGFaEtra-J6loEnvDnaNVUxDZ0Y0XOcXmuBME67WgzsnNIvt30eaRq9jsDCdE_dfQusYWVsxbJE2tkfJWLFvj_cfy7-Xg88CvA-GBk-8rGmvC2_K9hLnUztUbMN0SxDa4Ap2jIg0zFRyuMKzGzCvU7XRu9AA5JTYg28SlFqua_is1b9PQ0wXwNCSNJrf_bHnlQeL_Mc-gPk9ts2DW_e5If9X2sXGhbXLxZLp-GBIMRhHhZVXcygSkaneT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWXFi961zts7IljDmWNQ1M7kFMmnw7Ynd9n8KnzITjF8MwEEG6jIACrX2JVAdHzk3_SEZHH6BW9yT5b6veNLdW1qHepylQDbsxgyKHRTGFLtbl4rP7klCwAIg3UItv11QrVmOvTePWIgYJuBzcPS0umXOkpw3aDtteig8G0YUAV_YKVaJpTzeCvEVEIDl1AQwiiWumClsinICeg6zwzSHcpkSvQD_anhDkxklvnkMn6KH1mA7M-7F3fxMHTBHMA3St2iu1yduEBC6nlHQhJnZxMupry2PAmu0Fcln4PmtbVPEoMnJRx6N0UHwTt5RNUUgEM82KBY49FTjLnOyCZcVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d35a2500.mp4?token=UGa5FT9Az9-pM5SYoRjkmJkeG4iO2vc-GhF_qTwjvRrn5Z18ixKG8XVMiNiKEodGg3P0xzKFvVkKrmfLcLGogpB_cHZB-RNJvyg-5M5eQebdUN_GaHsvASjeds2rxhyj4x3GpW424IRv1Wpw7Zn2E9W0xFe_tOT2TMb-iTTPljdB5aR2Q2Co66YiB0rwUMnBYbtjsAunbNbYGhWSxmVVQvLoPLMc6kfUBlMZfvHRg1FBrV5HoRMhswlPxHllm4PBmU-ndn7UEt3ijxgwdDStQ5eADWYMQyudTO8xpcjzwAJLyVNhRKCDzwNUxePeJzrfeoLzyHFmlea9_xDv6gPnUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d35a2500.mp4?token=UGa5FT9Az9-pM5SYoRjkmJkeG4iO2vc-GhF_qTwjvRrn5Z18ixKG8XVMiNiKEodGg3P0xzKFvVkKrmfLcLGogpB_cHZB-RNJvyg-5M5eQebdUN_GaHsvASjeds2rxhyj4x3GpW424IRv1Wpw7Zn2E9W0xFe_tOT2TMb-iTTPljdB5aR2Q2Co66YiB0rwUMnBYbtjsAunbNbYGhWSxmVVQvLoPLMc6kfUBlMZfvHRg1FBrV5HoRMhswlPxHllm4PBmU-ndn7UEt3ijxgwdDStQ5eADWYMQyudTO8xpcjzwAJLyVNhRKCDzwNUxePeJzrfeoLzyHFmlea9_xDv6gPnUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای حمله موشکی ایران به یکی از پایگاه‌های نظامی آمریکا در منطقه، که توسط سربازان آمریکایی فیلم‌برداری شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/136360" target="_blank">📅 15:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136359" target="_blank">📅 15:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/136358" target="_blank">📅 15:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIa1wRj212wu3Mx7-I9Tq2JttsJENMbQxMpLCG0xqXSTG9L2A_ePtjZHZIK9J8dW6iMkgV0jDl9uuxloGn0CrOEJ94-r7WVShlbtFdyNyw6zz7prAqP6B_xGDl215wS4SZKZGN3abuGlWJ4dJIbw8u3Aq3aBP3LiC7b3dJlhUTI9bD4Phr5kIg6nOP1qsFSnEOBK85IaM7puys1cRTi8WA2vKVrzSddnGMvvu8ZEhQZ4Yd740Mw3xovUBcyer63T1T7RB_rR4fvQn-2Q3DQAEjvRicvHh2Jp6zVJ9-ArmEN8hSXMJSHFNwPKGC5_NbyD5HWeW_pzNiMuW5W81FIn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای چهارمین روز پیاپی به تاسیسات برق و آب کویت حمله شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/136357" target="_blank">📅 15:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzAeZkT7edqUafwVPuBZBsJY_qQ6GXA0xHNaV9dwpkJxNq3gAdeKuZ2CnGiFRysO1AbTqtdrRlWn7FpabEf5RJyZxGvZS88M1vsjtyPJh25rS6w5pQjgtZjD8LIVJ1QBwUOZLrq2pPy7OjCSLRAqKsN9bqd4XvWk_LRe0lnPSmLBy-vYQkPgZAj0DC5zpN53hluCzYf5l2hbm5ttzfLb1X4oYEMNh2jMyStPHhNb4dgLkVCmfE0usg-qYkLwBpy3bjaKYvcTIYHgLLVKj1waNOMkKxVinnO7EqbYDM_65LS2n-4A9FQjiaxUdFAlhg7SJl9J-Hgq9vXxM8FX_MiBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور با نخست‌وزیر پاکستان دیدار کرد
🔴
مومنی در اولین جلسه کاری در اسلام آباد با فیلد مارشال عاصم منیر، فرمانده ارتش و رئیس نیروهای دفاعی پاکستان، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/136354" target="_blank">📅 15:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: تهدیدات امنیتی در تنگه باب‌المندب بر نگرانی بازارهای جهانی افزوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136353" target="_blank">📅 15:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqT0TpFwJ3Daw5w0A8Gdupya16tALUNV7-WUi9nehBFGOSarPT1TtRzjssxQBvhGZG2b3Dp1VMbjarBgNL1b1locKZwS-ih8SEj-RODnmIjtTl1P_JYxv9BW99HYF9mvlc3AaRHCiiThlAXC4ph3_lo49Bf0OcrVA3-kLmIoAGu2gbBOpZcNsSoTk_IiSeEIdpqy3LxMWp9td89U0Uv1Ps0MrgdrAHiEuc8R4xgdSyR0SVZtgmnsq0k2DnSVartmErnYuFS9g9ATGY8a8iDNUHuYRDCV3yu4GBjI68bQxZ07kWrZMHbtPoOyk-NedktfYLrTbSBuUxB4Ee4ouQKlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده مجری صدا و سیما:
عراقچی در زمینه مذاکره خودسری کرده است!/ عراقچی بدون هماهنگی با تهران به آمریکایی‌ها قول دالانِ جدید کشتی‌رانی در تنگه هرمز را داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136352" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jbFHSo-_vQUJSKmp1P1qOfgrt-07li6wVoAqMA3u6uuO06laVUoJkDGz7J269cJngTGObbCR2jhGWD5_9V6rgSW2yeftaKKON8eS_LToWCD2GFdhrXfHJJI5JkyJOQXeKAxg7BxqdtmvhWxLjBggLB0nEy9uuYlG448cp29MJ-MPAwPEpiNMmeFUP8AR9eF36Mci7lGHi6vlOMUQg99V3E24WQdWlAVHrI4ZAASFPBxPVlR9ewLpL0sRwEkIvIPJqSs_JfIeNS7w83wD6QsahuW1_xPNvTyjw1o3MVzLhnwCaEx_O6jxONQicW_9xTIw3-qmMhSEPhFnuG8KYGOGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته: با این مملکت درس خوندن جواب نمیده.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/136351" target="_blank">📅 14:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daef934e1e.mp4?token=HcnA5-8XlBcXw81q_593P548U-JAbzVIhvRqmlzrWZ6q6fN8Uzul56w6Qlm67lJDb1P6VkM-e0_wosvyfnnwKPwPH1EKb46s7BMdK7vTju3VBdjfekTZAX5yh0Y-KqAPJeDwgen8wQjBk7_I2-l1h6TR0eaa0-kjiYC_Bu51Ix51a0BbUSACi4jlAUI4eUGMBaKeyiII3eK9x0RRwV7ebBU9mhpq9EMZ1dRE9X4V3ATkqM7qzECqhjHzf06VeurZd0tOfiria_qjB3Av6KsYdy3K6uqFL6fm_kzBYzwyeJ3WXuwTk1s_J87pj76uZwVZz8MVYmM9cnut-WaHPDBifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daef934e1e.mp4?token=HcnA5-8XlBcXw81q_593P548U-JAbzVIhvRqmlzrWZ6q6fN8Uzul56w6Qlm67lJDb1P6VkM-e0_wosvyfnnwKPwPH1EKb46s7BMdK7vTju3VBdjfekTZAX5yh0Y-KqAPJeDwgen8wQjBk7_I2-l1h6TR0eaa0-kjiYC_Bu51Ix51a0BbUSACi4jlAUI4eUGMBaKeyiII3eK9x0RRwV7ebBU9mhpq9EMZ1dRE9X4V3ATkqM7qzECqhjHzf06VeurZd0tOfiria_qjB3Av6KsYdy3K6uqFL6fm_kzBYzwyeJ3WXuwTk1s_J87pj76uZwVZz8MVYmM9cnut-WaHPDBifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی‌های دقیق ۱سال قبل مطهرنیا از وضعیت آینده، تنها یک موردش مونده!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136350" target="_blank">📅 14:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXhoCyFPIv7vH9w9nAiqDIa93hL6bkwL3LT9DZXoY08arQOMxU7sKHekeLw0AZWTBMP02B7fsajLDOR6KdaatVYAM8eVXPXhV6baORrmfTLHsGviqPQBjffM-ZosXymJLDvPCwszjsW2qsm4mffTOxlyvgnKQ-PIJHv8MmnTi-ePS1bP46shtFdCft4YZDwP-dZa4yl63rAT8biYaVK0LPx1JJ5UXZLo3Od4j3-TNlgjOYdhUCf2LJObs1LzmaZvFmOj06Q65r4-HI38kT-qZbW5sVFWzJlzKKQUSRi-sDwIa1vx5r_ZaW8FGgkW0pGTs9FjB2unjcLCwbpuuP2qVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان :
ارتباط ما با آقا مجتبی خامنه‌ای، روز به روز بیشتر میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136349" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzdc_GFM83BrwOvYl-cMbjnKWyjipZz_3mDW5Xc8KeMVAdisObs-2BKMg6NPhbEe7VURymWl4cqSalSCOwUUN896xDinnNGnE5r4yuAo0vjpa-2znLc2G0rY-MnbN92mP8PwXAxTIe9WNzRNFWnvkVDpVLvcFF9mkNaK7ewRiWyoYQpItnti7Zo6nICAmOodI5c4AMXS797v45_0LD5_vSoskaKOhpp1WtGDz5TaUm3NpYPRV5bcx0OVZ3ItmfpCV1g-Rg-j3iP2XsPeA3KlE1VwI-fA-ONGxX6hBLlk4dO75L_Efc0qdHCEvfFwRSJAlQnXU-Vj0y_cB_6Bn6jnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136348" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgP76TCPAcFAC5aMvOnDj48YN2O1hiDO-hlxU2HXVSzyW7MBRFKBs039bJcxtfrk04KJkkEvhiDuQNdaMcQymZJy9kZ_xaeAkfSogYkVif-7g9qWcuHODpIbuHOG1fGbAW-231L5p7EHyUSAv_lexRld_vbKDxP5u5QXd2W3f3RqLWhfhVWB8fHYe8jxwUANE6GGqogei_RI25jnHo_UL7M24OHsLzyDEoWSzcuNt67UyBJsHaaG4yIfaQTmt1o5Fxrhq0p2tvYQYbyVX4SGWr7WxuJU93tXhNJxXKTb42eE5pVjr4tcskORVm1IuFRdcJRQvOgl0eIHeNMQC-KMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی از اسلام آباد داره میاد سمت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136347" target="_blank">📅 14:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNQ-QVKlbT-lOyWVKwfBxuAqHqA9SF389ugGGQyQUDDwo1bwPsvywodwT4VPehhpvEq3n60t2vP8rJT70CbF9nAOzMXMMfkLDNR5x1shPQunVbctBjaPUHxZT7LkkljHy1pxREnvAqNlnqVvgLN_KUKqt4NFbx2klX83sqBP6nXPmJBSS6u-iVgZCUzyurhLfzKg_Mrzf68x-A5fYFwlkJKvLNjVvJY7vwH2Itnj5aQRDWBATTkgZkpst0ghUfI2IzbhPjR8W4qEALyvil2-4qdqKzRd44PIPNVyPBo7tjtNrSTX-aOE6rwB01SVRoX7nSg1pz42J-U9bUQafGHLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مراد ویسی، عباس عراقچی رو فالو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136346" target="_blank">📅 14:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLeUxi9ZW3iDbSyjxorWxFPc_ZArygz6a15wew1NVnOi1rgtlOmHXUD8fjlAqxqnlTt0fQHdkl8FRV642dWPu8sgTxkt8hwKz-mb9G6bHNiHQvkaGZTXNsPS38nKUxSGre6kbSeR9A21SCLxmimd9PmGrZjjdwGXC_6KVYotuVBuzKYmL_o7PBD_cnatgsukc5vTzawk9LTNhtHJ6U8YniKnfxd-JQ7FQwrr-XqSAVaHU4BY36Kuzf7sTAG09tU9VkxWq8QBkDHpp_q0yURWj7O8P7_xRB5zAcmRs3dAi1XqeKMkeZgpnP6rdQUZcH0c9uVRusOMRHidxd3FVXecFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
این افتخار آفرینی فقط بخاطر من نیست، یه گروه آنالیزور و نخبه داشتیم و این یه افتخار تیمیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136345" target="_blank">📅 14:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjqgF5SE0i1RVGj7dU0HpwtmOfpj-U6U2zOA8cUGyWUFY6Z1yrBIOptdh0yXX4Gn1xUrq8-GA4qUvY-qpHBMSJ5PC8flaqMCvzLA1due9KyrL0F3rYn1uY0K5D0bPIGPtxeNU45cP_vozXabvzRGgW_MWbelsJHCJwyrKug8fqKYq67Qr6JyNm6N8EkCSo-oaKBcyIev3Qo6Q1j6UWWY0V4ss8RXX4HrFF6nJxBnvP_gpMiovPq2BZa6skqBgCT00U_hPv6Ta-20NARLaEiAGA0jn6v3Lot2HT0I3J0p7jvE-NQs0fcfmIwbOS6VFiUxX8N4d5olhb5jPLfZA8EmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLI9Nb1-CownyJPLjS1fhfn80IQ9xwXekD7nV6Gq5RppXZWqBBFBsOrK0N_D0KMU5ocqfVeOPOrn1bFazzLu-CeckWG0UKzCy0yrOc32no6FURPmXlpgw_C_Uka30Dl8gFT7dpjMQgX8xHdVQ46kr0iDHF27KT9b_r81o1ZtkMf7MgsVuHIWvJ9u3YHXL8tsjWRFOzys_oI6F6f6zIH75hfWvv3A9XvFqGubrvshTW2djMvH1cY9rqWYlAVGVvva0of_u2p4RGBnDVfgD8seDe3DQww5hzUxAUp4aJG1wibmJ0xBuPC3wu4qi93iKG6c0FGJ76hEvZ2ue2kdfWlNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWs7bDWVyr4zb7hvsvKh1-w57S2SUT2OKiF-HJ6V4dxs1nO6hfEGfZbQO4ZCMEHT_TgrcPyZ45ChT2AvObKNA1DWYYeiYmAWlxBnB1vYbavETbIDr_JuDwWS6HZE8_QwFDpIzwE3GjYdJjZj_M7csU1offkcINkP6Un_nFcdGMGhVl63PHPnkujv7-HZL3P1q8xtNbv5k2VoXs7GLjIf-L6pX8aMp9Qz8hKd8SCUJcZsILPPfU8nBGXeR2v2ROPM9h9YQRD5lxIUt4MbN3LAefa69EEW34ZKtrKrwjWJEIrhwm3rlasg2VjT-WQkwFUW-PCkO24lXqvB8JC_SJ4txA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید سنتینل، آثار اصابت حداقل یک موشک به مرکز عملیات ویژۀ سنتکام در اردن را نشان می‌دهند (تصویر سوم نمای با کیفیت این مرکز قبل از اصابت است)
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136342" target="_blank">📅 14:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فایننشال تایمز: ترامپ ممکن است آخر این هفته تعرفه های جدیدی بر ده ها کشور اعمال کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136341" target="_blank">📅 14:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136340">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d4790891.mp4?token=MjF1QrE9tusGbDjOhzf2khcJbfwoarrFP-efUxBMI-rbsYVpc8A9TCk6ohkx7sMetMGD1T4UsIUuUZ8j8CCltiBJKBerLji-zxBYXLzJkiwjlGUp4etko1Wviyr62KsWiQVUAznfpHMdL8R4RkpRC5VxzJt6kZM2cra1QT5Re66xUOcfHyiNrSwRKDj7qN4yZea-5KSQloJOaXom3Q02fnyx_1QYVbd6ZmhZkp5sG_CfrlGXPNaqhTnXHBD0cVprCchQas-nn3Zhq6_ZCQkJM5NYZpw022BKS88C3zFPlvUrXf4Yesd01NBO4x-mCL1DlAAd8etP-I9JvG-UWzzWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d4790891.mp4?token=MjF1QrE9tusGbDjOhzf2khcJbfwoarrFP-efUxBMI-rbsYVpc8A9TCk6ohkx7sMetMGD1T4UsIUuUZ8j8CCltiBJKBerLji-zxBYXLzJkiwjlGUp4etko1Wviyr62KsWiQVUAznfpHMdL8R4RkpRC5VxzJt6kZM2cra1QT5Re66xUOcfHyiNrSwRKDj7qN4yZea-5KSQloJOaXom3Q02fnyx_1QYVbd6ZmhZkp5sG_CfrlGXPNaqhTnXHBD0cVprCchQas-nn3Zhq6_ZCQkJM5NYZpw022BKS88C3zFPlvUrXf4Yesd01NBO4x-mCL1DlAAd8etP-I9JvG-UWzzWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بمال بمال در تنگه دار، شمال
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136340" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9CQ4cmDaBYoLXZfXU7pP0zP14kSVTwjoDlOHvbQnROU08OUQg7Sd0X_ULj-P1UYvCqoOZBp0k7zvYocNUzbxTlw-ZQxnPl4RzktnPJN2GTg8kC7nL_AnHGav19CPFPM6CO4nqRL5qZZLPu5yHvvtzKURTzuIRTN5ml2c4Miv7RUCNwJfkaMJ9WxZAutRXfPSiLMk5dUBlWLYuxbSEzf2qTLaYt5y4oQOImKJY4-ayBLt8PQDxrPt5ZfWiHebIUslWZdIlJgStvOS_P6O5UAUKf8rXp9PWgNIGrmYr6Q6FzQJC8XjPKY9HwKp8pihQLTLRabfRjuIIAnvmdcxb5afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای دیگر متعلق به بخش انتقال پزشکی، انتقال سربازان مجروح آمریکایی را از اردن به آلمان تکمیل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136339" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136338" target="_blank">📅 14:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230d24ae4d.mp4?token=T2-cgFFIWMkIH-h2U-sVxyMp9bYxIQUkyNHUiQSVezDDZKPPuq26C-pb2AEzENleUztNoksnKrhVZkMoGoRNXCfoJAfDvL3X640iR1ajmPeRZ--th--tjZYJi3zPQzwSFg_ZvIIhpdX5RrGiUIHgOdTQWIq1LErcKrVJTyhnM7k4n68PJctBpj-HapexLbboxqgqGwpE5Zd8LihDCStb7LsPR9yq71K1j0lMRCJnoyDw20og4MXN1vlkTIUjykFVKMK8Uf7Z3QmkR7GjdNVEpCO7Rkmh9M0M7dhpLXRhwV1QF4qgMu3lU0LkJBUSn8WiEoUshb0fOn2VsQ0by1Ih3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230d24ae4d.mp4?token=T2-cgFFIWMkIH-h2U-sVxyMp9bYxIQUkyNHUiQSVezDDZKPPuq26C-pb2AEzENleUztNoksnKrhVZkMoGoRNXCfoJAfDvL3X640iR1ajmPeRZ--th--tjZYJi3zPQzwSFg_ZvIIhpdX5RrGiUIHgOdTQWIq1LErcKrVJTyhnM7k4n68PJctBpj-HapexLbboxqgqGwpE5Zd8LihDCStb7LsPR9yq71K1j0lMRCJnoyDw20og4MXN1vlkTIUjykFVKMK8Uf7Z3QmkR7GjdNVEpCO7Rkmh9M0M7dhpLXRhwV1QF4qgMu3lU0LkJBUSn8WiEoUshb0fOn2VsQ0by1Ih3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمزه صفوی از توهمات مسئولان کصخول و جنگ طلب
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136337" target="_blank">📅 13:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136336">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a820c8571.mp4?token=h1ZV-7C-5S64USaMYZvDGSqr28NZQcBVnoGXdlrDqSsAX0_7g-S2_AYnHqO5OE7JHxVgNzymRJLKsKWAhjxCngnT8vil0sG7wA2bILAeK_0RCcT_q5jm3wWPs-8gafP622SGxx4xhqpISmKjYALdnSzXtbOQeVGabzZWnfWtenXxFvpDSL1P95_ICh-LRXlVtjqjl0RHakbT81fTF8Oh3Gd8gBNsZUH42Zf1QOd0mYemp50K0Gqu-wjLVkiMrjY-4Lck2Cns8amnNhFiGAx8FVSeVGijWDxZWyPuzlrZSeP2QsaW9PfLpl8rEd9bJ7bg2Zkku2aFYQad8t4hd7loWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a820c8571.mp4?token=h1ZV-7C-5S64USaMYZvDGSqr28NZQcBVnoGXdlrDqSsAX0_7g-S2_AYnHqO5OE7JHxVgNzymRJLKsKWAhjxCngnT8vil0sG7wA2bILAeK_0RCcT_q5jm3wWPs-8gafP622SGxx4xhqpISmKjYALdnSzXtbOQeVGabzZWnfWtenXxFvpDSL1P95_ICh-LRXlVtjqjl0RHakbT81fTF8Oh3Gd8gBNsZUH42Zf1QOd0mYemp50K0Gqu-wjLVkiMrjY-4Lck2Cns8amnNhFiGAx8FVSeVGijWDxZWyPuzlrZSeP2QsaW9PfLpl8rEd9bJ7bg2Zkku2aFYQad8t4hd7loWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد اوکراینی مدل FP-2 با برد متوسط، به کامیون‌هایی که در ایستگاه بازرسی چونخار در کریمه صف کشیده بودند، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136336" target="_blank">📅 13:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ آمریکا و ایران در حال ورود به مرحله پیچیده‌تری است
🔴
روزنامه فایننشال تایمز نوشت: جنگ میان ایران و آمریکا وارد مرحله‌ای پیچیده شده است و ترامپ در یک بن‌بست راهبردی گیر کرده است.
🔴
محافل امنیتی آمریکا در تعیین اهداف جنگ متواضع‌تر شده‌اند؛ یعنی به جای صحبت از دستیابی به پیروزی قاطع، بر بازگشایی تنگه هرمز و بازگرداندن محدودیت‌های هسته‌ای به سطح دوران اوباما تمرکز کرده‌اند، ولی حتی در مورد امکان دستیابی به این دو هدف نیز تردید وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136335" target="_blank">📅 13:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پولیتیکو: دموکرات‌ها به دنبال توقف حملات آمریکا به ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136334" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: برخی اظهارات در داخل، دستاوردهای ما در مذاکرات را کم‌اهمیت جلوه می‌دهد و نباید با اظهارنظرهای نسنجیده، زحمات ما نادیده گرفته شود.
🔴
در یادداشت تفاهم، ما بر باز شدن تنگه هرمز به روی صادرات نفت تمرکز کردیم، اما طرف مقابل این موضوع را نقض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136333" target="_blank">📅 13:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136332">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / حمله به ارتفاعات خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136332" target="_blank">📅 13:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fd9fe95e.mp4?token=dg_16yIznzxaZRgT4s8854cNC6RSNfuKeo9RofERsct8x-bNeI84BzkgERO6KfRs78u8HRvLpgtRG-IHMet6nk9-8HRJ_Ues16UQTY9ieOD4eOpSMQzB3hsiBlgevvnK-KF6zgZ3aL91ovVGWiUuNy8q0ny5TKlsJdnKL5hXSQQ1OZ6C9Uo2peM88Ong5PH37XYCVJM8DVqUavuMWp91RgXzZ-GbsGDBz9GQLaUS765us41rDwTOd51wbmJe0IdHO5VPxXQkEH4fUwg9DyYR2kNeO9yD1vTNaBtSDmHSxFN6cfpCcc-2rN804d_iH91En2RVUct0iH7xMSFW1AkOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته
VS.
دانش آموزی که ۰/۷۵ گرفته
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136331" target="_blank">📅 13:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0_4zQofpDfbKKDtVluutA9vXHy1Bwq2OzEligkn1mHU3XHst9Uw82nbqgwUgsVAu6N3PK2k0YMYDWpNSEiY2natRzmzx9W6cqADmhZ0qj1yR7s8SapMQfMV20GYYUa_GOZCOPu69dQxN39uTGeFOJO0K8JDzvNTdQRHaQiikHcwKG4RyR7HIGL0fDtNChJWsILAHr-yLaBbv2ExFH6VTQzE7FIZBLxZkhN_uWJKM5cRxkL3mpdKnEDjAQEBPIbGayC8ez9kdJG_bAc-sraq8jKvNxwMt3UUvjeAlARnRl5_4l06DP2lWAV8Kd2Lq5VlW98vqDThM4KlYkKCWwl3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنین مشاهده شده است که یک عملیات نظارتی و جاسوسی مستمر توسط آمریکا، که از عربستان سعودی آغاز شده، به سمت قطر در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/136330" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkG6apNAVkgLfFIk25W50Sfy-8_IvVgA3p4WwppAm0I_2qWefKlNGRjmUG-i5O-CNLnQshU-oM4f0uo9bhHx2m-IQHVZCrFk1XU2PE8VpTLeTkMPfdQmZXl4akqiai02P9imH51lbH5hfcednMSBTEUUq6FIszihRrWsy7L9Vbg2RcSHftZsrEFJl7ueFozYOd_9WWTQyoI76THnAdQ3hzoReccLtaTTKeSrTxr3Z_g04IUgBHCmvyvD3jfOli9qnZA5pCosIlY5qM6t3nZP1y2M7AOQZq8neHjzyn7tNP9uiaSLCV1aGCs2SJWCta2vbXZ5E5qllRn_1vwrEWqD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد یک پهباد جاسوسی آمریکایی در آسمان قطر، در نزدیکی سواحل ایران، مورد هدف قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136329" target="_blank">📅 13:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136328" target="_blank">📅 13:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / به صدا در آمدن صدای آژیر خطر در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136327" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدای انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136326" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / به صدا در آمدن صدای آژیر خطر در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136325" target="_blank">📅 13:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcPgHcD7pyW09rzoc-kjc705y9_7lNQiA6fFcmxYO98Y4rk3vU5580-soiPc90HYmzBbmSSuk8JiVPU4JfkhbjJgtJSCDulM_vfJOESr9kHRvYtr2OuiWHNiRMHK0WthLDRJhcU7-MAvYJ_hnxh7_vNHNBsqV_bDillFPs-sBIklLZat4C5_hB-saHFJKZ0FBaTj48JRPZhS2jIEf5DOtdHXpsZSLhcAZSV4Apmbcr4K8Nj1qy8c2cbWUshTJyD-CJqilWf_ghz0TyjGdIHHonQjsz5hHwn2-5JyR0qOERMJqzrdc6vI-DIl9hjjE-sK6Kqi6gaWkisdBJez36cSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeIicYDDapj2ELwKA-JOQnj8BeKKTv-HnB0PeVacVgOWZR90XWlHFKuYXilqyyaQMNw3-yUbDMi30PhMRz--__FIP9lbNuoBXCiqau2s9F0BzMm1exFqkJLHnitGwj5uhiKdpS8z1pEqpRVpKRktqhWUknxItVku8OYVCQROCtGmzm3LUTS3hwsmU9PjusvedYDquvDchtLGWFaEYn9z_iWgF0zmOyQAhiqfMirW5n5IP1otquuz5ASZIV40TDtlBmAcug1lh1YiQcQHF73kzl04ENCCpNjEW-0LJ2oEprFdZroE0hc-6wo_K_tnBfCZlrM9ocGZKm6J117U3n1AlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از شلیک موشک‌ها از ایران به سمت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136323" target="_blank">📅 13:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136322" target="_blank">📅 13:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl7gDoBat_YLxWQ_mKs5okFG1pJm5b2UaamrL1LjdaSknFJWlg4682yFIConci9isLdJKfcIMRxatg16wEU0mTnSoI4erMms4rJQIVg5Zf1YoTOxczYVOM_avPDIwd2xYPiJSDMHRG7Ey5W_BKvYuSzmvAZ-drYm4su_iawLLWFeOgUMy5qjT6j0YnByvhSea6VLgvvF22N8l85BSB8JNthBUJWqpcPKVW6_CdoacVadtiwE38uYbL9FCMSjL6mc4ZUOHc3HPf1A76rJr6KuNO6rMm_hsxHiW049S44KBW8aXD9HWXfF3K3iQgyw9ENQtdLN05XYFdEbb_FaqKq-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری صدا و سیما:
افتخار میکنم مثل امام‌خمینی، هندی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136321" target="_blank">📅 13:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وای نت عبری: مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
🔴
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136320" target="_blank">📅 13:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شلیک موشک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136319" target="_blank">📅 12:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY40uOeiWEA_zMvplK2fex0gQ2Hwta5VhGHqOwkro5pavEqt_ABPMbN2anvbSkk-ZimJoxtPl04FoYWVlTWnpaK5MybcjqtBkbFIJXuc67IImyGMj24g7RoxQejhRj0_5od4JPTKZG5CcIUU4InTPc5gOiag1ydPqt045IiJwfAs6s9CYmolxUPqQrPIXZbYWRfr7mBcw4sJx3WsfGbtCeit6OJHUz0a2dVlic-QWD9FDDZrkHLe2lmoQh_KwmDyRexQ6jEfMdX555AXJvqTRLyqvVxQ0ctGh_BuC2TXdQrgegyrT571Yjvlr0300bpATmi98k86RliPBuhNFAKpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f15b07102.mp4?token=YPZJPa72R0RLVBaukMn4YTNU1EQI9sU48dJ5Al1g8Sv-eCnQ3tTBtMx9NDdSVHh9SPDDOIajqU2H8cUL8HrorTcXXfExYjKqlTsfiT5zYOj0uEMCcW8Qp5hKLYWEOwHkGssWWQRZMBGBUKHGCGqsC3jFdEDNwSd36tF1H87MRnqZA1783iFTfB3CFoomxrBNgJl-xJu1ZW9ghYWBGDF53-_ynbbpoWaOHlSGkMpTowmdrrvT9jnwZhFdf9EjBu4ootk2Rl0ndZ-0cmYjo0Iv619lec26Skz6KbCvKbOGpa7ZpTQ591HcCgRXpi0OIB6rSoYJvoJSZRAL-KdPIBboUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f15b07102.mp4?token=YPZJPa72R0RLVBaukMn4YTNU1EQI9sU48dJ5Al1g8Sv-eCnQ3tTBtMx9NDdSVHh9SPDDOIajqU2H8cUL8HrorTcXXfExYjKqlTsfiT5zYOj0uEMCcW8Qp5hKLYWEOwHkGssWWQRZMBGBUKHGCGqsC3jFdEDNwSd36tF1H87MRnqZA1783iFTfB3CFoomxrBNgJl-xJu1ZW9ghYWBGDF53-_ynbbpoWaOHlSGkMpTowmdrrvT9jnwZhFdf9EjBu4ootk2Rl0ndZ-0cmYjo0Iv619lec26Skz6KbCvKbOGpa7ZpTQ591HcCgRXpi0OIB6rSoYJvoJSZRAL-KdPIBboUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله با استفاده از بمب‌های هدایت‌شونده روسی، مناطق مسکونی در زاپوریژیا را هدف قرار داد که در نتیجه یک نفر کشته، یک نفر مجروح شد و ساختمان‌ها و خودروها آسیب دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136317" target="_blank">📅 12:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136316">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شلیک موشک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136316" target="_blank">📅 12:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136315" target="_blank">📅 12:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdeo7oICKVkuU20ZCwjXhRlq6_LQlrRm-vw4aA-KNExc4d61nBcWRuNwkF2LuJZODx2ytdtDtj197StiGbPnPdkMh_VRx0ZSQr8QZFDeWlLK0ysJe6msjnVFCIyWRdDtHRonYAMrdlL_k2DIG_zLBCjR7e-CbJsUXSn9o3ce4kB_gq9WQgMUUDI0SIjpqBjtgFaZFEqCap7zuzaytI-8a0K9OmGS7yU2kcCXecbU4MVQuMeEEKM9bkRPCeMTgLtf4ZjTW-RgNyKHg5M9yUTwkMflYYDNjyUIwxIo1d5qzxUUUkVBXjoe6USoYbEpZ7H5s19JUnds_zeCzSNCkEEZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه نویی ۵۰۰میلیون تومان از پاداش جام جهانی خود را به خیریه کمک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136314" target="_blank">📅 12:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCSj9BsV37S1Yg2tlAxTp5IYiP4Fs5SPGYxjRo2CrTrfZ7T__GoCZxhYCm6gkk77O3NfbgpT6HseqcxYPYbLFyw3dzHMdFry2TPpDBkpl3RI-nc_N6aABpWOGJFEl6hIDmpDM-r0MPxO_a5nJBN2QII7oMAnf2SprtmzuzRPnheXcplylvsBpQPmds3u70jFuHcpUKQeky4WWsgw61O0VsBtw2fW8rjFFmA_haUy0-AQiIf-_3hfrI0qb-YohlI8z4h1pZ0CpUC_cYhxxNrQoVGwKOMnsvrTAQrDKg39bUYhB8WAMtqtACL2PY7lb4YSYe9gF9DW9PGeiHhif3DRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgshMk6Bq39xsL3Bfq1ujDoaCshb8A4-HCiT7NTzOaJ0Nl6sduCqNeoCKkpmG68jFB4hGvdk-QLgIB8_e56a8EH-dIfA9v72xzXZy5UolzJs0zuJWsi27ZL25lIhfAvDuHIhpl47EFWPa-NjnenAIt_ez_rsrwPnotpA0wysGjZ79RWBTEl5O7_ZLYMyBiSdOMRqaEpYs7MoJYnmEBq5-i18AA2h7tNjNCgppaVcv1hZLm134zWkDwB58bxxH-Up1tDR-C68qCHYzVTqL9F10y8SW9O2FQQWi5uhUEOJ_HNlm7GthURPg68zcPkq4DRf71C7XL7P1YzoQqZv3MIsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/todhPhB9u9x_X3irdWOAzw74LYt-ptBdbRrqfwCBh32nJ0OyQa1_4GlbF1Cos0fouuDlYa6EmYmun3jfXPhawHQqMM9hWj6xF1hhcX--wq-OjlvMCNr2D0pWvrThuO5zpdqxOPa_3UEwm3yIK6E1CEzpIrwalOouCsg4mjIDsZVC_7VLESY4Z9X_Pvsikv8EwnGFk98PLEQg45CUi8UAYJbo_Bc-FEzk8nj2W65VJSUQCcsg0GYNQAzOZhmvSjZjTM6IMhvgb-bqmj3B4Wwj45rU-fsTlOFdkARIW3F8Oyj1O_hHYTf_sCr48GnTsVV7rgWQmm5MdOCBKgQnhybvSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل، درحال تخریب ساختمون‌های جنوب لبنانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136311" target="_blank">📅 12:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
در پی حمله سگ های ولگرد، یک کودک سه ساله در سنندج جان خود را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136310" target="_blank">📅 12:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533201e41.mp4?token=GeeijKyR1Q8q6PonZohXMnnkoO2-ZsGQHgBgZZvvqBgKAP90zczenF3j2NHjde3lUKF5Qg6Uv_ZZqLMmo5GdDgIs8joeuX5Ude1dBLb1IaAG34XyNk5zeGRXoTcN7WQhZYX8SoDn7TDj_XWU2-Ubztat8myL9I1Wyh4d9c8EN6e2rTD84Pp0HYKAItD_GeaapPWrx6nWJzaKBbieU1VikbYXiVSqEWWL8GyakeS_-g5QutGe_8sCEvgOSz8Xim76oItjeFTwSJw8Zdvjjs8XLE8FnScFcqdIlq-jiFrfeZSFPJAbFHlrGCra1b6bFZB16dMzdK2NwusLvc2S1HtipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533201e41.mp4?token=GeeijKyR1Q8q6PonZohXMnnkoO2-ZsGQHgBgZZvvqBgKAP90zczenF3j2NHjde3lUKF5Qg6Uv_ZZqLMmo5GdDgIs8joeuX5Ude1dBLb1IaAG34XyNk5zeGRXoTcN7WQhZYX8SoDn7TDj_XWU2-Ubztat8myL9I1Wyh4d9c8EN6e2rTD84Pp0HYKAItD_GeaapPWrx6nWJzaKBbieU1VikbYXiVSqEWWL8GyakeS_-g5QutGe_8sCEvgOSz8Xim76oItjeFTwSJw8Zdvjjs8XLE8FnScFcqdIlq-jiFrfeZSFPJAbFHlrGCra1b6bFZB16dMzdK2NwusLvc2S1HtipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافندی اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/136309" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfY1ts-Q0zyN3MoqGAhBYLXfT4etTFz5WdXon-8BcJ4iQpbYtlQRxYgHfANvzT1FbhXaejmfIlYpNPWCGvdktbhGVivAn7iPd9_Tfxy6KHvs0q8J7uqJsSjhKR67jDbtfWJZFFVqr24ziy0hB3vNmAopVp-eqgfwcU9V8bEbV6uMN66k0AnzFnMx3k93eYqyXigL5vuUY7JuUNF0PWaSKRG6CMullF82UZYRIEwmD1I3BNu2zUbERdAw9QncK4WbDV0Ii_pn_Z7e2D2k4XcXfPc3TrAywpYVb3luPwi1CiubyluS6xl2b6yx7Qb7Wav9-2o0TQe7ajFn2JGZvxyz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه WSJ : اطلاعات اسرائیل تخمین می‌زند که پس از عملیات طلوع شیران(جنگ 12 روزه) ایران هزاران سانتریفیوژ باقی‌مانده را به تونل‌های عمیق در داخل کوه کلنگ بالا، یک مجموعه هسته‌ای مخفی واقع در 80 تا 100 متری زیر زمین، منتقل کرده است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136308" target="_blank">📅 12:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSoiu6zvQ3Rdf1p9WIohi4HGWhzCL22dtJ1oygpZ1QqY7GPZvWyy0InhR6nYigg67tGjNPX9nPMB0HYbNa9KdwREdAzbojrU1yXGom4ACwZ-cWzk0pw5azH0nvEMvbohpONipzIlsj0QI6_9IeP7sGd2aWAEb-N_AVn8LFpHIOHVVfVtTg5wkwzIxFW5t_1j49UKyvqcyZSbMHmXhXgoHnVtaCZUxxTbHShofkW9Y00TaG8QTPRaVQaPD142el5svrAAyvgBdi6vHFqN78lMo2D4v4NLVhNf_moBF5Y0ycQ3aICGNYCDQ76jv50cB5Y5ITn6FLo6RMepE7d4oZt83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور وزیر نیرو و عضو ستاد علم و فناوری شورای عالی انقلاب فرهنگی: مادرم را به دلیل بی‌حجابی به فروشگاه وزارت دفاع راه ندادند. من هم به معاون وزیر دفاع زنگ زدم و شستمش، او هم گفت بیایید تا حضوری از شما عذرخواهی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136306" target="_blank">📅 12:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
الحدث: آغاز دیدار وزیر کشور ایران با عاصم منیر، فرمانده ارتش پاکستان در اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136305" target="_blank">📅 12:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
قلعه نویی قبل و بعد واریز صدها میلیارد پول نقد به حسابش به عنوان پاداش
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136304" target="_blank">📅 12:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE1aeqKTsGktAIdqjMhkuAE-mfc1RhHtphzYtpAgcC72b2kwxPhSv78qRq68v4CwgoU7pyuBwiOdlYDtrXwYypl5L0r_jjl0maosTL3WKaV89ES8HMxTkgeeGZE5LOeoR7cDo60I12RLy-9t0s6xn3hmeWClYrZ1iGmp7K--4dthB2RMUUhAug4Nie-lk4Qln7P7rrbdKMo1o1asCY5n4m2eQIrUc1aKqQZFHgP5STft3bnNdH3-E15rU1Z7pQld6coD_ABktX64EIwzB15mmseCCQRhGrvDtVmfVIGqGAfAoxGtVu31T9WOcRa3JOVn91OJTMBemzoQOlbU84twVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
یه مشت وطن فروش بی شرف مخالف ما هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136303" target="_blank">📅 12:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سس گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136302" target="_blank">📅 12:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136301" target="_blank">📅 12:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔔
تبلیغات قفل ربات الونیوز
هفتگی 250$
میزان جذب: حدود 30k
سفارش دایرکت</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136300" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بنیامین نتانیاهو، یک جلسه امنیتی طولانی‌مدت که بیش از پنج و نیم ساعت به طول انجامید، برگزار کرد تا درباره افزایش تنش‌ها در منطقه گفتگو شود.
🔴
این جلسه حدود ساعت ۱:۳۰ بامداد به پایان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136299" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136298" target="_blank">📅 12:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وال استریت ژورنال: از زمان آغاز درگیری‌ها با ایران در ماه فوریه، حداقل 18 سرباز آمریکایی در جریان عملیات‌های نظامی این کشور جان خود را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136297" target="_blank">📅 12:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
صدای آژیر در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136296" target="_blank">📅 12:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awaL8DonAucwvr1bhZAZoVJgqdZNlOTNqQB20p0DZcTZrN58ZWXHoc9d5r-rQfNPFE6bN5NSp99lPGIBxJ-wQj8fgOaAbvKrL-yhueQ1YBpDxzFAzFESGFPjbD_TCRT7lf_ydMPb604_oj-4qwN34Wv_r7lcIdBySr1Fe-yRsJ8k7LqVeLvEeirWtWkaV2YzsrnD0OMkSd_7O6WDNxkCavxjx5lyafTC_SB5zoKzru8TLdCDJ2yZpJCUcTqflbUqV5_akT89Ap8ZrFE-vULLuxufnil61a2DvzDS02lJbDLdK70JKgqhq2-UVoxDVkcsJeLTpza13HZqIrzicl7ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ شلیک موشک از سنقر کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/136295" target="_blank">📅 12:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت بهداشت: مرگ ۵ نفر در ایران بر اثر تب کریمه کنگو طی سال گذشته؛ ۴۹ تن هم مبتلا شدند
🔴
بیشترین موارد ابتلا در فصل گرم
🔴
از مهم‌ترین راه‌های انتقال این بیماری، تماس با خون و ترشحات حیوان، به ویژه هنگام ذبح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136294" target="_blank">📅 12:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بیانیه مشترک اتحادیه کشورهای جنوب شرق آسیا: شروع مجدد درگیری‌ها بین ایران و آمریکا بر تجارت، انرژی و امنیت غذایی در منطقه تأثیر خواهد گذاشت
🔴
ما نگران هستیم که تنش‌ها، فرصت‌های دستیابی به راه‌حلی صلح‌آمیز از طریق دیپلماسی را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136293" target="_blank">📅 11:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت دفاع اردن: ۵ فروند پهپاد که از ایران شلیک شده بود را رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136292" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
معاون امور زنان و خانواده رئیس‌جمهور: به هیچ عنوان موضوع موتورسواری زنان، حرام ذاتی نیست
🔴
نمونه اولیه گواهینامه موتورسواری زنان چاپ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136291" target="_blank">📅 11:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de1e4db8c.mp4?token=FmSwe_N36gSuUc8mRjYFwUu5OMbO0s60b9a9H05tSI8mdIb3iZDugvrKZ-XNAusn-OsAKDIRNBZ5KXr3OdxSDKZ3DanbIANYB2BeiUuYQcF8X9xtBqu1ZsbfeSKevuqWBCuwSWsN8Gn5COKJrsBYQjg85QwBaQo-bv1Oyz6l208554TGOSBkwGkSIPRJilO-5wj0dnPQL29fYL2JkRsPElzfyRAlAiy6eH63GYvBu_m3VCHPBXSnrz480ZsPVLViT-sqmUrChkw46E62yUi4im71Q54r6Y7sHEpP3X6ZgRVO4cDuvrehPnwTxG1wjE9ibKzcoeQBHRmBVghTdzePkLVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de1e4db8c.mp4?token=FmSwe_N36gSuUc8mRjYFwUu5OMbO0s60b9a9H05tSI8mdIb3iZDugvrKZ-XNAusn-OsAKDIRNBZ5KXr3OdxSDKZ3DanbIANYB2BeiUuYQcF8X9xtBqu1ZsbfeSKevuqWBCuwSWsN8Gn5COKJrsBYQjg85QwBaQo-bv1Oyz6l208554TGOSBkwGkSIPRJilO-5wj0dnPQL29fYL2JkRsPElzfyRAlAiy6eH63GYvBu_m3VCHPBXSnrz480ZsPVLViT-sqmUrChkw46E62yUi4im71Q54r6Y7sHEpP3X6ZgRVO4cDuvrehPnwTxG1wjE9ibKzcoeQBHRmBVghTdzePkLVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد موسی غنی نژاد:
زمان شاه وضع مردم خوب بود اما امثال شریعتی مردم رو فریب دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136290" target="_blank">📅 11:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouf2NGbJxn3JzdzEKbfUSLLYijRiYsHkh_0a5UJdLYEVKdaeaLo_jDvrHSkxA2KnjPfdSK0JIua61LgnPAIp2B44sBXpZH7qD5NiBE3vk8rB_R8IdlR0WNrPVYGiZg4b1CNBw28f1vinOps58ncOXrUg-Rv1rNARQJnwRURCZvE28wyvNk5fTVdWb19T7YXcKeXe5-opycg7NQBjqUuYkunJi8EWqgENycTyZBHqwokFx0dcZrRtbTtNpTKOJb9kd3rSLX4Ir5kgYeePC61OGk_B9qmRVmanPD89DlR3TS1Bz1_hatpborFKwiE-P7CQtYE5FwK8vyn-HkX5VB2CRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری مشاور وزیر نیرو و عضو ستاد علم و فناوری شورای عالی انقلاب فرهنگی: مادرم را به دلیل بی‌حجابی به فروشگاه وزارت دفاع راه ندادند. من هم به معاون وزیر دفاع زنگ زدم و شستمش، او هم گفت بیایید تا حضوری از شما عذرخواهی کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136289" target="_blank">📅 11:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر مالی اسرائیل، اسموتریچ: اسرائیل هیچ انگیزه‌ای برای مشارکت در درگیری محدود بین ایران و ایالات متحده ندارد؛ وضعیت فعلی، بهترین شرایط ممکن برای ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136288" target="_blank">📅 11:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فرمانده نیروهای دفاع ساحلی یمن: تصمیم ممنوعیت کشتیرانی برای دشمن سعودی بلافاصله از بعد از ظهر دوشنبه به اجرا درآمد.
🔴
ما از توانایی رزمی دریایی برای اجرای این تصمیم و جلوگیری از عبور کشتی‌های عربستان از دریاهای سرخ و عرب برخورداریم مثل همان کاری که با اسرائیل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136287" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN-ZHvuxoenZ3xBDofrjKZVr5K21FtznGukmlQMqAcBmG31EQtX0uK29qdebOZVE0SxkKF4PkabKWIT7q3jCZS5pXn73lIC7O3NORM4ObZEw9I7edYK9kcMk6cRKhiXm_p0ZM1NSt9QXWE4EASdImSBpP3qZsOcUQwSuVD63AF0uc0U6rE_D9k0V0ns50dSGRUf8um5wyNGSmdJ4p5FWp-HJQQgM0c--xucrkSlRE_Jnemn0-plJt-G68qhOnGsIA_XWQyIY37VKst-bUF-dII9aABLUHXDDGH89khX0vNuSdUl_PsZG1xSfZL4UGhmxcq87thlxkssXyMLvAvmAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور کریس مورفی با بازنشر یک خبر از واشنگتن‌پست: بسیار نگران‌کننده است. یک مقام ناشناس دولت امروز گفت: «ما به دلیل کمبود موجودی و خسارات ناشی از نبرد، سامانه‌های پدافند هوایی و مهمات دوربرد کافی در اختیار نداریم تا بتوانیم با اطمینان به عملیات ادامه دهیم، و فکر نمی‌کنم کاخ سفید از این موضوع آگاه باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136286" target="_blank">📅 11:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مدیرکل درمان ستاد مبارزه با مواد مخدر: اگه از عطاری‌ها، مواد مخدر بگیریم، پلمپ و دستگیر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136285" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759573b975.mp4?token=im3kB6QSeXPoRgpClfO4Z3AEXtH7hCWv9aWj8SiEuUwSmcMUATF6q1YYDUDAgInFEvUMlaeH5Ij8gI7w2o7tIUwCg7mSs8pMRfncd9WaWac53g1VdJH3femCcmuiL1SXT8VeZo4Ay0sPcxEFu6re3ZbdO6wC3ICevQw6DtQS_B9D8e6RNLm1MozUi6LWeA4MCncGO0QyOJPVEuBujPgTFJf1UI5MRa4mU8wLUOpwPJT7tcNM3RcHQv44_JIJzHcnGjyWpED2yFAzjX5R7ntqIWTn2_XMP37dSLXcqVm-lmoh9HYTMtdcDLzgT2jiYvvQtIJd0ePnNDZCP4zyGfzxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759573b975.mp4?token=im3kB6QSeXPoRgpClfO4Z3AEXtH7hCWv9aWj8SiEuUwSmcMUATF6q1YYDUDAgInFEvUMlaeH5Ij8gI7w2o7tIUwCg7mSs8pMRfncd9WaWac53g1VdJH3femCcmuiL1SXT8VeZo4Ay0sPcxEFu6re3ZbdO6wC3ICevQw6DtQS_B9D8e6RNLm1MozUi6LWeA4MCncGO0QyOJPVEuBujPgTFJf1UI5MRa4mU8wLUOpwPJT7tcNM3RcHQv44_JIJzHcnGjyWpED2yFAzjX5R7ntqIWTn2_XMP37dSLXcqVm-lmoh9HYTMtdcDLzgT2jiYvvQtIJd0ePnNDZCP4zyGfzxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازنشر به مناسبت کصشرگویی‌های مجدد عوستاد ک..چشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136284" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خوش چشم ، کارشناس صداوسیما:
توئیت قالیباف مذاکره‌طلبی است؛ مثل فیلم Inception به او تلقین شده است
🔴
ببینید این جمله را چه کسی به شما پیشنهاد داده؛ پیگیری کنید! به شما تلقین شده است!
🔴
فیلم Inception لئوناردو دیکاپریو را ببین؛  قالیباف الان خودش یک پا وزارت خارجه است؛ مجلس است؛ چین است؛ همه چیز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136283" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کیهان: جنگ آمریکا با ایران و اختلافات دو کشور هرگز با مذاکره حل نمی‌شود.
🔴
یکی از دو طرف باید از اصول خود بگذرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136282" target="_blank">📅 11:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / یک کشتی در نزدیکی سواحل امارات هدف قرار گرفت
🔴
این کشتی مورد اصابت یک پرتابه نامشخص قرار گرفته و سیستم ناوبری آن دچار آسیب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136281" target="_blank">📅 11:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpK1xapOcaXLXYjrTfk72P9qTdagHKiRiXx7ogzc3E5Oml5L1yDw9XhZDGLzLli907CgWMRZPJoeqHwbkPlxNAI04luK1QEwJfmtyZtF9RlJ5_EnzJofX8QOk4sGBN0c6IenFe9P7JdTS66Fro66JZ_UpmjbCe9t1tO7TFavOR9x5Dk-ClQdqfmkFVfBiJYvNpZRhrRoah50MOTHBv80ob69_qOqOyeihCerkIKfpNLDwGpfT_GlbjhdnGprv-72LsQHHgVIbFL1BsCnTG_q76EPXbD4Wg_gkGxIrGYLdHdr5e0TG3WpxWfZmmsoV2joRV6c0Sq4S5vlEGvf9pVTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
بیرانوند بزودی استاد دانشگاه تهران میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136280" target="_blank">📅 11:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saF2H5RSkRAmPKdh8ldnXNRuPy2aTgijIdWwtJzmcVoYK1KsGLXU4TIz9AnVU8rh4Ho3Qqdh6LmPC8Hh0VBcVxyEeokbsOQYkdVVM9CTKiXt3oizRhhvY7aTM61d-XeOc1L3TrAIOCxG6bi1JktHDc6z5P2iVCCfQ6b8PLuMWW2iPTmerff2KJAGHbshiEN5Ug_9e6fjowQ86IbmOBSb3XRNp-FzZqxSa-2e71qsiI8gOTAJSeWaT5Msl6uO_h6FKoZXQMb_cFLRNoSzyphzzyAyQ6oQ2OIzq2qdmspEfz_QPiAiwc_a45TO2m_87XDGjSCThzaRq7kMPzihES0yYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مغزهای کوچک زنگ زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136279" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قالیباف در نامه‌ای به پزشکیان برگزاری جلسات علنی در شرایط اضطرار را ابلاغ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136278" target="_blank">📅 10:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYfVnDNuWTheuiheqwpha6oMnjv0aJoVijWjX6MOvX64xT6EZup2Zc5tJfUz5E9CdA3k3ABi02U-rXh5Gz1uU_Fc4mys7dSXoj1NC5rpYLfKLmMJbk3wHJLYpQLF5gr1iBjOoj-DRuavBNxX4ofMDLsZuJQTidL_pbBzYoXlQsXxFgQDtgSJL7BjWt46JLr1-4zjG7-GrurMW6TjWOJdHF8--1MF0ES067eQB1anB1kQRhOu8N-EgMj3w3ouaqEHs5TvZ1u9OUxvTti6sc9NqFDAcGmQ_IVvI3PqrtUK39Ka4ymCjhs87vnEY3hc-aKLw3-8k3IuUmVZWzwL_lz6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده!!
🔴
بلومبرگ گزارش داد، در بحبوحه بحران تنگه هرمز، عراق برای انتقال فرآورده‌های نفتی از طریق سوریه به سایر کشورها، از ناوگان بزرگی متشکل از کامیون‌های تانکردار استفاده می‌کند؛ زمان تحویل محموله‎ها به بنادر مدیترانه‌ای سوریه می‌تواند تا چهار روز طول بکشد.
🔴
به گزارش این رسانه آمریکایی، تنها در عرض چند ماه، سوریه از صادرات صفر سوخت به صادرکننده بیش از یک چهارم کل سوخت خاورمیانه تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136277" target="_blank">📅 10:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAxFhUFBp8wDkoyciT-VPii-wR7Rep88XZirRDEhWJiaPcqQmVrSE0r455HgPqPlaJSK-xk8et0o8PWuV4JnVjkZwupqES_1mr3WfDfAA1OwPgqGaj7Voq6dgVMxPtbt8Omkw726-N9gApKvFtTv2IknIuy9aCvBIFcK4YP6F4UUomy990JycM0slxgODlidwhpnrgjJQqaK6gvxayKLpbY0XXSVSEvlitZqTsdjtWsXXk94OXszCr-M7KbKEHcUMRzNKJGtv6sv-LtQkuKFTTfxhUc7GqCYNYHSHR97UhhBIOpILmK96jadynevltkeAdddKR7cam2D-xu80Tgygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شاباک، عدام ابراهیم شعبان نسمان، رئیس بخش عملیات تیپ غزه در سازمان حماس، که در حملات ۷ اکتبر نقش داشت را کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136276" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سوخت‌رسان آمریکایی سیگنال اضطراری ارسال کرد
🔴
هواپیمای سوخت‌رسان آمریکایی متعلق به پایگاه هوایی الظفره در امارات، هنگام پرواز بر فراز خلیج فارس، سیگنال اضطراری ۷۷۰۰ ارسال کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136275" target="_blank">📅 10:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McgoGh_JqnnRuy3sGeAl7qQN7GRMbbPq6nOZVkF6ltybAjqk_q7vnfOHR7mcWws7ONEBdTCUNZEOsxfHtU3WP5zCrHzyVCgv9ULRbLStF5yRs-lxR4aZsPuE5JB4Samvs4BJ2WWXa1eiBK1qxr9PLe6AiFLL64JAmrYLAs7tZjMVUVI4qtEZR7OvP91P0FHhBsSpzXEoD1wyn9FXGFzoK-cixp53eD-Mp5PAZAkX-hy2pmk6nBDewanGDlfVEZrq2n5tNCEtE_vptnfRNkUMJ3eOfnw3GLAdPvPJCWczDCgaJxyQM3vqtdiEz2g7lP9ETam_zjrLaGNnId8WM5NQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی‌ساقی:
هرچقدر پاداش به تیم ملی بدن، کمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136274" target="_blank">📅 10:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نیروگاه برق الزور کویت هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136273" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfEnMtLGt6ajsXFB4bvFPvGojvTm1A1vvO_QoS1NVYWvjgeg8WcBbYLLsKVk14_ys8_8MJkzu5EAg9diU1msrSb8eUsGONJajUGA1N16ON4NMdpZkx_ztZ2HrCVr5wtfraZOUKjh-F7eocAd458Sat1FchW4d2vFRAb40LRxOTXEhm8s22shTvlz8hoF-2gYTi5tSWybg_MAEcwzWakouW5L64b_R_HlKK-dg3zvttfu23w-lFdwqRGvTF6TEE2_C1WLknIR7LwOmDBmucyG-mt7WhcDj4fElT2G0c8vbmd-YAlPK1HatyM7mIClqlGmGoHgHBrcmdbEzCadN-AX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شایعه حمله زمینی پیش دستانه ایران به کویت و این ویدیو از انتقال تجهیزات زرهی که وایرال شده، قدیمی و مربوط به یک مانور نظامی در ایران حدود ۲ سال قبل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136272" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a015ba28.mp4?token=m5rkpBlgj6vg7kGNHGfC2RuCnKxHBHIU_dMN1Rk4et0gB_JWD8mJl1qF0lhnYjmJm4vEWiwR6T4LuW8GPMBQt94BdYNOjQEimUecHIWPmTkSE8sxeeiOoOIZGnvLqarJ-IohXmIuMCVx5dm5wNkcjOawB2dZhyLSxTci8pFkVrLJXS-jP3NJFNMGABJrg6RHuhIff5h-zG500Fy2Hse-O1IXN0zUTcRepOb1P7ZjOrIVVuVxvZoXNXROeS3eCqCv1A4MbWgt4qcIWTGzUBs0lY1syBlTFbR5S--L6Af7k1gDlBlThB3338g4i-rNAYhTTtV6pv36GrkkbB8BCeD9wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی منتشر شده از طرف سنتکام از حملات شب گذشته آمریکا بر علیه ایران ، در این حملات از اف۳۵ و اف۱۸ سوپرهورنت استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136271" target="_blank">📅 10:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PitKwAS5WJslY1F6VzhjL_XPPObXKDwWyxdvmpRgdBJIpeqzSothLeVhl99k7nUtOT0DM6m-qplo18nfZP1D1WJ4vZXDXoo72SHIHFUVpR4OaEYZgUYgmiAfPRdC0MhB7bi5YSC5bdzSR4slzl76BlDvzfNm_c6xh3dlGwm_9snourxeLLxRgZq7AnWQUEcivbFjftmm9QijWw-ruliG6tt_QU_qmKD5m40ClNm5326wzGOpwF3WBzK2a882xEH3x8KJITQaXrV29O9TbCGsAEzeZ4QCyQbQXwflGcXqViZRiN4LZKdAUvV16ybU4cSwr9OWJ9P6BDlEzLFXLDMe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnxBpNrdANTm6-j9pNOjg6LWeE1VykNm9E_upHXSo6IKRTNAnSnhIqmyYp5iv52jz8qYjd8OyuF1eR96h3YM8mBn9oK6SprP-2WoCmeu3sG-JtK2GGs3kylAXAhmAO0roeWedFHy7KBjMK_NhyWha58lP_wd_ziwn00XqsTATuh9SMSrP_g7UZG94UYIKFRjAoIvWvS9Hpq5meLW0sv-YPFj1k53MIAOvQD1ZydY6nLqR2PLTA4TViQOXVqsaC2CCuQjDyH_9X4WDdKmZmM-slCHOKX30giLQ-ExX7GoAsmJjxuAANX1RojOfhu5uKBz_DZh2Sh_mDLUJZv6o3vnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRdHE9lhUW0epLW5Ji5-YqCFYpIjVol-QO7kCIFRcCQC_RD7rqswntjzPbxzzSjTiVsF8cx-_gf_eJOiID5Dk9WbrAKuTzvs0Et6-iugXGU_qZdBITaOk47Lv0AGUAGAJl9rBi9fTtwaTwYMXOoq4SqjXbhb8srbARvEa9jgW1VAueyc7LDuFzlg_pQyIbJuRcUh-zVdgzs2lRhlarNAGSuKNJGIPPAqZrPVcBs0A-1xO9qQmHJCu-KovKdvPp1bGAGIVmO1nurP5X9iMydaEZx13EndPnAgnole-Mjmmd7Y7wuLcHjURWnRBg4g6lxHQxBC5IvQWJ_HOVwXUCFTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ed-EKD-E_nJiMtJXyTFEP7GVdn_7g7TxGN0oY-GCDLddFtnPpTO_84SSCZ5_41HWjvGOfpdLTNqj-Hco5I75pNbuDcqvK_MXtEQ9yl2Cy7DXPktFKN6mpAdf4mwFpaW5vGEMqQ3yFgWsplVq05D6Rvj55B57XKyeeIRk7B6pfStawwbJxzs0HUlKNUU_H_WXwsdt-Z67_kDstdcFCbqKxd9UujoFefM3TpDa2ugx-D-WoM-EfjQAhym35877o-Cw_Xe6i6un9EEc-eLTvVE0KA94aUGaov1eR_emYgp4HEJlHYots3qil1N-1FzSJ1NG6r0dE1_21nJlhpaz-JmoDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هدفمند اسرائیل به غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136267" target="_blank">📅 10:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQSyMn_5wigGZBZyGL2E6yWHDDoQ3S8TN4ohMYt2wY7OotYmtkv3XIDWP83QVG46AocOw41eU-2tkVf3WA6hAX0tlbr8H1aX1LHmJidgirSplbcIeZMY7ss1BxIPqQTf1_6c1uozCVmwAFSVtN7UIKDZG-3H35dxx26jgSJvUvHIvzu-Ai2thFSz27Pv7uwmOpuvoMKOpzph70ZWgtSmRHBUIhAt810I5f-hZ07pvIYYIykonHJYQTw0WRl17pkW6GY6rZgsyB_juvcMpHFo69AS2x2Jx7V03ct2THExBi1qIL4Xa1ooCwd7v6XU8udGsSoXDQVxKoELPhZwBDi3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله موشکی اوکراین به یک کارخانه در لیپتسک روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136266" target="_blank">📅 10:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=DdyIPWr4lZbKcYdP39WSzaMJJGucX5ekBk1UeCJYDMhgufHgmA4-U2yhXwzoWSPre19X27Rp8-6FALw0WG0Ax3jfkY503mpxhZlfFguVyjVd_g1sScWppyZbsxk62XSITnZPYpbneFCIvLOvha4tSlBmXulAEjC4GUkwiX7jwEymCJlVbpCogqRL2ybMJSw5_eTVjq3oR4vugF89Qls4IMYGTTO-V-xsXldYXgo5J_ovCp13_PPOzyjWpdHkVPL-HscKJ8265NZjkQOKuUZOQlxRzbVWXdf0O-ki_v0QXSDUip-n74trlagaRMVzPF3Q2QZmbwCJSorpqNAz6E_dTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c7cb1f67.mp4?token=DdyIPWr4lZbKcYdP39WSzaMJJGucX5ekBk1UeCJYDMhgufHgmA4-U2yhXwzoWSPre19X27Rp8-6FALw0WG0Ax3jfkY503mpxhZlfFguVyjVd_g1sScWppyZbsxk62XSITnZPYpbneFCIvLOvha4tSlBmXulAEjC4GUkwiX7jwEymCJlVbpCogqRL2ybMJSw5_eTVjq3oR4vugF89Qls4IMYGTTO-V-xsXldYXgo5J_ovCp13_PPOzyjWpdHkVPL-HscKJ8265NZjkQOKuUZOQlxRzbVWXdf0O-ki_v0QXSDUip-n74trlagaRMVzPF3Q2QZmbwCJSorpqNAz6E_dTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در پی اجرای بخشی از توافق با دولت لبنان، از روستای زوطر غربی عقب‌نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/136265" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگهٔ هرمز همچنان مسدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136264" target="_blank">📅 09:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سپاه: یک رادار هشدار اولیه، یک سامانه رادار دفاع موشکی، یک رادار FPS۱۱۷، یک سامانه پدافندی پاتریوت و سامانه ارتباط ماهواره‌ای مربوط به پدافند هوایی متعلق به ارتش آمریکا را در پایگاه احمد الجابر کویت هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136263" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سپاه: تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش آمریکا در منطقه‌ی الرُکبان اردن کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136262" target="_blank">📅 09:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
آکسیوس: تلاش میانجی‌گران برای آتش‌بس ادامه دارد؛ اما ترامپ و اسرائیل به دنبال یک جنگ تمام عیار علیه ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136261" target="_blank">📅 09:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS-Vtg6-cgen-tJVApQn4qzwtALY44IrcXmzCZWSTgj_x751KqiPMEDCkIuNfbUEt6gYXmH1wtvXK1Y5JN8u0UVxRgyRhVkTTFJ0Zoa2NE1VfM00dFSuL6MyClxWkivaUmh5pvJPzGcvQeIPyIuUIJOSdoG2-wotokds9LFXnff4M0ya1J2Azjhru-gRmoePAxe2aVhUIfETjUDiztjR4fEN5kLfpbKgUiQacHFh8biJT_6qwigwKlQw-Fyazi-l_lFDBWTfv0U0rJRhVVUAqt7ktBfWILUte3q3ELDgvjClfhIPZ9pZeWOtyXXgy20uoxx0sPSOtCegNaQDLQoffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل آبزرور: یک نفتکش صبح امروز هنگام عبور از تنگه هرمز، در حدود ۸ مایل دریایی شمال‌شرق لیمه در عمان، هدف حمله سپاه پاسداران قرار گرفت
🔴
این شناور نفتکش M/T KAIFAN متعلق به شرکت نفتکش کویت (KOTC) معرفی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/136260" target="_blank">📅 09:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مسئول آمریکایی: اگر ترامپ تصمیم به گسترش جنگ بگیرد، این حملات شامل تهران و تاسیسات هسته‌ای خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136259" target="_blank">📅 09:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سپاه : زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/136258" target="_blank">📅 09:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=wBkDIexpvhPblr-1lmUghcfy73QYDb6AlA-McyPQwomZHpTsbvleCx6R4CgSVFJckBNZtGMQeG1GDQqqyX8SYn2dqGB6CMMIrVpeqIh5i1f_CQuAPSWSRdecirkibZ0W5jnqJA42A-KXVxAdgvdz3BjhKZEdRv8dKzwxToouGr0P0kH-RGLVuvRJKZKrR2u5MDbD-kJy4mGsJX2soJdV6DH89OgH2sLuA9N8h3svPbLFp1rdmxpizYHnJtnGlgGCnO4Om44LyRYPOdGg8YdJbuUKiUE53gRpNXe7ONBteBmEeqhHSHut1JNnolsZhoEpxOgVDgbn6kLGPEIxT5b9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb993d4abd.mp4?token=wBkDIexpvhPblr-1lmUghcfy73QYDb6AlA-McyPQwomZHpTsbvleCx6R4CgSVFJckBNZtGMQeG1GDQqqyX8SYn2dqGB6CMMIrVpeqIh5i1f_CQuAPSWSRdecirkibZ0W5jnqJA42A-KXVxAdgvdz3BjhKZEdRv8dKzwxToouGr0P0kH-RGLVuvRJKZKrR2u5MDbD-kJy4mGsJX2soJdV6DH89OgH2sLuA9N8h3svPbLFp1rdmxpizYHnJtnGlgGCnO4Om44LyRYPOdGg8YdJbuUKiUE53gRpNXe7ONBteBmEeqhHSHut1JNnolsZhoEpxOgVDgbn6kLGPEIxT5b9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: به حملات علیه ایران ادامه می‌دهیم
🔴
کریس رایت، در مصاحبه با شبکه «اِی‌بی‌سی» : واشنگتن می‌خواهد با یک توافق صلح‌آمیز به درگیری با ایران پایان دهد، این امر مستلزم همکاری دو طرف است.
🔴
«کاری که ما اکنون انجام می‌دهیم، تضمین جریان نفت، گاز و سایر محصولات از طریق تنگه هرمز، با یا بدون همکاری ایران است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136257" target="_blank">📅 09:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=DQSDAcPZGIrGtMbciXgJ3DoWihz3cjriRWuwx6kdRBaN8YNw1l1suiJd_seXTgArze02Qi_oLVh1zlZyPENs1LwM8TZg3pPnwVMUgabmsuTj5ubHplllF53Gwa-nFfBh4ppmSr7iPTtEA6LZ8593qlFULHx-nUGesMWVe5vAH8IGz__DO_3iHwRI4gh-m1iRX--_EZTRKqki37lIl4gPFz0JdeLTgmdC20e8t1_4PcZ6AT5kaqFo6P_vdAAwMbow9ola_1BZeGWW9bk9li91R9rzIITVctCUHIWVhhCO0Ps3hfVl9yhzxINgBbVV47bOe4wvPSBroAX6fhGfJ4PDzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb851bd1b.mp4?token=DQSDAcPZGIrGtMbciXgJ3DoWihz3cjriRWuwx6kdRBaN8YNw1l1suiJd_seXTgArze02Qi_oLVh1zlZyPENs1LwM8TZg3pPnwVMUgabmsuTj5ubHplllF53Gwa-nFfBh4ppmSr7iPTtEA6LZ8593qlFULHx-nUGesMWVe5vAH8IGz__DO_3iHwRI4gh-m1iRX--_EZTRKqki37lIl4gPFz0JdeLTgmdC20e8t1_4PcZ6AT5kaqFo6P_vdAAwMbow9ola_1BZeGWW9bk9li91R9rzIITVctCUHIWVhhCO0Ps3hfVl9yhzxINgBbVV47bOe4wvPSBroAX6fhGfJ4PDzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر جدید انگلیس: می‌خواهم به کارتن‌خوابی در کشور پایان دهم
🔴
ما به اندازۀ کافی خوب نبوده‌ایم و باید تغییرات اساسی در رویکردهای سیاسی و اقتصادی ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/136256" target="_blank">📅 09:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136255" target="_blank">📅 09:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qts9xQAKxdLGht_ysoOBB5CdD9AlfpVVWr5hQ2uTI88mf91qOwZ4KV9MYGoOBpObFI0AljGzP0gVdervL5uz1LQhCP-57Sg_LXSZgGVweIfIdicZIhx8Bgq8Q0RcLOyTew64jrmUDDsELVJDrRIkZK9DD69KrPVjje0wbrUHZFFU5tyoIJ3LUaYC0MluwQWNKPi5vN7XfJrT8R_HurJP8MqdR29yK2pe6au_dKO2eehdBGz-4v077gxkBS6z2fyntsW7slZYjJem0WZLmUkfwfD7N2bALbxnwnYN4ZVgdLuFB0crL2bhO_hG2pIY3Kqvvbtacs6Cp7JZ2LTgPLs_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر نفت استراتژیک آمریکا به کمترین میزان در ۴۵ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/136254" target="_blank">📅 08:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کلید اولیه سوالات آزمون کارشناسی ارشد ۱۴۰۵ دانشگاه‌ها و موسسات آموزش عالی فردا بر روی سایت سازمان سنجش آموزش کشور قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/136253" target="_blank">📅 08:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn0PjnKINweOS-O9Czo78oRsP2LhMD6_yWdzlLkHXc185G-m9_P-O92pV4VoA4PahFesbBpba86pRSyqL0PWv9f3gdbqXuMoMNZWr2uxUw3PhUOKlXX3hdCIFIxFh7cnovsDDF6izm3rVIH3CkkoepSeKTV8KdLxags2WSy54B-KkH9cOwMf1tW04BUGIe-KV1r8CANLY1DWeqdjMUPGsA-ujuEHhdEDIKDhJVwxbxhQJBhLVQ7C46WVbN1rwxakqQNXcBJU414P1dSEr8_kpsNYbj0A0Cow1obbjr-GEqgLeOF2bG1zlnB1N9VDfTpvYmvZGDqB5xynP7E6Kwhz1QoY" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d40636c56c.mp4?token=GPVi2cm-mV34YilAgQ2ztWZKWj6W_uv9FQKIifxvSIdZhnosPyBc7EnEdgNwzcYBRSiosceemJ-GaMj47YwG3AFaILFVyzauYsj5H_BHp-UV2UFUMeOcCGAN-Ec_6F-X8Dqm6C-XEdQtLVapZYeZwOLGhPIRi7-kTrAoFzyvMNVxTAAu2oKWefdmR-EP8bM8PIhDN0NKnPMIDMlQXUPifSHzbcpcSyCx7u0-MFJsUiBNyKWeRmvtaK1avAUKAtyCcg9FMj6N8NZqrgyT0IHQj5tY01AYmgulPIxeWGK17jJj-LivX03KVbjmIhBfpQCy-ESHxPqjQKTECtn7A4uJn0PjnKINweOS-O9Czo78oRsP2LhMD6_yWdzlLkHXc185G-m9_P-O92pV4VoA4PahFesbBpba86pRSyqL0PWv9f3gdbqXuMoMNZWr2uxUw3PhUOKlXX3hdCIFIxFh7cnovsDDF6izm3rVIH3CkkoepSeKTV8KdLxags2WSy54B-KkH9cOwMf1tW04BUGIe-KV1r8CANLY1DWeqdjMUPGsA-ujuEHhdEDIKDhJVwxbxhQJBhLVQ7C46WVbN1rwxakqQNXcBJU414P1dSEr8_kpsNYbj0A0Cow1obbjr-GEqgLeOF2bG1zlnB1N9VDfTpvYmvZGDqB5xynP7E6Kwhz1QoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله لفظی خوش چشم به عراقچی:
عراقچی تحلیل‌ راننده تاکسی‌های خط ولنجک - بهشت‌زهرا ارائه می دهد!
🔴
می‌ترسم این تحلیل‌ها از طریق حفره‌های امنیتی به عراقچی القا شده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/136252" target="_blank">📅 08:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=v257PboXua-naErJa8NUbOpDc535-BF9FRSnRWBDt3XgqN9yOGT7_zzq5tCutvJTKF05ySpE2f7lqP1ymCeANxPLEkk2oJ5RCHNbJVYGoI_GK-yZruJmtAmFzKIiWOZvLIVGTu_gBaO8RYf5jRSGr8iVZO6aaDSnHVVJYRjtTiqLAaERajqvgP009JAL6wTwFjaFHHlpsBcEIMdzqPSqUZCuitA4BqbHw0IyUGwJzcUxle76KMUtf8C27Vd14LdOPBFzkSvc2u4fipfyUih_PsGYabw-eHSer4Et7lEJMfvekEzgN6hvdumqNFGsaga7XpmZ_eyQjOxIh9YVHHPqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22cdf53d0.mp4?token=v257PboXua-naErJa8NUbOpDc535-BF9FRSnRWBDt3XgqN9yOGT7_zzq5tCutvJTKF05ySpE2f7lqP1ymCeANxPLEkk2oJ5RCHNbJVYGoI_GK-yZruJmtAmFzKIiWOZvLIVGTu_gBaO8RYf5jRSGr8iVZO6aaDSnHVVJYRjtTiqLAaERajqvgP009JAL6wTwFjaFHHlpsBcEIMdzqPSqUZCuitA4BqbHw0IyUGwJzcUxle76KMUtf8C27Vd14LdOPBFzkSvc2u4fipfyUih_PsGYabw-eHSer4Et7lEJMfvekEzgN6hvdumqNFGsaga7XpmZ_eyQjOxIh9YVHHPqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارلوس خیمنز، نماینده کنگره آمریکا:
شاید چیزی که ایرانی‌ها را پای میز مذاکره بیاورد این باشد که بالاخره بخشی از خاک آنها را بگیریم و بگوییم اینجا دیگر خاک ایران نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/136251" target="_blank">📅 08:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روزنامه انگلسی گاردین: جنگ آمریکا و ایران نگرانی از کمبود گاز در زمستان را افزایش می‌دهد.
🔴
اروپا برای تأمین ذخایر گاز پیش از فرا رسیدن زمستان با فشارهای فزاینده‌ای روبه‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/136250" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKfwFruIdvDmvM8r8QL9q7aGqeH1lUVEgamE_1UiakKvEJUXNraDn3bqOnHjpktHYIKA16Jr38tQyfHqKytOXzFbZse3LFSTVlDFmYnJX9njKR4LaRR83Y6rXhyyPuCj1lwUN29CAP-GBQnK7WlBxstM0nKx5zET8rz3vJzcgj68oP9ICRuh_GbNTMiBGizl6Yp_3XOyRL244HDjRRMmJ0urFtKH3s9g815S4y9jZGO_rfpa29PuYQcRSjUcXlPoBW1KC3KY6iCWKlwSoGMDBS7TyQdmiIt33QgpbMd6mMhGQYfwmmdatsOsxMyeO4vwuqUc8qFm5lbnIp51uQ6RRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت شونه تخم‌مرغ یه‌شبه ۸۰ هزار تومن رفت بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/136249" target="_blank">📅 08:37 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
