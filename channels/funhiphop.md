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
<img src="https://cdn4.telesco.pe/file/NCpguSLUrZnZg9KR1pqg7bTN9QTlBwtXtrr7ymrnvDI7NyxcPiyqorqxCxH1CGoLDTBZI_5pTV9_28DZOLD6IhSNVJiWpgqc9xdSqRmSBaI-UrwXyO60d0scnLXeS7uIAAFnk9aho3TJeYXdgFxB2zFORXP4NS-eRFuUi6KXs0JMtFiwEz5fD9QuO6nn3dynE-qWiZjP3V7NT2h0nIm5PEozOIJxEVUdkaTU8qc44PJbkpUrgIgQo9vE040FmD-4FYPBTajAvCoZKA3XWif_tuuAbNylQJZEpID6bwEPCLoHKFnfjKi8mVmWwBCeUSF4jof9_6-jL55Lq_APclE3cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 261K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvnJ7o5WT5H9g4kuQkaWbQMGY9nWYMdE2mwQQcaG01Euo34wm_D2T9hwVkB_f-_4G-570S1oO5YbWAxFY9Yvr1JCR7CxAW2JqFHvXXSZj1KNbHmiTb6bwKCWmL5yc6GXe7alhugB1l8A0oMupdQhcLE-8mOM7LyYCyiqCepXN0nvVeMO9LYSCOp6Ddw_3XAMaVhEUtY6K_oRgnUySWc-8eGbC01U-5Fiia7Pr2GQNv_s5nq-ZsJztmUtfT_IOMaM0IMBzGj-W0xbpQMmZgmsI67wBQYlwIUrb4Jgc-kaxm3P8ItjrixQt21ogsXEiMF0CxDbsPZTmEAmcskDy5zzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP9mlR_xKVhfa691qxaoyEl3oPvAhVnUQMu0QofVq-2Nx4i6wJzc26U6G559n9ENIsjL6wmHgr7Zchv_Ryt-tb4ZKW9yzJ2kxMIf7KpreSRBDicQOIHytjD2chXmLCjBymqiS8Svxcj04bM5HfSm7ufeme65qT9IUco3ou2lAzBKcUMfakaVMpBwSFCudo33s1iqZm0mKZxjnIhhY6lmCXIytDwd19HGGIKah6QmIuCt5l2qdKQ8Y3PXz1CoKuS3UI5lkFcQdHYtyYjoZKAxEfpgGh6cVzSsWWmfGjtBv-Wzyuf0nLzTdae6Idgk1CjCS7DPn1_c4es0zbQ0zNhdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4ohiEYknZslU9HmdY6-AtBpLpu0jAOi46EKTCpzgAbfJCoIuj31sH81RB25hA4UUwk6-gv3-q1E97lW-U8aqwEUJdrrHcFFipoetvvMMjqM3BRmLY9k9lvl3T2e3cdP35WaUq1adsec6pKAuIpV4u-RIZTapSFdWGliy4EWs830cmw9H0IyZsNdbtsdeMNcYusS801bZzQGFv9et58elEktu_kU3Y54QBdSdloaGF9aXJlqlUnvOPNJfEcvWP4yngts2D2aBazlbwBppINPIsgrHwscOtTKTMt5Hr1fQi8KOIayljMKclZgK09gjOyGThPoj_oVpVwNdafWNFynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هرچقدرم از خطرناک بودن طاعون تو اینستا کصشر تفت بدید من یکی این سری ماسک نمیزنم، کیرم تو این دنیاتون</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84488" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2951b20357.mp4?token=SFYJSsNAX8dPhK0jtageIDYIB-jZL-3uGQH59BfJ5SThaeHVY7hkthHuHqnAGJlCvcR_6cMjJ6PHCmeh7yHqyK6um-Pbfb6HqopHN4th79i71zZuqR9687tfLsQra5YlmdRKa7biW8e2MKH0pUbK4fCr2q6DLnmph1zb5ByFRVVUH70jTJBw-6Dk7DYg6_yx1HnUQCJkko7MAXIdCxqQnyDh3BNyIDCeX9_m8JbUvdyICFB2GhzoCuW3Pcjn6zPM6NAIl9f1z3zAMR3GyFq5rnw41VXgKnsjwp06A-9aLifMlEvJytL7y6b8OCSL-RRMAKQPG6zySbxneIkQlYQ64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2951b20357.mp4?token=SFYJSsNAX8dPhK0jtageIDYIB-jZL-3uGQH59BfJ5SThaeHVY7hkthHuHqnAGJlCvcR_6cMjJ6PHCmeh7yHqyK6um-Pbfb6HqopHN4th79i71zZuqR9687tfLsQra5YlmdRKa7biW8e2MKH0pUbK4fCr2q6DLnmph1zb5ByFRVVUH70jTJBw-6Dk7DYg6_yx1HnUQCJkko7MAXIdCxqQnyDh3BNyIDCeX9_m8JbUvdyICFB2GhzoCuW3Pcjn6zPM6NAIl9f1z3zAMR3GyFq5rnw41VXgKnsjwp06A-9aLifMlEvJytL7y6b8OCSL-RRMAKQPG6zySbxneIkQlYQ64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو بخدا من نبودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84487" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84486" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbDmgLh97lWGlEdofTxF6ilXTI6mZvzuyjF9KE80fy5xHP53s0f536t7DI72SIibFH7opmMTPVOrtjkCWmrZjOmIzXuC-dxkzylmbGTOLagfINNVZ8cF4XDVD-vfU8p--8_Fj4X-8kIB-baJXtmuT0DP1JxwznWG2_KF1zoUp2o3AYjh4ScseFPmwItnsF3rAbXeWI91WOgToaRP86bk60JamfP5ekog73COzgyYBJ4sZfO6P8PwOEV5addYfQwf4cxH3WYI-x8GjVQasaA9HRjFfRNILUQMzR99zjfOtZHYPFfwkmL39XQa1N3RVorRgeAHne1Xrkvb8CoP1B5Zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
کرواسی - اسپانیا
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - سوئیس
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R14
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84485" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeJw-n-VPzEQ6F7TNvX6lVsphhDYBGjEeZRzlkQfkz6Fs87ObCsWv-H8i7vUfeikY02Zhu0UHR_w2PnDQxD0G-B1uehaKzfKkBkn_Ng159MqFb-3pd045iu2I18SLNGUBmwaRqRFNUS2a8Qtp3yixizPe-H3rGoi2u4aVWqkzadUncOA_f7eINlovlsixqGeUio3ieliTGbBSAPz2ClH4qKpJve2iERyeEXJgSNND7tGWczap0gGS_g7qZrva1YeGL_Z_99dMT-N5s9uYBywX0iAiroIQYzr3uZUFJ6MVEVMxLzP1sahOPg2UBggYFjqU2cRcFZu_kXJbDoDRnaNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4SbkL9FmyOdb2Z1Ftz9jPZEafyxmgvGE_0jZFaW9G2unaa8wyOS7y8VIRbXSH89W6HZSIIBcM8y9yejl_fzmbi4fLh6kt9zzpTr6-lCQEAnrLJ3IVTOh7rO16QCkFwamlyqIRGLKeJ4IIoKQnUG7MdIZ2rfgynP_3JVPwxwTUdUUCUpUib_xscpv64e36bZhdQIaYJue7Tbd21glZyXry0hmGb4GPE5oIqy8rY4G1YR0bvhldU-zTIvsAKqZZo19Ub09NqIKvWfV3yInsoivpetxIlXXnU4_06k6nccv3f2fsdb8uJWoPp-YQRXgomt6GBf9yCXzkupJ4YnnJEc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPlaZwQKplvkAnr4oXnOkh1JU2oojidhQXonwyqqr61vIj88F2DcfQq_Or2rXiUBOX_SCJidvQV_Fu2iWFo5jr3rgucMo-b4D7fdI86vJKOmtBI_-DI__7Un4gnBy-L4RgWowZEoHwzuaSYFZ-eBnxe_YoFCCHPsi5zH3JDFACvhndz9vsFk4eH3fLL2fqcXl6Z4tUkd5rlsOz68iTrl5ePkxTNnhZpYowajPK3RiUgsoSSufJsMN_uEgh9gHMBXi3dN0DTrUHuvsBKconwCu8g8DcWbG-a26TwiUGBxc2F1cEOub3HaV--cvH79327p4j6ouynKq67TF-lMseOX_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6pYsFLrHwBq6Xu7bpdSPdHMJMS5PfJLmBeh5dpH0NoC6UO3pQLM5o9z0WaGwpwrpWs3aEo8asryeyFujMmsW0w5KISHQmJWafQV1rYTuxbyqbEHIGL2_tHWlqS9Huwrx5VleoWeLBWQxPpTUpRM1kTOEWF9zddynhGaWFDHizTxUCMSFJbfW8FX-luJ6Xpe78yZKYjeUeHA9a4pMTtbhhwd11zaTbFWsfM6mke2WClPzYSEPOWg_uvhFj-CQ_ZW_L_kyBrI5wQ3O1Fu-Qztlh2PVPTom5rVzy2At2mllSBwxYlmjz5_orwQXggbH7_cbvgOPi1XT2_nXgF5k3r12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b249c59827.mp4?token=MfXMPfv-dEOrmDIWTL1iOspRuUj9EXO-gtP7_Uyk_ajJyQLFxF_WcKPorFr_nFVXGW9e6n7KSQGXVuVAswooD6X12Ov9Rr91k0pKx8aC0lr6bxmE5aMvUJpuINTkIXnDy3ibN7vYen8dbCZZoWm-DJZxVvnnXt4QbWERGeRHLNf2U_InUt6V9qfmBGwd4Y7xJR9F37VpisrFThPRTU8JR4YVenJeeW0UfAx639sjhgbzCbkQfR82QAXNbxYx24s2ZOzLLmR935nA_m43ak-7CpDyyW3dBXVZlcRLyfuLCEmwNmNJJGurgbmgAYGaC2wTxBD9ajehe_vCTPmZWiPU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b249c59827.mp4?token=MfXMPfv-dEOrmDIWTL1iOspRuUj9EXO-gtP7_Uyk_ajJyQLFxF_WcKPorFr_nFVXGW9e6n7KSQGXVuVAswooD6X12Ov9Rr91k0pKx8aC0lr6bxmE5aMvUJpuINTkIXnDy3ibN7vYen8dbCZZoWm-DJZxVvnnXt4QbWERGeRHLNf2U_InUt6V9qfmBGwd4Y7xJR9F37VpisrFThPRTU8JR4YVenJeeW0UfAx639sjhgbzCbkQfR82QAXNbxYx24s2ZOzLLmR935nA_m43ak-7CpDyyW3dBXVZlcRLyfuLCEmwNmNJJGurgbmgAYGaC2wTxBD9ajehe_vCTPmZWiPU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84471" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این لوکاکو چرا نمیمیره</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84470" target="_blank">📅 22:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=sQbeQyTKRPNIbco0CcHNb9FonD29JuFiY0Wa92FgMR0WPQpleWxA199al7qyDVaENLiWIJ26i9U65kwLlzV11fl-DzGo_FTKKAYlKI_2Td3JESFjmwdoDrBdBM19QmUXA0r9iZ3V_0cHwT0YLfg98_m84QBXM43kIh8QXxbQWrfkqKZLSPbo5WEqgeAbcJ8xb608XOk9LJRtkGonoJMUOU2L7NrQRhleNuOYSmaq5UeXsgVNYQMm8soX7MBgTwh-t2kwXiXWhW-A3du-MyZqw014vmQ0QUIv_xFNxiJRDcd7ZLO4h8rTllExW9zo9czIRvIC7BSP5O0P6K5USgHfag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=sQbeQyTKRPNIbco0CcHNb9FonD29JuFiY0Wa92FgMR0WPQpleWxA199al7qyDVaENLiWIJ26i9U65kwLlzV11fl-DzGo_FTKKAYlKI_2Td3JESFjmwdoDrBdBM19QmUXA0r9iZ3V_0cHwT0YLfg98_m84QBXM43kIh8QXxbQWrfkqKZLSPbo5WEqgeAbcJ8xb608XOk9LJRtkGonoJMUOU2L7NrQRhleNuOYSmaq5UeXsgVNYQMm8soX7MBgTwh-t2kwXiXWhW-A3du-MyZqw014vmQ0QUIv_xFNxiJRDcd7ZLO4h8rTllExW9zo9czIRvIC7BSP5O0P6K5USgHfag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84469" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خیلی دوس دارم بدونم اینایی که از رپ دنبال محتوا ان تو باشگاه چی گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84468" target="_blank">📅 21:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منو برگردونین به اونزمان که تنها دغدغمون این بود که حصین زد یا فدایی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84467" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">LCPV</div>
  <div class="tg-doc-extra">Creator (ft sahar)</div>
</div>
<a href="https://t.me/funhiphop/84466" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84466" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8eiY__tb4KfHpmDP6Vm8L36Lu4Pbvs5B-gIxjnTBDDA7C8Fw4TC37H4sdavTSAd6ktNUjA91Y8iBzsqKsTo05-xq1Gy9NetD6JndR977dRjQ854-y4Gc8K1sZiFyr1ER-xiPzFVg5TbGlMZ_N7gWAnEfZdQcnuIueWxciju-aKWXd1VJQ4bydO1-ew_7rOfbtwtZjui3CGw37RxRq5iyq3Z_9lvx0c_KHSTVa9iGuPmAzFXDyXU1OqEZTfzAh8jMkyo9fwnOUCbPT945FbP40pyYA1yF61s28VTKQRypAyzFLUQpJ9OV9jYcA0-e5mhoBtvOE24gC_H_cDuHO9syA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84465" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruZ1sHJlf8k8SyRHqLE0LM_vD7HynpcRUApKvOFqPhU6HAAcblB0AldHSu_bbq-biox3mFo6YfVOCZStkVXDCDHb3OKvcarWRVNKOgYLr29IiMO5TVxqTfxqZkZJM-7IqxQdTH_BlpyDQPQeoNxeh_IFlUbqTBz_mLRaOM21fmY-emC6BuKdmsa3ZDu31Lm-tBj304V5cxLYSiDK-v2zhl3njMzuyP6xHGyLhJWOX77rKUn9IBYyzjQ37oRtNLLjdwmiyzxIJKQq6nr6oTUJVtd5o-kgK3qiNSdUhqw6VRnjRWvV99Gahh6D8Ak2mJxYYJLwtISV94HgizcluQ_ZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkMjlFvO4iXpWGvF9zV8SpJZd5fgzo88GlZV5McSerQVOjrcT1_AXkPkesPp6aoqOj_V-PSDtwrFnlYnFd1hjWgnOtq-A2jHey6LkT3E58LSZpTyX5YqKn785Uzc5kmACJZR-EjhRFptrsxCA-3CInE4FPavsVcabjL9SWVGZvDPYUBSl-P5FEGX_pvLC9WndZanY1ZFQijxINpLVvhBoA6HfKRMRjujb3rszTm1sJBXoDOsNs_WUgZJfRTmNzljuEDfqAhnOCalhLpfthHHxI3PQKX1ztiRCnR9JhMtzL3cWjcnYthg8TSbey5EmegQ1mKgyhVMOGP7PhQHwkrmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLyrbk0AS2VD4yqiaWA4dPzyQZapKyl0rV35ZbKTGqzbHf280qS1nD7JOBPMM7sNAlIXo5uDq9YMRRUKrGUDNHTL5AC_hPUiV59srFPzAzdavfIfK3aoyeiCyMAUxNPi0bMm0Gtl_F5leENSef0p8QegWW4M1VF1uoQtEROPrgGDYAD1cx8lqfqzDoovMc83wyNqUAoAIT21OYNnDne3sSxoyZKVji_ss2OP4V4Cfwz23zt93jLhHtifAATODI0CnLAaHW8HWq2y--HOx8M5oFa7Ft6ya_dcgJTvsJzvpD_zKR_tZyWTLZ_7_BVkcpg0JFcX4uQBvZAZvZ8rxVwLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKT14pcp1x7gCSjtMkr7y8dnuoX7B2YcpVPLlkJ85QNCI_g3IQpwMDdOWZ7IlDsi9TFQPZLoy1yYFVStFLp-UDMv0RHoX90pOAcNedJh4MffQxoDn17pwTheL62A1pLp4npDjOT6dM437UvXejlll6kLAw7PXa-IvIxFkORAHNqdESVl3nymQ_j27QVoeZBuAr7Fk9-U4egJ8e88lxql_-R_bZAxnRkXf3s6btyC8U6pWwhy55CkSVOJnILsKWudtFyk9REc_K9SnpyDXxFUZI0Lg56oLnKYEXkGGCS2Osw6vJ8xE0NXUO90K1HBpNynReW7LOT3A-4opGTwO42wyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلیشه برعکس و اینجور پستا تو اینستا زیاد شده و دخترا با این ترند حال میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84461" target="_blank">📅 20:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دکتر مسعود پزشکیان:
تاکنون، آمریکایی‌ها سه بار پس از مذاکرات به ما حمله کرده‌اند و این نشان می‌دهد که آنها به دنبال گفتگو نیستند؛ بلکه هدفشان سرنگونی نظام جمهوری اسلامی ایران است.
حمله آمریکا به ایران، که با هدف سرنگونی نظام صورت گرفته، فقط باعث اتحاد بیشتر در میان مردم شده است و ان‌شاءالله، این ماییم که از این دوره سر بلند بیرون خواهیم آمد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84460" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84457" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=eZTC7blSe-2yv0xFv3bfB0GpUgcQ-u9LpnLUkwF5AjMqtyo6GLYZd_iwSAkFI6DGdwQDk43udnEVv-2QYWAKcSy_RUVVEuR08ChCXzpE0igwmCq6bFPv8LeQoCMdCWRTjbV-APn82QmLWR-5gUAMzpNv4pI_s9JkotMU3k4lDKl6UQsm6XuvCDBdTiluxCS87FHqNGu2X9ehNcXSJMd5RGTHEMKd7jTpMuoEuQ7W3bIfJbM8DNmMA2ThwjLpPP2cXwldTvTCCVCc2-saTS5Eu2jLmtxkDDSsGz4IGVOWLrWoSVFhJJcPyWj4dN5SNz1SchEQGHfnecq9nyzGkZNLiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=eZTC7blSe-2yv0xFv3bfB0GpUgcQ-u9LpnLUkwF5AjMqtyo6GLYZd_iwSAkFI6DGdwQDk43udnEVv-2QYWAKcSy_RUVVEuR08ChCXzpE0igwmCq6bFPv8LeQoCMdCWRTjbV-APn82QmLWR-5gUAMzpNv4pI_s9JkotMU3k4lDKl6UQsm6XuvCDBdTiluxCS87FHqNGu2X9ehNcXSJMd5RGTHEMKd7jTpMuoEuQ7W3bIfJbM8DNmMA2ThwjLpPP2cXwldTvTCCVCc2-saTS5Eu2jLmtxkDDSsGz4IGVOWLrWoSVFhJJcPyWj4dN5SNz1SchEQGHfnecq9nyzGkZNLiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84453" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84452" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esQfisaHq2SHkeJPl8T-tO3WqotA9Ui2LpApJkyhE6-Uwg_xLUAhNa5JOCgnAWXhXZ60Vo-y0tWmOvwp41ikLUUCCtLs-qim2j1Jfd5OnjOKGe6HfA1CrCgsDB2_ZuXyu1P0Y536EfXV6NfsIeHf0PH19l-6A_syKhRd-tC9QFzx3L_Az3O74SEaENFVvHDW0jeQpaMoWCxkPn7T13BjCkO29WOqAI4ZsHF4S_lV4HrRh1UZmqUGyaNszrXgcqxQRbK6fZ2TKhoi2ymLJyzsNihNnxkJh-f8y-ttnxrThUFR88aDn_gL5JUMAwpAG73Jtl0H-P7dq4s891bA3KlMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G13
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84451" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پسر خاورمیانه به روزی افتاده که تو نسخه بدون جنگش روزی ۸۰تا نقطه مورد اصابت موشک و پهپاد قرار میگیرن، وای به روزی که جنگ دوباره شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84450" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVkOREXULZjcHU2pl7DYyLEJWHzd7IgTjBdup3yyJjfpPJold7cuZHNCgVbD81trz8dDr6kMXSd-4QVVqH5uV_0J3ViwC5VUOR381wp1foRcSPLrLaYT7gSt77ZCMYbLik-mfgEaynLI5BJnOtQHpHQE8ALFLtz9vWpPO63pY9OhDMJX2lscnAeEF68nmMt1pHnccAVFKtk05Nngo-ZH7bKs5t8_TP-RqY28CrcuIFboXYDRl_nPvJJyC8p-bmpyWHf1BGs1BddnltJlKPsfaNFQZxIKxtVZHSjAd6w2ObBCPTGR-YO7U87ustRQswvGLteaQ81vhhjMk2sZt5vCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر عاقل ترین فردیه که تو توییتر دیدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84449" target="_blank">📅 18:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUryIaHRddJoWFCCmz-8OxKGvnSZhiOJ2mNutZJr-LS_mDgPO5DX3slkvg3cygZdUxcJeV5M90svvPFbjtyaCCMIZxdImv5nVvz7UIU6i9mcWr3KNU_K4tl90UEWCnUPC4fNuc7_t7i_3SpzD5Mp2JESGo6wecpwfUuV5Zc1cBopW71Zxaexk5oRYO7i5MifUqSHvK3W09nDMcyRLle-_bQfe6MroxlMhGmsuamv-sHJckyPLRkoaZ4Co5qRIB8aUiq_tCe5Ru1PdsIWUtHOCjCbnZJ6CZTJAju46DWhJusydU7wVOPTao31fOEMuGUUppILZ4FJZR88Qw2qO4Rb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این شاهکاره ولی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84448" target="_blank">📅 18:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84447" target="_blank">📅 17:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مغازه دارا واقعا بدبختن، با یه کیر دومتری تو کونشون دارن کار میکنن درحالی که ملت فک میکنن اون دومتر کیر برا خودشونه و میکنن تو مشتری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84446" target="_blank">📅 17:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAsxLUmSm_Sx8pGwwl_YqJCzpl17lqMEWEpd6jsihMQlLtjimAU9LbmF90moB_BwomrRBQKwONfqZcjJ9U0-yhdri6LEwj19sPt9esAzl1U_wy1QVdabOhobpKMLTIpWPCfzwLmskLaVK2z2AMNIyKSM8Idmv_3pmwSo5kMsaVlA0X-oynPjtgms1aohxc5SSM_qSsmD0asLDU9ewls5cDCD1_7kyHfDUqaKRsavQ95T2X__0B2HHyuztwK3UiEOVrRtXKDLTK1WBGsfc7U79aCbEDNanuPjn7qSSY4b6QIrQLk_jikZTvLjmIvQ8-B031zBdtkgU6XXbHPPhhVtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84445" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwqGuFyw9XnzDbH2CGlDmUZPhuIEwsRik9fYfDxihJ-92wTqL81_2517zcZ_vEEzEwNHrnL_yS1MT9sgbmoskDWFD_Koe_G035MCSn__8UQt26vh5KZEUlx86BPiZYHN_Fvgge4oE8PxxMNnJCXyXTMLoU-zsevanbYLuXgCIONjdTjIrA2Si6rwPjvRzE5ffMi-EFglrwHALR291lakvg7XEv1E3qZNxO6W1prHyzcq0AzjEoTtQNicOMk4r9FAkl1zu8AYdxOdCGCGO7k5QYrZMaxnMZlIlb3CqLC0qHjGOG17Uiphed4AczJ94Wzne8Zt-7wx5562E7crHDQN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت؟ کدوم چارت؟ چارت یوتیوب با آیپی زیمباوه یا تاپ۱۰ ساندکلاد با آیپی هلند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84444" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=f54AS-adDDvdMm2IBx0GAaqaQGz5E4S90OqWlIOEUOlmv8_Ntm9YD5sBbyMiVuXVJE1xbF9ILvB4fSOrqBg8B_gtYrmznnm3-b7_Jp_9qlzWrK2y-BYBCJrbBQOtTJ-S3tie_h241XcSfF44RSHPFAKFQ7WrPkszLP96iive-XtsI9JXvKbSO8KXJGnmvsRaoYmPKX7dWfUdZmlgEkOGcHbhdb0GKyYdPlGSUKzlnMdkrDmfwV5dqWL_Z_2TUeknvgM-JQih1Cm6yA4_tkBmzGVTdSzLMUWIbZ5RkFpYqnyq8RDjpfLw7JWzuhMJEzMdXeLryNdNjaLoOrCjeCnmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=f54AS-adDDvdMm2IBx0GAaqaQGz5E4S90OqWlIOEUOlmv8_Ntm9YD5sBbyMiVuXVJE1xbF9ILvB4fSOrqBg8B_gtYrmznnm3-b7_Jp_9qlzWrK2y-BYBCJrbBQOtTJ-S3tie_h241XcSfF44RSHPFAKFQ7WrPkszLP96iive-XtsI9JXvKbSO8KXJGnmvsRaoYmPKX7dWfUdZmlgEkOGcHbhdb0GKyYdPlGSUKzlnMdkrDmfwV5dqWL_Z_2TUeknvgM-JQih1Cm6yA4_tkBmzGVTdSzLMUWIbZ5RkFpYqnyq8RDjpfLw7JWzuhMJEzMdXeLryNdNjaLoOrCjeCnmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورو خدا بسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84443" target="_blank">📅 17:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کیفیت اصلی فیلم اسپایدرمن اومد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84442" target="_blank">📅 16:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMt8o0IgsakkbwCwABNzRc1k7eMWq6EajyORyF55EbEBdWSSLtyZ3W7UD18GHuin_KrYgDXmfHvYxIwgluWye-H4tpKHXl5SGJOjnxmd1vMQMHFccAcn1tz2CcNwDQbGpGJZq2xOxrDiDFSavvZGOtDEIsGEs5hWNj3cMu8RTLeJvT1ssz-KrJ5g-2L6lqmVXn20ZN5r9EJYW8T7F9KiGi0DhtZ9mS7fZWX--G1eRW3qVbnOw7IohJkpn5Qw8KrNIVedpS2arfNzEUGHwfyX6Zs4AevBKzjv86Mqbvv-SXas_NqIL7kiWlQbbLCSgqeYSCLR6ptzNjVYdeAfnelRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان همچنان درگیر مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84441" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnpHNnjryl0pqakU9ZHAGxW5kCeotM2o-avydZeGijGGCKHadjqqYkORxJyRQZcQU0ZHy-QuMmZNhLzOIM-pcBKU6D7H7IbIhWZKgFFFjFeARmkvLLryD7V-GAxhPhLt_u0lWWrG2kcUAVAQXHHxOHNn57Xjm2wkAKt9dO4rO46vzJVT7NJFeM1USk0zKvaxk9GUUfx9HL3MrYbNenLGWuRs0O5U2ef0Yc9Z2AejkPSIfMJZor1shcsc4jX43jE807nE3ZWCmjJ2t5aWCkyiNo57-9mKsxw4X9Rymw0vWCEJ8rY2kFNRmzGYrUrr5WaTFwM31ZO6Txot2rLuxYIixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زود قضاوت کردیم
میلی پول ملتو تسویه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84440" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تیجی داداش هرچی نسخه کنسل شده دادی بیرون از نسخه اصلیش بهتره که
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84438" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وکیل تتلو گفته که تتلو شاید امروز آزاد بشه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84437" target="_blank">📅 15:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_hIGzxnPFVdRdKQwjVRaYGy0cMA5-DYRj9wHou79x2aAB5FyALwjrC3fUJGVbqqEIbQ9rW6qUxaMXkPKs_yt2_WAwhU7a-rUpuVEJb7opkRZ6ToqVKk9QGOBnEscBGzh5D_RtfcnUJnn7s-gbmkJL7kuDp_k4uK2VpihZwdLtdcfiGNup3navTgszbB9PgNimJm4Fm3EIczZVLDER_YUOxPCgoW1wWGKoCKldwHNQokzRPeIFKqRRiCuvpUN17AFp5jgbT3oxVQGlK8qrdRueRKJv28DvT65RXUFNBu8XLuJMXYjsw46pdqJAPuaFWEZLpEmXDMotr8CuDVlWjMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورشم؛ خبرنگار نزدیک به ترامپ :
آمریکا در حال آماده سازی حمله هسته ای به ایرانه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84436" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84435" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgOaqSlM8BzqOe8v-QC9hlO8w3QeinwKy_Fc9-K8QoQDYRAESpKAC4hkpeSGOWzBYbzKpShRSpZKZBxXxP9QDhDacGRSalttCjHhoZfuRzPKFmFnDjTHZoB0RuMbWv8_x9gGKN2xHjatoUJCXQXN4UZsOQjem99dAiCvNJfETSUH6FWmsbBe0lQ8kktx33UwdBGlbLJWZiNp-S93BnpYsrRjLCF8WMqXQldBCpucKPZr7x-JzU85JZqCUDesb4RLe8JAyixHiLlbZ1CdKRardAAPwuTopU-Fbnm05GZSwS-cSw2I_OyrBpWQeIu2K9BgHrKUe7pf1_o6zccEERVrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R13
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84434" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84433" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=Ly0hy7v0r6QG6lek7tt1YdkAfCsfHryuRPzn4Wf5WnoksETHFwC_kGv8C1TievtPUHJID1S4F2N-tdsejW9a9_ep30yN27umz7aGD2mbXriHbaddMJWE9PsPHP3gX-3WP8q-TUlovJ2DFXVxWul3sq2tEGz1XufHeG42uQ3qqvFcHYTKmdoz30EQlgwsZ-OVjvqkP-i146jsuopyhLthxd4L1MF8PADZGV3HBiYiFV9ht58Zy50U_V3r4MseuDha84Yp0otMX7k1RErEiPbI3s5dwK13JovvEf94IX4AY7otzh5bODKxurWLop6SvAnryFC5vShgjEk49g1FU4Im1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=Ly0hy7v0r6QG6lek7tt1YdkAfCsfHryuRPzn4Wf5WnoksETHFwC_kGv8C1TievtPUHJID1S4F2N-tdsejW9a9_ep30yN27umz7aGD2mbXriHbaddMJWE9PsPHP3gX-3WP8q-TUlovJ2DFXVxWul3sq2tEGz1XufHeG42uQ3qqvFcHYTKmdoz30EQlgwsZ-OVjvqkP-i146jsuopyhLthxd4L1MF8PADZGV3HBiYiFV9ht58Zy50U_V3r4MseuDha84Yp0otMX7k1RErEiPbI3s5dwK13JovvEf94IX4AY7otzh5bODKxurWLop6SvAnryFC5vShgjEk49g1FU4Im1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84432" target="_blank">📅 14:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم
یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده
هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84431" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84430" target="_blank">📅 14:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8AkJ6yvjMWDAIPJbRvoT-MgRPkxjXuhYYd53cV5MIwgmCgW2S9WIjGqcDBTICJ0oW6J66_bvfsQKg9QOuEGYLIjsJraRXZ1nF87u73l7Hhpgt-eCWquVQdWYw2gs7CH6cUXzJJ44wUlaBMnHsgw5CXY25hKbBRvnwcBWdp6ilRVmITkaWI8ZAUQYlMIP-X6N-6Fs-ykNp22SciIaq85yZMWebsA0pvy1z9T4Vz6WM5ONKk9OJ-MYQ-OlFE3GWHAQGQcOc7lxEwLl8_ZPAxFd6HX_hrveFaqlcCF7YF30WHxS_PS3YuZW02bUp6qM-aZZDkJ1d4GKcffnoxScD-fTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد.
Spotify
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84429" target="_blank">📅 13:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y2SHhB-zKMfVL-DWSZLFlJt5e6nxtKcPsIlLz4sJV6QbX_J6T7wgqT7-VagwIE8KpW4v8MOLpyJfZiJErHfylsJhPR_JpH1Dr6SP5tEHT5_6OkCjAvdUYxfx6yX3B1eqQpgXediUVbZ3UNP1OLNim8X7PF2kDAXHmeHZRVaSp6bHq8Xo19y7gzA6UbnDJuMiGhz76iuvDlZOwPzZCLwAQYhkN5C49h2uwQBW__ApCIP-xdqJ8Rp-iXk2bOFva96gtyFO5XUA8srJ8ImqCZJHqFDr05MnI53tdztbNvviWYhdjvC9Cyb7_9E0dIjG0sRiaK9uo5NHE4fgKjAJnmdpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jr0ZISwN2zFNssfPJDTjtbGlpkrk4fpT-JATr_zzZXd4vwTe0JydYN50s8AA2MaVDuCL42SFfW8Ussk96eZMA_V2e0BOmAJJLOC_DxxFZrNBrWxfbWdu21lm07OnwsS7hTUnitsdh5SujAvqpGTUz7w3uMR7Pp1jOaRFjOFffHtQM6n1r9WjZU_AV_O2t8-TWW09JOcetO0NVJsAU2XhUausv4ak_DiwePzzOixJ-Ip9O0mgj7viRJSi6xUas8sMrkgmlhdlp8kpWDCe_q60QV5i87Z2I24_wkak9pH5HnhhqnV-O_6EirMad5scVDtZg1yBnzniJ9rP8PUZWH1Sdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صرافی ایرانی omp finix که امتیاز رسمی و تایید شده ای داره، پول مردم رو بالا کشیده و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده و مردم رفتن جلو قوه قضائیه دست به اعتراض زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84427" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">علیرضا رئیسی ۲۱ ساله و علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شدند.
قبلا علیرضا سپاهی بخاطر از حال رفتن موقع اجرای حکم اعدامش راهی بیمارستان شد که متاسفانه خوب میشه و حکمش مجدد اجرا میشه.
علیرضا سپاهی با دختری که دوسش داشته شب قبل اجرای حکم باهاش ازدواج میکنه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84426" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9NKS_ony_Zi5daB4bjkGMqrdphR5lBCGfbPboS3OZO9hufU_bM0VARrtNKEx3VU_uV4kxk_1SGBJYA6ZeXHTb4peTofBphoUR5tpGFqLXb1U5adJVsEvsKj5JD3uSxa9xZOfShx1Tan6VsG-hAL7AMd0YweKh5WbNizvSVPPo0wT3yrt7cmr-iqWeu8KTaXOIx7vrLbxj49H7Yp4WXAthgHeN5gzhI6-SZdBXZaAT5zt3iHl2cPJ5BLhtC9dU0yCpPd127JCzYCqRoy_MfVd_dLsVzZOt09as45xShpdDbTV1IqmPOpnML-RkgnkF-SqHEgXJUdoYg8hLl4OjyR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84425" target="_blank">📅 03:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84424" target="_blank">📅 00:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تو رسانه های اسرائیلی قراره بزنن
تو رسانه های آمریکایی قرار نیست بزنن
تو رسانه های ایرانی "زدن" که میگن چی هست؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84423" target="_blank">📅 00:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بمب افکن های B1 آمریکای که برای انجام عملیات تو بریتانیا مستقر شده بودن برگشتن آمریکا
ناو جورج بوش هم رفت تایلند استراحت
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84422" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DBqkKBKtUZiy9Yxw7qC7CWRGZYiMJi2H3LkoJBr31QvXT7Pt7HsiCI7t-NgAyAOqK5HGe7_yqKKUsn3_3qGBqYegULHTCsLm-9nJisbkHafmfYNEqr5kfcgPJv2ictFlGxzt6pIa74TuvpoDsKyJ_2YwqWoc8A3fwjJu4RtmsX1G8hVeQ1LBHnXdjfbE0RmlAJaYEBMsNOIXyHQ--ISnt20i2XfaLvIXrhth9jwuTLjz_ZddNjDsLmqKJ0gIxLXEzUPWkQcPP-GkwWfZTlGLiRkfK6aXwRl0OanypGMy7ceqAkOx44WO7msp_rFXfdIRQBWInp8RSnZzK7Tutqs5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DBqkKBKtUZiy9Yxw7qC7CWRGZYiMJi2H3LkoJBr31QvXT7Pt7HsiCI7t-NgAyAOqK5HGe7_yqKKUsn3_3qGBqYegULHTCsLm-9nJisbkHafmfYNEqr5kfcgPJv2ictFlGxzt6pIa74TuvpoDsKyJ_2YwqWoc8A3fwjJu4RtmsX1G8hVeQ1LBHnXdjfbE0RmlAJaYEBMsNOIXyHQ--ISnt20i2XfaLvIXrhth9jwuTLjz_ZddNjDsLmqKJ0gIxLXEzUPWkQcPP-GkwWfZTlGLiRkfK6aXwRl0OanypGMy7ceqAkOx44WO7msp_rFXfdIRQBWInp8RSnZzK7Tutqs5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه همجنسگرایان
🏳️‍🌈
طرفدار فلسطین
🇵🇸
تو فرانسه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84421" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=ayxRncHvllYnOT3_sXHatRGY5DYI8IV6AfaP4qVkJbUeIvCutqdDRyHDop1jV8N4xhK6shSb96lH4F7ftA_Us4_2XNi_0oCPzz5zRNwk2ROXGILrY0Vue0YCrF6KGKhCQR61u7Er80yMxDeoaZhIdxFvmH6jy2ih9u5qY2vdAUqrnyN4F4Zi3hgjCXkvo1MQEpPkMm6cEKrpI5sOBNq5sVfC7_mCrxSLUt7gijeAkiA87imj4IBgKQeN1xhR1PTQ_OQIZoSWRORjpgkIrkBH_Zh7D7sGIZPFHydwRUCh3mSydu1DN-cc1VjfDv_r4MXDfkjXrPIBDd5BRXPrWKuumA1gB1ihWDoqZGm56oLS8_G8YmW-7T29E_lE1Qn_dR6lcV2RgzCjx1PjCnI9NOMJW5rDOCC4kev0wraugTHEQfoI8q6QzDrqnNAQigr7kYx3kszFjpgqRVRjHjGdvlCUi6NaI7QPZ0713hb3yA_OKE7RPp1GmWcQRryCvLbaM0IPp1BIgfxhVpeZUAqx2yzVhPTJcKzwFBHc4tx0xzd3B4vRlxaxlO6Vr0uGuUM4ABi2zSEcp34m8Jo9fbHcktuxJNfn33LNA1leq_WG3JyQf5TmAHILWEvzV0ftrQ-z3V3kW684i3bC6vI8BJNMlZQY1lH0dJb7o5diBuVJJJU0xSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=ayxRncHvllYnOT3_sXHatRGY5DYI8IV6AfaP4qVkJbUeIvCutqdDRyHDop1jV8N4xhK6shSb96lH4F7ftA_Us4_2XNi_0oCPzz5zRNwk2ROXGILrY0Vue0YCrF6KGKhCQR61u7Er80yMxDeoaZhIdxFvmH6jy2ih9u5qY2vdAUqrnyN4F4Zi3hgjCXkvo1MQEpPkMm6cEKrpI5sOBNq5sVfC7_mCrxSLUt7gijeAkiA87imj4IBgKQeN1xhR1PTQ_OQIZoSWRORjpgkIrkBH_Zh7D7sGIZPFHydwRUCh3mSydu1DN-cc1VjfDv_r4MXDfkjXrPIBDd5BRXPrWKuumA1gB1ihWDoqZGm56oLS8_G8YmW-7T29E_lE1Qn_dR6lcV2RgzCjx1PjCnI9NOMJW5rDOCC4kev0wraugTHEQfoI8q6QzDrqnNAQigr7kYx3kszFjpgqRVRjHjGdvlCUi6NaI7QPZ0713hb3yA_OKE7RPp1GmWcQRryCvLbaM0IPp1BIgfxhVpeZUAqx2yzVhPTJcKzwFBHc4tx0xzd3B4vRlxaxlO6Vr0uGuUM4ABi2zSEcp34m8Jo9fbHcktuxJNfn33LNA1leq_WG3JyQf5TmAHILWEvzV0ftrQ-z3V3kW684i3bC6vI8BJNMlZQY1lH0dJb7o5diBuVJJJU0xSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدا این بابا بولد شده حرفاش شبیه شیما کاتوزیان نیست؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84419" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Chera?</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84418" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgtyEtiPg5fEM9tp1LIXTILJa8AxP3qCLCkKq7dYGWbulKhanYIgk7OMNdN_Ro_oANITiQm2IWWAGOe1TDMAtnfLvYcj1Eky5rSY9xOs9BuCI10Lw-v04J7TEV1Gyx_S41Unm6xA7nwnEQNqA9yP7KnGpbh0k7twNtPlZ7HXUkv0PQo1BxAzHRMeTCYcqEbWvljghjWO-iPYRCSURmJprlYI4WWvUsukI-QpqpfGVQTdiFoPEHq-g0vNA8-g5qNKzEuIhVTtLeCViNCavlj-iKppYn2Zm1s0b3Sk-U_KaQERqAsW1nLaCK3jbbvYTnCvqskceVH895W2FewBuew6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84417" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر نفت جمهوری اسلامی استعفا داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84416" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riam6-VAwHAf8-Iz2X_cNbKkdVgQvoW55KSeLZ_Rr74H0R0W8Yk02tyi5-CbqpIf72GQ7xHQ4jrIF62EvwQPGyJwy-DG0lIL7uevOL_fdWnIVekG5EU4VK-Ecwp3UbZH_2PZiRw7i55CDHr6NuWFgvLTw7Wmylo0ea_vItbIEG8NUBaykV9YSEsEUvbQD-Z0oko_9nPLZCgeqoWdGV5JikffN5Q7S2FyodAqWAgmG_LHJ_rYk_nCHJJ0JDhFv7uyBOnvPWtLVw-yb8z2qB9ZY39HNePj-U1QC-GaZSTjMTFdQZ7aQqhHJHuNd-Ymf0qzhBwrWHlE8572Ymj8G3B0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و کاگان به اسم «هالیوودی» منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84415" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNkZXg7FwDZOrqqIObI24b8p9qV5HYwP8MaUxZYD_yIlk1i_aGvckNSGAMf53TgNrlaP0DzO_wzATjWg-APyyLxBioEyZwhDCg_IBl-ErOmlE0DwDfyyEVOG-iAO8ni_c5YULwjAdxBZlijI6pKFhXae3g1vt5U0r6mc9vLSJWOeEHrFDVw3jgXg6Lonk5m-vs02CLpKa4YTt5Uve_UysKsEq66TAfMYRNwY4peT00_govEpE4KjLJ-643nSfkuFsn43Cp5D97AJbIxgdEvgZqDZS9ag6-gvQJmRxmUZWjOggmxx0CzaKj_kQo0TddtsjUL61FmVqqpu-VG9s-QcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G12
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84414" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkr6av0D-gnqWtaw6a1ysfGx9XXNv7gbt23hVYvoocZ7mkaO76AgsjdBCb1k1Dusxs0YPUg3WKpOJE5984ZKA4a-RkrrU1H8QpYjqL-wHA-Lm46A25jmAc6zrnF8I2rpZ-j1N43LnBNrAXSuYcVgohP9VEF7b-t59FlXavwYE11CRVYx_2hH5-aRt3909Hb6Tt0_D5Vnhqxuc2x2g0rAJvwb0tB0JoQQK9vxZ3fhzvaXwfr7zn1pJ6DC80ZkRtox3jKEarh7HAsgf21XF0Zp6Pne1OCRaIhSmTpFzP9RPZ0yCxKJDR-0k0950Ai3Ge5tI74TPKVit3jdOPFqd_Po9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاد کلیپ های دوران بچگی میوفتم توش میگفتن من از اینده اومدم و ماشین ها پرواز میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84411" target="_blank">📅 19:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تهشم داداشم جوکویچ پیر سگ مچ زورف رو‌ خوابوند</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84410" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84409" target="_blank">📅 17:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84408" target="_blank">📅 17:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFUtGoU80Len1_jcXGYrm5fWtowLKkrL5nNiBnJvOPeh3d9YnEyMFJ2mXPhzZ8arbzfzogW20DZc6Jx3VRu0v_827Jb0ai1jrRtABcvNHiPKSsXxUYU7_vL-NQ6IbQLjt8JEDScPHBn0fhB6rDf7H2Px1GVVBQhw776CUWvja0aD1Ka4bRl5J6Q9YlOFjxQY3dZTCR2w1a6NI2fmrqxea5dfseV0xGM12FfBozR8xloShYQcH5ZMoE8rbaRobUJamFgCxUEl1X8fGN5_GGDARiv0XLUFss52THTcdewfquQeZDPY0YyJ2HuOf1ZD1ayrK1_HlHNvOekiY2F3PD3rDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام "هاها" ریلیز شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84407" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84406">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=dMQ3nNV1eUMRkALplLyNhIAtfihzg2EBzCgCDCfA2celHjhO0q7mUNlGbuZ2Dwv3lbkXZbgBIm9DqUK4uASYzuM7Q1GBLPvwmsHl3onOZsdAgTZWfCHd2bMN9nItGl2Xmwe3PCH8dio33mQc1JZyNDQJzhXqhgYp8JeGpOhIxTSw4jYhoOouFVhcPrPhN2B0ffn9uaeYlEKWaOxht5AzHoN-DHMWaaQlayyLKc9fALNF8ShGeJCDW_ONY-Lr4dRfjZEzB5VNLbDuxDAbq5DETsQF9JNplj4Z7WFassPSaPkByIR-OLGntn_xiv-SmJcj2wiNQhhN_R0KtIob6scTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=dMQ3nNV1eUMRkALplLyNhIAtfihzg2EBzCgCDCfA2celHjhO0q7mUNlGbuZ2Dwv3lbkXZbgBIm9DqUK4uASYzuM7Q1GBLPvwmsHl3onOZsdAgTZWfCHd2bMN9nItGl2Xmwe3PCH8dio33mQc1JZyNDQJzhXqhgYp8JeGpOhIxTSw4jYhoOouFVhcPrPhN2B0ffn9uaeYlEKWaOxht5AzHoN-DHMWaaQlayyLKc9fALNF8ShGeJCDW_ONY-Lr4dRfjZEzB5VNLbDuxDAbq5DETsQF9JNplj4Z7WFassPSaPkByIR-OLGntn_xiv-SmJcj2wiNQhhN_R0KtIob6scTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عالی بودی حاج اقا
یه آخوند یه ایده به سرش رسیده که رزمندگان رو به موشک ببندیم و در اسرائیل هلی‌ برن کنیم.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84406" target="_blank">📅 17:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84405">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlYKSbOPPiUfg3xc2cqiG5ABcWpvywmG_0s-s7fE_F6fGt1VJwyCWJ4_9dwkiMasj97DIcKbIDrb7CgpGA-uve_Hry3gG7mUI5aAJXrDKh242qFCYY_Gd6SqtGoWtxh4k3CNyIKLyYfgFVjaSfF6bGSKOIx4V0OLXjUBEpyCDzrTkx3xyPVrpD5XqgEAUMODn9ON2DUa66yC2B2yzMOV1lsMwtpONWXyc1XuoedE77D1oQouz21fY-i-tYJTZ2ZV-7e0OG2HVEF_UJFH47evrYqeZaJX41FiP0mwN5ytfuge7KCf049kS_2Kx7pH8Nw7RCGYJqIdtg9gj2r9fyE-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل زحمتامون بگا رفت، تازه تو ویدیو هم میگه امیرمحمد افتخار ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84405" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=CJ7zzPQqwtY1cu2Oq6uyRetY2vBBkK-W9F0cP6QIYr84N-5P6kuy16rtXAFLqhsYwkXXY2H44-QHt-ACnFCWv-ydCuDzbizicVzbF1ULdi5QMkAk6p6fJqC30rkfvHenpTjffwyoV4P7-8XZIFbkCFuaU8spFpCFpLUcu0JvjI3389N7n1Y-tNRs45xduYxRBLkzGrl6nLJZqHNo-zatkyMSnWGK2uM1QPBpT2tdiwhrFQBIbjgI38eUSFXqlV9ZGaHxSIaVj6yZfdFrgzbz6cBih-xvW5PDdhsR8B1oCnPV_1CB1qJa1yB-ujchTyPQHyPT_26lQ0Zqy82OdRWF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=CJ7zzPQqwtY1cu2Oq6uyRetY2vBBkK-W9F0cP6QIYr84N-5P6kuy16rtXAFLqhsYwkXXY2H44-QHt-ACnFCWv-ydCuDzbizicVzbF1ULdi5QMkAk6p6fJqC30rkfvHenpTjffwyoV4P7-8XZIFbkCFuaU8spFpCFpLUcu0JvjI3389N7n1Y-tNRs45xduYxRBLkzGrl6nLJZqHNo-zatkyMSnWGK2uM1QPBpT2tdiwhrFQBIbjgI38eUSFXqlV9ZGaHxSIaVj6yZfdFrgzbz6cBih-xvW5PDdhsR8B1oCnPV_1CB1qJa1yB-ujchTyPQHyPT_26lQ0Zqy82OdRWF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها شاهکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84404" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=gWBgFGd5XGGOQasrQXcrO3PpH2Hrov72XqdoygMbN4sY4zEcZbDuVg5d_SFB7lBsiJClJ2pi2Fg6LIehJlH6jt59sHBY-yFi3tkONCNyvkUrWJJ5LILCm98zVkOW6uIiHojYuqp1AqH_Z-usw_7eer6ckSCogm74Noxtr1Xbo2cbIwaLnKM1zJLeOSSxZXUCgqF5idmm4u5PmvAh8vRHMz-dcgX5jwBtnjNgVcZGSWBVLw4F5512lICm-Q751TKwiacwJVkAW8moR9Akrz5SFvZ_Dw_5ms3J7da9_D9HDU-FrSWOQfXm1Xz8n1TrMxjAwtjw9qM8O8WJ2h-nafdrow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=gWBgFGd5XGGOQasrQXcrO3PpH2Hrov72XqdoygMbN4sY4zEcZbDuVg5d_SFB7lBsiJClJ2pi2Fg6LIehJlH6jt59sHBY-yFi3tkONCNyvkUrWJJ5LILCm98zVkOW6uIiHojYuqp1AqH_Z-usw_7eer6ckSCogm74Noxtr1Xbo2cbIwaLnKM1zJLeOSSxZXUCgqF5idmm4u5PmvAh8vRHMz-dcgX5jwBtnjNgVcZGSWBVLw4F5512lICm-Q751TKwiacwJVkAW8moR9Akrz5SFvZ_Dw_5ms3J7da9_D9HDU-FrSWOQfXm1Xz8n1TrMxjAwtjw9qM8O8WJ2h-nafdrow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواشناسی یه بالن فرستاده هوا یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84403" target="_blank">📅 14:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s77GSI18qTm0b6Vf3ljB0xUHXnQad2GMGmb2hvvcS78nvm47qw-MT9pxdERXUdGNncpwAXlz5VLURpYwdxG6CTVIxXC_Gmrwun9a-q5_iN1Bt7xM_w4AcTGU1uxIr9M-_KkgGlbGgzEBiFjmS71WCW7Z7PAlT9RDWsMcWzV5wRQEE1u5Spiw51hNfFT6K35ugxFVp6fMdWbLohZrhxlhzqpLP49pyGeTlt5hgRb7PzxNis9YxCIVs5vDLqRJpKb5E9sT9Qb4mHOi5PQc-5I0FP22i04ygMMOWaqG7Df3fGGr6pNkfk54v4rw0wUvGnSKzDAn_HliWtmijqo2hMGRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی تو ایران هروز شوکه ات میکنه...
دو خواهرزاده، نسل دایی ‌شون رو منقرض کردن!
چند روز پیش تو خیابون آتشکده اصفهان، یه مرد میره به طبقه بالایی‌شون که خواهرش اونجا بود، میگه صدای سگ‌ تون ما رو اذیت می‌کنه.
ولی اونجا اوضاع بد پیش می‌ره و دو خواهرزاده (متین 29 ساله و مرتضی 35 ساله)، داییِ خودشون رو با چاقو زخمی میکنن.
دایی چند روز بعد میره ازشون شکایت میکنه و این دونفر هم به بهونه گرفتنِ رضایت، وارد خونه دایی‌شون میشن و اونجا انقدر بهش چاقو میزنن که کارشو تموم میکنن.
تو همون حین، زن‌دایی به همراه دو بچه‌اش (پرسان 6 ساله و پرهام 12 ساله) از راه میرسن، این دو جانی، زن‌دایی رو خفه میکنن و اون دوتا بچه رو هم با چاقو، می‌کُشن!
در ادامه هر چهار جنازه رو به بالا پشت‌بوم‌ می‌برن و سعی میکنن با ریختنِ آهک، این داستان رو مخفی کنن ولی نهایتا پلیس متوجه میشه و دستگیرشون میکنه
.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84402" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قیاسی سهیل پرنک رو دعوت کرده برنامه اش، سهیلم با همسرش رفته، اونجا گفتن باید یه اسکارفی چیزی بندازه رو سرش بعنوان حجاب، سهیلم قبول نکرده و نذاشته برنامه رو ضبط کنن و زده بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84401" target="_blank">📅 13:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Winter Is Coming
بابک زنجانی: زمستان سخت در راهه، اما برای ایران، احتمالا یخ بزنیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84400" target="_blank">📅 13:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SumKVVd4tyAgmW846sZmvHTqHLl4C6A9SQwHIep8TMCEKEFAb4WlWgm4K7vemkS5cm8yn2qd7F6QVjJDnmuKkpdqI42_5TW9gBXM_zZNaz5cc__ov2uhWlbXBI1Y8FoGSD9Ib0G9dsAD7nbKHXfxUKbXIJ_bLScAMd4Jnfgq9JAHdqFVpDMXkB8d3BO4Mf7qnMigRwRxl5OZAAPIui4J0g-Ufx70GujpUpwrLMa54fcolQzD-eNHvpFk6OLUcFuJIPfp-WFzJ2TnsNjAO_4n362HDGzHXcggHTiRy-R62dqzw0JGPfsC1mOR6nVRezRRueChwTdOi8looN9kdxdR_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظهرت بخیر ایرانی
-دلار:۲۷۲
-طلا: ۲۶۶۰۰
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84398" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=UI_egGLn4U-sKZKn-8E5SMLovTuqjwOVTnxriletTlJsSAtDil67WEkdwcea_ncF0K708nN9EIqRJOzPAxUmSzVQ_OtOuZaLsy6A_goKsIcH98bk0LNBq_am3N5hxaXGvtwOdwMvjK6T4ImWrMGC-sfMIf24yyOp9j03UJqyC6ksdCFvOZ5RCH9bC8nPmHtpc---8ZymM38dhgs_2NcByxt1XPzWK-_oSFndRwyTxvfslvemlINWk0i911zPGfiju5m0lV3Sw05x37M-KawJt8V6QcsFU4pTS-p83My3ll5Zu3Zw73CVeI2Dv2e3m8LRXceIa1Fv7GLBinRFJfgv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=UI_egGLn4U-sKZKn-8E5SMLovTuqjwOVTnxriletTlJsSAtDil67WEkdwcea_ncF0K708nN9EIqRJOzPAxUmSzVQ_OtOuZaLsy6A_goKsIcH98bk0LNBq_am3N5hxaXGvtwOdwMvjK6T4ImWrMGC-sfMIf24yyOp9j03UJqyC6ksdCFvOZ5RCH9bC8nPmHtpc---8ZymM38dhgs_2NcByxt1XPzWK-_oSFndRwyTxvfslvemlINWk0i911zPGfiju5m0lV3Sw05x37M-KawJt8V6QcsFU4pTS-p83My3ll5Zu3Zw73CVeI2Dv2e3m8LRXceIa1Fv7GLBinRFJfgv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84397" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY1XShR9jTwKD63TeqZV1MCnzelJSckifuC8_I1_38pgcFcEcCY4vjFL-3-izgyOdAJOnGK5iyu-Muho0Qe5Qku2HFDteNf0_8a07zYL-uSdYTmMuQJEd-E31loOP3zlOgh5AuufdNnPEzdW3r34WufrYl9hiIbMcjauUo6QhO2s_yPUNveBUl9cI_Ulbr9vqz1xL9SLhdO2hRKI2_kSmGZxhcvLfBvFZ_gkolONke8M5k6uZMMI3ARBqOAmsFctTSHMRWEbbca17-eqLSQN4IQkVISVJo7ToF-bYKJkkPUDezR40vs_DgqluH53iP4c6qLgEUMaTQPF2ryK9FkzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
روزمون دراماتیک شروع شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84396" target="_blank">📅 12:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKl1qKv390yrdclYQf34ewNlVn6nF8diFxeGt44tnPfUi7l4bM0Ror3wYUdfUuh3FgeTg1d5gIT2cO3WJlIAHqoTjZtN5Y7xjFGhpS-r7QrS1qba00i-2-htDgJ6bHajqdPHESojPS3ikrRu_saqFFSlW0di4W6WlL9faCFydbPwQZwpM3jR8-JDztwnI2y8AcZIgjFkVloTUDy_RSFFiXEH5hoIEF82HgoML2JHDxX3X_yqLeL1bgxfm_xXOua906LBGdvdNEWuSHEKP7nhGcikjYx4Rm1Z28chEB_K0MDOtsHERomK-I9kDyKIXE1cUPgh6Mw9RdffiXvKJCpv4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشین جدید ایرانخودرو به نام 207 elite
قراره از این به بعد اینو فرو کنن به ملت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84395" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84394" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBUKEwID2hYjJcxfCBIk3inAmy0A6kxIAaMeshyuvdUnc2ELI0qsSkhGKxiul5x0P0zmz06lnWG-LtzqhaaG-HahYt9V9MQC6bsmmrYhVu3sHYloQxStSo2yrFR2-2XPAz5dNPuSZWs2XkOXIPFrynNVIxKeST_-lL_BR-JembMWcTrPHo9Hn4oPPwlVbX90VUVSZVXXL7nla4olEoadZpWP5_59JevLtjbalbcznWKKbElYo8vBTISfVKKt8GcnFjeEjNfwKy5u9V6CC6MYG0yyEMgpCFqvQAB1Ufxjk-dGX_rZOTx7JWLyUJV3HSi_X-QFqiMty7LCFhlJHV5cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R12
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84393" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=ijq_kL6noya8peuWUYkccaMNUNaCxrVizTZRiWvlVPI8prGOF3ZGd3BAr4UgG3BH352ccj2WTGxIQ8gt73wChBvjZsXqOtUcRIn-B9lJLiwc_iNn-gmk9suf7YTJ3FxCBIoMHVp2VlH1lWD01iFFNmeUtL65XEEub1IiKP5HCT-7Zt1L1RI-PoFAWj3cliaU06N3Doy6AMHy19A776li_RHz8ZYzF-SbX69ODxOz4BmPgpiXXHHATttkjLQoLQ6st6FLcSfcJl4a9FtmFTnTI27Wd3FmazyY9XTufvwGzGN74yBhFMGWb-gg4FRRByNFPKolJJVpoAKyos9yYBb1Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=ijq_kL6noya8peuWUYkccaMNUNaCxrVizTZRiWvlVPI8prGOF3ZGd3BAr4UgG3BH352ccj2WTGxIQ8gt73wChBvjZsXqOtUcRIn-B9lJLiwc_iNn-gmk9suf7YTJ3FxCBIoMHVp2VlH1lWD01iFFNmeUtL65XEEub1IiKP5HCT-7Zt1L1RI-PoFAWj3cliaU06N3Doy6AMHy19A776li_RHz8ZYzF-SbX69ODxOz4BmPgpiXXHHATttkjLQoLQ6st6FLcSfcJl4a9FtmFTnTI27Wd3FmazyY9XTufvwGzGN74yBhFMGWb-gg4FRRByNFPKolJJVpoAKyos9yYBb1Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتش سوزی در پاساژ خلیج فارس عسلویه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84392" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پاشید برید مدرسه بدبختا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84389" target="_blank">📅 06:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPwXa1vPYdxe2tpvAiDenhKmwTqx4WQ-apGJ2Z1bDBG_8tHv2WqfJ3OJZqDXnNKnT1OJS6S5GXkWhjhdmfFi4DDWYhbhxDIX95_fiw21pa8TsVd7GkkXE09nSBnVI1frbLhVn9n24yCPhkmPP7ALrx8IO3PnNbgvxY2NsKujBDRePYCOdq7kCQgDr-iq-bZO0gzU2MlL1adqeDx1sd4Dmh7068kJi8ypypIf7xJ7MCaPxxvmlBNvT47FPQjZRyRQBx34Jmjh_l_Yie6KhH5sg29TJG_JYZGvkTfNHc2g9UHuoQk_KRX834-RUPX8dAt8e4UJ5MA6DA9l8oj6bweKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ دقیقه نگاه کردم اخرشم نبوسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84388" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exR1bk2iEHeBntg45SPkeHjjIq7clolgUbz3rGH3FQI9PeGz1wr-off__Un9-dhsnIm9tTXDimfDQSNwN1-kZseWTKTcxmHFej9Jw_8duUO7K9M9bKRhL_FI943mSEiBn6-R6n6siMQn9HDvt9D4KXH4u_cGNErtLl4Zdof7GSAOj3iAOSBSjZJN2Q5SymmeuHQsnlrNiYkUxZDnWh3RS3lta3tctf-yN0j-ycTr9Z5mzGCqGl59c5yfeG6iu2I9NE9HC0rNGvOo4JE0yfrlB-V-y3sKmsKUdPe1w5MXOHQhqACN3y_iEyN6Ig5dZccSPSEofgvDZbdwUVR7XvOcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/84387" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=DGvtbKJTTvM8VWu38KZoXT5i5LS1CtwNRRmSKNPz99u_0aQv3Nxb8s0U_tn2oHNnJUxNI6biaFzsnZtWXmdWxiLalNk7B6PaOqsx4fpbl5Mg5fyyZ124SNV3RJIlpLCok0x2pLvLdkuHm8og408Cj9aDhZlTWvzkBUEi7DIvCqzoqHlyhT3NiBQNbQ27AInpoF4a4lDGcAH_EwWzHsNpQQ0Ga05osablzoHtA_yuEsxvuAUfWLoRpHbaGr88iVdbpjophUcRDVLKCtUYc0UIMRlRH2Jfn6gJ0RArYi-Cs9qieyC1eKuTvGiDJ8osfgDVU4wyZphv8akbTTUvklKFWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=DGvtbKJTTvM8VWu38KZoXT5i5LS1CtwNRRmSKNPz99u_0aQv3Nxb8s0U_tn2oHNnJUxNI6biaFzsnZtWXmdWxiLalNk7B6PaOqsx4fpbl5Mg5fyyZ124SNV3RJIlpLCok0x2pLvLdkuHm8og408Cj9aDhZlTWvzkBUEi7DIvCqzoqHlyhT3NiBQNbQ27AInpoF4a4lDGcAH_EwWzHsNpQQ0Ga05osablzoHtA_yuEsxvuAUfWLoRpHbaGr88iVdbpjophUcRDVLKCtUYc0UIMRlRH2Jfn6gJ0RArYi-Cs9qieyC1eKuTvGiDJ8osfgDVU4wyZphv8akbTTUvklKFWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رعد و برق خورد به نوک برج میلاد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84386" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پزشکیان: نوک قله ایم و نزاشتیم فشار اقتصادی رو مردم حس بشه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84385" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=sCwIbhKnSAnlGwJ9mMcq8xdQ0-3VrZFMO1JvGaFTfyqdCyibYoZCLunYDMrtHjH4YlfTRrFHwhtaKMGr16FHr8v2gKDoQoTwsp8dcYTdb6HcTASlrs6slusjbgpVkK7JPVlzQgdQMbRgc3Z3KSMPtb024Cafq4Z8X17GlXmjBksbZqRmcn-728jKuDCn50fxU_QAlDr7WAG2P2EZzh9yRkN1TnGXZ9ZDy3TqffUopPEQv_Qhg6EsCKf35TPd1Z-zjc1ADaLikP1p71zwdU8H88jqIssHaQI2C8Y6KQxX8ExJa2miLlKoytZpwPi-M9Gs3up03Xpiv3zoahR5iEk0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=sCwIbhKnSAnlGwJ9mMcq8xdQ0-3VrZFMO1JvGaFTfyqdCyibYoZCLunYDMrtHjH4YlfTRrFHwhtaKMGr16FHr8v2gKDoQoTwsp8dcYTdb6HcTASlrs6slusjbgpVkK7JPVlzQgdQMbRgc3Z3KSMPtb024Cafq4Z8X17GlXmjBksbZqRmcn-728jKuDCn50fxU_QAlDr7WAG2P2EZzh9yRkN1TnGXZ9ZDy3TqffUopPEQv_Qhg6EsCKf35TPd1Z-zjc1ADaLikP1p71zwdU8H88jqIssHaQI2C8Y6KQxX8ExJa2miLlKoytZpwPi-M9Gs3up03Xpiv3zoahR5iEk0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84384" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توپ طلارو واس یامال اماده کنید</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84383" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Nq2sV9_SFcF3kolWidpEj55gId4ArHIFrWNpHQMxpnLXccAb9_xfybprIzFU7OiAZzb717yIfo4Pg4ryiDzzxcShztFazd-UEeJVzHuL5Bgbnh7d9RzzN-C4s2219MxqSJG04jPUGa1skgx5rzYybYxb2lXQ9wFCE2JFe2h-jKM7IQRzXY7nSohLdKFhDF2ewBVXbdnwnShiT5be_uxTaasuoAFrFcwPnRjGFdJlRjcdi84SGvDjIIzk_JbwwxHTElhhLcOjFT4vKAvtqTS3TljWFqXFa2c5-SzXkCyzNAQuvyVGONGkPPd6mKYqMB4eHoAAkqRnpxCrSvCLR1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDH1bj-0piSGP0AeQOuKyCRcdHNsGxrkCZSs_UEDl6Zj9pEaQaijes5byyuGhI8giBzZQqGqnUMuDUGjhSTl9PjQgYGGKgn4nSAVaSLYHS41L18lj9O22cbxIuruUmbrn7lI2_i3SXnsJNNl-ItkMzsv57KCFgWQMuXs-mUyetORy_sk4eghn9a5b6L3ij5hZP_eejMyQv-uyP1WYIhs8qzbk_1SwAcema0OJIkgSu3S4VumTDWEWt1ZWDQ-y_2sLE085852kWgR8mP9NqazL2zqJobF-rRXZ-J_1YO_kSk2lz_rs_pmghLRmpNilKJAQy4fb2gnJ2WCMLyl8erlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=iDEn9bBO0jpzXdO_HFvE-cwwY5iOTqWoK5RHEy-fb5IhKiNNU2Mwpjq0XCMGlmQjQtFQi3gPc35OccKF9W7ad3NaQDFR1B0WtGFki_jJkxkUGGavFefJtz0HH37Wx0ME-2Olu_O9WwxGwdGKYpMcPWNcnSjo5X68JuMOzvD3IOlEKP2USULEnIMVFpz__1Y_FWlv_UgJHVm1yHi24zs1WZ7ZYp1d7sSP2evT9oRqGoF3ec6a1ckahDhyzOvwMYrtTnJleXO6T9Tdzl8737sCGkZJVo1EVQaSTBeB4ASat51fDgsoHfS6hPrWdjyr-lh1H2lZH4JeUxL6hX5L32oSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=iDEn9bBO0jpzXdO_HFvE-cwwY5iOTqWoK5RHEy-fb5IhKiNNU2Mwpjq0XCMGlmQjQtFQi3gPc35OccKF9W7ad3NaQDFR1B0WtGFki_jJkxkUGGavFefJtz0HH37Wx0ME-2Olu_O9WwxGwdGKYpMcPWNcnSjo5X68JuMOzvD3IOlEKP2USULEnIMVFpz__1Y_FWlv_UgJHVm1yHi24zs1WZ7ZYp1d7sSP2evT9oRqGoF3ec6a1ckahDhyzOvwMYrtTnJleXO6T9Tdzl8737sCGkZJVo1EVQaSTBeB4ASat51fDgsoHfS6hPrWdjyr-lh1H2lZH4JeUxL6hX5L32oSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVc7FAXOqwga-t6vl9YXAhI025FS0wvjP6QgZswEgHkVzerzklJpK-ThnKUZFJatcGeVDblQd1eaJpFbwrQ8DNxHtnuJn9PvQUPTBZfDTfyTQmiqesrWMOCuLWbhdhan7mRGHmSQyLWwFG3c_tUR7TLvdAoUjPqdRg7mr3oGt1xbaTbDEk2QYn6mPBKKsPS46RyWf8AHlWN_JCA2IWh588zrjMuI_1EzJrU-POQBwJ8bOj-iK5qD7xSw9RtMC_DiS9Hqr0KaD0O6-J_mc58jq2KCeTjNmte_PQjSy6XQEh5JTD_oUAC2PFw-NavwYj2eHEY3Lunlm98P_880Q0OY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
