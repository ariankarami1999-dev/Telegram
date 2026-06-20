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
<img src="https://cdn5.telesco.pe/file/KPm2JpNcySCLoD792yKLp5hFKu9bjs53jR6nvetrIXqnvFBi03zUAEYu-HrE9Msxl-bmuepnmKE1W5P-CL_Mg3-L-EqH_O7W-bs2-A4rLf0EKQm3ivnftoDWvurjF80Xu8oGeKfN9z9ktzXilYBJR2QZsllciy3capovzqFXXFsBmdX-ESTQfwpG21nn5QXOIsOZv8jqhc9fWS2BIA2XL0L1Cq2ELmpM_D7MEn9Sl8zRsaQhhOj-WXfoxp4mUx6YVnWSPs7E5aYJRuCu_9PzQKa7vF9S-7YAsBvA73am8GbeqqvAexA8cGGoKvwlultsbwn8DFBi6Pk7BpM1g9v4hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 676K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 08:18:16</div>
<hr>

<div class="tg-post" id="msg-94612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری
؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/94612" target="_blank">📅 08:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آغاز نیمه دوم بازی</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/94611" target="_blank">📅 07:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viKttt7MWrXinfY7pWkOyuOQa7qa7cFsK_ykjPFss8cNq2mciFnvPMIC9GBcGesUzULF8HLaCn0cjpe23Y9p7FNJi8j-VyOKK5ov7euQ3Hc5JElEcCllCFCr82gWSeJSnKBCYhTN6a6Yh8hKMirTitp5lLsDXET--p5mO-Hqfeu4eWcHmXfp0zapeF7FHtOtYwiFCCfmUg4OLWXheUOiIBdLsM5PGWNCQo5stLTgtg7SdA0RMJ7ojAiDuPyZQQvKm1At8--J7S2RQJ4Iwz8lSlxejM5tOar2drTkGcTut0p2q4SE0_7ohVvNOf9GBsGU5ta3C6KoJxrsXSqMkkjVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🏆
میکل‌آلمیرون اولین‌بازیکن تاریخ است که با قانون موسوم به "پرستیانی" یا همان  دست بر دهان هنگام صحبت کردن با بازیکن حریف، اخراج شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/94610" target="_blank">📅 07:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHlNJvIwfbXDaAxy3yxDPItn-NiqVIS-e4QAgDqTLqX6WIzP0Y8foani_lslW6h9b9vP6MGMswfwLayywbCNcrzCfUctmcbq7GIFZtSNdj1D8HNbNdQi4WSUeZd_FPWG4FcE3ewsOztMYqE58wD9ZPi6QO8hy80aKoxizgBljPnMO_UzIXwuPekPmF6JllLH3gagXVKge06VQMgLFtjrzIQPXqBWcQahaj0s6Q_hNc0q57KUwBNS7LP30-mLcnHFGznyEno5_k01_5WnYP5mGs_n0lejb1Axe18mqthPcc6aXHg_2hifNhov50_asGBch7jAhR-IPP4WBq1ssmahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/94609" target="_blank">📅 07:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVdMgfIx1OPp7GjVzeKJHwVgzf3GHMXYZRqn0wvtRV0CU-T7HsDdErbELJ6UDpTONb3Bmzj_vjZfWfIvAAPMhgJ_OTlXcUcrShW3n5TA4HNh0peal17KqEGci_c8ausnHVTBZ5XJe2L_wK6wRjaHEDNVHFDjoLeAlXA1tCTpeafhOPLLTyPK7QkgBJoZrwK8jiK9S-aHtJRkjKlrqMa8GLFHqTNu1G5X1co5-CzEYAz9Uhjhc2_IyTBrMc5gFUU3KdEKviVAfb9Y_AJF0HFlIF3kXBwVlZVm6HVPfWvN6oIUzU6JKZZJSXa1Ox3YncWlmovsxGih4-itHmy002by-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور بازی چون آلمیرون دستشو گذاشت جلو دهنش و با بازیکن ترکیه حرف زد، اخراجش کرد :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/94608" target="_blank">📅 07:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=HDStPXjXC1FQ_Ntn3gTz7UmSsF8lhbxcxy_kIa45I6bkFC_fWAxNXPQtJJHlBlzGhBzLM0e2Rkr4MehR7N-aj_-2DdBV6tvpq8i8zwOvJeFcXFI6_UhmJerGv4BSDC5mNy3wkaTzERty1xtrAQd3RUWk-FqF6k3Rddoj5skO4YIon27yQ86VcHVgDqpyOJfyxoGASdr_VGUT25PqHXMu-onkiGx_YDrrJTJoQy9Ckk_TNwUdkqSv0Te1aTkoBmQ4Vsf0NLO0kLeMKjiscJopm21KgIowbqoHbUrnk4JBYWiFLfmS64BTnKggrOa9DoYs4HG-cCnXuFU2HTIaCHYJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=HDStPXjXC1FQ_Ntn3gTz7UmSsF8lhbxcxy_kIa45I6bkFC_fWAxNXPQtJJHlBlzGhBzLM0e2Rkr4MehR7N-aj_-2DdBV6tvpq8i8zwOvJeFcXFI6_UhmJerGv4BSDC5mNy3wkaTzERty1xtrAQd3RUWk-FqF6k3Rddoj5skO4YIon27yQ86VcHVgDqpyOJfyxoGASdr_VGUT25PqHXMu-onkiGx_YDrrJTJoQy9Ckk_TNwUdkqSv0Te1aTkoBmQ4Vsf0NLO0kLeMKjiscJopm21KgIowbqoHbUrnk4JBYWiFLfmS64BTnKggrOa9DoYs4HG-cCnXuFU2HTIaCHYJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94607" target="_blank">📅 06:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترکیه خداست
😂
😂</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94606" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دقیقه 1</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94605" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پشمامممممم پاراگوئه زد</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/94604" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شروع بازی ترکیه - پاراگوئه</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/94603" target="_blank">📅 06:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=H-M-0QT2pvac8qC_Xr37r734k9AU9LXIPmLaFGPPJZuCKFSIyX9aUHSNOU0y-ULcmTjnbL-Sf0fJLuW5EbQDOtwuViAIRWQloyoRqHfB-puqEwa54SLB30qrkb2PhOmzOx3FuH_WD6dF_9lfAQqwKGefEL37tmbLMDHUGJMqEkQmCATzVckvhlzaeilnVKZczx15q11FNBShhFipR6j4pZ8084MyOKYILMkVR2wlMPtUv_D6WlJ7QRFrMB6Fyz_O9UoNQZjypnM-LktrxSiPBwM38HrgWR4YpfKgC_z7z62K6NImktXMfvJGBhsjy_OYbJWxGVH_2zvBJWDvTNC0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=H-M-0QT2pvac8qC_Xr37r734k9AU9LXIPmLaFGPPJZuCKFSIyX9aUHSNOU0y-ULcmTjnbL-Sf0fJLuW5EbQDOtwuViAIRWQloyoRqHfB-puqEwa54SLB30qrkb2PhOmzOx3FuH_WD6dF_9lfAQqwKGefEL37tmbLMDHUGJMqEkQmCATzVckvhlzaeilnVKZczx15q11FNBShhFipR6j4pZ8084MyOKYILMkVR2wlMPtUv_D6WlJ7QRFrMB6Fyz_O9UoNQZjypnM-LktrxSiPBwM38HrgWR4YpfKgC_z7z62K6NImktXMfvJGBhsjy_OYbJWxGVH_2zvBJWDvTNC0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری از اولین برد برزیل تو جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94602" target="_blank">📅 06:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94600">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P23a8hjAXQh1jQcJc4VSJF05TtpwGNvQOVswSw3XoFadqxqM_ECBy_beiUsKGB3_20M9lzsU4hJgLc6qxRCXBsdLO7t7dHNfJfP5H9nh-q2AI2jNhaO-yREwnCr4sQrJYfjhVxI0HYHY2jxqDtZIHwm9IJHaxFBUt2UX1pD4JQ3sbesQDyBqFCUXxHNxxb53mrfw41hCTHNd2QaWkBXp1elWBQlf_4UPOrv6KVII4zgzgUGylp5nD1TVB_Z1hee3EIJ6SQKV-v-bjlVWaSJM1mcUEjLgLy3osm0eTe91-XKNylLPvTEKfdPiwZWwZQKMFjTVY4i8YUjPJZMGB5p9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
📊
آما
ر
وینیسیوس جونیور زیر نظر کارلو آنچلوتی :
‏199 بازی
‏
91 گل
‏68 پاس گل
159
مشارکت در 199 بازی!
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/94600" target="_blank">📅 06:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94599">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjCLlpCOTWnX2JqbbXvw7P7sY0Z9SkcJJFFkAF7qgz57dTAMGvnQqJB5SpgTjBoCwjx-uK5Be6APaYBmmaggKi7DBI1zaYy4UGSPAjSparJmcsVSAxVzaDGjssXzgfJonLDyoj89ducQqixs5G1fhU3L9kib5_TPut_7AULIQXkW41eip0kvkumW1B7DT7msiftv9zGZzrWGjxR64grSYXVhHCpqh_zngSjv0bGxoAskmGNXqRcPGHxkW3a5eRUsK3n3kL24SiOxKqym_pewB4JEofTpyQ5fQ-WBIi-oD5JWZopxV3rf7j3fDDNQ51FdQ3oNV1rCCgBAyZXXfMvFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کمرم رگ‌به‌رگ شد از سنگینیِ این عکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/94599" target="_blank">📅 06:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLKkkEBP66b7DCO7reyaTz2fEbko2kSrJHT9JojxHRu6x2-z20GVmvNHH2uKHJDrs-b_dlxeSIqTPdftbujsSWF35NVDXKqG51GmaV6iJMxY6SUd_S7lgcvOv5TnT69c97rURVgAs9r74aF83AoAzCylNjKswZzB36JlceMPsT0IUYSy-foiruNP-Wbyn_a1mBg-xaAQgWaWScBgZ_z5nNkQ8AKRQAUHVk5O-qI4NoRhbP6iYVmbfj9t6pFUQqWJIQOxyLRxE_Cbm9aDQUUUsQhFUdwfzdo_Bx7niD8GB3zJiNg2TkQdbAFLBj6LzkPHwKToHfS_SqPU8GoZkvlGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3 -
🇭🇹
هائیتی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/94598" target="_blank">📅 06:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFzJ2kkkn17oVSi_hcLb8SvuR13KEr9CKadJYe-f2t3E8-gQ6QrZQp33HihU6IYpMyNDx-5O1BqdgTBYkm5FmbhpKpdjlNc7MNyxwBoy9sg4gwwUla2TC4X5i4xkIEoInBTdtv0A4IbVzraX2L8O86VFqerfmfensjjUISy9ue6EL_1qHmuICOGyPrs9BXHju5jXpPPI3WWSu8xmwdY-rma1Ha6hZVTswYeoMsz1qKqh4A652t-AvIo9kXHUI_ftX5Hv4yoU2ZwM0d14JytKrzVVwWbOga3-DCLcnmT1WSdPUIZwzfCBUeCBFKIAHmuSK4YcKEtuDblp8Ccz6PRSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3
-
🇭🇹
هائیتی
0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/94597" target="_blank">📅 06:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXd5pNS7KPqfD1aQoNGQxlOyBKxT4KBZi-ore7qxCK-UOC7GpzAUwERKBmv7FyppZHqZTx3cmQEf7EemHuEGisxjRWVT2At4oI2R7n8PZCbdNzTkL3E3FvU0mSPf-IlLzIUdpA_HP1VYC8Dbrmrl82JoMycxpBPQELEScnrgXSwM0MprR6tqjgLs1H-fiW7WFlWVVJWKv4NwGb2CeTxc0vjotAv_HyDSrdjbeyiJLUMR9_LxZJhkGbrdcgPqMZvHOHRGmje82nXs-ImCwfAGVZcoKn4KYLSVMMaeyORSwfe4kOiDxiStU2hJ8km_xQtmeoiuU2Sd2p47RnZWyNfGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
خوشحالی گل وینیسیوس به سبک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/94596" target="_blank">📅 05:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ7g9Zrqh9mMqruOnqD5nsGcmvQpGzTcg8_CLboqkY0Wu2jHkkMDxiq6q-2eSCSuZZLhLwTbLH7RIKnj-RqTcZtnpPn1EYNJlzlPfpMyxPVq3pFaes2p75QWDiQeLQ2BDM5R04Dk9QQeyyOPk_Z4l-6QwLINaHhUU6BIJRXJojoC8fvixqyFbs9SjEmkUlMXJwiVz74FQE5cMl1cfZJyNKBz_Yuah82QJSpefFCpSKrAbKvR8PsVDYWEI1jPJ3I9lnETS5U_1hT7IIiDWXf-INmB8cJicXmof6_KLr5C3a71hHi-vW_NHzZ_D6XrJQuE0hll4KtfTKrbBn-AthDyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف 2.9 میلیون دلار روی اینکه بازی برزیل - هائیتی زیر 4 تا گل داره بت زده
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/94595" target="_blank">📅 05:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اندریک زد ولی آفساید</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/94594" target="_blank">📅 05:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پله زمانه وارد بازی شد</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/94593" target="_blank">📅 05:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=NQa5IDtS5QMcGvQneE1BlkU3csCHnVZKh1FN6mDeXhdfYbT1jKTqZDklJkMkCYpCemR5B5GYoQOxueudpaXgcDu78lGJSYA1jwr5YfmBoTufSzJqbWZkdMkx4L7GhPtgD3nJRdGo6_MpDBa2YT3e-UUmgNCXRiquNeuA46wnrwPn0zoLZfvd_IE5zyKEGKM6Alvu7-vUMjBH2paJLFcOsxlbNQze1DPOpgAQGfurVESZdg_2yLTM23CLZvg_3r3JaEOML4MFvg2UZCC7Bi89Hvdx-N6Rzj2nFTbTXhWi_qCgK0flC39MAZwmNioBlPbCRPpoyYNPsyLm6JS4D8oZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=NQa5IDtS5QMcGvQneE1BlkU3csCHnVZKh1FN6mDeXhdfYbT1jKTqZDklJkMkCYpCemR5B5GYoQOxueudpaXgcDu78lGJSYA1jwr5YfmBoTufSzJqbWZkdMkx4L7GhPtgD3nJRdGo6_MpDBa2YT3e-UUmgNCXRiquNeuA46wnrwPn0zoLZfvd_IE5zyKEGKM6Alvu7-vUMjBH2paJLFcOsxlbNQze1DPOpgAQGfurVESZdg_2yLTM23CLZvg_3r3JaEOML4MFvg2UZCC7Bi89Hvdx-N6Rzj2nFTbTXhWi_qCgK0flC39MAZwmNioBlPbCRPpoyYNPsyLm6JS4D8oZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینیسیوس: ۳ گل در جام جهانی
رونالدینیو: ۲ گل در جام جهانی
کاکا: ۱ گل در جام جهانی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/94592" target="_blank">📅 05:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94590">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_h8Ufe8zccBi-b31hbbFmvpKa1W7k6eAW7SQqCgjFEkoIU9wqyD_zVw-JiohOgls5Psq5BvA9FOuX1UX4Lbu8VkjxpK5GoqN5u2_TTrZ_CeW1k6NGOzddV_VLaIYfoJuKI3KR7952Dg8tu-xK6njMtoOLILFrHVzgjKuNjwK5zg-oiDDLNKDJQ967VbVvk80lbNWmZPPjBNNHVp_ssdfznBqSSnlOhPU8K6w2qJ_5B8e42NckK3dV4nl8FSVT-79UOg_eCf5jw7-yi6NbNuX59Bmk4diWhTmQJuED5XTnDkdvNiXcWOaUtVcXM9a80bd5xeDbzV2mvYXZU1Ej2G9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPdIjHPvIz_OcqdEZc83wjWPnc6qCp4gaZ_hub44pz9jybhBkpDpnfCbo-RfR0cCHZZE5qh5WkmlAvV2mXTflSSV_dLmiLviHU98iGL09sUuNcEgJhUOsBts9X2VkPXdKYTWYM6__4_aVBX_2RUwupoKjhDYlfaa7C3nvNKk--VFu-tYQutnm6lVfd31FQUC_BBS0CHuQnoD2p4M6R5GplZvCH0A4NId6EEhBfJ3CW9RMjsEIrEdaLoib22mSM8ELglSMSjILf9bh_Bp4yguLgN0bCIqGXFSwF23qv0iXhRLtCZQYaAFWiV9oAoQE_nglgVRzfShaOFN-5ByK5txGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇾
🇹🇷
ترکیب ترکیه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/94590" target="_blank">📅 05:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94589">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=reMp37Jpsy_fzE_997GsaQ4YFCn4xj8uOcB-Bk8tdYqj1dkgHW8RxpkzKc6O_yn5HhFVTKmysXwslMO2yCl-QFeIv4uAcuyfqfIvMBnZoQnRvO9q7tKRDfY3VqV9G1YYgnbkaVrq1_oD_PIeDjk0hS4Dgetu4JiNlQLUhDxJZlJ8N11OAJMG8sSfn0A4N1iEE8CUdMTGB4QtG4pEDVv_OMNhTQe6B1IPdN2leQq_jLG4Wl5rzEjv1Hbt_6XwcXoJBxhim5IS2e1r4N-k2_OtXtpFVP2KReXJ8eisTv-Q7B1yFC1WCar0YGMsexkdDEbrfDsFotkWHMVHi3VFR_8kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=reMp37Jpsy_fzE_997GsaQ4YFCn4xj8uOcB-Bk8tdYqj1dkgHW8RxpkzKc6O_yn5HhFVTKmysXwslMO2yCl-QFeIv4uAcuyfqfIvMBnZoQnRvO9q7tKRDfY3VqV9G1YYgnbkaVrq1_oD_PIeDjk0hS4Dgetu4JiNlQLUhDxJZlJ8N11OAJMG8sSfn0A4N1iEE8CUdMTGB4QtG4pEDVv_OMNhTQe6B1IPdN2leQq_jLG4Wl5rzEjv1Hbt_6XwcXoJBxhim5IS2e1r4N-k2_OtXtpFVP2KReXJ8eisTv-Q7B1yFC1WCar0YGMsexkdDEbrfDsFotkWHMVHi3VFR_8kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/94589" target="_blank">📅 05:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94588">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بریم برا نیمه دوم بازی
🔥</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/94588" target="_blank">📅 05:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94587">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8BxQokOQnJNjHIjrFE-SigWhYBdYhyooxLDsHfxaRgvYCniWhnJzh6nd9x-SLREQOxwxd-d9TKnRXPFGeEUfUY7seHYhP4_c-vmLwXvz0eBf7sz2Jy_p_mLjfQVjdRbHb13rJvLCAca8VxzkL1nu9InjMI1f5OG7fWzu9c9pgJZRpdd6jmDNKFDWkMyZv5ty57s2uud4ZBedh4XVwy6G3tdMCRjPd3jY_7t3lcPLZw19AMzCQazHBwmhcTz0YtrrKlzhHvnPRZADYvrG-aoZZNTYrnADGIy4u0aDWIZf3PnSOuNeglfEs86cACaLI73k4QJxaDL4ZWR1vqm4PT0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
آمار فاجعه‌آمیز برای رافینیا این فصل :
🔺
پنجمین مصدومیت رافینیا در این فصل
🔺
رافینیا به مدت ۱۱۲ روز در این فصل به دلیل مصدومیت در بارسلونا و تیم ملی حضور نداشت.
🔺
رافینیا به دلیل مصدومیت ۲۴ بازی این فصل رو از دست داد.
🔺
در مهم‌ترین مرحله این فصل در بارسلونا مصدوم بود و در جام‌جهانی هم مصدوم شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/94587" target="_blank">📅 05:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94586">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgqgWsd00aoowDFqGOchVAELXAchdGdwwGa5RQsXwRW3BzNjC-acfy9xwxqx1B1BwSYV2O3SqZYmrJ4mNBwmQcGXMpsxqUJJMUSEpVoBKW6JI3Am3SPQqUMHoYVUvfAOD1PO0S4zeHb1Uv0FQ5liB7C5y0lehz9x_aAq8gX8-8TDp5EHmh6EPxJ5ZcnrSeRvpqR4sUqEX4q4UXF4IdE162CBoyxGIvEffI-0bRGyBfsVBjdJTkK4i2UOwSIlPM1z7aAfP13venZCxeIjAiclXdCbbZs3eGPtwcWC7JiLfdAdofpPcapwwTFX5mx7DKlW8TCyUTmYtVuyTbYiW0wLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
وینیسیوس جونیور در 6 بازی حضور در جام‌جهانی 6 مشارکت در گلزنی ثبت کرده
🔥
🔥
⚽️
3 گل
👟
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/94586" target="_blank">📅 05:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94585">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9330025fac.mp4?token=jO3Y8_cDkrgWGJC4GQGQyaYST5F4YP8yA8TCIAb4MF5c2SRGTVOYDXpPehByfY_tMrz1AJp-bIEbBJktZWXRMXmsMtTuwSlM432Bf-nKDH3MMk86F2pIKSdtuxZKvvaBQXix8CQWcUTAMl9M2M-wlQNIskI6jaLpPsLdzrGQV_eeLMmbg7alx8b5myPWwk9olk-WBmCZDlxXIuAI9cWgEhzwggVI1aMEKJ0LfI27SsmZv9HIOhU5VSimYQWNgg_Bx1iFHu53nxt9hKzSK1JNlH9ehMpe3TR3_E9yKQ6dRgWIVLx7jYY3Qg7FEhQXUNF6slqXqTGucTYVZlXSoR8etw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9330025fac.mp4?token=jO3Y8_cDkrgWGJC4GQGQyaYST5F4YP8yA8TCIAb4MF5c2SRGTVOYDXpPehByfY_tMrz1AJp-bIEbBJktZWXRMXmsMtTuwSlM432Bf-nKDH3MMk86F2pIKSdtuxZKvvaBQXix8CQWcUTAMl9M2M-wlQNIskI6jaLpPsLdzrGQV_eeLMmbg7alx8b5myPWwk9olk-WBmCZDlxXIuAI9cWgEhzwggVI1aMEKJ0LfI27SsmZv9HIOhU5VSimYQWNgg_Bx1iFHu53nxt9hKzSK1JNlH9ehMpe3TR3_E9yKQ6dRgWIVLx7jYY3Qg7FEhQXUNF6slqXqTGucTYVZlXSoR8etw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🔥
گللللل وینیسیوس به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/94585" target="_blank">📅 04:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94584">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وینیسیوس</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/94584" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94583">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سومیییییی</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/94583" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94582">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=V3rITqaP9eU-tDHza12bwxm379G9OOKnQYA74qIlaqREXStqdW1A87NmWbQcMrcaKK_xWTyQYYQ8DAKzJ8xKcKWd67q6bhAR53IjtY7qVXvfbU8xlMPGeuP4UvzmKqp1etOyXqeU2EWFqZi27iqIYUzDGa5GoqRFmmqZJ_jLVtPmG6vmNgeP3cQX-XA7-YLECJ35246q8aZ2kge5Wx2RwH-vjBTsP_1Nxzi7ACBJLmBQiVLcwbj19Mv9YESdz2o2FDwP5hJMVUFX_KbMewJRHFDT4qHiJFyBo0l94UMvhNgRq9LHxsA8U6q3TbiFLm4zp5z_QdMDiFD45tRIe3Ic5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=V3rITqaP9eU-tDHza12bwxm379G9OOKnQYA74qIlaqREXStqdW1A87NmWbQcMrcaKK_xWTyQYYQ8DAKzJ8xKcKWd67q6bhAR53IjtY7qVXvfbU8xlMPGeuP4UvzmKqp1etOyXqeU2EWFqZi27iqIYUzDGa5GoqRFmmqZJ_jLVtPmG6vmNgeP3cQX-XA7-YLECJ35246q8aZ2kge5Wx2RwH-vjBTsP_1Nxzi7ACBJLmBQiVLcwbj19Mv9YESdz2o2FDwP5hJMVUFX_KbMewJRHFDT4qHiJFyBo0l94UMvhNgRq9LHxsA8U6q3TbiFLm4zp5z_QdMDiFD45tRIe3Ic5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
دبل کونیا مقابل هائیتی
شادی بعد از گلش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94582" target="_blank">📅 04:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94581">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رافینیا بگا رفت و تعویض شد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/94581" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94580">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94580" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عجب پاس گلی داد وینی</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/94579" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94578">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94578" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94577">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94577" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94576">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دومییییی</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94576" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94575">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94575" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94574">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003b58fa6.mp4?token=EYg2ZwZf1_i0jixu6cHzB9H9cHqzQNmeYIfy5Qlubr7Cx_jZt8g5n_T70TnL34dMMPwmB5SrfQThn_Hl5aCQ0QswuUeam5Cd7UQGlHEwWIlnLjRLILtVGWgTxRfZJQDpbuaISja0a6toCbo1d2R8MlnccU0QVddeOmagTRdN4yx-rTAp7UEwa6976VkOo0DgcrQ3lkW7xTHFqq-3OZQ29Vcnk76rwfz8kP_rF7d8JYwosngfHiOPWCUCCYZ3W9al8RYOE7REL6pupjrp4y5BQStOL8aliiGaH3k7iXv2eD-6LExzGvtVFPTde6iEqMAkI4enam5FQtnoOslJqOhgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003b58fa6.mp4?token=EYg2ZwZf1_i0jixu6cHzB9H9cHqzQNmeYIfy5Qlubr7Cx_jZt8g5n_T70TnL34dMMPwmB5SrfQThn_Hl5aCQ0QswuUeam5Cd7UQGlHEwWIlnLjRLILtVGWgTxRfZJQDpbuaISja0a6toCbo1d2R8MlnccU0QVddeOmagTRdN4yx-rTAp7UEwa6976VkOo0DgcrQ3lkW7xTHFqq-3OZQ29Vcnk76rwfz8kP_rF7d8JYwosngfHiOPWCUCCYZ3W9al8RYOE7REL6pupjrp4y5BQStOL8aliiGaH3k7iXv2eD-6LExzGvtVFPTde6iEqMAkI4enam5FQtnoOslJqOhgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل برزیل به هائیتی توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94574" target="_blank">📅 04:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94573">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfaFXW4w77uN1r5iqsD-1NDO6flWeQ-EpOLfgD0te_niRwu5TYN3xN-Wm1loTN2pPxZhou79_Jsp69rZLgLnX7X4CHjlV63JmrLBWpPbsNHjrUKPrImojqmv826KuCAmhQ_rztjqdHGRrFdMaGJTXiJPFiZwXaUlbrIEeoX4oKAH9FP8gKvzD2hxWzKNznl0CywyuGY6rke_ebjyXkA0p7Z-8WDswhD95d43Pnry63TT3KFBSKyBfAp6psIhntmY2PWEXZlafZ6lnTLKPCAP4XzW-7XKUFZishF-ppFgCiLOkvsi03LsUOA4vZ2H-eLNbdzPAGVFSAso3WLbWLlx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز دلقک بازیو شروع کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/94573" target="_blank">📅 04:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کونیا</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/94571" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برزیل بالاخره زد.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/94570" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/94569" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رافینیااااااا زد ولی آفساید شد
❌</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94568" target="_blank">📅 04:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPQasx2kvolKp8iHx42spnhaZgTsZisi9VnnHOEEYxd4Xxbofwj0iFe6v7Ou4bIqqv6q6w73Q5-Hh-8gqKT6IpUdhSIvi_MMKhYcZnCMDuf-9GTR4SPfcFBu-quW1rl0FySos3cLaIORY-gHI3WLlyxfbSfBqhl3XFD779XqP72dRui7oj77v_nUj39veUmn0Xx7h2E9e_dQriG8qQTyNwBZ0yyxqBBtgBTJC3MhH0J1qZIiE0vWp2Tt03k-yyTisNXLKduQdG4kr8xUgIjCeTBltIk9NXs6l2x1xuaeKMHDf1viXwPp04UjseRjQpz0FYQYTKsnGQFweOg9qqC1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
استادیوم فیلادلفیا محل برگزاری بازی برزیل - هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94567" target="_blank">📅 04:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بریم برا شروع بازی جذاب برزیل - هائیتی</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94566" target="_blank">📅 04:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtmgwyNSYL6Pa6JwBrIEYivcXPycIccAWkslkD63TkOgkSrVMaB3r0bd7NRHYLZ2Fia5l1WKX2yBaVbrCnuiPS2KmeVwbIr8DGNNkZWu2ECB-lO5lq1xLKDRBzYVCwggJyZ9HOF4SusucX1GupjpzmP7eYM9wwoqgbbmAjs2nry6OHhb88e3j_0i5P2euovL_m1QKJAvVWxx1spXJOwuS2deJF0dgOSTQLiK5JK_B9Qqjy0c7shzFRDl1Dx7ecLgCDtL7V77wLPeEUsEKaikJcXp6fVRRnZMUrLrpyheRbxOZ5rj50N1zKP-JfF-0o15ZFjFzsfW4k85HowXP9tXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین پسر
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94565" target="_blank">📅 03:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2PX7A1yseRlK_C0xUOxOS-N4ud4bszZJePdTXDrseczdUUd-Pf_VZEd4nOvK8irImCZFy7S0HnSlvJAqUIc-HoRevq8h0OhRehSTouc0QXeapiqwDUZ8v16QqlaUDgrwp6zqJAh7w221iG3LmgyTmydlhzm2duafrU_nKoP_HKpg9lcpEN_WzWPhTuHCwbNi7PtgTxE9l_hk8PwSARNsp9Vy-OFjXcws1EUESXLlbWsjRr2y65L62F8yWnn2csTajSHYAIPRAuDEMexq0CzBCdAjHzKwwAdVRnk7K12CKEW40iiBHKPAgeeP8tT-NQfzl5ATXnoasfqvL8C91n0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با عبور از برزیل و پرتغال به رنک 5 بهترین‌تیم‌های ملی جهان رسید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94564" target="_blank">📅 03:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3YI4wOg7nVr_oC6juD8Zj5EzDjVUc_gGQ4J3ODMKk5ja5JY91gCS8AZUnhqD6Nk073CVEm4Ofhi8oo2pjQZSbrlRJeIn7X3pEtNwcvLX1II4snJ4Rp9MMUs4Lm1tM3Y4flOP9nAGfwCWzcpXuR5aAUBV9sqIFy80NH794Bcs9zX0eayd4fGig0lPk0wPe3C2Oug15nd1BQ6k2En0MZhIinK270RtRx2MXDXr2bVsRU1RVNPxGOoOqLYbrXP_gk5_M-_NLehHoF27LI5vURtQF5SLdXffeyhi6TLTH-rGVAA2S4YtRIOTg5XdFz09C-82lFt6xo4ZkkPDbfUO23S8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🏆
اسماعيل الصيباري مهاجم تیم ملی مراکش به عنوان بهترین بازیکن زمین انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/94563" target="_blank">📅 03:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfpJcVMpIe771D6G96fGzs1rSKq5gHoXfKACFbMofbU_IEVpRZ-8tt1SbO2WTUQo--Zu8CO2LQLNB3NLSPsNlP1mnGQmJgVhVbJgoi11kGZs-xcxqwX4eTipgjaKgfXg8iJLGSeoQCABFl_Zb6k88C-AgJdtGe2bvMIACQwA49ra45MFgIvkEnU0THr6zCi7xGHpBBL5nT9P2_6l17lGJOMj1SDawjUwApOajvjD3MffFTPD7E2oZf3oPOhArAC-pPjqzqhZoysZA8rEJHx4pFhYOrGBQ1fz76PucIbzRdwfCKbjipGPMeSlWenAF4wL4vo3_6tOcsQG_YnICWUtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طولانی‌ترین روند بدون شکست در تاریخ تیم‌های ملی:
🆕
🔥
‏۳۹ بازی —
🇲🇦
مراکش (۲۰۲۳ تا کنون)
‏
۳۷ بازی —
🇮🇹
ایتالیا (۲۰۱۸ تا ۲۰۲۱)
‏۳۶ بازی —
🇦🇷
آرژانتین (۲۰۱۹ تا ۲۰۲۲)
‏۳۵ بازی —
🇩🇿
الجزایر (۲۰۱۸ تا ۲۰۲۱)
‏۳۵ بازی —
🇪🇸
اسپانیا (۲۰۰۷ تا ۲۰۰۹)
‏۳۵ بازی —
🇧🇷
برزیل (۱۹۹۳ تا ۱۹۹۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94562" target="_blank">📅 03:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZQgAtZCjjSAhhDHMGVdtQMDKVHHakFNQnfIsQj06_YHl57Es9lmdWXDSxYeO2lumb_UYJ-eFYhoZD6x_yUZ8I8Jmxc5qV_Qn7vjjO0y37Z5dDqrERrCx2kWGPATYrIy9GXRBq17tnIxJdCV0Nx0Crz1DxrAXThy-bkvPtR9c85np4FgTNlqDw4TUiAVoLzeX2Au2vRKEQQ41J6oOh-pIaBni24aPDf6nniY3InqpAwTmrVldjq1TgZaYasxovIQRrxfNUcflAk8XTyi3s-cD2gKJPWaG3zB2zH-mPOXnSP39LOLhB1jl-71uEiBFmNlMKhO5SteK-I4EY2ZTDjqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه C جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/94561" target="_blank">📅 03:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ-AfNysIRegDJQHYCeobGLm52LljodCj8hfV-M_GnV-awDVJOqWs7K92OBD5o1pCuyBFWA-F6_gTun84To_7JR7YZb3Lu0UP8A5ODLRDb3tG5adkuJejgVFB54YdKJzUX_H6jxHpPDx4pQd2-6wk4B0YG3cojrMswCCtaN38zcsa0H62pn4eyk9JJIIH21idNaFGNaVIhDVZexiPLpthXboJG-VlHyBSckWk12NBJtXZ6mo2UhmtSHNk6Mp3MaqsIidgc7QiD9yzYGus0h20inOMqWh-I_oT1Z8oY8B-_4BHt6D6Hehcor4lxfH-3-5Z6JBWDSidEmr65cq96oDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|برد دشوار و مهم شیر های اطلس مقابل اسکاتلندی ها!
🇲🇦
مراکش
1️⃣
-
0️⃣
اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94560" target="_blank">📅 03:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRiug_z0qR2Goeyld6eGYaCjqfsB69g7_1cxEaK6szK9KK5HTM9yRnC2CrE_UJm8JzbQM9u5AOK7O3Vk1E2NzDrUrq5kPZFcobWIuVebaPa_1vQfPe9Q6ORymYQtByZ_k7CJ2DZau3NP_Xu7XsgEepYe2ePNqTkW909dfHzgp90dHmUq07I9aQNqSYcPMb-7Sxtsgn3HKJFf5c1fe-gpE7EP4Lx0Py3M8PROnyqbmOMVVg8v-r3zOoETAllHERhDLhrTICA_tnO01WQExbM8J0pe9_Pcyi7XGuzbER6KhR8c2QfBUIyMV6OvAWAefSIWtNbuiXYyizsk5fc3Q320SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
کامنت فنای رونالدو زیر پست ژوتا: روحت شاد ولی به رونالدو پاس بده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94559" target="_blank">📅 03:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnwAVDBM8K2u6JhLuEAerH6C7uPysRQSdobfrbBk82N31SjdCkr-QRb1G4rj20HA4_NSMmgK9UAdAwkyHyxXbLVAGZxon_X4sgcQdXp1ZHfYINw2W7b6FfT8Tpve86I7XU6YKsOopuvqkQNVX82HDoaZnF7wuEUPd7PJ2Bc27FD-W4mr6jkzmOfymh1blCoeiLA39k9gU5kzARVJ8qeQyjHObLaG4SHIeg6XQnN5XBK71Lf2xA2UJx4FP3hQ73IEY_6-3X-YcrI2A-DLWb8qUA3Xpc8umIpw6bPecIiDOuzi7Y-YWa0H2W_peGs4fUcGfkh5U04MHHug_RTFtAv9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکاری دیگر از پوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94558" target="_blank">📅 03:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قلعه‌نویی که تصمیم گرفته بود روزبه چشمی مصدوم رو با خودش به جام‌جهانی ببره، ظاهرا تو بازی بلژیک هم غایبه تا شاهکار دلالی اردشیر بیش از پیش نمایان بشه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94557" target="_blank">📅 03:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZk-3C_sXJYp6IBDmcAdEYQmEF61Uf2hJXWAJdCoaQiY2L0aRoAooBnNGkoFi6UtC6ii0RBkFPZnLH2Sldtzd3UM3vxkgGIqZRZcDTzITEl9aeVqdv5eeu0r4Jl4bJNAK-25AdhIG4MU0ewA1-1n3hk0oAOh3oXWRf9ErJnCjZevQOyYjhGStn7ZHBaq5BoVLizzwWCw-m_3XEL5D71mjfGjKT-p7bkmdGBNPZpbSz14ZBVfgnIiwcqZg0piWl4__xc_5RqHBlFMoTCY0teM_QqTorIeOQRC-XrXHNE3OUCmdW0-LfSTK4JWnm5Y_5lLKJyFYm9uRcmc-LBhjI_vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
#منهای_ورزش
؛ مجله تی‌سی کندلر در رده‌بندی زیباترین زنان جهان در سال ۲۰۲۶، نام کیمیا حسینی بانوی ایرانی رو در بین ۱۰ نفر برتر قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94556" target="_blank">📅 02:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDvyeYCS8nI0PBCiKY8mEqG-NecQNtIoU2O7DoIDdJUut574_0tIgAJ1xtI8FGvekf9GgC97PC5Gk02wAtkXhgTyOjROF3ZCBPcp5eF8sxX4EiQ2mxBpUN1ikoUNoXEGPfD_hjxmR2kypliLdgaE5UOUOA5GG-2TG3mtTE8wXQQltQxCQx06FbW5ODTsRtjAYdU027VS8u1qHj6zGFy193ZpVcfArgZCo-zqzrKxPzZU9vZVorPSGtS0-Q5m2TGNcR_bkASrtpTAq1uFEmsjcZWRViNxMPVwjPE70YOGuEljn3pyk3AMpOsD_t-2npttwSMWJ3GAMhIxYKLfA-1W9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل هائیتی؛ 04:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94555" target="_blank">📅 02:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5a95aac0.mp4?token=TZ1FLWcIgUwwJeKkXIIUJpethnNTQSqaz_C4AXTLhtmvJHM_x6c8IXfi5JwRhQ9D8W1DADGnw150Di7BCq5oiz2NHDBBzyZw67LmzUF7jrNf1nNqkgoE2J5OQqXdAUxPqH3RzKqM1cC_6XaylvR0ZzDCQdbyG2jzErK0ZV2GUMwgjGdx8eklDyWUAaZ8SgPDsCMJPQWYpinNXyalEYoS4-4MYt9ZNBcMBN1O8LiulDca3K7LNnsuYQkC0hxm0JLShkQ6HiRPbkzrQ_JkG8NXPqD8EBbgEzVnAmhMoXJ_lbAbCurmgQJOXmPebDz1SxydujCGgEpnA2MWkNccpMtVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5a95aac0.mp4?token=TZ1FLWcIgUwwJeKkXIIUJpethnNTQSqaz_C4AXTLhtmvJHM_x6c8IXfi5JwRhQ9D8W1DADGnw150Di7BCq5oiz2NHDBBzyZw67LmzUF7jrNf1nNqkgoE2J5OQqXdAUxPqH3RzKqM1cC_6XaylvR0ZzDCQdbyG2jzErK0ZV2GUMwgjGdx8eklDyWUAaZ8SgPDsCMJPQWYpinNXyalEYoS4-4MYt9ZNBcMBN1O8LiulDca3K7LNnsuYQkC0hxm0JLShkQ6HiRPbkzrQ_JkG8NXPqD8EBbgEzVnAmhMoXJ_lbAbCurmgQJOXmPebDz1SxydujCGgEpnA2MWkNccpMtVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
نمایی‌دیگر از پرواز بالگردهای ارتش آمریکا بر فراز استادیوم‌ محل برگزاری بازی‌امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94554" target="_blank">📅 02:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پایان نیمه‌اول با برتری مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94553" target="_blank">📅 02:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=tvdjaTjvIGXe3ljRYFLCuoEcsRLttFqHcuXgYKGC-bAGIL0M8bgLgcbayWL1Mh68FInOJrdmJpU0hZ-UyfaUP7wWzZS3ZU2EQ7ec-fGUHpndgI21QgzI5ASw_VW7y_fXlVmCN532ZngHrP0fhxIg_daMrefwOyolGFutXc8u7RsAmmKkQnpgMtLBrc0vSrhM0-smd3KJQXwZim93-2JSAkwuF8YZf6u65muRqdErwW1PwNVqMbh1Nz2xcIULS4XAu3rm8RUkH74W7JfqE45y3XbDXTbTrHdPFaWG_nwNwWXdC4o1XHTLMkt4etgMj-oU5qjIdJBYaZ20jIvRrJSv05GdXgr7qGRfYLXM84JoRPbtWCdArXIMcv-sqTYcj175lUFgvsXqZaN-qoJPLEmNTFf-OPZenpanh1_PcVFosYiwaUIvHm4pU6-cMdVQdQe5DJX90VTBA8ZwZ8Ck_s6FAUMu-cAC_kBoYPAsQA3ukNdpkQlCSLCSp_rz3e5VwMFo6obOxTQAgTpCVH0GgHC799sYgGlVgCWNIgLgDJWkykv9-KlAIt75BJW0hXViHHRl902ANwIdlt1ZJ67LEQPpA-tvyfYvtoHU4v5euXE96b8wJKNV1tlA8L7NAwUkyjIwYfSBFiHbdcmso0uWlkA8IadDHJKk6d03Ycmpjk-emtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=tvdjaTjvIGXe3ljRYFLCuoEcsRLttFqHcuXgYKGC-bAGIL0M8bgLgcbayWL1Mh68FInOJrdmJpU0hZ-UyfaUP7wWzZS3ZU2EQ7ec-fGUHpndgI21QgzI5ASw_VW7y_fXlVmCN532ZngHrP0fhxIg_daMrefwOyolGFutXc8u7RsAmmKkQnpgMtLBrc0vSrhM0-smd3KJQXwZim93-2JSAkwuF8YZf6u65muRqdErwW1PwNVqMbh1Nz2xcIULS4XAu3rm8RUkH74W7JfqE45y3XbDXTbTrHdPFaWG_nwNwWXdC4o1XHTLMkt4etgMj-oU5qjIdJBYaZ20jIvRrJSv05GdXgr7qGRfYLXM84JoRPbtWCdArXIMcv-sqTYcj175lUFgvsXqZaN-qoJPLEmNTFf-OPZenpanh1_PcVFosYiwaUIvHm4pU6-cMdVQdQe5DJX90VTBA8ZwZ8Ck_s6FAUMu-cAC_kBoYPAsQA3ukNdpkQlCSLCSp_rz3e5VwMFo6obOxTQAgTpCVH0GgHC799sYgGlVgCWNIgLgDJWkykv9-KlAIt75BJW0hXViHHRl902ANwIdlt1ZJ67LEQPpA-tvyfYvtoHU4v5euXE96b8wJKNV1tlA8L7NAwUkyjIwYfSBFiHbdcmso0uWlkA8IadDHJKk6d03Ycmpjk-emtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
واکنش یه هوادار مراکشی بعد گلزنی کشورش به اسکاتلند مقابل دوتا در و داف طرفدار رقیب
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/94552" target="_blank">📅 01:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr684F1Fc-Qy5OgpEr_DrdNDKPnqJZuiZtQOgYZYhzYPd0M2O7ZHt3kaprg8W2TWiKVHSP2OOXHdQNeyQRIJdQ_udPVf9-EqzmhtIFIR2o6xq9QRi9Xd3xcVrnranCNiHzPZoM1EtfKuSav3hBFEHfcYqUaUVbB0HO1Fxtwqpp76CVGJTOD72tsT6zKSlPXwVKI7Q9RkEA33DLZ1gY56nSudfwnBOQKtARMabN8Yi4fBYs2TMXZF64Yx-6JfT4EqgAvLgwCnqr5KcfIt63CSsaPYARBVe2t-jWJtMLlniGn3ZJvubQTGWDKGrJVSLu1e-dlRV3kMivx7R0lsdjKkWkv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr684F1Fc-Qy5OgpEr_DrdNDKPnqJZuiZtQOgYZYhzYPd0M2O7ZHt3kaprg8W2TWiKVHSP2OOXHdQNeyQRIJdQ_udPVf9-EqzmhtIFIR2o6xq9QRi9Xd3xcVrnranCNiHzPZoM1EtfKuSav3hBFEHfcYqUaUVbB0HO1Fxtwqpp76CVGJTOD72tsT6zKSlPXwVKI7Q9RkEA33DLZ1gY56nSudfwnBOQKtARMabN8Yi4fBYs2TMXZF64Yx-6JfT4EqgAvLgwCnqr5KcfIt63CSsaPYARBVe2t-jWJtMLlniGn3ZJvubQTGWDKGrJVSLu1e-dlRV3kMivx7R0lsdjKkWkv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇺🇸
پرواز بالگردهای نظامی آمریکا حین بازی امشب با استرالیا و ذوق‌زدگی جالب تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/94551" target="_blank">📅 01:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONS3NTY08FSOOv1LxfTTj-r0z1R2oG3u-vbQ_jomTF-VWlm9wiJzyelzaHRs2U-JwRB6c5B7CG4GOVtvv0WwlgdT_QWTtOEMB_aSV4HvittaU5g0xG-PoWYRsjeADabq94UTOflzW7mdeV9EwNEhlZ8VNaPpn2CNGTxru2bSKsVykL15js8xKSEV6_hu9tQzz-QEiVlk2US5ccns28Tvu8ycYK7Ys0XKdpwe2Vzkm6T_4RK-T3TULq2NHt5HD-69TjzgOOr-jP97uXwGGwh93dZIrdAdMJy8KhVM7MMpkeLfBZ4I64hdxA3lPQBhkDwmIVNkT2n_twlwUUqEKKSDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌اسماعیل سایباری سریعترین گل جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/94550" target="_blank">📅 01:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=rJsFOEQlbhP1TiMUccP0e3lDJO0bcw3jGIknzdk-NPlx-UWaA1xRkDI7ioo92AwfrAFUoTa7zujJp2DVW9grx0yrrESpP1kUG73-e-plnHXP0H-ou-x5OGGU9C090GanPVSLfCt-2zcP2rp7vj2B1ZuIDM-HEKTrLEodPnrvNe-5w1PFmDThC575vHSiBRRHqQz5QBQ3sDBWD1Q0VDoi012Qdu-Mgh508s5yW386gPeyrbXahvo02YwX7hmVSWKRtW_6vyWc3-Pz0MmchwLohoSrApv-Sl-mZdPSd6lJpx4bmKuZIKUPVXeCsUGtYW3ziFpy-NgoJIZMSBoFhFttcYwJ_GmknMNKkvg_pVVg82j5Y-CBGHUjdap-C5dLj6EhsOD_hQM4VoKP7Ftdxg1MujwgXszDQzsX6T7xvVLNGOnf-H9LxjX9NDfgxKSYWyOFy1obNiYlmtoBqDCgu-oPEwnZxCOdxbzWJpyI0GpWeOz5BeE2_OP4memZQBLzeYPn2fonwgtbjUs6PENTToeBsTj_Wpl9CWicQXOHoru-Arpauo9mLyp8c4CwLKHlcGczVgT5xPazURJu4UPk7ohFU5VcCb7Px0wr4g-2LXiwI85Q2CS_EMxuB0rpfaq1CIyD1RRCNzfK3dh5uVc25hctFkCdTbGFf2_zOW0VdGX7bAM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=rJsFOEQlbhP1TiMUccP0e3lDJO0bcw3jGIknzdk-NPlx-UWaA1xRkDI7ioo92AwfrAFUoTa7zujJp2DVW9grx0yrrESpP1kUG73-e-plnHXP0H-ou-x5OGGU9C090GanPVSLfCt-2zcP2rp7vj2B1ZuIDM-HEKTrLEodPnrvNe-5w1PFmDThC575vHSiBRRHqQz5QBQ3sDBWD1Q0VDoi012Qdu-Mgh508s5yW386gPeyrbXahvo02YwX7hmVSWKRtW_6vyWc3-Pz0MmchwLohoSrApv-Sl-mZdPSd6lJpx4bmKuZIKUPVXeCsUGtYW3ziFpy-NgoJIZMSBoFhFttcYwJ_GmknMNKkvg_pVVg82j5Y-CBGHUjdap-C5dLj6EhsOD_hQM4VoKP7Ftdxg1MujwgXszDQzsX6T7xvVLNGOnf-H9LxjX9NDfgxKSYWyOFy1obNiYlmtoBqDCgu-oPEwnZxCOdxbzWJpyI0GpWeOz5BeE2_OP4memZQBLzeYPn2fonwgtbjUs6PENTToeBsTj_Wpl9CWicQXOHoru-Arpauo9mLyp8c4CwLKHlcGczVgT5xPazURJu4UPk7ohFU5VcCb7Px0wr4g-2LXiwI85Q2CS_EMxuB0rpfaq1CIyD1RRCNzfK3dh5uVc25hctFkCdTbGFf2_zOW0VdGX7bAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇦
گل‌اول مراکش به اسکاتلند توسط سایباری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/94549" target="_blank">📅 01:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مراکش همین اول کارییییی زددددد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/94548" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلگل</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/94547" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشب</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94546" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0yAJ-zjknesTwnHXVGJW_Ei-Z1VtW2IMRHykNmdaLVnZ-u_tzqsUeSq8llab5G8_nusefQ_l8_4AcNuF6wdI9Tq4MdD0Eae8Be2Pc1VSt8fE50_y7Ri-ySXX5a1MlYkOq71huOEAOQ_Oz_BNDUyrsIC9s7cyJlQ4mZuuTZbm1UVnRcf92IAFWi7F_cEN76zpZlu1NJFYUl8GSL1jL975SXgi46WndfmxA5uCuBcBIe50onUiz9SkK0aStL-XDDs5J4vFrZWuqKuWSlRad2ZQVvfzIylPRovbhK_OMh0sAhubWMaUkqyZf6wk7LiynzqhBg_Wq3m_bDOT_XzWGPHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
تیم ملی سنگال از مشکلات متعددی رنج می‌برد: پرداخت نشدن حقوق بازیکنان، انتخاب نامناسب هتل، برخی از بازیکنان به دلیل کیفیت پایین غذا مجبور به سفارش غذا از خارج از هتل می‌شوند و سرمربی این تیم چند ماه است که بدون قرارداد و دستمزد کار میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/94545" target="_blank">📅 01:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇹
👀
یه‌سری منابع خبری مدعی شدن که رونالدینیو تصمیم گرفته به فوتبال برگرده و‌ میخواد تو تیمی از لیگ‌سه ایتالیا فوتبال بازی کنه. باید دید رنگ‌و‌بوی واقعیت میگیره این خبر یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/94544" target="_blank">📅 01:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBH6qplBE_SwC_pKCHP38BwquzMPzfxFHmCRB4ubPQI782zeAS9KqTz95njPzL4LAnqggwwoKTxposC5WH0rec7oVreyQxTzI0Ac4EsZGBslog8-dGvVw8EL6RJlOjb6fzuiaw6qMRvgOGUzcn2QJE41AqokLJ3CMveJsNED3o5_wIcIpli_U4SwFEgJqghR2Mo9MUcwlrsl3Wcf26B5rDpQJegM1u5VKKrSfPO-4zw20wBXR1WsyXk0iROjrAuvYjVdjo2ds_yN9xbHvRCJPa0dRhLJXsIPuC3aju8LVf5Om2u6aX5jBr0px-QIwz2T-AvQkBjOUvaD4MZsANCXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووری
از فابریزیو رومانو؛ کانگ‌لی بازیکن پاری‌سن‌ژرمن مورد توجه اتلتیکومادرید قرار گرفته. بازیکن با باشگاه به توافق شخصی رسیده ولی مذاکرات بین دو باشگاه در روزهای آینده آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/94543" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2dilgsR6cZaUkeBzA7hD-n9qgCoOEv_bwe5YJbcS50MQvzmHcKOOwAtkevSBSSE_R95RHqssXBtZWKVKID0qAR-14oCYItWRgy8J-GxKrbTXhzKump8wjag6KS4GcQJGScZknXBau4ziDONmeb77vBxFppuLFT1Vkhps2HLWvyP7t2SS9F5KWYCr2FVzKDA526QB8q4-U_WLlz902sfz8fZC_O6C1qFmvhSrP4BK5iDJJTz1rC1gUNO81qTyEnqxsrfQpNR6fPOZHtM2exAXzT_bH6Wgc6ksfBR09_BZXReaSM8tCnjw3VeXIwqxBjLZRZx_JWfMc_MP9_GD3f09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طبق گفته رسانه های انگلیسی مارکوس رشفورد از ناحیه کون مصدوم شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94542" target="_blank">📅 00:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jysNcZ-cwrQBgZnHQX1NDbvQ-vKkNP77BYtgdQySA2VnNLKCMNUDShwvmBFfmxPioIxyucnMtz5vnSm_81-JZ7bIEtkqCmgqnuLH2AEdaDEXqfJky1q_4GvuQlDq6413v3frQMNGgR_hQx3HPwAt_IWLxoc66aUiotkiqFe_Q8ClDw9FrfK-MXi0Vjb7PMurzWCH34R7VVaXrNNIMOfeMNYX8vcLd4cIyitmOjvQXM-DdxWKUwVI6dVHyjTttYx2xEKFz03y7u1-MLFm9179eBOUcoIvJez-F6MjqvFDSzaEmknPB2s23BSvvhBKmrevHs8DaQMtwtEeREEkmNyATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
📊
تیم ملی آمریکا تنها یک بازی از ۱۱ بازی آخر خود در مرحله گروهی جام جهانی رو باخته و اون هم مقابل آلمان در نسخه ۲۰۱۴ با نتیجه ۱-۰ بود.
✔️
۵ پیروزی
🤝
۵ تساوی
❌
۱ شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94541" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGN3sB8DrekrrvJt0VUXtwnNqOVAfp4oiYHJC6GnPI10CkX01zKkzKGVuAO0A1XxBWhSHrNj_DZOQPCyVlw9HbKibyYSKt9DKbl0wuDBX1sjNtnzU_PnvApkoMmGCbcy89OkzRE6gxNzP6EuVS0yG9AUMC2ncjCxJfPnlrxYUKBfkZNkDorswJ8XJNEKgt77oROUcd09H-xwVR5PI03YCq9fDyNM2_lL3LBXZr9KzrrPM2gJfdg_P-q_j7bV0mgkyQWkq2rpxCqpIQx7r_-u6tdwBcfCbovcqursXRFvdzdXyql03XMA7HMZpeuZZiGklAJhQeNnYIxL25bBxIQ4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بالوگون مهاجم تیم ملی آمریکا به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94540" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94539" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXRUVZ2zZcDMpcKRXuxkgDIKmeus7u7awUxfkfiSi3mx2Plmp-okBmeJ4IUXnCXXL5bkkAEzgXpc1lG-e-6bJBZGg_5KPTdN6k1Ki3GRO-QCVNhMcvFSq8AFqTT2wa7T3NgGqQTzye7EIUbAkRBxBu9f-UqSEjOHgBzWslSusDN5dLTBo4SunX8Tw4G0KEBguJ-3qiTiqkoW7ldCtHnIPqKaNuREzNx3G5OjQV2deiWi6JgVgiS2V6_xhN63xvkO1eADF3YOuYJsj_nZoL2NkL6hZbNEgEeEbBuC2qxqAm7ysJx6SOz9RE_s-weN_9gEqpP_vqbsQ05-hi5UWjAOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94538" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufIoHf2VunsTUa0sOLX-sOCv0mdFsxLusRTKcWtN7FK39deTSpkL1XCeCZyuTF7cG77YUQPuMLhNe-QQSNTZBaB5nzj2h4ysdk1PzlcYT4IHD6-Bw-dWDuNvs6fthJt0AXRDWihrCtyrvyiaLonirR9jRzrXTUFR3f9VlMar9IaPbRpu0JFAtMEk5V8B6MIzENHvh6x2LC_Q16xrbc_q-5PRxIxAgXxwB__FmXJhpJRw-9spbj-uoB8PKqJTBjSRrXmDoBjkCAT6Q1yEokIfNzudWekYdiKBpV_rkghGWW_xmL3n0y23xtk29l8FGIB8GB2CYquMPID4ERtSFJ7zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه D جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94537" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3DhzNwPayzhkHz7L2ioz4aOLAPTtYTXcwFm9QxUCDo3g8d5sSni5RhE14pNh5_3f0WuvlqnQMBWnGx3QwhXoTihss7PRdQ-FB90HbrEozSAO45PVkH8xsXiCWkiN7dWmAYXLBG6ZDnFtJEGFVK8ry61FHtTr6Y4XdvSo8PoEhxP1rUavEgZ7ZZy1HDzhEMiqQiHwDL67yl3ipCUt_bDXVDZqkhBhDqgVYAngViCCzPnRgKKfN_3KWOv1P9Zzn-kEuafBiqfMO6P9VB0VUiP196LhRNDn0SIlpTY2Z2-PKfW1wBeEH94tPNOiSH0ZC6DGsoZuLQ_Jmk3sGbfIoxhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94536" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyCexYe4ZuySSjd6a1BhRmCidWQk3XJ5BzD4rYEZNxMedYvmuguJyhzNf7079fY83vCq9H-rZ82YTfYYIw0lpaZ5tZmx7N4eqC3SdVnl3eqMdQf-WcZlnhPQAXzeNqKV5XyicyEyZIfqkIwlzbs78ilovbUYFhEFTyuxu9q1Vz1NxITW2iAcOfE63kTPdB0YCvIB242jLGkbCNMH2WvSekq7LJSrR5siNlYssvsvlY6riRaPH_qanDuiQEkxBZF4zKLLMMHpjRABD_UGdYHMARGLDRjiX79vW6eUh7aylxBH_zSEurHXKi4fokGlFb0LVOyI3fhzNUDKV6D6qb3Liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🚨
تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94535" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onNpMsyhsRcvqggbEACZ9QVXAZNFF0klDPW14nckKyWRTFvEKowpE2hrEBoYyyv74AG-1gMoO0-ea-q5n4dbCjihdobfiYOfAKga3YeCtAOaSdN3w6__ezYUuOzp4dlbdNXZKcqqjb9kPjC4gd95FEL18-XoiU6s7EmXU_chReHiI5u3--Kpg6Rc4KcSUQrZSpTSPo-UxkaiPMnsTvfA2QwAbvJ-MPw_CQjD8dofJGGG5pb5iBlgxPJKNebqSkXr0tOm2fDindUWQHc-ArGluOh5R4nbi8S-x8eorW9CTTv_mUFLj6DjqFH0FS5ZNN1ekT-agvoCDvyPrR4bTTHKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش برتر آمریکا؛ کانگوروها دست خالی زمین را ترک کردند.
🇺🇸
آمریکا
😀
-
😏
ا
سترالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94534" target="_blank">📅 00:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94533" target="_blank">📅 00:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94532" target="_blank">📅 00:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این دقایق برخوردا وسط زمین زیاده</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94531" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">استرالیا همش دنبال پنالتیه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94530" target="_blank">📅 00:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdru-RJNCiOH_9Opx6mj0ModDLK6-VM55EmzrfpsQ2n5RxIN0qb1axVlN2l39gJcTXOT9Dn5Vbxjpz1MIM-G8SEk2t7JJQVSPQPd-a_UtQJBBRJzeushrk_R5alYRBSX_YWUxXIROP6aivh9Hjwev421ooY_s7pQ5mM9ERq3wFG1o4MQ-J_N1hJUUO8lnup5KhrwJP2j4ADp0gNZQBXUkVT1bjMDlA2p4gH-OOKLPDlX5eqNevBQwph0ejXDDwEsZLf6TKM9hzvGz0WgTEHFDjLlgc7dz6ZBJxjPLYaEdx_NjFCveI-xcsj8Dtap1bm7FUbMLnEa4MCOYMZQOTd37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو تو استادیومای آمریکا میدن 13 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94529" target="_blank">📅 00:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZQ0AgFCOE669tbgQ4_NnYNA-dEoxZEmoaEtYqqBCN3hqfJurOm_Wbcjy-fve9VDgvNxWhdoY0d9uzLKJZb1szTthvjIxEbO7H29GEneGNJMn-8ny_O0W056Qw2msCYEJI5gNEzZWSKJP1gm4-0FWAckbWDW1TGVARq0zHRDqIDuW8lawjGBoWhC5LJJWpsYpTTyNOFe1FtEzb1Q2V8tNc2MHm1IEAiUDUwGmuVTImm7BEwwDTTthfEggf-XnOiEtuJG2TIGYtLTly_J9rMLXDVIZAkFFBGregamkHeuxR2WvzadR_Y1d_0W5skbGzZ8deNUlPFSsp90T8mhQQHtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDATl8TtdobuvabhLo9KLYjoJqWm3Ds4YXKDkx2kJGZXIGiXUxgXCY-pB2ybqdWMjjCb-btVOIPiYfhi0E6tZIcaNBgKSv-jFR2M4cHdwccsb3eYJ-Q2CpHOkKy8Cc8Kf5E2clJweR0jWxMhEl9sZve_6LVdlDMMuaO813YckAQajOF4BJ2o8XaeThM2Dq7eWE0LNp_FL8SkPOdH0Ttg8E23aqm0pofpoOyxKoYiChmq0rnnu_YLdFlTClh1KWprIQ6twlUcDPp-fe9zp2uUimFIQW5DP9DlYgRbKqFHVHwQdL_vzyYD6XYbgHt8WFXgdO0yrvZFZlGaF6AwA2oijg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇲🇦
ترکیب اسکاتلند و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94527" target="_blank">📅 00:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=CryN75g9zRPSJ-KRsUVKt5yYJbvkJTh0JJlZqfZ3MJt9YgLf-KHNgswZFSaC_iGHEZ5XLWaFrO6glKkjKrsU7G4gU2mXFgIXl6Xv_plmiaobU9QQyQWiJJuWQGmmpvVR1qQ_M9A4mo1DqQsGCk8cs4DuFBrj0w8GqwB-mmjdEVj-hwpl6bU5zcPy19o6EjtrrK04KHkURdATz6moWDMxgN2K8xD4emJllyeEC5N7KGq7JSPumrzT_NwJsxtAlf_0vd09FZptnymAEkz50vI8_9JxPxiuedG0AhrrDnDpY36TS_ZLVAGe9zfV_InbEhXgyT6xtajTRSUZUNXzMz2OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=CryN75g9zRPSJ-KRsUVKt5yYJbvkJTh0JJlZqfZ3MJt9YgLf-KHNgswZFSaC_iGHEZ5XLWaFrO6glKkjKrsU7G4gU2mXFgIXl6Xv_plmiaobU9QQyQWiJJuWQGmmpvVR1qQ_M9A4mo1DqQsGCk8cs4DuFBrj0w8GqwB-mmjdEVj-hwpl6bU5zcPy19o6EjtrrK04KHkURdATz6moWDMxgN2K8xD4emJllyeEC5N7KGq7JSPumrzT_NwJsxtAlf_0vd09FZptnymAEkz50vI8_9JxPxiuedG0AhrrDnDpY36TS_ZLVAGe9zfV_InbEhXgyT6xtajTRSUZUNXzMz2OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند/ گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند/پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند و تمرینات خود را خیلی زودتر شروع کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94526" target="_blank">📅 00:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استرالیا داره فشار میاره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94525" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0GruEcymKEIYLLN5_KbGd3vCl0rPAu-Nsp6pFpxFj8gM2XTW-mY-LbCih94vZHd8aMt6wIvQSHySJ6nxM2p-FPcqphNjgHRX_Ea3P__P5epLU-tSJ4Jp1j3BIz6KRM5o-VpXwJLljwOFKVs-CLbB0ETYfHg0FuIkgZSrYSQylDKqjqHHvTPSVvg3ezx6TxnW6qNTCKcqC2JELvB6VA2uBk20D299Lnyjp-putdy4CGEflHwG6nETDn65AwVGQ_FdDqF0BPOJDQLOIN-mWSNpyzXAw0LxLr0gyyZ3YX5UF6BfUm5h8IRn8cH-Lw99rd1X4L9kA2XTwsFGFUgLRJayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پست جدید رونالدو تو اینستاگرام: مثل همیشه متحد
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94522" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وااااااای چه ضدحمله ای زد استرالیا خرابش کردن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94521" target="_blank">📅 23:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puaAhdAagJAgi5bjdPKTpZYV3rnBsI7D8zuvvdqjjIVhw65H2EetmC7ukn68UhUrIMiIgvBABYqHuFdwC_TOfOQrhUj8CzBA2cr3obMNJaWSCp3Yl4XeRYcB8Gb5FRXKQdc5_OpnryHehCtONMjvUblOVbCVJZvAGCwFZ8Dau2uh4rqWpBgIvECkBLATKcRcvlaklyiQG3_yn_NiXx1WKlTR_E1O8fGBSnYReplxFV7vfZ8ZIBTJcqIsMdSTiV1yJkq_QcsPEssx_efB_mSCUvtF4vMM5QbNzHr2nujUD0H_Cm8x4P9rFfkoi5SYrGUs01gg9wPP-_L-RU6rXlmGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh3XiYuD9eUd5j1A_PPNFkMV3y4SiY1RajhpGSMvT3zzW8LT9tYbjGdDEoNbngTOWB5FMSa1qQK_o40v_cpC-asABBkwjzhN8lYJZW7FcWarfupcWnw-fDSS50ismglUFBbL6cyCcaMYAWkXZ294l4ReWl3a_7BJ3073xoXoPebMzF8OsTeYoCcUvWn4PcPNcJa1nmb3SC8Wb3CuBgEk4jNYlyR805UHfgsHGrXdma6zaz6aPmcBPtZbcFvGc7ggL3ipF863yr9t8KcvPX0idYDl8svqNLdpCtLMZbREJj7W4yJU3YM5Cz3kBE86RSF8qJsU64OUBdUBbNVCqGNDKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تینتی رادمن بازیکن تیم ملی بانوان آمریکا قبل بازی‌ توپو آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94519" target="_blank">📅 23:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">واااااااای چیووووو خراب کرد بالوگان</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94518" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94517" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0663a525c5.mp4?token=ibJXBHExPofR2D1EWZLWM0vqTscxjxC6CcguuBx5Rxj_oH_khP-C4vGor0_Y_Zrj2vrX1KDx9pYRngTFr4mBJvhSuIj8fWmi42ubZ7TWrszQrl3OaP9qWaWlIaErHj9k2yz2xicyvjE4__PSMaTTIYH1NNBi5wMVASrkQP1MDZCZmzGQszWz4x3sed1ki69ISnM2MhZPHyXr2j9kYmC4x5WuonNv1qm2nsIEjj_W4sFCUBVu-Y5ClQwoqWWW2Pf67WVZ4BBnZqxxACbXF7l2bmv2EQWDddYukJ_pQUxK7pBHJF9iLHMJUkKIeRlFIgP9dRoFLuPdqwjtf9B8WSuRQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0663a525c5.mp4?token=ibJXBHExPofR2D1EWZLWM0vqTscxjxC6CcguuBx5Rxj_oH_khP-C4vGor0_Y_Zrj2vrX1KDx9pYRngTFr4mBJvhSuIj8fWmi42ubZ7TWrszQrl3OaP9qWaWlIaErHj9k2yz2xicyvjE4__PSMaTTIYH1NNBi5wMVASrkQP1MDZCZmzGQszWz4x3sed1ki69ISnM2MhZPHyXr2j9kYmC4x5WuonNv1qm2nsIEjj_W4sFCUBVu-Y5ClQwoqWWW2Pf67WVZ4BBnZqxxACbXF7l2bmv2EQWDddYukJ_pQUxK7pBHJF9iLHMJUkKIeRlFIgP9dRoFLuPdqwjtf9B8WSuRQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدول‌ گلزنان جام جهانی:
گل بخودی - 7 گل
لیونل مسی - 3 گل
جاناتان دیوید - 3 گل
کیلیان امباپه - 2 گل
ارلینگ هالند - 2 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94516" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58175e8427.mp4?token=SqHrXbu5wg4tW_lLGAaYNH5MzFkGMKvfAnbFg6I8NpXiq1EahJVdv6YTx65OwmrcUa07_nyasrF8EcSOWvKjrQyyyYn7JRZW66PiXMM_zGh1dzIODA_Uey1PelVFNpS2xhyXH70k6uXZ9qE_qLFKjNt4kl6dVd8v7bIOyb5m_czBvCSp9Ir53HoetmUFQtLY2jDotuMdHBRLHFRc2A7QbFljwvCwFL3sqP08UdehmV7Xw9yjQ4I-pyTnClijT-55CzhLDIb4l9aTBK99YeVyFI_quP2fDetI2vJowGBZ5vi_cdUDG0ozXvuJSWWfTW80f7qAIfDgrtWdGY6YZrupSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58175e8427.mp4?token=SqHrXbu5wg4tW_lLGAaYNH5MzFkGMKvfAnbFg6I8NpXiq1EahJVdv6YTx65OwmrcUa07_nyasrF8EcSOWvKjrQyyyYn7JRZW66PiXMM_zGh1dzIODA_Uey1PelVFNpS2xhyXH70k6uXZ9qE_qLFKjNt4kl6dVd8v7bIOyb5m_czBvCSp9Ir53HoetmUFQtLY2jDotuMdHBRLHFRc2A7QbFljwvCwFL3sqP08UdehmV7Xw9yjQ4I-pyTnClijT-55CzhLDIb4l9aTBK99YeVyFI_quP2fDetI2vJowGBZ5vi_cdUDG0ozXvuJSWWfTW80f7qAIfDgrtWdGY6YZrupSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلاتان و تیری هانری به یاد قدیما اینجوری براتون دلبری کردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94515" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=RfbuqvYZlS2Z-1xHesKNITJwoq5D5uH7crF2DuARUvwJ-55OnugqGbMBr5-WSGAoKUMedoFBdvKBu3_edO2Me-SYJ2uBIIXT7jIWqx-Vna9kGWA4u9NkV1dRF9iZbJ7pEIQuoQxD3d2ITVvaSxHdpkLyzHMSF0XFKGoZu74IwtTbV3GzpHm6WAXIn099trKUsC2Fgay-mk3lPcErkOGp_FuVbGnFRy_WxHQA-gHPKfarEG6ML1b-7iqOvNUJ8kw9_4AQ_8UfC-UPCfAyOhuRqQJ_Ehivd47Nf-zFfyhnwmYcTtDEXFOTCh9qIDEfgMaT0K5nGjt8RC5EU0YkVRY0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=RfbuqvYZlS2Z-1xHesKNITJwoq5D5uH7crF2DuARUvwJ-55OnugqGbMBr5-WSGAoKUMedoFBdvKBu3_edO2Me-SYJ2uBIIXT7jIWqx-Vna9kGWA4u9NkV1dRF9iZbJ7pEIQuoQxD3d2ITVvaSxHdpkLyzHMSF0XFKGoZu74IwtTbV3GzpHm6WAXIn099trKUsC2Fgay-mk3lPcErkOGp_FuVbGnFRy_WxHQA-gHPKfarEG6ML1b-7iqOvNUJ8kw9_4AQ_8UfC-UPCfAyOhuRqQJ_Ehivd47Nf-zFfyhnwmYcTtDEXFOTCh9qIDEfgMaT0K5nGjt8RC5EU0YkVRY0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود/پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94514" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پایان نیمه اول؛
🇺🇸
آمریکا 2 - 0 استرالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94513" target="_blank">📅 23:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
گل دوم آمریکا به استرالیا توسط فریمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94512" target="_blank">📅 23:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94511" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آفساید اعلام شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94510" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94509">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلللللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94509" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94506" target="_blank">📅 23:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v229UU66wbl0w_E4YdOvyz5wAk45Cag-5-0-KlMg57AEpGBj4PHNg9AzhVOuS0kkENpCcS8SrftiIGi469ZiTDUXsYGdVJvmRMu8SyIwDx-iszcOgIXMIJsTW5tZxXSSckOlu9jbxbtx8VKO_B9kgXVS4EIUxLduKJSCs0QSInGOqGKTh_sEqB2kSY4541cX_mVRudN1hoKEXGbbMHkHLP3R8csFumWtMJzb3eUY7qxLEGAA65MUUpdvEIOw4AUuI2yoEinIS6JIFFDbRbjP2fnhTuOIjyo1w2t4I3vFf7CFP3m7lpAxXFKLHbbKsoxdQ7QTrdp4wBtS-3XKKTmd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
خطای مشابه خطای مسی توسط بازیکن استرالیا که این بازیکن هم اخراج نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94505" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3R56SRpjO11urdfYSI1GwZjD3MDAZuvt9I6pMMRK29LnQQ_uk7BRLJ4BjKRkYmpdgBjSeQWPwzWFOI-XMqNZyYOwZ8g8LPpDXa_GUEwTseVExCxDQ5e5qvErSWn3QGk9b2JMHkoKZkmBHh6spMYSgaOZxAouu85d3fF5VBe4nR9ur8WiAquSvnkRdKk7UknkBw7YU68ZdOX6yho_WtUe4-E3JwxceNwpJ3tDru4VAKG_iBQHL9ppY2JNLrJe3tYC0XsfZOFkXwbgD5g8O9PIsxpFJAPEnvKFuwiX3jMvrmH8WpEXlLBT6qdVuuA1K4nYRhj1y7UKV4ateG6cOuTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇲🇽
🔺
تقریباً پونصد هزار هوادار دیشب در خیابان‌های مکزیکوسیتی جمع شدند تا پیروزی مکزیک در جام جهانی مقابل کره جنوبی را جشن بگیرند و این معادل هست با:
🔹
بیش از 5 بار پر کردن ورزشگاه ومبلی
🔹
تقریباً کل جمعیت منچستر
🔹
نصف جمعیت آمستردام
🔹
تقریباً ۳ برابر جمعیت کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94504" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
