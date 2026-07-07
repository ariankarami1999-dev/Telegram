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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl2qsNJMBs8emrfkYcGMhJ9wrHiqMbZx3icni5rp3jNyGpQ5hH6kAIffqwGfv28Y2gjWrwxwHUzUbvSt5iJdg8_w0zAAV29Dnd5Wg-d0cByGTNocieR8zHntDksgf-t1mdbKbrbIYV8qqYhaNthKaVXeP3vgdZOoNflJ2jtRCcEOB-GIEYL90vucCLvflcWYdHEEKyxvmcbrueInzzlFra_5W_6v-iKhojGpXH1H7hbuU_IQVjqXwE6I1KWZxfAmeu-sPQOsf6FEXhadp8y16FeuU0ZzVSnMWN0gHEKy5phXctzZGzYwAOuKFU1zVIucty2mzaa6GMqUc_rmx71G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uMJDpNcrN5UrvSH0vtkH56DQgz8woy06T0b0S6aR4tyMJV6SX2p_lfSGKTt3KHK9rw4PA9DiS7XXb3ucQDP5ss7I6HiECuz0Rar-S0dkdMU-vezyUei29eCh-V6pcb1hFfPtnpveJ4trm952Cs0ABwPVgBdTXLGbb4xb09cQzVDi9_kv6XpFVjJyBufkGBzgh13g0qxRw8-_52ToVx6_G3lt1DtVPefRSa02hN6kubA2aAoLsyYeotfZB45oUP24xznDYwDrFZ39rYiqFotDnEUWSGZI1hxtl8P5UaIkF5VHt4eCdgBgR-QiSX9mRunddpU_EYRBuAD0-hz17WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZGZ64jq6wTdRMfItnMveCJO0vhXo-n1FqBteDytEKd9R0cRJL_0V90h3sqNv1CWdHl6c6vOQ48sghVe7_2tuITDvkmoMMjxMIvctHLqhwwFSIVCntQVBXfso3cQSKRQumF7f-iZ6jyDAzb8rsh3qOtuI4SytIx3MG7ggLI3H42UZ_JgODgbUyxYFueC8rJ_yariBWMv1N6-xxrAIGvyYzRIZNRaR3ds1dGmft9HLCCMdUkCvMjAI_Us1rekNuXs-u7VFUqsuwE-uNXTwY4ToyWt4uD4vUlCZVtu7NVJCfHXqPiyTqFHnBrtmPMJvb2O9sNg2_4L-4vYKrb9dCQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EevuH8qBf3x2t_6cCO5UJ5AgG2CtfBzYhNfRuvteBF7b2Bv5QMik29hYBA_AfI83-RA8nNmBlxc1iookMdgfHFTR9EOIVG9r1skijaLRyxiDXbkm0Pw3yT_0g-cf7tmsO-SP9HN8KnTcKme9aR1IKQPQ6rdqRSqYBCI2aYOIy1e_o8zKcpYOAqU18lRqXPqrLPmlnSS8FpuYjEtNOwxbwLgY2o-QyBGxEBS8lKPYkmw523lMywQicJuMhP0jSVProFzAhYn42aeIF58TnBQw0Lu7IiBBcVTRF-Qgd1yLlyB0JTXY0QKF5hclqI-tkBT7NyVOX-wFberEX6JSjorZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ7TlaiiKyG2ckC_ZgcD4Aek-109X4wCBjEJEF9O7rAx3omoYxAnfBhcNBzjVhtH-NEbeCVSkGqWK2X9dbc6a29riYqe0-WLSfGbBSjf4IXoIS1wwVwvtmJP-yYiKGWzdPCAxGj-vnwoV1uiqsBf7jmirvkVCpBGAU4xS8NnKqWZHdr9Wb0_Pp-Y4uRwWiOWT2iqfYXMmd56wW-ez8FRPDNeUN4KsIQtXdoxEhN9a7S2vN2FL2-jG62K_Qj0UaFSWTYNItzTDlBxpnV9P6nm7k5CTxf9RRPzrmiZxz3jdhqswmya96Y2GIL0HYaAU9bpI-S99MYY877wNz0nrSQytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB-y4QwN3W3inBpLygUDncdWTiZNk-Fst2AHCE6rUdOsQi5iWOV9xwuUOG8IUxylolOAjOCA3wbqgCH7j1QtCD5PR8jduoVhyrJz1YKPiGiqr1fUU-MzIZRWwT17bLdtCX9a6_zh93MyNUUEb1EppAZr2J_zVfFf_1c0bEBK8H-rVKLJ_URK2eiZ6FPFegUdRjUDyVcC25rMQ7up5zgwmlDcm5Xzch440oaEq91fjNexs75BO_I7bTUR4Y4gXkANolvRGN40-VpbiwYWO4bWLk4FKbqHwvtEsfV0hgtqe19rqqBcIW-jJKGh9LdN0QIAOREIodAMhIvPsmOsog3Trg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyDeGUTAgeSvXlsqqP1762C7XozoPjbg79NUcS9eAzdgBehXp27BAxNlZ07ha_J_o0ToooSvGrmp6f4_v8FmkkXo6YcWoIGHoA0EfpwP7eq_dvEC-WJ9S6XtHV50FbBv-LKc1fF5b2heiSgu8xitZ4rmsgyK1ku8XPAR4bkReEIn84TPGbWjhZPpvx-Q3hYn_lMRp2lWEkJwZ-OYnWgqDnXCaz-dz_hgpLVnxn6qf0_Baethe3jcwDEDrZ34vlQXj_0DBM5D6ifb-UzRGt5YedV7Fr_Qj5l50By57SD0nF0BseSbhE_at0RkXQtZLDISFitTqmYBzdD4mAjn5IMCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBMyirs-eJR9rAec7KbmUtMjj5t-4TaXBGecmAd8S3aQdYENueQuTNF-TENTrsDoSnoKpMohFdmGL227Naf4zFHDrPtoPD4ckKaXueSINVl41EO_d0QTSwPz1mccI4YE_OTjHYHVxa-nvmz-yv3uBejeks5mEKKdj1osrp8vtgYNtmwhSnGQubBdLcFfgAgXBVPN3nXmOcH4_oQlxynbGSPJJOK7gzQryGv2OOzjlTb8AdV9a8NFsOB3lfUL8jB27-JPKZk6xhzDSufOjuvYIG12FZXzS54XA5K00bns_h3cJhhNx0NQ84nntwZ-M8FS5crw3LLRxKPJFtH_ukCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl8xIxNC0Lkx4rcE6oSu-QJ5LLI_AfT3qYmfX3ek38cRjmw7rZGmPdSSrF4w7XTASGnjPXtoWA0oYaUjrZ3FyfIGKHQGSZkxUHoDTZpkRIpGfFDR_gM5ABo3U0x6P4EXHNPENAxPl5jksZz3V_C2aJEoat2LgaOdzbc0Tl9opMK5no7zS-32dSBY_eG_tY_jeqxrTk6Rev345FHxJfA0GgI4wxBv5iBL6fGsRHq86Rsj5xcuRZ50olCQ6LywRvh6R5rIz24RdF5V3YHNlRGQIPfPIAQQSi8WR2chVxfWXRTSRsHPkshaebTg79rgyqH6QQJ9IerTe7EV7RWsXUq5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5loZ70G-xM_A9SqhA2H1OeTDXJBMSDTuKZzd6kI4uQC_PHEu5FT8mVQJADKRFbimzfWn5oVCDCxQhSfpdIkrJKKXyT_UoXKQr_G7ajth424F2kVKm62wde5ruO1DsMiHKRvNWGPOq9g7ENCsaVcYv7inL50G5a40L95k80nRm5lJswdyzRqkePuXgMyXLydz5wO5hHzSwYn9E0PQPR34Rdu-TllFUxOfGxj8_IdMDBbT0v6w46mwyNPr0AD1nygJQn30iNNrZaDDtUc6-bPlmdxoHedgZyOgbkLPFIpIw7_I1OWosYkAsT0FBwit8Ah_c5SNpzbrZr7VD9ikO6V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci2eRtTDgwz7OeCC45fuXPSNc99vpNUQXfUSivEYHMENorscxIGw5ya3YY_xEBQQSQQoI_22_mRKq3OSozJWJCPIj3jzOM4d5o-GA7gTFFv5WOmmleFWOYREHjBEp2_sE1w98EGfhXU8_gh7oypDq8wG58GA_PkjUDEc4VxtKYJM9QtDlrStu7Xs1wcxLgfp6ralCGlv6x8-Kayp3s5PipZHBq3EpIHTKhpmOYZz4kid-QtsYaIFfxndkkc89hgtqgMUZPCgmbOT6fsTPxrscfA3z-MenCAJbUQyXZrPcBaQ1ALplBS30yQyLjWfuna_3y8RlYnL5QFHOUJwLDeifA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWMJjmWZ81wNp4-z16n86RmAfbDKMsVTlIpJg3nGKmZWzniW6noasm9cblYDdjfe8CWkWSX6fgGM2gZCCBhaPWRF1ZPV3olnyYQ5OJOX0zRi0z8I_M9S_LhqFApNtZV1IYUx4GKUNsqNChhgVEnMVImMryw-olRX8UbwNIq7Ppzz723ZjiLa25COi85YAhM88vG_x8QngDu4rOrhjk-WKB-Er6SwLad5fCpFOpYk9Kre5f3hIF8_PabxLfSq0Mg9BdHR4qCNDxnD7LRcAWe9490h8Zsf2_6nC6q1f_GrEm2l3FxNH4sJQWxP7-zTXM5cMhkZH-By9gLssSOOVoNVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6llFZw3zUjIeNr8UWLqwyOF2pFtxvWq6aFhfaatReuGhMOrA1kRwdsDv5YC1b_iPc4eJy5rEu4vdqJt9vGwfCl8od4zJL1OlK53_1sDPFPd3CliR7l28sPIe3IBYR9_6K7R-e7Vdk2ka71GVLpejMLJFk2B6XG0rW1Tymht7bN8XY-vWEbAR2PXZ0bWmIx6e52MB0h05BBofSNF3Vs_68YNa7NZ4Y4t0p6YQhqVv34sY1DFsFE2Jwd3B16psYTvYHktlN9LPLPKr3fV9vGNkFFR1910NxJhdJ9oYV6S_Lt20xswAj7ZIS8h2UtN95wlaz0M1Zrt7VqOQAmwra4o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVINSLVCnHlNkyS10b-Dyax2lbwdmq1uZIu4bXFJsY4lx45lk2tck7HGjQHwY-5j1D4Ka5gaSzKE-veizqLPtWKFewo26JASwzkBX1gBQ21xeXq5SjLssFka1Suld38gwTUJasq4H0yYN4UMqrNQHBncuTRmmOo2QEZMjjAHHyeRHJ28v3jlaTyWH4k6qdBVedgej3yGd7pn4yzwyFZHSoKFzMHx2c_m2l7J564V_fuMWszyDLebZnKH974mI08idhnN2CG18ukCWdqvJ9iJDNy3QiQc9u5b-JYqNLngAdhLM2slgwBjOZ7gbdQCZZ8l8-ZG7pUYWf8NIQA-_By9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fem9yK052MkTHKyfxCwtbng8brItZgt7KxhYe-J3TV68wE6D9Izjuy9zFUsl-N8fs2-E5f5V398LVrPdtcRMqrUCgC1haLHGv5jmOUy6EwbnQB_SaTakG9tPbaklxe05EZifo1mtBhB1supsaK3Fe3Pk9HXRO2hIuxGSeq4jMBwTIIQfs8iqOF4IQFO_eDOBmu0IFiof7p6orUvT4pef0vWNZbd2sQCycpNGgwdezZKwq8V9etwDBpwFFcC9hU1dhskLwIFB2zP0OYQVtQi3hxVO8oZDD3Jqm5ZOzVrwRbhd4DWBHkzRoViHOwNKjsSakD0_8FUovC3a6Y0z-qnDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2fRq9w6Ue5zW2lf3yYqyCQptvsm_vUYQrhIg16HJsS-eYi9io0661BiaUIWkrSi_pLkw7vuyYJhQXDo2ubOF4QPjNup374FhWTfVFZtbnFwW9QnLXLxVhWqT5X_Cg7km2w7G0F8-wbouVIYE3U1xAVinEOC0VgaDLuwMw13Hxpk_nMqdCx3LW7Hzdr6TMZG4LTPZ-_Q1-me-68-c6nZlRyFK-EwQkUPM4C1rt0GLImtLBs7nZZ2NEOXTQl_z5pBwvBTv_k4eZrMfFONKMpY24GUYEMV0I32N72kmCoK910j1p3QduNongt2hNju4ft7KurUmaB4318X4zNyjMX9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaErQR-wB2DRuJllxriBNRKOPNuBey_IohJH0hR79EXp2ib45FkzY0L3T3Oke2KcDc49EFkOD52lPEaGnl7myBghyIHrjFtU2JUgrIJXniSfUhleBFxO1cZuXzjO5e9k2gio3lBxlHKk-dZgKy-P-exwIgz5mjp2ydZvw2q8MsuyNGymm-SUcPYo4ldAlcEnwVCGIjSYQ65GRc7ItxE0Tcb_xxOpndn5cFugevthTeikn_-jy0s7LI6zNAdvD7fln-gSO8Ki7Br_dns9RC2iejcnjBS7K9bwBD644MUlzi2kzemA2o9ch2wumGNCPiYn4rTbA8-S3yJA9bNxv_qvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_vmA6PrJ286NKfC47fTG9ulDrBXjRkvupbfKcGGTBJ5sYtN5LXvtzuEBNPKhlDFQb60BV5sMW2pUTPUzEnZoR9vdVnQAITKUm6Ac7Te2GiCYuZhXMQFVPAHTefpGGGDr_n3udU7xSEN7L-LnqrRoFFpXUO29i0Oa2IJRiiS1cESw1jgm0z4uzZ9Hd6pldQXCH-J5KhCKVJnOoMtCngqGiUzQA0pH4cec9kOWoNw5UHdUrjFXqbUpB31Xaa-ysSXpttlLlCSuwLOC9i4EQZoXRm4IlYbEF3iy57OadrDjZxTLQmfB33wHzKtQbFU6OLthxClEwzKNen-DW7_UU8Kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8-IdXEqDqfydr9zLTrtVXJP6w4j8U6SDvUFGScO-FnUbQJ_k1QllGvlOx2eHVld9ww-pMAAIM7DReFngMh5fNKkZZQzTpRXUQrwFJFufE1GgYhq0Ofa4_O4Q5LA_9rYkHQKfDuRIAp4hLy0xgMBp6vOfx1dvxpNMSVmTQGg4Ku5ZAhf8Nnznh8ZYvlms0bKOKqQiLUBeHfQsoeazKsJtjSFxRYAAwOI-HVnr9tdRz9fuKHGjq4AalEarQhBo0rN_U8vNZn0ZDMbKpDslfmKi7txHWA2dzKpF-WKom15QvP-URpcik9MBlRz_H__QhVGmNhadHnrO3g6oijahUk_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYsLswt4nM5g3Rorvg3vjroXa5XUE_310JbupsidKVwrWbD3Hr5nRSZOCuUMI3rKxakJdTtraSADSft57uyPbW1DNjWzS5NwdCvP0TkNN2l2E7cJmaRXuyzser7svK5hUGnvtW6yQHh1Xw6JuZTIcRQyLRN7QpI-F6b3_GwrMwQW7FTCs9ATzGhZm1bhBSgJGq5hWBEDJMbEvH1_UiBJ9rKfqjESpXo-ugY_bS64v_fRsvk7rB7v2x5QXXQSLP-1YbCGPbYBZQkZW-43GoGsK9Si-M5A4t5_pDRJH7CrzofbFYKA-fMzEQitnMWg9HAru47V-3ZdFeJhp-LRs0sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7eJZIkrsDNBhzLFRcHiwxwmyGycsNPqKfKGUUo2XiNr0gYtCRP9Zl1R7LMWV87U1B9VSZEJWNGYz7BI84Hx-yg6j8d67GmQ1avWMJJykUnfZK_7a3neZVMHDyWsfZn9idjNOrDhJ-K6B8IXtk3sKLU3rHliZC10qBpiK_Q6QlI5q06UxtOKOrOzcmSosb5qKmcHPElOtMn9_kDnYrjr6CWGcHFuSwaGoIvSFUsXSE7REC68dGEYvmmajy0AVn7dkKiqVugmfGYxIdn-IlEQYvqqzgMxYZh7QDx6aLP5tzOHnuBaum6-Y-moIvOtnclTTAz7DuCcgx1oa0mna1aaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLWWa1ZrGx1ZtBYn_Cc3zKTmdTt5dN0VE46u_eHkn9jxc--XrHvvwpsUSiSyQmMJ00D70rNGYyA_3J7VeGN5FLjhP8ug5hC6Ld-SEIxzsv9UlYD0QdegwCrfDbKbEeTBvKGhQHHQ4WNlEsKISAw1ngIrfm__V1JsVzaxSxLkfDZ_8yvdtWnlj3hXo4fWGgwE2cSuz3RLBf4eM4O1lmprioKouc3E0l-LpsAGdn--fxi14WhmndWEm0k4HE8ptF1p8Dgl8tZ2zgxdoHOhqcjQ91h1uimlVg4zBGAbRU40Up8UXbn8-bsCutJPOiazqRznuoWEakQ_mISQUT8pgrLquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERyRP89WLcRKno1mPH6kgBPNunZA18Q2vsnKcjmSWnubk1_dXxpR6caKJUVaa6XYJGwtxvQNbum3JqaR2pIux51W3PbSCOuKIYXCBYZnbRLDfE6obqB5ZsdC6xM0TCJItMXXDQtXDvV7rtEI2PqfOR47otaHDcoR305ge1Ks0_BMD9MAxsizMr3vePxwQCWdMeNCem-BRF2l2oR1LTNfnU3PuCw1t3NX0lljznnltC66zNzxhal1XXeVM92ffyLZODw478He0sOFHcu3U9xz4yDXbeMBm7OPKONoKLbPLWP86OZuJTVqr2Mkn5mMl-iWqR46foA_Dq3eSuo8Qntr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVep5UnoavTD6EpYkcKV3Q_TAgIxBHOPMTRkG1GCgfgiAeuOkiE4F16A7NIjZUznVtnImtMulTd6DXW1YvvdYjqsqywGUVBI_-TQjtewMf-Vtg391o-iCKbdepuRbbnw7nWJSOh1ixJF8wIttjTvzl5_wjzcH5v8w_6-fI6PO0wW3palvS9LKMTaBJrZ-DBHwZrobQZYr1uZEdJiQo2zeywByaseKuh8hIJTzxHi8ZLaMe1Vw6EKT7NDSiHXKAXFroWudKIvPSWpKbXx7d34zI3cRawTeI9rsXXpisBaDHlQzwE0-KLpnOZTtd2RlZDgwulBGAoLetqNnK6OGKHlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPoykHd-JwfEioK_lL0rhyq5TzrM-EPsLO5vZBBiI_NgGKnkVsGhk3fZwsdbs4OUq6WEGIdblcSpYTfR0zch4bw8Pq4LIV7uvEwTKKBm9jURbcFk6ZJMskubDeQUWVjFTU1RehJ2WUACyBAq24kDNblmOmmEpaTVE-wobXH6LBU9qkCyNyg_WXeJku2K8gR8GyPxL5SbE-3eCF3eSr8Bhkez6-xNz1oU4uPdAzv-ddYT6g61uLGgAYzkD6Dnvhb4yyZ1RtRTFsm8YAyRllF1u_M8_W3BmThZS9czXs6dCCdDizP4ljXRjfMl_lZhVzS8xKv9hj5z9mnqiwmtIoK8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgPzwGXl0S7fq-KJXDo0vHmqjTMJUbEQE1Uv7GcBbLGCYsQjV2v-w-BXt2RWGjEr_ppLpmrJNayCg4rNpFTREWBKnveGKkkrGbW4tejFi78U-y18E-mniYkxx0fCApNBAMZcopWJJ24nZSQn9-_HRybQ4rSj1Or4BRmu9pkjpTQkgdiZ-5MpGJb0EYZS88XUvvuk7Kp7L90bgFfssJ-hRJUvuNXYfS8K8JBAvBMJk25Gfad8XmVY4uf3UPzsRky0bCHNIDR08bpONfJJ7JuUPgO77nAXBgd3lrqGP3AEHrR4bTf06kn61tw-xu0WHhckGp3U-kQCdpPoTU8d2bYSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNQuX8hesQS0JV7_Uw20HTJxUG9IJXmub3KA-46uE2lBekdjEmm3NZZzrehU0vrYhpuRPMAyL5eze41Fwka1cAxl8SV5OrkGGMRK-2BmORBHIB8onFWh4dOeCHa_Fy93_mDVe6r4aSXoFLQTN3F_NkpM5oSzpBxPN62YXCOJvaykc5k_Yej133O4CxjXZzb77z5Wt7pgBkTNPvVpz6NslMxjspNYGS-hIjnT6gBKxbqhW4UcilPygBtiSXbmuOoiwSUyVfQ9_OxuEsrjI0hzOLApYqasAI4zj-cdpOC7G5jdXqnUS7mkK6LBcHfGVPLynVZJOGhpedon0_kB1TMvEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUshrmXBlF6YN8bWV-lHSN42mMPA6de9LirYzfvUSs1dd2ZAh9Nl-tFCC8hkAd-uJpo5_LHqtDEzd3sEdF8oZNDvait8ZilQoR27eefE-aARyuYvAgNMYfFqSjTGXuFS6iXii-LQL5JtudsHwhV3Gj8GWWahPCDoc6wOBJHYWTRktOzJdmhZhXV6UtE9Ny9Agu4wVoGt_2sbX2sjt9CeEflurEKqMMwcJE3USSE4DbjWMZZsuYcCogcGu6txj2LaXgMUWG0eHjiAQ4pdvNkTqvEGbAsZGYZ8ptRW6FhIzqaZmaYwJy20TFIJ1temznVczGGwgQQ3XfxvQC5J7Rr9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaLxRgUIhEWs9u8SdZgeXYgueRp39igttSuqmWHEhQP0NS7j1ZfTxtBARrUonjPt2VtJztUsM2n8f6GGAxSx9SF-gxe_japtIkeCtQ4pd0cBd-GtKXVcKeRRIjWPYnmOSiciIi1DxqFuyrK5qqaE0vA33Ycq9IxnKjVCmgiLXGKRi9J8f3HQRJdOPr9O0X6bFM_EHC81UN4nOlxMrnhKCTsgtFYtSbhYKzyQ_ksQGFmOoDpuo8XqMNlu1SKSEAd3oW2pDKEYqUZ6sktoeVe4ElFHnzJGab4wQiIM_AsIU-o4vx3r1Ertc2XO5yA-9t1SryB5ROubSw3L9CzJq-ZDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=DwYmna_e7x5gKARgyHLX8zDpjpU2NvaHuKIihAy1GjmQmB5K46gq3wE3tSdkGoRoVQsJXwFXuRj7PgQr29gYbSJt3nxi1XFQW2lYsOjouoTcH5vNvqB7ImjpW0QmUiVb6ZN0ZEJfjHdLRMDL9isNCjP42YraNfxm7TmGbbTS-uqfrVU1tKbXQNaan3JDgpaLf27bofxvDKzjOyPndl0DhU3uzfkA2ajRHZKusEW_-r4MBSNbvBfn4wFl5I68UfzydKxJQ-dDKCi7xQtiR9e3YPO5-7MsO7_QjGXP5tXtyrIvFOmrZcv2Z4RpU0TlOK1rYXmknDzcQubGKRb_B8hMfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=DwYmna_e7x5gKARgyHLX8zDpjpU2NvaHuKIihAy1GjmQmB5K46gq3wE3tSdkGoRoVQsJXwFXuRj7PgQr29gYbSJt3nxi1XFQW2lYsOjouoTcH5vNvqB7ImjpW0QmUiVb6ZN0ZEJfjHdLRMDL9isNCjP42YraNfxm7TmGbbTS-uqfrVU1tKbXQNaan3JDgpaLf27bofxvDKzjOyPndl0DhU3uzfkA2ajRHZKusEW_-r4MBSNbvBfn4wFl5I68UfzydKxJQ-dDKCi7xQtiR9e3YPO5-7MsO7_QjGXP5tXtyrIvFOmrZcv2Z4RpU0TlOK1rYXmknDzcQubGKRb_B8hMfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8PHI62Vaoc3Blx7bZTtSLlafQ7UsSb-ircFAUbKG0a0wrvwCqlROcZg99a-QBnE0Pxt71QPm_y1XOv43_cvWtie-hXtG0V4e_hlQbcUyXrr-4fIgrPBDiK2D-Ver72yPURBRmttOLxsQoEF2OOUvcWCzQUP5s-PlkCuqYMHRvFdZKdqKqwHt9B_Ns3JAEhRoBYf05nYbkKiEP60KIopycsM6xIjXopHCpWDrGiiamhUPgAwlCq4dRoGlh27PJSC0t8z8vfKnaZnLBGL6MyeyZlaxfGvxp5xtaPpySeJnXTcmv7UohrPbcy_gK7qt3gGZ8utgRVYzoGza4uzprYS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLQxUDKh8yzIqyC8YHHdI3ethRpTtP6qwRHE2q9WT3t5OTNGldw59aOW5W5VzXq74zMvXosvJpV3vjBaiabh7KkKdyKgm_EaKFqRrVKUffTAOr51K98PhV5ilNWKlcngrIUmYa8ZgHdu9F_DF5QKl8eGOYYHnCgg8pISwEj_cIL-kGDKJROAntYw3LlFcCvqEw_nQEMT_qUOs-oLiKzWuMkeJB5w0O709xjFL7sP04D5IVjNNCIvsgVdUe0OC8QmVrYgiuxgUsWzCJiaRJpX7Zn12aI4wLS-yT1YZhIitH9w-aAm7I1thE7ag-vMtUawLOCsecVoi5Y3pwZUrfxlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dyp8pAOm3Yx9woFQyVB_DhVMKmD7xfopgn25-GItP-TtNy-I2OfWBdIUSDGcLmVV1ivxLcpLSNONv1EzR9VQ5dspLI1BmfyNzYlhxoV2iAWAu7aZd3Jf7UBlEhKTOxR1ALFQrGzBw7SJfuU4UnO4ilp7Pm1k-2mL2MbDbMbGPej5l4-plhjI3sFcaG1NrlJlCE5FKMvtZDf4XAEiIY_SepDtI4iuk0YLxVxoyShC2meaeJJv_xv-kn4X6bbRKJk43Tw7usjQ-cXk8zF7OLmt1J0OhuioXvgv-JXv3ecZPBYx74r8_B6ciAb0Ti2H5nxU8WtrS-deeLILwRbmDkIUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQMzUZYnN3nTH0h0v2KFTNRuJzqN0E0RvFf1q5QRgpd75LeQq1B-NTC6HsRPRaDPCh46WpZyb7FtFuWZ-GaVndRoIVl_CRUGOscgQ8VWeDCH2Nev2qbLgPPO-Farq5ZTJLzcIv-Df-JdC0gItYpS1GyPTXoCegeSHDAfRRn87AnGvvPywFrXAEkMi-MzHXdcLMYg8T5F7s12cTCvbl65oYOF3Gq5wl36dWaN43_C1zJSGlDPlR10OBESFfWX0AmrHErcnnIvyoLwWAtBBZfgH9KtLFpUdag4wCdmkB8EE6ySiMgG9y1gnasraLO6iO2TlWRJPHdcuQgZ_B_cHfsO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlrgQAvnGdxeUtPbx9mRzo600CzMjla0e0Da9GKKTyTXFC-fxuyt-TanHEr2KZ7pWZCPESVTT_ynlZ-9Fx5BJ8fco8lTeXvHbAndp3ywbcc0Lht_MkBmURDAtTYx2boGvYVp_8XwvXbIeZ76Ev9nNerz8taPuH-pA8Sj4nEZ_WwjD64XPo2tH0_GotCiRLH1lM3jsxn6BhnV4nEqYhR7sKdlNPc6-1uubymLFuOD_i1JHNPJ-WbSxERiHSaCp6f49j_p7nj4eYuSOvi7bweikv4w1a7AewuM_B_izBn-kMqNi5_Pdb5NDijeUFTz6px81JLDnWV80a_VqLSHDIId2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtFQkPh_GTGl8uD3IOdIkpc3wk2xtaYOYXv84XPJy67Faf7nyPivaEPKQmrO9X31A7urO86Rd8u7gPYHpYESGR6t9K3iUQrZqebIMln7gi92K5cQTDjWY3aZ8m7DZanq5eFGWEJEtsTRfGTVHnX1d9WA6nSJAJ5ldpVtLVC9RR28ghMUk95-sfr77l9P4ncnYTG5lahBc0O7iWvdx-alNo9syy3n1dF7-lT4fWCfFIagd64qSdCnNLiTG67Kl9zqaU9mGmOzbgcecmi9Bo_GR9B0UCJl9VMfPzxelElPXd6-c9BqauYPSdrTz9EbtNkzUfdHLZYGk1Cg9Tqfus3SDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av0ZU_vimNn4RFH-NDxrEeKgx925N70jJilxfdFlrkEFHCVNIGN_xoXvID-EHmeGB0gYXtPk7Ot7eEP6ylyxlgfKeu830_kWkz7KzItCki1FRTGaVQWJZcOw2bXnIw8OPKL9cMjYIn42kJJnQvogFW8AvJ3LCK9BLuSv-lbbyoZfIPRxs-YDMu0Y20PMjMWy4R-a3l4TXVvMhrtbUgEDilWkaIPXV_tLH_SSu1J3JxOcL_EiZvp5NjRjm0G5EhCdZJRjZwkEQWsjAwqZgHL7qB-BNMqgt2RojKYqoZnTPOBda7m-s4mVZlL0wx-YN_BUuzhmqxq-K7mIqD3lcwhSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcandjKeqgK11xocToEBPmGi_PffSQreCkHLFuqO8qOa0a3oJ62s4_PcXOfnsK7jaHgwwbF3D47ZctzNTh7FdxvrbP2elabwDIgQx8ONHdZ-y8uSp-VroOVH4iEMZplVQ6PkDjW71hJP6ukl3Q5b2a8HBSxEZici9iD5juVciF8r6lds1MB14TUZNii5KCQno9lQYfjMy5nQ8DoarZqQVxeB1zFoTEFQeMKKTEaED9MRdaAslwe_aRLDdmTIMKHKAPTzJb6dJQCuMZqrznHnmr5Cyfrrr7g5hsIUnGytt2I4Y26v-BqKSwoRYvqI3NWKtmpDeIfW5r_IK4SoEBb1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=o9ij_3H6O1GNd6Cj5Q29_urViZx44zk2RmvJJ3txKmzjPzaserd5Fo9UXMqqqcm3V4aKrjcIXTcnUBm7-RYUlxVDLzLZVTx2Oq9fxkUetUWx5YQKXNWNN253vPiM5Ka_CXE2h73TiN253SqY8d3K0fSM3AynUCZam1NUzqyemFciyRKIVudHrB2bh7ncNQKFYFYN6TnIHNeQeL_ANxTKQXOwp_4Sj3rnbkl7GjCU1hT0UgVRHZNbTc4KK9rjW_7zrIMQwl67GJ4LUO7yF7sRcrIWzPKF_QdYrEMMzBjKzeDBslOwdFvOxrZLy7aGfF-6j2Oyxk9rUcf7JxFgjkWC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=o9ij_3H6O1GNd6Cj5Q29_urViZx44zk2RmvJJ3txKmzjPzaserd5Fo9UXMqqqcm3V4aKrjcIXTcnUBm7-RYUlxVDLzLZVTx2Oq9fxkUetUWx5YQKXNWNN253vPiM5Ka_CXE2h73TiN253SqY8d3K0fSM3AynUCZam1NUzqyemFciyRKIVudHrB2bh7ncNQKFYFYN6TnIHNeQeL_ANxTKQXOwp_4Sj3rnbkl7GjCU1hT0UgVRHZNbTc4KK9rjW_7zrIMQwl67GJ4LUO7yF7sRcrIWzPKF_QdYrEMMzBjKzeDBslOwdFvOxrZLy7aGfF-6j2Oyxk9rUcf7JxFgjkWC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5LsjMaQYpn-1i-nd0RJbhFDCzqEmETVPj3tlvoRoBvl1f3qoj7c9G7r8hI_rk9PQB1QnkPRrLKtZLmH_SrVaH3nF5tl7LUqW9WLDMcGy7lx85cMqbKnuEu_Q0GoHVMWrBTOP26XBUaQjRTqQ6rq2aukl9V-0RnGl1mGCJPXclC3T6RCCzj5UKtvlZEMF_LihXN7ymXYeAxycqCASXsJWMV2Vl_8ETrJNygGVB-3hug9gOng6MAJDE6PNAYjYB2crNi4TkLF41Wh0xy-p6F_1rcbLLDsUXCHtPZRtteW654e3GA7w_cemZoSAoo2aF3BpdhBXG3svSmNLozk0iJCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=v6BYh1fBJ5r308Qdo2NK21xBp_w-wkNssNZQq_F-jGyrGfwli84KVN96WLc4SXstrl-KHRHCW4N4sYKTpn3ZvlYav67Kvyuc5ysZNz2xirYZ0MEvd5DXiMLqvsphx6SPYDF26NcGWRfYfeP2GbQjkA27pVEV6jwULC58bNhtWXeoH81SVzu_sMpqUUNygc0taSexRhPQtGu5zn51T04gq-wlg3M7jUHWx_21DQHwMEv21J4rtKStpypKgM6d9_IKYrGddAgpb8kgUjb77DGU9f-cfVu6AIRRn5OF1l9scWEqQgj8J3YxGASlU7nXUtXP2nY8JqeAKpSLy4UkbrCmcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=v6BYh1fBJ5r308Qdo2NK21xBp_w-wkNssNZQq_F-jGyrGfwli84KVN96WLc4SXstrl-KHRHCW4N4sYKTpn3ZvlYav67Kvyuc5ysZNz2xirYZ0MEvd5DXiMLqvsphx6SPYDF26NcGWRfYfeP2GbQjkA27pVEV6jwULC58bNhtWXeoH81SVzu_sMpqUUNygc0taSexRhPQtGu5zn51T04gq-wlg3M7jUHWx_21DQHwMEv21J4rtKStpypKgM6d9_IKYrGddAgpb8kgUjb77DGU9f-cfVu6AIRRn5OF1l9scWEqQgj8J3YxGASlU7nXUtXP2nY8JqeAKpSLy4UkbrCmcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=dgcnHHamFmEkLWtWH90IRxIDEsZK9lCbz6eEVknDUa83o7mW9rwktXo6UE19oJTGHtRvBKk9C-k46bVETqmEBt33i34hBmo6AEhVqWE1LYGsCBZryX2LTQuGaQAs3udoZFXhlDZO80Rl298e9xweSj032-tNFz-sw2DstO4Dv5KBlL0KBY1WpHRH5E0FNmL2L9WH_ehATW4Tcedw9_XOrSQY4dQpXo7SzALBHACVJ0ffQolFJtWHLF08UrAkWHOaWf55mpotCnBFzge_5-nQ59qRHJqJnGU4mVu10Pcw0DZM1OptXgo87WFhchVqMDzp3P5j4ZIZXdPO1Wmo229O4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=dgcnHHamFmEkLWtWH90IRxIDEsZK9lCbz6eEVknDUa83o7mW9rwktXo6UE19oJTGHtRvBKk9C-k46bVETqmEBt33i34hBmo6AEhVqWE1LYGsCBZryX2LTQuGaQAs3udoZFXhlDZO80Rl298e9xweSj032-tNFz-sw2DstO4Dv5KBlL0KBY1WpHRH5E0FNmL2L9WH_ehATW4Tcedw9_XOrSQY4dQpXo7SzALBHACVJ0ffQolFJtWHLF08UrAkWHOaWf55mpotCnBFzge_5-nQ59qRHJqJnGU4mVu10Pcw0DZM1OptXgo87WFhchVqMDzp3P5j4ZIZXdPO1Wmo229O4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=GL3nG4eOy_uKOxGaN1q6NKLn4lm_4bzXSLNDzXj5JnluIinsqGUmXTwoO_CUANhNokHL4DLeGaPMfbbqIywJO0KLpMxwplfxLmHaMnyiMq1mguIUBJ8erO0r5DY4N7zUvZ_1v7LBKizXTu1LIkWrY12a1IuaXWIv5b_19c3sX81DGsDR88nseqsqJJ-K5fgJTQuo6HfWZhDEVSTSYLBGQCA_GlMQNbu3vP1BjTqrySJYpFIW0MsVUrs1YT5k1TGSkWakKK29DvJ0b41jY61wZ54v5eirghdNiiEl5cLDyfDuN8bUuQj3OoJIQTIlq6fDkFFBkoVLdM4FgU2sMiW7Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=GL3nG4eOy_uKOxGaN1q6NKLn4lm_4bzXSLNDzXj5JnluIinsqGUmXTwoO_CUANhNokHL4DLeGaPMfbbqIywJO0KLpMxwplfxLmHaMnyiMq1mguIUBJ8erO0r5DY4N7zUvZ_1v7LBKizXTu1LIkWrY12a1IuaXWIv5b_19c3sX81DGsDR88nseqsqJJ-K5fgJTQuo6HfWZhDEVSTSYLBGQCA_GlMQNbu3vP1BjTqrySJYpFIW0MsVUrs1YT5k1TGSkWakKK29DvJ0b41jY61wZ54v5eirghdNiiEl5cLDyfDuN8bUuQj3OoJIQTIlq6fDkFFBkoVLdM4FgU2sMiW7Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf1SE21olufvJhjhuhyJXzXFc5r6CWqbZjUAJVAzhYKUd-4BswBV4tnB1UFpbM-LfpPcf3wL4gPrVTc3Sj5zVJAvOAGMh5qSmT6vqSrVLxjHjx2_a8I-hOj7IcsQg_7wsWnJ6Ftqs-ARkGiVqaO-_4WvcKKwbnFsiNphbxuJfiaZqMMO_6a_k3fwHEtRDMvZJcDJhKvd5QhZ5284vARDsM_GqkXZb39NH53kqeMSq9pB_hzMy5qcYXLiu9bn_OuNlY3SGqBLKYFOIUUPx_FzgcX76wcVGsRXHDk08HEHK8j-ibkXuQ2mIa9ZvOzFZ3xM2VSwxdO5fkoIIBcdupUnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXqQPugPEFs_Yws4BigZKyDvbYRUw1-N2so3n-ex3SJLOX2BQOthDbReTXJWxFcfww7MIX9QPg8p4mJhNszSqUtBnDTpQd4DqpsfpvmkmIw7CyjC_X9AF0cADmG5NqwLIM2uajXAENunGd_u8NmBovyU_gdMIjywDL3y4O72M3p-ibYzBmS14eSrvLc6wyh7tTiBm1sDoWb2QkfMb4fXFhZCTL44FvUZkbd9jfyryFGWwYSqMWgeiar5awpIDzHIU9qF46emUASE0JBUgzHa8v6oc_u5aw0RmE9vhy1zpu0txwT4f0ad3CfclJVMM_r6Y2N4yzxDMRiEa_xlbtfkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USxyBEzvlxWIK6RJ4JHn2DyBuGZ6ik0xJjDn6XaFciQ8eSCZ2ho5oThKB0FthEdWY4zFlPwIjTNQs2ellTC5byU0hLPTZ5OhVc5sFEdSVQ5gjo0vixHbP0gFZ3UzU9AwpFc-dUMTP3NBWIuHAa9duA4x-BworidaHdjkMxAowGA6FgVliQRUFFND9-z7m1ZuEIyNsdKaassc53JNtVYsBYlIsTn417hfiX76HP2xZwI2pvB_U1wNsA9iX2VgGFg_f1y44Yg8ZBlzhbc6J-M0XxYcbl56mSp2IzwwpIG8H2k7TybKPYvuyJslwurm0DfxvIl8Gaqdg18yBjIwg2R1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=dT5k3Xdse6lLkljv06EdUidZOeATcYXP5lv1-iiOaRyYB3BEoQCSL4m6hFbw--sJzWhWSEvhhZnW38hC941CFhzlYDi31lETo3hs8EPYedTpWmEmBihJFDWr78cxglykfiK4KOfDdHCvUvPeoaD1jn9hu6B7MBeH2mEKSS27fyym45RxCiar8m5auKgWDZcJX1TKBu1fN-PCtSI40Nyd1K5DPlF6lIToVgPMn9TMZEbCYh3X8YDDI-7ckibXWpYKRC7GmjbA_PL419lHwHwbytMDE4u006KED8C6slgXXeesAtlSaj58esnrFdr3nYppZAoHb-klyj7Vc64PH4f_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=dT5k3Xdse6lLkljv06EdUidZOeATcYXP5lv1-iiOaRyYB3BEoQCSL4m6hFbw--sJzWhWSEvhhZnW38hC941CFhzlYDi31lETo3hs8EPYedTpWmEmBihJFDWr78cxglykfiK4KOfDdHCvUvPeoaD1jn9hu6B7MBeH2mEKSS27fyym45RxCiar8m5auKgWDZcJX1TKBu1fN-PCtSI40Nyd1K5DPlF6lIToVgPMn9TMZEbCYh3X8YDDI-7ckibXWpYKRC7GmjbA_PL419lHwHwbytMDE4u006KED8C6slgXXeesAtlSaj58esnrFdr3nYppZAoHb-klyj7Vc64PH4f_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ9nmU5I1PDDpB2hSM25a0vnXhszed6GBPcXfE438Ss606n0pMMpCIvWZVzCv-eJ9kyi3VYDZgWAUjx9DA7cXU9a9ZDTnOuRRCcFhDjgWX5tISPhunx080KAEazfhnOtIU94Mxu-aBPpv1nFt1x514M6fHVYavjO5WcHuQvb1tquljb7AwURsfrZz1pnQVQw7Doaa_JZ939nXp3tkVny9MAuMDa4XbPAVvZpgWAQefWLE7iPAuaXdXSk0uO7YcvsKCr8cPzX6D-qa5AY4A1-i3Vy_ETXJylx1OdN1lmEIX7UFq5vFJ0XkDlxq3kifkDZhM7NrtZmFFZ1dVFYnsjoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U38DKYXpkUMjvQXN_s-QxSRqYE4WRJGv9PePJiz7vg0Ywk3FBwDhrk0MA4BXWSBMBt7VrNUky2I1wurEJdjMYh910F_f3ppmbgXjWHlsxB9ViwehTRKqQDeJwRQCNyUjBE2elkQ9WHO-VeUFEiHT3V1E7NKD5IGg0-eEr2-vw3me8jS55xN1u08xwLVBBLwFrlzdneqhrsTrjLgUV-tcc90cPwKTXbVYdp2oi05ws5X1VL-EqvaQCQ5tGbvPwmQln9uFYma3m6SG1S1-7RzAP0q9uCikzvW8IaFLRRv-H1K979ltgZ7hEfsIpbmJUrLHejhDHtjcGpl8MdWdG5qC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXOaeuGxAE2c6AM8wJOKWdlh_H30Avv40zzmUwnV8L9AiV4Yy-yZAF5f8J0O6boCMTb7uh-7lk5exZt-AQoqYIQa_K-bKcsbSWwDMGls3TS_s7aZAWgyaFs7bkFom8TyfVR1LEChbIkDtOXOhyEhK_XDtt0K1Y_NPFxKRKM99Xmc8luTyiL-J3UCDMr-IsWbopG2r1tZuOHJQ8ESKnGeUFAsy2DmTbqhAm6T0c2Qjq1A3z6rFhQpYzgQKXmP4B_MX8dvjp-q2f6dmZyAhD9EZ5mk26S19pd8H1g1zzTV9bpeTdez2YQnVCqVZ5EuuU-CO2ycNMqWn4lWSAy_SvkO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg3NKgQXSI3ROkdIPsMQ4C6nRfarYnUcEiAy5gb15sf1HMXMw2qqwpAbAONBPe4sX7KbNG_5aDYr8KuOj3aj1enIQ3txA3GgESgdqbqmpznCP5q5MZ9aqOPfLiMb46CVr9JOA8974hCj1XODtdxnt8iN9sw9_1Rip_j7VDYKYDpKDlHpBM2HdounILptGfRPpWPYxO1Pnd9PsC0RP50GoPz6EuUH9cfSJAzjTei3NqHJQ78hxAcOsDuvj5xURSOho9mtWbszaGJAggSvk9e9f4-HLTSnu3yaw6JrHS5SJMFtAQfPJzeD5y5tCuwYpmXxaWKGvXkV8cfCOVK9-CBZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Paz0-9jeKK8oEbvyoR0GTLDH5Z7bCeCO1JMax6MlOMqjnI2prlUVxGQ9vn_IZloEHmPAfzNW7Kex15ZwmH1p90fwdKMcSCyz63gtcPCuQ4MSKivgZfAxE7xYE7w32JQ4OH7FV4dsncbgc6hD-PiD0WK5XqGU65ZfowBAQA836M4Aw8XEq1kChVxF86AsQmbMUARA7qRg9KfnE4I_cPO4KQarDswlE3bQ-7DswA1caidVQNH-_1zTP9j05kSRNwwDs-0MINY5GqyOGYJwTD1erS86THPCFlKWvOwQKTx5xwoSxASO0YJ2b_VipQFS4GITPzHuEjhEBGRcL-IRQzEhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuRhxomkkzPd3i_jOpRiKhVUVPNMo9IuD5nIoOvI3_CUsuNNadnc70npFs8dMOtp7bYh97GyBtmnxleSDB1qt2z1rPptUTgTd9uU3exV4UNUM9uaNPf8b3VkCpfYVm7vuQFuR-w_uNHuRJK8irswO2ITQEvd9TPwjgypOZ5y2rCYcGMAlN8TTabD6TxrKmd6df-XV_gicfeVFi39bKcQ20js0Lw0PCdhqvBrad1TZiB1wf8UeQ5Ha14eNEDCVHFxv-pi_07UojwKoGrsCGvTJlimaXUjpkBRdD7GF0ZnIGOdJ5FYkoU5W51zE-AccEPpsVfc_66-0DJUkabTVAsq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=gfgXdG64XXBCes1EB3YhfzBYvneiemxoS7odR_-q7af3vtmnH6MLlDr-PXPOns5up5c2ToU4E1GxUtKWDguVKIrc11H4V-XURnlw7ZJ_MLdQYJVHeFmDbXQYFUWh2-Axoe07qeyls2kT_tQmv9sLZ-Gzxesx7vBlTBq1HMSkcNYzDMaOjU1_s6xj0jpHPBk6nmXteKjqVhZ7x5jEiTxq5t2EBb3-fuR82aZ2t-QUrgMo9n6dFNFSnAs2qRRclltPAbECZl7Zoz3SjYJqBXAf4vbWPzUIiMrbMSelDmOdzR2iLXx8LnuZ3MHQNFRayrTlII-2yEgcEm43yWFm-C6owzj9r34JJ1PO-nXkiS1VgqE1ASdCpVG2iyW4MPfNNp_RtKtwWeg28m6gz04fCMr0FNVF8gOoyrlTuW6bG7SwG5-sTYU4ZG7duhjVth3QrCUmqqPTaIzoHUmcs6-UIb13QOwYdQDiw_m7FL3TQPlNtUlTRXto8-IStYdZkzaToR2ypRlLa0UUWfwo0poI_IX8AgLvuLPDQp7phHRLUAn9QjQsaDB7nYX70aIoCSjia4as1MLtn50sSM_Yucr5gyvkYXBcqnzdQlGGiohgShiR43OCSmt3owNtflR4V1LMYj_I-QSm6zLR1iz_I1nsuyg_d_8ywURJKYHhJOxbHFdJELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=gfgXdG64XXBCes1EB3YhfzBYvneiemxoS7odR_-q7af3vtmnH6MLlDr-PXPOns5up5c2ToU4E1GxUtKWDguVKIrc11H4V-XURnlw7ZJ_MLdQYJVHeFmDbXQYFUWh2-Axoe07qeyls2kT_tQmv9sLZ-Gzxesx7vBlTBq1HMSkcNYzDMaOjU1_s6xj0jpHPBk6nmXteKjqVhZ7x5jEiTxq5t2EBb3-fuR82aZ2t-QUrgMo9n6dFNFSnAs2qRRclltPAbECZl7Zoz3SjYJqBXAf4vbWPzUIiMrbMSelDmOdzR2iLXx8LnuZ3MHQNFRayrTlII-2yEgcEm43yWFm-C6owzj9r34JJ1PO-nXkiS1VgqE1ASdCpVG2iyW4MPfNNp_RtKtwWeg28m6gz04fCMr0FNVF8gOoyrlTuW6bG7SwG5-sTYU4ZG7duhjVth3QrCUmqqPTaIzoHUmcs6-UIb13QOwYdQDiw_m7FL3TQPlNtUlTRXto8-IStYdZkzaToR2ypRlLa0UUWfwo0poI_IX8AgLvuLPDQp7phHRLUAn9QjQsaDB7nYX70aIoCSjia4as1MLtn50sSM_Yucr5gyvkYXBcqnzdQlGGiohgShiR43OCSmt3owNtflR4V1LMYj_I-QSm6zLR1iz_I1nsuyg_d_8ywURJKYHhJOxbHFdJELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=gNhVs0N3oZoVGmWs5f0cIpEsgxZSN3girladrhg23VS4XnPhvuTmrUaybD6LbpDkTDMuIk2ges2JmLvaJHr5uJRUiYqP-nlgPsHc7bJUKlKNx0psJ3p0ox6uoWqa3yA3Kth-3g3GlNFUBZ_mhUmoXLGgPweSg1RKq9z65yTdT2CXKmTTS3uRLfQPg63kxzcwrMOuHO-VlDpQSCwII0mWjUX7RxOx4FSloRW1TRTp5SA9Q09jwniRew3BjQCDH0A442PnOc876bEby1ltzY43R0dKX1tCbG0C0uCmMhyRAKOdfAPJ_5PXogVbImREVVvehYgpJf1mMsIkaf16t29M-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=gNhVs0N3oZoVGmWs5f0cIpEsgxZSN3girladrhg23VS4XnPhvuTmrUaybD6LbpDkTDMuIk2ges2JmLvaJHr5uJRUiYqP-nlgPsHc7bJUKlKNx0psJ3p0ox6uoWqa3yA3Kth-3g3GlNFUBZ_mhUmoXLGgPweSg1RKq9z65yTdT2CXKmTTS3uRLfQPg63kxzcwrMOuHO-VlDpQSCwII0mWjUX7RxOx4FSloRW1TRTp5SA9Q09jwniRew3BjQCDH0A442PnOc876bEby1ltzY43R0dKX1tCbG0C0uCmMhyRAKOdfAPJ_5PXogVbImREVVvehYgpJf1mMsIkaf16t29M-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYUAQxbMjn-aUSSA9ZYcYFBEn54kZCcy5Z2Xxdba4Tw8jOvCf6VrJn6UuwSN52bZN_3Ze6ipq7FOInR_Q1mAvYprXRotP2DSuVTyjY-YanmM_mrr8Q7GrTimJjrKXeApDlqjrlb6WE5wB4ljDMXQ-p38CLNxsBQntt7yKjnqFGBVZnAt_d08-PfholLyFlbMua9kzcStlhzbts-N26ZXxDh4aQOzHcEiNVbf6ENhxG_FvpM2EhK_9hA3ldpJY1TnZ4bOdLJsexCUmjb4TBNRyatjk4ssn51XNGcFBscub7h4RlQgb4sa_TlL1OzjP7eFuQcxDF1BNZPqvsQr99wd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs0g9WHnLCz0DlSb7gZQ93DU_S4F_37a86TLjKl_NBOkiUClVT_SK8h6wEBNGFWf-0DqFfEimn7aySyxMUQtuWlpirHPZvbEVrrnmk3WQQ0_j4AkCDS7vs1Lhi2xIg8KKCWeRKkAV_RJ-xaiiE_22gRmW9j13Md8U6ZvJgHKz6xMq_jp_h9C21Gjo7PMpT9puHX9-eZSNZec1kxpDiJPMo9YaMco9d3JzGyXo4814uZVCqvyS3WgNtlwTG8tybTYuUgB1pBvNBn651nXSTop2r0Lz7Z112CaEiHu-9FpNvynD1MGJ8q3PFKVudEiEIdxMjes1I05DWXxsQC8QzOzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O75l-HRQmloXoWPeEcoKiH8Z1oHdZBuXojoTri6VvW6VQwfIWxZmMvcLMYCuqEdddjQbjHIPSGPjdNfxZfNLhjlJugoPeyvIqp5WpXcImu_FCzNzGsj_sgqil7lmaaHXfHEvgCKirtNEkRla_gZeOdODifaL1NUl06Kf_Gmp5fNu0hFG3vzdgcysW-eOe8C4upG9H91vB9KncHGe1omMrQgTLmYkTl1VwNhXeJAQIOh20iNTN81LGtupbehqtcGplZVUvFitHhO4WOqmyVf03lBULqHJOU62TczzkAxgPqvh__AQINhhucEaNQUcILH_7qoTTzjnosoUgLM2lKdWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6rpFgI47LR7VEUlVFExC6cpbaQ6zNNYm8bdYdJl0bqoZlT24c8hTZEimJm-EY_W8SfOD83HJYC5UxJ0W8JdgDlo9u1NZxedyQlZF3V0ObJSSKbhutIGbjNdLaMNA-2cnQKunPrZcO2wZ1dW7HI7x1p-bbY1IrFzv5oHmEZMRRvTJMLnuMfl000FDqpRe6JhhUsxlwmsd_B1HYXibJt8MWpZ8J6APf-yD-4YTvN4qtoSiYg4viaRbPhdn6iWUTYEv7hTKTkUo2RyeHecYjODQIqyE_O5-knIxJDHQ_VzDrLDKW0IcRoukEXExzvi-HKMd8S4xyZ6kS0Uyvu-k96PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouklnnp0FRyuUqEHxC_BJRwa3zDpcOObjg3cBDn1tKsbJMUsirG-hJhtXJTLiDlGSkyAVkEIY2r2Wwh2o4sirm5h1WGefITdq-SdM2AoTaCx8rUaDq4MQmb10quBFMoPpTIwlTJ2usqwQXOIBufbFKR6I1zeb1ZdTJ8hU8uBVuRtoblrdeeqisUBU2La6nK0hcABrBbLPEFsiYfTQvbNNyK_Qa0pCsiAbxqKekH4hU9f_V30ZMD--lapr83NNcAl1VFNpPqosglW5WwfNpLRAlKBxdnwnb0fdDbIM_-MVA8La_RbkHM54yYXsOBG-kCwQqk1kkF0-a-U6m8VqNGRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-rx6IyC9KoW6C1DA9jnziJVjZIGvqIkKvsEcdhYm-7Kg9w9bAeRyA5sko-xfluELF3J-kzNuG-i605fJ3Ow9j7OgZdt-dAq3plzmLIIjYGq_S-mvpfTE-z_pj36jkVOXiK-N8tpEVr_Dj7tQiNaav3DupYxlaCLa90iBLda1Xpl5Neqd-k6TrHiRDS07c8dlPpi3HTExIcOUuDd0_yCF4EcrNocGvFXo1cmVY_ppnV_Ze51xDSvlbv5VkqfyIKBjLKR3PqRVaVYhNU3PrsSeIRD6JOWNfLdnit2HcibuJsK6dn_RJIlFr3r4YjvVz6-tMJVmbAeyynJapSCsSyMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmBzqrkVt_UCC65F8bNBKo1nWY29IZ8_XkKemwiAaX6Vgc6HLFc4l3s_fdmVXDenatPAsTiF2PHkvTtz9ifK6oNQU170HycHcIA3z8f5RXGkGsbj7QMDKvKOiOxY2Qtep-YLzPA_com78mk89_6vxOoI5X7BYTnMC9y44z5mc78YcSppVypS9ELVdie-nPJi2HZW4HIE3cI5Z3UlPcz51aCwQ35xIl6UPzIY3QlHbVVQdGkBf4jjPc0v4XlwtwL8PqefmFDEMO4LWq3le-4IQmQHgN8QeIVNgkuxZarrRXOh_Uio3jXgKu_yaIbXcaCb7eniVjMHvDjmDg8FKkac4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSAA88Wc_95Vrsw5-KURvg-FMPNihuWRIiWYRlOTE7duM7hWQCk_lj-sg3vHsAdcBoKyTCw7N_MukseKFXp0GZ1Q4IbDa2vjXrQaEWxbPBf9CxtrsJiIWCPnYmUN00CtSKOxPRcWF45Wgnu8aoJ1cRWG4XDyHGCShEHxXzUkyYHxdAZrUse_sRzZl2WIuWnyMhIct28dyARz5-lMR9fmN1mz2iiMaUWTn6aZZuiMahwsluWjEOODSXrX3e9KbtLLu740d3bJqmWviTTmf6iZrrNwh-vUdyEBL54iExf4Jyb-X08KZG12FRmgzRge2FrCu0wxU15BEyYXTkHHKmGrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjSgzW6zK6hkgKtCE2f3Sp1R3XBjnU3f4IL3-1g0seHoeC3gkzU7N2pQu1isAp9CXIMz3iJRZnymnd2emnEyizdKcDEGJ76PjDtUKHJY_L_fcKWCfbXe-tl6SimJeRjUhLB86B0vTR2LPvd61WGoJcXL8TudNdMTJhLloPB5zPSfv6_kp-3VwslenR4IRWyxJmGAxcb3Hb4S36dqCtOiMZIQVuOn5s_YLAkY1EV43E5mAcIsjwgMtpiyO61pDNqsLtsN_5uyK87zTkWcbCeSIhP90FBJj8a_CY_5Tdd47mTp_5Bmdf7QLieZQhYEKEZlNWiGTcOOUozr0s2lT77Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdZpYX3FEJb67MbWDPhJm8MyGr_zOl9RDMvT3tYJCR7b-4QFuXGuZ91MSgnhZM4nWTNPN_tuv8DFq8c0qHiBlsr5XJLuDUvBbdEa0MeNhgZHiyIq8qe06CRdqBx3Q8a9v1nU_j0jNcHiHbYEFP37Zu6j6HNOyWYOVdzcqjx7dvqVJezigH08umFBbElT2MRmlh1NJ-qTSMQYa9q53q3jgjdKF0EAHzvxQEk9xpVP4bn52GKKqTTOn7OxcNZH4sbCyXWF_8ApingU-DRkkLHnM-j9mwXX11h_oaolR3364bwvA9gIg30jiE6a6kuZ6SZrS_dW9FoNT0WqoPjfy-pbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMMrhIqV8UMwoStX0CoAsQtU8Y_zXelKSyLqpUJHGw7Nz0yV7lYo0sG5sVUzVckkaJYT7OPK4ibn84vUTi_vTPZS9B4je4UsnPYmRca5g-AXx0mgrWhuV8Yh1iNi4FFO6b2WYXOp51uIATx-KncsfstXPTXNfAqHSdU-iA9yEi7ueH3xoyl-BP6cngzDbgcKmvnrI_hjIgvjtCzLsxRdqCJCs_PUKVRW3q8v9I3wy3mKPYInm5ywwcF-PFf8gw9IMTaBWxMXJMaOqhfBitEKjM0dBjxaFZEyt--JtLn_aFfR4vbofUwDSnwOvP_rYDGh2yV6PlqgmzZfV6vZTosoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjgLoWMP0bCsRt31vdotTS1IS_kwhXAjxrycyA_atCpv2nCH73v71bQCTKrc4Os4ef-ooM92VG4aiCzo7msE5WXRVqekCS8NEH_8jkAV4UpziE2imfy9Oc6EhknXoMWiuhm6NLQBV-B0AAAj2CrsNyjANo2n1eDEUb6oOpTCKkoFNdt7dSv9peYxgEKjCdiShGOq4AbJUrfYilPlbkqZDz7z8P-aNb-DtMi8aIc0Z8mxaRAJzBs0jgTI8FMJxc7qFQN1YQX1DVJRsEDNFwdojelf8G_J-58RsJTdlqjNFQntUZ0aclEet8zU3oV3fMA8IjGq04ntrFAnvjU0gf5STQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eET0HaGJPHCfLmG_7uJjLkRUiILym-7mP8lXcph7PhngmVmjOpdwPYBX1lWA9a1OBp69kmtVlJxlViQq8vTNfnQb2f3mfyQKbPV6FOWY7EXr-32QINjyxW1ZiPmIC5SCRTfk7jj77NWy5ao0X7hweKn9dWOrrz84j1XbCQh8UDXKGSERUPWJJ3D9AHuKPtQ_DRTio3GGtlxjh7JDgt8oI9b0sHgzAEooBrfVVElvFFQC3ECuKdTNtYKR0snyOzaoJcdLhckf-PNogrAEhOaADAnktHAQr8zzNUO2K3Q139yesqinYNCaeNw_JzCM_YcKgu7QhI32YdIThYhUst06_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNzJ0Q3PszNOiH6qXSnOpoo3hQmq999CrtMbD6-zxO-CxftIHFdr3XyfcxohiIdvJHmV6hrfwHkYzG-hS2kZ0tdfwZ_ve_ZPUHPuRS9ppwONn_JplKb7tSkPZiLB8Lcif3P7nR1YiWE0Q4roBi74WLC6R-AXWPtrYSzlcap_wNcx4bNLhVEPWxknJvEArIeok9C4GMWb6AYLuVC9g_27xX7AflzYxH-ywNE8TVhlHgeKWsAcBEtHUCZg_JChVcT7J6epa5aV9xGj0uRv43XM5ZWtpz6rXqeelppbWUz134a07379VUW9Y_llDlXhoAT-VE3nC8WjjcmYuT6yxLZX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8FBGDZLs-_GvhK0C79kWhoBOfJf3WjHqMRGw6hixTwlM4x6G81vEX7z9oDJMmJOl80ucjchQLKUqRJqu9p_RBNtnsJ8cETBMz2iDxZ94lfwkFIwGJ1kzkSvV5UWz3-E4OqtWC4JZlijZArjHow1KI1YgAF0fDyZy0-ailLJW5Dtrrz3DfOgHp-paz32gCu2Oj4XMjYaKpSnXERfSBO84j26k3oijOYeio4g3722gWW1bnsvyCFDixU0TAFRYHzXswIQRvNpAZhl1F15y1fbWh-fZJx5zoB-oUXRVDouJbpiqfFnfHn7VMRC53ynl-P-oUpg7aKZOgp6yvQvrwqwMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO-iEPzLODxqjkpuxC6Jg9pwl1oGkQbK9ykY2I4gwSj0OGDVEHB7bwElq1Z6XKGjzsG9ELoikty-FkBEi2WImjBn4AWTtooGwF4Gxtf6cHYDFnjTVFNv2St0sguJmWTD3uev6fmAOP51SpJcEPNNC1vHL1T7GMofaYsn5M0Nm_6mxtjlb0_1GcDRHnd5OnUoDQArTylU65jF_veH1dDN7Uxt2z9NELkznpFGgr2jfvwzdiLU9elSyJdO6ES6eD7mc6Rn4IXNrADKdnuPuiudWV9MzW7b53dWo-iEBI8_zb0oLt_3181E9uCWKpFDQSRLtAeRedt3errZ4N43HanaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3L-eMuRUikGIdC8u1adyzbZ5fFSkX8-Rte-uygpK_i3Y9RBDQG2f2OKur2ZfTkcZl653eIV8t9tD-59c6hKt1tvSVKAXZWBV5NPaeT0MijHea9pEMST_rP98_QXlW1Qv7tXM5L3kvXntl8tkkFd5wmBRF_ZGGVC7Yfseioc8v8-c9lDOukDWmyP65YIbVYyAcaxzlnC81VQu4PxVNZbPcnV56VtTu1xEbQLBh0c9ijJauwV0jTarTSITt9Jid9ImNUmhudirvjYp_MSp3krBMgNveGTRIN6Fmdd-wGAz2t5jhxFrYdIUz0-GRyT3aH8Zg_1UE3U4cw0e6xPDy16dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=DPE9RhXKken3diQ8Ftn-ljxZs3JMgtYQzyCiQkmAfnyL1JNDYlI-2HUsASLDqECwSWhmzA30NaSBssG11AgIeAH1BNMD3TDy1zb3tIPKcxMFe78iI3ewCpPMDVV0Nc-LNq1M-jnvNj3pJIujGbuvjnox9U_1iG1eZUGT1trsMTxUFGlFCxSCjx9ADko4ZUSpM11ZOkc1yHbctBUhnhRtzkFBSxPPvDUHvfg_HxMO9nyk2rl5Vt9GQ6LHO27Oyv_iT5LRDRDzu1w1_lB-r1LwV30Jbvxuhs8eOZOyZ0h2_z1DCJrNM526gE9uzrmPJrNe9sgBH1pJKMifdCPkw53VArJKBVy1kzZMWP4b43Vs8a9A59qK0hlp0sPA0UZhO-7JJy2U9p1WwdFUbI-IJzWlSEUwjzxUdT-cHp2vunTvlU_n71Ntj3w0cN37-pcA0wSziAr9O1P7JifuohHtdrwp1iy9O8Vgn7ZeNlitb9EAnkcsJ7cjKeL4iLBHPQhej8fVoHRDTbAPIyo4tlonFhVyhgJ0KkJNxJLvSlL-ZXW-YqCqy5Bc255_eEYiFD7Q1NboOYE_NESc7Xfcv9_knwkfrmL1wHGoXcLiITZtn_bk_lDCXM82WhPbK1my2bT-Y9kFvnXW5KS57oS5UYn6bwZq-fUeKmuZoZ52JGIiMYK4Ewk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=DPE9RhXKken3diQ8Ftn-ljxZs3JMgtYQzyCiQkmAfnyL1JNDYlI-2HUsASLDqECwSWhmzA30NaSBssG11AgIeAH1BNMD3TDy1zb3tIPKcxMFe78iI3ewCpPMDVV0Nc-LNq1M-jnvNj3pJIujGbuvjnox9U_1iG1eZUGT1trsMTxUFGlFCxSCjx9ADko4ZUSpM11ZOkc1yHbctBUhnhRtzkFBSxPPvDUHvfg_HxMO9nyk2rl5Vt9GQ6LHO27Oyv_iT5LRDRDzu1w1_lB-r1LwV30Jbvxuhs8eOZOyZ0h2_z1DCJrNM526gE9uzrmPJrNe9sgBH1pJKMifdCPkw53VArJKBVy1kzZMWP4b43Vs8a9A59qK0hlp0sPA0UZhO-7JJy2U9p1WwdFUbI-IJzWlSEUwjzxUdT-cHp2vunTvlU_n71Ntj3w0cN37-pcA0wSziAr9O1P7JifuohHtdrwp1iy9O8Vgn7ZeNlitb9EAnkcsJ7cjKeL4iLBHPQhej8fVoHRDTbAPIyo4tlonFhVyhgJ0KkJNxJLvSlL-ZXW-YqCqy5Bc255_eEYiFD7Q1NboOYE_NESc7Xfcv9_knwkfrmL1wHGoXcLiITZtn_bk_lDCXM82WhPbK1my2bT-Y9kFvnXW5KS57oS5UYn6bwZq-fUeKmuZoZ52JGIiMYK4Ewk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOUPNIiyRfdHD01woGTfeY0Z1nkkFiyC_rwHujJ-mHYlXyFHPVmOGN7iPxQLy6exxoO0dl2Lb4e2cC73inRFoGglGwkXFDyaNhXaROcomzPdaG5EMz8ozsIm5gVeGt_VxoNeOcwrkNVeBOd950w8TabNRQu-DpMwhherV1AyQ_QAsTfFEBmfEto01mlA416woMPXdmFKV9mkXfWnf7z4x38i8AeJUzreUu4D4vZMmi3HfR4FItinUAGZ-dfFQ-St434_8hfDHsKFpA90cZyRz87FxMuH8JH-mfnrCWCDMyWx9BKJy1WMHKgYaYQw6MOdKwtWrFf25KV-G26T54v1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwZJEYCCLfO__755_nnlDJ5NEJcCJWKn8pz1NyV8X-3Pdlx8CPEFCBhFpYBpO4baQ4GX4l0tJgOyNzZTk-vwvlzxihkxm4HWFgjhZ-c9XoDCLRLm5MJSReqopKBwIxncTG5va_7flfJZYHl5nmFkDKfFVwYMBLS8XdEkYLle0eUo_JgARbv_Ey-MeMZd0Joa5rUZnD4hTWWSLH5Gnmsz4_Ed6cetkUkQUdIXazIc2r_vb3CWSziX8l3NpHgpItlo56gficFxHFT5hyiff05wUubhMOPipTAQF2wA4S7qJfS0yMuuzbffSCj1KfyHg1f6rVXL7r2bOoaWi4Do-a3G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsWtHbsgE-JSuPyJIeb_P7nWn8BPrBvQBhEzYw_NV2wPFXcUmgfeIS8KZcl7tB9gtqsdwYssdZOaTcAAgIlSd41q2BT4KqXLNH5N7x3Xp-QnruHsEjIMhAc5K-32E8bibUNh8HQq6R10UH1ldhH4smrf4bG87Wsg7swo6farLo3jWj0gVuzNtR3dCEJTWP3CNUM-Wy1BV6QgGvEYnAUUemFcNIBMQ0AUJAvbDWl3ydyIOoWYbziCu-3PGyOin1rdUwJa5jd-G04rNjV6R5m5xqjkN2sHEgTyxqf4M1VA3Aaxl1f0wp7BNO3n-7GQxd14OBjB-JAoScvbgRxInHPE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmVTdrhUscpGCWRvBJYAV95kfptsdUcPbke9yiFNkc7O8IxzTQkqvVMREM77C52D9i71SmKGwKF7KcLXbw6y3nZrMLGxWtbLqPd_aCgHSm6kRaVJW1H9n-g0u9D1floTgIPVWbV3_LNYyOXVUNdNHg6ZjM-9sreG4yDLRao1aGbtKDq_gsiuwSD2LwpYm4ldnMwKDvhCucRArqlRUjhTIs25IsIDn2CT_4fjMElzlapXRykIZ4vERAwjo8M1hYLCGgv5MEod_05E-6acAy9pL1okufLoufsaExVps1n0-oeCAJknh7j6AV-0TL3pNz2W5EgQ1hx1LMuwQiVABnNj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJb1Oq3I41S5w-zAxxgrMkG6ZTXWFYwwYtVNOkCguNNEZ_nlrvzk4dN7cZPa-Kx6EHnK2FG8r-SsnYp1GrW651mN6YfxN7a-nh803GCzIiSbhB5Q_y5mIQPhqRa52IxcxbZCysWRp6gHUTYt_whd40m4u72KBvbTVUtCrOyQMiRGEoCR-_RiJgXltGEJdeNyBeTd9AW_gXPYDPzutIWZw0dORKzlSodpUYFMHpxXaI5H76MEdgcEQYsPDoS890WM-8vMDSq8Iwsk9C0pWuqVJYOaEZ9pLqCjMZCqMhMfUWjIZo-Ek-rhsKd6vxM3q2OESTmIaw-36ecNw09REaPppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srfz0y4zZUAbtXJUrBfi8tsyw0zfkn51PajnSMEbhciU0gPZxufqQh8ttopPj8xaG_Z5ja0SVQtjNwjp8IAzOAL-SJ6D0q_JK47c-AqhDl7WZCz_2lV3aoB6jA6Uvog5jXpJJhBjs2PotAo62e3B1vtjFUzXY1p2SaG6R1bSHOMOkTnpJ-oh017n4WCdTuBjCNV7iQJP0wtMIDlsLVwp_YfG_Oez_WO5tsGj1xS4dpyxS4ztXBImJ9DzE_ZQT7zLRdzdinxbiF3Urrx1kW0pjZRr1TWVtTTyF0iGaSqUpxfaCCoXoE9E8V4xDLgELAvdwste3bew7H3nf4cynyDY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcVsmr32Bb8iGoYaDmnIBEoPu0rD_nRP2r-wJLmEYKn-70hNcCiP_3YJ1kWH7uT-G4Dwrx88h5tVkSXCepBuvGhy6QTu89oDGhn3lFD2gEr6KpXRvO2-FAN8NcQCG0uhbQyQtknmFqf4-px0K1m_Z4aBWUokUUScTVMXceOQMbDUdPoRQPHv7C3u0U2p1sFvp_0Epd3-zLjXI8JzgyLRkFjFZfq6K6rC3dzRjff4EtXORf-3jC1LsJuL0x3IoWOGTyRXgZH3kWjrufPiUSXFd9d_qm62-wkAwdgzEQI5pqxqttL-9mp5G81jmjwobBGYrGxE9nukz5XOC1OisDslnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSemRwScbRfCnVw43uYdeP6D8jQbkQpOi9VzMLB0gO7Dk-TmvVzvfjAByOj09d5TtsNI8krNunnB49hOeOBLZTt4RoDTJ48YnDoi8J32cSnCNdhaIqiIaXKNqNY7fzXKefJb2v9_97ncCx0A7cKiF79e1zgGjEZr363xlH1cW4VjlG6_dnK95MbHKV6YHw4GFVEcEoH3bwxJ_8t2jXsiSsrpyULnXY6d3y7A_tGsryC-9PTTYiCJ49dm1v-nH26TIREl2gyBcsklHwMHEHG8oT2ToLAha0twJ86WFLMT1Sm9tVbrlQAbItJpsM5Q58A6gwm9GEqplC3eJKgeYJKDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hvu7Bp07HNKVvKbH9VOKOn1h9MV5F6_tRm8JOs61nN2pwOk6AsJ8Ux-Fn0_wMVcItHbe36hWqal1X_e29rQNed964jKcj1WtUH5SAlqaXq7hyc3ewGy3XO3kQcpwQ-RyL5CCNCUsjSs8b5JkMMths1lrYxiIj9hlvS6SsADPV2KCxZ5VoP4mwQLJHJ9Y2mFFMiD3YzZU7CIeVPAQVxh46fNRc2AfWnpYOy7u5FG5LSxODl3ADB1JLrR83QHQnCADeNrXCr5EgZmYn0895V5R-4Im8DXvqkkVQckUix1JekI0XlFGSoUZYTWQ-bQc8--4ZJWNMaIt-QqBGwd6GQmjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRY1PBpqEzrE4lwD7cyzBBW1eezZIwpQDpJ1HzGCnn_ZI-sJQZdkWzrBUydyjil_VMYi01tXchx0rlmySTaYSA0QCntwhbzJT4D9WE2N9Qf-wl2ikMBbrlsbqwI90vBxmuI-9HgNqy6qHcCqwq2JEL6J9J371BRZNFA99m96LYJdHOGaABpxH3NrCmwiREAqtU_uL6kMu2BkW73IumBEFxymFRZgGsYUxLyVuGmnsWgOdbaCKdJMW2dfCfsQRl_iNFQSWnpd0ypjxq3o9Udxoc4kgQ_3AjZyeucqYJi1ErcgGS6umsHAkXI1hVgvOvP8R7p_zWyR-uUOR63CPVkILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Hm3Uan6Vbgzladml76zATKkqgHaKqVrdFzHqckZqzMmTSAG7Yn4ixiiugiOk2EEFk-tHpmAYzWTyTL6xzyduj5nCLtuEBuhT0_WoKb4Y8gZslLYMMU-omrMaaWfssyfkxJorDHCE0ywuCNYYAOCx7ZqP5kWSUEyJmnh6dA2Co57jnEBPSYZu9g-wf3pVzg3wMwgjM-9Bq1-gnjpE8dwHoolI8lb4dG9ODHEsvI-uNczHsc5bcze9MrXDP8acMn3RbJZA8Tjw5JUWXIm83CQRMBsjdOyYHkCqcpPsEu_TqhE7eQK-Re851Z2OEOw8CInyXUdcQRYx_S_afHaWSMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ31s0kHFBSRANBbTHH682gUerYeOVuetelgyXDYswpzYCutyRQX6J6XM82-zEtpgyTn9fjfzhRPYmpbEogotjlpXnUaf3oRYyo2l2pWi-245mEQ9lAL6xGs88wBFeQM1g7zlTXnQKd0ANkscxtmMTAeGCZu_4ZqeczkPph0xx2kpvzqoH5UuzVhDnME_n6ES0Vmfxd6tcRQSczTrUOtvP7M6u0Fal8DZMrmhhBrL872455v0YqkWDXdvLR9M-bz9GJMTNHPABQLo18Ea7VOuVvqFmatAV8bnc7fnr5HSOPOg5CSHatsIsm9DBjq8jw3BXENQC1xjwQwYuBXkHIK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyqB-89t9Ea12bmPriVhs8by1853yNsZ_ZEvzOB9oYVLTOOKuoH1ejRxigLppQcCecQVB29NMGbWWi1pEyvTYmNUgxBoCA0CA4DsumOH0EJtvD4a5o8YEUDabevJhQNevCtf2u24hGbhw_wyaq1z8m4uEA7Qt2GpeW-TPx6U90jUGbdom-lj4TH4cTVWhYVFioCb498rO-6ffcz_kt48IM0MPh1sTei7aEVD8VL3u38mG2KEfISNwySpyfUPns5EYjf5_hBnaaa5l8JcB0u8F7Z_qDJURsbmCi45fsDcax90Tk_uO9SClvVcJcqeuOh94vsVysvUUDy0xdazosCGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=phH4rYW-5x98LPYVyyKXzODX9Y5dSisU3RlxrVHOgC7aQxi7UmNUTv-Tk8WxXV8NbJDWLsFvL7PKqJeA2IypTtnHBKq5mjo--9n-cnPEX_SuBGAXmb3-qRzLgYQyTsfkuwULm5arwSdSBJpN1NbyAMcaeGkKXk-6G62If8hyLEJfP0SMbPJUkYPelJ1RW87OA22ogRzMo_j3qJCz-pOk0Osn7v_OWacDvCPXIjpdYYDPo0ULEZzZmpUsicFg2E0QoAnYqmlab0oaNrrUplIrg8zKjnrjBFMv6TLdXI_Vbd1OFerVeH_dUmbu6Y6P8Ig-w4-vE_gj_37y6q-H0RvtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=phH4rYW-5x98LPYVyyKXzODX9Y5dSisU3RlxrVHOgC7aQxi7UmNUTv-Tk8WxXV8NbJDWLsFvL7PKqJeA2IypTtnHBKq5mjo--9n-cnPEX_SuBGAXmb3-qRzLgYQyTsfkuwULm5arwSdSBJpN1NbyAMcaeGkKXk-6G62If8hyLEJfP0SMbPJUkYPelJ1RW87OA22ogRzMo_j3qJCz-pOk0Osn7v_OWacDvCPXIjpdYYDPo0ULEZzZmpUsicFg2E0QoAnYqmlab0oaNrrUplIrg8zKjnrjBFMv6TLdXI_Vbd1OFerVeH_dUmbu6Y6P8Ig-w4-vE_gj_37y6q-H0RvtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt8FkdMv6PIoCTHfY7FROeUgnSvxnjtgFtL4R3gkdiqPbWWOxM0xTNWx8o-r3K6n5YytooPa0-dimW00q5Wd9B6p1HbyDFxiKZZyG14JFGV88GwPk4nJcVXl0eq-jl1ZWuGL9uYWrxBdQTDu-wVNIaIWVz2MXUhpAdX1urUrwFvny4JtBGihlI3-SuwX4zJpm4ISaBQUurxeKqYc7iLzvCghTNp1Bi6jsbbkvIGCg3_Pv07jyQ_8pnWKIdz95Q_NGjNzf1MZ1RptyMn5cmk0rHMo35LIzZK1SHZUuEOxirUULz6ouLAge_ffPbhEI6AGigRtVtpa0zKNkFSlj96i7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZ1dwlX8qo3u0NxQ5tFagHbb4R-MYellTnOuLm5s5Jok9u1RzwAkAzY0kB6QRP-sZgFF2RTXot1pH1RTEA5y-Ux1ve3yY7SZJfI5PZnNPhsfK0EF29uvhqg6pskAIbJeif4dItphI5yBUFaMjXjrNiqtHpa_jE-oSfMTKsgMp0uvDbiaGYYpE8HsuRhBoyaVibglseb6aP2k38nwPR0XRzPXbjGNyuZ0No3WB0rAN7qec4R9PMgFX0yC6miFExqabRB4GvRMg0Xl_Ag2uAIvLnW9C20mD9-P3FgMK4haKM5CCViGDnNb_4IByFa6UWWD2ej56mo13XWPA71QrWcXqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORoWlwIdshqCB9774ure1AqkpnWm8PUxxzfHdvcY2l_XXZx-PgbykfQGkGgjkDZUWET0e8Eu64A--N6LqiDmC1JaI-PRPn0WBIx3bAMrax3Tkfaipg_mgQreVp3BjxREY4eEm03H2LgUHjy4zoJS16RnncXiNzSX9pvADqcI7zBBGaJYnktKqnhuIKRJN5Fd4Hr2IMxTw97Vx9TDURhlfNzgIw7MNEZW8EMoqe7CJ59Ir08F-GJknP-sr1BYlzEUsriCozH2FwICBfpG9WlJM9aHWDQ-bnx45njJrHNSjuqiDc_NMDnK8H70ng8vV-J7daKee_7rOyKnCrWz_WP0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBftUOEJT1HkWNHhyGFD0O5wZAMYp_ek0IcACEqBxtWGV__Vh-8bBB0bFPR5YlROb71Ov0KMtIHKVB_LixEFPITrNieOgJQeM1nGLvltzNxO5vrG8d7JP4XB5eRTceHe5KKmmPdYf1JyEsP7UScf7cKbfBvaGckSGWwYqTrbfg2mPNfdest9wDLV7Ehw4p2HtDfcU_u3T62ZL3Ura3vjZkopnfKS04lpHuIGTsSGFRaGcVax0DPSU8V8kJTaTADRHpUG_kMQKcjX08FyyrNSYkj0oOg_5LJaUj41zMEcedYvUA1IBp5I3jfiEcDdzoKvsz1f9l7LZb84U7-Nc3RvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjYcZ_Lwfqs4xBua1OVWUnhyg77ph_CBfEBpen5ljbciTkfpoKojkrw4EDbZKJ_xY5bu0gctR6epBqQJSjrAMniQMwqaRb3V64SHuivcOWIJIpP9yakNo2n_DRYn4tnWWCD7D3YPWRdQ9c94yze11rY12pqjFj6Oors28ra9CGoGN2cnbLZwJcOy7seCU1U94Ap-OifQHbQ7-zkraqqOGLeLX2-ghGdZlCN4ziikd715paXkiAL7NR4LfrG7EV_9NQyCmcdybC1QmGVBAQy4Qo01RaSMM0kIyE4_MLEe_YqUHHKnrXFAAONOo0sMvCCRYRoDoTAPkgrX42DExfx9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIbMfI-HenGiXH3ref2oYx8Z3PuaHllI4c1d8AajY4Daci3FI1TAm3U6Li_MyE7eQf1liRjrSrBBaMjEWm8IJCOlmG3kyISbaIrIHyNIKW5vroLYfYkRxIlJnkqCSUYmNxyfhrVPRGqgzYLcpFHn1xtbrNfh1m81LUM02pzx52-_48DyYROLz6cetDlQWqfyRA_ZzgMXTpPtn4ypxOf70yxPhGcW_2ZNFPF_Lwer_nFXcMkiUX3FmBPagGnh3tUsXaPMqO6-HXfO70IcaNvUZAE-1qlpKs30dqro7s3JYRqmrG8QoQgebww1c3Dbpr1rKIQ8GqJL4KPmSQlHUoHcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dILVjKllATkOrorTmSSLjPniw6ZZ-N0uXMttMgYd9eY1KEWjIQJ6nrgvuDYpEw-gl6XDPFDy0m9fViamw9yTcFiusqV3_vv54KdQRr_LGnZ0YL0I1myJl6lwg-SlhRGM1M3KlY0MCvr9eUWgGQnOqCsZctyw72Kea66e2CD4fxK9pTTuIl-QbysosExeUY-WC0eUQRh9PRWfcAI9HRmf-CvcT6AhMDz8hKH6Hhyeuo3lqTUcmzI6pY5CISe2UoyatG7w6cGZCq1KF3SrjkDjCi0OotT0kaTAEWEgM_24Q_YpuUuyMWsw4j2Yt8Tm2rOoyLA7TA_WNt_Fb1Fzi5OgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=LIEUU64kfE37Fkz9vMnx-UQhvPSMcWD562upZILP8CI6AzHDZhuQ0thvbOhol9pQURR8yokemA3wkaeYqZRqhRoXvFI3AAOgMQxolViWPJl3mjiyZ9Ap_iZoIt4Hy8dnbTlejUOaS8izstsuoHlnNQj5-NxW4QrwzjPXCdEpEmP4-jLNu5In6yrTY76bHCG5BibEy6qo92VRMHdmKLfQUWTXW8lrJaonxZhY5q97NbEXYCcXnWlz62U2Q0gNdPaB5U45MGs3BYkIDAokc-rQp2kV3UBUuHcGIh-c7ZZak7gwCnCyfnuzjxGvBr_bFS5NtomKSLwb04kAbvy3Fr4E2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=LIEUU64kfE37Fkz9vMnx-UQhvPSMcWD562upZILP8CI6AzHDZhuQ0thvbOhol9pQURR8yokemA3wkaeYqZRqhRoXvFI3AAOgMQxolViWPJl3mjiyZ9Ap_iZoIt4Hy8dnbTlejUOaS8izstsuoHlnNQj5-NxW4QrwzjPXCdEpEmP4-jLNu5In6yrTY76bHCG5BibEy6qo92VRMHdmKLfQUWTXW8lrJaonxZhY5q97NbEXYCcXnWlz62U2Q0gNdPaB5U45MGs3BYkIDAokc-rQp2kV3UBUuHcGIh-c7ZZak7gwCnCyfnuzjxGvBr_bFS5NtomKSLwb04kAbvy3Fr4E2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA96pjZUMXVOYZrap1Y85pxiTT1y1QCcf5KI4RA6lLjWGryhE823AhHi8HROLj6BYPen8q-peduKs77EhxXOEAF4tiEYO9a89rWneXqwvsdmr877H1SrctC0c-pwfwfYHf-DFvfiCVnHADZzLgZMcjBV7BhcWKizFPAuVuTBwWqpMxvrLArslg9kVOkQbNjZNdOk4WrYWVk-jjHoHFpOQklT50DCNZMZkvqUc_5wDsUTv0ezcFV9YLqnXuTyXNnbGhEqCCPhkMdGg1eEmA4mpREYBRDSScZf8cbF7AmJMPGJMoC4lrzCbK4UsTUpxdIQGLQpjGIW19j95l13fvk3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4djIfaKlk_WFozuU_uvTBE6XEcYJTqv2QBRMcFr6egiYkBR702MMV-ebGv-XV3xwvaMt5owdUL1eOu9VZRwtAsOQLVTzwH8Vs4cvxCBZqQgMce0MCUhB_nrXQhK0K5evPyaYOedkzmfvaXbjyjQRl5akZZmJO7HlrAZL6rgXzoVoQYFR-IFauG5GqOHm1SvW-yOAgrF6NSdTti9W677tdrmhjaSU-OitkiZK4JlceK3lPLIw2u7kJ0lu1-lK-3wIzLJ6sCIL4wHn9D4s2IGaqWbIo6v1gFbE9Vdq73K6xy0eHErV20q7KYSh4lSN-B1fIw1-bwcMeghr8wqJYgGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=WoqdEMBJVMnzrkZNpN5QTjk9Qhn_DfMwroGYG6Kjyvhc2N4ghDBIjPXdPYyk1Su8VuaYxSaWmZk9tgnbdSkMouS20MPE4-SEBBjStIPW17DEVHs9iwdH5SZDymQjNlNlGImVlhrFPDuKKGusvJdt4RXvvT4rXT3WUAYQBLsLR9G64gqbYGkWGc-2BxvUOurwft4WbR_ZyBddevsZxUkGBapZoL8Ck3uA-Gd7fF_ThBFwMHJYwO4GFD8YzQ-_MfOjMST2mQizssx7MdTmHbOcrKnIIRsrhm16qqUXJt6NgUiypHcSFmyTJpVvTEDAjJFo3P1EwoxPo4jmmaUh0pGBFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=WoqdEMBJVMnzrkZNpN5QTjk9Qhn_DfMwroGYG6Kjyvhc2N4ghDBIjPXdPYyk1Su8VuaYxSaWmZk9tgnbdSkMouS20MPE4-SEBBjStIPW17DEVHs9iwdH5SZDymQjNlNlGImVlhrFPDuKKGusvJdt4RXvvT4rXT3WUAYQBLsLR9G64gqbYGkWGc-2BxvUOurwft4WbR_ZyBddevsZxUkGBapZoL8Ck3uA-Gd7fF_ThBFwMHJYwO4GFD8YzQ-_MfOjMST2mQizssx7MdTmHbOcrKnIIRsrhm16qqUXJt6NgUiypHcSFmyTJpVvTEDAjJFo3P1EwoxPo4jmmaUh0pGBFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=cmPu9wk3EAxc2Xjvw8LIcRRWt5a-Hotq0pAJhk7MT6_-S7eHQsUJ97VkJ5dct4Y8Gg2HbPlMTNreHHh6srnKR8lLU3lgL2PLnYk4JwGOIDsz3S0J7yG0KAQsIZgzfKH02U_68D5jxscMOk1SdHk9dMqja9IMqn3X034ncrvqjRYZHx-izyr_flx7sTPnSFwhr5wHhtV7bG57VST2eM4izNrXeNl-9esY60vNIsNhi6Vp5KNW09ecH2zV9NacmxDxi7XY7_8VYKvBd96YY4m4qMZCbgqnauPk7Zto583AJ69a4gfsbg3-iTMtQl-g-8POWnqgtkVetAtWUtJfWD_6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=cmPu9wk3EAxc2Xjvw8LIcRRWt5a-Hotq0pAJhk7MT6_-S7eHQsUJ97VkJ5dct4Y8Gg2HbPlMTNreHHh6srnKR8lLU3lgL2PLnYk4JwGOIDsz3S0J7yG0KAQsIZgzfKH02U_68D5jxscMOk1SdHk9dMqja9IMqn3X034ncrvqjRYZHx-izyr_flx7sTPnSFwhr5wHhtV7bG57VST2eM4izNrXeNl-9esY60vNIsNhi6Vp5KNW09ecH2zV9NacmxDxi7XY7_8VYKvBd96YY4m4qMZCbgqnauPk7Zto583AJ69a4gfsbg3-iTMtQl-g-8POWnqgtkVetAtWUtJfWD_6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
