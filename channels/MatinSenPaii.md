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
<img src="https://cdn1.telesco.pe/file/CjuJa9ibHKnfijx7V32D2mHz2eGo_Qy9O6NMniELssZYsjKIl4DIai_4eW2cEZo0DwWBHvYoxVHwM8ERTJQHegRQ1IsBNd8iZylvv0lmP39aGyk2IJbJOg4ROzK8MIKOjQ1T8kPk0y_VJFsFkWeyZrTLAcIgpysoh6Ng-dhrfn1LBJmCdmu0MBqmU6Uoe_TgCAb-b8oT0UstjkmiYYc6yZp2dUkLtGFCCu5T7tb4mgCvDRhtP6dTu3a-wO3bTbNJ7VVu-BM0b9F65-DAk5oVQIlNsQZQCedbIwY0cE6MFe7JRrKooAvcnrTepEzF31424xdH1ofkIXmLozU6iLfvGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPL6xB5_jWUUNQJZ360Bfm0vdbmt_RvE3vfyBh9gQxOOnsdYX6Hj4ZQyYYPHX05bCYNR31lEA8TnH9yeFjJz8kSTmZxBvzNBiZyk1aela1on5hY4jBrK8nofBV2QuIpEEG1JiyNZSFk0BxKyYb-zld_R9TVqk77_QaK5vHRLB9ob72GMxRTWqWKePBKVYL3ARs2dhLNk2gjDEmqTa2g1uImQaEc6eRYGDTTbVLAJtSUr_tedxy24qYDKZZw2dFEfc8WVfimawozf_mEUBWlgaJlepl-Vecv-MolHv7JjQAVbZPljXhCTlVEK_R8_lT7j2C8XWgX5V5soTp5JaqmawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=iKOBgMXkCez6dEsGLUTaHlr61WNHiOdC6aM4OBDHhBB3_U88839OaV5hteDXl8RAXP0_sJDZ6Q0eNBKwRGltXPpRMHsR5OIXYhb4MU7PhQ5LvxZhPEuGLsAvICcW1hZ_2RXmIKoWtltfiiPrlQjLiEhPV-qakZJlUp50BOJ1nIQ0OXTDc7zTW0BXjEASDGI9tCrBKpWbcw2YTfiPy5kE6ELHM1HnwB0ic2NpkBPD3DTLcZMs9A6ciIvilalEzgtjYXZMDw5kjl3nJxCFFvCn6ZFqacSyXY_IrrdifAphz4ta_VoWGOA-p4tP30jr_nTsyBtpwbAYBybrZT6B8YDtaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=iKOBgMXkCez6dEsGLUTaHlr61WNHiOdC6aM4OBDHhBB3_U88839OaV5hteDXl8RAXP0_sJDZ6Q0eNBKwRGltXPpRMHsR5OIXYhb4MU7PhQ5LvxZhPEuGLsAvICcW1hZ_2RXmIKoWtltfiiPrlQjLiEhPV-qakZJlUp50BOJ1nIQ0OXTDc7zTW0BXjEASDGI9tCrBKpWbcw2YTfiPy5kE6ELHM1HnwB0ic2NpkBPD3DTLcZMs9A6ciIvilalEzgtjYXZMDw5kjl3nJxCFFvCn6ZFqacSyXY_IrrdifAphz4ta_VoWGOA-p4tP30jr_nTsyBtpwbAYBybrZT6B8YDtaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ai_kVNVjA7XzX8ndpxz4bZOnCUmeMAF8tHvlByRAJRR2e-RqeiAKSku-Do_R1w1kCk6gy6eT49NJPP0LmL2PuorwYTJFiV0IuITPAFpbxh0KgZXaAuu-ndUlp7IR2KcvZKSKhEJMz5VhE3BdelC-IQUv9NukrzGDWwx-OTJnnH9A-Qix7QrQNT2EDg71zp1fTWAD5qmlB80gIXlOHKevxBUuE-DnjJiefTZXO7J1waykeZOSPTN23BFDzRiI1QXX9GKI-KIwgs9jZzBa6FMK6Yg_uqAQOkxpWCY4Z7k7wzo160CFqS3BmIx8Z1eQD_J7WQ3LiQRlCrTUUeFYbONsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jM3I117Y2L9chEEfjCNI0MVtfoAF40kMixMkJ0zEcSWC8dZX1rURI7LBZTsKppwpcABhynJTdDzG89aS1kZIsIQh6Xvt2W9W8og6V94XF-Jo2EMnOlwYTGQzPXIwTiMe9wyzbFOzDb8D4Z66B6Sz31GMm1jqUONrSAzNLoxAC6fxXRa7vjFtCQLM8RWmCGg5jEPhsy8sr4S9ccwkY6JhQU_J8CTFa8UhSXpLaN771_PM3SyUZHwXdIuu24oshSQ48uXMvsMJw_lBsCdqHXjfwOPXpdfzsnX2pyPPQV_nHK_BhopOE1fwJaF2bgaj45e3O3FCeBiWHAC3hoq69YV0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lvAXUMzWZKPcWoTvRezUvzWp76h4cZRMGKc6ZCCyUDBl1ndULjprlwTQKa8YZQPyQx-6D_htqOSjyv_PA6vJ1KIr6vJHCouuKkosiqanQT8FfzOOV71i9cBILYjV9QIZy4FDlYKppCH6YJ-uXbSJpRJgLOM6hXJ_KIv7T5rCDbVP6CDveqzJkArGJsLFct5t7qkZ030LfKUiso0wwQUEd0OxOWEonJVSH9QsKrZX784H62MBLpalHiDNfgPYDYS3yJShOi-l6qUJUIKvx1h9Dpw46JIYyoR_iDVUEA5GuAjDvtel6TEU5l6qs9jaSGMeWoqT7cEbp_s4u0894xMuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MB9w3XSFviEGKd7Y1HSg3TTWAP480Zu_Loqwlly3TN8EssAzCCuilUcShYyEXzKFcLpglhYl_HYUfp1SBHcGHD0f311cmhUaW4zQtQoYnSeD3PdhY0nHNUl__O1MZ8Qzq6kMZ3TjRKPpveBW_j6UupuQrlCnlbA5WYgnmlJvqjrpmwmNzZ5TuevlrTj5XymV1gX8yN1GOBGMD42u92BzM0ImhrtxUSR18iZaiBpHc8NlI7up-vDXxLkiprbi6Il_78xlL7R9_bHLe5SxqXdMFlJyW6xWHvglAWfx5GbIF9jFpUCdbopnSTPn6KU-zdCbC0dLuwrB8NDtV5cyBl4bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gdUYU9HukAlyDxiIXyIjSFo-nItd-fw8SvWssfhFMfoITuQbapQEl7k6gLoCzKK7wSWEzWW2G-mDQTCbNJocq1Ajy6elx1WbofsOIZ5w2rWCer4FKs_4ELZekfgtOUv7gWAfysc0_nQeTeakpPxoBIUpzYAidB4DaOA9LGI7pJkk4xUenBmijFFiELjEtINbCK5bjlzMVyGNr6DDz0CCx7gUkyAoZLtwxViIvdK9BWX0ey65FX8v9Z060CyFqKjBjnrkwxpXZWGm0JUAwnIzBAutfWhqor7p8niCORqMGwJIYyK3XxRlPo9J4PynYbGIhUuD51H6TJt6oiS6jtDkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kwFyK0Nck7dmTpnagI3W27GtjJADRbKhz7mVZSsOz2WLkk0yPHLeJT6Z3v_XRsq9M66dwWVli_SIp8PEONyS_v18me1_RJO8rzZem-IkDfwjw5SwjI3MZ1FXUY4ItrYEznZlkOijLtc5fjodHfJ2AF4c2Bp_TxUxu_mdO6AxEFCapkSlvVBDOg7XqDQqctYhnz3jXIRCjhg9fxbICtzO5Hxbc8TBslTSLxvOXDNzcqd212BzPRUsEn09_rxuosU9sbFKkeWqZ8Ehq8I1ButRhlz85tToQZROKX3U14vh2O7bpzGcFb5E6EVknwD-V13RUE-nqcp8pfk8aJ-GYPPliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5zZun_nZ5vIhXjqtC6xKUvErmRjj_ut0tBaGUwSwT72YwBgpWFHD8wiMs2VqtVLL18hUZxeosi94Zm55DlEPxBHRNlZ3H5gujyCh_7djHY5Z5iUuhyMctH3S3JNAkHQOIP2ACpDYwBeLHIwbMk8o3u4oG10l7E7HrwvkVoARonO7uT4BM0LulylBG6rIeyTqfxU2-z7PiP9l1003qHDNb_Z6ef8cg11qzbr763JaBKQv_lX8Kc-QoBEmRhq1nkfV5B4VFg4avOH3w6JqaYAIFe3IM-klLPdZoijxUrc2ErzHmkXMqzF08b9P4fajgSv_2nfzsbY21g6HgA6X7_AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E8_wRI3ucuXr4N7Nl7dkXtQZkVH14cl7FATpMAPKakmzIlVbjLOOx-dd8ukl915GJ4P3cUiWInm1SMTKwfW5NYWhgCTvCQG8zRVjtMHCDad7cQp1tQsb9cLGmGvpGDHsZsF1nDkS88rzc6iNU9aTIpRSfmbUoDNHfoDqyt6NNdFHmOUmiW9ZEgLEtLgMR6KIPmS2sA4EgAyoyUhnfZXJ9ty7scQ0-AiKc1k36gLYMxqiM4jn4AyyiM9SrZz4q6533fd4ld2VpKkJylfXWf_62OF3HBd8mmmxqBFsk50dA4mqxvcF0AeBDsdDnz06DQ4jZKBSTpO7dD6MLRdBppT25A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw-KsWruSaAqQCJ_RJ-XXkmgobW_MdrSZbh0nBpLpBlvId8fO1HtdUXWy1umfAcU_s8jSr-Bf_F5GpKX45jA-lFPoQ3NTDvFQCm3xxZEl9wzXftRzBbRKtFK7Ks_iYWG6HSXTEPo7qxEbPvoPXeI9unF5dsatDrRv_mQk5UrhWptPheBHR2Tl2X0qcqdED9_MqKgWIYt8N2suOm2p-TPaIBG0riIHsJ5X1bzGyHuz71C3Gtypf6rUoWczJK8dydkRnlexfZLF8B69nvgnU08oM8fX2sHmQ7Lg3jo3iPMNcGr6EY9BG9LrrPXYXAM6kPhkpO8ou-w09TAFSXgLUqdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hlIWL06yH3h5FTIWgjT07iPawDB7Lrl35L8RUuz8qRefIqABCad0LgRvhRHP4yG-jlNhR-3zei6-WtXWhQEMaDMdmVw-jXrPCJDDpTCmU_fM_80rduhYB1nUBpseBhbe2vI2NeoAnOGLXrzbotI-hR0F7mwEHlzHjS-vrAj3TQ5MSSJAr6GnKejGUyaLwBBKFoELgIEXZNzFpDqlUmmGJ6wUnpzoJtJlHxTlVWL99lQGEK9UEo_HkOuZCK50YpS6DTE0sNPleQ_5qok_P4cpteeLX-_mfORcy23PHNTzV0LN_vryyKLc3cp3NG0M0FBXBKd2cmChKNdG5tzh_IVotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJP_b_laUGvNeJr1bbB30RWqtn2wW9gptkTVGLTH8-f_dtn2RWy1j2dihPZZ6mJ9lmpJ0x0mXfC88TBfVMl1S-1WDwrDAK4S1SY2G093tWNhXdNWeTkO7iNY-oulyljUCH3Tar3VcB6TtlzdUYwGV3w5U6KW1g92s6NP_CsXDNd2ecOYW_f51cMvAb4r6f4SsjH7GZ_RFPxXuX-a-SrkTrAmZQKMrk0wEV6s_pY_0Fs6D7JtQhLCVG5k922fCsSShw5qQqz5tJc2TRNAWFpHSq1-p9v2vfa6Qq1l9Wl_07nTBWZ44nSrrCMs8O8EesipKSA6HsJKhqliysWwCJn0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GIw-s61MobSs1w9HpcY_kPbqNfAEU3cXWBJxToW8IfdMCjjrAI3uH3g840pL0vCWhn6h7K6d9XFwge-YKucVCCsw1a_--su5Kdg6f62kdbeP_EJJ0qrhH5rQK1D9Hu1fwHsWmjvhW-Q3D4fA6KN9C2rRPjFsJgjSIOcuuwg_Sw0gPZIQybfEUD6xcTkY1B9HASKaKRWrKXnD_L3-dcJSz6wW7MnSAUeDBP0FBJwOXCjOtxrnOvD5NEF3hFvtZ3zGlvY399kvt3GEDcss3tgw0pyqsK3xrYTW1KF-rvToSl_A2WqwLOnQzY8QHiv19FAuwc65p_utipAI8sR5T-OajA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1voTnNVfmIWq7c-nOFP9z91Yi9xxvAXqLLFRH3uL20jX8DzdBJeeZsSOgMzyc0zX53SfDH_A1mADPwTEtdSIReZagS7aSUGK_9bJPltMYsYDGyPfUwgMkCrFCOwYDWD-hYaflojAamTs0qADi0zGibZcO_-zRVqVq7vMU2BSPKn3TxBdz_udnOqpr1BxWB5lwQZj67Iy1_FuWVfFnG9l4-scdLWrSHL7o8FT2TT7jBLBHsHIORD13B84LBo36N9Hs9fnNTMLjXOxecGMhUkyfsIcJoV2AJIyAFySDOLFVrgJafz-2yc2oWukVbkj11SAQz7zrKyQxCez_Ppo0UyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAt0XWpClB7slKX1cDllFbkYfHfl4P8fmFSOBWUOMkmI664TIpZAZs_AlR9i3-SyBJzXsxc528yEK11BjRveYCLjm3nIDJtfNqwZgrn7P8k823n79x57h9-xsHL6KT70XhZNFrN3T97cOKGGGyVEqxYspJ4kFJvFB2xPskaRuwq8C5HZQLc7Rqxpe9ferNV-5gwAg4A8Q5AX65izOUWUWArjr8yWzGbg2vF7E3XdQYXT_FSgkA6aEVM8e81vvChOXp1LxnePNapsdG55_veDp8ehQXY6WrJNSq_A30mqMHWmBC_J-qxzdWhDAcelQLjIysnGYFUpqs89xltjrYY1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCp5b7Nbwjy-eX554zR9v1oZPJAB9YTg8cGHAili4zoLESFdcWr8kemd5oJSAwQ6Vv5H5IBOe_9McBLpmnKtBmkb6VW9FkUieKtu5svRdJoy10jIpwkQArvhfVlusoziu1iNJX74BFR0R_vFCp-1T3SOUZblFb9atha6gd8pCNf5oKLcy6gwJA0qYBZD8EUR3pdB86UigurBsGIIiQZQsMr-m03XfCjG_ucDDgwpQ-1KygohD1_-X0_EpN4g_Wt_FYib6Mf-jt2c20Ipro8dRtKi3A6Ojb9ENYQa1fFMgMHwo4OmYUHtDQIt8PRgA_wHfw1WFISA-JXv1aLUUnORmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tufAJGpSDXFna9ro_6RwVzBZy7F-TDy41yo2coLK37X0QXBsBL3VAaIECVrdA-OWVLQQfmnytjJ2DV9bO26vtkCs4H2aAML3KCLx2K4RRgYb4Ww3TYEM9IRpQWZZl42rMEZPDSHNC8-wcxSpXbirhBVbifWSjAJQE5o-Veffooc-F7d-FPYBZZrdzYj9cKsU9nivI5AodjIR1TOwUzIdd5x6J5jiDJm3sVVRcqD4z3B-i9uEvnJplz_czlJ37oHWJ26rcD06a5iLKltzTjKNyBS3U-iYDMWqM-CRvfnjqU4xt6nJzYybFB9SYk6hzzi0A9MlBmr_MhYlTgIHOcgRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YhO8SiNCfmlJITQpHZcFyrcGIsNyju3ktJpLs4K2OqCZDrCToEySdpzUojOdiBu5KFZGldOKU7oIRLJL0bWn9C72n5D8BLtIJbVpSj7vDF5E583XVwqtW9TDBUkr8KYBm-RXvGbRYAYg1Kkb8YVdA1yLnRraiRrCsqt91-10TikL3JeZ1myCZVgypKf3MSc3Ulvl7DhWvKvQBG89SDmI6pE2mB_rNfcrm6Gh8FbXeNjr_iWYkYW8zvKYh7H5CI1wrn8an35SsQiVus4fQCywO5tMTD7m7xcTNMnWP7NXjnN7_purfslvwOJKEpWzFDpa-rl4F2isViT6EohywZkDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wn5DsLQEU35DqDykq1j8MwvG_DWR_oUbGi5QkcUTmHf-i0RhN7xdh85_10g6xu7yMkjoxvMu_Z2xpbjqzzODvMnFBsivfvXsA0WXbYbvoubRv_bkEJH-XTBbQ_KeqPhObaRhpX29brSqFhXTgw3qkLW8m-Uz8dY2rXmCaXebbvh19_3c7NnVoplOpp5ShABZvKVlcoz7emDwJUFDY60wiraHOA7c7_u_WhQEXnF40BCs9M3m0DCMx1NMPBpqdccE5NKpuoz4jufDbQAuYr2PIaLcdmwvzN0WdAMp2H48uUXy8icrQJyaipmhRLE69ZyVYQICp7xPr5AlsZsjiwDZFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2JgrQzWeXSt9CO_vVNiPjAwdhgcx05AHTxw_d5JH3ZgDHJp70pbIRGmdwE9hhSoNHJaOZ7s14n-90qKD_aQxqwlLx-iE7ja-3AYcW7hJGg0ErUnXaNklCnVrQZ2phFuz-KssjdIi7_LLa6PSKGlWTBvOip5vUZ4PS0FWyYZMEfHMZ7wyJKMTLCd-uVrhnscLpxRefXSnro_r7Hgy8dPFaYJkYAcipuVCF-zAEf2L4fczklEHzl50XkZdsdiSBnX4qCj9bYGstNTYGRnT7jnxbylNO3rk68YomahiIlASc0rHAfFXhlzT23R27RMUsTi22ryqgEktX-CYn-rIrHdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0Z96A6q9Bz9PRS-y0mc-tNYMZyS63GtKHQuaeRZIp54mz4pOj4WL8duIh9MjYBFUdySXJyK09cZLHEzUuula0_IduA4qkSFv3Tvrge6VB0p-ujkJI9F8_W0N6cg0Aa47_MFhBWnX5QPkUC8NeH_E55s6_xRjk4zCACZRfIszKEKkZ8y0E2ZTVI9Un3BLsxQ6g9cpYs1TMdTKFE2VWSQpTzkhbf8aw6a487XCKn4NI_p0uE2NUdj9TZstce9YhQ6LCAGkt0aR9nmae5UaDu63u7TfucVm6JFnurtdNxfkhloOXwn6EeSxdN9yEaRHKdnpzpNVuzTsTA90CKggZQyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kPCBJQiF56sr9qt39XuAEpjIxB4l43VHI7KBh78NPfwcxQQF_yDOoMpmmxp1xsDouaUuHMYpF-UXR6UWiM00eFgRyrVfwNo5nKjOVMoN4pTnIUk5tuTLUnv37zldLiAQib41AkOzocLoI32qcJU4kgazys78mZL3Vc7pLeTJ0kXkgND-hGlchC3ioia-p61XloDZBmEUvslitlslUAAgtPH5GGPETXjYbTc0akVvfxygmgHgpoKpXuQaxK1CyCmTrx1gHEq9zN4rTDyUMuES4GF5FqVSh2VAFei82LAXdgubzvykbc9Ryzf4iHFFHXeC-22WYlXP6J03HWGceabz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgNj2FE_7zJEkeMwS8cvbdeOb31Xt1G_acKzD44V_E9oiEWkz7ufLuwFkhOIkya8Ngjsu-TRiu3VdudXG71_F6bWzaPVTmc1x4jYf9Gl35Eg3-PJiq_QoDETo3TQMauHySf7s5acrbONEX2l6GD5LVwwzeLnWkgAYx4aEnHixTpkCsveoNxBiC1N9uJs6cYVUEAyPvaRHkcctnSgGnXKfBC8qSf7kM_oaUNdqm8w7umQsi_sAc7nS0muEuRFfdpoPU6N75PxgBBN4YxDZUlXymDpmlH9LK38cwNoQ7aNjdma7CEW_aMcm_lTrANBcbzYoqBxP1VQn2xq2bkaf8X-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZpG4tjOFfk1IxaxZ4gYfXdWoFmRpS--QZSTY_Bv02gw1wPqlQz5Ogy4HEXovQ0nLP5VjGw5YzVmEEkU269WphiSazctzQhwLRNBnMrB7qdMJ1KgSix51AfV1wLImvkAIk1P4z8E-K9ULVqqfzzwWy17giSCoHx4j0JB0FKMmx3s4Ax7fdR3ZUzI5mZepql0o0ZYoUbjS6GEYGZKEN6XVuFCRKMAN21FZnh1cbfZIZ7r7xvzqz1ZAxDvmCnhJ8etQ8nJdYb1TD9gkgcStw8wG4HLkF7qF8oL8maGPOAS4B7PIvs1PVGPR0zls2dYBr_P9ycnliSGokKSHuyZ9WVibQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxFRmJTlPuuc1vpuGmReCL4IqTw_o7D9kA2vYZ_Ii843qgp5fPF-1RdP9Bxta5iLBH_CsUVZX0Gp_kiRGi1JzDlI2iF0dFfDhxatuJfDv3kacqL7vAvRxAPXE-AE8AdvFAzW6H0Ga1kqyixQ2FxJVVEAevrddZa9PtCCcvkNDNJ5TFmnDUf6BXtM-VuiWCPJx8wJPUkVDchwLJLwu0nPZ5iM6apVwBlspf7y-Yb6lke6uPH8_blJHRrapU5iaLs2zayx8vlgaddrILbMyZjoKo9C-pPbYpI0LNWQ-RTS9Zr57foWRuvs5UY4iofcgOAy30qnwuUj6H_4EJGfRs5RBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDn0JIWMBN7VAjbCw_6FUSSBu_4mYGwUyuX7sWAtHH4GJCOsxwMLNSYUsCywIjzW_s7w6_bSpn-l1gGtgGYyOaUCTZIm9iMrMjDr5upxs5AJCFXpjb_71GSg5By9VIawMBoEh0aGQvQmRtFvjNDDL6SnrknkZf367jpvT4tusrV_nMqy7neTjGimXgkRqJ3QAktisBCg5JwWDmkRO6-QjzVlGi7alTVxz6ko2ZoBfq_NXSJSqYWUu6eRmAC_PBHlEJdMIdwha7r1vfFoJEFc5yvrEogDxKE5g0ZTTJe04z93hFprgHMnRIpzq9FRKFOeOFaF3oRza3pZK0NV_XCboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmQzeh6887eNGyqP3R02zL7TTCDPV6iOFTxbxFge1KYAUnrFFCnlIUYjdOOTPUhRTnJTW35zaHUcw-7efURwKAUM86YmMiDj_Uq9ChEzIQSgMCVIl3ITRG4GiPJT63dFbYDVmzHxz7rhPm1nyYuAZKJywXlOItCn5c4sf0TLFt71umxKzwjEBhMRXJL1-g3PwvkhPipx0OPUY2A_gV3F1toHKXGqaTMMPRcWAFKAoPM-gqWUxEA1wqgDVVd5zLRycV86z-ijxOB66v3wybdSFBHpAFNgETM03yJ4kQTX8ZNFo1dXrI-EW_LTSxZHuI2uYN_da-ipjf-qlemKGVbJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=EgUY8H0CL06SiPvXlmonVj78tJsaDqp0PcpO8YfaRT9WVjuy4VjOE_yYDUtHA0k9jNHPL5EM_6HU8shLkK-cF_lkJI7k1TnYpyjELlXn1LwulSoOrx0I4NaKcymiH9BjdAnq-O4P1n8gUUb8YvlmHGmbPoLloqAVykDkLbWPJFrpJ_dmmBFRxFJilaT8u42ksWHC6vxMBu_pWFXVmc2InGTM0dFa4aIn88WC5MDR6mXRvkKAn1wPO1JelPXbO0dYT8JdU6A_8zQD_7WwudymmuoUP3w1XpqMdFKyHT-7FmP40OV7p1VkWOqwAeelkkCJbOIaRO0slfB9kag_bbHr2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=EgUY8H0CL06SiPvXlmonVj78tJsaDqp0PcpO8YfaRT9WVjuy4VjOE_yYDUtHA0k9jNHPL5EM_6HU8shLkK-cF_lkJI7k1TnYpyjELlXn1LwulSoOrx0I4NaKcymiH9BjdAnq-O4P1n8gUUb8YvlmHGmbPoLloqAVykDkLbWPJFrpJ_dmmBFRxFJilaT8u42ksWHC6vxMBu_pWFXVmc2InGTM0dFa4aIn88WC5MDR6mXRvkKAn1wPO1JelPXbO0dYT8JdU6A_8zQD_7WwudymmuoUP3w1XpqMdFKyHT-7FmP40OV7p1VkWOqwAeelkkCJbOIaRO0slfB9kag_bbHr2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=qzWhhP7jfaLNYJpXnZ7eF29Z1y9MZ3alfoJkeegYCIEXsIJe5rk6vBJtvhfPa5knk5aolwc_7rjmVgtTecPmFiFbVfmA8XnaCjnWcmXx2dSEn6EO89WFVkzpIF5B-TufDklJzVSGsxlY3KEMGqBeomaON8Cty3UcEBD8c0iHbEaJPe2ZmqRFQHaD-FPyzkj-pr3hEmNZtLrgvAAVke_8UPkPywMtXWxAr7oRe_OuWETc_h7DJ_rODHIR6KsFzAT-ULV7W6YoyFJPXyTfXIRK98wBhBGET78-eYG_WuE3V49kHw6qx8mlDYx1KX80u2BEkO2vwZNCk_XK6J_xQ_Paaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=qzWhhP7jfaLNYJpXnZ7eF29Z1y9MZ3alfoJkeegYCIEXsIJe5rk6vBJtvhfPa5knk5aolwc_7rjmVgtTecPmFiFbVfmA8XnaCjnWcmXx2dSEn6EO89WFVkzpIF5B-TufDklJzVSGsxlY3KEMGqBeomaON8Cty3UcEBD8c0iHbEaJPe2ZmqRFQHaD-FPyzkj-pr3hEmNZtLrgvAAVke_8UPkPywMtXWxAr7oRe_OuWETc_h7DJ_rODHIR6KsFzAT-ULV7W6YoyFJPXyTfXIRK98wBhBGET78-eYG_WuE3V49kHw6qx8mlDYx1KX80u2BEkO2vwZNCk_XK6J_xQ_Paaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DzqhCVSEHFvOs8HTEl9h-adkLm7ohbq3TEyL7G2QI1ElebPeXNdkX59moeRlUB8o310vvMNalUkL6yJJcUJunkz_TYs2z0GH0zRDDL9iAFuweNbpuwQcdIuLgWXhYLhetW28S62S_zNhdGVP1vJwhyq9jGL7o77qHbxmHytYZWVPVDOYwnGZIee2qV3JAf8mdWEWH5f8lc152LdQChGvm6VvNL0Nx23lHfDU6qeMdAnvnak0NT3TPYBRqJ4meOhV0aTMUcfxflUkAgMSHVsjlBVLZvuDdX4Eorxvec8HK60vTxQ15H0OxqmAaY0QKeGH6Kpf7ASQmSZOXremxfv78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hs3J60-Bv5mu8vlTzFF9TuKinZw8wJ75I--OvIrN-uv6o41IotSwjB6fcQTQU1bbODbAQjRyhXFqhlmzpvcLiK7fPgmw8O4149_RvWHQ9_ahii3MBU-j_CxaPd1CzueKpzrZIXQ2faWSqe-Up8l6EzX-4yMwM6IvT5fymLO8i29n30UWpTXlOt0-u7xhRQMG1I68qB5Cvm9r2E7EpmH__cdmHuLBJzyyb6xekY-gZoCdGOhYovXzEWrpHfB3zvTp1guT-WBxKXM0msuVnzWh1ws1njAMW-KqlAAf34zjZ8g4BtIfS58POXbVu7mqaNm0iNuuhzZXZeOsbMiVlWEZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QKDi-uUl8UKY3hBSHQPwndDr0cPXurfjibeAFePyuzHdYOEZxcYc-QhPqwNiAJeQGWTVd3tj1F7oAo8scaxpuvU5Axgvc37rJtTODCnxnVdS5EUYjeqTHWDHqwEs2pw5jGZ4StcrLx_IpFNOsqniSJZ5rUWsDYwt7VS5qvVKDPC_5ZIwhN506Q0AG4mGH5EVMJl3De_jNTCr7i8GfQF3oIvGCgdajqWeDdluWRkbUDrDFbhXJD62R-sh-NYbxPqiaWlZX-jmewpexBSw2WPIi_sn93Vx8jn28I-t9b-hUYayG4sIstADjKj6wwFsGMpcH36-tk8pPi-xAn9CzjEBug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QKDi-uUl8UKY3hBSHQPwndDr0cPXurfjibeAFePyuzHdYOEZxcYc-QhPqwNiAJeQGWTVd3tj1F7oAo8scaxpuvU5Axgvc37rJtTODCnxnVdS5EUYjeqTHWDHqwEs2pw5jGZ4StcrLx_IpFNOsqniSJZ5rUWsDYwt7VS5qvVKDPC_5ZIwhN506Q0AG4mGH5EVMJl3De_jNTCr7i8GfQF3oIvGCgdajqWeDdluWRkbUDrDFbhXJD62R-sh-NYbxPqiaWlZX-jmewpexBSw2WPIi_sn93Vx8jn28I-t9b-hUYayG4sIstADjKj6wwFsGMpcH36-tk8pPi-xAn9CzjEBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHkD3Pbeha8zIv39PYlmaipuNAGEsgYH8l8aQrpybjpnCUXzUOuO-USHO0A-gH4TX9ZjIOTJXI5fCG2NPuh8VaWC_tHeaog6aiorvq7b1XJFocVnfB6_fOhvAZkWjmMU8nDLUGEkfC1ArwABsEhgG3wzUrYyXBk34kjpAGV8xmzYC7MHntEIvACoAZZ4uF40t-YLcXTb1ZCWSTdFPAvFy63qb1mSvaj6G4PMQ_974vD2NLHyCeRGASovftV6vE4DW8yqOGqMV8Qpv7HOFyOGz6CZY2kvts7D9o_7ZxS0xZR1AwvJKa_BrJ-xSE1dQ0-ot_iqm3SlSLDfXzyHALuBMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHkD3Pbeha8zIv39PYlmaipuNAGEsgYH8l8aQrpybjpnCUXzUOuO-USHO0A-gH4TX9ZjIOTJXI5fCG2NPuh8VaWC_tHeaog6aiorvq7b1XJFocVnfB6_fOhvAZkWjmMU8nDLUGEkfC1ArwABsEhgG3wzUrYyXBk34kjpAGV8xmzYC7MHntEIvACoAZZ4uF40t-YLcXTb1ZCWSTdFPAvFy63qb1mSvaj6G4PMQ_974vD2NLHyCeRGASovftV6vE4DW8yqOGqMV8Qpv7HOFyOGz6CZY2kvts7D9o_7ZxS0xZR1AwvJKa_BrJ-xSE1dQ0-ot_iqm3SlSLDfXzyHALuBMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vmCnUA7z5BfNr4NUTNxDzSQ08rMF8a6VceYID_Fp_kZN1dl2gOTfrUJKII8m9n-OAhH7zo6Vcx2SrTCDKTJkmbLVnNYid1RiKe9p85IJHSHctp3VM7yxFIkpZGb2FQaHrfheCyq7TmDiP7OWBzdDDDpliiQuUBxzBk-A5Drdsti5-ZpK7TWbyqc6TOR97jptbJ7ZalXEPCmv_hOoQ_LSALKFcnFOiG4JDmNeASSB0e9v25D-LQoMwa4Giqh3KH5jdpnJqVCkmGYs6lji_tE3v_weJEZ4_TjybxwjdveL9UjKiKw6dBi8ne4eW2zpWgQGnjIksVwqBjytAzdXEzQxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0ax182f0BsD_xF-hjHLrEVc0oDUHrW-ri0Ix25uLkJ7g1PqmoRaAOT4RSL6fnASLHuldaOnDg-p0OAIVaoDv8AZ7qZpNY4AlyTd-hTZgw5WX125QLhht8x9QLZJH-V6I7dTCUwYiS2eefeLQR7pDRepW3-2k-Y3gXD4BoB_o8MiFQIkoqRqYRTDoM4u6yDCunwRkozod3wRJUZsA2YPgUNL7Js4oLHabs4b3aPhURKlIdFTDSbxW01Hu_-b6x8joc0_UmJ-vnre1RQJ4HvK8-_xv5Uo2KoaVllyjCURpez4S3_24IzRtb9I4VTvFS_on69o-GmBzdrTT3__5BhpfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdZLlQ0iOjy8w5VGBsNjgJiLxaJOWQEE_hXeVLEd1gs_aYWtXrrbamhX9TPUldlk9FMTviptrrM4zhOcKK_OVpLOofYNl33fByigFGy25bKezBvEpReEe5HUNUWC_9kLWLs88KdoH0Ac-J5uQ2sJ-Tsdi5yfsXy-Zqjz009TvwUlYX8R3a-P0AscUk49nNnY6YKPqDnW3tcdJylsltE5Ruux5H91odWahrni3Gsw3CpYn8tpcoNZFRyXoD1uj-GeBWaqk_IVum_VU6dzslT3pJlyccBm47B8KZZ3qpiXXimHHCpMLZcbE5DqEh8spZgEn6xoXso-nkQxKtV-iuWvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjaWr7CsQMYi2dH7HSO61aqWh1TIyqQU4AQMVsp8J15M6bSojUPjA6P54LWNhZM8LmYINaLmsf7HftxnQqOT1pxKVorH4dP0NVrJg-6cVX1phw1j3slmv24vWkPRZxB7_IvPuHPmj4YMQ6C-dsw7X3lfhTGwjZUjz05PrN0h4J6Yhgajv7OgZjyIXO_fClMANpFgM6bxq6gG9jRzsH6k6MR0apEuvYs14Q_2bibEluJGfbAlBXLbX-pBSLO8WcckL6Aahr6rtdA8_wLw9Fyu2c2atmz32mrXec5qafcSYdYeaoCmhF384fXa88RHcVzYQkws0UPpdyOYc5ljDEmQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLRVX3o2HVuH2iSSo36RHzxgab_gHRR1yOyclSCHq5g3_D7c7o3tA3KBavMrYq6tIU2CD1CNRGejvm_suYDdOKeBIOiD9kLGANxl6hHdPiGRDr04XKByU82RPdaXpukQTlIsIDxaE8lrcOer_7X0U3-rebGQ66H_cGr18x3eGau5SxDlqaszXdVn15ttUEvChKHq-w_6WPOuv7MRkmiji9OBrUykHRa6NROQeboeDQByvwotlwgmKKuIFYUyVum9itODD4r7fKSBG8SH_OOAUq5W2IvwuwJ4AS9buHjyrmgbTE50pamFcHNCwSQvJlLWTBeftB-8y5SFT_ostbvAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-e1rkmQkxMG3XKvt7iutQR-Oo5l5Dr81Ii1dHhD7OBokB6AD_uRrEmyH2KRX93XCnxBSFVxVlBcMJDp90cl4WS4zhVu2NnkPRe5TGQw0UkJfxChphSJIdl25b33mv1W2qd0DG1F-Ll3gfLy3ilW5YpOaI92XPDYSg_7se9TtXtk00rcwe2oyi5CM3WFZ_SpeI5dYzU_0HWkMjzew1y-uqWxmK5K8OPpohJ0We0yjVrCBSjGvUfTFFg28cTPP_QKDmEAuuzygLZJg_xdwJaAgAuJW08MAIMdVnLaOq3sgh0oXF3zRvrH3w3ZPldC6ET00igRG7bQyCLHMm8CMcnZUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1WLGIzMG8R5wZAE78C5mZEsUiUBUP2I0i0-yhoiNWHLEVSQJQQpUhCm0s7J78r-QSu62kPX4Y2fwd9QMbSiSXn1NfyFN-_v3sgLhoCIgnsrt3nP90g1iD_j8h8jw-ymNQuaHNaeAUKLgrYTaSXBvmxDEATT_7b_DolLhnbksXWfLPhDH9SFhzZW3lm2ZGUlRQN9k5zjpliKruwcKHDF7WG_ZAI3y6ZnQW1cvhEF4XWlv-oEyEJn6qDe6OW_BRIwvghBXGlcA3wD7Psm3oH5T16OsOOQDRVcS3FomN3b-cw4J32bu2JYmGPrSVBwh851JyMTakPl6q9LZ2SL0eh01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBp8YF2MK-qXFZA8U2KB1PtYvLEaN688GBzhJJwJAb9iaDq1VoN1joXLDWK2bkrWngJvBTo0OOu0DPz2GKeEpFcYh53RI1qSjZN3dJLj0WLRIxaknDaM6eyw2yqpvoXLXK_s-wofCTHlhWWg2PTzTz8ydQmEI3mwY6AXQv1Ch-yeN0BN8kBMuyIPoZU0ZD0-io7VaH_IcXIb7SUg6xZKGraYz6SkDC9cJJoMXVnIli3PoH6nuxJRcmjMpBwM5xj865MIuhxH0wW2_fvgN2qLGL-_8PoEqGGpcNBe-MvpUe3V6whCrDvIcBAXJ5-9Gh7pYtmifQpiurlGvupuIiyAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HVpsYGKsKPXV2nMj0W3drwbVwTOcD423qj7UwGnz5WuxzhDj_EZcRMy43ea-42fvEyp-lPkS5hn4FKa5a6LGRL_NdknZJfuYjmuYBvQliUfWwm7-lBzRaSzM_9L8oCUVpWh7cKDtRHzWMa307RXMhhA8EVROC2w0gpR6erPNSPyKjXM6VJZRCl-S_icgfBRYJManiXWDDAZxBd9vpKT64lvFVNQgz8ffnnCpXJkE67dhj5aIJoEurBFqgFuFCYOBLF_g48v7etwnZL7KK7tn8zn63CtddtpC783c1YY8G_ekZXLtVG7GHLPqZjHcE3qe0Zf09pZIXiwr-6FK-01HbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5rWIx94UwgwsMXyso7RRAdFMzeZsXcdL3ZGw08ooiP8_sxQzXjNDRiQygOVvBVY_rJG_VWYU6tKWePn8lrM4jCx8DvtokUNWMSAJ6xaChy39bqSqc_6txn7rDUmnLJBJr-un0weZ72dqvTUWXylcxPqv9QRcHZWuNac2cmCbl_cuP6lEiQxBS4HPct3S1kRs65GHLInY6Y4vAi6FbTZraEZ8aYFCu7VXuo_9H3oUTMwC05yfYGcrTvhmRAbT7MYqFYFtmrC0nBRJjvoGS-a3AoODtgPREpRp2gF8E5jRb2kceWFAOyM5F7KVtI-GvPLatLCqJM0HiRafgZHopFCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzGnK7RPDXhocr9dJhtQ8TSummS2dNqytvPpV9rVS8yLuzlxD7ZbPELrartJRQksV-c328lm7SeaR9nt3dT1Q4nJrCrerbmLkaO7fnDMBditxfLuK6Yje8Y9JYX3hE9tFY_407rRQhsrAd_NLVmgea-xYioCv3NZ_ec_AlZUZzx5IJlUU1gGDom1JqShndYEhdUuXlrKwbiY5cEeHRXAlSeaAUr3r1624p4DUkrVX_hEkfh2HLv9IbkATSTlGHfZ9RvpVumfIm4MvtdhIXiOjOJ6W7vR6dx6MwbaxoHml4FMz1AdbnSjN6AOUHLc4EN7K08bK31Bql-yaaBAIeIvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtwuSJg3yA68dwD8MJoZb-efAlbt1yOCgS6KSJx1eYxhP7_balmsW30ADVxFt3pYZJOErc507ftvAn7_uXd3xOBjLwvKlcszuNYDA3t3Mn6vs5IRlvMztLsnU40BaqagVQJBle2BpJCWguPJ7X4CtPUnsUhQWpXLDvs5d7uTNTOHx0hkM1gpznABG3e_wxZyBKPDCWqN9NZcOsWKXi8Mvl39EksboF-Cu1SMda8fbSsQS8H2ofWocfQzbTMrz3oCwY1j1WqJ82xdIYe6yYISoR4c70BySgmXzYSiT5YfgkZEVvcezssrwPXOLdB9gFaXt_UhhINU79Sf3aG8DFgcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqgH5W57I9t0pRAeFcMDdCntFtsmiejSCUWYsP7vp7R5vFmC9F8lfh6SqGSCc2Lqb2HJ7OgnL5n3FcCxR1XX6JgdaWaQNhktA2ib8hCcPiNU97QyMhOz_2Nk708-OK_a-5XWBPEqhBhWie1tHHIjUd6nYVJt0XY-tp0B38tPzrAQWkPvQGbw3cYRRons5QBBLHk82L_TQprx0zE4Vujt1Z9usHX-EPl17ExQvctmAVNvGLvXxs4UwZB2h7I7m6Nl9ZXHTa-Qbwb6iPZY-Q5lgiyq7TIXd2jVHblSdOhu8EaVvXgl09yXwxgrPFTTebF8h9eWYRfqPx9CRdzalSZszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQVRstr38xLut4ZrcdT_mIJ8RBnlJV8rxUODpkMkIgh89Uic8cUEyxeT99AhJCtf2iu_hp3NqI0HZvcXjQAi3w96Ajn6FsDhXfRjF80Zk8yfI77NJra8OshC0wAgjFIuZQWQEsNMx0axksAg3oscgmx_Uy0bYJCjXBpmHWaUzwh1PcIY6fCY64KZgG60r5YsewGna-hjA3UYGIGfYz1t4mpvioVUJGZYbmJByqYfnT1tl6wK31Qq9Xqlmh9-YzbPcLZnDRkU0wAcW7z6lrZwMgJtGXZZxkthF09HFWzbenIxz-B0hbcNsZtR2Q417pLePjZvVlp2D0RrPWD7XR6jjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5RV3I5J7YcBQV1xAPThs3vENcqteF9fAbj9t6aaRT4Q9MWhlP0TjWH0D7tmw5vw8GiXejLBeuB1d3O0WRqR1hnX8wNpi-uDNcf3j_9s18bf9z1ZRi9NIBf3N2IQkkwJXQZeLEDz4EvgQaGynTR93og3i2oBC4ZKN0h-x5UXlPycCLS_jUTZSfyWuuNmaglbFovFckfWm5jTaluSmsXD6bsPAn0hCUiEK2QgWVsu9ZpbTrjlherEg8yY5EEGFo1oRPmfnH7uyQLrVRlchZUzk4ZXow9bS-l1CWPYXR0pU46oWEdNZ8Fq4kVK6WcAk2j_g7YblCTMYwMR2bG9weJ11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC9At_LlcHH51-9UO23V2v3U8X6i3mzkgXB7JsGNw7IvQXIm2ctr91WLUMI-PLdipS0Itz0TtE-ifzboVqWrs99U6m1Jf1pmGwRojTNBHrk0_EVF4jeu5vX-8Sgma8hVM4IM2qsIMTBaSjTG_nfGKbx3U_uNwQDdlwg8AjPwo6CGmAGXEfi8WC-hVd8Iy6sFGBdrUFt-8u_fIr4b8kJc-oLABDcG3FL5mPzpJnpXYNKEhTZGrhbqPREdJKiV8J9z6gIHivaFo7P7M8LbnPKqguckpDnRrygPjhcr8if1JUGOpoMstSTWRuDunXByaLI0Q71UKAg7QhmN5MrPQNKDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXxwakUBS1Fgmlu2icgAzlZFalxmshieshedEKy8M9e7dE57JvEi5dgiLmzwnNjoNre3915chQMSk6miUNn2hpUMsmySI8ngD6cA6lfLyVNT9E9Rk6YbqD7l2lLsNRGV1foilU68iGT-IeyHOarZhDV7U8DHlKsn_AxGmwrU2E-mvbpDq6AFQZ_ADTZJC-lHPkqgVG32PAIBIepn0ALVDZsc6RMypSUr4I30RE_QxapibwnqtzWDNydwHSYT4WMcSJW5oOiIm1OJnXszB_wDcrytqktraC9iDjNy5yJvnlAyN2lYHJpSkWN2m3gO0ud79VDPsAq1XYbT8Ns9l7h4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=qYzbcAMNl1uatWfxZJbxX5Iui1T8np1EY6yp6TH0gY3RBi76qGHRVkHTmeo77oBdMzXgGShMiWqCk8EnBUPNnKvYHPbZ7nJJW8M_c7TqfloThMMg6MBuRULnMOgh-WyIg7Qf1CcCwmMoogrogU7JiZCbA6fNXzw20JXcSIKHPGc-nQ3XXeQq8EkvR_k9kpL2FH7SWV6kCVkAEdYgpmpSb2z-uDhjs3Vae2PdAiLOoGaX6ejXh2vupEQu_gRNGmPuNbS_IS1LMOxGjNS-O5nWhUhokmJm-snMQSAIs4f_oSJQImjxGd_RWiHD_6C2qGlJFTIgN_pTr1TTCYnPlsyRxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=qYzbcAMNl1uatWfxZJbxX5Iui1T8np1EY6yp6TH0gY3RBi76qGHRVkHTmeo77oBdMzXgGShMiWqCk8EnBUPNnKvYHPbZ7nJJW8M_c7TqfloThMMg6MBuRULnMOgh-WyIg7Qf1CcCwmMoogrogU7JiZCbA6fNXzw20JXcSIKHPGc-nQ3XXeQq8EkvR_k9kpL2FH7SWV6kCVkAEdYgpmpSb2z-uDhjs3Vae2PdAiLOoGaX6ejXh2vupEQu_gRNGmPuNbS_IS1LMOxGjNS-O5nWhUhokmJm-snMQSAIs4f_oSJQImjxGd_RWiHD_6C2qGlJFTIgN_pTr1TTCYnPlsyRxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTa-5lY_67sn5fn4dp-H6NEPGU05JN1ilPpxGi5M9BApNYclgccLPVa9ZzenPF1i85Ij1dcmKXbnTUndOchqL2naNa0sw8TLh76gaWSXWn7kbOXiOKwQduWukiNHlU3AxmNqsELLb3C8wMp4EACMB7fgx3ayFrQed3uEHkg8Idx0beFfWd-F7Dk4JE0YrlyBqDbKYYhhkGwx7sSVjh7LVVc7DNFfPpGKsGGX8vbPfoFKruPZpQ5hzCB_KYYIUZTB9HUpjFAUEhQQ_9tCHD25SMu-N7LgEtmPKdxK5O2jB--BZkgAExGl0je1UfJDfAlVQa59cWkWgBB9UXvjC4beEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QeEgcpZ6BlA-11fwHQXUiJewRmFvs2BWUNUjjcpx2Z1yvFnBl6bqTqK1hdQLl9pihpFSbCQ_0bYPe5xgX8C2QjIkYUaoOCI0RP0Zxhfn_sxb2nXBZjHPAwMbyIRyXAHYMXVC-7ZqRdRWh-cSyufxECVdMA2pLW4M0LiNqLmJ9RHOXhPi5JqwqYvpuRqbQKAqU7aU62BPJ2bE3D09ay3BT2yTcxxL2f6hG_PxkpfywDaT7psbfkVyqEtnOySZRF6100g3_y2zwXxBJbUctBC2G5uwnOXfDW5xTwhH-FmaHACtHUzgdlw2D10E7KrWvoqiyOmWWjW3hspQK30SfJ3TaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBgpDHgw8rZAMZG3SaIjoAuZzQrki56KvcAIpYn2FNDsbGrnmAPw8uAApAO9JfJnGASS9l3QHV6LVPD_vQo2utSkso2J6LXJgsM8vsCV0xxvHOGj2eVwklB2l9CGk8aiGEkUj0aN4Gr22afZMKjfMzLmKy8mrfCOJpsgkiAmJaGcZcNn8VHw1o_y-XgRvuHOrR83rQp3c58RhLBBvxnlDxtllfiyEJWmTTgzBFFGVCkDTj8idsRBEU-TFX4iEf-rgG9MHpyIf_0c-UHyYH3yRJsc3xKFWDYW3qNC7Ax9_j0yyji_L0OCYMLRt_4bKne9CsUFMozXVR4Y09xYBzQCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=sfN6RlrO6NQcJC65SKxpjgd-q7izDEcm3NUJqxa3KWjvb4_tvMUlNKeJrkVBF1e4PgQukA-a4ph0N5lLur85ix1huqGGoptYxUBt6e_BdWb2C9LHsHbY3DZCx1bC6BrBJV-rJoZGHPnt2Qpp6oj3OKZxJo--L-scE67QzWj_bDlchkEIgYFBp7ORAUQu4J4SEZETv5U6cz3tH0gEvPnLPOeIp4Agz5GegdNwofADZkiekqfIKFqzlokcKKp-D0bFxXWdQ5mXiwf9K1PNtWjKDfLptt0qeP4smtO4lKw0jbFU5UUjRjllNpEkEsiR49z1o3kDdOd_SN2H8ldORxnrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=sfN6RlrO6NQcJC65SKxpjgd-q7izDEcm3NUJqxa3KWjvb4_tvMUlNKeJrkVBF1e4PgQukA-a4ph0N5lLur85ix1huqGGoptYxUBt6e_BdWb2C9LHsHbY3DZCx1bC6BrBJV-rJoZGHPnt2Qpp6oj3OKZxJo--L-scE67QzWj_bDlchkEIgYFBp7ORAUQu4J4SEZETv5U6cz3tH0gEvPnLPOeIp4Agz5GegdNwofADZkiekqfIKFqzlokcKKp-D0bFxXWdQ5mXiwf9K1PNtWjKDfLptt0qeP4smtO4lKw0jbFU5UUjRjllNpEkEsiR49z1o3kDdOd_SN2H8ldORxnrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaqpHoshlsmDRbR-iu0_rEfQ2__2csTQ8EwI9vn5P6_BtbGGt9fK4Fc0o6zTM2ViwvsLLZSbTkGJjBaV8-QL6rLtKO-z324pVqlkE7f5de-fGmA_XvRqdkU5vrlJi3Udnh_1VJaIvOclpf9_VxGQ_PdDy_dqjHyY88RORu3uBJb93XCzX1_lYbcGzIdROZw9eaZVJBcJzgE_MnfOU9B_TP72AjkmPo7I4oK4g_y5z4I_W1DiyyDxMU3DGfwBCFGuhDPE0Ab9j3pdKAzA27f-gCLqAhPDEh7AqjH3aoxJNHKEKhWO3pGFHDeKD1leWASinFutPDDlon2r8oQL5Jxkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X2Nbs284jCGPACkqNpJUiGUapJVGGQUUMkCQvUSdxxGs4xDlgjJpPVR2RGBJulk1rk_fDj6v7-svyhKL7VghG30cuAcBlFLa69MRA0bk3xBiiCfZElRhpZD25C3FYiW_bFbZ1n4pQoO6DepoVrtUJNROCRhOlyZRtmySkBmu3W8wFb_x17CphFnsNvyEbr-dVLBwiojdF4-_n9ibXeqbw3AbHYGZUKV6dIFYWYK5XhwUJbGbequ9li7zoZib8JnFp6D_2jOCYf0xzvxRZRsJxPFXZtBVBVr6vU2Kw-Kgrw-SbkvVMnPlfCVBemKsG_KcZX1vgxLJY3vEwplAWZ_BsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J7WsSsDPT_rzP3UOqMac5LEk2s6ZSfr5T0_5cNxWv9giYjyXxQjmoAjx_CIPQyxIBc78bxj3PP-YdHU3AloTYDEQ62bRqaW6b3oZQW3_rNHgfcrRlUSkhzC-4Ro44Ytkj-A80HdkHwFa579_ZnRSS6mTwgbmUEe6liRpG3gBZlP2mGOF1jm6BxPPgKRcW-65LeXQhhM1J7i7yfF3Aa9jILW6LSwF03MAJN80cGb4ySDdYyScBQSDLKpZyG9-IbV2Mru_y5SWJ3WKDK_OziGAO8Od9fttyXJotu1jYfy2QZ6afYxmj6KrbKteqIoGDVUNZF-RQ89IyGEGdlE_9CUc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L8B2Uzr7__7lZb_w9N__0Z_JsyfIPRWCbpZw2eUzs1YY44Br4_BiENspjfRS1Cp5L8Lz4hZPX34fJKnV_Vd10yKKA7TrrK4EKrccu27St_IMJIDOzGSCbO5UBOEvDP1PqITdwBW1iwFIIZW_lqP7-Ylolasxfv7lyuxzUukHzhieFYeOcPFKZRUv4RXj9UOUslj7B_G_W3q0y7UINmTeBkwJIJCR4Sdk1qEdXxPsli7Al8jmqlC1GTEUpY0-cwJpy7rGscu4xiIz33oRTrcMeJSRfkERG1eRU6Z_QwXFPH5738VmtBdCkYq_NgfWBYYOCTQJA159xPJgBD9VpWkd1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDCAgHqGGl-FilBMlqQP1VUDPwrwI2EhHQTo2katm78k2dkqHVy51vKHbS3-WSMhy_C3jU-Tn6qBy1dEwBN-URLvtC-uCY1aDiFuHTVQAuokClrqVKtzLsorTA4zRWLXByZhKcmOWkKnjJ0gjR3q1zpabDOTdtd7-RcP00RVNzB4hQ_47McmPByvdT2Js1eBrBP2geGDy7BVruVV2W1gMij-nJICKe9Tf9KeLWzdAnch6edM518GdslO3F389s8C8hGZYY3l1DDzeYj5yegXu-3BaB6JYHuhnsOsFVVL3e5eT1YMv7nr43GmdsL5H_q2C1IY-d9e2xGl5XfmnKe9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qe92Wm8hvvZSivhDKlr2yaLGbZ_hg-vG0GxuvlSjf42dtnfAK5O-4RPI7xKenncuUo-MmXSa8DQaFDLefa1Eh0muzALe5PTe_u-OG2bHO_GcKg7goTO3vwTekifyOENM-AkpS1fdmAGgNtuFYbC4cqOCk2CPsMkpbJXxUiVaIw0wbIuYb_oRvClie0e0vtx3yhbCofeA3Gee64U9CxIeCwpbe0YoDf7NbvbQEx3kgp-yISh9_KZs8YY1afza01RwNXU231-JuJWxYRnnFTpwHzkpT7Ll0xAoAwj7lhELFiuG2RJ1ATngglsT11ruyH2tEQJoHZM21aGhsvkVxZcO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h8srEHPuxWqWXRFHA6wpC3K7AeO21omZSvAFsy6Zpb-DIiSwpzjls7s1I0d_bmJn54-21c_k4tODl72Enyg4i3DdYYHB9S5u2I_a7OUHRLJ8XcI9YGkUbkTnUaL2ipi6sng04Ai1nwRcyhDzndl0U-u-gqdai3VmPE0z5SQ5_IIZWQeAdpkaWNnd0FQ7H2DPy0cYpz_Go2AeXPjdc7TSxF4D3lmO9FNmI0CjZh-AQrr2thArlRhYlVKjsNxbEPxINj_TYqgoHBSv5fb6z2t7G-lAhEFBvH2rLCHLsZN0HHi5U16Y0q73DV-OZ8LY9xalo5LgFINfwrfTNSc48wrveg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h8srEHPuxWqWXRFHA6wpC3K7AeO21omZSvAFsy6Zpb-DIiSwpzjls7s1I0d_bmJn54-21c_k4tODl72Enyg4i3DdYYHB9S5u2I_a7OUHRLJ8XcI9YGkUbkTnUaL2ipi6sng04Ai1nwRcyhDzndl0U-u-gqdai3VmPE0z5SQ5_IIZWQeAdpkaWNnd0FQ7H2DPy0cYpz_Go2AeXPjdc7TSxF4D3lmO9FNmI0CjZh-AQrr2thArlRhYlVKjsNxbEPxINj_TYqgoHBSv5fb6z2t7G-lAhEFBvH2rLCHLsZN0HHi5U16Y0q73DV-OZ8LY9xalo5LgFINfwrfTNSc48wrveg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRj7BIds7bd9Q8ze4_FjfpzIrR-8kFISUGwg7IfGjaCVXRo0VKsKP9AxJy1X6Zjhi-P_Mg79QLhInB3ZsUDvG3RSF4y-byKFaDa7mjo0QznvNakpBuxx-nkXWNMuNzbYsSid2W83zoGrywB3vZ4bbamSqwgPA1rO3MqYbccbl_bUyleu8IBKr_Az0mWRxRnOd_IMaBtUtiKOv2Iz2bfUVcSTdb7dWBqdXstzPxQU7aIY132cTQSYeqyiiZa6r0WfTMS8pMS_0cY66AwknznFT_imsPO-oUCTEiBtRuNYTEC9sF0fFMZrN31DXu1SH466aVN_xbfmw-ra4LGeF45VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D3CzZ8wafqvhVtUVJmuYA7Ri071GxHrgxMKI9oDaRY6ipMKly3ItNpdnBYeQUBS18CzGQp14NqaOccvnc--eOuSAUpOlp6MhdZ-J3dwfDdQ41HSiHU5tlm8kOJBkAgc9dmRbsKuSyLjvW6BpBpdUDWa32RXhcx5WFhO5M6MUXwdIKbC1qt9OKI4UGMTPEcmX0hv7VFvFlDu-N4hgj9mQqZFh0KTXL0V_c55KG60r0j1-rs0a4iNITI277Oe4DIE2viUJ7mHbk052pzGG1aCNg2WhwYZBpOJJy3IfCoJB5VWmG2BzFnd9TJQK9N2nd1R9IfAJ-SWZrupaTpC-PdhABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRFVouPtNRyU1cDQPP9fvt0yKfmeMAIUBLEHdX5srQMEgNtJASUgGRDLLAmHhNaqyk5OGB5UPMfplI-BDuco99yzqLpkb6q6JHm85rQRf4w50WHT6LYkSkgQZSitR-BtQZdVHqmC1SDHo0rwBO-evQ8QZHdDZwPQ6AMBr2QOh6mQfpakdoL1IAY2A_ve6GXE9aDTfccuyGgL4VHU4YbdNEVDcZfeQXAfBWeSEvM5oVJnocQ0ZOwjcJ_0rJygE9TLMuzILhY8Sfur11oGckwzQIrflbuDUzlkI8qK9DJf0L9jaeIhKGO30JPr3wrmshzZvDWLMecbT8qf4NpnSsODAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW9YPXVgwABCr-v4KJ2seq7SlDbv5fiuTliS-Vl1cIt4Dq7dgCHySqcKyW8Ys_h8zy5r5YupKJxoQOtSyO_J12_rOP3eE9YYcgO0PDfRm_2uv3L16-23FqORdpZGxsieCrOjcYjzds_02xSHJp-4yWxNyeTEmeM_O2RCe-0W7Rhner6hIIiyyToEumTkBTLMZLH39SQF9yKWl7L8JrFCV7GmSkryWNLlCgMlQjBIzz7u4CL21q18iKGghL1xERZJDDJ_Mb4MgvaTdgyoRQ0O8e8qlT89M9zp1p0Tfk468YWsFY_4aLZa7864Q5NJRwCX0SiIelPhnJdBjpMvpXsnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j61tH_Rv9zJUfkNunzlPvk_Bab_ESagR9t5ZeL9svVn8SFLWBDSDXbCeB6vTS1MAQnev75FDEoj3sxMz6nv7dLyYk7ghIj_E7KYs0S57Jvj7PcMl8xlLj6IFx3EtLIpnr4FJf0WA1WTa1d6WVUqaOfMzr8A6GD3zKLG3yVpJcK9dNE79fTimBB7VltyMszMytZPQRHCpJmcNL2uNHtkWXv6D6jknKbGrQ9FbeIWB0lIDMBgpIdzXB0gVuY0VzoXfdTtdHOK2B7ePQm9MAHuTrpnTKLiaH0s8HfnlKsFN6F1dtV2Xpy20HO10nsSJylQyPnWxHIWb38ZPZu5UOIH-UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTNLev2anbIs3ff12t0ja7_OEmxQraBWQ9p4q89If6_MBq86M4n2-fSBSN_q9hMaS5xsl1dw4g39i_d8kbGG6TSlEnRGU7jsGHXNPFfMt5Bp3XAANKQp5c7ZUEGQoBH2OOR1tafGc4lo27BF3ivkAaYIb0draFgRR5LLaay1lniWScm_F1uLfFePo5qwx0eydpdr42joqgsj7ujDvGSSIJWmwCNAaqU3enTpt6yw7hqjmhGMd2axPbANmpTTQ1e-3W6HOXWf9s07KO8WJmE5pIX1Fzv71kHAkMICdsQgR9_L0jBHOWpCfRft87SDV_S0FKs7m_7rQrcKPBfYQVZdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
