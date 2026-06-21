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
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 693K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-94850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT-c3Lw-WcwipxHlFArQHuNY1eVzyzJQSxbwHTswihGx6tLQhazE7neGzEjYcwqmjfLD3TRNWjFJqZDU6FKTNcSeTmrz6KWPS_cGXxb7J-03LjtBrBRrZG3AWfP5XpKTf1ZzDAKGjh725LFcnuZvxuI4xOxfh025tgA95YQcQ3LtiF9Q30jIbCE8eQqyad1icjANJiB0T9h2WNM6AWzf6slTpUQqKn7mXObMd6YHmmiDaEfaQdiwY0YMDcIac0LkLIKn6aHMlJB5FooBFz0m9vq5u7gXmMU1o_aqRtY9iT8AsKc39rzNXzC7WKapBSGGyiHzC6nei1FJwAUPeKuWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم هایی که تاکنون بیشترین گل را در جام جهانی 2026 دریافت کرده اند:
🇹🇳
تونس — 9 گل
🇨🇼
کوراسائو — 7 گل
🇶🇦
قطر – 7 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/94850" target="_blank">📅 10:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUKScGV2XLrDceZTVKWmM4JzM6Xi0NWEJNoFuizCc9VsSQ6rLucv4sFgmwuqxTjsK9FR984JxhVIbu_Gf1ve9YrXdOTpz7wiEaAyr7Cy19xhRSgMZQt7ykIbTmwMMvw7tTjrZJqDNqvQFmZ_xeUhke3X_jUqOIwZowNNsMnfwSgEVL9LU2OlnxoPbz0UCHUIYeLT_mt630-EndDwofFADvTFl7Za5CMeGwJ6NsI_zDRbGeaSXHhJ_Jk8v78tdPhh55UJe6cVyYDavbtokKnYF2O7n7rkX71h2zAxzsWyNjaYJlBB_grbqFk6ZoP7lRqSnqAbpnG-_qecRGz9f-5q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
زوج‌هایی با بیشترین فالوور در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/94849" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIuKIrpgcqMUFlmEkbC-Y3ADOnQ898duNCNhIUmejx4k-M4hZvGpEsVm9QDd8N7i_xhwXLbjBCusm38HOUGmcV1XTe8uJ-II0lI-a5UZPiurUVoIbW7uVazu502L-wUpK8XCJfuitHy3QUxeRAOwxRZewEHLRcsR1vD0koeeFOZEJMY4xUSDlkhlXxMqtSvPTmzRz2p_u6wEc4EDFl-ZMRa0RrDLVq2PD-YrjdA6XtjcQrkW9lOEZFLs3LEx-GjMNuKyIFzLiN7P-3IXrbrK6nq9Ec6jUzgPBxtN-JXPEglfp3U-L8EuxhPo99S6IpOaJ9rM16slGHbUldBjky9OXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
ژاپن اولین تیم آسیایی تاریخ شد که در یک بازی جام جهانی 4 گل به ثمر رساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/94848" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJL-Ya6QJtPohzM1elYHdo-elMr3jNOiNlZa-ED0LvAdJWJGo-rJGc8GHcRjwLbG7tC0IhRRxEj9F0jXYD4YP4hblnAm7Wu_DPv_TUG-HlqngxSKGzOC6FjjDpWKegE8wKnOTdVKK-RZYX1Fuxn0CuYn7PhwohkI5rIE8vR363YDhUY1G8fhCcDGMonEUTzQwbA_LDZJhEPXMaAEyI4hUl2FkJWKsiuE1henBSckOSUiTm1XzZW3KwZ-KPwL6FjKJ4tRd4GUBsYgsruM8OU8s2ZAwfjXHTxxkn2s7CGCuIeO261XgIv2BqsJsjnqOJwJ_GaemsckGGgxIMNhQ2ehOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین دستمزد در بین سرمربیان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/94847" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94846">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36c2a4809.mp4?token=F9e8l7cmMIq71E6pm7jdxlEmrWBB4yHYVOYuYx4PgitnhGhuKJyLXcXzaKBj6ZbDMUinGgWhNySrzto3SKuZlPVpObigFaQ8o6by47lxghDTyrE5ZcSsA4BZ1IncINx_3lyoZsewtrDcrzjQB2qF7e1HdbYeR2_ZZlhEVroyVj0TMy20QZEZ0iK9xiq_pvyCB0mm86x72UMNsOUYkkZfvhh5rkzV0_HBdeAZB2a82j_kSRuxfHZM1jCKPq6g-gf7mc3YHUSvgv5atqvGO2Wx-IGAYyHVFR3EOyu51FHjc7v4a77ltQIDB_Hl_fpU7TMtBKLLDjpweYR03FdYuAodCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36c2a4809.mp4?token=F9e8l7cmMIq71E6pm7jdxlEmrWBB4yHYVOYuYx4PgitnhGhuKJyLXcXzaKBj6ZbDMUinGgWhNySrzto3SKuZlPVpObigFaQ8o6by47lxghDTyrE5ZcSsA4BZ1IncINx_3lyoZsewtrDcrzjQB2qF7e1HdbYeR2_ZZlhEVroyVj0TMy20QZEZ0iK9xiq_pvyCB0mm86x72UMNsOUYkkZfvhh5rkzV0_HBdeAZB2a82j_kSRuxfHZM1jCKPq6g-gf7mc3YHUSvgv5atqvGO2Wx-IGAYyHVFR3EOyu51FHjc7v4a77ltQIDB_Hl_fpU7TMtBKLLDjpweYR03FdYuAodCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه سمی بود دیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/94846" target="_blank">📅 10:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud1mfGX4iDQOC4TCnF_rk3VbziXZXGxEGTtnbddKJtFw_NX8P_NaoN4QDZbzl4YCaUekF6z2V0aM3OhWvwCk0NBbff7o65xFgj8p3jpUI8tBvtqVfRM1JGFefuBnqWaSoeEwtg7VpbDX2fnzOtt5fByHrJL14Ew_j8bgnUk5i3kIyyjGLpsIMrtRkEB264wws6k8AoeY3wSBAScdNJclFmhLH7IsH9MLCASsU9CiFP2rFeEpablAYfoYzyQCB4tKhyn4ngfkMrul4QwosD83Guzjjbp-o-_yam2R68GIvOxnmADCHE5Ev1Eh740eZp2frvGA2q-FSyNsv-eaH1PSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سامورایی ها نماینده قاره آفریقا را گلباران کردند
🇯🇵
ژاپن 4 -
🇹🇳
تونس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/94845" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVUvLOtggRG6_OnRXSaRmrrZRDuVPsYd_W0-BAITIcjILYGCSuRmtaNazMXizukDghon1AUPh8Nt-e5IFgQMfoMq0X7ADTwvP-OSb_CZbwjEH8U59tpudF8sl78h98Mwzh16dLmphbyrgkFEw-dq3qVCzi3Er5cPF0l_b6X1Zlz6-UhstDA5RBYML1hpmmMI8SGao641RdQNiUTKyS4gad1k1PxpXOCHdU29dHgCVToVh12wYa97KNs5lEpdgdvHkJpEHwJ3gXLNKxqsDk5BcIINhSZczv0qO0CivgVz_mM9dWDkgqC7rwo8n0EQN3YnNoEraC4bnw024SHhPOeDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام‌جهانی در پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/94844" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇹🇳
تیم ملی تونس رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/94843" target="_blank">📅 09:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbqauGwLb0Zh-9rnqg4_-aDFahaiXXTcr9N699bQG2QDVsK_QsYoiT6k7JtO1JDZCWPVRx6baU6Rpf1m_RJ-UTwe_pyITp2-IlbrfyqmuAzfVyQk26vqhocbjLCUE7gC1Urlm0_4hBsCOnZnbFaqjN_XOix8ZClds2qdUYzCurocokRHdngj0XybcymUsYb0W1Bmki2Z3QPrYM0gtOTnXqIl9_yX0GCQvCJbdW0uzjyG-AFZJ94vo-4-utuCYTYlZNkrKCu8QDlBRgSO2ngeQSBkXGoYUKn0lrNvWq5Rk67ncgBsKLreqoDJ6tH1_mWm_juIRk_veKXRyE1oNCn3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سامورایی ها نماینده قاره آفریقا را گلباران کردند
🇯🇵
ژاپن 4 -
🇹🇳
تونس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94842" target="_blank">📅 09:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f14661e9.mp4?token=VQpo91SoEGfVGUvkgbvs7bwmL5DK8MtdaxToGMAmMmLczz2kBNpf-Zbc4ti9qynjiwM6Bp4skRCmwolgU9VZF9mdpq9gbN-hxEDNjNAPSZHLIvSb9TEUTGtENem1jcn6z4Fr3GZyyaOpt4_65ZX48EGYJOW-M2kV2B6S8KucwnUYQ1wapiZRPvHd-EdQieyatS9RbTuK7r5omTZBoxNIyoL-XoNdW5Mxlvlyd8htyv3qoLIkTUFSVNgcvN5ukDh2fghJiA5xROAYkhur2U7weG4dVslQbR-gspjXMazjnouf5_FcVFG795faF-zJVVnMeX-gl186gm_ydOZkiZnIXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f14661e9.mp4?token=VQpo91SoEGfVGUvkgbvs7bwmL5DK8MtdaxToGMAmMmLczz2kBNpf-Zbc4ti9qynjiwM6Bp4skRCmwolgU9VZF9mdpq9gbN-hxEDNjNAPSZHLIvSb9TEUTGtENem1jcn6z4Fr3GZyyaOpt4_65ZX48EGYJOW-M2kV2B6S8KucwnUYQ1wapiZRPvHd-EdQieyatS9RbTuK7r5omTZBoxNIyoL-XoNdW5Mxlvlyd8htyv3qoLIkTUFSVNgcvN5ukDh2fghJiA5xROAYkhur2U7weG4dVslQbR-gspjXMazjnouf5_FcVFG795faF-zJVVnMeX-gl186gm_ydOZkiZnIXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
گل چهارم ژاپن به تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94841" target="_blank">📅 09:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ژاپن چهارمی هم زد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94840" target="_blank">📅 09:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94839" target="_blank">📅 09:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcd18e1957.mp4?token=Ft3vQDUobqfZJhWtqmKkDnqVy7W1LGxw-p_MSnGzrr4rAT9kBLty7keAoiP3lBQXsOLQAsGqfQyB3JL1TgNc9-y9M_a86UCeWq2rrGjK_7qKZ0XVTQUeuBcWfZNn1lLjsBe0WlFQQYjF5_y2ZBa3gjDVKXQZHJ9OPWpEQkZBk6hLH2MCh8lAUYjC_Lym5S29pWOBLEiK4aELYrp9r1hwxpTWPI3BYic13UGIbRrE15wPm5K7VdMxHnumXMlMaD9jGA2VCi_Qt4dL1M5KZnk6Dekl_-IUyWavU6yJbHO6GOTLga-nsZvSYwGzzi9d3AQlItFtOqF4ld1ZNkNAJ2kcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcd18e1957.mp4?token=Ft3vQDUobqfZJhWtqmKkDnqVy7W1LGxw-p_MSnGzrr4rAT9kBLty7keAoiP3lBQXsOLQAsGqfQyB3JL1TgNc9-y9M_a86UCeWq2rrGjK_7qKZ0XVTQUeuBcWfZNn1lLjsBe0WlFQQYjF5_y2ZBa3gjDVKXQZHJ9OPWpEQkZBk6hLH2MCh8lAUYjC_Lym5S29pWOBLEiK4aELYrp9r1hwxpTWPI3BYic13UGIbRrE15wPm5K7VdMxHnumXMlMaD9jGA2VCi_Qt4dL1M5KZnk6Dekl_-IUyWavU6yJbHO6GOTLga-nsZvSYwGzzi9d3AQlItFtOqF4ld1ZNkNAJ2kcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
گل سوم ژاپن به تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/94838" target="_blank">📅 09:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گللللل ژاپن سومی</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/94837" target="_blank">📅 08:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY65i1kZU-7n0m54t3o5yzJNhfijt9zARpS7TkxZlyovsvWwjYet2uHvnb0r2T-tqq529XiZ-o6YXWxVdh1vqKyxXZoCkknhdIu1lolyZuX-Zt8WRit19wVJOJS6t8NTDIiCG23E2oPnzLhhIRzUe_4yMl5YT6rGrwiWUL_Pmh90U0l5lYa7NauE4LS0McMtc3s-HdubmT0iZ8Xtaun4HBXuMRMORP9XvcFvfn8B7fakQ0HjdfM5f7rB3FOCwUNdfeT7arbK4kIlfGapS6w2nQm5JFHBv8OqBeYzjVjWYCjIAxCdH7ref9naS0vLIU6V9ObTNhKCl6cAcyF8sEGa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الی روم دروازه بان 37 ساله کوراسائو تو این بازی با 15 سیو نمره 10 گرفت
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94836" target="_blank">📅 08:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایان نیمه اول
🇯🇵
ژاپن 2 -
🇹🇳
تونس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94835" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از فوتبالی که ژاپن بازی می‌کنه آدم لذت میبره</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94834" target="_blank">📅 08:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf20ea5d55.mp4?token=RmaMe88Wvj6A8_yUNfum7dybONw-mhpvzHotqRdUc9QMV5GooHJu_kGgfUzl907oSQ3b1ljNUyekWqhugAap63Lq4M7lIg5uJyqVVabuWiugoPwQE2HWObs4EAYc5xisKG5BXyGnS-UPGWXl3mW2LrttbvxpZau3rTbHOIOyHVT0sJ0oN43tCL-N9ZtBz-lPGgcTt-ElDRXnLdzYrxH9xUbEmriFTXmgAi1FVCBCmBYclF27dHz5nfqxKLS0sG--XgJ2qGhDX8Hk9WvDbm209njqDt4Yi6aqSYCm1SLNXEwL42vlZ0JLptyLz0bxssBx959Q_MK5EBFPOWnnE0HQsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf20ea5d55.mp4?token=RmaMe88Wvj6A8_yUNfum7dybONw-mhpvzHotqRdUc9QMV5GooHJu_kGgfUzl907oSQ3b1ljNUyekWqhugAap63Lq4M7lIg5uJyqVVabuWiugoPwQE2HWObs4EAYc5xisKG5BXyGnS-UPGWXl3mW2LrttbvxpZau3rTbHOIOyHVT0sJ0oN43tCL-N9ZtBz-lPGgcTt-ElDRXnLdzYrxH9xUbEmriFTXmgAi1FVCBCmBYclF27dHz5nfqxKLS0sG--XgJ2qGhDX8Hk9WvDbm209njqDt4Yi6aqSYCm1SLNXEwL42vlZ0JLptyLz0bxssBx959Q_MK5EBFPOWnnE0HQsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
گل‌ دوم ژاپن به تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94833" target="_blank">📅 08:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSXWxpSbJNuqjgaYef8AKA06rmTVwgoQg-26dWTWDOh8dGPnjkFGzpvnrhdsz0ChwFvX-_Ba5BrASG6CazNk378lsD5WPnn6XnXIsmxo2QyWcLpZwL1PtOQKE9agiwjZJryE3nUp1pAyD08EOXa477gmIE7--8F1DjPhLgsLHaAyfx4EWqk3RFa1NAfRQbumEsunLx9aB5CgXM0jyRPD4O1Zyx_XTFRVyz3LWahLxRz-ep3ezrSnTRVSIrlnCPFsK5HZI6rENIJUWJk_36VsH9k6WxzyzDSlItyvSk4ARPBPZ9ic5ZovOimjFiektCvQBKljfJ2dU4wTV6XiBuqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صحنه ای که ژاپن میلیمتری به گل دوم نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94832" target="_blank">📅 07:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8055af24c5.mp4?token=NV0VYsXC0lxWqr8lfpJFywXjcZGdwXeGuofti-GYHv5jS8sK4qKIxw_6VRj-ps9OprYBCjDK4msFVr0vJozKBrBEzC_oPioMOxzPp1u0H0YoOiH0S5yoGdMeG4aElrjzxrTSpcAAm2TNy8_fMMm1l8fSUiwbta4XoSwhnt_TNjE8r8ao8TqI_e_RsHAT8__n7eF6Lemnj1N0lhIv1ys6JlSb4YGeJWcGnAVGtSNdeayo0TrKnfjRYYq7ZkYNBCp7APcoiJGUXoj3BJPPlBsH4r_aVeJLoLEx4ta5FIh7pjmYA4wXtltrWDKv-d4LzNcXvRuGGcYSwFy9rVhIbH8afw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8055af24c5.mp4?token=NV0VYsXC0lxWqr8lfpJFywXjcZGdwXeGuofti-GYHv5jS8sK4qKIxw_6VRj-ps9OprYBCjDK4msFVr0vJozKBrBEzC_oPioMOxzPp1u0H0YoOiH0S5yoGdMeG4aElrjzxrTSpcAAm2TNy8_fMMm1l8fSUiwbta4XoSwhnt_TNjE8r8ao8TqI_e_RsHAT8__n7eF6Lemnj1N0lhIv1ys6JlSb4YGeJWcGnAVGtSNdeayo0TrKnfjRYYq7ZkYNBCp7APcoiJGUXoj3BJPPlBsH4r_aVeJLoLEx4ta5FIh7pjmYA4wXtltrWDKv-d4LzNcXvRuGGcYSwFy9rVhIbH8afw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇯🇵
گل‌اول ژاپن به تونس در دقیقه ۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94831" target="_blank">📅 07:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ژاپن دقیقه ۴ تقه اولیو زد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94830" target="_blank">📅 07:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇹🇳
🇯🇵
برررریم سراغ آخرین بازی امروز جام‌جهانی بین تونس و ژاپن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94829" target="_blank">📅 07:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6040548fef.mp4?token=V-CN9FabV9y3J4OUVWY_Lyq25DovECj7ElfCVUij8cpdBZbQ0pUzRxOAR2xDDXo5auXzZBZdaIIth31wpY48WfWblpqkP-35QodckATghDPFGw0hoSmvT872kUDWrXhVDl7MZbTT0EUD5cVmxrvqP24xnDo2gEOGWb0bgv3MfG-KNOA8vb7fEfgVnCPGlm63_y3pkG35azzOQZHCYvbqfMbOlBVj8ycsgGaFwyp1bH7IdOdU0onWbdARbhlYgoLxO4yrs-2ha_dIwoEzBuqPUtRriO8H_23_noF7WG5FMnmvG_33hX5jvxw3NGou9urfnNNU1qzayV3a7Mmvgd3mDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6040548fef.mp4?token=V-CN9FabV9y3J4OUVWY_Lyq25DovECj7ElfCVUij8cpdBZbQ0pUzRxOAR2xDDXo5auXzZBZdaIIth31wpY48WfWblpqkP-35QodckATghDPFGw0hoSmvT872kUDWrXhVDl7MZbTT0EUD5cVmxrvqP24xnDo2gEOGWb0bgv3MfG-KNOA8vb7fEfgVnCPGlm63_y3pkG35azzOQZHCYvbqfMbOlBVj8ycsgGaFwyp1bH7IdOdU0onWbdARbhlYgoLxO4yrs-2ha_dIwoEzBuqPUtRriO8H_23_noF7WG5FMnmvG_33hX5jvxw3NGou9urfnNNU1qzayV3a7Mmvgd3mDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ دی یونگ به انتقادات:
"خیلی از مردم در واقع چیزی از فوتبال سر در نمیارن. اونا بازی رو تماشا میکنن ولی درکش نمیکنن، یعنی نگاه میکنن اما متوجه جریان بازی نمیشن. البته این چیز بدی هم نیست؛ واسه همینه که فوتبال جذابه و همه میتونن درباره‌اش نظر بدن..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94828" target="_blank">📅 06:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lgf0P2MXBTIddTlYoERRtQhy2XIemmi_L8qPne2vwdLlEjbBO_jzls9EIVIUj2gDPONbuY8gPTxYden9Cgxg-nQwecQL2rPPkk-Mnv616XFDYXsZw7SKcl89K1GsWe9B8tejT7aq-JT-pvn_-P7C68SJ_OIiHf5lJzW3LaTQVND0T7HbXjB93WJf9gl__dC0jmy4_ALr0Bd28ZZnzraFKYLcbWDFCoE8uvfB0AiTFNNkEZ6x6qoEEXCi_cgvLaMraeyYyyaGTP0KI0XdX08HQVd7Z-YiqkXkLFruNeL9zXaE_6fTyeMHhDDCQof-yYfEblpTzhOzqc9FHQ2qXtUzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇵
ترکیب ژاپن‌مقابل تونس؛ ساعد ۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94827" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bvt2lkd-XA7fuQ4ykozg2KxraGsn5L_pjAGKNp3UIJUT3ABKZxmkeGBFOUr4EbATJB7IJwF4J06uZLiHQxVo_ziy8jNPn3juFusM8zTRw8kGbMGAm1XTNC6o6WoiYLLvxxTnG49qp6vVbGpFWMzzm1siJWMg_9O6kJt1NFbjK1j92kAKdduf2nZROh6VoYQXXTsGEnHvJ4M9hk7oXwSMzZpsq3Of0Wlt2N9Kwdsx4knl6extFuiAdd_PbaemfvJTFIPwzxU1EKiWU9ByIicmiKoVR0ZLrPmsGCyl5C6anzJ8BIvEL3lk-8y3-i55xpp42WkRUFV_sUevqFgo8GtJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇳
ترکیب‌تیم‌ملی تونس مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94826" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzcpvDLFVteFG_OyEwja1SSiKN-Rij7tyNJSR7Bt2Lkq_szTmNLSs2gzHoo7Wyh2NCs3m3wxEIUQcv924ESUicWMSffI6O9lzsmg--PKlH_gsf1mgtA7RKpK3mQpXnN1jeV97Fbov3CO4RXzZ6i4FYIisNnpEY0wE976-uDFS0Xcifqz2qIh7tSNSVSvUqayv_RPvaODnvVoqGCNlgr44qIqqWTNCn2boQ4-5MSHybHgTcQlM4Bbax0nnNzRvSQm9YlbxnQFnW4zvtgWuC3uysW5Nag5i4yMfHa1avv5vKyBpUgSuMeo2Ayd-o0n0RVg-WpDEOaVUEJCDkDLcnK3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
کم‌جمعیت‌ترین کشورهای جهان که در جام جهانی امتیاز کسب کرده‌اند:
‏کوراسائو (۱۹۳ هزار نفر) مقابل اکوادور در سال ۲۰۲۶.
‏ایسلند (۳۳۰ هزار نفر) مقابل آرژانتین در سال ۲۰۱۸.
‏کیپ ورد (۴۹۰ هزار نفر) مقابل اسپانیا در سال ۲۰۲۶.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94825" target="_blank">📅 05:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHtRsiwMLj18sOsnWg6prsFHQi3KsgHAEfaZA7XbMTw0e9kuV6alMvpudKZ9Q1zGmO8yLshPjnb9dbaDYgzr1cwlZR_T5DttpYh0tcMfQn50Tax7-tON0tV-LqtTtQj73HWx3ZJSHZEbkfFDa03a5k-NB_GXJK_BTbybykaDnbpLkyYVgWnnTwnVIdSKGsoOXuRHQBpT94rdLu_-Jfcn38uaatEcls4fdYWgMyCYJOYMkcNhDa1K281yE9LANiQhEPay9KhA2hyzXkkUWjoWJwgaQvoY-lqw9L_xSLQlJ2JllL5VmxcS6-Nei1Lj_FtDmO660U_pPC0t9cVu9URZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EB2X7HJXmmPstN0C5SwgF3PcLGNOOD5uXasp4xgfNf5o9LZQDsnWcG4HdA20dFeYFeAcZdeXAHCb7RbhUhuDfJh3BcvuE6XlsLnpQsdj6KaRgQf2MTHp2h8wgDLWBa1FCsMJboL0wxYRkIjYCk0WzQzivV1QOQTjPSWf3sOGjipUQEYgaxAHAcauo1JhP3dcnCAhSwKa4yvUBGkCdtQFZ-prUtIDz-UPBcqYxHWIcIpHrc3JuyRlJ217aeIpchyQ2IbcotFjAG34x9pHWibBJlqGcyBJfZxCgDcTGqq-qEECWKl92_pPzvPOF00lymZtjqKYFeXfYsrR8PTj8-7HWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در عرض چند دقیقه 300 هزار فالوور به پیج اینستاگرام دروازبان کوراسائو اضافه شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94823" target="_blank">📅 05:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9LojSjxuD1gfoZDtv-PdLjlUjYQcBtZibtSVMnZXu7aZyyMA6lQlX56RiiZTyq9shxui5ZDFZAf-j7UkPnKOcAQYFRRvyIWcGY2wdTFyxtm7gF0idgO5LIjYAxM646TWDqCNQvWJgfU7zaLeLJdKuVlTHkr3IZG3cr8RsRMAxYQ6XbaPHyjFIENRlFqjRBQBz2vPZe0fGa8a_1nJVHf6OHmpPtL713cLMg6FQYNdKRmTRzqL7riGlyS1OEhdWuwGLR3dTNJLrCymswEraP07_UCPYpbMnVt20V7lLZv0r1g15obit1PnAHxEabR6dPreltYNVB2M8YIeJ2CQY5DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همچنان شگفتی‌های جام جهانی ادامه داره..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94822" target="_blank">📅 05:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94821">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lII8kPWu78rFmboqs4W8_8n1lsYM8qMI8DMaYablmmq91JJe_ahgikgpjFXbVTDKueTIpAygfRvkYRp76MAv6AjuTvAcGb8bDFfLDkoFRc5Vv_-w6gL3a2CWCcCyYLW6y31McMGuEEmGDV07IpJbWfT44ORHertIfXtDJoAnvItI0z1-SNCcFVdKDa9mL68URCmJhPEg0NxZddFEjoV8iuNV8egmB-IT7daPPozwvRn6ncBMdfwqQsV4flvwcdFU2d3DsSgY6_kPMZejyPZN9RdSz1eBQ_XAN9oWfL3YE9cMNuHbI6BjTOwreBCEJaKPszmUKzto0MBOQegJreIgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94821" target="_blank">📅 05:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94820">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2GgLtM8VS4sDqRGBjZd8wTJ_0Z1V2kJZ7zjcVF56umrbEEb-YbGeaeg9KU_E1v8LFqgwwdp3ZmzwCBkr-GehGyG03OYInSk8Ls85fHyHM_ISRz0Nz1Z9Hf7PORwe27aCwxtt9zRVJAuu5F_kw5nafM5RZpCsIJd0Sy2InKwNZu4HO8saZafWGENcP2CEQfkhVZBp-y-h0jkeBLCCkAAB1xoaYw3Bsj7c0c5ThiytC3xO81g0drIck-t0bzJ0SuJT2TpHEA6865o3UxHxBvsHOzwlzMtbNpBtbG0U_4gMHQGYZQtMnP-2LOhEIvOkSt9x1J9XZJmfXDA_c_1HMrkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه E مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94820" target="_blank">📅 05:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94819">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94819" target="_blank">📅 05:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94818">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfm7DEl6Nl5Kb42LfVF4PJCPGcAPDI2THIVhCs97WvfFW4DRch_-TzhyEU_0ziCLq-TBGVrSENI3Is1ZpgU2Flp7DPgh4AqZO3MU5gpPYL7eJIXjrpH8IToCy0WepDq4uMwZAKv8dxTpmj1PzgGG7GRqTAr8NVocuRqkizLLOEicFEPLLyhTA4ls_ise3o4WpQLLsCOnk2ivjG3_ToVpavURFT-Ev1u_EafXYb820BmdmA00J8jczaiN-BsFDP2j0PF3zyd4mExJB4jfGvoEgcZbg6STFZxGQJt1yytKPwvdJ8F7X1bbG6bwPPEu6XY1b1km2LgOV0CCkCJgkIHGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94818" target="_blank">📅 05:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94817">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4DRNwAtldCQeawdJXiDaT9Mf-C9xJmsxjfxy-gpYgEDwME6gOETQPCrLBFRMb0cVI6UxIFOhs5oh0XsG7UDBBY7V6l65WgNdbfB5ZAKkDCYI8d__2zIQiooOKcy-SdlBhdu6TrirdNgdoBWHP-2yxNwrblDOzmOsSrBtxlPf795_c-Ctax1wRhDp2eKKIziKMXBbn8F2HJOc21uQVswcuKTNDg_UUb7_j5HySA70b2FkGbYpYHVR_9kE6wvVn3FdhSuHooG8Ua_dZ0o0nA1f57T9q5KNEFp5Nl1l_nw5Z92wsYOdE5FHptfKLEE0a5waa3XjRM1PnFRsCklTXflNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇹🇳
استادیوم محل برگزاری بازی ژاپن - تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94817" target="_blank">📅 04:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94816">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgwuqRJOc76yq3oulcPzkg4sFZ2KPDP59NcHpeJinoXlHTHUATOawv_eVzzWwBtqUj3zVi9_U4MvOls4RSHz3vGCgfEsuu5pIWVTz7bPqCmmVw4Jc6XDjZhOqtPavuTRs3hx1udJckwjyXmnfsGnTa7ZkaxapqC5o7X0RYsGJzTjUmXFDzGxyxb3PgrvB4KKTUJhSaOxnbFdMyqPGYxkBfV1gDEwr83rn61MrMYCa1H1aYTLw8U8xG-3nE48s7t_-yC4z1_vSDcOWwA9H5VmHM1JumKTsOvzhacjCDiKcRYdkyF4d1kpvNVYXAC6OcVbtO36WlDIcriIMu7f6-U3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فورییییییی
از رومانو:
⚪️
رئال مادرید قصد داره رائول آسنسیو رو در این تابستون بفروشه و ژوزه مورینیو
هم موافقت خودشو اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94816" target="_blank">📅 04:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیمه دوم بازی کوراسائو و اکوادور شروع شد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94815" target="_blank">📅 04:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=KrJy2hWUXxwjic1G3zOUDQ3K6S6dWHRoHRlqr71KisWbimfXdfkNQHV92TITY_lNgId7HS5E3Qg-4gbXiw_TLE-FgcZ2nBQAEdjHUf31eKJZKDAJ2vfSqz1Hytxnyg4-MXEWGlM2Hie63dyWHRZh3WjXkIyLB6-gfIb1RplM1_QyiRu758UNzhNsaYK5CrAAYd5yaknMsJXdjxPBUmhbaXmFqvjm1per_c9g5MruJf5ZBsWzp1nDmgYMq3wdk3B-uj9sFr6X4Lm4Wjvu4iqCdL81GFoXVuAwjsFykQOn9n8gsmW5h5Xdqx0wwD2w4xCboQOWQQWGpjxhsPnDcHQbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=KrJy2hWUXxwjic1G3zOUDQ3K6S6dWHRoHRlqr71KisWbimfXdfkNQHV92TITY_lNgId7HS5E3Qg-4gbXiw_TLE-FgcZ2nBQAEdjHUf31eKJZKDAJ2vfSqz1Hytxnyg4-MXEWGlM2Hie63dyWHRZh3WjXkIyLB6-gfIb1RplM1_QyiRu758UNzhNsaYK5CrAAYd5yaknMsJXdjxPBUmhbaXmFqvjm1per_c9g5MruJf5ZBsWzp1nDmgYMq3wdk3B-uj9sFr6X4Lm4Wjvu4iqCdL81GFoXVuAwjsFykQOn9n8gsmW5h5Xdqx0wwD2w4xCboQOWQQWGpjxhsPnDcHQbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کابوس کوین دیبروینه شب قبل از بازی با ایران
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94814" target="_blank">📅 04:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینقدر بازی جذاب بود نفهمیدیم کی نیمه اولش تموم شد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94813" target="_blank">📅 04:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Scsq-xSeFL3RIq554MqMsTG24-9s0fJAwGhJaSjCyMAjpu-Xk2O2RYnlvSl5RbYM3nmuOuQ6EHJQ38Rf1_XeaKxP_tQW8WEr3-ie2J3jD-1mdOQtlPrR9hb6F655MWXc-W-1DoQCGYIjgmX7uS60CMHibC-Q93-IHnAdljaJvn2vNOIToH_gKBx97uaXGrJHp9AFeFkH6P-YwTOcFypmcGcWWaml0Gw19NUEm7-W7qkk47D802aLN-B5daaCLvD2Pw-9RCYuoDy0nGPdhYpSmMHxiOS3to9eC3oyQRRcR9QyKNLHoDkMYZ2e53HmHLwl44288CGHUqhvGMfbzI9LDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Scsq-xSeFL3RIq554MqMsTG24-9s0fJAwGhJaSjCyMAjpu-Xk2O2RYnlvSl5RbYM3nmuOuQ6EHJQ38Rf1_XeaKxP_tQW8WEr3-ie2J3jD-1mdOQtlPrR9hb6F655MWXc-W-1DoQCGYIjgmX7uS60CMHibC-Q93-IHnAdljaJvn2vNOIToH_gKBx97uaXGrJHp9AFeFkH6P-YwTOcFypmcGcWWaml0Gw19NUEm7-W7qkk47D802aLN-B5daaCLvD2Pw-9RCYuoDy0nGPdhYpSmMHxiOS3to9eC3oyQRRcR9QyKNLHoDkMYZ2e53HmHLwl44288CGHUqhvGMfbzI9LDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیگو دالوت در حمایت از رونالدو: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94812" target="_blank">📅 03:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n62tgVPJM_6IVy9I-Kzn3ChA1tdDXp6Kg15GnL8pcAzJ-o-lGQ5NHbuWKt2Aev38l9DMCDtk-Il1rSFgz03ywSLQk0Kh218OGMFDO-4kjWBNJqbplx5aQdhxvw6gaXlbLHhrTeAMjGM8XHi05Agef7sCXnUe7rv0GajOPK0QRSIAX6BK3NXWBqWfVUr-hHQZEP-rpst4brwyudOcnVY2pYRTS7WAML1ct4aY5LSvUOuWh7DHpsb0PO_U1DqlXOJBUdsPcz9P16mGpDF_nWPWqJEsCVrSAoVXLtstyKr0mjVxOINH8TKaQcO5hGqaj5uRXx9jX4a4lczhx_8kG4jIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رفیقتون بازم اومده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94811" target="_blank">📅 03:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOikkW3E5Mau0Lw3L8RbS8DtCrZj_D0yTbO23ltTTbdrz1DbAdfRxcsb7GrVkBtpr3AsxrgT4kedIfGiF-ksz5PJCaiy6m3j1c5v7t6RaKJjo9ub1tGj7QVeL3zNsnriTGFei31AnB25NShDeBeEBpznqpRzezRFM6I1-Ps6DHrrDT_K19mk2cwV-IMxlZWXftOU9xsHlPVyA0cI3dM9PjMDlQqTKyg6eYvoyKGI3-6Ne5D36yJ7VdFPvfKoKYWnLxoTWSE3gxvL3YufrHAWg83-5IdzR9OTmCKrESqmPVhn9d81TnaKfSMQLqITvXDiMKRgDoZgGwmK1LonSxKYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94810" target="_blank">📅 03:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOM6gywXtEQhMS6bLZyb5Qa8knE2Z3aqHFq4VzJ-wwc0MSU-Ad1FKsMZ7i4emGeVBrWMEc-DvIcMWCYNriK1iLZQG9j48nUw9hRRhcea9LZA5dshza_fVogHGRxXqV04ilSBZBAhhKBmoH9yyWhEDdhU96QId1PW5ZM_vWmqzdd8LYuNtQG-Xl2L6Zhg9S4YCoVAq2izT93_ST8n2dNC6_nYSu0WH38eQmTElbmRg1KXdLzISrCwB5Az1fAEwt4dXtf2McB28hFYtd-DZ3K4UUFExUzK7bc_Q6vGSB_M6KUDGrL4nYYJmK0QQ-KJY7EUeG_buJDGu01jAPHdNm3TLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اردوی پاور لیفتینگ بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94809" target="_blank">📅 02:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=TFCprHTc_tyBm3OcOC4H8mE6Bwjh9sYbK0-v1aWMrIFwfBsNZIIhX_dNglvHnIXKA8l2HsbLfuKN9aleXPdbQP_qYEkBmDs3vgMqNbpBRb2fWZgsfeYzfvJ2w7B-jiScKjkGLdv3gSwQNJ1N7bv72mHecsAA6FPkiDgULS14mSgSRimB550kf9IaoRX3eKJ8PbbwurXKu4lYLo2SWstet5BeFmwhRBNiMiEI7d7QxL9m2j0nB7mu58ImmpmpVQjY0RaN9E6fxTLyc_au_gx7mGfuTA1MRazpHIzUEMRot_C0O4Lbkn4QvZlrQIxSlrdHoGjVthNqSBnCf5Zd64Uo6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=TFCprHTc_tyBm3OcOC4H8mE6Bwjh9sYbK0-v1aWMrIFwfBsNZIIhX_dNglvHnIXKA8l2HsbLfuKN9aleXPdbQP_qYEkBmDs3vgMqNbpBRb2fWZgsfeYzfvJ2w7B-jiScKjkGLdv3gSwQNJ1N7bv72mHecsAA6FPkiDgULS14mSgSRimB550kf9IaoRX3eKJ8PbbwurXKu4lYLo2SWstet5BeFmwhRBNiMiEI7d7QxL9m2j0nB7mu58ImmpmpVQjY0RaN9E6fxTLyc_au_gx7mGfuTA1MRazpHIzUEMRot_C0O4Lbkn4QvZlrQIxSlrdHoGjVthNqSBnCf5Zd64Uo6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت تمرینات و سطح تفکر اعضای کره‌جوبی و ترکیه در جام‌جهانی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94808" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGkOEfnRA9U-IPDH-8bRmigVDmS_jvl5F4sCbZ6CUJOhf8arKkQJp7r-C_Lyyi-TOI7ai2KYlr9ahLhdEXng9vbFbreWCvbWJHEXQvTlWLbreIaIRBhp1n0iVnJ0i0mFPtnrz_Q0d269u4qTloGjoYQ0PD9xKxvd--WAex5GwiRPm8CCa5JGScz-nNc0X_2H0N5vTzhQTkoachn6GqdPlDyWnXYkD_ADl4NNzavVLuV_TXrdxPWflFHxxgQKpx5DWVFMrQ4omKQDepWU4BWvKQ__fhddambZYojritZcmKBVvC9mJPJZPZBJ9j6ROIPy_2DnKKvRGC_qLHZUNSrf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 2 دوره اخیر جام جهانی هیچ بازیکنی به اندازه دومفریز پاس‌گل نداده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94807" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94806" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyWkSYLnwOf1HXG3dZ84XqR_yq81cnt4kAbhIfgRM_Ik19UralGqt2AJ7vd-09J8FjE-s_qOBwvf6oZ7HhJ1nModpohAXvlK6ZLIHdFw-ZyTz5oncHTPIDsc_LrZ2J0aGqQP_7MBuOKn9DzyoKejLguPrCCtwqGCvWW_yUbpml-zrFK5z49b6b7kpMDkZbm_I8z51A6Hyf7vCSVQTHZ8oO6pXPCxydtGH3g7Iak0PV6YH2S5Om4hCMsuCLZudF-G8-wutJLQHyPxLS3IjhsRUjv2CPg4_vhThOV_KMMBtcrl8GHos2w0ufF_HwOMc90xunbpZ8KGT3j9FOlY8RI6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94805" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94803">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TVbzM5Y71wU8tNwUTdjnPKP7JIR5glwGk2BNy6hrAFZphAxLvZ5e8B5ZrTR0hsjTlVa4GCe3ge_6b34Ov_UTOcXCpJCxUpFpGMAfPiU0fdtOzKan7me5mOrLm7ANGJHEpls5vi2w37xCwRpAFNU2x-edzAM59i3SvwdezLl7hV0-GwwncLb9FhbrJaMwy68UDrxDWkaoBEdkuPwZhPjx0AsCD8_CbjUdkHhKD6zeb32aXLQZP5NA6tcghVoXp06_YdeXc8-e3ETXaW4eArs_ia5DruciPuUh02Ktk8zfDNdr2sRoipXHxUweVoc1NMJLyh85R96TTh75QtHtrRqIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0PnJDHGWw7Wl6FFbtT_7CHSbmMbcUxsYztiMh62lJL9_wM922bJOvjwcH4yQZyEU9SDdFrO_U2SusYtGnUnthhwwrfH8HYhpQbGmgOx7n5AMhMeXfbt2h5QFkyrB_9UqhV5dsYuncvkTaSFt4hf9n8OyQUdhomCJXMN8ya5krJW8KVadUN_TDTuvw7_LjXz_LqQgsT-o5_jFAhwLQ1grYONO-TDB-e9DxlzrFWRaMSpBGGHtawJX2anGCqBhDNG3bvu1EONN5eJhj5Hs4Pg9PgNFGzGSUHl-0SHJtiipW-Dos_SwO_HrdHFQ51Iy98NkD92JTVNtYqfDTiip0ELsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇼
🇪🇨
ترکیب کوراسائو و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94803" target="_blank">📅 02:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94802">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ناگلزمن: به نظر می‌رسد اشلوتربرگ از رباط زانو آسیب دیده است. اوضاع خوب به نظر نمیرسد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94802" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94801">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFiMZUZjD5IOEsNEKNhfVJDZNzjjdUlpCDsLG8Z5T3h-VblGtJCgndn13JyUxeBDOpqgl_5WIRKB63GcOzGU-CHqRbcJb7apRzi1Qkpfgxc1gbTle9hIEKm2OuFJzXnBMujZ645wZcMGobNBfMFDK0RuOJ79aiZizPv8W5fH0VFD_zQ5yB70M5vugs8ot3TGrchJaMbPTOWuhpNHJp361zBk42YTV64vvBcUQ_vg-HMEV0_NAKnbGXk6tda2vDT7nF0oyw24A7KyGdHhTW44AmRiDJGaN_Q1_2y9XfNqQy3Bih81_Ni-D4iWYIF4ypP4igkxzaC6cjnrI5DnESD-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار پس از جام جهانی 2006 دو بازی اول خود در جام جهانی را برد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94801" target="_blank">📅 01:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7FmlKwyjgitIYM1qlNxVajmumvnX8GWoIEtUgTIaok5d6xkIdHGSA1nvS8M9Z-TpDoH21DpDrZPMMgHS6Yx54tQt_SOJEpYwJOhzc_daHFhf3jxbU3SnauzkRD9Pr1CxS7_j-AXPI46Lh2CKYDXkyjOdSl4W-NcrtWc6rkXrWdxSCSFkrRyD8fk95dHt84GF63_AHkL22J1Wz52nbYxgFJ0d4MqH0ELeV_DpserX_-nT8IDteq0n-HOzHZNvuat3_DngaM0pidEoEadIC2LDDJSgS9YYoLJ-ZFRVg_Tg7Ne0nvTWa9cI3U-RIE385pcjhhw9y2uLt5iCAAKj0dX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94800" target="_blank">📅 01:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRqgPGzv9gkKlYfuBRxaEBudlYKa5xziShy0tibbzJ0c7VZxW5sFGJGS8AEBDyUkF8kVjrlViQOKxkmtJdvL5o1rykUb_GEm6m9ata6a7DDWx4q1a-GmrRhUiIYmLW5Zf_BqNxS8xPlBfg59n8_ywr8d-wYUEPhlUKf6lzL2u9mV3AzPzIxrsB4eP1h4B12S5x1ghWoAp2LnLorGPG6dql1EToxYdTeZS3Y2ePNN4t3isj9AhL3vecnbEGJfNsG4XAXbDPNgXZ_aptv4GfCqcLmvUfUKAefOCdUFpLwdB8_UbzmyRg0yQZnQb6hrQGG8Dw2rELP6KqCZwt3thO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آلمان به عنوان سومین تیم به دور حذفی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94799" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-bCWQLtxNyfwEYMSn0LWliR8XAXSzvfiN0o5p9k-VocRTaQxdePQu6-VzQBSk9_WTEvgJi0iMoji9faX06nvfc51zL7Nhr-zn7y8P3-rQt8xxZ-iL5PKgkW662vw2U7GDaYclzPdZp4Lh6MOrfmv8XQ0t41IhPOLwvcfdSU-3kRfB78MeAzjSRv2uK7blTqxEN-7I6-qQhiuA6UHNqN2q_iJLo-gqwnSUOW2ECXRhwfr5p8QkZgN6EOp2W3e36ifj7WsKJPPHOUhfkDbhoBfdXiscaHuxRrc_ul8CO4A4PjIpciK4KKZm0cLfX2TkX34CrOPKUgQIyFqS6DTxhFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک شاگردان ناگلزمن تکمیل شد
🇩🇪
آلمان 2 -
🇨🇮
ساحل عاج 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94798" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زندگی سخت شده بچه ها   میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه  میبندم روی برد برزیل مقابل مراکش میرینه  میبندم روی برد پرتگال نوس و رونالدو میرینن توش  میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94797" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=neiBBA7A8phmsCS3XjS-ppg6fdXRuEWrHlVJ11M9qAaxJHBBRoJWk-GO0rw_qi5H2Xw35lGpcWThh3KU8Aq6SwmxmTxIAsWnE554G-of4CcHBnKbOaOCC6HGVmlscW0lMYDupoc06fn3NniKJlKY3lLtA24fhoYUG5LJS3UtIwHi3tvOvjKtFZ2tyrIhH33hWqe3UngHMPYM4PgbHafI8msnL6ssYTxXNI2tHwkH4r8Lnk74C9C2CaFZTI81BM4UGTJA9BHOBOYQaOcAMgfrt0wAfUlqZuvqTwpXiyahaNScI3jh7ApWcQJSsR5DgrcAOrGd_Bqlx8XunZt0QTV3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=neiBBA7A8phmsCS3XjS-ppg6fdXRuEWrHlVJ11M9qAaxJHBBRoJWk-GO0rw_qi5H2Xw35lGpcWThh3KU8Aq6SwmxmTxIAsWnE554G-of4CcHBnKbOaOCC6HGVmlscW0lMYDupoc06fn3NniKJlKY3lLtA24fhoYUG5LJS3UtIwHi3tvOvjKtFZ2tyrIhH33hWqe3UngHMPYM4PgbHafI8msnL6ssYTxXNI2tHwkH4r8Lnk74C9C2CaFZTI81BM4UGTJA9BHOBOYQaOcAMgfrt0wAfUlqZuvqTwpXiyahaNScI3jh7ApWcQJSsR5DgrcAOrGd_Bqlx8XunZt0QTV3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94796" target="_blank">📅 01:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چه دقیقه‌ ای</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94795" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آلمان دومی رو زددددد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94794" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94793" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آلمان چه توپی رو از دست داد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94792" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این وسط هم آلمریا تیم
رونالدو
به مالاگا باخت و مالاگا موفق شد  بعد ۸سال به لالیگا برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/94791" target="_blank">📅 01:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d006b86423.mp4?token=BRnC666mNEkdPgOYbEyKvPDVqoyFl9ne3iNbYez7AQXHC32B-WgTYfj6oFkg093YmhJyIjUf6-meoWoshsdQlSzVnwtIop2fNB-Uec3rabUhRkv9f-gNZ5DLevkGIuLAidHsB5eLghWDkmfgmyoeBl4aOXjf6cMu93F-cCflra7BrQzSHHRc5_UumefEIAMcUxzmfw9C8CazJ5_StMx4S4gMpnl_Qs2gQfv80iH3HM4uXSGFu5s1frXqHyyq02SiEF4yDra7Pz91NOWwqVnQ4LdESp7bnZofY9XYplxAR5rdJ145fv3cAOiuKzB968fUnU8UGaIOiVPSt56UPm59rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d006b86423.mp4?token=BRnC666mNEkdPgOYbEyKvPDVqoyFl9ne3iNbYez7AQXHC32B-WgTYfj6oFkg093YmhJyIjUf6-meoWoshsdQlSzVnwtIop2fNB-Uec3rabUhRkv9f-gNZ5DLevkGIuLAidHsB5eLghWDkmfgmyoeBl4aOXjf6cMu93F-cCflra7BrQzSHHRc5_UumefEIAMcUxzmfw9C8CazJ5_StMx4S4gMpnl_Qs2gQfv80iH3HM4uXSGFu5s1frXqHyyq02SiEF4yDra7Pz91NOWwqVnQ4LdESp7bnZofY9XYplxAR5rdJ145fv3cAOiuKzB968fUnU8UGaIOiVPSt56UPm59rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/94790" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلمان گل مساویو زد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94789" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94788" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4c0CmwjbLGDgCixUHywnhwl6eq52Zcw29RbtZhSXTHQ0kd3WmX4sxHE0J8c9wiC6n8GVVFPI5ro1_dWwnM3as-7SVkvoopqLuvoCrIcSH9M3wC3E1HM7R8BGR5ldw6zaGK5imFwOW9l08OF-E4NtszjMLoeXkwfdOum5xbrtQ6Z3TVAaIr9Z6eTuqNgUgd7BViwamhhx3wD5YUG2aIb5CUUtTvmN72lipehJc9mSriZGoXIteSp8NkIIiUPzAH0IEJoYYZIDOM8cwKl2TMDEDzAuZ6Hi5M9rM3noWNdSonjC50yh7BTuSZmOia-m8HYAL5-BIleBvL6PRQvbZKKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلژیک بترس که اعضای تیم ملی آنالیزت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94787" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زندگی سخت شده بچه ها
میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه
میبندم روی برد برزیل مقابل مراکش میرینه
میبندم روی برد پرتگال نوس و رونالدو میرینن توش
میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94786" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJVzuKZIQb0arGeTIhSEGUUGlt2D7dHkQZCy6i_FlM6-xWfyI54PFpMN10hvu_UYOdsiVv_Nuqzjf6KknWoI3JY1VZs7ppkgjoaKaa1uHaCbpZS5K2SswlKSKHHmCTH0RGNfLJ5dhMqnGdyQ7D5aWUGFsStqBranZeS7f0-fBtOb0DSZ92sXU9Ok0V6ym7lMTP82y5tYqYRPTsDFPmy9s0I_kjgUH5RpEybreWqz0QU2Rsqob8Qo4zOnhyGOivDqxK2fE3pCKSLJlnyVjXy_OhA_55qebSkMBNMilsI2zNQVwdycPjrwNpB1sTz_3wZf4VbXJTByW_sk6p5o63HqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف شایعات ساعت ارزشمند ژنرال رو ندزدیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/94785" target="_blank">📅 00:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
👀
💥
با توجه به نتایج فعلی، شاهد تقابل آلمان و فرانسه در دور یک‌شانزدهم نهایی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94784" target="_blank">📅 00:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اشلوتربرگ مدافع آلمان تعویض شده</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94783" target="_blank">📅 00:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/94782" target="_blank">📅 00:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvgDahAw1rKE1klNMq-6ZetORc3-EUInedoemGl7Il14lQ-VvvrnuIgOaBEXXAAilSH5vnlDV5aHyxvBZXDRBhNCC-uGo3cae7ml_Bvo3ogwx_PXThQoizbfuEGSKusFm50qunCgd4KL8lBXTpaDTQv_K5OxwAYPCUKG2Kttpnuf4OsaiPBC6gO9HO-6CVexlFETlny6bB7CIiIKQT_NHgR-ua-5cYB2jxF5nDgwmbC3fZdZBEIOvME55MeDSYAxwjfdUBcfboAhR_7BdqmfBw3ChQ7ggdzuM7GqzRsUu_bDDHZSiQUoaVOnDXJm_DmTVYDP81wVFdPXuzK5VFlu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇫🇷
🇮🇶
#فوووووری
؛ هواشناسی آمریکا به فیفا اطلاع داده که بدلیل شرایط نامناسب جوی باید دیدار دوشنبه عراق و فرانسه لغو شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/94781" target="_blank">📅 00:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94780">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYcm8Lle4g_ri4lI9tKUN_LhiHzTdB4OJZUjbJlWel_ykgzYFZjletuWuEf9364RQxBAr1ayZC-_9f_cifR1RtU-nRY5sgdCRYK_FZVxb4TgiHU6haz5dbKVMADFqp0iPDQeOLBdnSBEYxRGI6Xt-8avNJXQMrZArrvboqXwDbEEr3S6wk2K3oLAUzjA7RNOM13717LsLJZhy8zh80xso8V5TIsxjnUvBUlEW802TnerV7JPPYp_KBYqnLRU6swHOiTT5XOfyBhh-toRrU-qKWda6MEuvf1NxunuFE1OTVLbOiCIHDMpVk_FgzxocL1joSas1rjA6_WdzX8pcq9BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مانوئل نویر تو 8 بازی آلمان تو جام‌جهانی کلین شیت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/94780" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94779">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پایان نیمه اول
🇩🇪
آلمان 0 -
🇨🇮
ساحل عاج 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/94779" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94778">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آلمان گل زد بازم خطا اعلام شد</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94778" target="_blank">📅 00:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94777">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ساحل عاج به آلمان توسط فرانک کسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/94777" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94776">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ساحل عاج گل زدددد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94776" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94775">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94775" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgwdUXZaRBiUxKYpM62cNLWeONVqdycVoDK_LCoVye8RzYQSCEZ8ZJXWk1vhnfhuW4903EE3LcsDxEb-2MeztU-rjT0nN4g_1K78gB8n5kyY1haqKlFV_0_oEZx3ySeMO24taLdm7YiAeUjVwPz_zFdA5LWPzxM89fWMw4_YGwZY_gzxCj7MTBtgPTaRwWFEb3pMqikzLDcgWpXqjdSbtU8X4eNITC9Hs9Z06TaXOtTirX_SexRefgTuTZPUqMviJwWjRBYNnWZqTTtkiLzJuaWD9M9LdqqBOmUGNMGHLlemZ4kDwZFOiSD0JVGhiAYTR4DJMylvomyQ8C9NjgUxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/94774" target="_blank">📅 23:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/94772" target="_blank">📅 23:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94771" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگگلگاگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/94770" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نزدیک بود موسیالا بزنه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/94769" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد  به سرعت آنتن رو ازش گرفتن  صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/94768" target="_blank">📅 23:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94767">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشببب</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/94767" target="_blank">📅 23:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94766">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9ZSd_qBbiVek8Z4N37JX6GZbUoNvnMuFNs1D8GqRDbVKct6HEqhOJ67VhTMHxLDG03EfBRChGdpIe9dwcCO80EZlNyDxjiPvd6r9i9OdjJ_JZ4GLb7AizWYOXV1J2gdojAMjIcN0iLqjZUtevj9-7OEl5ZtNRrDxt53J9o3s6o8ZwW3O8esbz3hR_Kb2mNPstsAwG3sjWNxkzi2TOr9YMZJIz-3w6jrhlXmbgYaAzeAj-HpmFWuWJ7nlzrXv8oDprVsZ3EYGrEoqoYL7k55s9tkN2_kGUYE0g60rBnpm-QxS_R2L5tCCsXidIvvnLAXDStYrqKFqR7zZCldKhZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
تا این لحظه ۱۰۱ گل در جام جهانی ۲۰۲۶ به ثمر رسیده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/94766" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94765">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH77s31UmZ7mi4HPAneOfBSuNzgQs8tTOTym4EU1m_HnyRIC8cmJuscyKON56sz8D-4-W0z0_FRb7E4hwCqeGZUAr6T6BOPIuGkWt9tSGW7tjht99DosBHQxMf4KhUPEEG2TxPQ4M1Uryt5nNSXo5Ujq9gUrufFMAu-XpjCnYLrelWLkFwIPg3WOfkcCBxlqyQpV4zMdvxbnQb7uEaPxWzlagirHxs1JR1ZG7sKHBaD-aq35MZs3lePF36fUFVNgH66aHSdwJ9wGVncBsg6t9LoQunHBj3mLgyiyCZXf_0PHhobQR1OuE6HTV29_uWy5YEylLMVF-rmFTZF6m_rGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94765" target="_blank">📅 23:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94764">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAZeGBkRNSIDtB27mpasjU3SC7-RZR14SZhF-pH2XEJgMTYygJOHJM0EPzV34GB4eDsVAfH8Ek0TeZImnnY473irY0C17aXae_VCXUjtUkNB_c5XW5hjuADWV2cGiJPGLEP_Su9ZNBDMeyXLEjPR56sAOpbaTNV2nuhnz8eIG_TxiLt19m-iICCPP4O3WEI-ulirg6SVXNHrqJ415-AqA7UAi5ocizrUxDQljBmkpRo3KxTYII15WGKGitPgStDP81dtKk4r-BDalyFvMo15ZIA_N4OQYNRGueU-xwNLwDv0K3vx9bToDb90gEDk_z1-ABlcd9bxzm8MzBWwZNO1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین مشارکت در گل‌های جام جهانی 2026 تا اینجای مسابقات:
🥶
4 مشارکت گل —
🇸🇪
الکساندر ایساک
⚽️
3 مشارکت گل —
🇦🇷
لیونل مسی
⚽️
3 مشارکت گل —
🇨🇦
جاناتان دیوید
⚽️
3 مشارکت گل —
🇩🇪
اونداف
⚽️
3 مشارکت گل —
🇧🇷
وینیسیوس جونیور
⚽️
3 مشارکت گل —
🇳🇱
کودی خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94764" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله تند اسطوره فوتبال هلند به رونالدو: او فقط برای نشان دادن خودش عطش دارد و همین موضوع بازی تیم پرتغال را خراب کرده است/ در دو سال گذشته، پرتغال بدون رونالدو بهتر بازی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94763" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6zN-HVrXMvNhwDEKqJvwWLphNoxFKgI8plexOwhdjjgxWw1AAZjTkJiBLzf8nztdyulgEGvT03tUFJ0EtEbLFn2pc19X5d_21kXyrzYSKINkLnfxmvEya-SLhxB_OFcgtphDJiZmFVXXiS7uae3fnr4H40w2B1C_bW0y9vbhYCDZ-WlIhSLGitfDFrN2wAn3re1ythDOfUFGsuV1-6lXm2tZWvi3WV8GuJXS62De3EpcIWQhyt2cjT97VkMCHrwSsjRFft9sDaKPGWfiX-YbwrmIV4j3Ta9NL_SYkTc8aUkjo8kdQ6x1aZfWKgV8eEtVp8Y_fcq0T0hikMVPS3Mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانوئل نویر با پشت سر گذاشتن هوگو لوریس به دروازه بانی با بیشترین حضور در تاریخ جام جهانی تبدیل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94762" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94760">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7d1NqAIYlHLHyrE4CdhYsr1RV_Zee0xdH91VyiB4KBMqIWBDQRFc6H_auSS_RLnmCzhZkt1EtdOrKn0ugKQ0SvdWxWg-BMhQ7yeKZASZf5hpGoOxmf7nbi3h4q1l-4kEPK0vSwG_kbtoPgZrfSiMROztmF67WbQCG9L81ADC2_NK-RMwXtkfSxyw9cYqK2lKQeN3rls26LoekJ6Kx3u3Q-pwGBPzuvpY3ojJHADzj3-Z0rPt8NMnyKyAKXWlRMy-TkiK5TChRZaVfFC5jFlVbmWatVLUY_e1JEJEtV3d4oAGTqrbyrdTqEGKPlUyIAPGUBSfQ8MXlQkpJuohEIhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0iwzXYI_DqDSm7ihVL0l3YmdLIbsszCaxPOxaE-zyXSNbvNO87U2aB_tJS88-ze5qKFSlWhBEGR0bkqT_IVutXxD2sCo91OOTZ4HsO27vjwGgA4i-uBEmKWAproq-OxGpk0R8FN0r1h61QHCizi8mXIIYrHqEUggyLuJRilJGDbpVp5wpI3LtV9fTVG8SRqVvy-hTqA0dwSdsBqdO81pljzPCCwHbnJfz6QlCwV-1GzO9Jepspump9Q5RCBSarF8fyggZ6knI382fMWjD9DAz-enZHoRcRIAPYhPEenU9o75WDOhEshppFPgrD2in7KNP3XwOeLqxJiDdUw5-wE-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇳🇱
کودی خاکپو با گل دومش مقابل سوئد، از آریان روبن عبور کرد و حالا تعداد گل‌های بیشتری نسبت به اسطوره هلند در تورنمنت‌های بزرگ ملی به نام خودش ثبت کرده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94760" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94759">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spzpX3CBFSr258iP5JcBlNHtwOz7Irq_Jl1oQw0Ittyx2_qDPfOMEtmkAzb_CPoZm-OLSxYMmvOHoYt7KqXC0IgYuy6tE2y9DmFpyM0Flt8mnDDUxN5oJYZmL1g7sGjBkJYewJJ-rDd6jsdAYtn8k7Glpfbm819LgXcbcwtgx81cnVowgH0K4k0Lq-5DbGJCDVtnIaVo1_0RBWy0TTyRJyE6S7x9R773L2rQgzoWMs8-3XBOEtiYq44-VmFkMpP_mRlmPiMl8YdH9lA85dafCaOtxKkRQxuC1JNanAsZ7iwcTKINC1q-tkNz72pYlFAxBRbjVnXcEHTJxISN-2AI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر دی یونگ با پسرش تو تماشاچیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94759" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94758">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAJXDcGXcGb8fyGp0q2CuIbtSLpdq2nTgAjqp1tbLmuB8KFAoOFWJxBqVwxkNfMXnZ4bmnJAOXR226LGttw_x3EkahJI2O54hOHedb_0tt2q5dsmSmHXmivJeQmKOYm9_f9Vdy-DJsRsYUbns3-earLwDr0_f_wqko88yzSQCktod8OXuQ7bRn03Fi79HDIKDbtTGXWUV9YYUtjt4oFNl5s9CCrcmqZmlisu4fNV1lbe9XPvuR1JS2PZ_d2l9zK3UMpOJdu1Wde8sLS23o3AyjsU-690pVmMfRg91klUxVHnxzErdp_kfqf0obvyCUsAKA-ZbAdv1TlauEpxwBWPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
با یه عکس فوتبال رو نشون بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94758" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94757">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد
به سرعت آنتن رو ازش گرفتن
صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم
مدیر کل شبکه خبر هم مجبور به استعفا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94757" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94756">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLX03-eD1gJw5Gs8daAC9DPALIPPv3D2x0dsLFNXonoCBi91vLgxxTLbkipOAPlqV8LEYRKnxMw3gYuryDaDEIeNNEYLLiYZ0YQEpg8ax84lDo5yiWUAN6H1eCol0N5nyOnv5sM-gPdSok_6_GMbQJ4F-qg0N2TsqwbScNfVRTJ3tAV7HIWJEAf3e6lsXsgrpC-Be48Gpmui-Gsr3V1FiIdE0Mt7PZGPBq-cXe2FfpYHBgt5OZRtTQ1aFaMmwgGLDPHRlAuGWpZJdwfYOcUO6SyGUVJlp_cQzTTozR4D2G-N6VKzyI6VwwyorGE3wp7TqGYOG4dfBJ5MrwmeK3GJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94756" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94755">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است/ اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94755" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94754">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akq5T12SVHxHSbJSnjIcmVqJV6SlNVFVSHeW6EknyV2km3h3kVdN1jFrIXQFQjJTEZ4Os12OLSxxfPOYF9AzMkK6ATlWM_eHyrE4EnXzYhSW2uI2WL6cn1ro-ZELUhZ5rXCmQs8ogYjJdjRk0MdBLMWHoXSHTwQypL_cSweRb84q9DHKTcA0yVUfL3dPgkXCSOldOOEQSWjaCgewNCdlYcoN5S6yOiXouwul5mlcHHJZkiyS1Ocvsc6myhm8Si8ncj1RqO7Lz181TfSlyyygYZSMR2pB29Aoa9s82RzD-F2e63btVp3H-7FXCSgbb0ZRCsD5BbU8wA5RrM3vZbRQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش قدرت هلند؛ سوئد قربانی شب درخشان نارنجی‌ها.
🇳🇱
هلند
😄
-
😃
سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94754" target="_blank">📅 22:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94753">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل پنجم هلند به سوئد توسط سامروویل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94753" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94752">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلللللللللللل پنجمیییی هلند</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94752" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhFUOb87k-KN2PYsEOjPNHRE4Qr9plzvZDERMisW__H8tIBazq3hQylmjPqu0aYQnYHUwvJd9ThPvpfibsgZ1We5KxaHI0pLIvNdP-nfFi0WGzGYO9HmIFXZqRWUu62aEjF8F9-hS-xgQltOMmLeWIaaRu5kxhN7bgf0hOr9aZKBeKFCplB9pVdC_HWoB2CoZwHq0dMA5qJK2e9JL--LspxxMjikYq1zlZ2aEmbUASG-nHIdTY9r7h6hoccFlM_nJPftEiBJr1Z6DOfeT03xhJKfnKoQMFjMhHWvj3kYb7DB9eK11v6uxS_LRbU5-KHpsGBnq4cgTDJODYKeovvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHToEGBS-fExwp3oBEO552RqZTwIysFjcIEKJwxCc28FK6yi5SHfG4s_G_dqrOq2QxHXFZ-8UmLaZOn-1bf6Mhu3djU-1EK--MeRI21hBYsRGKZm9s6iPfis02zCLLpplFyX9-4hG9gthId2EtJTDnW19AlLNX_MSmQX6RebHlF-ZGP7H4CVeT1O6B3v2fjzAWJAq6EQzCzajnKhYULghkqrvTZ5xRzI2I5bKQCgaM67kE6sXMApwmPZROkENH75ry55mEp7-HWzqJMmPN0nQq1ULkZR6FbWq9laSZQw4LIISEjWOEXp24HGjW5521sofoauMJORgUhDcQ70Y4rTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇩🇪
ترکیب آلمان و ساحل عاج، ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94750" target="_blank">📅 22:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAxi3LGazbi5DbSqjLuzThDgpMl6Ps9VvVkr34Zc2CJ-fleuw4QJhiJ9U0RQ6WShfn4hp0tydzMdS7LH5-Ca3Vi9w808gqhuaWTvoiGERC_wq8ATKw_wbFj-BIFx6q6peTp4Tvm5NvKznpTorKQRGrKtyGs_H86Fa2Mh5LwQ5Koqr05apYr5Svwo2MhDIOdK6aip6g-fVaXT9i8fljtDwIRhS2oKLH9hQqYgVf9pZjBo5-rQX4CMZIfx1R2VO-8jAt84N8sOZwO2bnm28V2xtc4bEMlP_Oram4A7fMZOYZUIaR1aWpa2PRy5ZxclCwFKoFuCExPeUbGwaivtz-GpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح تونل ویکی فن دوین توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94749" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این دخترای سوئدی چقدر خوشگلن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94748" target="_blank">📅 22:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چه لایی خوشگلی انداخت الانگا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94747" target="_blank">📅 21:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇪
گل اول سوئد به هلند توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94746" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
