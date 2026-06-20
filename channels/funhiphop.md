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
<img src="https://cdn4.telesco.pe/file/uuBqIuCxj1taWsOKRqAlOXySBDTZSHa5asfVSOb1MZvYJmFIIF6TMIcQ3VhTCT7K820JdqFDX357GBPj-LFoMJVUzJWADmpelEiQiQsXYqzc_gMDghfD2W5hLrHWJeW7LRLm1mFyASELXafxfL_QazeWxyZTqGUo6FXlFJNd4edd2AVJBS8F9gLzhIYfhyrzLaK1R8v9GtNmaXKK6axZsk21uzr9JSg2yXjijhApTgdJOMpeUscxw_oMI41N9YsYJ8GE1ePQ89x1VUqusD-IiDiv9aOW25AfF4iAyYTnq0oxWMUo1ILyk9XulKzObgXnjerJmYzDSjBf2P60QnrYmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IOZVb7vnE9zYidljHQz7aAaHcmACrTMUESnHYnXvqnZJ65ixxWAYMd6INSUnXaAHs3OvLkjX42976iRcFlX8KMuI4KUXgX_pQQ5PCwwY269os3UPBjaoxgiWs-482E-AVzpkMzCfsxxBW8-tdIYbJIW49e8HJJxB5YmnVqYFyfzZ8Gymq0ZMC1BPKsfF0_u5kwFIqtqL1YMGLc0Gvn4A5fTB6crMmEf6mL9wqFi-uBc3xrpPYrVO7Ry2YQyuLuTYKHBHzCWa3RkN95fgLs88WIh4dWF0zOwsITMP8j_gZzWYc99kZdUiZsFZe1eKwhQlM6dSrWIZai6Wnb-APkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcHnPy64UYPiM_rS5gBvMEF2AZfvCsfpjXUyv9cHBx1fn2y6POovFi3t8KWE727VJnNz_TwOQCwHN08V4K12xApHogZh_fQDAYzHU885eqLwi5GlYyPpzI__xkHt_MJN5PxqKQhwxcGVIpeLurkMUGJMFpx9SxPUYz4o2A2UwnVOgGnySn1aC7UX4-AS6JkIALI8tEUZlHaUCTj-PJ9koJbh9yQ0G91yn-3gcAz26VpholBP6T3M7Zrtn3xV5O3VODzGrZQhxLrrYLJw4Mmsm8fukNfBWqKu_p3KN0s68eSYyw0Cmt9Fsfwl4nEXBkQC14ONq4zz-UaCMjCik-L32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCURw633-WlvQx9xOc31kHHY_EvPjsjFNSPRcgCHUu9Vm-XwRQ4mVtGubITDcvfGQnvMVB69HPnaFWztPgwWpVQl_OLCBE34CISifKEZoY6qmH1gX5U8ZdeoUjifcszFePLA4LJKx7gmp3fmfqhmkpzmO2wUCYJILbX4pp0o5IylboAQdCqw7-NnVQ18jw1D0HIb0pPYFuRpYmFIxjF8GaLwrzbeNSazPT1njdR_RIxPEsgideHIt79gb8RzQW7TEjQz7axdRUilIYz9VpanE2p_rd7npuKOgss99ZG9wJXmZfIhqlIVWeBIZM6VXomudITwy1wV_HC4tPrz6kapug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8k3B03QqqFtgIuReTj6heX9bsKzpyWkqjTZLZuJXD-P0lJTti7fzkB0jjwv_27I0q3K5mcu8PeTcK-acs1uAOHbDNA8vgIoZHkK39RGtCbcHftH-sKOaQFJDv6Q7njPXhZojxdQd2K49ncXqsM3xbCywHNtRf0oOW_8JKZSyMHsHVI9gSKRILWbUwns5LmUOBtWbeTn0A2jUZTylJ5X40cW11A4Vjf6HjV7FYwpFTlRGVavcgOCDndgW-NH0GjF_pB2aFIgiDM6BWLjE0fAM1a8kp2KyZwzf1E3Cax1jiQjmVwuQey97Q56ubm5dnR3FDQbYsFeDlWTuHE3aOEIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKglPph_Frox4bUTgYoK2VPwXwOM_AQ4gVLoQ_pbKqo2HnvacDw_y1TEcNl5qmPO0TcaPc3mZWP28b6BEjJjh2EQ8ytbxR_-56VSk1N1rVLMG3itwmdlsEy3ywATlLnd8fdflYpT3c-aYpEzsY5hdp7XNkTjgZpejmI7pR0Q1G3Pq2UNQ-0fp_FBCEivSiaugNa1xlGMTyMztyyyNiv82Kx9sDLzr84Yj2guz3RfAaSNxVVhm03_CQdYcrQ-QETieFPBTYujjIkRkoMfLvlua84nawC8wqzzruD0abI9Hdv1jUD3CGYcK-MhvrX7b1ZEBmJOEh9ODk9_6PibTzudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ546SPYDOnPVAcGrMpIvSWB9jVjjFjh_mZ3y8YQMQDJP8xsZ-erETJdoiLRN2oKFmw6XCIIoubWu5_TYYq8Gk3gA_Ki05KlJNgiwj5vsrL6DHOgt4lE1IXtt-1bMOE-MgzpY1d9Pe3-icxjcl7dSY6tN6JFS69WZwgiWE7A0V7ESAcmF3G9uJMX_ISxqjGmoz2jV-YQqdpa9XBxYtdJx37p3C_cRlm7I_TedAMDZ7l_iddj1hAsZpyCDyoATIzT9iPj-BY9PJ2Abm8NOex7kCiPzTlEBBbQ4ninwedZs5vOCMV9MweHUBMaazvglvIiyMU3sYBQnZUBp5chdF48nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhe04G0qF0TAV3GymFjeMjTkKkSOgTDhY_THmQWPPh-x_DL3KrX5Lyvv5_hTIIJXOV0wikAAcFBF3rLu-IJwiWi_8l2HHCsX3WVgNUNbJYNHejtZHPEcrwU9bxiz4aQgr9CfH-iWK0v62LuEOzMnghxTEnUdVVb2HVJmj7Cf4D6aCczGqVQ7_JPVfgxA-jNzZxRN660YaIadnp2c4E3lEIUTi0rGD0wUREQtGR9QqNTlmfvczpEBsRGg6WLj_GE1j3JkDAJE79BLQXh76yymU_umRuNPRmvSrg9km0lSIVO7Kr1F7KneIE1zVGbEuCWS8_LjuwL5fsT_iVuCwFBFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv9niYtcIAT0CelmNIgBEtmUoVp3zMSGCJfyqa0GITBLe7vxnJw3VUCLKpOnKP4rAMazQptCVrB2NrTniD5hECfZYsNKawPEMeN8AuGOntdy-wK81D5_UqJicOgm87qWtkeDYzrTO235SAfDSN34mze_ehMJwgoymkEr2WoYX-wXRJ2WNzqJZ5WHSukVQc-s7YX5gez0TmHaQOi6nFi-miaBM7nMY3rwWdAUW98yHPwCXynsDMAa-uI37OH8WFBl_BMZiBWxVqgDxO9lb4rzybbxdIIza-eurt1Iy7ytYYuMuHfEmm1Fu-TspEmiDUPfkM4buVSOS2b2pv8k7RZKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIVOT-iQ9vo3vqbAO0Gw2DHHnS6FzcmmdbMLJdOtbJrObZHMmTMXxa3SYk7iL3opw3EjUHVf-JhRh7aebY9wz5FbQAOfntGv3zOmalKoJAcl1Y6tlmTizte0KnRx9s-RQN_5ohPC3NyFhj-WOC13yuo6_mSQ4WAW9j3pOis598suLSUktxq_FZBh278H0df6XrsRQ04zoPK8HZ-5bQ8FsAZ2vvPaC9GscUegFFA4QCZmyWsHTYpUen9AE62N7UuwEgzlIBq-4CDaOevaFQrdvNGNj-13BJKYnAy6-2mfsEj2UeV9U71ZBYtLnFJEyg4x9LnZb3JpO_skkvTJ3YuXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4X4rVzSepZ2dBxExb05esSqrKW333rk0dwBMOdQKv5rUw3fR-BgiXQNWxliwiSG_JD67hCZYDxwI7J1Gfj1xnjurT4ZDODs5Td_3iuvawCfGz0WUIrwrBKUnxE_9OHekuMdlZ_CpKyIVIjE2__a3HpbdDTaUN24fO6ZfEsrAM0NHv5Y7n6H0-NGKIR4vDnClr0aBccWqpStaNDFwIRYkD9UpU6p1v92kj4ZmJldPt7Q6qRsf8Z-pE1VUjbuAi8r0pPI93XrNlysiHKTMyH3fVHfoJX9gbMAEdNT-YQjt5uuYZlS8sycGfjQl4RARuhayG39VV7AmTteuGDleuXVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWr8lWHltcBk-Sdi_0ZKqoM9jyOSY6C7zQLmmQV3fYCPe80p4q7ChKQylFY_u1UWctjFsEx3KyFni4RY2xELslYIK-5HUJUFzvv6fEgailUynemUbSvCy1Q7jmKwK-eSkLprRpgQ7PZomrPQngHgWSU5ggf9kfcYUhg0Y0m4RTqHPKKuciJlsKZUSB0XhjzxAPMMpBH4P5FKsYbbymVszkQGYZ3QsN85EdK5NBii0hZKZIY5t0uvNUKlAVpzrI96FUlyszrk8cTnStkomcBaKEuuHywSEFkH-WfLqsCfQoPPfrOkJKE6jR7qFoQ71qCfCFyL9BvqNjp8twnV5MoYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRQrDiZA82UijXoe2A8OT-2Q33DnMMw5-yhUapnRHSF1esatPyJCSLPjmfcAKC72kpcAF1qDBnAq3O9Jy_-v9oTR_tgZIeIxuD-O6QVji8hq6tXJ5bUbXfGrZkw1kELiMbKmiTPBY2Y1TxWcuiHBgV128mhjgO5uItscDwqgASWs9Y3My6IBi_v8PJe-Sv6r0KqH6iV2I3ZHAB-WurxBjChvEYr1YvbI5WHANIAh5cgbh8uKsuLIq0eWNL7G89mUTHAN_PMH5JGuXFCO-FzltGYkY4d5GlITM82jTT54tI5yhA0weKqD0zqKAvEK10lecIJDNSAs8V_XWpgkMdp73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifffpWl9jdiw7hJ9GW5ijKPr0NOn4D3bEg1N5x5DPNz6-Kid8UmhdQD7f3jEk9tN8kpm3NltfFEOfer6MKkU5y9gTW_7gex2l7wXzS2ZhUqKxfWi_ETXFCZLvPZtuujiEjNtkzx0JHmbRvmiLtmqy-RpYF8mmucQeI60rO8r-UFD965iVn8AVpP79B0YE1MxOMyJkTqbxolGBqVLWxcplxrHolmV5CjSjY1B9fJkz0qr-WBkrhyqqNJh_emhsRayCUAUc8-UjoAnYEk6-sMm3agy9b1lMP0xlhLlNl4vBLYwuDX-cxldE_dO9I2b-QdRpU1J4N_a-0tYv1pkV8wZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kse_yNLF36XzjYJFL_WAHOyTwJ7_XNzq0p4wVpxNWvtWh8uSZRsJrRAteHIeQX8-s043rAFQLPVxJPZ2I9g_SnnipbvS-Dh3VFH9L8AAVL4vGobB5F33fCojHjXEN29LlX2Rt6FTq7_FOT7eIBB3ShAAuv_ZlCz0vfa0pyohqfTbDe0M8iX_4yZvUhM8XCia0VVNsLnSDbsSR_AI6idiObCTMUSxFd0lDTz56O6f9IM2TPgwyHpC_TvzCeS4t8ulkWeVIYgsibzcay6RDSDf8xD8CkZfIEgbiyLQvq3q87Kbn8kVqcMukqY5D84-6-Y4lEObHyUdJ-96wF-Ha0MYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUTfOvnFkTLPywQmGDSUf1pVaM1u3zGQkjuB7PFMMDQAGB9o6VkHwnJ5ujZAWAIAAMvf3-kOfW7UE3nvAIQlCJAdKMw23bE14nfSrGGYXjAL_NSll8012SxYvEA02NwiOQ-JVZCPh_21FgEEFHpr-fkWHrmW4tK9G_ub9JnVllNI3rvuQDgAJ6oBETYa57DSLulxQ1JBrtbM6WPCz9CeXc6li-3uBkixPljNOOJ9MBPOa3gR-cY_CgI6Q8OBSN-2GRWFLprLQyS5xjkW1sdx8hfehwwJUeD1Pm7Sy_nTYRaiuJ0cSC2xD0r3PpTixH9GB7FtWS265BQGNDffe1__cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7H49ui8FRuVPj-5KWhNrAPHst3D64s1fULPP4PYpFQVF0IUCHTJUor0dUj-ltbjj-nwU6nyv-U_B2StxHJOeNV3UOcIq1f6UXR3ofcflwWrbLQsmxxx2fHa5beAjL4JkSX3BJvFEp6xWgYdoJpbe6GVC1SW43ym-U0yO5atAv0xe7cONHDb1qUvCx6B0tnzA9NG-D_-sMqXqM9r6cUx66MVmeR6gR4lAxTgV3rAVY4bW6A_MuoqHiu-ARlNX6IAckp6lWamc9UKncYXxdv2knFN1LuId5yesAxIfmcpZ1ER-LDR8ozqsCUMsbAjqvtYV7NTq4unC5s1Tb3ZnnAQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIE8rpxARz_sxZ6RqP9pHlVqV0z6hbu0F4zurukpGG49FxmX7805zSpS4-udprDMcssgTqX8RaBfR-2UMdO0Vbb477LoNfaNSNP_i-QnsocjJUhjyWKzQ5DkBAouUEw2vNuZigUWcJyb7AWyXnu1yoG8Cnm4g8ISRL7nHp5IzAeUo7yRXM0ZzzH5U2soiWoK9P5bRdzyEbIb2KJmw-WeRDxMM-RO5EBNBr4-0yjeEycCv1xD4nW9pPNgnZ_I4rI9yEJQII9qq5cSCgR-4_k9_jGAbWsP2P44AvoN5yEORlNr0MFNdnWDp86mSPrlBzorhwyMIchkDZQa2780Sn2siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-ftiJ62RZIauVhJ770IWQjrJ-yLZvArRXvj-EB0xQtC7aPCfpvn0ibP8ISkmuAt8ic9LRBYyd4tDEmdDVawEOi1MSOMvREzsQU-fLnG1tGaDyOEwwSzMg5r9rvFQHRiA70oWnQk-HfFdvZCnWouCvQGpkrDUe0_iMlCAkZ3Xd_6XbvekURJBrn1JnXsPzbg94z_1nKci_0fXxmBGGiKRmDKNDH7wzfOKLutE9s3M0qxWXTS2CepJzLBf8ck286WX4EJWS7EtoZKWbJER2hXLU-_snd9C0NngBV4EOH5tmD0EWRIqofg68181pVFcx8T5WqI9G50UnBykNW4xUAqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rysKxa1OjS2WKcsrROaYQX63F4hz9v_aNsuoDJ8kXo0wsu-n2tC_8UtlE3cYZ88WY_O_-C2XgHvKhJl5cyq3N2R3HfFH9BdNKcFB-eBxf3jvwpNOvuav-T34odlqaJ8Vc6fLqkjzDymaBp8U9iC0hLXpMtZyK6VZLRWNDNtZ1APJ52kDglxVJsN4ava_BhHPAo2eK7SddsX3abSEVM7DFVhD4YzndAKAYVSwP020mTkd2YpjcyyfEKnrx1AvlhiFsvtbBxDBMmhrkoEA6cK_Gf4gX_xtFvDa3ZSSFszh-ewzmmowN-OArmJaUiai3h6Vq-TvB75sy6XcMEm_RQPE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMjr5eLvA8oxXBhgIf8IFJkq84511DFYB3XFZh77bpOAucH_e-D5jnNHBBJtpzWaAgnX92ZeLinFLuSMZTgG_KaBb-piPH21GEJJEtTb72BpVsBXwRoIn7UVKCNN93uxVToc10pwadHwc7hwOP9aOELb2GMHwZeu444wVYQTPRctDBusO8TaAmx_m1ImEVVq56wsmm5ElSzMWpWRfU6dj_069wl6-IVGNQCK3_24LXUGd8M_83cny_RqVm159KWGnYet_z2K3lNFyjniMOVA0fEyB7ie0Nt3dqwAlw5LCtUnb-GiXib-8uCI2LjiSOhJRKyDJwMCgUV4ZftbYoC8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaejUpb6dGN6MGXKPHZyB1qUK8PDdVrGEN6DZLlDl9Gg-aXoifFPKk7A2W_m-kUlLgaQzN54pqt-h3vVWgXZPU8WfxyMN7RRyfUu8YKnP2DEnOp1CApgrqhq3seEWnG-WKbQA1MMOzcDnMdjSNrZBy8zs-YKxOlu7oGhHKlWbG3P-TrlGBj3s7ZRpv2af_B8gH2TUhFwhkmZjKaO_GMMMBdwZ65fDsjSomdmEULijl86p5o895QC1bYFuIWsWKdpmUQGf8o-4zb-UlKK11y02vkyOf6Ve6yzocMH4J68KK9jHU6HSK2o_RXuXuuRLGVKkHAPpFBit4DNe-L8-zTiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8GVhOSdFeK4MDsbxZaPicyEloCHfdTY7gczJTPjeb_bWbcg-NwYaZZDl_gWWU6AxHwFrzi_sZXvSrFxP7ywjGhSu9KTSdUG6pHDJcMN2wtdf5xqKXRTgECHPrD93MisywFuLlcjbmYLIurC6OnHviClM-f2KUKoOTNNegN93dDoIYKTORejRXv7pXSKBEC8Utbs6wjuXo0ITl-BBbcIdbAqstkZX2A8hZSn07L3hIs_mg8-ArTj2Ub6278pXUIj7rUt1dMSahbolMVna-uCvNP-vH13d16zqmEToOoHlO6VFnAJxjLNtAlgwjPcapDYSvXJoT54XIZC4PT6piom5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvlYqW9_p0TaXmkqDuvY0opG9V1KieWMY6DGvxy3wMeoRLZV6I1klSS2pqxUQQSRnbsgxDggpwC6xqT61xCHQoifPIWxqoAUWBGcEFQzDZ9SYoOZM2oliEgxhZmN-jnFrvfYEb6uPuNfcFfJONSv15OKxeF1LShqBkfiHD8MmkEq3TxNoyw6mVbegfEGTZbpVao7GWu13p_XcLPTBG3vsTgDVPuID7J0yRdITlxLRcAd4t37n5UdDnlXVGbzs0iw8FQ035QJG2Dm085ej-PcwJVq8Aje3n5XJEnPfO5G14rjJ_Y6MWK1AEZKnideOkcnvxtDXOsISWo4YYyIFEVaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcEmHpz0tH0w_RIljwOnZsDxe0gOhvgQ3NRSPkBskcfGq4-eYJfKxm2P-56bUgEonx155W4SEY7mBzESypcAtAS4u3WzazULfUQcZuzIjtGuNwTtFiq6frgrjF3pQKCgdOnWX2Yci87ccwjTZ01wOL0yJ0BvuN3LEvFNOyanSfsnkURQPzt1ZBt_Sn6Nuo1WaSKMILb_M_l-JsaeH2wKGNEXvr10nGOZr1Y9hxSEYHo8WT1T3Agx1xXXa41xPb24IoiGib5IBHJkpZ064ykJp_IAfDTWL-1zmc8S-CYgpNoUHoil9JvXlhVUkEcjpJJI8qyITK_Ck58LSLEd1Z8yUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVeTVbcsA8RDdmj04iytq8X_JgMbzGelXB2t6JE8DSmHpArH7rEFN66cUo_GjYEQLvMPPPKpvpTEvP3-vwgnzjc2XPzYGEaOZbIZ5oA5oRYvTGiT0CrNo97gIvZn-ShZo9h3CkK6pQuxjuOq_cJmFcOiojEabPJMwsXjz_98SAxyxEUXDnYB9W57rWGcmmYRcYUnlAwI4wHDvFC22x1yEpAId3OfXsrnDocnWgyReYsOag48Cfn37ZHL9vWtyoLsSkrs-Q4BAYx_O0tTX94VPoKPNfixhMNUOBDYbSJsDfgmoguwf311qXhc_GLXkZjmw28RL8Fw-toAtbKPneLpgg.jpg" alt="photo" loading="lazy"/></div>
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
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZFlAm7WHxAJVL78P6cvSD5JfzlRwTdZuC6dzZlRjnftJP2L5mLrcWDXztFHFjPqeUgVeK1fb11iSHSWCpk9t2Yp9XOQqNgEzGZRxy_UzXCvla6ioXtKj9gu5gHcNpcY5ePSSs3hLGA0FxkBPn2RbsbUOWuE3Rx0jIUzqOjeVW8JSPFEmp5BNVhXe7Igxsfbj0ua4ttzZCexwGHXKCE7KbvmS8ucL5k02oayxEK738CEV3tJuaESH8yxKVTrbVHxU1HqlywH4soGk92pGJteXd8Baji9RIi-CX-c24Tay_z3tft7WlabUm_3AoxA_DWe_0P2_Ay5fJWOkr2xNBihmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlvhUQPNVC7i8JJvRIwXc1mzkU9b46aySBg1FZ1-nIV5ufI7prH00wn8313_gNubs1pGs2DDZiZhwg7xYwmd0mvn5Y9rCeYpSBp7c5mXoHnfx77-Owknw0_SkkCpMChj6gH-tgrfGFqV8PAIhkCV3_gJF4XY9hHdn83MqPikRLrclZF_xhxE3X5h_Tx-rTfF2xt4pah6aCS4N2mxpSrlbiFG3HG9cBM5xwPNx_nh5YOc--uOq4C-xtoSNdcs7i0cnSepqyG2DE_klyZc7LmA4RHSClvngBFravTRmhT3RNAXMZWzjblmSQdOx8otcaCuNO17IPIGaEpydIRYV1wS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=jHvzwa4gaBC4cfD5f1i3i2abtSjtn8AQXcxjfrhynoPA9f5EJhFWpo4UyiUDjzNVP0ktyrAonS_rgLf74JBOx8Katmr4lwNbchwIpRW1LJJ8TNiZaiZr83Q5dRLfu1UBqoY3hskNEsnBb9vD9s4R6ia3982GW7HjZN9x4VKVibtDQkvxs8dBRW0F_QWuwp6Ln8Jdzj6RLVOQwKnnJE__tLYKZM-WhPtCX_V-vV9iXYFL4OBSGYW7Q9AlTlIZLLQFsXoBywPOf_8KM35U9rm3WBoF90pVct4g4C_rc1ZtYgLHoaEhAsOvm1BSQUMe2RtZRccP77DRpOvpmA9r-wlVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=jHvzwa4gaBC4cfD5f1i3i2abtSjtn8AQXcxjfrhynoPA9f5EJhFWpo4UyiUDjzNVP0ktyrAonS_rgLf74JBOx8Katmr4lwNbchwIpRW1LJJ8TNiZaiZr83Q5dRLfu1UBqoY3hskNEsnBb9vD9s4R6ia3982GW7HjZN9x4VKVibtDQkvxs8dBRW0F_QWuwp6Ln8Jdzj6RLVOQwKnnJE__tLYKZM-WhPtCX_V-vV9iXYFL4OBSGYW7Q9AlTlIZLLQFsXoBywPOf_8KM35U9rm3WBoF90pVct4g4C_rc1ZtYgLHoaEhAsOvm1BSQUMe2RtZRccP77DRpOvpmA9r-wlVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htb8Bwp_lYgwWfCvZ7Szmu9MR84RcMVyxV1CC_Aae2E0x_jfdxe7q43rWEbpOzTyWZoT1cZgcjquxL4wWfoieaD5sGpQXGua29I_E8aZednSJFGVgfx8NAt8HjvW2oNJDlCx-Xtf7I_DhV5ayTVgCTau-1FMyKphfnKExAYdaoJLVr4VwJC2ek2T0LjlKSK4uK2rfw1AAZF1yWF0gvrrOEWTGMaFNtrqGBpZwFde93xlAwqtwkZwXoaHmzK-isrUdFMQvvHyuKqiquKnw5k44fXhylnSb4mtdZRQMQAIBTSbi0VwPxcSnCpOwobpstMBvYObDOiGSLMwd_SoUJK74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJZSuyqq7Dp9zOnzyhMVZVjaaMKGh0iXXzol6Vhy57T_GKWfGYjBe2LKO1QkwVCO3ZOlUZYjb-lDZ8J815aEjYYXxNTCvu_XzfxXlvB783T0b-bxqtMigP2xjgOOqW9iev9ZRCCL4wJVf9sS0pP3YOXkA1i1HUVssa0Z3pSk2B77WQghZipsbxz0hEzSBJtzGNimxSUKtyyWks3IIMLRvjPkK2IOueUAMXhK3T82PIDJ6YVJd0nNSRgKa6QMcArU7nXECl7zg8gDambUVDK6INTcWUcGRmtjkr1Yfol-o5V2ih83M1_AbTPoDbeU3eul-WB1ZVN9uPePfRTiykzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4JuJpHThGoSTFycDxpQ7KQPEYh2Jo19m6mYIF26ep6CJRcDOFWnoafQq4X3C8TMWUT7_abQLMs5S9Vwgl5dy8r50k5SBQRqcv83HsUS0KXo_2YbX0vulfaW2kp0csw22dQo0iTpxB9y6QaDmOg6CkqBBSTXLUS7SF2BruIZKUDG3jrp_GJx9nPY1CqK87YW8SsHp4dQd-Rkrswx_bopYxiTPHsU7CW4ijo3hADP8X-J0Uw3fwYMfgpP6OWdniFyz4lCJvGElEBYIQa0Q4fv0RZVNjB0S9qxsnVVLe1H9GAm_QGYyosadkTy4daIegcU-dCUXehmYkdworSLglGmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHKEZ8NxZoGW3QnWXjZqo6CCvQi5SVVHA3KDsn66M4lHnqh6pxUwyrRROBfArPRviU08LCloIqekmwJSq99F6JTR_6BQ7DwfUyhbgQ9LD4Q2C8OcFHY1wWbMyHybJpr-RyJySH0wwFlfD6f4EXRt14NWb8GdS42lEayiJj57BSvkQUs4TFqgGyBoNynHerV2qQ6Mvm8GN-XdB6pRMzY0bozv6Kwmjx9LJzFS6pj_7hrsERi2-qQSgsFR2TMzy7jBEEJQve6dTALUUyv8yF_gaSU5stFnUdIpyxsGEguRnb5mKmjtER4eGohcLR6otqtPbLcA600JjtOaXtfy1MbogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezKcZQHARgEqOJbjKUSmkPtl8Ws0LWB7EAMe5bZJZGzYiuw7LG2Dda82jEUZE8njkaC0VVAFJo4sdqZgZEL6pFGV4UbXegrMUB03em-lsFGHYVEJB9xGKGHTRx0ZNYmbk94oAaxcOXgo3rcjRuIVIXutlN95zAjGsjiShgvJq9Hr9weHr1YwpWxJY6nfGpaXh7t49mGDnaV3qyv_7OJ2ttXEz20FRjcgd9NlqAludXOAxf40v8OfgVf3jDpNIp016SeSOCZlu6drwZQuUSNQF9NzH81Q1eBC8G-h5AOgMUir5SDOxVPNsWcrQxC0cbDrpvLdeZVs8zzyUWJsD8sj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcW-teLqt50E8bh_kF9zC9Q1TAY461eB6Rpz6dKJABUV74cjWXclKUmqOof_rv1OpohXu3NpsBWc6e4jRpZZDkI1yCB-3WY6dg-XR8fdYSS1Nv0LTlSVLevqR6OcMS3tkRyCRy7HwFasNMOYC4uqk_J8pZyQ-Z7KOBnjr7_dbkgdtoqNPzc-Mjxx1O4MelTS2E3hN8-gswwzQBzvZw0yJj2ckkevqYchPBlPthi5kOXNDv9CB_gszqhC4igS-UmPrpF5Tw9YVb3B8fMB09LjJl_ZLV-SJcfa4lhbcy7fT7Cvjgibwk7f0NsV9OwjuzOnkKMrsKc-HBgPlhVJ2csw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfsw9It4al4XtqNb3o--jkxio7IcFJrKI4kvnZ6RmM57isnbmf_-QeLvvpXj3MVpHKXozZ4hnXp5IRIfSA6cDjk8pPYE43i0eJAphwHDOV_4sxKKy-WEqXl7hJTj6ghJ9dvWj5wDKp_ozWkcw3iY9becbp4oVJ4lqQl_qJbr02nF6-q1nTVE-UbYm-MgzDcDsnSXAFo-Vi70_GyP714cPFXLXiC4TLTNf827-3U9t1Luj5w7_WjpgU1mDN8pkF19rQizA-UjFuDqVFCWr2ZaPHqiWYiOayJbNg6cuYepYH1OwGnE5rwJcpZ1gpQcctmUgrz572qPBF2X3_YVWAm9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu4AXcp_ZmDyGzlys88FshtwI1bORZRO283KPrNPX20Iclkc6R3LE2GdMjz2i2biuDwi2AW3nbiVgfNODRR5D8Ku0nFqYhtlYKqhbpwaSOWYH2H1YKaC0H090EFvTZnD6jNibO9p7RvvLazqudeQr4-0_sZ5INSY34_PYF2WPzpAuT0_D6QgXBQQk3ZQWVIOjzVbRuQRWyoJ8qXyAcXds2qwcBFKf7Cbko4EbFzRUlN6SOG_jImkFc05piCuCXMOzVd_No-xqtqtmK5bCpy7CyPLMy6XQVRPg8w12zRlYLSVeLKM7zdk4X3BLE80MH1vWw81bmFncDMmzGWe6MGIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwO7SlXpICC0iiiLq65jCQilMdWIlaeiqNCdssDRHQpjQF5Oo2etzD_8Vyxp39DHm26pcxTu5k2yougP8lvzibJwNTmTdG1Bj-iKjrrIoBquplsvFq8VJ_pq3jYkS1Am9pqQX7hQ5ho5rYZvfWBDXvtds1oXGKxKHaN2IsiYIFohe_QI4x3vU7k6NenmPhPCkAgWj6QJBGorqLnCEdfDoMDHx7DAedtTAEYpgZCkGKHBXyyBNSBvg-sg8GClM6K1EmhEltQn1Og580xgioXc0ybG8T-ONTmWtgFNZ5j27n24r6a446IiliYFg1Z1r5353y-E8cCsa7N5g2_JQlv7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4CE6Vq9DUS5u4LpAgT_2_jZEH2xfxtpCRTK_2Zdjr19FkAiOhmMOX7jEtp9rEoarTUlmY_JQuw7Q3x7gJx1savFsn63Kye50hBYCK3dwTxMgs0qp1z2oKh6sokvneEaJPPG4nP8ilJND7DOHzEos1_NI6c33xYo5yaCqVbndt-yq4bkFgMLl8XtiKXHpmNnjmRHBOaeLk2dDsk_mLbr8-UgbG9Pt_YURd_xgzjz7DmM2ZOdrvOx4vvd9hdF4wh76Gb3bWa84Zbr8Bca2wp9EC2XICVWGnhVZeMgWWp2ETH8TvdQf8pOBDsA1PmCgg2oK-NXC7Vk8Vkh8A4n8ol-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMJ33sEN-uhKasG5I81xAWK3oRGmLmtrr4czyO_tF6tw18RtiyAtG_sPk0NpLamII4s2nf9aUg64jy8RR-w1UB-q7QrEqrHOsfvDcLcCL3vzS8Q8Kv91agAh1lLktUMJQIHbZ9J0E2vv7O43qIlPqMWcRoV0jSxNXbjKo1SH4QqNnt9UzDuCJq4b12TvI82FxUPWgZjhZL-PIx33hqDLZOKgR4Sy7V_6jAeiqk4gIo7gRffkeZNfs9CD-7yAOkCEqUUxnhZJi0wyLk9aiGR1VW4hAmGs9C3C2pkDS7pByvrOatBOkPthR5KGHcUzyg5yGSciFUiTKjRzFfxoctisxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=l2Et5ol1xujMi3rTXTNYA7UGzddD6nDNZP1WZkTTPK_G6e5HakgUpsISlXotJk8_Lfl9FffZFbw7CXf_oSUP7_3qW2_8htv9t3wCXChpZB-L-yrl3OXHpXZsZBa8ABGA0x5hp7EF6B6An4RIA5j67zFnlCvLsP1loVuJc7QVmJsQlPRsK9QAL-_dlfqpSKivsU6y4gROxkwC5IkYSWGmnIKNLVBYZpRPzeeGbiwuMa4p3Kn0hUegnZv-Q8M7C8f1piCGDXn11YMPq3Lm76Af5l-GoQl9Hv92asj5bYyjAXtQn1-egsTmaNaGQjmkUQvEjNz_YwA4SPO7CjR7tda1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=l2Et5ol1xujMi3rTXTNYA7UGzddD6nDNZP1WZkTTPK_G6e5HakgUpsISlXotJk8_Lfl9FffZFbw7CXf_oSUP7_3qW2_8htv9t3wCXChpZB-L-yrl3OXHpXZsZBa8ABGA0x5hp7EF6B6An4RIA5j67zFnlCvLsP1loVuJc7QVmJsQlPRsK9QAL-_dlfqpSKivsU6y4gROxkwC5IkYSWGmnIKNLVBYZpRPzeeGbiwuMa4p3Kn0hUegnZv-Q8M7C8f1piCGDXn11YMPq3Lm76Af5l-GoQl9Hv92asj5bYyjAXtQn1-egsTmaNaGQjmkUQvEjNz_YwA4SPO7CjR7tda1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc8kHtJwY0CujrTq6cFIteHF2hNh_cmDQKuczOig8Wus_o8GuPa9rFiq6wbctKSPw5EvNfy4z8Ce2fktidweku72xlsk8uy-qBZSrmpgHtOzc26US9hN2hyCaazRqAuo0iotuh6ubDHbvaAOuVvocPPdlz8iwMUKZ4swkR2Li43H3aj3WHV9oGbazRvf4mx5u0neZPgkGijrpv1gE-toVFciWpsMBFboav8mLpxjib6OSq74rkNGoBkR2S3DiQGHFRAZAwGA1kOmDmLLqU_LaPJkbQe61zj41Z09iGHzIVkWxq94_y-4kbT8lJRfJlgINasvYSh6gekoRNT0dLU4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMS9bOXUWYNurAwG4bV9nhSaC6N-SLaq1hSpRjJ_wju3HtZYxbYwn0DuBSqr2FgK7ZZ5XIa3MqMdxgecr7Lh-bL4l_w6dekcfX3_01VdjQLamApqBXRauTR0ap2bYhj8wjjZO5PaN0CS2CipG8A0yyzCwdnJomaYedl0B5DbN2V1XTlKmYGTS-sk5ikvxh6Utf6FPrYvHaxE4X5i2lI1e2jl54EcYcY7sAvNGt7OlFBcc9QirELFJ3Ntxr8A9GDThr0CgEucMLAeW92BJY8fSK8pGBNbUqEWoyekbcivTCUHAH2N_sGWxQvcDCw6AhunyvnnGr1Q1bqy0vClrmNWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao7e2J-3qIHbh7Yixv42m_8cCkBH5ELhSonNyTWXaX97kawHFVHxZ5TnDpLNsNlzN0Y3WgEYx7Q01LYL0X-aLIy49KYNI3WTOKZVjn2hXNfMK4Md4yhV9bz4aZ-cwcYc_POSV1Yvs78pfvGT3pQF-o9mq2yPZHI5evBmjCARDqOf5u8EZcMakSH1VtkMqaw_PVSeknm7AXUBZalnDYKOEzrOJZEKgmrLXFcxN0oXNXrLM673X0IYH8AD_YgQg7qM0s-P15tL2yglzoyUSfWWwO0DcEypCp7_MqhtmPDq3bQwk1zL-wE0EQ2INF0njIbdFqYkiVyMLpKX8VNy8E82sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
