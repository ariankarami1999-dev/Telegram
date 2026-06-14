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
<img src="https://cdn4.telesco.pe/file/fiUtkfufKVOKcdNwJMsdSaiB0cUDSvUdrM8aoWmrB03xOR3HJXFTHCOQfR570KL518j_ZiB6T7GtfHZuv_3aAwgkhIFvYqgyvsFHtYBFv3fvTwUWzfaUZUrxFwXWWeSsB4AQX0lUSTzrlX-e3D8_itnokSjTa4rRvzBSMoaySVbNS7A3bwMw_VsR7PrEuKT9rCoi1A-4p3pbf40I3ws_0kKlkA4As4vZLJckj_uHus7ws09HKu1yzS8SSSwlSxg8scS6CH_sE-g7yJ4g8oynmHZzDDaQadj6_H1sfXGdRNPxEHc_5MArJP1Byojiuw-K_P6b_GF0eYzPXS1ixz61zw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXwyrn-AUJk17LQq6YBCQq2ruKu3uZ9rnoBt8Dh9Hl5ycNkiF_F15dTh1l1m2Q1TKV5lcuiYG56NfT1Oh88PiV29o43hYLmlN26hKAPErUVt-nwxmFv4WQCu0K4OdNWmWhPiMMLU-vY8kG4Kr0L1uxG3vqCytiIYnDW_yuCHP0x2I-IeI2cR6XA3ZaXki6e-btT-mdFbTex4IwG6xTKL4_neLFioL8pG4C0RacAQi947CEhwnSASJsKQsBM1Xy-F_iFfe-TPjA5s_DUWDqym9gToGDM3vR1f6ociFjQlJJhzPZTY1QIKe2S-zyqxujWtM30b-TVat9Db74M2NH1MFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 525 · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSu3vycLg3c0o8X2OVBFT34x7a7125nRgBXEcKfRB9Jtxkg_WtFshnUIuzseZ_D_TOjthO4ldOiaN_FmzQa7Rjrw3H7Qppkz9uxcXc-zw5nt3VkVNZui-R-5rNrZUCkWCYeYRNjjz1n09VOES0AeuiGN-RPkNDSn-fTd1S6oRQyGHsNRVh62hFArkbxufG9QMug4H_p9rAWv5Zd40NEtOcc5wioQPTevYBpnxpVW_Aav1AA3a4o8ao6LgJwBtNqDTNvsW7mlNyZzeqezdfrKUsFCSPPQAKkFUWE6BhFmn85_IMDe1mfgd47FmXtjXesiClqpvK0DQxw9ys7ZKJsW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=W0lpeZ6jbgdfe5hUyzHZCBWUsyLSz44FcVoIfpd6BX3UbbENb94V6mM8aNDEcaZcaVtt3pKD3U57lvdhEMMT8nlJIxPgWVpHvPLKibmmiEi9Iai1jo9i_urmbuT8uUiQpC2xTSp2AMnMgurhcK1iCHFejtZgnP6rvYuL48hkUbnX2HjHZYZNjo0CGs57JgemiaDHLjzT9-9FM5ZA3yvCEc_wqXOSz2smrmbEDKL7XarFKwyLUGBg-7a6aAlh-G_3W1DO4BmT1_5xZxi5f0Yl_gCGdGqb5_HZWpzHo18mzEMGZxcRVo1g5YlNYyvcQ8ZzMeKkcktnFmJhWZbL8tNWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muEb5WNQMEUCLdOW7Pq6uPnA2JV50wsmGQ7USqGHr8Nemr0qDxkOHFR_UR17YmYEv92UmgumbeOIkjTnxZsvZ4WNjqIbyMYRc_57ZFws_Msp3zKoE0WmTvLp1up2IWhAEZtODchzLBbxIsh7bq3AilVeDcgWUHfsh_cAaPnDQjfI9d7Tkkl_kr5ApgcSds8749mbfeUTO6D9I5zOdYpnOogjtWNsPRKUwEdZOUFAT7-n3mArim9hisbuSJXG2Mp_gPUNnzlkCS-IAcJ_dkSN6GCJnKPrOg_yojYOMBQ4wCfRtCN9U5NSQ75_-NRk5JkfIVOpWWrmoUxdCYBHbujpbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OjnTjKCPNr_ZDFlEaAzAcoHXuarndP-Uk5hU1hdJ94szFF4jSecqczRwKlQVxsYZjVC51vxpKBdiSVhzFzARV_Odpg9N9IHGzxOsLN2alDzeli_aUIc7hsgaHpIVq6IK66Poy8LqNGp0Sg-G_z6JtFGFTLnXMvOQfdR4nXtaAAsjrA3UkQ_MAztwgaLiU5Qz5I6UIOsie3UQ3N6LljjVhzPXzh4S99UDmFTVIYvaXQWp77Do5i7DaLdo1w6lzSw3AHOSuMsfJ6jRbmfN3KCGOZgeXmHhhN9y_HTw6hk_HQVf2IGG_jwWWkFp29ogJ8rPl9CF-PIjJsLEhlQOXqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZKC20AqQrs4QEOcU0HmDtJfCQLnxsT7WmBQuCRjJM68t6TAHiGnR_obi-VqtDtsRyXfrrOT_ELQxKtBBCcSOvUiEam2YOvGQjcQTBKTk6Phi3qkN047mjmq-7z0JKZkeOeUktatdvWEAMNTE-aVXVcy_wytd92SXtGI2jIF3JDApH-SjAC21TpmxkEzc_m_jyKTTmI4aJVpM4EzbcC41FBJ744J4u5AJ4FrVie_QHLt6Ka54ZqYxXIA5DIEQIDsWALYGXlPwwCA5botPPPKQnF9Xe-eM-Wkzb6J3-YTQyR79YNLeJIVFhEXKMMCPKcPp_d6NbxJ1mJA12gdO4TxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-DWhHBMynzlMn5RF2jkTu_VPlGyVFxnwsf8elUaahpUXVpna7gXfVQb74QjjxxYNLDCJ5bIgb_tHAkBNkaHN4csIX1zqf7neVVGd8aMe_BaDlHMLkU_F-QcMUggaLQqciEcD8kzoy-cHgJx5h-JvvgqXtDLTG5gMIhk4qU_AS6wU--toWeGed2IEGjRr5vAsNukZkeO-1HbkgvidEpkJZshBa_eDj0Iu2ipIkbqttVA1RwZ0rVu1ntq1L4i1nQbiFWR_t_tLdnMYZu4K67Q1TH6iGzqprDeNsCmzfTnR4-Pg2_3av2SecjKLCPKY6nuXz6z6j9UUXxoSikzzedVpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMrTP2qEkxdzuTGsNkAiDXQ-sDvF_Ybrp9yclRccN10aG7HH74A-krCnHSqwQ9RiqUd-gMHaTX5U3Jaf2VgpKvgLokHfoYdJoDlS9YKgYEaEOlQNlw4me0I9Lk3IY3ylMQ3XooxGWFV2rnU7vuInZ5ObiKsS5t39FKsZUucyGJEPPWmh9B7LgnmpJ9hHpVcEsSAxhYsDJ7VkNZK46INMb62QF0Hot4aqsOxH87VxthxqerkM1g8t4DQoRbGj-nWf8gmpdvS_luGEe7O__CSjzj8LwYxKCaXXh-vIU2B93lwfi3zvJrw_W330-d-ugfoPc79iDPQqUc5MMXRWfuu-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9XH3Y1aapypLTyNRPTet_YFzo7zqgWDKWfQb32AFPzjRaNChpiH2T6tOtV8EnTQaqKXL5N80I4FXg0t7LgP1SmDPrfo4U1Lf-bbTcuvURwKQMKOATlDm34cNmentOT11WCPhoy3xVZ8Xiw5LgVpbfBybJq12kAij1jMelf-akBQ8HzmuP785rczSGYFoc8X4CjKkZjVFJsqOdCfl3rI4gZ3ktcmy2G_SipXuXm1__yeSglPEilK2XibBdRq8HkpYrUn75Xt5Oj40oRxNX9Mbprd58hNecclFUkbCMtMSrer54aQvAkWxm-zkUWYA88XsMHaDZxGIEWMZkesZ-LHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtnc0v7z6KQCPpolQlOqXYuH6fH3eilu6w2-3qhfR5jrOL9fP3A4TntROoXPBKJEwa1vvaG8Rz0h5AniiM8c_8mGEgKnejhFpv6hfi7C5QxuMlAt63aGJCplXRRxOYfyzFFN5K6Z2LZ3g3bQhW5xEOlSVBYPO6S1fIWCSsPen91IMNxYYDvTM3Osvk_eHFKFWLMn4MNrOwDur3pORoMH2IKgPUqtPhytJZGuk-11cJ4RIz8Nk22M-Gr5b-uKiuBHVwFSXQP_wrlPhMjZoPIUMTQnO-nH7Xp5tGGnWQOYC_WEo1cl4oPJ0-wTcrLbSidc9z7V7ZLLUYIifrb_rleRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJeSGPoOpGpiiyvamsfMXtoPwKm9_idHFdo9l2hreMTl6rjZZZvoJFQcRv9901ckc5TVvDtz40J8khA96fjk5DbfHnu5FxDwpOSB5Ahvr12rdTNSj4kGD07mcZ3ghJTnQHdNErnqHfnTcDuDhVBjqal4ZNQdywnvLn0A41rMjlv-MtD4b_gj6xGpQX58v-yxHXfO6dfsaffPMe_htsjsChc2y1CMp4uopdmAlEnThXBx77_D-3Ndj7ZgtUgPBnuZzSs2F5OKrw1PetDpcSltX1q6iKC62Qu6UXKLMzR9ujijKain5v7i5xtWvf4bim7jwsOkrr1dmHJxcw1lPI3oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml0DT7gxOFnSfKxi-G0HuGnmTQq8rOqDwq_RSqCsY4JcW_-7XtOUTYWFlMHvd1-VBl4fUJS6BIdpAM7bQd2l2d754zvV2-rRFrL6E9n2Od3u_9io0bhKFL-xsbGlnKDKZmmoqVRUiyFq53kzjqToahAxLkuDL868BwHEVm6Kj-JwrkHXPMnYy5q5IC5cxkhYdfoFoBLrzB9uvunxatVurkvJGIINWDTSOv1wcYBQF5g3u3jQyHoSLcBMIkhBPKNPeV6yO3VxINCV2-6ZNLwI9LHnICkmdsX4U0EesiPqRHMf4c8A4Et8XummI0MDXFGQ-TAJoQksga3KL3_4Z_6vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LkFGJREW8x4uAu3toQ600jBRLMO99F6wUZ74Vu93-UaNHp0tkL9fINsnoB3ugWQAE1KfcTVGCvdXJB0IC-HFawxEgHy3dZZADkFkb8fzqLFgb0D04ifxCmiPZZ88ZInXSqy_1CzF_X__f0GLMJz5Z1juRoZ4l34WsLRTCxx1yjCbE1cKTVyYYgqsqv-jQG0W1qcyVaIwUWlvS7FBIlZn9tV4TkR4TcKKCwYS6UbmQdOyaektO4xIKRPTtJ8_EO4Op3-jGKMIz9GZqM0GW85AcYkiyuAufAqWNAFLRuKGgGehSxyeRABTQGqr04MPbb4QfTvNfklDlAoYyktYqI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMOnd4SugvkC2gL8IE--0u3DVOpjNyHVfVfhBopyYLdSUYRY9ZIM9h3c8NiPkNrkMR6bMay1yT_lsnDyhreh9gXpYzom_dwH_WHlE3aRsnN-v5f8rQERBc_kzOH-GZCHKq_1Elq1mmfB0a9hchAxJUN7DQBRSjzLEbPMMEwoNx6xAAbKdRTE2nXyxgiAF3GyhBpVEe6ngImhOLNLdeEkI5pB-hE7u_m1wTiUX8hnMDlSCblw8ULjJPGpkud0E-VWdCsEx2KdLR3u8Xfa6zPYcJTiwtRX0PuIaIEEjFtG68HfVTkS73pDgLDaL-HUOFZ-iVjaYcmvTxJDdNRIcKky3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz0VEGNcWvXoqNKjY8dw4LPQ4aGcOCXg3q4AeAoGpLoOeKOn-XzfWNwIhFITG7kxPUIBSAPsgv9m6QkLb_uI3End7Lf5Ge78uK2SCN7yV92CLheReNhbqUfesI7Ypba22SjL07UrtOST0KCN2dYYahYl6UYecahA5lxGewfOEikvBQwYMynRdr9IBvpiLN-p3YHPqrY2YmlcP5fez7tXFvhPiaYLx9prU87SoKY-J-SJLB_U3mBvsg7RpCNyXIpAro9hNHCN2QmaxcziUHXiirmqbQawy0mdBWmsiCn5qtM3rf5mT3fMWaA9HQB3AWTuuA4auAvvRuCC8ZBucNYOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=UD0GR2W2eTWh2hLvI3R0U_QiE03z29yPqHVrpFoMC5TL177uKT4P9viNWQpk3RyrkzP8PdPfgBwG-IpUO-mL_hLTr2OIvQK1H-E33IiENsHgYdLIiN_l7suxnunSfJmjJI_AK_8P31DTAJUVSSgA9xAC53D8dKKHpYL_3_AFP9V0MIPo28lwYyYv4H_tW3tmy0mIejEgDk1Dt_2LKmCP1L4qy528lw0Oqm661KJsSjAtLlnLFINnljP0tCQ7m4cMGIPxvvLNRitX9-hV1YKE4xbgY3JyrzsPhjkpOWb_XnLMz2izGcdccOMg8rnNUc7Za02zgpVRIpmpMClqaJ8jlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=UD0GR2W2eTWh2hLvI3R0U_QiE03z29yPqHVrpFoMC5TL177uKT4P9viNWQpk3RyrkzP8PdPfgBwG-IpUO-mL_hLTr2OIvQK1H-E33IiENsHgYdLIiN_l7suxnunSfJmjJI_AK_8P31DTAJUVSSgA9xAC53D8dKKHpYL_3_AFP9V0MIPo28lwYyYv4H_tW3tmy0mIejEgDk1Dt_2LKmCP1L4qy528lw0Oqm661KJsSjAtLlnLFINnljP0tCQ7m4cMGIPxvvLNRitX9-hV1YKE4xbgY3JyrzsPhjkpOWb_XnLMz2izGcdccOMg8rnNUc7Za02zgpVRIpmpMClqaJ8jlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Imlzg5S5VfNaU7tl5NIsSv1sihz1mn_c4sBcd_vZTGq3vLQxID021baVEKa9DX9YklvB3TC7FoxDO_QnGJhMP8YH_tFtI1FiTW94SzImzEPQJWPXKwUh22wN50YbdKfmKLL5iTSzBrUaaUSgj_2SehLi5E5MOtOTu7Sm-fEaoorY9zbkOfU3qluuNZpUtQVI79Cv3UmfeE2vYo6U9Vq_P8xgofzJRGhHX_1VDttk3MVDxLUC7o1UOrp_7DkW7dbsRmyklFH_fvlwgtS_M_fZKO3Ncm-B1zm46lsg18-B4CsGhyJqVULOvegglzGbdOXxxPhqLMXjCK0Pb5Prq5cwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=Imlzg5S5VfNaU7tl5NIsSv1sihz1mn_c4sBcd_vZTGq3vLQxID021baVEKa9DX9YklvB3TC7FoxDO_QnGJhMP8YH_tFtI1FiTW94SzImzEPQJWPXKwUh22wN50YbdKfmKLL5iTSzBrUaaUSgj_2SehLi5E5MOtOTu7Sm-fEaoorY9zbkOfU3qluuNZpUtQVI79Cv3UmfeE2vYo6U9Vq_P8xgofzJRGhHX_1VDttk3MVDxLUC7o1UOrp_7DkW7dbsRmyklFH_fvlwgtS_M_fZKO3Ncm-B1zm46lsg18-B4CsGhyJqVULOvegglzGbdOXxxPhqLMXjCK0Pb5Prq5cwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=QExytK9FBU4ufaqdLlInsCIh_JQ9ny2Rh5apm0W_aY_6LojYU_PVmwnSeU-2DAHQMibqIhnirQLHlExRJaR868RjSgMVlsljlS7BIJl3MMYxJ0mS_C-M4AlbSFh1xYQwpImr_OcEHopgHUHr1iS5IMk2UPNLS83SlUNFTTZr5bh14gjKGoRIIgAFeVPemtcG-8ss1Gk9HkogQZ6jHnFusutZPTB2fVsKl2qOg1T5vIWvXUhtw0Y83XLKD5AR5dZSbX7Rw9EvzE7SepmBgrwSYGVa0VGGDmgMut5VWDqiDKgS2y_4yxLxjjwRVMoBDFfWf5ga-H6K9hhr6drEnVznMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=QExytK9FBU4ufaqdLlInsCIh_JQ9ny2Rh5apm0W_aY_6LojYU_PVmwnSeU-2DAHQMibqIhnirQLHlExRJaR868RjSgMVlsljlS7BIJl3MMYxJ0mS_C-M4AlbSFh1xYQwpImr_OcEHopgHUHr1iS5IMk2UPNLS83SlUNFTTZr5bh14gjKGoRIIgAFeVPemtcG-8ss1Gk9HkogQZ6jHnFusutZPTB2fVsKl2qOg1T5vIWvXUhtw0Y83XLKD5AR5dZSbX7Rw9EvzE7SepmBgrwSYGVa0VGGDmgMut5VWDqiDKgS2y_4yxLxjjwRVMoBDFfWf5ga-H6K9hhr6drEnVznMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxq309aMuOLWMD95A9TOIz1rRkao1NjVekudV-KoxWnrxgU1EaVofrLZEarmuEbLXjodVeTi1EHQ9e5JUP4a8UkLBrFevz4Lnf-MgnhpmgZqlelt34z2zBiEmGIeZyEQscz73ymzifcOKfe1WNv7FNFcTEADawUd3CLFdNvL0pPbAOQggnbbOaZgJXJnQE9Pjn3WGoNiS3ylIkteEIJQqzy4iBxzJouBFSoJmnIEPm3Hh71CGQkX6y5Vlj8Deg8G66eaurCR8pgvGP6DQvfOA4H1DEGOD_jBjbaVDGX5kaswNvqxOGCVgV3AiSG0Z94I8ryzVvqAOgyVabXJVN8TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJs2ry16czj4C1eY8EWPWgVqV8_bNjhDlMRWBbxyWSQ7h_qC9QPvj-jgpcdULO4B2h_OQpjmnx4NFj_O3VZtGX2OjEW7f_6t6YV9eXHuCBmVRH4NsL9PMSnVfTLhuOOLnxFZuzgQ9zJqdF6M36hAAkdRzSbgL6GUDR-F2sMAy-LxsvFCaHHYNqY2g9DqoqHx7Bimd1jpnScmTrbvSVSoPkEr7nlg0vx2GEFgobcYv0B8ekHpujpx1aUZEQ9WR75t5kYfBXFSAbHF1kC6kheTU7efrvdsoKrzCYHu7oVq6tQn8zJhuZ5TJ0qOYO5DrDr2-pYioKOyIiLD9zXet16L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCtN0zFcqxTVPmTH4N2X9ZZQhCDrEZyB2mUfJhP-H0vn6ZuF3OG4-uaB3LPg9pOBh26P1ebj9UwCwFWMFPpQuPry4KPd40Ln9xOWLYPrn57SfwhM3jIraL6jGNLS414_q_p-4kVRPjdFPVnAqn05dYKE6XGnt_kU4kLXCAEOdjEV0LzA1fWdKdN4r-JqwJAVYtCeus8LiTQyUa8pWu2agnzoP7gtwnJOjU9DfluGWTtDz9j2yvyIN-yZrVwW3sMd_AlAYNdeezg1GyrWUBpcHIy0MFzxuj5oY4_-IoefYjD9vsQRdo77sj1Jsn2rHQAD17C_QDzb_tHiiHoOWa9XXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZnSUQmTUjhprAPCDKsMKXYpbNwiM-kXRqpsCctDpzlrZv45gQ678fOUQuZQsT3w2xdsgRQ-hE7UU79Dmoa2oPb9LYeaZ9VWed67gi9H0q4PANEcGqP3D8I7VNDPultbuEz9LCR__38m0HpMJpmdemxwAHlVDMP_QRQBoRZl_80sFxh2Wcj-4MTvmSGqMc8mkoaWuhrVG1-E5TMr2rzHfwLGC4mI9sgIlsflRcv5IObtORyi5K3WttIlzCdcROx_n1chLaJqTk06RZXWBZjRWnhBN6dD3CuZqz6kVzPQrPbZvYoSlfOy-P1ZASWze6bLpKg8O8_uPbvxwyyEJmDkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbSkPERTq8G_NF2C1C4sKNupvkqBkY0_-ddbCVSyWU2kKGuiXaQkS0vTj1_g-kXdFgDTJYfkwBib8WsE4xmNoVfLa-TP6pTPUnbUOrDtnqwjIqezyZJ4gBUvEXft-fJzaELCif_13AKM1EKwMOOFiuTK85CRur_Nw4zMEV8S_vnOExICRfJCVq7KfhlMYKSCSoCvqpRUTIUxForN7A4lI-WaUpNBFlJkeoflDWTQ6LGDeHuN4HC8IewqCr-VD0zShAhF4AXQHd7cRDFz6Lv_q8t-rNcGnwqBfdP_WpLvs5Zb0UI2l1mgDHBbrPH_ngYvuUIeHqzBXOwQRfMSWhXkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epwRutKht6PqvajsJiGHQOCBJVjXDdmpX1A5uhAAlAHCuh_BB170QMtlSTMYKFlY2EEaeit5mROh3jeQTemtJUDDl9THsZe16mQXtXkQJ4NcptIea6Ja5sSFLjNrfJYE_w6iZ0yU0Cqwqixgj2qly9heM0oV8kYHCp441tp8aq8qqm_-p36g3gqptZWu6P9dd5_19iQQYL489wCcu6ii3egpW5R5HU7bEAdUPdZ2HtB52IasGi68Wign3H_kFD1WJgaD7CqoX01RuQlI6XKJ2JMAOBrggdwGxbwmm78mrwxmkT3aLjHSXZUWjsMqUi3x2MU5G_vyQ3crtcjddkmphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdYOYHIXY7CI_HmzjWE2AdZdjSAaZt7ussAkMcCl1m5fiijMc1enYuVElZTpgsaQXwWMKuVVuWPmQiCPZSmC28le-diCF6emF9aVVueuvQ9D5fd4Y-nxL14w4YlGeQRm1HR8VYFHqg-qUSvWaa4j4pyBz09zp-2LIwfZnS1r-bU4lr4fpE9bGaRxeJ6KcUWzDYC1rGQgSwAMV7Kg7CMDMLhzOAANs7h31sYDI06OI1ykVbs6821OfYhpNfY8oEVow0Kxn3-OOfn2-vTYGw3hH-T_I49Lb7naqnBPhXAJxlqDMFJcmtT9KX_sTqJdPnm0U0FAPsOE9rE_LgZHABzTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBOOrTDw_IP2kroRnh_OwEfdBjbIEK140I-5HLQ5VX9gVDyVO7r4hkDF-QlkPdLQm7qQlJzE_pmONmvCUztHV82buzfSqDWjs22LkQTNaNHmOBX4HcjA4qQo2Ec7tPwtP50GJbDRokCB-eqf_f_SB69VTED31NQAkk5Q0QrRpWdcYZd7QkN3cdp--3LGsNPW5I6QQ8GQrTD7DvH-8c_08VkMeU2b4fzl2VHCY14W0sNoqr_Acqn6NWyugwvp5BabtUqt1ialHodQV9bzFI0N6u-9oGoPphykg29jE2d7CqseU_EKUmMpLqlZq-grP7_mDW15HUIUvSEgQRWbJpCAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQVyjUMbnxqRQlHQ7C8Rnhx5LGnW2Iju5neE06gD5Xap74I4X5ankchzk2zsKO4NfrtiSOpSB4TqmHK5bPSedQTzgty-rZ3WrVWdbCO-XSCWnsuEjRG9vT01Qt5wu9rYJoWSK3vIcvUIXyXLZRlrZ9XhzIyImfewyKaHWBQ3g_DWGeSO5EPG4Zi7xT8OA53js3MSl5tak4uRG7Pfg6A3mtqGC9SZrfIrrTeYBo5777S3ddfc2eOULc5dGGMmWfqzUYQZw0h_iQjtkVxXZMAA5K8apmwqLr88a9lkFnOHmNsAW91KFau2sH9W6LFXBZybL2d4kRujyfp1qnZADnoN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqQgRTjqqXBwPWYOrHgfV5G3HGQw1hhmxxGKZivmuhOEvNidiBIofaNXkEMeHLTorxVFsyz_l8XMMGw2UUmQoGyd-9FzCoblWsl3qiqQVwNNvcGkaVh0G9TREZl4FAGhJQTGusK-Q7CH0NltPbgz7xY-2TT3KuxKXAUy9HYelPF4FIzxz6FVfSaOP-z8OCN8BR075dGJwV5nZ8lvj6m0kBEe3gXT4qX0PRd1k3ixfd46DvOK4r6PszMdoW38L7cd76HARfgCZ3b8IAlNIyGMubCME0Op5egZ8yoA1ZN-1JcIFfg-0LFz4TSesSKXTh5xKeP4riQuuj3ObWEH5_ZQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Drake
📌
Ice Man
📌
Habibti
📌
Made Of Honour
📌
$
ome $exy $ongs 4 U
📌
For All The Dogs Scary Hours Edition
📌
For All The Dogs
📌
Her Loss
📌
Honestly Nevermind
📌
Certified Lover Boy
📌
Dark Lane Demo Tapes
📌
Care Package
📌
Scorpion
📌
More Life
📌
Views
📌
What A Time To Be Alive
📌
If You’re Reading This It’s Too Late
📌
Nothing Was The Same
📌
Nothing Was The Same (Deluxe)
📌
Take Care (Deluxe)
📌
Thank Me Later
📌
So Far Gone
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJluTBQ6V_9foGPLU9hhhj7E1RhjP4q0dxJleZ9FLuVub9VbVHNK3ii9jfQeQsBY7lahCWsyd73mtB7owYynz9dTqEusz4c71MGlu4nhwxO93hlfyGQkyJYMHjl1e7F0xAaLneutlmopk4OZsDXMNlu_IOPvpR_WNsBxIVlco99s-P_gpCefFQ1ZGZr6YQOufMTe1qT1N3jYHTOHZTkuyP1U9bV02N7MngD3Rzq1oVbNUODNqZaLpGE6UjFrMHS0QmI2DVcdM7EBP2y03-PYcCZJWcdLaH64oxItTDesGycNY3CTA0hgkKmAVKISr6wubcN6TBuLJ0go54nx18DKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MacIjePN6J-6TpX5wWmwSg2BfyXPpAPhnJXHox6VFhHIydZDmBkdE75oBEduqaqMhsCbDN8n56xwj-c0e3BmHoHJXEKpsjR-cgcZNyXqrLCruKmKx25shQxusMU72zxohZbNMq5QhgjF5xg4AqeOrd1O7jkQwmeFV4vC9SwdpSC05OyW3QagChhe_TEEv3B--2eKUia8sE0Z7oHGszoflPjdP9-ZUzMcxCwmOcy1FLAhg30TL6o2hTRMDJKUQoLYzsenHGFA-uDCOyzferrmHDY_J16Tx9fZm_UQtJ-uBR71XXQjcs5keFrWLiQ74Hc-O4f9SWPFFh7TykAaXB3tDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abFNWvsBRePLPdSTFzJZqnaMjH5sKjzmg_afi2e-RdbVdJjr5ClIhFVXRC9KT9XQztA7Ulvk3SN0AsbEjazSek_4y9QXd_e6N4f_fnTcO0q0TLVLNVYSycARuUfp-5EWEmX74sEgqjXkDj_XO7Gm0Iiu0hcjrQLOOJaM2qJkiZdrv3nrQzIY6RI-dqgmY9tPXwkdMU1bPt9RbijEHHd1CArfB1P3VWJtGI75TIRADFAUXjC5YBQhIRNaNObk8ytKRry9AurqDVVzmIU1Z13SrCEGAB_P5rnGgwpAHpAo64XhMOLEcUfEgG9N1BycbPvQie3Jxtc5ihOO4WbvMfgwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-UFWnyv3zrHERBn9ZbJ93sMMzUNN5NdxWpaZA1KWwropjPpgGwF2GmleeWkbPBFQNCySohe86yNHLTUfI0PIuf6AocufnStcrC3LHOoqB1B9Sw6uC9qZNPi-Ziu3R5Tn7uqw6gyV8tqqoJH-rICd-2bOnrpvyKitjrmqvL-SjbxOWEHo4DviQSByHCj_7GpyroKYt5kCdmnXv2XmEXBk3_VgHvsaSP9o9IcwiYMD4_MNAvNdtfR8zfUwWgsNSECZAqUR2WuFRsl6b17bLYAQeZMJfPJsIvlZaTxwRhkAaZxjbhO8jU76RGN57XjzfOhwKTmrD6BKpOO44qM1ry29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=d_3G2jgmcN7dxD_Qwbm_dm7frMlDA3zLd-4WWprnxoCkduqAg1E7EuoglBkhDd56HkuhqtNqOG5qqxhBeg5Qp_JkrfK-AAbmJ88W7cbjhJXCsSDEZ7tDaE-5mj8P5l4u8egAlKa3Vr3F1IDj7PnUdcaY7awo18ampjNS1w8vKcYK4t6Q5FPMR_APVTixkkto1hF4VUMWfV-hEcruqqbfcZJoruaO8mruOCnuNTvYlOFPTmBfT-2r2meBaq79YC09QJufEMHBWDPuxhAX6Z7XtkzSwoHz6-RkSqJnbz3SHrQSlv95yg6MucEDbN7E56ti61aUvVUoGoLKlc1KN0BmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=d_3G2jgmcN7dxD_Qwbm_dm7frMlDA3zLd-4WWprnxoCkduqAg1E7EuoglBkhDd56HkuhqtNqOG5qqxhBeg5Qp_JkrfK-AAbmJ88W7cbjhJXCsSDEZ7tDaE-5mj8P5l4u8egAlKa3Vr3F1IDj7PnUdcaY7awo18ampjNS1w8vKcYK4t6Q5FPMR_APVTixkkto1hF4VUMWfV-hEcruqqbfcZJoruaO8mruOCnuNTvYlOFPTmBfT-2r2meBaq79YC09QJufEMHBWDPuxhAX6Z7XtkzSwoHz6-RkSqJnbz3SHrQSlv95yg6MucEDbN7E56ti61aUvVUoGoLKlc1KN0BmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNiob3vvbWmQNrRHaeenac-l7V_WMxY9GV1kZXiYNk1s0M_cTDfbn5drDZ3VSQVppTIwYZJdNws9nhjbaJeyrrT0fpvRXACCDrZkdky2poMh1pIkcAaaaiNWOcRStFyFkgrD25Mz2PqAZbAN7XknIPqkBjohozODhVxDIEHe0T3c-VCW9Pbkvr2blWxHmewTl2mfBE_wiqXSo7W6grmWById6I3zOLn6y6Pu-PH4SQKqQG2FMKoNji5DU0ITpzodQw8-bfO-b9R51-ios7mzGYNV95u-ixyOcttySKqf4jRkb-_5OHV1SVQAsLpHRXBBkgg9W3SiKtnRa2VVp1D2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyyzoWIio8Lc0V5VizvdcZLWWjvz6fbdwFn8HVL5mf7NsHN7eG7_kqcFdwfZJTIBxhwvwIfNUBJHW5Kd-AM7uvB-ZpOrZS0n3hNaF07mIQ7_i9HFOEMEFVR0Rrul4zPh8fkzYuGjIISk_CyC6K6nzju6DFQWuj9QNQiyv2jrGzKi6fD7H51Lba2xlbViL3U6KYKTiu2EWm0xh9A5NdzO6bxlJ9d5a8R1FBTjn9ICnY-S2X8lBE_GHnZmMNDtT4JICwFVLBlk7sAbzJ9T_JF08AeG5_kJqIXnjJkKnQtAz1FTRCwOcA-FR-XHolhpX86zX0DvVr1ggsq5aTuPHtYNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO5dapp5UON_FtSJ5MzIsAN1XCOBTsxTuM4k5zELvo7lWIK1mDhgNb_o7EaCRgFnu26jzPat1CkKxjYZl0gMPQxH7ns_inHIh_JoGpyZF612n9_p_WQaoF6QsY0fz-X4bfgzFIVD9IrsSDjXzRm8Fwd1mHIoSIbrlkLONHKeCCWQ70zpOs7g1UrktfgQyfprZKB6avA1qcpAmjEQOKriozwpbmls38Pu0mj6jqaWpTcEXuu6pcjQh4aoZQcslRGso8Eyjg-s4UHq4R9dsEZLeoo2RVh9JhhMrkYdy2OpJBrHraPycVXxKe7HEXUVUoLMEPiGNODYQ0O9xxMUpL02mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCEge3IWGJY1VkpA89appvIWT_zwrjy3QZo1iAFlcx9-BAXL3suhusf8Swf1-3YsDHrkE6LLoFklNegdqqT2UjzBFzCxGE8cQ6h0pNKTlWT2DkaQ3Q0pHA8M4CkNxXWSyUG-J0q1q5HBZOtryfq57g0ZxCJN0u6pD5gtPKagPP9qKnuWyNxSFzZ2DVP6FU_crRzEi9jvRlHsZFbyY1s-fHjMK8OMJkfTSJ353ci3-0x4hY0rmwMa_-W8l1CAoehgJIo16QxP7mqLsO3eSHaw3eS1VteT3WUJF5YLOge8R2a2oQhDyHI1ZwShA3CJMK6SqCXQ6Kqnq-kFK16f9Ajh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDg2VjiAgnIXSZV_MIljwbJPJohQNTV32zJpKfUHonW3G7_QSkuclECUEN12ee6Zz6gB7BmF3Ze4RJAkuGqSmyK1dcG5w48aRX7aXXkyeQJgKxGfxn3JaI8LS25NmgahbR52Z0ezYXiBLYQwpoOIbUqOjY5XVoKNgtnIn9PEKkr_CEe2ceGeRRufMlPeBrjat3AEqvPxCxuWpWEczt-w-nKYiCb-UZCWfQsbCaL7VSVBlwVF_vFKRr-h-HG-C4gIUgtx0TiNbP58y7LRePw2GhOsvbBBOZgoXhBu8eTb0feV9aOTnDJ57elEn5Gi455j7gl1mOophodTy3o_nj-aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_oUJ-sc0KCa8ND5DWsK8uguoFMce1xUPkIX5pTzDvnr0kIHwzzK1SG0t8rzgueXnR3ytRAO2x9eAj82dRjM7GwPmFQVEgFCLzslXaFPOITGPi1fFAraIPboBT1Dbph8zsBMR-xvus6GZWVL0ZLGSbybGU4iQqvowPttumFmtmBvoyck6DgbT7QLpVSDurJTlsRbQkB0D0qHgQqZeCZqgLmhRSv8qHwxI2WX7aKesl1VsQ7MtROPTMlNLj7AAitdwLpLKoqnea_aj2kPkQ2xeZ1k9gMOC8FVtt_Z8U7p_UkTNxV7lDaOBJIbL5XzS62ZL52hRS6SlMivaH0AKBpPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVZwM5D4bdtgz4ssxqrknL149oyZvp0TNrHhFzYT5qkfJfby23j4VTm9zUPpPd8_z27mJIINRelVpVwLT6AiJStaMNVg9bCnKtnuZkI8SEafV3DkMQC75MfLXuQr0Zl78AFvzUMpEYAK6GL75AN1WFsbMuDSspTve-ixp9SzK-QKgLtYQkEAWVckBV8FpBSsdzseQ12b352ptCay9LPnWByaa5YdKnZqHh7xk3zph-oId6Xgg_IPkL6rtTE8pdUT-hp6ROrfShe7W8RkZheOKjlb5Iqj8PdSJR1LpoufTZh2Z1EmUKQ7gz-tqsMUh1c-xPPqL-Wx-RVPO22GmjD0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fusDz0UWhT41C_3elwRzEFDZuFMqic3rLS1I_tV1VPP2mZStcJnIfk5pVE1Sr4KTgVQGTQ4dfHCcNVQaAEw2Dvvv96nWEbWuKKqzWhaZxa4SZhDIUo3zpOUT1Hv-7kBu3idCArS8V9D3PgjH1qKL5toXg3mIs0lr30KvI5sc6TMiYLM5feVOy5_4he15NKlDWfZxnZUDG63iU2weKrOAFwDRFyq69SS-3N5fIxVv96KhCSt3qq69lw-b_-phs4YEH3rUys33-JHOeKikNteIXWBOHQgObUXKQ8c8xev--SPKvcQsoL3DDLcolmQ4kWPZf06YTLYHkA1zcpRvMbOUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
