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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 656K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-94143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8MbORB3k0b0q1yqzJUjsOfAcBZZAUOkyliAfCdLFY2gVBIg1_9VkX_CfovK5FUDertbGh7fSnK0WP5H-6PW9JRKZHAe3kMjn9YbXUNYJVin2oRB9xRIVmUmHnvDvoqAgtjnymqfsUHLidSWe3HEqrYzNjTECF1y6edCo3vY_PazM8eSl3MKCOtE1VW5KI2LEc_JukcEnkaNDsq8LWdZIvTgOsk3PIlJiVhT8RP-oe_FUWG4VJLAySIy6JupS5CtchZw8syOOzVDBhhpEyT7NOOdguS3sGbUy4emO7sLbDe5Upcysii6a0GE5X8ANmnYs7MVf5fsLLSGE5VDX1kH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رفتن دیدن رنگ صورتی به بازیکنا اعتماد به نفس می‌ده و بابت خاص بودن رنگش، تلاش‌شون بیشتر می‌شه.(روانشناسی)
🔻
از طرفی هیچ تیمی صورتی نمی‌پوشه و این رنگ به دلیل تفاوت با رنگ لباس‌ها بیشتر تو چشمه. (اقتصادی)
🔺
اینجوری شد که امسال یه بخش زیادی از بازیکنای جام جهانی استوک صورتی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/94143" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1N32ltGBX2mar0cuI70ZFNDFiputQmx8FAmmJSSWqSoQTRRM46CpSmuU0bQLnEEwYxWG0L58BV9q--AcT8p2_ckRZKQUB_7JdcdIv4-zDXUQFWswE_m57Vkzxd2y3oalOu-ynQnK1zBM7hpYLlnVTsy5Gd7NvMmMb37Vx7cEFprBFZDoGfwL5yyT1Q4Lnjax33MabqhXaX8Vejpi9_Q9bPMrEYcbScBpKBxoxTQdXXakvuBKSxugUu0FTEPGu2nZReUYSjbRxiit7zUBKl4974LkLQ840RfBerBa372MGOBhxHxp8lGqkHVlhgH4v1vQlzUds6SioR65SQ_vO8ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مثلث ترسناک بایرن:
👑
مایکل اولیسه:
🅰️
+ بهترین بازیکن زمین
👑
هری کین:
⚽
⚽
+ بهترین بازیکن زمین
👑
لوئیس دیاز:
⚽
🅰️
+ بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/Futball180TV/94142" target="_blank">📅 10:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94138">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTUmRBZs2h4J8eGLVGqqAbxyvgwnrfER4SGwjMbxmZ9eMhvlQMHDEr6cvkQGS469hjp_oqLTPw_lIBU3yIUBFMLwfeIrMbgs93zKggxch2_xae6zbulmFQ4j6cQeGD9Tvc8qN72okJNREAuvnSOEp5oU-MvbsPJ288nbwJZDWX0Rf7b11SBfkwqLOMFsq7GGAecnOGDvIG-R6W9PolsA_jS-R2HAqg7cVtceYqyiIwTZheFuiNXsPYOOAI20X1oBILt2mei3Yr5dgabl26pWAE6vOZFoE1_89TLbiyFHE-Ji8Z6_iOthQb3F-BUfkFKTCZiwgf9Ov26Jikzuq1_Icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CETkSD-JGNA23QspEkr0R4Vh3Gt1d7N-sJ6owRCrfNfE32h_iynRDXaJMADAfztZZNdasQAGlyCt4lbfLjezZfY9qo1R8nlzTxflBvjvWE-C7ztEHi869E_D-V5sKUGFEnfjPmeG-Uav8p9WY_6FIsaDBXg4DEFfLmDtiEwLuEYhkZ0PmT7pzauQKzi2luO_39aMkbS0_swuZ2aOlqmCFU1tho1RwXp6RfRbTRS2myf3S8ZgFv8kEJ8txgvEGLeCeZUn5--CbMgBq-2Kl2SOWFazao4n-VDHXRqoi-Ga7_i-B86gp-VfU8v_7h-1qs6E_cpsNSPdoSqdmsyxZEMX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twHOJs6J0rjBV1O0YTT6m2zI0q7qkmDCteaQI6xcnaxqjunY1dNDOSYeHIlCcMcYpEZfW2hB9H6boiZSUjMZa5f5LhSbenT-bYrs36WbzzNctZ7s2Y6OL8G4JX7Tp9k1ikM5uBamhCnxyWUQSaZ14G7KDvIybX2Nj3w83ISmh3ZsIW7WDi0FwS2aIyPMabEG3U7anCQfRTKrsq274iZ_jz_ypjDJZqDiNioHHtLy1xxEpVbk3vPx-QeOQRWjb5VjqME6CPYQ9-cyIj3k71_YAYU4N7exQ7LJ9gEleCI_w_v0FYDkvW2GkMh2rxL0y3V30iiscwB6eueyDdM-mNbvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBZFs6rZKbXjrutDHphYhzW96OqibnvDcNAXhf8O8j00th6bSlv0xGPbUEdDXk-smvI6bSa6XeVBhul7g0V3TAMA8nUIT94B4mjntYP3SBZeTSbruTQDcGhGHgo1T0QBxwmI0XAMBA4kME0VDANVMKfLpCvwgBjBsB1zyb6YckQWCDQi6CAVD4yTSolP2suz4AULOg_MljmbaIajhnMtILdJsY9I8OVyzdmJF4uZXKQWRfVaLZYB2eT8fYq2r_9zHrMjXttuUShGi9wZuXd9Na4nLvCmFwKfmzf-G9kch2-j9gl5qbhPQTvRmLKxAubzs1KWFzzTtElGsAk3BAwTVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
حق برزیل واقعا قهرمانی جام جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/94138" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94137">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=S3x-DKRFkVcUCgri6bVJ-DBasNzucgFvA7FufD-8lHZhpoQco_o_LY255leKJOZ6Yg7bDL_MWFFlaFM0O7gmFUKiOpiDhDwqrylh_kr3bpMwXo6znFc78i9c_FM07uLKceKCnz6tPrmwLYS1bSHu1Wn23jAAys3ZL_wFNnTtkbKyDaQkghCQ6RpX4TZuTArOijZL-WfW8BUkICD3nrIVKApvjWQqJVX0wGiTQwiMBhLyrRpUFFeS26gXbl_Y-c5ODJlZ_ZNJsfZ-g_jxGe0-Vir3MZL-CSnNjGC0MoZnqj72KeCVgakk-FgxTRz0EAqBAIq3S4sKdfAn-iqfvTXxRmQZeT_9NBVZrvlqQajJGXNE1thNpSVSR-sF6CfSfN3MsNOYJbGXXBMqvelef_2w4UXN1Ckz2kUqAkjmhkM3pv3osoXF9FE-Lxdwi_4zru2omp8HkwnpfrLAGvClOP-YploONNbtK-yEH-nlSwLhIVET1TpZzm6_sUUwF20U3fVZ-6FmDyM7n_mxI1IKRCD2xCKwsgAcG72oeXbKCPdqdp_neA-MzEBmVndmqngnQNbD1gITu5N0t8m4fr6wLUyaoUstY7y9M6kdu6qJ__DWMN78MPOs5gQpcZjJcVJ_RgKNs8WZEjTaNiucj8JgyzzNpTgeWLKRyQkHqxejNbE3A7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=S3x-DKRFkVcUCgri6bVJ-DBasNzucgFvA7FufD-8lHZhpoQco_o_LY255leKJOZ6Yg7bDL_MWFFlaFM0O7gmFUKiOpiDhDwqrylh_kr3bpMwXo6znFc78i9c_FM07uLKceKCnz6tPrmwLYS1bSHu1Wn23jAAys3ZL_wFNnTtkbKyDaQkghCQ6RpX4TZuTArOijZL-WfW8BUkICD3nrIVKApvjWQqJVX0wGiTQwiMBhLyrRpUFFeS26gXbl_Y-c5ODJlZ_ZNJsfZ-g_jxGe0-Vir3MZL-CSnNjGC0MoZnqj72KeCVgakk-FgxTRz0EAqBAIq3S4sKdfAn-iqfvTXxRmQZeT_9NBVZrvlqQajJGXNE1thNpSVSR-sF6CfSfN3MsNOYJbGXXBMqvelef_2w4UXN1Ckz2kUqAkjmhkM3pv3osoXF9FE-Lxdwi_4zru2omp8HkwnpfrLAGvClOP-YploONNbtK-yEH-nlSwLhIVET1TpZzm6_sUUwF20U3fVZ-6FmDyM7n_mxI1IKRCD2xCKwsgAcG72oeXbKCPdqdp_neA-MzEBmVndmqngnQNbD1gITu5N0t8m4fr6wLUyaoUstY7y9M6kdu6qJ__DWMN78MPOs5gQpcZjJcVJ_RgKNs8WZEjTaNiucj8JgyzzNpTgeWLKRyQkHqxejNbE3A7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
💥
وایکینگ‌های دیوانه درحال دلبری تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/94137" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94136">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=RsP6Jd8M1DAPfktiHJOJqpdzhsBzEW92LfLucJClZiHw0Sa0MxqxKDU3-RsR8k5v7sRPsAkmJnvTZL0s8aagbZ4LbcMrC0iWJLORj1ih6Ryx9o_8grn9YT3Um61l8frJfGSVe6cBQvxc1-A6hanssqiMSAh7AjRLKolmUMOEBd8vs8DuaUvxprCDZTbHsCIAPod-AB1o2rxe2Pa803WEEb0twaJ2OwP2xJpwjYpKzKVDuLeE5T885QZf8ZNJPk10Mpfui1nH6uBXQ5ngX7QqKmAzeMoyghHr_SaDgPuJMZ8hy1a5xJV5_Jf9cAtegk9zQ0BW_Dqy_j-jBRLxB636sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=RsP6Jd8M1DAPfktiHJOJqpdzhsBzEW92LfLucJClZiHw0Sa0MxqxKDU3-RsR8k5v7sRPsAkmJnvTZL0s8aagbZ4LbcMrC0iWJLORj1ih6Ryx9o_8grn9YT3Um61l8frJfGSVe6cBQvxc1-A6hanssqiMSAh7AjRLKolmUMOEBd8vs8DuaUvxprCDZTbHsCIAPod-AB1o2rxe2Pa803WEEb0twaJ2OwP2xJpwjYpKzKVDuLeE5T885QZf8ZNJPk10Mpfui1nH6uBXQ5ngX7QqKmAzeMoyghHr_SaDgPuJMZ8hy1a5xJV5_Jf9cAtegk9zQ0BW_Dqy_j-jBRLxB636sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
دیشب وسط برنامه زنده عادل فردوسی‌پور پاش گرفت و اینجوری داشت بگا میرفت هرچند طبیعی جلوه داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/94136" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94135">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434481e09.mp4?token=DX_4KabBVDfb4GykVcqbmEPfTUoXnrw8-hdxGVqDKfrizjqMVDIzrZOA1995OhBH2zRQ8fh9jCrABMzVG4i9A1M96R78ciA8Fl_qnd-e4MsUB3EX-nSgjLjm8Jk5gtlrioiK_HJQ_2OMprprmUyjmP7sVvHBiyBLoPY-nc3aimyRVYUOUk0rbjJBNow-4vsS4o1-_3NGXPVzLGKRLKUMGdAvZFnGTmzLjfGR7Va4tSAekXZHrDe2LjISAMEpjv4cKqiwfUH8ZCGFNClInPn4THj7SdiDhPsRAJFvsCRJDvCjR6NU237imlTYVDifctiZkBy1mit2Tu3zoUoX178OeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434481e09.mp4?token=DX_4KabBVDfb4GykVcqbmEPfTUoXnrw8-hdxGVqDKfrizjqMVDIzrZOA1995OhBH2zRQ8fh9jCrABMzVG4i9A1M96R78ciA8Fl_qnd-e4MsUB3EX-nSgjLjm8Jk5gtlrioiK_HJQ_2OMprprmUyjmP7sVvHBiyBLoPY-nc3aimyRVYUOUk0rbjJBNow-4vsS4o1-_3NGXPVzLGKRLKUMGdAvZFnGTmzLjfGR7Va4tSAekXZHrDe2LjISAMEpjv4cKqiwfUH8ZCGFNClInPn4THj7SdiDhPsRAJFvsCRJDvCjR6NU237imlTYVDifctiZkBy1mit2Tu3zoUoX178OeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
👀
منتخب ایران باید این‌شکلی باشه تازه مورد قبول مردم قرار میگیره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/94135" target="_blank">📅 09:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBIhvS6zeN1ewifCEfTRgdWyA2aqnX2biB8pboGMJHpJB138JEyl_eu_yfeVhU5K1gKwpZAzUTyQ5ISv4kfszZ2gaSr2fkxV831I3n1DE7-eGwtcphceoJS2jJqL3Pz3j-8rpFh-me6jOQt5VgMjyVJ5DQKPxf4ozwGW-8PiPXPoD_i-THaNj4mrLsKE6mQeh9Dmkaj0TIpzpo9RoEd_H6o_xmDSUjpSpJpOOrfYLHUd1CuDOUGfSn-CBBc6YzXG7W1092YUgnXh32ktEKvba8FBb8YN65yVoAgX7w6FAYyt4-JvVmY2BCTsxvqiqywPFgN5RyaF_-8pz1o10CSY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نتایج دور اول جام جهانی:
‏
🔥
۲۴ بازی
⚽️
۷۵ گل
⚽️
یک هت‌تریک
⚽️
۷ دبل
⚽️
۳ گل به خودی
🟥
۳ کارت قرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94134" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94133">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmqeqc7_dMEDhE3GbcENIZFfMg7loRSYvKGvoi9OjhPMCQleFisBG9EHyf6X-asNj15bC8cHr1bUv_2GNVNoUt6eO4ApO5XxZFVO0rCryPHWbkAY0JyzhXZ5DBzF3kcKEdSHHWL9eg191szpSZZzmnIl2nBIgcthcsoHIeRaEQfRdBJJcm6Ob1ppvGAwj02kd89UWiCglATOKD0OJ5TPisYpM2eppatdCn2E3QUSulJpetoTMoQj6DRTu0CpQNREKPr2biwiOtcGs91OmPdi1X4UpZp-vCl_n76JiP7B2rijb6Mme28a2g7dotaKAndBcCoo5yS4MmmYNheY652UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مثلث خط‌حمله بایرن‌مونیخ تو دور اول مرحله گروهی بهترین بازیکن زمین شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94133" target="_blank">📅 08:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgiItb9ImENglqsvcTZV0OHNx8yKfS6cO-Z24Xs12ntCaC9K6DXGyY4vN965zl8ndFWY4Gwsr2PFdEjfeS2P9_YUPJIZqXjsItB4YZe4AfEjQ1KC9dTT8qa3gqtS3kUOn7slddJ-YfjMK56ElS6io2elBQ2m29wfTWaNXLzilzLmadA6qAGqCLD5fSQNQAy0o2a3EElNBNCmjrAnZml5kjztvZFDegBFSpDPDpUvQi2-5IKf9B7zdh3RemOI3e8Hov1OmJB4eKNXvezYAPNzVBDZjclJqDp150asmrRRRqYh_DZtSVzg8hRxyRd9lFLKCgz2G64eiPS1h8xV5to_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی بهترین‌گلزنان هفته‌اول‌ مرحله‌ گروهی‌ جام‌جهانی با صدرنشینی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94132" target="_blank">📅 07:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdzQzNL4c2tQLsAWXLjWYDo--MOTD9iu0H0auaUufUFLGA4XYJlh1mefTSf1WcikAW32-O-6T2UihWNFHdnyozCKTFKZ_IyG8dMCuNN--Lgpaq2ULQGTXCCDjEwKlrHOjM6P0vZcqRfO39HL5jpcZKiFN-La7spmqBbmRKvn9SHly1eXtx1TTAAiOC5iBgG5j0Ce26gMR6vyrmyA5-OvmcuPsO0TbRtht8q-nacbphXwrqWmgegG0x40mCVEEKZ7J90xIsyPEKnZ7J-bxdSN0a1heJJR1esLR_Qq1nE5_rL8MVprspA7fwt0Z0IzQ5xhkI_-K_LPBizVK3mnkExycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی برترین تیم‌های سوم جام‌جهانی تا پایان هفته‌اول؛ هشت تیم از دوازده تیم سوم مرحله گروهی، به مرحله حذفی صعود خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/94131" target="_blank">📅 07:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYauzoyjOMlbT8YB-646RWiryDveqkmYg9gQB0-VGwxbctTtgwa9TlubmYao-R0koyHJgruM1RKKmnPYtvc-BSanX07LM3LR1O1KE0m4ROjcMufValkjkAxR3_sMEt7kVOOJp3m7aivOAaUwyX13uUuQmc5QSDE3pvDEllnGL8prZ5kd-jeC31PgV3lrRD4rz-gZI8ZxP9bz4KR_AtzFfnJRLpDF7d5LgOmDwWpvJKSLUhR351l2pECeJLYq4DkpihT-6KkIaS0AREsbeMEyH7DsRw7881XQ57xLVs7NsFg6eT7GWC-cYBPGS5h1zhO3SKjzNUq74gDqx3Jw8kT_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول‌نهایی ۱۲ گروه‌ جام‌جهانی پس از پایان هفته‌اول مرحله‌گروهی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94130" target="_blank">📅 07:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEwmI84sz5fPop9o9zmHo1uDMbkBXE0xtqV4Oxg3JgANVCh0SNvlGjCkZNW8Igija8fUeiYLrryVYjW-h_DrAu3J5fK2HfKrBRmh-5yYgf5mvK-JH6ImMYCqW496LV8HlTiEi2xtTtR1_spqlX60sPo6JI8N_CP_QfCkLATf6l_b1v4YOmf0YovL19qBbahKPFyTRVgMzL3fSt_wEOOsEFkjc2b96uOK-KigWNz1U6OUm5b-sFzy9Y3cGOkFLuqeU2rbwy2YPFQHyz0CJJ8Sh6UBwDFd0z6qZYGu3j2QVHU2f6sNwGWjI3RiaAvf8-iDcGiZT2wKuWBJYvSsjtu5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لوئیز دیاز بهترین بازیکن دیدار کلمبیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94129" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP0eIVqf15GDpzxv-iy3MiCze4wu6Ccs-QejgB33TQPrXKwqecyRR5Ze4qiM7EtBgRrRl6EAPMoittM7QW9FLAhOvy-iIyndxN5sEETpJrxQEq75-JSVGrGeheEx0cG9YSBLHBOKvqhc_grhSZrmSo5vWULNLJ_2azj9DAEHqXZI6niI8p0ZRSM_Xb25cETgZ9mpiPjdy4FrvAwdg6F3hsefoB9tiMTNHC8-_kZPcaGWTPOXtpzCnpa1flUCf3qPJ93n-tdQTUYp89O1PTPbvFouUa5niXisxC_MX1zosgTdybMSLnUS5owj6NkV_7HA0_riKmgyPYehgP48jXIJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه K جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/94128" target="_blank">📅 07:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی رسما به پایان رسید و بازی‌ها در هفته‌دوم از امشب آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/94127" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|کلمبیا
😆
😃
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/94126" target="_blank">📅 07:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uva9HhSIhjhR-9iFyiDKQK4XHnZXnuX-5NCdPHRpV_kUsR8yBFP8Rg1O4f3qcdV1cnf-Umz2hs938Enr47FpPabHMt6s2fPxJA9TwXV5ADWqQN_m-u3Rq62CeMKWpaMHKHG3KJS5g5ilxncEVCMsdJ33ZQkJwieUJ23M4_RMgRp9S9A0_rlJS9IyCqRfhF9Gw-HY5vrDuWKelevbDXKvK5ESulPQ-3SDZg5SHFKt_WH8GyRRYCq1qgFfRpmhY993_-kMh3IPiTlJxL1Lz0j8ScOQrgAq52X9eXcrCwjxq9aRbVyIBJNDhjeDUiP_sbMhBdVA8yX44rNlzHkoScAJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
۸۰۸۲۴ نفر بازی امروز کلمبیا و ازبکستان رو در استادیوم آزتکا از نزدیک میبینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/94125" target="_blank">📅 07:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAWbTfyUXx7Od8ITHOrHAHdkWHKc0X9o3KAadinCLg3OgU0lIIF3kQ05hmk1wfP-Jvk9F3ANY7-6JfjEWyRPZGuLRYAdXuToCy_e0rAELYef1JFnjmDnCyY9MZ38-YBMfFZ5hDg43nUx-hhEQMWLWVt9Gat1ieId_Gk657YcPg4rYDERQVtROmnJzb7OOonatDwLxgt75V9W_vF9iWfC10EQeZfvwILKo6u8xKr_00p1V8GsoT0gcSVswwb3i_KiYqdIeumM33JfMZBDmEo_lO4sb8zDuFo1521qh0gMQzPlrxy2QXs-oEA62SQcKys8UAG6pr-21lbR9-bRKp6Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
تصویری تاریخی از امضای تفاهم‌نامه میان جمهوری اسلامی و آمریکا با امضای رسمی مسعود پزشکیان و دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/94124" target="_blank">📅 07:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=F9Oe0Kjkpx5EQfnM0U2U3ZfRzt2aRHGhZSvSjJA0vTT5DyEEkPHMg-_SlxrTNovb7TLMNs52MnKO2XDAuvab-rOStZOv5ir4jR9mKtNXW5O5TDSZIeG-NRhEPDK0pHfgGnBatS1d14CrmQr1_QCGYuQuq-jf2BWokSfsWwBZq2qtbKovyEXWDaMRalxRPl4-2iFeQxDh64FJF7-YSPRbfcWYXlO4RPGm-Rnh34e8Yuwm3NpaA_kfvVxQySQdJ3cPboPs9hMalFzdqKBbfhl5rB3oeHL5gEa8IZrp5-SEbIKQV7iLBzlwOJCIbL5fS3pCPIy9w5BWW29keXxJPc0QnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=F9Oe0Kjkpx5EQfnM0U2U3ZfRzt2aRHGhZSvSjJA0vTT5DyEEkPHMg-_SlxrTNovb7TLMNs52MnKO2XDAuvab-rOStZOv5ir4jR9mKtNXW5O5TDSZIeG-NRhEPDK0pHfgGnBatS1d14CrmQr1_QCGYuQuq-jf2BWokSfsWwBZq2qtbKovyEXWDaMRalxRPl4-2iFeQxDh64FJF7-YSPRbfcWYXlO4RPGm-Rnh34e8Yuwm3NpaA_kfvVxQySQdJ3cPboPs9hMalFzdqKBbfhl5rB3oeHL5gEa8IZrp5-SEbIKQV7iLBzlwOJCIbL5fS3pCPIy9w5BWW29keXxJPc0QnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌دوم کلمبیا به ازبکستان توسط دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94123" target="_blank">📅 07:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=m15PrSWO8qfI_1BlK5YhXM_4wDurBo5dUspwrU3znl9AikIc9jNp3q2O8JpOgAYjuQ2JcKLU4jllb0LnmWZrk1ZMdcNgOlRzGgDqM8KBj-jw_wthcshn1tPWV3O6dMmq5MiCVt4F3a4-nbnl6rPfrOQQmy86ik21MZXffeerme7S6dg5vuYRJYD3N44-P7zuMzl2YAdTGfU9q_zjLHC1De8Tml6RurRdw2DVAoCqzj7OR-97Q5nxgPRGPa1ew9UFaOXOQFS5HLSbisiLTLSZYNCsGqteKb1tRwBkwBnrRm5bZr8zOu5GpJzrEZX34YrdoBMjChDC8th30yd3blfpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=m15PrSWO8qfI_1BlK5YhXM_4wDurBo5dUspwrU3znl9AikIc9jNp3q2O8JpOgAYjuQ2JcKLU4jllb0LnmWZrk1ZMdcNgOlRzGgDqM8KBj-jw_wthcshn1tPWV3O6dMmq5MiCVt4F3a4-nbnl6rPfrOQQmy86ik21MZXffeerme7S6dg5vuYRJYD3N44-P7zuMzl2YAdTGfU9q_zjLHC1De8Tml6RurRdw2DVAoCqzj7OR-97Q5nxgPRGPa1ew9UFaOXOQFS5HLSbisiLTLSZYNCsGqteKb1tRwBkwBnrRm5bZr8zOu5GpJzrEZX34YrdoBMjChDC8th30yd3blfpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
لحظه اولین گل ازبک‌ها در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/94122" target="_blank">📅 06:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لوییززززززززز دیاااااااز</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94121" target="_blank">📅 06:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کلمبیااااااااا زددددددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94120" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94119">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوممممممممم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94119" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94118" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فیض الله‌ افففففففف</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/94117" target="_blank">📅 06:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اولین گل تاریخ ازبک‌ها در جام‌جهانی</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94116" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ازبکستان مساویووووو زددددد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94115" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگلگگلگلل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94114" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
🏆
🇺🇿
جو پرشور ازبکستانی‌ها در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94113" target="_blank">📅 06:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=GGaLX4XWvLas0C70uZWKDsOj7uKN3PMGpVgIU7QfNBsU6oRuTn19pIpnN2Ne-5vyEkXLkEMSyY1wfODrns4wRYEmPcrbxpp17bru7tW1X8YB_lGrl5G2a-MaN6dMhFue8QToTIvtBusR_Ncfs7CTsVSr-NXMonLnXyRY2bBM9_EysEWV5bxCVW3R9tJ3jrLL4Rubb0b5ZGVjRRK_xuBhx_9UV1VeqXi23Mda6Cs0LtNHdVNiIWXQrxtG5GCyTWEhwCCpmt7JxTVZsGmb-22B6lTozB6LOEha9GHnhPdpS9Lvf2GOwU_FuYyAvfR-fX5XLeaOhdiE9NNJuIJ6HiTckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=GGaLX4XWvLas0C70uZWKDsOj7uKN3PMGpVgIU7QfNBsU6oRuTn19pIpnN2Ne-5vyEkXLkEMSyY1wfODrns4wRYEmPcrbxpp17bru7tW1X8YB_lGrl5G2a-MaN6dMhFue8QToTIvtBusR_Ncfs7CTsVSr-NXMonLnXyRY2bBM9_EysEWV5bxCVW3R9tJ3jrLL4Rubb0b5ZGVjRRK_xuBhx_9UV1VeqXi23Mda6Cs0LtNHdVNiIWXQrxtG5GCyTWEhwCCpmt7JxTVZsGmb-22B6lTozB6LOEha9GHnhPdpS9Lvf2GOwU_FuYyAvfR-fX5XLeaOhdiE9NNJuIJ6HiTckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌اول کلمبیا به ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94112" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کلمبیا زد
🔥
🔥</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/94111" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94110" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWvqtE4-FsxXc41zJr-ZeKY6-XmtYFS_FIYGfLuZdru-hRIfjL4egQDP-LSG1s5d1XVa_14GwZtQK_pVtvk0fTuFR5-OIdEtUvURWgPxxsuzQIZfnPEJYAA5xxgpyFXcACCo0QWtqi4-yAmSGll7lobXG5o28KcYbaUFaw37sXURk3pW7pXlSzsXpHIlfT8TUGddfP91vpJISlMS9M74RC8qKfPfAOgMvc5j_u2CaPfpKKXRBxwJhNZR4j_TSSWsNVMe-NYO9ZH91LUa2WydQqIYbROc1AKIky9Iisyr6lz612WBfPUIVyJEZTZ8DgJPJwhJeSW_hMGfjYGJ8yqCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی از حق نگذریم تنها برنده بازی دیشب ایشون بود که زندگیو برده..
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94109" target="_blank">📅 06:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شروع بازی کلمبیا
🆚
ازبکستان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94108" target="_blank">📅 05:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsOEZeIdnpfvAGbxoJD5Uj42Hd9cXLFji3jw9AMNUwxpiSk0hYAi5yR2Z2TvRMNXObNXGEfkmCx71dx5JgAqdfZaBq9ZRqeBSiGPwbDh5tijW3aFqZN7ylJGWjkYXq5dR2GpbptFay74nutwyKh5w_k24E2wzSTb8tO2GGiEjJsTP4XMxuy2EjiZlHvlIXmfV5miJ2fnnzdTl3v8gJjqSmeIx_JYSIQBenuAY8yDHGDkHTaVrVowcUhAQvWK6elUGwyIQVV0A_WEjEFGmo1Ic1HqPxraBcZ-ncd_GmzlwUiXKSumnOg7jGLs5Xdkz-p8gxGcPF1Nl_dpbIksuTSd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر جنجالی رسانه‌های اسپانیایی از کص‌ خنده‌های یامال و زیدش بعد ریدمان جلو کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94107" target="_blank">📅 05:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xd1YHz9VefHPKg4bU-L8R3INPmoBMB0NDV1k3W4rGe3k1T8iHVWhHaEyIlgUGOc5Z1pT2AW8TsJxyraQMmWNmCj3lv4iELFd917GIaHjVU6qCKQiN8OhPQtuL4zowILQL0lODjhCnxb_ptTlGmn7L7CATe7q1mrRt2XIFnTitE_YkVp8Zb-oITgcZXK5Um68ATtt8x1GdymIajiwfW3EmQlDJ5cIU0DGgDXnWOUiVTUz7H9IrvuKY_nnShG7de1pTAzvMpuyv8LKz9icm7EW0otZBG9pKh_9h8s57Oga1yaSeVh8-tLfUgUDm61OLAl5pBvMJVNl5XwZbHH-V6eYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxXHZiFa1AirF6PaYEISpEvDIEVKY5oRm8yWMrdt2ve_7c9ri_-AMXZ-Tr_SusZudjxToWR9d9JoNLGzmoUtM4mrHE-wrstZnYx4RQlfaVS_mhmL24DmnZQd8ONeuT78SoXse1wVYjG_0F0xC81uctcC4K0JYpiLrgTw3wMgoVY2ZDG9W6uieWw6K3rfEWAn-01YhXNo9LzM1SvIIjZSswbo88VUP_9VIvpi74iZh45rB6Mvmndn3_ij2Z3gw3-VgVc0ppDARdvMmjw3wXKe0CRA5BIeAyGbT8Nf8ul-OJwvtKpLYmQt3Rrql0pBTL4PUxgrRT54OTl-lDDnpt2gQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">2014
✅
2018
✅
2026
⏳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/94105" target="_blank">📅 04:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4VEiUL5uGnWIVbIIA3U3GxO7QiFHVUdCBtwokRjIIRv2YVKVtyauCFkEm0H4ldqf9zXyXik8mm_QGfjxCBu4NxK-78Q08NrQoXJtxeSh45Sz_rVbm0uCv1GPAj3at4NEIe84I2HsZ3YGW_IL9-m09_fe4hT369BrGUHliyXaIFr6payZYIfDNNuxXYmz7olScFuLDDsIDNslEU_kagxIjUxWImNyYhR_byvQHviO2_bfL5UKXVn8VnYVJiqPIsbWHF-u8Eg8cniiLBxS20DVYdvIHdNZs4mmrTkaZE3AxN9JqFjQTdTVxirsaiM38X3ze5RMAK7c0cuO-JPN68umQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
مصاحبه روبرتو مارتینز پس از تساوی ۱-۱ مقابل کنگو:
🔻
نتیجه خوبی نگرفتیم اما ‏در جام جهانی هر اتفاقی ممکن است بیفتد؛ آرژانتین در ۲۰۲۲ مقابل عربستان شکست خورد اما سپس قهرمان جام جهانی شد و اسپانیا در سال ۲۰۱۰ مقابل سوئیس شکست خورد اما سپس قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/94104" target="_blank">📅 04:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPBgTyfKGe1I4oQcaYS5lClFbKJDG1rzQ7XjPm5iHgYrk7DXgEfLdYU3VDIwY4C-MUbdaIX3FmZHGZOehXlPGdbBZVutBgHT3QJ4xYNanDFHof7xNb4it5Dg7OJTRRbaqdYgYe-EF4DwGWwJS0fRdfXw-zHYv1Tm6mtXrWq6hqVjbojx5C3CZFyK-M3LDDdxlE_YF3lZz9cpajiIsCSVy6OzK3q5UOzcTkbDwFPpxXD_i0B2RFVMBegIVQJAZ0CSbzXgwO70J1ppz2LkVs5x7VtE5ilVgtzfBY0BDfQ7oGtm3izrOuaYyyIvfMlKczk55-DPJcEfQqV_a42tmaAP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇺🇿
ترکیب رسمی کلمبیا
⚽️
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/94103" target="_blank">📅 04:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTTuo7I0twDdOvuzXCnYTcUu4oiK_busTD84PmjAeAy6JCgt0HFN0lKIxQ6c8gWWJP7SkyzcoiYz79zmHyGzpdelVIpfUD2V0e_4JdF4AbfB4PO4v10jTQHJN7soRbULkLAB3e-yEoJWYKPtPs8lPYvRDjqtMR2AF0hZtsOfGTd7nOADuP7ejXHejjbWx07D49pjPlhFQcEXOA0KYrEkPEYyK8kykMJEag0PI3vNrRt6J382YyHZ3dw-BM8VsOSseLN-P7-cNa7IJabx78MvKjvZWiaOpO6FsXWtL5GoFzzUVvjYj83Sx2No2d5PVEeegWbMbtSo1lb1CZNh2VnLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94102" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nicd-cpmh3ss4CTuAGa5Ch8GMzxxmkG_DFhzAQlmVe2vsMbvCPBnsbV_1mRpR0YSRjcDV0Ao5iXMYDFk2EwgJp5DKKNHiz5c65PuRvGGITsPUEEaPLZyxv2AUva1HbTMEwRb-F9peIpzYMo4gkp8ky6MCWQyXwzmX8_QQoyp_xD5DGiLwX30-oV82wa2SJrtQY_simp2i_Wk9wrtu6ndy8fMqoV9dOWDf9GdLmSU5WsiPsFLHVkyjFENbTTh8p3eEKPhyg06oyKhwUoGbZO4aQvUpEMquCzNgu6cSzN32Qk1rXngav9cGLmMB0p_J5MZos4_wCkr6a4ifp68Nu5A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | اتوبوس همیشگی کیروش با گل دقیقه 95 به مقصد رسید.
🇬🇭
غنا 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/94101" target="_blank">📅 04:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=pV53Srx69Jd5gREB4jWF-Q-pQQrWYxva4OetINPCAE1qTlJyLQWRmDnWbCaNcBxleqGUnmUg-Ht3R1HDlKqzzbcrN8KSFr9P1_9GbeqHCdTfz1KBDYCEGM_hbRAUsaXe2DHh4h5v0U_sD7RlyoiB1unu8GeK2kowuZZHaTPrVWIjhdrvTqp7NulrK4YEOQrxKn3d5_q-UJV007e5y8z3cZgsxSqpAG7YhDNPfRHqC-G0HA-P463hLzxAhQkoYjJtCHFDVMKqxhl2oyK9pUggJIAPC9jgJ-w2shvqmMFR-qSMrV-d3ZuyJ94g8tUPCvjGggD8thn0H2glit9jbKpb21rG56a0nX4l3e_H7Qc93BqP8E8uZWtQw4F--itQqZW0wGfQYwrfJl46_6jY4qGygF8sV7iyDF8AtAgIMj-7Ew4oi0sRTqg3qTsn2MNipkMFaPhZa3bTd1fF8f5tok2COyE-criLSthA9qjttWs8QOqivrHNAEjiI-Tq0uEMiv192amqcX-qnJt7zdz_Bt5TFcI-xQpTJeyZ53E_cIICcpLHxRhsbDwzTUteDBjECULKBC7YcIQT_-7S_TavQ2sOXVAtc0pZTqlf2BwiyoS3y2s4T8uIuDGSof-qodxazd5h-4O3nE5w-FS3o2O7Ec3tg5N_ECEu2KvYqSJCFdX51Do" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=pV53Srx69Jd5gREB4jWF-Q-pQQrWYxva4OetINPCAE1qTlJyLQWRmDnWbCaNcBxleqGUnmUg-Ht3R1HDlKqzzbcrN8KSFr9P1_9GbeqHCdTfz1KBDYCEGM_hbRAUsaXe2DHh4h5v0U_sD7RlyoiB1unu8GeK2kowuZZHaTPrVWIjhdrvTqp7NulrK4YEOQrxKn3d5_q-UJV007e5y8z3cZgsxSqpAG7YhDNPfRHqC-G0HA-P463hLzxAhQkoYjJtCHFDVMKqxhl2oyK9pUggJIAPC9jgJ-w2shvqmMFR-qSMrV-d3ZuyJ94g8tUPCvjGggD8thn0H2glit9jbKpb21rG56a0nX4l3e_H7Qc93BqP8E8uZWtQw4F--itQqZW0wGfQYwrfJl46_6jY4qGygF8sV7iyDF8AtAgIMj-7Ew4oi0sRTqg3qTsn2MNipkMFaPhZa3bTd1fF8f5tok2COyE-criLSthA9qjttWs8QOqivrHNAEjiI-Tq0uEMiv192amqcX-qnJt7zdz_Bt5TFcI-xQpTJeyZ53E_cIICcpLHxRhsbDwzTUteDBjECULKBC7YcIQT_-7S_TavQ2sOXVAtc0pZTqlf2BwiyoS3y2s4T8uIuDGSof-qodxazd5h-4O3nE5w-FS3o2O7Ec3tg5N_ECEu2KvYqSJCFdX51Do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول غنا به پاناما در دقیقه 95
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94100" target="_blank">📅 04:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حرامبال واقعی</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/94099" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتوبوس کیروش آخرشم کار خودشو کرد
🤣
🤣</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94098" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">غنا زدددددددد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94097" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک دقیقه سکوت برای اون دسته پسرایی که بیدارن و بازی غنا و پاناما رو تماشا کردن.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/94096" target="_blank">📅 04:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94094">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ct7z8q2iZ3Y1SfT_OWON3NyZDupxtZ_HK_TxMdJIg-cCmmhZj2SZmiU6WWbLRyrJpp6Mlmy5l7lLzZnnNGy2MtMxTgpT2peo_jfejY42Zm-pRuF4CEhmSH9lyJkGNVq8wWn0drOr00x6HNvVtrRTrMwX2uINyZT9et0QFG1QthRs-vMu9Vu8ZrhZeIEmV1ykxAUTK696YAZdCmFPkvdC8nfzk9AtzTECAY0Cu-eaz6dXrVx0ztxqx5rSQr8nbEixD5fH07kZG4zVaKhCjj_qyDhLZqthcIMfSDN82twcz0U_hRhaklkmLXbNWISycNgKUxQ6l-8vt4ujGGr7yWUthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFDQscHDxQUs46RbFYu_BMLc0I1X9CoyzKeG1yIsnC_8GDOTr0FfMnfioJLrZcLvUEWm53DPRnGOPRRAZTiLCTsX1mrZnaQ0wb4eCZcUhEEzx9ROVSxzl-PBiF91n0EdMCDPDIPzd9bs_xEZovFtTxBVbS-SA7xHNKqEBVHj-AIcCIDW66V0s5jEjn4KZulcFhUEDEcMO601VNJcvsN8OO845cajcExeNpK3b-JfTOIGLogY6Nl1B7fBRmPjeg9Tx2vIicQNFiBaTvNWNuIdqXtQUTfW60m8l-HoYijlZYKN-eUuKdSuVhvAm_Hb2HM3-kGpa6sgJL7CmIbKUs4lzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇨🇴
🇺🇿
ترکیب رسمی کلمبیا
⚽️
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94094" target="_blank">📅 04:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94093">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb68696e35.mp4?token=Nosb8PVyXrmM10Zqo0ZtKNlDXLCo3PyRVDrxV-GfwiIsrAqxf6fWAK1GtO5gDjuCGg65y7R6N5x9i9SUcaozRElq1Qcn_JF76wLI0b9sg4Ob0XQh6xRKsMNUEl2vq2gNH-_ysEU00K9iNGpZYOdv3p2BYHJ8ehm48IEqgIm--1FZxvOJFArjixWiZ7pPFJq4FVU3qFIdt7J200kkqNGWZTlBdf1u7_icNnifvm54nuDogueyzv5C7WjTTKZcC-rQbWoIQRxfez8avFUvv41CS4ZOM0BKdiWV4zZd6-7mxwOkkP51cMGi5jsa_KNZzfQsIqvkGvoCpLceUkutLtNgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb68696e35.mp4?token=Nosb8PVyXrmM10Zqo0ZtKNlDXLCo3PyRVDrxV-GfwiIsrAqxf6fWAK1GtO5gDjuCGg65y7R6N5x9i9SUcaozRElq1Qcn_JF76wLI0b9sg4Ob0XQh6xRKsMNUEl2vq2gNH-_ysEU00K9iNGpZYOdv3p2BYHJ8ehm48IEqgIm--1FZxvOJFArjixWiZ7pPFJq4FVU3qFIdt7J200kkqNGWZTlBdf1u7_icNnifvm54nuDogueyzv5C7WjTTKZcC-rQbWoIQRxfez8avFUvv41CS4ZOM0BKdiWV4zZd6-7mxwOkkP51cMGi5jsa_KNZzfQsIqvkGvoCpLceUkutLtNgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
شعار مسی مسی هوادارای کنگو مقابل رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94093" target="_blank">📅 03:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94092">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a621f46e4a.mp4?token=ij1ujeKxoDqsnhQE079U8-b_pNhangljC8lU0lVI3PCv1xFLj1_xULgYEiaWtymNZa9ia-YBoePKDYo0HAWsxB0huGlzLi373QtPDyGTC6O9Sd-M73wzRP2zn0AGUoL8b2BGNccJqP5LM8Yq9nEqCDakcV50kzrSnlPz4o6_VYEloU9GRhjFVOCAWar3WiOdYD3_QtqaNhHk0iY0USJY7-gsb-rl5bKXGweXG4mqUjtslYsROMYkMcBApawgxCO5hV2C7MQrpvXTWIJEqVavSbXzOe8oTNqfUKcI5ZSrAnr1ynoPEongedK-0BpAWLfhe87ADlILb-4aWcgY4XHkPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a621f46e4a.mp4?token=ij1ujeKxoDqsnhQE079U8-b_pNhangljC8lU0lVI3PCv1xFLj1_xULgYEiaWtymNZa9ia-YBoePKDYo0HAWsxB0huGlzLi373QtPDyGTC6O9Sd-M73wzRP2zn0AGUoL8b2BGNccJqP5LM8Yq9nEqCDakcV50kzrSnlPz4o6_VYEloU9GRhjFVOCAWar3WiOdYD3_QtqaNhHk0iY0USJY7-gsb-rl5bKXGweXG4mqUjtslYsROMYkMcBApawgxCO5hV2C7MQrpvXTWIJEqVavSbXzOe8oTNqfUKcI5ZSrAnr1ynoPEongedK-0BpAWLfhe87ADlILb-4aWcgY4XHkPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا برنامه خاصی برای مهار رونالدو داشتی؟
🔺
آپل موکائو بازیکن کنگو: راستش نه، واقعا نه؛ ما میدونیم که رونالدو مثل قبل نیست و مسن‌تر شده..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94092" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94091">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF5yXEBCYAFVBdW8QZA5XCKSwqxlYBDqQgj9muxR_S0HMKb3wgXI5tWXF-rxjcbU_Mhmfdm_npPbbAEKXBrZsw3KxDEC2IMOMNb007_qs42B-maId_quw4S2NUS2m24R9nBXY_RykseUu4ck2GcMcAr3mFTyvaZjfMh5bvzMV_DRfbogGM5Xm_N65kQfUU4rVHErc4UtsVxHp904D31dVY7mFRzgm0V8GOCRfikfRhf5BB88zBwNVyqBcsTBHvZRXCJoJqNItXjb1uk5RDw_TxjN-XvDn1tUfd4PTP9g8eOwggWS_Ys4pZwGOgXOTXo1nidgbYrYbX1O8uJZpBeH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع نیمه دوم بازی فوق حساس و جذاب غنا - پاناما
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94091" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شروع نیمه دوم بازی فوق حساس و جذاب غنا - پاناما
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94090" target="_blank">📅 03:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0SPD0o21UGM78xnlR58XYwO_FH2QECZcGSUIUUh9W60T0LBSU2OrWx5Lw59F6M-E6vGj0_43oz86vkFM7OZlqIIw94o98X8RkN9QiucFPYvYgvlrBN7q-syc57E9ZCfUZnKa3piyHg-b2LZT6euUjOy27htegTnpe0x-czuDCnedjhUWKf6vhWTLP45IQwoq5qjuGpkl2ARtVcrZqQpGV9eH3lLUw6ceOs0jUbE-NIBBjSahdRiU3wznF5PKTUbR5gWFlusYVyjGd_T6hxLXBnyrHL01aKEoUMZjEaXP25FyoLXYJ7MNk5jA53QUbK9N-_9giYq33xvPzi64L6bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
#فوریییییییی
از رومانو:
⚪️
رئال مادرید رسما و شرعا مذاکراتش رو با چلسی برای جذب انزو فرناندز استارت زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94089" target="_blank">📅 03:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94088">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a6b42281.mp4?token=jqtJlXUEMCsgAi3jJlBnoud5eqvg7Us00UOP_C-4RRf9HyzbIwXvn5ZiqNC9R_yA_H-XQXupde49WtFTPbtnbNPvAWreFkZ1awUJtU9js5PzTSR-SYzgSGELFpy_9Y-k7nGHK5AGCBHpbid9WTo0oykyenfJGQWwVravKuGCXcimd4QF8EyrH6N-_5ydpV-tjYrY65tRJ_W18eNoSINE0QhBil4Cqb4TPpx5XL_9TYdKb6GGTQ6tFmqwi43r4KCdIlaZj3SNozijt_S4MYtNi5wm2mG7zM_8ilUDlwEExMLij8oaQ7wrSQYOyQt3beXtPW-RsqtZIXZxr_tDbOw59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a6b42281.mp4?token=jqtJlXUEMCsgAi3jJlBnoud5eqvg7Us00UOP_C-4RRf9HyzbIwXvn5ZiqNC9R_yA_H-XQXupde49WtFTPbtnbNPvAWreFkZ1awUJtU9js5PzTSR-SYzgSGELFpy_9Y-k7nGHK5AGCBHpbid9WTo0oykyenfJGQWwVravKuGCXcimd4QF8EyrH6N-_5ydpV-tjYrY65tRJ_W18eNoSINE0QhBil4Cqb4TPpx5XL_9TYdKb6GGTQ6tFmqwi43r4KCdIlaZj3SNozijt_S4MYtNi5wm2mG7zM_8ilUDlwEExMLij8oaQ7wrSQYOyQt3beXtPW-RsqtZIXZxr_tDbOw59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
توخل حسابی از دریبل تر و تمیز بلینگهام تو بازی با کرواسی پشماش ریخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/94088" target="_blank">📅 03:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پایان نیمه اول
🇬🇭
غنا 0 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94087" target="_blank">📅 03:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کیروش این جام جهانیم اتوبوس چیده باز.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94086" target="_blank">📅 03:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzhFZ2KvQtvpMlx2SZZwirCD-Q4F8tGtT8tr1KGdLpa7_qS-1LJtH2T05fe6gh27MDGXSnmXszGRNo5wZIDmxPRJW2c5yHYfQfxeCGpwPMVvh7UpAlscEGWjOBqTYffycEYVwKMA4TQvLyOI4UAdoFbVqd3CjUXE7a7MXrXvJbl68djV3_3OdzVzaj-IYNZYfqlo2udMqoBak2-PkHYswRzVfViZ9U5yiqS1dJdfagTBslG7ATbZomQ-4R7e3fs5oh76XxDXmHoh7guB3tFsFv0bPi8tf7j44ts-FjiadZIS6TXVT9hRebC4xVVVgVYMsfb4sBArUIfVA9NoaRpMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طرف حدود 800 هزار دلار روی عدم برد غنا تو بازی امشب بت زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94085" target="_blank">📅 02:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بریم برا بازی تیم کیروش و رفقا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94084" target="_blank">📅 02:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
اینوووو اگه نبینید امشبتون به فنا میره. خیابانی یه کسشری گفت که مغز خداداد به گوه خوردن افتاد
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94083" target="_blank">📅 02:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=uInIQuNNy5mFLCijEUbEvzMR96HXGYYOMfvCXU4pdCvf5Q6aofKcRQiTQqAVFA5CR4NXx_kT2xuihNmz2EJ17r6rDULAcFwWYY19MWskfI73IwOPA08pJq2VvKG-0XDukBtDrTYZ-JYHaK3ZDPsG-FEtNRYV8luFxUM5wUUhIHcXGWyca6XBYGLFzNCbBbYkr5HYWy3VLs3-QVXtTqQrqpZ3rk3zEy3oKKArvTt3ONP0cqH6ln0pxrFzsWwDSu3oADhv7MchpklvrQ-qbBM-URHMfL7GEldI_9HBZyZ8jF8na2naFSjE6bWdZeD_RGG754HWTmZ6N7woeisbGzIk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=uInIQuNNy5mFLCijEUbEvzMR96HXGYYOMfvCXU4pdCvf5Q6aofKcRQiTQqAVFA5CR4NXx_kT2xuihNmz2EJ17r6rDULAcFwWYY19MWskfI73IwOPA08pJq2VvKG-0XDukBtDrTYZ-JYHaK3ZDPsG-FEtNRYV8luFxUM5wUUhIHcXGWyca6XBYGLFzNCbBbYkr5HYWy3VLs3-QVXtTqQrqpZ3rk3zEy3oKKArvTt3ONP0cqH6ln0pxrFzsWwDSu3oADhv7MchpklvrQ-qbBM-URHMfL7GEldI_9HBZyZ8jF8na2naFSjE6bWdZeD_RGG754HWTmZ6N7woeisbGzIk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
فیروز کریمی خطاب به بیرانوند: این چیزی که ما دیدیم خیلی هم تنگ نبود
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94082" target="_blank">📅 02:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdR9XZrE1LK7gAjWGR3T10fOzJTVKwOlSYP4gn4WkwabDw_VPqGTq1BQxInkolxwocJ9bU4Aezi4ZUyyKHSZ83eRYWw5gx4Px1ZkUITSrryqYC9a7jWohk9TFkbdVwzrhM5U5kZo7vM5LcdVpenIsYOK-Q_5WAJDtpgpwCMDVeVD0V8Ga1K9SRGw59qrH6VRYdB0a3bmo0Z3kDUzed_hN-WuPEuBviAoEk77u7FZ4Or1POhhU5rPE4IlAhG0an6ppyKIYXXjhAS5m5xOw10az63AZVwxvKumUZnNfRGRm5X1rIygzO6LSd9_pYTH1mehvpnRbyzJ6rbgcF29u9RHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwZ8RTUV30hUGQgQQU3_dPPPp9Qf1VErbEcNcQn2Us85K99oxSTHCXqn1dmvT_GHzRVgG9e31TkG0gKbGzGkUD7WYbl2annxeN5zyf-T4giYkreFDnUOUDLK5VamxtTA4WINJcqrg7NoDYr1xrxOh9esU39XI0EvHV-UN9AWa2uVjZuB7GGMgf0ZN2lTSj1pS6zgAtnILXMv_8FAAmHkCKWb6h3RRmxOVw0wayyE01AUCJfZ3XuUgzIpILO0PNPeROk_iQXCL-nm4IXPTMLOPyiKltS5lMTa0g-3xNxkqTAOdq9EtwFkdH7NL0AHXtmy3a34-LWN2zygunkZoH5izg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو با ریدمان امشبش قشنگ خوراک میم یه عده رو جور کرد
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94080" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP7aSWWwif9WE59vhTpraQY3-cEraT0m3cGtRCQ6zXfZiErJi865JZcKO90ZJpIgk5b7WX8iyrH6OWYWUXRTwr192t4nE_E40y2fuAf_G9u1_6NaWAO6XjylnWmCF_ABKVbZlHoBa-_77oMdqLyApkM4HkBW-FUjoSdziM-qCDeRU1jQ1GrVFWGLqt_Ru-5WXiHO1FUvGCvn-0q0tNfbv0yl55awGbt544MeCDh0jSAAEGBcLFVA8VCSbSoIb8JDyA3oUv82VHzb1WFtQOGChtwlz8USHEFsC2-KOre76p44H5_ldVjdN2mTNzjQjtVu1kMU014-2KT-BpSWfBNh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوریییییییی از رومانو؛ ویکتور مونیوز به لیورپول پیوست.
⚪️
20 میلیون یورو از این انتقال به رئال مادرید میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94079" target="_blank">📅 02:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3VHgC_wpAXIZDmUbiMscCIm1x7UWB8yxFrnNw_65fWE6hxnPW8r4J8zO8QTr9Eqo3bmwvpblPagKnMUO76jmT_hKNUSXRV3_wP96h45qPf5l8Rg2oYzPtOA5cK74zEkWmlr57g0Y1mEa7ezbHPAAu7oLDqqkehmGTjKLHSHhPJG1IUymMhHDtFvYwqfvOt8sUPagFjYFFkev11uhVZJSXwJmxXp7iQPixeP2-G9R-sdGPyEJ4IlQDYP9j7hg5Xfbklu2XLU6k9QYp5zeQn5-fP1YyX2u4FMLyW5lzRE1fN4_93mfxM9rsCol32SwRnoxXZD4jAELrANpuQZn7YE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
دقیقه 94 و درحالیکه انگلیس 4-2 مقابل کرواسی پیروز شده بود هری‌کین به این شکل خودشو جلوی شوت گواردیول پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94078" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94077">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJcBJMc_7HrQ-IC6lxcMJnNYoyvrfPr3er7qDySkCTnnR4CO7PImGxKS-xLrRWHGy15ENo5w3sGxVTgWrgkFp66XUHax5x6C1-59ER1UhxuVVPfduGbizBP4jg6H9QR7jXrLdXylfR9tEn1nxO4SdQau2yDUjlJBqex6HirCk9Y2QbC4SrMnC0r91oNWClJL_mPrLwQWjDl9osXleRJvVu3rLfGlTTIeSX00An24B0q93mx9mrsutss27SOkWL4iWNs12ZhiIdTU8BFr_56f8Odp8g06wN8ChWtOTBb063RUMq7gv2IYxwIuJQTvTawYAV7oItFpXyz0qr5RNkBmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
انگلیس برای اولین‌بار در تاریخ در سه جام‌جهانی مختلف بازی افتتاحیه برنده شد
🇹🇳
2-1 تونس (2018)
🇮🇷
6-2 إيران (2022)
🇭🇷
4-2 کرواسی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94077" target="_blank">📅 01:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94076">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvfqByXRglEK5IJ0z6QDRdemRucmWceTjZUzM58TWTdax5Q_7trhfGCJiERciu-PkjSLvqPg-pMrNFBByqB-hpomkRO5XxG8jtgQQRPtPg67ebL24Ec3vqJA4iYI32piG-oFCAz9JAs8l9IOMSNZgvUmwWHREWidQUxH7on-jCYN9D3WG6m1zC4p0Ns6hezpsxp4DBOhZY_lKHX059QN0YBKZNI9CQqKjUffuflxd_LRjHkWiEyktqNtscvQDZ2nXdnalfPCJIp7yLOS6LmYAxvLJkJqgivlkREUuzj1v25wbkaUMR7guMs4kV9ZKU280OjQTCcEHTyLNNEOSo0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه وقت فکر کردی کصخلی به این فکر کن که بارسلونا بند 30 میلیون یورویی رشفورد رو فعال نکرد و به جاش 80 میلیون یورو برای گوردون خرج کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94076" target="_blank">📅 01:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R9rJzLRK4PJoEZqviFSD2NC_t4YE8CYaZpHSMPyM_-_74o4K0dnkndTMp-GmTqj-wMgbKiNR8uqdnIOkWRuKVF-jqMxCbRCgS42lC8lJKMuGRxLIiRh1MrVOvFRRLpryaw9uir5Yy7C8lWUvgQfzDu8Xo_Fl7DnRPX-dlYjndfP1p4NWZgW4lXlezYWeggVWPZwdoflLNG9OnlsJzgGiZfoM4Wu4HYV8peYond2SzMyMvTWANLAhM9URvUn8EBCvJG3SMepiG4lW2fJ3f7-X1CdSEjR39bEDYZzgGRvxebxe_yrDHxeEyS1vfkvPDa_dXM1Al4Dy7dKc281SyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elYaOu4sqb4FyN2YUFeX453AyowOQiSc8iijhLFYC9qV_EbmJr6pUQWy4L6w2veypIIjKFidGODjD6uz3NNonT97N6TqqLxbaXx313c5a9hgtUHhN-ypoqs7QpvkkD0hyk1ARWDP3O0VMJDMXZ571H99RjlS-VdPgDF54m0OWQM3vLUeVSRyFjIFHp-sexJ5LtRKj6WJNwZXupO0iXXopcGkKdnMy_L07HSgMs_Ge7oECTMW1LJWqeTXkm0mvhB4TwmU-wJqDjCUR-elAJuN-n1uQaVK5b9XAZ_Kdgjku0XpkCD7T-DHcQ0H7b_mIuMd9lo1AIr03FPdy5iogPh3WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داور VAR بازی انگلیس - کرواسی هستن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94074" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q70DFNdi8WW6DLlolVevkFgZf-S1BWU03_Lo_6h4mxm-laX_EUg5h01NNrHkCbJmR7Zha0JIFDI9XW-6s3Ic9eh5GnCaDbUEZ81wzb5RHxnuRYz0qSPqP3WazoISRx1Z7fC-cVFhTrVh6n0FrYfAOxZnfYsw-b87NLdIyn7lCGv_YXK63BksolILERo78edl6TVfnN78Ia7oeQU334C8Vfqky4oiYvvFafOMFjyuErgigvdrN95kcT0XOj6wj7WcVhqhG9KsJBfsfbRMB-9xIG2lNr9PSizC2JsvqnnNPdpkj_DtlWYJFnZctQTnD9qf2ov7tdLuRSPDsEuaud4OFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
دارایی‌های مسدود شده ایران که طبق گفته منابع مختلف قراره آزاد بشه:
🇨🇳
چین: ۲۰-۵۰ میلیارد دلار
🇶🇦
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
🇮🇶
عراق: ۱۵ میلیارد (برق و گاز)
🇮🇳
🇰🇷
هند و کره جنوبی: هرکدام ۷ میلیارد
🇯🇵
ژاپن: ~۳ میلیارد
🇺🇸
آمریکا: ۲ میلیارد
🇱🇺
🇴🇲
لوکزامبورگ و عمان: مبالغ کمتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94073" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4wrcXkvbSlJ1ouRPRKVU9JVYr36e5lcXtVIFGNPZnrCf_vN_AYRvDuXSAmsvO6rRs06Utv8ZkqBxaqJgFhLzDeOsx12irNYhbf_WcbS-DD4QOwFWPaij10XnEFKnnLC2FOHAAUdL1kYA2_EYeijcA_-W7rJaGYDQ18KAkTz9itY2im4cGbzOPNrVhdPRrupg99pbyU_a189navA6bXHujVYUiWuwMfz_bJE7Yd345a_SmhA_YZWZxx5lpnax7sUVLmo5NWmPY9D9_Tv3BZCJddypHI85hHt2Udoq3mkDn3ty-zB408MF5A7BWDPJ0KFgCCtzfhIUsvrksRFirIOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در کنار دختر ریاض محرز
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94072" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suyKSoKH916eL0eTRk5_Q0sKCgh-ulYJeQyMLI67y4ob5FQZdcG_XleqLMYpPJt-RdtbhMlKqvwofveGn6m13v5cvVzvEkByNQXDTJOXVEfoQrrsfMZUUCG-bRuEuP6NAlmokV3WvCbhDssvSlj3opTgp63LO2ugtaPz3jOXAb1xwuAGwpmQDL-FrRP5wrG09nY6Rg3uWy2lYCqo1RlSveNUCDkekrVL0Vk7HbisyiCcPfbhRyy_YiPlZe3Vk6vHVAkRmfZiO5YdH2ovA90ePXvPVD-ZfCmiwF2KUT9vcIFBZ5d8a4E6T6-dg3lKdUr_vW1j8R8eixoyf4QmQaqwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلزنان جام جهانی تا اینجای کار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94071" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94070" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WoLTkj0p5NYQOhUyzQZJEp9-KQt_GmH-WkN5tSv92B4nImF_j8GFMZtzMASC9LjxVBVo2lvKvk_CJ4PvB7vyH5L7haGjniUh83CgHsQH6Ar618iaE2V-uUUCGtbhCv5IP-bJyy0caEcWzPm5SF_Zp0t9WeCMnD5wxiU4YkEQYQkGe8aVbf1Z3jrVDbrACrG4YsNHH4KU0qnxny3g-I-_y2KhK2ub5hUv4g1H2cpZFEsUAye3nnZt-8aIxFaJt7ck4FTlkSV8oPMSqOdxXdRZuvYTK3E_KXkylFr1sg-2Jr1tZMFDrCY4si3Nm3eIA-R52pruXegpeprnt7SFEu2Jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94069" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/F_X5Y68lfPaDcjzk_r1mlIXzNScvn0rv10mN2ZiNUCvtXbit4UZYydpJ2yIQeuV3IeWWQCEiAgbY-YuU5ZvA7ysguo16EYJu5xGPx7iucUGMhhIdLxAJaQ7LlHeJ4YpqXXy7z5FgrSTgYc0urcssiaCW9ETDKFWDM3U_pujqjzCmFcWAeIhvMjyjMIyaV8JJejN8XpM4PpI4_xleFp73FyS6S8w8_HBMDeITdm2bBiqhUTyvjx7U9-nHEBNNVNXtTtUrB6Nmi7Rp9Tf_P57oYVjq6cE1QxM0BD5njHs0lRadHyffhjx7u-KPPFtaY_dUKQ1f8FaFVw-v3khENkJCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94068" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJfOivE3ZEihNvWcwE98aEtjHeE9J-vSN7fHWJHxuQDX6jYKaET8rk2ljTNSfn5YTKitj9ty6OgbL5AK_m8XsoruosfbgIM9Z5xLI22KNUD_jkYsuMKIyZ9QY5Qx4fapo2fWwVacqsU-mKC-q1HkCv8fV3PowZw19tlyJFCTmnefZkK2gR7l3V6gwA-0ooyqR5Jr4PiX7LUpXZZqH069DNF-hFMUjNtWUnaHUA2yTa3aQ3swxcH4-7rYDFroLhSfUHjqFquZC-k92EUkeBQAdusek2dp48TTNeqCV6K8qWyZ_Q9zSFsC9bs3pnND-xPxXsGNqE3N9gLKyBQzo2X_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جود بلینگهام جوانترین بازیکن اروپایی تاریخ شد که در چهار تورنمنت مختلف شرکت کرده است:
• جام ملت های اروپا 2020
• جام جهانی 2022
• جام ملت های اروپا 2024
• جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94067" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANZrgGXMlXoHKoHalNd801hUalgc9QwHxVmYOz2uRMRHHX0l679r1GybhOWFiZ0QXGyaQW3ctM-Al0WSd3Tz2Z7ZFCu1A-bZFHiXTdtXaL8izppnBW4zurQdoTmX1OpgT5Irma45iI3wyyfYoamkyCWwfd0hW-W2QAV_DACE69xdFZ_Z2rJooNI14O0J3XdQmizzXcJa7v_isxL5jgidi6iGIPqtJvVR1hd__P5I9XUF8sqnJJa3ZggSd4RUPGLU-_JIEhEu3sxuDWy51ILv4qt4gN5fq6dZVQwykPOvd5XouudjHDkQV4cFV5psdKtmRoD2luLQTU-elsxIWteIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری‌کین در انگلیس؛ ۸۱ گل در ۱۱۶ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94066" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsz6YYPE6yu1yGzyibPwQwm3nd13_sK3UVmR5DbwFYH8v9zPHe1omN6baSt5ZTiEF9CEPollDauQp7Eky_qkVMe8dHVS9FtYu3yFwGMFRVgbk2ToERvow4Zvw8snzL7kPwOEpvwn6iAaHXjKRhfRztsGql2TH4Od6gsdEDCPA7SZJKzDNCjwbs3MKt0X-QpfyKds2bWs0p6cSDPclE7oVW-HYIkQ1lkv1wzH5rCgse0n79k2t03Lc7BXSOlIKm295rG41ViVCjOdNpfKJRcY5jR2z8E9oq5n-WmlZcJpQF0mswb28U1sDaeuzEU65GWRec79hmWc8_yYrgZ2iJ3vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94065" target="_blank">📅 01:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEJb1DCgdaW7v32YemtuBvb65DiJ_ygxScZ7nCayAW4VUo5vX4Z5pxTXF2a5W95BHb6D8_SLP8PyT_lKVxoGNXNlBqPQm7vkL3kvYrlp_7uUxFFEEtv8m_7YWerrA_abeqRNTMM_CkouGEiiAPNG7avqbbmb2u1UMyRoZFzcombImb7COQ7K9_8Qi7LLR0hlIEv_iUdW0LwwlPqFpm52iglMK5cUBTNCe5Zbv3fXCVrBrW1B6JQQh3qDuFsP2LuZc6Y4e8dFYdPglo6IFky6JtPQw8OSkPHDztxp49jYcqnDlDqHrXQx8IK28_zKDTaxM1oobbUI-6kCYQ2mRyoxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94064" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9YQcMcshowomChWzKiBLIBNP-eH3rioGiGL8QiknatrL_0jJzKYWNigjZSYqhGgzuujSSOIYep_TGmdK2lVVUZcmC8M0IirH-uUZcmugzlKOQXxaWZgWhQMUCR0E0NEp4-G0UY0IGiQMH_JxDdr-NP9aKMJYxVCbUVP6LaWZ6LhSp_cttxIJp87rfO0r_cPqZ9VSYqg-92Asj1MyZ5TV2i5xMbWWkZaa0icGwtV4jT7zErIFlCAudGUMuyWPCcFtKF18Z4lLusxBxyN4_3s6M7HuSusAGVVMu3ZddB-_yQoxbZwRRCSbmmDFv1j8_ew770qNro2Grbv2G-aqJZwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
آنتونی گوردون ستاره بارسا مقابل کرواسی :
‏
🔻
۰ گل.
🔻
۰ ایجاد موقعیت.
🔻
۰ پاس گل.
🔻
۰٫۲ دریبل موفق.
🔻
۰ موقعیت گلزنی ایجاد شده.
🔻
۰٫۲ برتری در نبردهای فیزیکی.
🔻
امتیاز بازی ۶٫۴.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94063" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PU5P4cEEet2dXvC7bVFTHHBQNKzZ445NEbnbhodwiq3fb6o9Qt58o9RRk0Z2MJQEW06MIobQwI7vESUJ_SAVNxihVY7diyYbChEIHHML3E8iYPF_Om78lyAwDuyIuFqM61MdSP1U2Nony4UTsxKEHzCiW43MuEZsjEgLkZpXudF4oSMyYHfdbvWGLBm467Ng9Mse93X_4N9JgAG4ZOCoI2D0gE6yWOE-x0wvYodVYJ2GvwSS9CrxXZ7-9qL6MBaYjYMBFHI77gJjXel_pAxK8opBpTellsMducpUP8DwYHgr6i8C0lhWxWntHoOHRW79wbx3P5QFa-UEhhX_0q6qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMSNBdNIZbp4xClGMlnBWxSQoN0AKO81Nn2N1TBZ3t4gBkwEmY7Hr25gLlryNvZ4OZ4IDD3q4k7C3Ha9mkMbv4aQPRc1A5fLXwGmrj16Ojk8qzAL6eX0vNojiptwVpi8uAJgY7Ce_xKZiFDBow7RzdK2p71gJYHwVSrgw5Nndt087nOe6QFeU3tPCxbch_UhVpemNFnLjKk4cBVEd5wkAtr24oYGYpfPFY1ePdaHQI7lqiLreGB_Mp5XBQQ6Pb4MTWc2xoWOM1MUO7K3flz7XT6YxxkIskXQ_O1aPL5E-v8mdq4e_VIpF93VPK_-im9a0FFjt0juzbwSbiOZni8DGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره دلیل درخشش انگلیس تو بازی امشبو پیدا کردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94061" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRdKaB-UhJfbnh7PT0lQjUjTxlihJgIcNhs3sd2sHzmt5npewClTRtX9GS-E-DRmJj6N6Ccj25eIhyOABsww41qQ-yIXc5FW-QKwJInKviY6UTr8VWEbDKPvdvHohi01CtCFkc3SAqHUwVtkVvsgnjbWmlx2lSAbkH0rXB5m1esrz2EVf30KF2bhpwzjKIZ368Z66FAd6bEoEt41WOnVvdOiXGwloPlIXe4Sf8ibsa6HdlEoIcJuIHwkwkdjegH2RNQ-LqKBDZHi6qf8rBcC77H8Jx6AFID1EwXic0khywaQCcSI9RhvJTAVIuR44JQjXrDlTY3Wk5GZdIiQBEu_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94060" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم انگلیس به کرواسی توسط رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94059" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رشفورد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94058" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بالاخره انگلیس چهارمی رو زددد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94057" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94056" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لیواکوویچ نبود کرواسی راحت 6-7 تا میخورد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94055" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیکفورد هم خودی نشون داد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94054" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIKMaUfXkh31aH-u8V9S0P3shD6VY6gxvHP4vT_UKp9LNVRONh4guLbAocyKNadwdiK2saeNbi7Or22PG2hlx-TgvdGuZXZcUJm33lJZ1rfagwQFMExGdPbRiTtj63M1XTRQpp_mxurtPRsmfLG5Jq0kC-12hDX44-q42gTNE48ccdd0utQX3DWWKH5ZdOfm0mrrwziyeDhGoePKiKHhLVcXksZsMb_Pvobnv8TrJ0Ytt38xiAJs24Tyxc_nzRYCWf_B2bhO8XXWIu9gcPWJuyANYv5UCHOrn05jZoj2fMwBf-oygKEQMmkAWVhYHK3_o7oVfI00iI9g4hyoDGqX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
🇵🇦
ترکیب رسمی غنا و پاناما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94053" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
#فووووری
سخنگوی وزارت خارجه: همین الان تفاهم نامه بین آمریکا و ایران به صورت دیجیتال توسط رئیس جمهور پزشکیان و ترامپ امضا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94052" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لیواکوویچ، کل نیمه اول: 0 سیو
لیواکوویچ، 15 دقیقه اول نیمه دوم: 7 سیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94051" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بدون شک بهترین بازی جام تا این لحظه بوده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94050" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مودریچ هم تعویض شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94049" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پشمام بازم واکنش نشون داد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94048" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">لیواکوویچ یه تنه نزاشته انگلیس گل بعدی رو بزنه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94047" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW0vi_2RGo6Ftpd2F8Rq6ZR0obOW_smn5WVm8bJ8H8zjfY2pKA0UWoBgTD1Zf8z7W7288We8mAKhPM_Km97RtkH9dRZ10TUqLNlzF1I2MOfxlPnKMvzxcTDPXIxbWoT2buBsmKUSaxOrz_Zbz8zLMdVly84owjssW0LH59yR4c62baTn3jeZxVku-PhsUB9Tk4_Ox0D0Jx-NUrJrvi-dEPI3cvyVMc15pKhWDEQZ2DomToo4PigBr4keumHASOlyue2hHlM9keKIhPis_KveJR854g8Ccma7imd7RpxD9UNE_abmfhn5LC1GGnr7kl7A_jl1ZUiMAqHNeCg3wO93_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8mo_WoRkn7yfpaiyexC9XRG0jlykdtwqvkd0emVfVEIAZyU1cxWN-HwxairdqE8uY3HCewRhIvk2cPIUtmOGCArHRTRJvFwzYxLGvrBpg5r_Uel_dBm_maNmMaG-fEVFFGBsQXODbBySrs4lJZwmxoEvZDTE_NuuZFE6_Uxjbf9rhFmWwCK8iAWlMqiOsT6ud-JhIR21CpJMbV1JMX08PBNmAD8NjLNFzfOdjQELox1h8wfz4uWh1I1oKhpBAUXuQuXrTEm8OvxjZVwbdMHd_mQVbq2TXkj-G5xvnLedc5XQhhWaB7pMUpSnTG0GHq9Ad_QaUEN9S0Yl-ZOZ9-1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی گل همیشگی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94045" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انگلیس نزدیک بود چهارمی بزنه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94044" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گل سوم انگلیس به کرواسی توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94043" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عجب بازی ای شده تموم پشمامون ریخته</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94042" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انگلیس سومی رو زددددد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94041" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94040" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94039" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94038">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrT4XUGoMs8ogRh6i8RgUf0iy6b7fciHt4Y0OFywtupyRwsEkT1TL4IXhcCfCiUBMHpGk2ZOPs2gK6nFD7zUWdYUF0S8mXNaSc58gcQXue_9FIBiI7s6uJMGSryQklEl4LPxopMm9j2txMi95iijPiOGc-Lr7q_pOoS-YORjTtZo5NOlkOoW34O63133rfrNSWdDDC5UEUFGum5YahSc-MH84x5cmTBG4dAiMq626dgqSlK5-u-Lx2MNWYRf-EOg7rvzXdDqKgvHZbr3lMVQsLKUUbC4SdAIRfqQ7Z94QkREXPXbPyuGybSIN55YQoopzEYWXWVfNUzdnJSyOa39UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری بانو میا خلیفه برای مهدی طارمی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94038" target="_blank">📅 00:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpE9vlO_ytM6USB0UW6ZeOLJ-RRfVizwLHpMRb2K142K6VDdH39DkmIIWYLQkS_vUzksd9q2NgWjCmb5EcHGaJp8EhZvDmZ3pjiegbZeOALgD8CrFQurWwzsOW33O_CUX95XypyhkGWBzRwH_Ryfr3qVsWJEZ7MwLB5of9oJe-QVEXAxM7shnywGqZCbpGoWdpsS17-3sx50vo3rRp3O60JCI5Ojd8Lrb795pRDeGe0-BGBMsl9RmyyCd3J3uCCyW9PYczwgLUJT0Sjwlnu2bc7hEUA465Rh1XEG_DOQ0PD9vk9vcSSro-orLYbAYrF7HRVDAnxXqwkt5CZiLcnsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هری کین با ده گل زده به همراه گری لینکر، بهترین گلزن تاریخ انگلیس در جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94037" target="_blank">📅 00:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 2 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94036" target="_blank">📅 00:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94035">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چه بازی ایییییییی
چه گلاییییییییی
لذت بردیییییم تا اینجا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94035" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
