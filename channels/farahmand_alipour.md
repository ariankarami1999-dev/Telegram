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
<img src="https://cdn4.telesco.pe/file/h5YAyUuFU2gx8IEElS0qQZl0qEaMdMFt6_mUa9vv7GGhLHHLqRLcWjT5sfMT2hHxIEWYmGFCmPLOul3M8dPn1rmR4kT0UPNVvx7nuvpP4gQ0vnmLLhIscnLiNQm2gjAHeV1Ys0lnpjQS2SBHsKxW_74pj9PP6AO605ePml__bJOKxJV8E45XtAkRfOB65Y1jTL7sM4B_Pyf0mC4CV4NHc8guXpdVXbLXsiUZdrQQd-JYNNP937I76RoMlJmnAFv-RHX6_VyU6GZSXj0FuJaYQXfj1uMcnMGf467Cm5W9RdPlgqHzAEkvPAYLs-YJuxxRkcj1Sq8cMetnuNh3whq-og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LndJz2xo-eldmWGJk3dOkz9uOpTn1b6vjxJ6LW1mpZqHGcRwPDi_4OevapX855JLg5aCyPdqBcQA2Dt7ZvHwR3CGBV1ek4YkN24pOQgDft0Jn6ubCtAAelrzqQiJnEb6bzNwIWqYz2Uzxaqa_U1vsyhyAInHpGKbFdzaBSu805kmPWyr1St6dYWU-QHcdGT3oIau-ts55w6kO3tMsGkpkXs8bNc_NoozG-vAg2oaALDag1EKPrlTZSEpEnS6tGNKc_OB2sUtPoniTsBH7QjDMKNWAkedZ6Cg6rWTzAOJotOhBqZ2QCOToKUE2C60D4xOqiyr9109ui8HTCK4qLAaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZFIX5t4jrKDnvoXPC0lQb5Rg-J4lpUoiazeBGmajiDCBzG22o7SYthkXQsCWD314UVsve1tLVUGSBJZmnR17Khz5JFznXp3cG8TBejkkLuVCOvtLlREcz1dDeHMdctBbF6MwRVYLTwuDZ8yaKzPhAjoKIgCBx5B0KSGnwVryyazslzyD-zufk2Zx5QOc_x1fmEcoB5A6skMbJxQAQFHsfsUwAwnNE4Z3ieH05eOcmSgEsKxTdEbBdw8hRD3Hkbvi6dRXUTAWUWEculbLSuBfLZj771ntjYnz2jnnQ0SgYTpRTI8BMoJkLdQqcRBzR4mGrGaqqaH6wIti_Ieqpk5MTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZFIX5t4jrKDnvoXPC0lQb5Rg-J4lpUoiazeBGmajiDCBzG22o7SYthkXQsCWD314UVsve1tLVUGSBJZmnR17Khz5JFznXp3cG8TBejkkLuVCOvtLlREcz1dDeHMdctBbF6MwRVYLTwuDZ8yaKzPhAjoKIgCBx5B0KSGnwVryyazslzyD-zufk2Zx5QOc_x1fmEcoB5A6skMbJxQAQFHsfsUwAwnNE4Z3ieH05eOcmSgEsKxTdEbBdw8hRD3Hkbvi6dRXUTAWUWEculbLSuBfLZj771ntjYnz2jnnQ0SgYTpRTI8BMoJkLdQqcRBzR4mGrGaqqaH6wIti_Ieqpk5MTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=EawzLfmnnhkO1NvKBNpilZLzY0MpGeEXK6ng3Q9tw07liC6BCXRdwzGJMY0G_R0RpiUpJ89-6lVX2cizkHHpAMyzzhKaN6EE8UvKKEtlKtKzpoNIYUrc0JEvHexdWxaPFfOqTbP1Pr8vZcd_n9eVB9gro7QbDO_1p7Z3jAhkagJI1fa4OFivaFWQ1qR0fxd2vxmFvmQGxaFRASzbx4iH6rfGqqgybr45DJUGiFhbO0iR41NfKCkbaYiftmOddPJJmIQVVR7fDnYIBgLVA1EHi8mUKRWCcwOv0fuylgxQlKw9Laq0aKCCY1RzSK9Nhl-OHy1n_HsZlivoxM348Vu9LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=EawzLfmnnhkO1NvKBNpilZLzY0MpGeEXK6ng3Q9tw07liC6BCXRdwzGJMY0G_R0RpiUpJ89-6lVX2cizkHHpAMyzzhKaN6EE8UvKKEtlKtKzpoNIYUrc0JEvHexdWxaPFfOqTbP1Pr8vZcd_n9eVB9gro7QbDO_1p7Z3jAhkagJI1fa4OFivaFWQ1qR0fxd2vxmFvmQGxaFRASzbx4iH6rfGqqgybr45DJUGiFhbO0iR41NfKCkbaYiftmOddPJJmIQVVR7fDnYIBgLVA1EHi8mUKRWCcwOv0fuylgxQlKw9Laq0aKCCY1RzSK9Nhl-OHy1n_HsZlivoxM348Vu9LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_UxmDd4i6rWFga5Y3jH6gL6zSB79aIQUS_4TF4c35uGCHXY4z2SFb7s550j13fj3tfEmEJkOnBsAySN3m8q3ocR65ukT4uuu0AHrE_3aVKTaDZTB309mzMISI_6B04inobD9oKBvb8fq7aD1FG-HmLgAxyIXwLEPo5M2ZKRHAfG1DvtipRxA9RYyaMkalrBATb60BzUfKy7DH2us7-YGRmHOv1sQjzMnt9SqNTeVlEQuspmNISj_nwl78v0Y-gkQ3q2kaSMcC5fNT4Uv5x1JSdY63hUs0_KObZXNsMAP2EXesV70gnWztosoLDCK3XgVH_LJ3N5Re3ZAMZQF-qDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsNPpN_H-kay-fxUee76M231nFEJfKBJ9WK8Vh8p85shEvHdsFpsG6_8YqxUVT-4RyzzIFVDzTUciqsE2EM7x3YZa0-lSTFS18WHzaO028pCWOxJtB4X_oIrCMHATGz9CTPU4trC5c4Io7MS6q7_CMlVFFETi7Ep9uFc6R7jL_wB-shXvU5DLdHaBsXCDEb0qBycVavFNJBFw36NV59IdahMXmlsy5mDz4ILtpOHB1ZA7Q_e8pEEvsaq7V1BAxtk68hghIBtOvczBv4PCQqTNTPzYl_7aYeTalJv3XB3ckdaGohs604aStIzLQoq-KsvLLnIhGnJZy6Ypi39X94Y6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUvStLJEoQ9PSh8Ojb55vhlSYG92YvddikEJ5b27G3lAigDnfKoxoSsGFbapjydTGfC5169RDAdkNI3k2dYKGfovbaHss55j5eZMVtSKDB39LBvgduAPL5UyI3PTX7sbfbP_ucGW0ZlI-2XZ3JlT2jHU6lxLtku4j_Di6_-dZgMQR-LciKFhyDVv5iave32bORFEGPZ5NjVu4HflupPVEk29HK3LjkxI2qry5kdBuWZf1eWHGg-MF__-Z5irTMxYgYAkmILpusmbLd2RileZ7fssKtj_Mu-Rq6XE9NhwFVbIuLHf-vM8cBZ3PAWjdLbvPfXx8f1MMMOR61FDgv8-dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DxRLB2dYp4JSXTmzMcM3hopuYncS0FzcTVqyq2PpiCQ9QgwH28al3tVTWOm4uEQMM5quZ11nbkvwufGaTVijNde5HNHqedP4-tIIV3SVjWC6MabxbC2gH9f0WI-ChFRuA7u7DzJeeQjej45uj11xjOU13SIRN1ml98d-68jO474ce3ckQBHB679D26MKa1K0Vh-9K7oq_x4rbnvFVpMHTGPfz8IjJe2f06q1SKom3j39L-7Pf3dxPl5fPsQ9UX7qcKIaJus8K29iSSTGcWq3QVzjtbwtIlfX0duMTlB_dHPc47g5fBjhUrOM87wcfp_iDpcJu1b-a0NTFbv5LSLB6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DxRLB2dYp4JSXTmzMcM3hopuYncS0FzcTVqyq2PpiCQ9QgwH28al3tVTWOm4uEQMM5quZ11nbkvwufGaTVijNde5HNHqedP4-tIIV3SVjWC6MabxbC2gH9f0WI-ChFRuA7u7DzJeeQjej45uj11xjOU13SIRN1ml98d-68jO474ce3ckQBHB679D26MKa1K0Vh-9K7oq_x4rbnvFVpMHTGPfz8IjJe2f06q1SKom3j39L-7Pf3dxPl5fPsQ9UX7qcKIaJus8K29iSSTGcWq3QVzjtbwtIlfX0duMTlB_dHPc47g5fBjhUrOM87wcfp_iDpcJu1b-a0NTFbv5LSLB6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWA4NAvTKcBcV5j8GbZTEBUdX5GKV2REgHtyWrQlTfDJWUU9QYGr-Z2Zc8ERUoR6ftLV7oT-KakACvjdbxePXYtX0GXoUD3buf6lUUjO3HPWilvhYfJfVf0Lp79GB14zhB3TUQCP0tA8L1wbyaJIe7m_hhe5vVR27YBmzM_AF4NBs4r3uZp1ikO0WgvESR5NpWgfKuh38URCL2nIXUzmsyFdQZPcWWnm2XvzXje1XyOdneiCh7WHxA0hfbRUxhbdTLlD95FJTyM6w8qKTB3UMjmC4YsajNDrW6Jls4uAIkwFi-yoZrttSdxYA97ODW-OzN2uAI5yJfSpgvtdwEQrtaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWA4NAvTKcBcV5j8GbZTEBUdX5GKV2REgHtyWrQlTfDJWUU9QYGr-Z2Zc8ERUoR6ftLV7oT-KakACvjdbxePXYtX0GXoUD3buf6lUUjO3HPWilvhYfJfVf0Lp79GB14zhB3TUQCP0tA8L1wbyaJIe7m_hhe5vVR27YBmzM_AF4NBs4r3uZp1ikO0WgvESR5NpWgfKuh38URCL2nIXUzmsyFdQZPcWWnm2XvzXje1XyOdneiCh7WHxA0hfbRUxhbdTLlD95FJTyM6w8qKTB3UMjmC4YsajNDrW6Jls4uAIkwFi-yoZrttSdxYA97ODW-OzN2uAI5yJfSpgvtdwEQrtaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=FJwA4oD_KX7FjKMFM0qsx1yzdQrL_-3J6Bw9tfs1w2c71AiVUtU62wShx84OvqVg1cBuToXCxWwTVKfFY47PsOQiYm-3se8TVNzfnOU9aAaPl8lXq86ks0zA0scA9L-krJdBGPQjSjjagmwlb6QBdt7NZvReeyuFTIb6Rau32Db9Qeymx7iDknFp-Nijd2gAJtDtTWp-gpwFHxey6iiZyzrdMkevEXTpUDPgYLLPudzrnoXsN6hNVgJqLnE0zjBBwNwU11V_GMyjYb4HY2WfsDKwjsmiN9_WQJ2Xvv5MauE2FI6md5QMV1Tjm_yyHTHLTSj2HswCeP5AQCFd3mOzDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=FJwA4oD_KX7FjKMFM0qsx1yzdQrL_-3J6Bw9tfs1w2c71AiVUtU62wShx84OvqVg1cBuToXCxWwTVKfFY47PsOQiYm-3se8TVNzfnOU9aAaPl8lXq86ks0zA0scA9L-krJdBGPQjSjjagmwlb6QBdt7NZvReeyuFTIb6Rau32Db9Qeymx7iDknFp-Nijd2gAJtDtTWp-gpwFHxey6iiZyzrdMkevEXTpUDPgYLLPudzrnoXsN6hNVgJqLnE0zjBBwNwU11V_GMyjYb4HY2WfsDKwjsmiN9_WQJ2Xvv5MauE2FI6md5QMV1Tjm_yyHTHLTSj2HswCeP5AQCFd3mOzDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGDjSsG3oKOXvbuW6E3jisVhUr9zE6-_2aQKaiIlWlK24zfHL8XpAp_RhaN0VQ8n18GNMQ7XkMc3jtMU7rDOyJJT6Y8LIMjVgcKDPFCy3vSnAumLV_9w6_jRqMr5mh7EIT7v2dpQGxv9W19QN-gUruGsrjIY-qJ-uWyDT0RaCiy35Eopb702yrwn1TN2gBD-F7nJe24XXfpqpBJMxCinacoUwKts6yssqdOE4XUlSEJw5KF_8jsnSbmOP33qVIuiuRV2atjPw0HQHHtVhN0A6SKBF1VUhqPZQHlRRf5-_IqjRI73OgfjehPHkluHeIPQPeJJBBS7kV0DmCWmM-_PKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiUfgXQ-MyK93OmTXjcPpG4bGZtA7B2eKV0GoCcjYJTmQHmGEvRHGHpal2q9nd183Z7CyEICM4H4192lOrPt3rmXYSFEEzRtQKOVbrIqWCRXq6__Q_iv3sooDBuhyH8wdX-G2KG3d8IZtT1nz-gFsUDTkgKrIp_PziwI31-hk_pHb1yLMkU_P9VLUlzMz38slQ2RjiIzfv0JsSZ4B-ARslproM-B-TCDIbefrIOKYeHgfbon6atE2VJUvSWh8KvF3UEM9xhvxuUAZDKl6ozPwTO1-hmzAUnPP5L27KWCT9kp53UbuMseA22iXwVKfneAIDuYozpvDz2iiNL5g5u_jrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiUfgXQ-MyK93OmTXjcPpG4bGZtA7B2eKV0GoCcjYJTmQHmGEvRHGHpal2q9nd183Z7CyEICM4H4192lOrPt3rmXYSFEEzRtQKOVbrIqWCRXq6__Q_iv3sooDBuhyH8wdX-G2KG3d8IZtT1nz-gFsUDTkgKrIp_PziwI31-hk_pHb1yLMkU_P9VLUlzMz38slQ2RjiIzfv0JsSZ4B-ARslproM-B-TCDIbefrIOKYeHgfbon6atE2VJUvSWh8KvF3UEM9xhvxuUAZDKl6ozPwTO1-hmzAUnPP5L27KWCT9kp53UbuMseA22iXwVKfneAIDuYozpvDz2iiNL5g5u_jrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmdvFSNxWxAHqtghhEF_6XKDmzAIwXGs-wusvyiiJeTTNjTVR3Zs1w1NXvzh2HZvipRabgKXLJdj1gruKjUmEbbMHdzTdS2bjYKV9FKZip-1Ad1s8LyaqlRYy5_iklZdrGh3NDmvsv5vys5cr9xZ7wBb10O6cEqLteYRLaEstudm5E6mR7xkoW8JwYb9JnjG0rJjpL8JnXzWPveSKaBjZgKIbBn_M6fsHKsiJ2Q9qK85u7L37VwqVThSccYYaQVb9oEjHE5LXi_NlhsCARLkQHfvmoImStUUW7P4KLb-rfrOqzVCXgeBpgIC7sgF3QG7wbDElyEA_YcC1CIVUk2qRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=BqPi2oWl97ANa7N41qfZSMSljPzi7RiG6qq9jEoCByn8yPxtnRIInI_hKynWZTDqw42ZEmvn9Qmil8hqeTLm71mVNa8MrrddME9a-MxuDPOyqO16ev0QzSKfXGPOV9sEKkTHdIReGcdzsvOLrM7lFJFSaeMKXR0H_ECbqBPajJU8uqDIagjN7I7NWGqnjRQYPQBIJgukLGzTBtrG3NJj_jB09mNG2ThlSHQ5QbgkgFBxpYDWZRukoME6LYnCYXg1juZ2hZH-osfcGNOlD9DB5HzjlmeaIlaoPwDHb8IiKrR9J4sjN2JR2jpsWcbKYX9qVgR2O7PLaLs4XFjvUlxFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=BqPi2oWl97ANa7N41qfZSMSljPzi7RiG6qq9jEoCByn8yPxtnRIInI_hKynWZTDqw42ZEmvn9Qmil8hqeTLm71mVNa8MrrddME9a-MxuDPOyqO16ev0QzSKfXGPOV9sEKkTHdIReGcdzsvOLrM7lFJFSaeMKXR0H_ECbqBPajJU8uqDIagjN7I7NWGqnjRQYPQBIJgukLGzTBtrG3NJj_jB09mNG2ThlSHQ5QbgkgFBxpYDWZRukoME6LYnCYXg1juZ2hZH-osfcGNOlD9DB5HzjlmeaIlaoPwDHb8IiKrR9J4sjN2JR2jpsWcbKYX9qVgR2O7PLaLs4XFjvUlxFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=pfGu55XZn7rhEQrAmMW6AdVJwGdgHgD1UiX-pLhBve1ZQiCrPPDKB2ZmstyLBVfwKHieQW5L-Po0a4LWLIeS5EYlJA-ONMVyeLN7DOeUaUX5gYPxBc7VlYBbLt354tvsnR30MuQLFZShj3oEgB8IhzgwXVIHapm9P254-tG4Ilz-oor9_4Y1wCp59nwBhTEnRHGUNOy712o3Nv62nlp89SsfztInbD2XmJz-7Gyf37Yot_Xm_OP0-_Eh3Yg46ZBZK0juhYHpE-_joXmZlZ4KZ5ys7reCv7EffdIxLAEZYZyZwmQ-WTMPU2hSbr8llwxDHtobxiSB4Od9Bbhq_0UL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=pfGu55XZn7rhEQrAmMW6AdVJwGdgHgD1UiX-pLhBve1ZQiCrPPDKB2ZmstyLBVfwKHieQW5L-Po0a4LWLIeS5EYlJA-ONMVyeLN7DOeUaUX5gYPxBc7VlYBbLt354tvsnR30MuQLFZShj3oEgB8IhzgwXVIHapm9P254-tG4Ilz-oor9_4Y1wCp59nwBhTEnRHGUNOy712o3Nv62nlp89SsfztInbD2XmJz-7Gyf37Yot_Xm_OP0-_Eh3Yg46ZBZK0juhYHpE-_joXmZlZ4KZ5ys7reCv7EffdIxLAEZYZyZwmQ-WTMPU2hSbr8llwxDHtobxiSB4Od9Bbhq_0UL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Hcfjpexvy5keeCCrcm9rfYvDG537btAd2Z9ZvrBIlIT0wYz-cn4pYRWUqBKG_41scy4h78Q-j_VHFXPtozUq9522z8BpV57QCRolUTZIxhzzZCBtj7u99ArQDdBdQcUbcDpz5AP0oofEtFvlx-9E0dYuOUzGcqmDvt3oNUBYNAoo5vjM_cW7ANOIDoATvCQDuGHCM7tT2ORI_VfYzljkQ49mbxwXvqh1Pb8BxfbaMu6zeME9V97IUPoovsAJfmIs-vLsXbXn4nPUZT1Tr8O6hPyBFg9bCV_kclmkUjnL2kduLkPswzHJGm4vmtF4I63hsv9bSheRx-e16dxRvZ-QjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Hcfjpexvy5keeCCrcm9rfYvDG537btAd2Z9ZvrBIlIT0wYz-cn4pYRWUqBKG_41scy4h78Q-j_VHFXPtozUq9522z8BpV57QCRolUTZIxhzzZCBtj7u99ArQDdBdQcUbcDpz5AP0oofEtFvlx-9E0dYuOUzGcqmDvt3oNUBYNAoo5vjM_cW7ANOIDoATvCQDuGHCM7tT2ORI_VfYzljkQ49mbxwXvqh1Pb8BxfbaMu6zeME9V97IUPoovsAJfmIs-vLsXbXn4nPUZT1Tr8O6hPyBFg9bCV_kclmkUjnL2kduLkPswzHJGm4vmtF4I63hsv9bSheRx-e16dxRvZ-QjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adWDY71l6wE-QanWmufQB5bc00yx6nJJivqV5fUseB_9Qmls_tPOE22QLX01OEU2RRgho-Vq3OSUe5dxolR19gRy2mGF-_6TWlvxiUNzMzygpuWHAR_sR2gp0izsyqrHvRNrqo87LWdVfnYMS0HkOOuiJDg4M6p8A2cGhQ6JRImwsckCLDSh8o4lqp-R1V0rdjAkOhyZv5AonTaGuKKXQEiHNf97KBrYftIZVZA1xdqLtobCwxXmtVZNGa16nxBkQAiUOR3lhg3pNyqPuYkux-um6hzGD3zVHiGaC5X5wzg5M15EBWmISs3nwWi4hyY9KvswXsUCGRf9vXpMYEbbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2DVZz0iLOsub6xTyV66gjtWuNblWuKjpGLQZ0rCLafWHerPs0aEoRlNJpvXOaYaxIv1zW3VNk7VljnkJtErAWuwy0T0uBa9MN8iqDBmZ3rpCpYurmUr4EZQGRCa0jCXzMsvcBTow0SofSGPYOYvC6uygwIJteM1fyzRBr06EJ-OyE0S6DKdEkrUBTlxARu5evv7qQWZgGTQG4E6cmWZ79jGDA_44tQXJkmOw0OPH6OQJahcZ-WzMwgH0eEuBGKc-dWBsT5cuEcx8fsyfWP1oruEFbspN3katblAaUZL9o9caBNLL6BiCo-pyugHWxI7dGzQPGtGJ6jJAFExIxnKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Ut5_RxSET3gve-sr0R7G6ILiyz3CGcxiPKrENxSvRiBOTcACDJs5ViEDxI5fUnSE82ui0dog1sg34gbaeFcg_CahaOSn8cG_dt6x4FH9EBMF3DpUnZxreVxf6Qw1dEYa0kZ4k4S7-eFOCWKpGrUwHkLbC1rkNkRKDN7Jw90fdLp3Sf2LnWGp9bi26hYDOAoE4Ys9eEQy6tRj7kdLrSU8oCeDikV3LuZ67dy5M4McClf2byjPW81YlqFzwTgeVK19dK-NnXLUkUp_OLPX99F84h8Dsk_SQSjWFA4fDgp8XlB-s6L3u_uhPUcMQmeDTfL2i3d0zWhvNS2Jc77Bq98T9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Ut5_RxSET3gve-sr0R7G6ILiyz3CGcxiPKrENxSvRiBOTcACDJs5ViEDxI5fUnSE82ui0dog1sg34gbaeFcg_CahaOSn8cG_dt6x4FH9EBMF3DpUnZxreVxf6Qw1dEYa0kZ4k4S7-eFOCWKpGrUwHkLbC1rkNkRKDN7Jw90fdLp3Sf2LnWGp9bi26hYDOAoE4Ys9eEQy6tRj7kdLrSU8oCeDikV3LuZ67dy5M4McClf2byjPW81YlqFzwTgeVK19dK-NnXLUkUp_OLPX99F84h8Dsk_SQSjWFA4fDgp8XlB-s6L3u_uhPUcMQmeDTfL2i3d0zWhvNS2Jc77Bq98T9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXEK4IE9-94qhIrm1sZA76PNfB7TuuGHF1yCbIyUx5wO_dGuooWQwRlHFQX1yNizjEv1x01D09wmmrGKqTOUxDGnYfLFk3J8ve2vR2lmUSQUdQM6lGftmTAfhq3sE_xo6MJHDSxPpG5ug2yCpHp2XgzEhKcYShlQwmALj2HEg8olFb14mvhAj5v3_f-L6YrMXLU1z9kZ8GxIeTEb_jX4n0O5f1FpCOKXIPMOvWjBRmkvo3Xi2O79N2qi7_1NSoPQ9AM3cKGAu58aCAzkPiumEBI_4lGuSShSCXGI2aH8fZw1OFVcZq2-ZtkHOx3ZctKb-gI1UyYWML8w3pqFcoVf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGJ1QoqL2QZQPuyDMq_G8lbuJ2p1XFITt8PPw8O8hLTY_xpbftQSDY2HCpLrk7wDBn7FzsINdwvoMWlvxx0SKsoudYS2RWqTD0gPvkrgOU2eNG2I-6zjYNV_SCKjNiJM9AK_-MWxAG809Qc3fYRRumi_ebcySCvElBngEvpZIhBR7wHedAxRRnQd1q1tpiFfKaXtM7qLa4ZfVuPN0D70PkBBu7drGE1QdL0-psb886zU6N59NYDUVeqxFUQ3P2a1ycZySnbNIlPIWYMjlOrAyUJwPfaX4nSduuZb43uPLNmtlWf5Mom3WueJLxlGyxfTMJaznZGh9QUNj6ONIDFPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=dVZhYxgrqlVyFYXZJLcUjKNGqqU2j1XAfnnLsi6hYBjqPzKK4R8Ui6Ay4kV6VS2vOXRYGpLa6EdMiEseRv--MXGtqAi9ctGvAgbaQARJn9pr_VAweHbK4e3RsvBb8Czrd38RY9lsv6ppW3Ml9bpR8uIVzGLf_n9yB3SYp0ZPe-aIEqUbuNdxa3Fn757DYV9o3aMlW_nmvkSG0Nrx4k7PV_-X2LrJKKPjvTExHf2o78dkUtX8ZA2O92L2ULpVteLcq6yfjY_iBcr4qijaxw_gV9ALL6WESoz_10MXeZmt34gdUkBmvfhOExD1f1wbylkDDrpMWUbGd61cXm-FvvxyQxFQVl9CqyW4nX5makh9U-mGB6Gl1oXWucVuEMnURGOKeaqhLvTBXCRpw56sIiMx4QIo6BuzrOAKu3T6JokcaQDSdgWCem38LtPcdD1-iZ_n7MzN4mTq6MyYNMXItHe7QG4I3qGAwFR3-kpTY8rAezjHT2XEPAxOM6WLuN_z2ASYzhnT5jYTTQxIk2EmAv2pmPL58Z-fHNgT5R2UmTsz4f-PYXaNgxKeD2KXZ_F0tzJo5kivCujIuoe862TxlUYWVThsOZhuLNNHpH_P0zEqRgc0KxaLAfCNFvzZtqlM-MWTIWdEi4RVmbOsT4I6XxbbU3j74qNTTn5pE2rGT1pzHuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=dVZhYxgrqlVyFYXZJLcUjKNGqqU2j1XAfnnLsi6hYBjqPzKK4R8Ui6Ay4kV6VS2vOXRYGpLa6EdMiEseRv--MXGtqAi9ctGvAgbaQARJn9pr_VAweHbK4e3RsvBb8Czrd38RY9lsv6ppW3Ml9bpR8uIVzGLf_n9yB3SYp0ZPe-aIEqUbuNdxa3Fn757DYV9o3aMlW_nmvkSG0Nrx4k7PV_-X2LrJKKPjvTExHf2o78dkUtX8ZA2O92L2ULpVteLcq6yfjY_iBcr4qijaxw_gV9ALL6WESoz_10MXeZmt34gdUkBmvfhOExD1f1wbylkDDrpMWUbGd61cXm-FvvxyQxFQVl9CqyW4nX5makh9U-mGB6Gl1oXWucVuEMnURGOKeaqhLvTBXCRpw56sIiMx4QIo6BuzrOAKu3T6JokcaQDSdgWCem38LtPcdD1-iZ_n7MzN4mTq6MyYNMXItHe7QG4I3qGAwFR3-kpTY8rAezjHT2XEPAxOM6WLuN_z2ASYzhnT5jYTTQxIk2EmAv2pmPL58Z-fHNgT5R2UmTsz4f-PYXaNgxKeD2KXZ_F0tzJo5kivCujIuoe862TxlUYWVThsOZhuLNNHpH_P0zEqRgc0KxaLAfCNFvzZtqlM-MWTIWdEi4RVmbOsT4I6XxbbU3j74qNTTn5pE2rGT1pzHuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zbQVZrabldemP4aH5ar0VsxxmN1f7fi00iZZ9EYXRX257DJBHtXudL_epSpOWqn8rdetm50PMRIA9V2F3EyJHJM3e4_3NfsIXzVB7Gek6oc_LSa0hX059maOe2JUdkWzvPuTVnd6w2bK77MX3_wI6dmga9sY8fqIdgXgD1VaxTMX2t3YPZUEBCjfQKNaj4-tVjhnhydYGDGFF1laSDrT2uJuDyI_udtAKW_DKHxc0aqFGzUMNXIilz-cEx4UFP8sZprBKNDTqXdahhhc7VtPOjfiOLS4Am1cgkJoUIfgNUzweSTO9qLU_UhTPkg3Jg-6SPOqQTPBohy4Z2n7PEthIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zbQVZrabldemP4aH5ar0VsxxmN1f7fi00iZZ9EYXRX257DJBHtXudL_epSpOWqn8rdetm50PMRIA9V2F3EyJHJM3e4_3NfsIXzVB7Gek6oc_LSa0hX059maOe2JUdkWzvPuTVnd6w2bK77MX3_wI6dmga9sY8fqIdgXgD1VaxTMX2t3YPZUEBCjfQKNaj4-tVjhnhydYGDGFF1laSDrT2uJuDyI_udtAKW_DKHxc0aqFGzUMNXIilz-cEx4UFP8sZprBKNDTqXdahhhc7VtPOjfiOLS4Am1cgkJoUIfgNUzweSTO9qLU_UhTPkg3Jg-6SPOqQTPBohy4Z2n7PEthIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=UQFx7TGV2WSXb2K4Fp-a-_ZCXqIPDFK-kwAwfo9f9YtxGf0FGyj15KwvZuhgR9mQMPHjoZzskmvevWdm8Er-_KEsKdrf0JuP2YR0gUgMhklLIoxHfg500Sme3_8Sz3OiL1p6BnWR8d4IMbu_zvEf66L6Z01KdONbXnNDtRqU1mOWWg0fbhlpKgdCBfKOP0LPy4g4n3FGy6GGSkQmUkX5cvZzoHUSdWOYWRzkU7t5s099H1vlxQfHAbba_YJuJhNVhPFeja-IyaJ8hIOIqdGgL_WkjFDTQNWVk4ypG02qqLRQ_6o6fv-Ql9LBpRJeSsdP1fHdPnyY5bI7wSY-0mmIGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=UQFx7TGV2WSXb2K4Fp-a-_ZCXqIPDFK-kwAwfo9f9YtxGf0FGyj15KwvZuhgR9mQMPHjoZzskmvevWdm8Er-_KEsKdrf0JuP2YR0gUgMhklLIoxHfg500Sme3_8Sz3OiL1p6BnWR8d4IMbu_zvEf66L6Z01KdONbXnNDtRqU1mOWWg0fbhlpKgdCBfKOP0LPy4g4n3FGy6GGSkQmUkX5cvZzoHUSdWOYWRzkU7t5s099H1vlxQfHAbba_YJuJhNVhPFeja-IyaJ8hIOIqdGgL_WkjFDTQNWVk4ypG02qqLRQ_6o6fv-Ql9LBpRJeSsdP1fHdPnyY5bI7wSY-0mmIGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=tvT6AwGbDVqzHWvDDoXxczzJbg1Ia8DtE-EUF62WP8Kavm57Qf7tG1y94SMe_VIJck8BbZJq3JOVTtwkfeieVLdkoMShcTeRlUlMOHR4ZQ_6s36jmEyL2buBZM2muXFUnz_roKPandSZ1Rkr-aK3cFEFeqaBvoeFLGLZjM6D1IW4nRdfaypCIhDw0L_inHFJntwejNZFV5gEos1zMcRNlbBS0ZxnWa0c2JDKvhN1MWkR5SXaSd3d01qTAJnvCiwmBIww3pKqCcB5DtpfpSquug53izAuh7W6UDPxX917IBYYZCemCHLW5iDY5Zt-sKMWJMDuI3vrb6kq4RecMhlD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=tvT6AwGbDVqzHWvDDoXxczzJbg1Ia8DtE-EUF62WP8Kavm57Qf7tG1y94SMe_VIJck8BbZJq3JOVTtwkfeieVLdkoMShcTeRlUlMOHR4ZQ_6s36jmEyL2buBZM2muXFUnz_roKPandSZ1Rkr-aK3cFEFeqaBvoeFLGLZjM6D1IW4nRdfaypCIhDw0L_inHFJntwejNZFV5gEos1zMcRNlbBS0ZxnWa0c2JDKvhN1MWkR5SXaSd3d01qTAJnvCiwmBIww3pKqCcB5DtpfpSquug53izAuh7W6UDPxX917IBYYZCemCHLW5iDY5Zt-sKMWJMDuI3vrb6kq4RecMhlD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8bElPaZueR9-8Y2cp8vkCzdqjyXsGGrJGdzVnbPQrvhevqPXWrwG_gHb7sPe75FRjyOKrUC9MtZkPT3PJmp0dXGkPuME4Wkbwd691BUeRlF6Q1GQpqrzwI87HpJKbiOjt8n41-64T893lJ5oSBe0cOLb359j_08R-0EVzMFIBXHLMa-4KBu6a_PCLcYHrMc85Z-riHIGx0mFtvJERt5SHtcv8smDxCx64Ckjwc_o5-hDxvQ4nrYSwY5Mh9y86pMdjWCMagqIiCDYlJvquFZeFtvsPnfdXlnFsq2M8O-v-tGXVU6oUo8DXA0dUfLN3ofBZE7uR5GjyK6oR0fz84xMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlzDmvUkUNocZcToIxp8AAvb-OzimtWLjQ6ZCXQ-OiaWRsk-cLECfSYlWtkSXRHZsXI3G5UoZbqVXBCGyAzfnVeUwGJSY4n06B_J1Uo0lX7QjxZNqHkLVBIfUk5P0hlHg-OtJlbCYwoYVZ2f2hvyfaxcyJf5LFg0uyiUPbLtGzwEUgdrvcCS4NW6SXHEfaNnGHKj-fzkBPM4VOGq86u7NL4WF4Tja0wq3gHGQLg2M9pLOGOylFHbkynMkF2UV_6Z1k7hrrxEbsw1mkryoA7Jf8oxphv4D9y5IQn8mZhtTKvubWjgXpWqmPww8nHhYBS5g1lo0zcjFpHgaDP2rhC21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMQ7REdwOkWO2RfR4sXUdWMxyA3fW6uE0CCbBXJizNeApdDsbBiWDso5YNSOhpAsh2SMdmUdgwcG9Z9JocbVwbL-bBbM7eyAy2LAY5Moi2fWTXFLdyrMovFuJGWBG2SUWBGWuoJxrPQnmrkS_KPRR6R6iOoqTb2qheaO9xLmG4iblQc1ev4B8iTCTwSDnWF8DckojybEOogwBb7RkrTnpAi3IAXutwtvyiPYsVNnAbWttYb6POiXtiX7EeAooJpLme535e7NW4GiacXEb0TK3P6iOWQwFnoRMnM9FKaPo5k8yg0YGkcm3vge7nj-4gZYDgkoT5z8jYoyE2IeQJ2JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6ihpos011gAYKFz0oIZjFnNBiRYmCKPRN0jn0Ouo1nGmFsw-Qvup4GsWKzf4SyVw5CzyPC9-z6CAatyFv6PzYaHKMTbDGXWgKTuJuKL6VK6HzbOWtJbD17_13DiGQ8POAsLrA7al3RmOY_ZR_TaSGqBayBuTLfnHl992r58R4L5Yl_y-HUEkHmqh8_nVLnI6Pl9IWG_kx6mcnb7ESObxgzAaXpEf23cScdBvalAxhPWTf8a0BsFN4YTKc-RCe9zUsJ7CEQ6TBVvi67PGiX6-OtmyLEWjtD3giSypMclf4qoRI4biCSTSiagKTXJeqk5K8kSpWptaVmpjhLREL3s8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlwqZ7eCRjBy-OLxCDxvKYnSo6Uu4YQmR2q6cfIMliq7Ec6AVFiwqmRP7IIqMxvPaSvGxC05XWzaxAGcyY8YdYC9RyTd27raKm_XT1h3CLGOulKV8NdZIrmZi_-32xTsRNmVTiaiCkd-i49Ksl26O2owJn1gcOCRe8FK4XsDdv59PpKRX5O0boTrz3c-NoeECBnNi3JJ6pA1FKu5YHLsSq4x9pCxI9ctPJypFFZdcWQTd3kzoyQN_FxKAVr8IhfqqVktoD8So05BUONdk22mvkugsY16hvRU8pzOS3KtLjrvEYXnN4Bm0q1FeoFnibsFYf1clcEFWepKDW1GL0QsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=qyvmUx0y6C2kkQFrka-Tltqi1TWtf7XPdrEyOw2z_O7_c_isjbaLx-yc11l6Ohh9Gmt9q6qdtUoec_uwo3G1WcvnHcDvE2SeuZTLnkAFE0KrC2sZYDkvvg_22UOSCLTpsCcVW1Mg5ENiaylSieNnqSJ6SETs2J529caCLfGaMVnXRa-_ZoaWBolr34_bc9_oj6zwdFFMO3AIdWYcMIoeBcPOPZA0WGsA3Hd27DGJ3Z7kbz_2lPDlHF9bC6bL5oYiVNwHrDD0qUro74qh8V9yHMfhDteOiUqIvHNkazqyKbYGuBX2XigCty2RoEndfE_cvHqHGyp_OXvkjJCwGwR2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=qyvmUx0y6C2kkQFrka-Tltqi1TWtf7XPdrEyOw2z_O7_c_isjbaLx-yc11l6Ohh9Gmt9q6qdtUoec_uwo3G1WcvnHcDvE2SeuZTLnkAFE0KrC2sZYDkvvg_22UOSCLTpsCcVW1Mg5ENiaylSieNnqSJ6SETs2J529caCLfGaMVnXRa-_ZoaWBolr34_bc9_oj6zwdFFMO3AIdWYcMIoeBcPOPZA0WGsA3Hd27DGJ3Z7kbz_2lPDlHF9bC6bL5oYiVNwHrDD0qUro74qh8V9yHMfhDteOiUqIvHNkazqyKbYGuBX2XigCty2RoEndfE_cvHqHGyp_OXvkjJCwGwR2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=bRvPynx_rZKjGPYDSAbQkmM6-DPIw8bKP47NyNoRzJOW6AuB-h8uiXIr-mZMqJSLOGkMnE0CheKCcCqGq3Sc1EpJpqeEcBGtO7bRLcPhy2sUCoyLrA8be7dUZFDR781fsCbjOVrhHMdhGKXpFTV07kQ-M7ON67wwUcgfIBAAua1AqfIZpf-znT2T1dKtKvXfG2KvL-rde4hbtRcN-gDtqCyOLIRw-k66gbiNZbYOQdG-qqnFIOOj5uf9IwmlbUOZ1c8RzvfaSRCR-vhCdQ_2IxFLG1QEXqdci3b0LkHWrocSe8AhIQwXh3JF_F--WZLCpa40XLsGE2fBuUzxNm4tYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=bRvPynx_rZKjGPYDSAbQkmM6-DPIw8bKP47NyNoRzJOW6AuB-h8uiXIr-mZMqJSLOGkMnE0CheKCcCqGq3Sc1EpJpqeEcBGtO7bRLcPhy2sUCoyLrA8be7dUZFDR781fsCbjOVrhHMdhGKXpFTV07kQ-M7ON67wwUcgfIBAAua1AqfIZpf-znT2T1dKtKvXfG2KvL-rde4hbtRcN-gDtqCyOLIRw-k66gbiNZbYOQdG-qqnFIOOj5uf9IwmlbUOZ1c8RzvfaSRCR-vhCdQ_2IxFLG1QEXqdci3b0LkHWrocSe8AhIQwXh3JF_F--WZLCpa40XLsGE2fBuUzxNm4tYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h60hljsOyV6zEro83U5M60dvKpu7F0MTTvEZQEuqS9-tDr_gVeQMMf6IMnovtNpH5D60ZM1SY2VNGNDldVE3osbrjmb9Q3SE5bvq8CTzU3XsM8GkTekfz2sTP_1nns_Zo2z0Lf1G5DZ2gbGyemWqUGNmuwbaEiBFIT0ikgytOgrq7h1MOEni5I2tCjNodoATNwY_bgJG7EMVyEWX1dbvglqf7WgUYKr1V_74Ikwxgdh0a0tgRt7AiSA8ViYRQYs-4DnxQISH9Ay5uNabQwimABnv3LP2CPYlSnQOgnjN8_Sqqrnv20H7Ij4E1t2Uh5eteSJSgu5TB8cT88vemKJ9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXPQUKEnQPan09bWVuu3zW9gtPq5XsKi9nt3IEJbXCWHlDHKcAb_yMHh_mqRcjnpEq9GYFr5r4_EhiDjzDtND-nqS9Bi1s7VhUWcK1t34vtj-mNTrcunIeWeBoa0b6JkiUbik1EIJhspO0JTpLZd-m2opqHmdIrg_piEwbk2GnK8-HYhAMs5kz7FgwmkxYOWygY46cZjGtZYHrizEOA3dwahHlFDmJxgd1C9r4a01GlCUD_W7uC8aUVYdgzp5lbV0pbzq2-jyanKbhhH1tRAJBIM_X0cn0WD3LbSGHj0lG-JNl9BCl_7mabB8ZGhcYHee20QW2DIStme6M2JTx6ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=F27ArQokIdjNVajySQTafrKjdXhTM8VDc8AFlPgBiMKLw8OW54Gybuo5TwYY0Xg6lg-jnbrmX6Aw4ze7xCWUtg88nHRoHPiQ1guW0Xfv2F3s0FZOX0-d4mYIoAk_oiL1HOl0DRpCxMuWvnf3j6FSPTAFmYDBZl58PL0kUDxc7Zq--zCv-IIGf_0QdfbSShuv-CwxRkcnqdz4RLhJIIsVbC7CsejUB4Mw1djdaTL_1wvpA2mgE99dahz2img3NSD6Y4BGkUP97XkeiQEg-dWAiCVQfXhA52YELI-cE0Wx0NIlvVuvxZzXIXxrNueTWYACpGL_RrNF3ZnHH4SVXLoisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=F27ArQokIdjNVajySQTafrKjdXhTM8VDc8AFlPgBiMKLw8OW54Gybuo5TwYY0Xg6lg-jnbrmX6Aw4ze7xCWUtg88nHRoHPiQ1guW0Xfv2F3s0FZOX0-d4mYIoAk_oiL1HOl0DRpCxMuWvnf3j6FSPTAFmYDBZl58PL0kUDxc7Zq--zCv-IIGf_0QdfbSShuv-CwxRkcnqdz4RLhJIIsVbC7CsejUB4Mw1djdaTL_1wvpA2mgE99dahz2img3NSD6Y4BGkUP97XkeiQEg-dWAiCVQfXhA52YELI-cE0Wx0NIlvVuvxZzXIXxrNueTWYACpGL_RrNF3ZnHH4SVXLoisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=qgPbkB_QAE5_QZLjBF8l1bjLqDmHyKEAYDEhkm88mGys3NtbCnELqwu5pHmDbLpJ_fpkey12voZjn8etVntWzD1esar12KKcaYa6PTtWsyvubGbWCrxvLmjcO0E1N1o_CiqcTpC2ZzJncgUcy8Amyu3SJxOXHoyDhNKl0ntxD-Nt4_huL2BUNUFaqpApn3sLdw09Y3BocjrEv1Dal5U5nsusDVUX0ZuqazFlMeE9VmhM4Ih8lDSoNbDkIlzwUHq-wvXewr1SbSbk1DViV_Vt9GuHSCqgEW3UnFUBlDqPkoG0vnBRSbAz6_1ZJLp2Uz4CVJ98THbSuUdfsKHA9-VJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=qgPbkB_QAE5_QZLjBF8l1bjLqDmHyKEAYDEhkm88mGys3NtbCnELqwu5pHmDbLpJ_fpkey12voZjn8etVntWzD1esar12KKcaYa6PTtWsyvubGbWCrxvLmjcO0E1N1o_CiqcTpC2ZzJncgUcy8Amyu3SJxOXHoyDhNKl0ntxD-Nt4_huL2BUNUFaqpApn3sLdw09Y3BocjrEv1Dal5U5nsusDVUX0ZuqazFlMeE9VmhM4Ih8lDSoNbDkIlzwUHq-wvXewr1SbSbk1DViV_Vt9GuHSCqgEW3UnFUBlDqPkoG0vnBRSbAz6_1ZJLp2Uz4CVJ98THbSuUdfsKHA9-VJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuUDwvX128XJaXjxYldhwFiNC4M6cWvP_HZ7-F7gTdEj_Pnk1zvyXAXe4CioPXwNFeh4QKMfNhed_GNZSKIZMMRoYu2NBvOMLae24BRQGhGABMWjUX5czGjfuorVWTMyW5iaTFEpfqP0S3pwJ84aXDWuvUi5oBdI-RYBXeIWYeMkw8GFelCsuSsDom552b9TaliOMmHhMlX_RmagczlgZAqsYFFakJV7YqqETCJamb13vo_ydpdo1YZdnzWVODQc6MPFQe5yUMo6VH7T1c3Gv9MKkqh8mO7_IvcuFOs1RZZ9BL5A99VDXj8Amyo5bmYy4LlR82cZCswU1jYYvHYqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAuANzsnBQDq0Y9KCNCa333mqadXIWhFOnZ8YQAoR-oF4pdV9EPiQq0flZBu63HkGW28h5Yk9nvRwTefsK5zzf4FbXlGtzwxQ2T8-yI-5FAAsFOQusXpWOCiADP2JEhKefB1dU8tQi57nBg7g-8EpajULCtANCpKX6aZV_axeb6ONf4Rq51cDLeMSW-50kmKmzUpDWuCr7anWmPLnthms1TeTJXy9-f65GXWP2V497hPXV88RdpD6iyEjTtyGu67a2nZIsK2on_WTPMsRSGCUYErNied5yeZRSQFXO1IEUmbnt3X9vhwr3i0EnRqCGReKq6jQys6n86ocblsTAZ3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biqX1RQEu6inLsk9C_KKaHxSS7WP7iVbmT1YfQSwX8Luo04wWkgMBNnvq_4bT5VAS2OTiQKDC0mfdINGPKVNvYhv5yoYAja8MNWG_gxL1UgTgDKAl--LyM3OFIzTO7N7DI45T1ZdA1iL9409gg4Ojf01YEdfiO3MMHzK6N5c4-vaCqL2Nzgx2R1uDzkGSMriqBfkVrkCU_EWwDmDk9RQIZg-hMn35Fz00JG7P07Zw2K05CPA4ql_EQcEJ7Wri_j-mxt33e0joY7qewYQhhDQor3l7FuheTc5zfUbAKD9dljCmdTGBHnICAbvZyVwK96RseunBavcXlWwWMrzlQezMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=BakKL9XVTcx1zCZrnucgI3vibzxqNhQKOBdAjSrjHp0N4dGHCrWqah5aG1NwQHD0wb1gpojX4iYr5LOAbXFyhQ7D95yNMgTR-mC_ST1s9hRfiVpe3B2PUbrOkh6Vvh9JEzQ-nRjTVGJv16r0xbC6RGlbuHpkbf-kYbCSzSojeE7nmDAB8ElNv6ls95AESX2edgURBL6yzPbq5DL_a__bChZoJ8Enwj5pFFjlk84NlWSa9q88aiU_jVhGBsgeFcszolHRH4NJCnQgeTr95FTFdU3Bpt6UqQ1z9SI7Tc5wh_RnoCnpJNNoTumdS5fc-srquV8BmwEEv0Fs7C_EJzh_Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=BakKL9XVTcx1zCZrnucgI3vibzxqNhQKOBdAjSrjHp0N4dGHCrWqah5aG1NwQHD0wb1gpojX4iYr5LOAbXFyhQ7D95yNMgTR-mC_ST1s9hRfiVpe3B2PUbrOkh6Vvh9JEzQ-nRjTVGJv16r0xbC6RGlbuHpkbf-kYbCSzSojeE7nmDAB8ElNv6ls95AESX2edgURBL6yzPbq5DL_a__bChZoJ8Enwj5pFFjlk84NlWSa9q88aiU_jVhGBsgeFcszolHRH4NJCnQgeTr95FTFdU3Bpt6UqQ1z9SI7Tc5wh_RnoCnpJNNoTumdS5fc-srquV8BmwEEv0Fs7C_EJzh_Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD5z5yRkIWK_J9rJU2O_wKX0ZnKKWKSyLXI9GJ0L3yhnPu3a7vYi-GgzXzJkEWx6UCdopFPk4WvZDDqbrDoa3SVH5FT29kG7ckm3liqn0oV52uPoHu_cjjZUCepxv59FjOL5fviQ0DJcPLHtjfte5M8sUuIu9LG5TDLI2cuRVVC9YV6Txm71GTHYYcjWLr4I12RNzhxN4kwdtrXWg-rQU3UbW3EAGtASlvOdZTDUVUT3asAc3vqeJghpVKvcBNieCSpbGipgkb4u_Jlbgml0GY_W8JoVljkULOzpC8lJzCFbwR68vMizKEPK0yincQ2lwqee6jUUbF4WliotvoE48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE6vze9k73ij84nl0_twxVe2vQYA-uB_PIPkfMOGkxLE7FSTFA61XZ2DdV1835OGdO3yBvKf6gwzo65RfAv0Yy-xWgmohK_Lzx5sg8gop5HzhCcW6padS93r87q26C5_kAZHos0ic_8INcFmtZE2ZY5bfHkdlUtG9YN_x2n62UO1kRM5Mboa2EflwR7rLBZyLFBijIFUN6EMClHHLSn1u_n7RlyRNyRyah5sB5sg9BqwpfQC0fsKLHXBBden_Rh2J7en4U0zrMIGIfzbvkb50UL6n0JgfITjDonBdJO6Du-uzO-ASuyiW-hZn06i_7ii2A7e-aWvkf4zCFzsO3viJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjAfvZlkt7gQEZDnOGgvX7lIRB_L0SJqTkF7paBCUAHi8DDpiXzTY0K5sDqZ0Qvy5Lm2RBkce6lmvAPyjo6Z7rK3wizX29ORM1VfcQ4O3MtZ24s2cy95uaPHrgyt5KbsfJlSC4P8l_ju3f6RIo4EU5RKAKYEGpviubi96z-HY4zdH-dTcWSQkJjNwNZ5MLRYGkbsZd3dfivDPEzXqmyNeYO5WcIerHsF5V_dwttf31NBizFazsdnYpCmFGTIEddDy5BtmUibL3H18NpZD9oqLsxG5pWjbljHrFt6EV_P9oz2_4fwjuxxjUyWaIS_moGGegCweYxdQpA2HZ9i8cZgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMsD-Het_QLQU-RJEgvFVAZKvMD0O1qPhkY1YNv7DJ6O0su7_4PzjjNa-kOkx0CMNtZvtF-1POWj-8MVkzpZyF02i9N-xo5ZMTyTKbj-qBeafrKIPX3E6xq61FpEPzSxi7aswypDvyuPChAu3TtDHk_Y0_aFCu1AgH1jATsY5ZJwCRMI1HskkkFbuRr0Q0ku-8EBRF-CPn86lvCp8hbW5GFxhs5sXdtL6IQi8iLtsXZrulLauUw0AQfYSTxFtAtWsLHBzzkfdoTs_QOzeYQrhN1_H-XVjj8iA7i8KRiPNIMqDDmnc84S8jK-nYkRs5bkFE94Hc5wrlc31JzulhAZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=BZlofvY1v9syO7gd1dvLpNBOzZDxWmtn-8ADNeqQODwOQZoSxVm48Ua3414DHOnTPK7jRNGwt2HD-7zjvIb0JEvRDbZg_tclJvN-4LPmHWl-n-DmmrrznPWJ4G9cnP1iLsruzgTsoTB9qHWjTE9uKOLrGnbGt0FtgQF0tYuSrS19DYy2IdArQk5CFrKbADy74k5KU4y2tYjy7BR_8K0LowVws4kpavu-KOwzEXfsRaprhoaMEJOxBFGTlYNy6YhDywwVxbvf6Y572Eb3oqFCKLpanTJxVW7wWx5kmFTqmIskN96dPGJxgZotLfSV66LeTlBvyzvWpgZ-2sM3Kg4VDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=BZlofvY1v9syO7gd1dvLpNBOzZDxWmtn-8ADNeqQODwOQZoSxVm48Ua3414DHOnTPK7jRNGwt2HD-7zjvIb0JEvRDbZg_tclJvN-4LPmHWl-n-DmmrrznPWJ4G9cnP1iLsruzgTsoTB9qHWjTE9uKOLrGnbGt0FtgQF0tYuSrS19DYy2IdArQk5CFrKbADy74k5KU4y2tYjy7BR_8K0LowVws4kpavu-KOwzEXfsRaprhoaMEJOxBFGTlYNy6YhDywwVxbvf6Y572Eb3oqFCKLpanTJxVW7wWx5kmFTqmIskN96dPGJxgZotLfSV66LeTlBvyzvWpgZ-2sM3Kg4VDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUaZJyW1POy6xh21wmTmquQzfU6KJ2-PMGrHRpNjUmdYQcvv-D_ZteAdn_Vk-WIkspaXmokW1Gu0ySyF-UUTfQkUAwUMCl0qyho42IQUBUcX-5yR9gyGvaGtxC8Rw1y11iONXmZWOWI0eAKGp0ujH4aN_LpbCKQugaRvTxV9VBGA8bo1X-HG93twElCsWcvdNsfRLJxHqJRrwLYjUxDsbm-ESdtIOaV49dAjVYmqhyLCA9qDnRq5rW7C4w_pdfLvksLOlx7DjWi_kznu3B29Yg_yEnizTqu-RkKDFBHjSlbvhdqQGDd8th6GbqChaHxEBWmmjxedvN-fan74SdFA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKrwxMYXu8HqNqv-4jLJl1sdmYuduV_Nks0Xl87mj4T_XM6soyZsMf4Of4BVXbjmT0cmuMlYdYkBZlF-SKzpXCSXZOyBaOAUUwRci_6wkrnI4r92AgZqnmLEbtkLYqZfXSE9HaUFDgmi83urp7bS-CLfMtZzGlEClg5moRpwZDGCy_5MBr3kfMzhsBL9frjtHX1QiVHsVp3eFqo3s_sUhUvwQG6iTb9rn0xyW1u4ugCCPa9GEOfpoaYhELXXJQIzDsxhBCIbBP33DoXXrYREW2-Ay8JzDfc7bG4ej6H3BwkuIFrQ3NPx_6U3_iuTgE-kM4MJzydPMDvPcdz01Gx74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtMcMgYPN8hkAumTaxq8WbBJfel0dVBhCYybyudyn2jU0Uqd3BmUyW4S5FV7ndWR1Uj35kP2vIaXqlL-SloLIAQzn3NW84d9HmRp-uifkKyy_j0UTMTQrEhhXtoiXKu1cQVZhLRgmyWBprmCXVJGOqK91-EIcRVZcf36IjXOknZp9hi4aeAJuyP7OBesCWHCk5bnn5XmOiFA_O48PjYqgjgny-nKkWdApLBs-RhXtnHiHpeHxfHtmm4svB3m1IzQIgTo54nOljJckl7dHNTsIdtps0D_l6GQ-V1WK_iDhAn2zGIPOuxgu3W_7-vk020Sj1XSqViG6wEr1OCH-UYArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SC_bOSA0ixg_goZYnLi0RKyXl1OdxbaoK79CmIEKS54yUukF1LnA0yqtmjN-ULmmHpzkudva4FTyAWPDlH1M4seSOk6ikjEYtKF84Hib5lQpewZmnMac1GZhkEzQLzDp_jpEohei9Lai4JjDjTuXQxQrCYqdfiFl6DCZbEaSD5MFi6u4dhZeqn4iNJlW1ywHcEzMgqoL0H3B9bP906o63biEYmAff4dZBAAPJYdsOxKBKXvDJ3weOydUMW4qNb02j-GmvDJJGAhByxtSZdQSenImPbFZGiTx8NWhyvgRTZEX0zlIY-2cGaAmNSoDQF1CuqmL8eugyXJ0oTwD49iVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SC_bOSA0ixg_goZYnLi0RKyXl1OdxbaoK79CmIEKS54yUukF1LnA0yqtmjN-ULmmHpzkudva4FTyAWPDlH1M4seSOk6ikjEYtKF84Hib5lQpewZmnMac1GZhkEzQLzDp_jpEohei9Lai4JjDjTuXQxQrCYqdfiFl6DCZbEaSD5MFi6u4dhZeqn4iNJlW1ywHcEzMgqoL0H3B9bP906o63biEYmAff4dZBAAPJYdsOxKBKXvDJ3weOydUMW4qNb02j-GmvDJJGAhByxtSZdQSenImPbFZGiTx8NWhyvgRTZEX0zlIY-2cGaAmNSoDQF1CuqmL8eugyXJ0oTwD49iVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=b_rIElf7oOhTVuGC7-v47SqLG2jsyrDrV_5Kv4i1kuexiOswwbC8zeDjHmyL3_FpAAvHNMMdT0cuD84y60Uypi2y6nuTeTHMwQGTS_3PH2aNLmh2eUp_cV-OU2zBWSdNcQDykRQN2nHsCw_v3ufHG_5ZfTOBDexWWvPCEUPl0R1dy02LZieVgnlbJd9hQAhtc5V52LfZp5psAD0jE5xZXoItp4yeG7pvYOnsbx9rDPu3d5Qkw2BNzyMWheJzgM7fTJhbfwnzm8xZcyG0XdXpSvIgLOlR2yED214DtOaGXUzJOxg1Fhk8Bf7jAS8Kt-dkk1_IEuYHAmf4vqIR-m7qfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=b_rIElf7oOhTVuGC7-v47SqLG2jsyrDrV_5Kv4i1kuexiOswwbC8zeDjHmyL3_FpAAvHNMMdT0cuD84y60Uypi2y6nuTeTHMwQGTS_3PH2aNLmh2eUp_cV-OU2zBWSdNcQDykRQN2nHsCw_v3ufHG_5ZfTOBDexWWvPCEUPl0R1dy02LZieVgnlbJd9hQAhtc5V52LfZp5psAD0jE5xZXoItp4yeG7pvYOnsbx9rDPu3d5Qkw2BNzyMWheJzgM7fTJhbfwnzm8xZcyG0XdXpSvIgLOlR2yED214DtOaGXUzJOxg1Fhk8Bf7jAS8Kt-dkk1_IEuYHAmf4vqIR-m7qfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RS7Mo4CRUezZITao-TrpdsVW0R5hwVNHTFmLJNefq9YK-8uGTEo0NQJvDRzNUL1X-g2w4ejRiySlgkrysypWxkzLwWMfJlKrLm6XYP9oHQxa1cVikLpHh7SLxdp58FRjUbgjON0qrwvFafNnskRUR3Hc_qNyVLrFwU8R_cFPcIyK7T8FlKn0p9J0TjXIOFYGOh56LdvhNwDoeC6_eauPtL2nOw4U2nqN5pXt-s-TZJUbuxCOts50kDHEJYbjPYgDXKlURZYS5bKJHu0wHocg1KVZlzkF4_JKG4cqLoEtccL2HNbFm-qNAVR0-ykcqNKtZZj-wYW7yHGh-dI_N4NjGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RS7Mo4CRUezZITao-TrpdsVW0R5hwVNHTFmLJNefq9YK-8uGTEo0NQJvDRzNUL1X-g2w4ejRiySlgkrysypWxkzLwWMfJlKrLm6XYP9oHQxa1cVikLpHh7SLxdp58FRjUbgjON0qrwvFafNnskRUR3Hc_qNyVLrFwU8R_cFPcIyK7T8FlKn0p9J0TjXIOFYGOh56LdvhNwDoeC6_eauPtL2nOw4U2nqN5pXt-s-TZJUbuxCOts50kDHEJYbjPYgDXKlURZYS5bKJHu0wHocg1KVZlzkF4_JKG4cqLoEtccL2HNbFm-qNAVR0-ykcqNKtZZj-wYW7yHGh-dI_N4NjGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5vliRsL-WckhEZ_LkUARZECVgyXIqeuUTmexmaoRKLzL5-8pjCkYLyV27RV35_cgvuuBzBVv_X4S6IGckpYphF9aBP8z8uX2Ytxa392SkFoVLF8Mohg52jAcAXBcG-wzXYfqMf8UfUQm_6GduQXK00bY64qV9774vbGvusmeXU7Ya7saLt4wPNPynHDv5cVH-nrPQ497daJ-fyxc62ynFBHejTm2Ux12yI5zI5oxgzfPQYO26jWryMjsWbZsrowNnoIy8df7M39fCyJ6VPVbkXlGcU_kwTZsUZYk6pqsB5zJV2YYX7ZAlbG2uATXFtvqlvjHAPitnAApr4-w31SWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-JFGLwFMRLiShikJGOQ-kGaIPJji5vDWurtsmURsSPX5CXnzKSjhfZZl6RJz012UyPlSTiQrze5Zdt6WRxvtr_fqQ8bGk8wcRU6QQTOM_UgyhDLwVF9DzLKpLL5xn_Sy2lmdKwRtKYXOJHpuQk1Dr5yOT85rOf_67AhppftVAUWB3QynqWMpiLFv9iB9ZvxgIPmtKg0RJZ_-6t5UhKbGyekWKehbS7hxJBF1iN-F0b_eKj_jwDP6g_aZcsmBaLM5H3C14iH4hh-wg4TZzeIvYwKelB4oUK8dElw5SvGKKpQscENlNuH4xtz1AsOS0Iv1BhNUD3fC6ecCpLjrmo5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv5PDDswdlzVA0Irh5iut3alqz1K1z_NCmwk0O7atCyl8pxd8VRUg1idqvp_RUUdenpRJj5yRe1cSzB47bMS0tvoRYEyRhVqyJgzHS58ZZLICWxs_k3CREOW81GQQCGZot4h5r2_btKWQsEUSqkJ1sPL3Vi2OpUZFVwrGEOX0KrGR6-s9tQrMuk91jthZeYtR2-cvFKGyExxdTqN0EYmRHjJP94weRSVOjmY8tAk8bq0qJNJkPpPPta_O_W7Gz0EKS9ZcAIfM66ZeZFbKbNvfWc55s_vK5Q332-PnF1GwL6qZwhra2C313-lK7mCW40wuQhcgKT-L00Ys6sfa-QONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgI_gSrveY0ezhCWxvS_1t08yp3KBeDpLj5oWg0H1xONrMWvIsyBuMZULnOeFuZXDSIUTI8_QcUz6r5nD5ymh_IeS3I-5feqKPtmBeM6IZpJiJUfarCiqLAneCkdKuzPGk7Pc34agy3gRlvW2t2uQwmjJae87cYC13NbLBA7wdy4WdNAPMSrgzQcsa0pZKnridNI0dEq3Lxnv0DWQlEqbA-toSqePmmIjWhG_7MfxtR9Sus7A5QZO1uyvyjPKN_YRwUI44D-CmWWvGMIjyX77aK4mQg2so3XiUHIRIi7PKOgcMEpxhtgQ-sS0bwVy1sdEq5jL-jnp7MHMAGH9JciOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOk6Bud7DXPVfYTbuLDEeMfDnGeSO2ZilMjaANmxL9FQYQ3Nj8thav9GbepWDon4_3lKvIHagVlQTLPfD7IL1I6P44qMutC_tFgHjia5W-uxHAu2JhG4KdyefLTplGsL9YWW-vERs2S37broN7WDGQZFCbS8BJn5ZYWfXwsaGa71NpJpt0NxrCPs9W1PWlkQKz8MIHLWJFII732fpSrpuB6hghS-m5Iss0BFPZ74BcvZ7tGUQr2CB5VSPETBEMv-Cpo-ZrePq_8l_vZlve4VBb6AZJ2qyAtt0vWs4cFkZoqJQ3p1vZIszcB86ec6x21G4vFCzZhH2ZiKMTEJyTZUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbhfMBh3PmqSv20_008uhIWx79IasSICZIBjpvPy5Blk1HzwukmvbM7404ScSc70AFRrpG8WX-CWp0YD4wXrOYolhiQD9-zp8a2GtcHL1HdxUz2X7nfy78W5z3o7Mur8gxMmASWjVoCLbgWg6E6QCCEMRUyrluY5UQpIzpI5XNBfETBRQC0orqSpROmVKSNRTVQ297M-KGvj7g889wkgcz25nMh4XhGj64p_IsT5O5d1sCOiGj1WAGJSTqr7kXY2AYPWuCmUCYNfrvVF3TYPuTZPk65phcwzyxUgRV496KvNCX0UwUb49AKDcnNkF_m1wLxwtjgYVBvEQ-thv5-2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmHrdfx1whfJ_6Krg1jWxfzKeiT3me0spM7G3CPSGu6PTR0M-EHGJE2cX8KMxOD1MN5HAta7RRMfEMNbm7aRW3BKY1i9iZ9HxlA2Ihp0xXAomrH1uoHcVmr54WmCL6E5D9IMO30rgp-0_5psfn25GxiTPx1FvwwNLHZp9ajNwH42YcekHI2QSj5pvYj1u64LHotkumCUMuNbm8Yo6t0-xQQ9Qgg5IEzNnbuDe-O8tqF0-CuF-Nvcjw0TT2g3smNomWHfVd90ZU7z9iOaCp7cjACXDgdSG914yPV8IJi8_jSuWehWNnvycgVO4qcdzF3-K34KEN2M80yfYUwC70ve7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP3lgJ96rsbQBw8A8vLYhGFH9YWBn9ye7QCD60ZIYGBlmUL1E-R8AR8U1tjFA35eoztl6_ra35yKy0WDY7bpe_LTitGDmvGahLKRlUgl07MaEHlscZVuHeFsmRoGp73j9qmEe9tY5mmxjO7ARN9zH6aGYOdhjlJJiS8LfKKsGZjBGoXghTxga_VL9Ayxb7wxr6vrwx0JF42nf2uNBVehXnL3lswiMyi1LHMyFdDDqcF0NfPezVOYVCnIOPEoDHG0G0IBby7jMeIeoS4tl-Euk73tmemcve6NbY7ZH1UEjC4MLhqv5jNzyEnbzz7wluFzXUVywbfKYDmp7votXIgM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7vQvEyd9MZLv8F_vKvc1Ymv6fCPgezuB1LR-Vn7i3xBm40Vsejt1OZcvXxnqDQH4HnEkaKhauj2Tew7y9_xmYzJNxDbEFu0ebeRfZjHCPM07fRPlKLmWu8tq2r-63u8RhMPeeQxxgTcFrSGyjvM8qKzeLi5ouRkXcqNW1Bv4CD4k9W0IqfG68jku2yEG6V1uIwnOG17RRKXEy2omVNfRHZhieb1WkuGS_EY7_pV3m3thD11qtQkOcJiV1D9NTt6s7n8q-JXUOkAz-G0cEQgERQKhfHn9S4i8RRPgtB_1WsukXcBeP3eSamQV3xPyqjSr2Bv5adL1oXHzNdWGhZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOHXeQdgpImx28zIDB0GP5-J9joWnWiypALqy6WiF3xUXbWblrxQnECDR5U2HPmK8iqQv8d_oy3-K3yDIVR65LfHiTzDnoSF7rt6hcBtXNtIDb4cedyA6BxHVEHm9lP0do0RWrs6iGmVjVqq6dn3SzD0He2lrkwScAmLe8tRbQ3VVqxo8lYJFR0bjUMzIXJtTngsIkS7C6TCOZA3BmU8Vyu4sdQMRs0rRADYbMBWPwqyakhLmOrU9Nv8-mB6g2lgLAwzusf4GZWH1CqXlVm9ekwcsSGc_PlEZQ_eZp4WNg8_cJuxbeWoIBGj7p1FSfD0h4Nir9tMPK5_pb20QBBmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gutrF3t9d_mIb0UqZL6Ao8PcXjuKAPuTUhgyrsPMTqmkb5twg5oDwQEWeRJ4K203mfq7V5KYAvpW9wU81f-Q9kBrTvs8e_tYB_neTa64f6YNqDYyoTkSt9BityJcqb8tk69qEVscL_gsX7R4mYKm7PWjUL1KAACJDOxxl_YUQQcUWIt0bvjo6gxpvyqvdDEstQ4cJAYqtx0byTWPMXrmS3O8srVH8fgCxHkE1gYFBRgNe04LjcMvxR0SxrcR2ez9c1Sek6zdG8yr4RFaKlvzwC7qm7UuAeZx4VAA_GA7ug8gK1tn1feoY680UL7FnxG8d0pa3b0VWPi3gOzQSJ8RVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI-zVHVazZi5wPSdVCZrDJqMcb_tksl3DhR9rBD6vHXt1Z8_VBatAlDVsXvivh5YiATE6b7BV3iN2pjhFVDlySs7xWhAAE438j-PXPivUaadfwRBp92R9AJeJHCc09LCNcCiR6Ou31K3gCpyQoCf-f-pO9FdkfN4CDB-O89lQbN3PkzVMteSxiJyyGA66Ry3VhjeCJLdYtnwl38YEbArUwEMTZptEhJA-Y-JbiH2QlImGi47m3VjuEnpCTDJZHqNwMaefJ7AYDtb9uAXFV6oxkObLmax5Gsiz0aQy3WTPB8I4U0ZLm5mOCjBm9BDRe_oatwI70Xi6OBEvPganUzuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQIZ-iodw4lqnwaI-QjdVU8-f9Bs27vKOE8fQL4sji8bsbPsOFz0gBj2x-YJ6NBRNEakcMTuMOze_szG20Kmz69q0s0lJhBfPdpDRddP7qy7vZErp8HOPxtVeV3VQ1SpqyxrB60kb4R8pDyqG2uPnyVfSnczbbIfxmZ7EvD3tN_e3l323avjrhhrepUoOtBM22erTGjrcFX-D6j6U3ewWqt4-SmKm63fB4HmEpGKvMP07yPXK4Rw4xbVn7k0hLirhU101sFDc4FKSpsfMioS0ld2HAHfWG126zDSKgqhDHoIpmlM_BBfgM7-734lQ7bRGXiP2hiQLFxBJIJVBBB_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg87Aw61FGEHIvjxUwjWWJ3XFxtQBiq4f206YTq0a6fdtHPdht5nYJEHDccm8LstoPnekDfJMqobjr2fmw1IKbxS9O79iDgJCWD3XFFqYO4GI2AaATdXgNOSvF7fIy7lScU3cR14Q8HSSzapd7uQOqCIZH_rP_gXWs8J77jPmDUEtCQmfjLtjwRtHVJ0JmDPMbO58ZUXe53gVxpTVfNAMFoGzkpO7GoC2MtPS3maHyw_rrz0RUAV0Wmd6bc1xMbo66ICbWkKPm61DLhP6NiZf8vxBOyvlllrPX3nrtQAeh8TMzrcKBeCwFcB5fRAO3xdm15V7y_XTtEIqRShP8aFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSJvXoFiCYBwITavhTAeQoP96mgPLGiPFgMSEruAGp4kvU70UrbAl7ZfuWTvlw-ERVU4AjPqxgFBxnQByFektm57ggzaIWpxFvNcqkWNL8OTwb-gfLo_R3xmzxEznT9ebtfKg_C_tCg0Jg4D1UsipU82Cfm6wLNHchheANY3nZSXwkBx6a17JiU6oQnE9bQimAcs3jO6_wt4pB-muW08cRNpXhO_k4DDA0wnnk2NjDxzFTnGjxm3398DlUmsuBRxDzay3g_XLCc1NWO2b_DK20Ys-F-icXiT8up41wvoB8SORlY7AbPq_ffreKbOKoLoMLiSsgzhuUfKJTMzvCChHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=l7Hewu2ZJHqoyisvEUPVJWwf6ibvfl3TjhbgXd-LX0kMR7ixU3Mt5ZFIOfK7OVtHGcJLfnAHUizJflhjxcaRXfM9u6My-UOVsyd3OlfEIpoIcDeAHO4E-HVTQxukA_UQJ9huZYXahiJHyzrfCrxNNMGhVTKb-7Ad9ZHCC9temNWiBDMU-Hs6VGUcjgXp56AGBDyMnvQ-D5tAfl0jWIoQuTUrQ7lDXxarkxoUhE3nxSky1fdsfEm7xIfvqn8guPgJgM2vlflJJ6gzjCQjF-PUtQujnTT2XS7LCioDM5zanXeiqbte9Vbio13RMYdRQfbx_Cg0_hG3hxAsPouZS7GdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=l7Hewu2ZJHqoyisvEUPVJWwf6ibvfl3TjhbgXd-LX0kMR7ixU3Mt5ZFIOfK7OVtHGcJLfnAHUizJflhjxcaRXfM9u6My-UOVsyd3OlfEIpoIcDeAHO4E-HVTQxukA_UQJ9huZYXahiJHyzrfCrxNNMGhVTKb-7Ad9ZHCC9temNWiBDMU-Hs6VGUcjgXp56AGBDyMnvQ-D5tAfl0jWIoQuTUrQ7lDXxarkxoUhE3nxSky1fdsfEm7xIfvqn8guPgJgM2vlflJJ6gzjCQjF-PUtQujnTT2XS7LCioDM5zanXeiqbte9Vbio13RMYdRQfbx_Cg0_hG3hxAsPouZS7GdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j45hTF90IRwkeYs8vli_pgLqAvlM_Ztt3Dq9IL-NJDct0qjuX30eFxLmHBrtFv60UH5oQbPFfpJRBCVGbQkk3cOO9t7SjQeO989k2ZGbt6Ob5xeq1e85hwPULfCpSdU2twhFOZ1xfKXXyn5D3ZsPsk1nCbMUcEs0bW6nVtk64M9OCgH779kj-Kj7jYpf3IqkqPugvchr8WnKPESaCMOgeUyn0Uj1DQjo9HPC8zt_doKV3kukGcSD8yni7rtFhl9ooALAwuI8L-25Ay8bYdTU5DK8Ljyxp-2ptHZpojeAyVWA0PTiA-UiE3aG1GqiSBLmWRh9PIXx1p6RRclhtPr11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BebAZpkUv3A1-EHAmY-F9J7RaPPVDpaCk9GRmk_37MTkKyd4g3_qs_rLtbPqa_PhR2fTfZGoJBTxg8-dtFhxqPPHTYdTMuZ3pJZJ1UkkvGL2Xr7Usu80yPmJT_AzUvzrzt4q5P_4IxvsO8wM94fItH5ZgH_AFcDmS8MqfVH-I538rN7kiXMxCZ7vzjNsvuwSo83u2EG6oK8_1dlvsPRr8Zq6cyS1CHSaje2iPztNpGrl_qQIZlVLN6olz2nz7_XN-jXBhPQEnOE-ShBg6N1JwB_tgBc2GGqL_zO-Urz3LMqufVZ1ZyuZpwWI9I0ff3aTBlL9s0GZr5d26t9l1l5Ovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BebAZpkUv3A1-EHAmY-F9J7RaPPVDpaCk9GRmk_37MTkKyd4g3_qs_rLtbPqa_PhR2fTfZGoJBTxg8-dtFhxqPPHTYdTMuZ3pJZJ1UkkvGL2Xr7Usu80yPmJT_AzUvzrzt4q5P_4IxvsO8wM94fItH5ZgH_AFcDmS8MqfVH-I538rN7kiXMxCZ7vzjNsvuwSo83u2EG6oK8_1dlvsPRr8Zq6cyS1CHSaje2iPztNpGrl_qQIZlVLN6olz2nz7_XN-jXBhPQEnOE-ShBg6N1JwB_tgBc2GGqL_zO-Urz3LMqufVZ1ZyuZpwWI9I0ff3aTBlL9s0GZr5d26t9l1l5Ovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Owwx9BjDeixBiRPYHNIuVwHWSwYVO9WoKdw3_unwgVBz6H3q7nz5UMWXTdKA2uRbLtKvWED_mOTokb9xCozNaK0v4mrykLy7v8eiszeKvnSxUqmvZJcLYvJ9bhyDQqnD8jkd8QBQUyWLONgwFL7Qmr8NoWW0loPqvTS6RhyWgs-Gdgqt6MLLhKi1j1yCHTADXKL8H6dbmzmOOs_vLIm4vB2uVL9OcfHck24eJ6xwoNNpgT3_d0_LdLhKgwazuQ9FzrRqoZwsoC4T_YbzhNrFnxmcMNIp-pazWsaqOmQjJtdt4akWNhmBH64k759Y_aoq7tIpnFgGAW1YAIAiUQuXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Owwx9BjDeixBiRPYHNIuVwHWSwYVO9WoKdw3_unwgVBz6H3q7nz5UMWXTdKA2uRbLtKvWED_mOTokb9xCozNaK0v4mrykLy7v8eiszeKvnSxUqmvZJcLYvJ9bhyDQqnD8jkd8QBQUyWLONgwFL7Qmr8NoWW0loPqvTS6RhyWgs-Gdgqt6MLLhKi1j1yCHTADXKL8H6dbmzmOOs_vLIm4vB2uVL9OcfHck24eJ6xwoNNpgT3_d0_LdLhKgwazuQ9FzrRqoZwsoC4T_YbzhNrFnxmcMNIp-pazWsaqOmQjJtdt4akWNhmBH64k759Y_aoq7tIpnFgGAW1YAIAiUQuXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SURMZo6lQpN2fm9U3ge3e-jFjpd2DHiswOO1S_AHr1QcqpSuruu0lL_6n54UaWcEkUCa-2phPmXa2skztxbbReRrVsQrcIwZLzV5UzYjd9n1fw-R0rGpfGpRvh69mLV3gINq-z9ev0EkECtJXWU7tiORwtclj052f2uJVXYopQ6rT_mkoheABId_wqINDtwJLm3g7kKGXEMPn7HxXCe6l-VTNFD-ADEnhfhqwnBv3rw5A9wjMrKo9kqRY0yLV3R7lI5Ng5WEm5tdv_HSKstXNJDyBuJ0KqlTbpaKZe4VFpkh4BG6U_jwuVhSWzxSaj00MTgWvFEU_9BwneL3GSkMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=KpwQEM3Mvdh1yvS74DpjiHvirCCXUOT-2mu4mGR7Cwzs14nW6kVAS55hhiFcHuXtdGLiItYXBzvEGIdPadDtTvL7_r0-xRoBdMX5ayKUSYaGPlVFRLmWlKgVC4P0AnFk1PkzdHLL_A_nkN_Vxcx9Lq6lccLL78JuXnb8A2HvR88NhtxA7g00--qMq0TEMUn04iyhThyxcptTDWvKt_OB7fT7GGBfcMtJ6vHb4fja57EIKpm75UgbJnF_epC_HRl_3gWgGS1qIJgQCrKOWsN8qBTwS-BMyHBmjp4gVHiK9f6drCYEtilAcVmop7g68TAQ5xlUjdqv9TBR_eIKlsSGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=KpwQEM3Mvdh1yvS74DpjiHvirCCXUOT-2mu4mGR7Cwzs14nW6kVAS55hhiFcHuXtdGLiItYXBzvEGIdPadDtTvL7_r0-xRoBdMX5ayKUSYaGPlVFRLmWlKgVC4P0AnFk1PkzdHLL_A_nkN_Vxcx9Lq6lccLL78JuXnb8A2HvR88NhtxA7g00--qMq0TEMUn04iyhThyxcptTDWvKt_OB7fT7GGBfcMtJ6vHb4fja57EIKpm75UgbJnF_epC_HRl_3gWgGS1qIJgQCrKOWsN8qBTwS-BMyHBmjp4gVHiK9f6drCYEtilAcVmop7g68TAQ5xlUjdqv9TBR_eIKlsSGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cch12r5sosQ969Af2iKifNWLrQVQzE9TwPUaEbkXiCzJiDqGFZaxa0xSNZaLu1G_DtBNBF0kVuBI_Tcv-lAxkG1rCslct9-0nHv-ulgmIkHdTseHvjcznq4kfgK2d1N_rkKym7Y_C3bMQ_Yw6voIuv-7scuaQYs0A_QacIpAn2x6112hVd-bRLhUtmMqbgnxqBzjDtzaa2cKtH9QrjtUFSYoz6uhntyod3r2_z7gN-CqPQIMmv9wBZZV_bjHMHfUETBvyv5ktg4Bcn6KQG1ZA5OkVrq-cgBQe-3XOmSqeIA302Ee1_chrZRPXoYxIOt9RAyiYTH5zrrejLr7Va0V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktu2n953oX8kS9U3DpIhBNc1mm2C2NqEIK7VDbIizRxyTWQEyMJx7WkKQgeuOKcES_HKDDHdaB_2ovLgOt3KXy6dyM40cqyPIBZxXsjVIEm8C7XNIjthN4HP91OOZwirRKCOiDGagWZzWXd1uuz_5TVf-zPQsV9qB5P3Yf4hWX12qKnGqioWpfb-wVoZyOs0ZBfaouxVeShi0aBOU18HkK7RekVkoBBpnIwuu40ur-udJm3agBs4b2LyOr3eRq-WVGi6gMcHVFgOrErHd51bXFtFoCkfsJRLvhmikjEk6ZtTLak6fSzNSDDUGKiuIiZVnwZOB0sXRmH6awd5gkdo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
