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
<p>@Futball180TV • 👥 700K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-94887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2kiQdhOOw6ev4mJgMUBxNscCtCyjnO9Zu1cRaeHLAELJcaLxHJKsBN7Sx_cQO6OAWG_yGqVKxIoPMP3aftDHFPDiw3O2v-Sp-Myl8PouIjsTyg1vX5eQh9Z3jTZg7IpC2xR_dI8xvVBOXplQzb2D_2ZWkcca-Wu331DwAPxpptstOIpwXO3N6yu_SuWpTN-eYSLQ0NxKQIY7vlhA-11Qx84nyNN-CkD8C5qWNrAmSFUF1G5qnbenwEFnORab7gTdaYUFW4b2JgKsdI0h7CKbBwxu0lvypQ9T_otM3lAnMepjj9YvzKgbHgfD7gouCDOYSdgk6NorzTPsy0HqozPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عراقچی و ونس در محل مذاکرات ایران و آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/94887" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_sv7uNIqVRURCGd128D9R4x2GEVbF2IRQfJnKrtKDWwNUXJw5MZZEHzRzDG0JEK6YjcycQTSuuydG-Xt42sTNLoJ59zI4I8tZ5HuUfHTXfqvheNddNGvFNYe27pUHyFFl5vu4io8APmO32L1xqzurEdNhBcRzAcLMOHi_nETTpbCCG5RkvaU7Tr5N7P_57LIsKCW1YIjJByvSwRFeOKthV2PWCx2SFVU5AZ1vUmtV4PA7CTYWGoVqRaMzrkQpB4uGbV5poHNqfyPy0pJRkRrXnFgnUxxF8udAmOMgLVAUlM-xGCuIRb5kJyBE8gINRVJTy_m6EJCdyz1Kkh0AZ_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ورزشگاه آتلانتا بنز آماده میزبانی بازی اسپانیا و عربستانه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/Futball180TV/94886" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94885">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK3466GZVM91OvQH3okJ8QJdL_q9mYmFKfjWvxq74m5twTeBWNHC3qNeyi1VmlYGzVbyNJaAHXtVddRlmaWWs44iOCHQk1vyqEYDUjT8JsnB0o3LVqgl7-Be3-5tj6RyakAhFlhgqR631M6-B_uXRKLf1bV3BJ9K6s4sw6HZ9JGSehYup3CdIEp0Xq-yoM1vcxpbB7ViTN83Rr1BNs5120C6m3G1j2F2JGoJ6dkXSY6PFne0x8yuxAgBxjdp6fTSCCha3gfDNGTNLWr0AH7K-vnXiZKPrg2qQCa3AD0cmyvNsYgMc7XPwo4dUGNPuyZnwM7KEpH2tTZFtfxDN3hvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
موریاسو افکت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/Futball180TV/94885" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94884">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/94884" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94883">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT85_b_cdV68_BMnuiVqYgKoAhUtUS1Pds5KmGIhz404q076THcFdrUbT4EnEO7CEbBuLnhMhJdQFJSKYlqgkKmSH-obZVuUVjqfFfbFEI5o_HmM02xP31yWRU_LYN32n3WXE4cZKIFHdVcKqZJcEMbIB12vBcHyVPfI642SCD0k3ZDnTyQZPlVsH7CDl9en8yZaUTRY1q6SB7CsnCP68ET-dFsri8-pRLwVLtl7epa8d1T7uymkClwtXuej_V2JFaUhuuUSDpkpNYz1z92VQWr_fStrMjIWW6r5B8Z2ody5OdiTE98jbOApWXWdMVnALPErgyvdMU4mjgrhZFNqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/94883" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94882">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a47a2cec.mp4?token=pNdnbBU_PlexSL78s25xVHQeYIHoDGy-5xWyQeakncF1KQZpwT6L97lN9ZorPT4kliqtBxUCSecxsRTfUXjhNy9-maAm1PAa0lqdvmpLpxIYqdJZUBA4wy8RrvUHjaFsfCy5a2RWi37EWGytv1bIZZMgjnNwKxNpFueMq0baCJjqWeobEN3O8SxfLkQxasAlrVu3hpkBNHRIJ_vbftYQgPQNucSbh2vsvmjLTT9yuoCxRYaWwlugjw7v1Xo5iADQmYEcK4n6MmHaltQlsKVSduUCcK9nolakOVVvXN3Ag83W1xPgeqSjZmVoq4Dbe-qA0yt6DoYNnjqiU3LQH0N_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a47a2cec.mp4?token=pNdnbBU_PlexSL78s25xVHQeYIHoDGy-5xWyQeakncF1KQZpwT6L97lN9ZorPT4kliqtBxUCSecxsRTfUXjhNy9-maAm1PAa0lqdvmpLpxIYqdJZUBA4wy8RrvUHjaFsfCy5a2RWi37EWGytv1bIZZMgjnNwKxNpFueMq0baCJjqWeobEN3O8SxfLkQxasAlrVu3hpkBNHRIJ_vbftYQgPQNucSbh2vsvmjLTT9yuoCxRYaWwlugjw7v1Xo5iADQmYEcK4n6MmHaltQlsKVSduUCcK9nolakOVVvXN3Ag83W1xPgeqSjZmVoq4Dbe-qA0yt6DoYNnjqiU3LQH0N_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبلا سگ‌ها موقع پیش‌بینی بازی حساس باهوش‌تر بودنااااا
❌
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/94882" target="_blank">📅 16:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94881">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💥
👀
🇹🇷
تنها تیم‌ملی لایق ترکیه همین والیبالشونه. ماشالا یکی از یکی دلبر تر
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/94881" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94880">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b04b1860.mp4?token=kJsAPF_c2meUU0buUcqD44mHb2faI5ElXyFACe9NGGXnK-Hc87FppnAY350zmFXPZ_7IYJy-AvNRTqvX7MYVqnswxLKf2qSBhJkJMQGdl5Yui7ejrbkbvJ4_vJF3heQLHx8jNcts8sV0BHojgtxBIuRJEjKrtL72GuxS8v_acEylLNN_c8cWAupcEpGZkjrQo28QOm5W7g49rjDWyIroArVjrzDYeInbbQMAWtZ8erAT79xaQ2lg8cB2kgFDT3xVj9-hiArt_G_TyxdJWholrlsp9mytUoI46hn8QIsZX9IC0TTDj0v0q12tfJjgYTce9cG_6_HzBoXrnROif9sUOFPvLdWw124UslXm4HWtr7T5XrlFKR80kNFbxLifcSJ6mkz9cjoV2bTK4RdjJIK0xJrwdTbxeIt0iDIkVFXVwW4tM_n-pNg6QdHohuh1DbDPoponukpe_HtyedJ3UtVr1v4AtzZRzR9eyA0qBbaiVrFZJ0T-Q1byISY_RSv9Yn06UkpjZS3wWK3HE9WlD3gWpQoT04lWvRu0ovyCIjmaw2EVrY88kyVvlta2WEdAsR4JfmqBjtHSpZfUTKQos-pG4IujAzGo6SexrcTO-kH-J8keatQ4Ai4o1nmMEZVJouCuco87oODLaEiXyxgAcjsKm5exTgMoNMBbKldDDqlJCFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b04b1860.mp4?token=kJsAPF_c2meUU0buUcqD44mHb2faI5ElXyFACe9NGGXnK-Hc87FppnAY350zmFXPZ_7IYJy-AvNRTqvX7MYVqnswxLKf2qSBhJkJMQGdl5Yui7ejrbkbvJ4_vJF3heQLHx8jNcts8sV0BHojgtxBIuRJEjKrtL72GuxS8v_acEylLNN_c8cWAupcEpGZkjrQo28QOm5W7g49rjDWyIroArVjrzDYeInbbQMAWtZ8erAT79xaQ2lg8cB2kgFDT3xVj9-hiArt_G_TyxdJWholrlsp9mytUoI46hn8QIsZX9IC0TTDj0v0q12tfJjgYTce9cG_6_HzBoXrnROif9sUOFPvLdWw124UslXm4HWtr7T5XrlFKR80kNFbxLifcSJ6mkz9cjoV2bTK4RdjJIK0xJrwdTbxeIt0iDIkVFXVwW4tM_n-pNg6QdHohuh1DbDPoponukpe_HtyedJ3UtVr1v4AtzZRzR9eyA0qBbaiVrFZJ0T-Q1byISY_RSv9Yn06UkpjZS3wWK3HE9WlD3gWpQoT04lWvRu0ovyCIjmaw2EVrY88kyVvlta2WEdAsR4JfmqBjtHSpZfUTKQos-pG4IujAzGo6SexrcTO-kH-J8keatQ4Ai4o1nmMEZVJouCuco87oODLaEiXyxgAcjsKm5exTgMoNMBbKldDDqlJCFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
جمعیت پشم‌ریزون دیشب آلمانیا کف تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94880" target="_blank">📅 15:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94879">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd444c9174.mp4?token=EBCm0iPZQTlhvHG_1__pMLiMR-OpVu5iI4-x378YstRAzHkMGhDRNF1Q6vHovlr9lJT3W0MS8SwUiaozTrR_ciq27F-utILNqbqPyIXB7EeET9qT29Y3pMJDjF0Y8NQx67Kpqc7CKk2n5NSXeZDE3NoVfuXFrCm57TsYNwG5-LoNy4tu3Ovn2Jb_d-wR9IshJ7DgC3abqcvY5SJuezXoZBsg7v6y637UO2CT1e4NIhlurceGNgaDQYkNMoS9n7UeQnnpUxiUNhQMSslTNQ7IxLA-AJnCCSvuBUxU_sXuobDQZPG_ssQYtWx0-msw6JltlPnn-I8V6R4GMi0E_Cr9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd444c9174.mp4?token=EBCm0iPZQTlhvHG_1__pMLiMR-OpVu5iI4-x378YstRAzHkMGhDRNF1Q6vHovlr9lJT3W0MS8SwUiaozTrR_ciq27F-utILNqbqPyIXB7EeET9qT29Y3pMJDjF0Y8NQx67Kpqc7CKk2n5NSXeZDE3NoVfuXFrCm57TsYNwG5-LoNy4tu3Ovn2Jb_d-wR9IshJ7DgC3abqcvY5SJuezXoZBsg7v6y637UO2CT1e4NIhlurceGNgaDQYkNMoS9n7UeQnnpUxiUNhQMSslTNQ7IxLA-AJnCCSvuBUxU_sXuobDQZPG_ssQYtWx0-msw6JltlPnn-I8V6R4GMi0E_Cr9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولیسه تو تمرینات فرانسه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/94879" target="_blank">📅 15:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94878">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d5db04cb.mp4?token=rZr-OvSemMG_h_w60Y_HH7EvB4gp14_7dL_1AVR-PkdNcK8bhyU3oMBA_hmpdO2emUh2rCPOItmtg5tqWb8w7jbubiFgZrRZn5rIAnFQ1WHYpd5_RbcYChrISjyNIhGmuxHSKmtKnOPqe4BJYVbdFZl0PLQQT4AJzUCYbpOy0kadYbGARknD8PaHdZ48ZpPerPZx9BMPiFWIutCkpmHae9PfQyNVqYwg0l9cdphaU5IiDkLqrLNZokvTh2PntF5L6WFVOH7lcFVidilUjMu_CD6qxfM5zvnDGst1-22BAPYiAM8JuI0LdGqnyd0FtJUhUNADu3ef-Ixc3kbw7R1yyVodwthQG5UBodNxQIUp33_mcmzesUV6wlLKwu7ojnoAherVrpFnsyS4gDFyi5WcTwYgbBRKG6IJ-kYzcchprBO7ofAAON-kv11kEyZe07CInyMPzXaacKFRNyjAWiirxykDzOgcG6QFUAiAjQMHUFKLRITHdaOAii4opPu8wEl_vzVW_Zv9Zx3MFp-8ccLUKjZtz63jSzYKhKgRoWoOMOLGs-u0G26c6JQwUsOxFHy-X-0KWSWqN-qBdWjHr8mxFjzm-IOXYQLxOCSFEXpKUa7EDxyW7myWTu4A3HknKjD-Onk82wNRPp5qXClV4AnM4siQLGU9OT7EdxVjKV5rVGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d5db04cb.mp4?token=rZr-OvSemMG_h_w60Y_HH7EvB4gp14_7dL_1AVR-PkdNcK8bhyU3oMBA_hmpdO2emUh2rCPOItmtg5tqWb8w7jbubiFgZrRZn5rIAnFQ1WHYpd5_RbcYChrISjyNIhGmuxHSKmtKnOPqe4BJYVbdFZl0PLQQT4AJzUCYbpOy0kadYbGARknD8PaHdZ48ZpPerPZx9BMPiFWIutCkpmHae9PfQyNVqYwg0l9cdphaU5IiDkLqrLNZokvTh2PntF5L6WFVOH7lcFVidilUjMu_CD6qxfM5zvnDGst1-22BAPYiAM8JuI0LdGqnyd0FtJUhUNADu3ef-Ixc3kbw7R1yyVodwthQG5UBodNxQIUp33_mcmzesUV6wlLKwu7ojnoAherVrpFnsyS4gDFyi5WcTwYgbBRKG6IJ-kYzcchprBO7ofAAON-kv11kEyZe07CInyMPzXaacKFRNyjAWiirxykDzOgcG6QFUAiAjQMHUFKLRITHdaOAii4opPu8wEl_vzVW_Zv9Zx3MFp-8ccLUKjZtz63jSzYKhKgRoWoOMOLGs-u0G26c6JQwUsOxFHy-X-0KWSWqN-qBdWjHr8mxFjzm-IOXYQLxOCSFEXpKUa7EDxyW7myWTu4A3HknKjD-Onk82wNRPp5qXClV4AnM4siQLGU9OT7EdxVjKV5rVGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
شوخی‌های خرکی هوادار برزیلی روی سکو
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94878" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94877">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNA7L9cYCqETskf7DAX6Qno3bKgY538EnDzw4uC2imWSg1Q0jEzUV0-Z6lXUt1DcYoqFbbRcY_GMrNiHNjWAbmqzYXjwBX6ZOBHoWfL5x6UzAPtiHrnqf9ZRpZa8Z2kqAK0POs0aG6x6nT3_rFanUHOLhMNzJAkbW757kVKMLH3iXF0to9B27FNJTXNGxzA3Q0oUG6BrBxzg9V1SYlEp0jKdTB1KtBQlx9Pm6_dEKLGvCB9lVZ-j1jXVL1juMRJWQ3rQKrNXEt8zQpQlpSukUpSk9bSByyNQ7lK3ZtcmbzhS7OVaq6foXqJ7ncLOU_7dDvfIwmq5-KXyGt9pl9eHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ آاس: رئال‌مادرید والورده رو غیر قابل فروش اعلام کرده و از بین شوامنی و کاماوینگا یه نفر تابستون جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94877" target="_blank">📅 15:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94876">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b9907c47.mp4?token=d_eBgMdTZcoIPJt1SBbuWxPLD_o2Zq1hrDkKmrHdMIehN9Lang6iYURB9WJQsuqA_eYwbSOJ8Hrz1ieILmPt4c1aCFmtPwzwg8eLP6A0I0voN9ZIMNn_9xVDLI7OVOX9qaxpNycUkmvaFO426CcOFr0q_keOghFXeh2hK-NyKoWLSIlQEaDE-uBYFLOH-SVn01NK4OtZIp_LywJo-1e1ijX9nhipmI0-pKhlJjXJ60lvE8aieQXzP0_RVOwB-SdRp68msoEud0uBe6yA0KoVs34Q67yMdcAiIuJpYvYcFvTr8WEbGeUxZGOF5e5WnYzXV6XDEW5_HeKja5SG1YZxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b9907c47.mp4?token=d_eBgMdTZcoIPJt1SBbuWxPLD_o2Zq1hrDkKmrHdMIehN9Lang6iYURB9WJQsuqA_eYwbSOJ8Hrz1ieILmPt4c1aCFmtPwzwg8eLP6A0I0voN9ZIMNn_9xVDLI7OVOX9qaxpNycUkmvaFO426CcOFr0q_keOghFXeh2hK-NyKoWLSIlQEaDE-uBYFLOH-SVn01NK4OtZIp_LywJo-1e1ijX9nhipmI0-pKhlJjXJ60lvE8aieQXzP0_RVOwB-SdRp68msoEud0uBe6yA0KoVs34Q67yMdcAiIuJpYvYcFvTr8WEbGeUxZGOF5e5WnYzXV6XDEW5_HeKja5SG1YZxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
کنایه قزوین‌طور عادل فردوسی‌پور به سعید دقیقی؛ بهش میگه بچه خوشکل بودی
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94876" target="_blank">📅 15:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94875">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SglKCbYiSrIMQfVeZ3o9ysODT3AJncrmm4v9ZDygAzSfYV5Na6dWjeeY14Uwdk9OAx1HgT5SC8rQeBdT9ZZK8eaB0DVkS_Utc37jPGdc2QsKtQIINOafaTg3Jzgov9xnA1_urxYwAok-Yl0Qmn24qmcXiHS-CD9QW3qAqt37QDpX6WFzNHSwMQgpyqWF7Za-jWTAIbgw9XQnC9k89So80MgCs0NESH1a61CV_41CPQoBLmEK5phcUygScVVyhx5d69ZJnXElWm51EsXM2O1gMwCpHFlbAVNU8q_TH9Jr3k2PauQQUOnUc8btN0IyFnYh1qcBo8NFppJTymyX6wfRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
به احتمال زیاد رودری تابستان آینده منچسترسیتی رو به صورت بازیکن آزاد ترک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94875" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94874">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چه ارتباطی بین برده‌داری و شادی گل وینیسیوس وجود دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94874" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94873">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0e690550.mp4?token=URwR2uyyf16SCS4WFpufnj6_wURGS-c7xDa_H2vsq598ig_uS1WVzcCUvrM-pajIjsVyBmo3ApUdtNXAaZDMyqgylZ-3LasJK08lI_cosT7ZuaLcDVUgjDllsI6MlLs9J2OsKTEl_7CwD67wSESStzpnGBj8MG461EGg9ko4cFoF55Vl4XdiUydAM69eha9TM_tFlVkNztsk-6Op15QOzeSpIKTGXFTqWhSLVv2wIqvfoJhp-93-UPeN1myslLkUvJnwmgvYkd0mwMubOUS3e91mX5bZLb-VUFNZWLdJ8K3SLIiujee8Ygy4P1xmh_wcejL1LLezgKNKqziIMUN3fSDmsZk0iNnm-fdu_X73n0Nj-_8dQ0cVsEgPkRmYvjmbQezSJHCP2xHuvwWniSgpZOhqz8Q8svHrUhFUgb9CtoMdcn3t6oZvO8rfrVEqyur0xmLYNAQ5PNLkOtrt2DxUnDapPzj9NJm-RtBhy7hJjcAN8-9C4xDwDpu5Hfsq7OJ5Z6i1O0VBYtJYELT1WkbBgaLKfv9d1KF6vAFRT9_xiCg_aRZ8rdmGYfvKteulFjUhDc8OKgLZa5RM5yGX42Lf5gdctfCFIfay3UjH-eP3-6o9AFJDrF-FLMQrvqYB6ID_iyqkft5yJL6EAGHhWaK4PwZ5nSk7tDsEcC3zSI6JNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0e690550.mp4?token=URwR2uyyf16SCS4WFpufnj6_wURGS-c7xDa_H2vsq598ig_uS1WVzcCUvrM-pajIjsVyBmo3ApUdtNXAaZDMyqgylZ-3LasJK08lI_cosT7ZuaLcDVUgjDllsI6MlLs9J2OsKTEl_7CwD67wSESStzpnGBj8MG461EGg9ko4cFoF55Vl4XdiUydAM69eha9TM_tFlVkNztsk-6Op15QOzeSpIKTGXFTqWhSLVv2wIqvfoJhp-93-UPeN1myslLkUvJnwmgvYkd0mwMubOUS3e91mX5bZLb-VUFNZWLdJ8K3SLIiujee8Ygy4P1xmh_wcejL1LLezgKNKqziIMUN3fSDmsZk0iNnm-fdu_X73n0Nj-_8dQ0cVsEgPkRmYvjmbQezSJHCP2xHuvwWniSgpZOhqz8Q8svHrUhFUgb9CtoMdcn3t6oZvO8rfrVEqyur0xmLYNAQ5PNLkOtrt2DxUnDapPzj9NJm-RtBhy7hJjcAN8-9C4xDwDpu5Hfsq7OJ5Z6i1O0VBYtJYELT1WkbBgaLKfv9d1KF6vAFRT9_xiCg_aRZ8rdmGYfvKteulFjUhDc8OKgLZa5RM5yGX42Lf5gdctfCFIfay3UjH-eP3-6o9AFJDrF-FLMQrvqYB6ID_iyqkft5yJL6EAGHhWaK4PwZ5nSk7tDsEcC3zSI6JNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇼
دیشب بعد از تساوی اکوادور و کوراسائو، پادشاه هلند به همراه همسر و دخترش راهی رختکن کوراسائو شدن و باهاشون خوشحالی کردن
کوراسائو یکی از جزایر متعلق به خاندان سلطنتی هلنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94873" target="_blank">📅 14:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94872">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af848d920.mp4?token=tu2p9vciRiVMswDgkubajekCgpUWsXkU0ENSOX8KifZ26Ln3_ziJxJdOpxR4_cAyobVMMuDQqVsvFCEr7t6qzwAuobnx3Y5D3kpH3jTkGKLhgZ_V-izdv1AOb-cWZi6PVBAbJAOwM1xcL_zaOpUS4FpAYZf1d91oud6b3E5rFpIu9vBBcYV_X2jMB5qs-AZaq3PgAbGoFQsNA7sveZ6oPTmCH9kp5BWV4qMBcSCmULDt5IoP7B4De9fvrEgdFJXtkR2A17C4bDqlGqLfkgCicIHZSeBOdRhZA0kE0c2hVn9fpFRBvqAjNmALa3UOLr8mcwpZyzuxww8Ze1ghQLHqxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af848d920.mp4?token=tu2p9vciRiVMswDgkubajekCgpUWsXkU0ENSOX8KifZ26Ln3_ziJxJdOpxR4_cAyobVMMuDQqVsvFCEr7t6qzwAuobnx3Y5D3kpH3jTkGKLhgZ_V-izdv1AOb-cWZi6PVBAbJAOwM1xcL_zaOpUS4FpAYZf1d91oud6b3E5rFpIu9vBBcYV_X2jMB5qs-AZaq3PgAbGoFQsNA7sveZ6oPTmCH9kp5BWV4qMBcSCmULDt5IoP7B4De9fvrEgdFJXtkR2A17C4bDqlGqLfkgCicIHZSeBOdRhZA0kE0c2hVn9fpFRBvqAjNmALa3UOLr8mcwpZyzuxww8Ze1ghQLHqxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرهنگ علیفر امروز صبح سر بازی ژاپن اینقدر حماسه آفریده که کم‌وبیش ویدیوهاشو براتون میذاریم
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94872" target="_blank">📅 14:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQwReUmLJhW5dJCiH0q-7E0meCbAGfggtfk0XWjL0nBk_rK5-hGLMmN9Vona_8PWUNrR9h-ta6u4LuHlibWDysL-9dHfRH6t1lj1zKrBrGDI3trm2pEYeZm6PF2xf2r6DwdB3kQjMTJbgwyJxf8dZClHHqOOE3kC2hQMjVIF3d3TVaNZ24LWjbw3fvabf3yaEEgfohPjeN99MHXXdFhLOf78fpmS0azuMXRE6FJIcMEsiiDOuc_wv1-fvfzvceH_W8Ujn1BhZND6zeIjaFEHcHG_LL3mRDy2DyPztPbV-3020GgxorWx58rgvOelnFK2xVW7e_7JXu3LtOmrI5CAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
تیم‌هایی با کمترین میزبان مالکیت در یک بازی تاریخ جام‌جهانی؛ هر جا سخن از ریدمان است نام تیم منتخب ایران میدرخشد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94871" target="_blank">📅 14:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGksk7DUyJEWHYGtMIDkNZATxu3_Scp_EWeZqyht22yX7ge0bXMpv47c-AMwOZhOwbZHvPkCu7zfo7bp2x-pYt1anTrZedh2_QIMZFU3Dyyk_5poxy1doFhZdrPWEVrl534ov_Rd3K3epLCaFnWG9JNIT_G_csRRtzxw7GY2AjlFE0IQcgi7_e0LchD9Mm3Zkf77bzMknyY81NGsS8gBwURrlnK0aFNtoliyKZ4yVKhzKyHuoizHqfdVv7S4flsLAvxEkxvM353YU1RjSFGmjMbanIcg5CjR6dyxEDYKrOmkdLAbJVlav3C2QLkVaC5aVsBAyz-qEwJ63izeFwhzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - بلژیک
نمونده.
🇮🇷
⚽️
🇧🇪
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94870" target="_blank">📅 14:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fnh2isjLg1Bh9ueDRgwUb3Z1zrgK2vcUSbj_IcWWr7nVcl9O3bVya7huF0Is15TWdkkbm2ZGismNZ5D_yAxJI0OyCR2mvchN8W7PpsdqCr0Dg6mJ28lT6jli-_C51Ho-RjFldn-smIMUVfzU8Q2DIhn9lpxxIZbiGekULQ0HJsjp1Io-04hl0GIvFZ3d304s69cmb7cZ16rpTy5IjxTaUnIzVyY431QJ1m1S_wWO0kmX6CrhVrF0ObPKDClL6nAFIHys1AKfx4WC1jcJHiVtdgkfpY4Xo2NqfT-cqwmG1r5UazX0tmlMBdvTEWV_cFTPM9nle4HDm0dyR35ir_XdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
امیر قلعه‌نویی: "از مربیان حاضر در جام جهانی مثل اسکالونی و ... و کاپیتان‌های برجسته جام مانند مسی و هری‌کین می‌خواهم علناً درباره رفتار ناعادلانه‌ای که تیم ملی ایران با آن مواجه است صحبت کنند."
🤣
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94869" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac5f38e3d.mp4?token=NgF1ilLkrPQKOK4ZTfutsMtYlUz4O25qkfc8SXoNeJlFD6SRwSgI1-YYPWW1LiAGS8A25ii6H-Wcy6j7X_CQZg15sfmbMuWmHHPQ8WivqPsk2m8AoAhsG4Wp8vcE380WXG5GOtNgKS8ZT6A4tsMRK6LdYZimlmpUcnCdLub7fXRrOSvOl_4ZvnLVaSXe4lxQnjwk736hq7fxzuWTVi3H2T4-RhKv-CBz6JNkj0oTsCSuxU35zFDU490a2klyDPRDRkD-ZztE-2htWB4EKIi4zBId2eUemgLhU9xtn3i2e9TOhLPcCyH-Wm8lttIzErAsjSwPl9rxY3cP37ve_8WpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac5f38e3d.mp4?token=NgF1ilLkrPQKOK4ZTfutsMtYlUz4O25qkfc8SXoNeJlFD6SRwSgI1-YYPWW1LiAGS8A25ii6H-Wcy6j7X_CQZg15sfmbMuWmHHPQ8WivqPsk2m8AoAhsG4Wp8vcE380WXG5GOtNgKS8ZT6A4tsMRK6LdYZimlmpUcnCdLub7fXRrOSvOl_4ZvnLVaSXe4lxQnjwk736hq7fxzuWTVi3H2T4-RhKv-CBz6JNkj0oTsCSuxU35zFDU490a2klyDPRDRkD-ZztE-2htWB4EKIi4zBId2eUemgLhU9xtn3i2e9TOhLPcCyH-Wm8lttIzErAsjSwPl9rxY3cP37ve_8WpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
فقط تو جام‌جهانی این صحنه‌ها‌رو میبینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94868" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U09ccbQOIQpsrlxXLjvzJVhXY65Y4GsI7ToK5Rb-Jk5cC020nO41Xj6Spm9PBDkyWVEGF1ELHMxxNyr8QL4pbzESn_eEj3mqmoU3_cOqtGa2xwrY3ml2Pc7-tm6b3u4ZpteM9OK4nCAynq5mLFt8cjmfNJAIqZqsM7DfS6XB-DeOyN10LrVZMb6OsD8sb1vC4eU_cXIqLoyFCqgY_A8tj_RdJmXpbMcL9hM42Np64EtF5Lft_cSQ8RLZ4CnP2_oo5EwVJaa6kvVRDElrVPMdHZP_vlpj6EcPye2RQ9t7BejNmLPYUuMDIxPji_WDcYI8nVooKPspktV6s8rvBnH-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✔️
تایید خبر اختصاصی ۱۶ روز پیش فوتبال180؛ با اعلام تاجرنیا و همانطور که گفتیم سهراب بختیاری‌زاده سرمربی استقلال در فصل بعدی ابقا شد. حالا فیک نیوزها از اسکوچیچ اسم ببرن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94867" target="_blank">📅 14:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwLoMjtU3FvNyL9hfblw68TpZWAgCD8yY0QpMZ4-HCq-yiiJyZOM4zwsF4RDjibFNfZ2w-ZW4gBm5NmgTpOgMd28G7Eg3iHV_IWEjmCeE-ACFzOouYt-nrALfLlAA9uaY-EZ7NRK6lX1CQ0Ow3RINP7XlJMvg_kEZ7yl-nR7EfGYUzAA49D64RGiFq9YljsV9VuSwOSDf1HDkGkTbhJQKCpwCj7a7HpsnqGPAYXuxIjA7AaelBrySdR7Fno4fFClZcKVLqjQWW6aSsHE5gHNDZieR59RyCDjBKik7-i3Jh2huFob3eEnoBPsOx1mBiH0YsQhbxjqvY8NjqAfpPXYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
10 بازی مهم تاریخ جام جهانی از نگاه اتلتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94866" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLQFTKxPPU9tSaEZJx-sQ0Z-HH1H5pm3doY7mCp_rMgmUBE6DSRkW8wm1YdrKJxwpUtOxbH__gLam-L0b4WqkzCr1UKvL3nsEeOphi4ip9BnAOddNpfTB1jF4q5ulYh-yKh8wiMgve7pSY-0CdltHm7bkRM_mcVMYKDcFGMsRkYWWPPxw20l_J4M3sT7TM85yUnvGtbeRoMOL1ZTyWbrKMZIivDjQ_dIkmfSlRMw75qmUIz5pJWMoGsHZ11WgriwLTeWJEXLU4PzJx-t3Ypca-RYFsofElHUXDF6xBv1-kPZAtsD6Lg0qpCuleqZhw0SXrmqp6eXB1NgqEW7QbeMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
خودت را تصور می‌کنی که تا ۴۰ سالگی مثل مسی بازی کنی؟
🚨
🚨
🎙️
🗣️
لامین یامال [
🇪🇸
]:
"غیرممکن است. غیرممکن است. غیرممکن است. شاید بازی کنم، اما اینکه در این سطح باشم.
این خیلی خیلی سخت است. و همچنین نیاز به اراده زیادی دارد، برای من او بهترین است و هنوز هم این را ثابت می‌کند.
او نسبت به همه برتری دارد با اینکه ۴۰ ساله است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94865" target="_blank">📅 14:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb45Kn8DKlhbS7SvuBxCoLciuo1EGW8Lm2m6-CHe-CyhxeMoUWGpAU1u7h4Yxi-rUpcVpEVG0H3JP5ExuNvv2VA3cdMRE6_2Hxx3F6zRd336BQ2raCgucapxqef06na0SxHKsN46zPNsIBg4Q1EqmdazwuywIj60DxRqc-c1LjmOAlD28Le1bs8pxuY56TPbgPCrT1Zl5a9Hn1Q53xTqtpi3OmxkMkfitX8NSF0U-VnlJiuXIrbETjU66gxTm924p5F3q-wT-0KpL-ayaxYlgrYtys5b8tQbrPD5djgHcXMsjEciGLS7GUkXT3zSupfQ0W9Ug6M8kzrb4adcGopfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🎙
🇪🇸
لامین‌یامال: برای من گل یا پاس‌گل مهم نیست. فقط به بردن تیمم متمرکز هستم و سایر موارد اهمیتی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94864" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593635efc1.mp4?token=Yr4IlwqVSN5GPMUcdcb2JbVm-EiIM1UvI8KMbVx6TO2kvKR9g_leTfK93RI3Pm9oed2IrjX4mO-t2sv2Zds840l-LPv-wgOE5vxeFxm8knmCKxyyo_fyGEiiQn5Pvwt0HDgqFTyW10sKIukDhyiZw5ED-ZdupAizqwFpyGhfZSObQwOaeZmsN4vZFZXBoNwX9mKP63b1kzC2_Z88iMh7Cda8Vp2nACS8kLRpTs_jo4EMJ0kMPCGVJe3ABkWB2V61nX5gBjl0zRInP_IZK248WZkc_o4O1nX_3wNGs4CMRusJDulelTrss2dcVmZ_mxukRKhVws2N3wQ59QfNRQmAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593635efc1.mp4?token=Yr4IlwqVSN5GPMUcdcb2JbVm-EiIM1UvI8KMbVx6TO2kvKR9g_leTfK93RI3Pm9oed2IrjX4mO-t2sv2Zds840l-LPv-wgOE5vxeFxm8knmCKxyyo_fyGEiiQn5Pvwt0HDgqFTyW10sKIukDhyiZw5ED-ZdupAizqwFpyGhfZSObQwOaeZmsN4vZFZXBoNwX9mKP63b1kzC2_Z88iMh7Cda8Vp2nACS8kLRpTs_jo4EMJ0kMPCGVJe3ABkWB2V61nX5gBjl0zRInP_IZK248WZkc_o4O1nX_3wNGs4CMRusJDulelTrss2dcVmZ_mxukRKhVws2N3wQ59QfNRQmAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های جالب فرانک‌دی‌بوئر درباره تفاوت میان دیگو مارادونا و لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94863" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWHbyZMxoYCZr7g33DZMyyTwJadKGQutNlvAHDxdrfSq8XuhqUbXQopQlCenZiFgJD43bv4OkglgwDynnLWqe5TVtdmVr6cBK6i3uV6G2GUEyDeezKMlnem_8P2SC6F_kNxMoKj5KNQInENwYEAvR7oxPjsCMTAy2ZZajShaloXoFz7IEDijvZEb0OZpNMGtQeh3m2lc1ylliJrAj6ItY5LfG7ykFq4O_4mcxWBqHkees_QzS_-WvSO5_AfSCSFgxVomjl2RuWXD9ngonAEvDfe3SBeuJ84Fkd5p5D427ear3nZP6l7L2yk6PCkr51CiSs1bIhXCUK4jV65gHQdJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوری در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94862" target="_blank">📅 13:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f56e9622f.mp4?token=EeE3M2nmI23Z6Yvo05YknoR19uiGMxILiOjBS82JVupTzkHOztmjC_6aHiiXxSVSlPZtK1_fwSiYOx1GJybMRAUrVNiGjt-SrmLVH1QrDyfFkjg-Qnoq-nCj5NY4i9dj5wF2vRTRVsQQQKqxy_9wPRF9CaDySpwQWPuXFJlxx98-eD01_jsreh9IC7xMfVFo3v7J4Cn3FoFko0qu3s5kEcbV32i-ecd8U1l80rKJPk1U_h4CEB7SUh25ku5JZyiie07obfvcSf0oE1C2dnOS_tgfkNl9C3ophDFTCqidgYN9-tOCzAFKLCsLPXQ2YyGtnE484CRiwujtQzPmURxdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f56e9622f.mp4?token=EeE3M2nmI23Z6Yvo05YknoR19uiGMxILiOjBS82JVupTzkHOztmjC_6aHiiXxSVSlPZtK1_fwSiYOx1GJybMRAUrVNiGjt-SrmLVH1QrDyfFkjg-Qnoq-nCj5NY4i9dj5wF2vRTRVsQQQKqxy_9wPRF9CaDySpwQWPuXFJlxx98-eD01_jsreh9IC7xMfVFo3v7J4Cn3FoFko0qu3s5kEcbV32i-ecd8U1l80rKJPk1U_h4CEB7SUh25ku5JZyiie07obfvcSf0oE1C2dnOS_tgfkNl9C3ophDFTCqidgYN9-tOCzAFKLCsLPXQ2YyGtnE484CRiwujtQzPmURxdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
انتقادات بختیار رحمانی از شرایط تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94861" target="_blank">📅 13:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87bdd188e5.mp4?token=RMdzhHPkQp8Muk43jbp5iDUhBYvbp8po7MKnRq3z6Swq4s1rFwucEK7pjndThTCDxieQmW1B6hWvRn6DdEnl8dhMte44BeDN3WSUopSjYkXMW0IDMRYvbUfw3BtpFlCcJVkmgQCf4vDXbD2bDa7v6Nf93kEkN1x6Cq32H0qKARTX6CT9hz3zpJioYdIm9t34lLsMPL6CdajCpJXHquInqIoYXrrNi00RSRkoaxguIsm8epqZEuftGKjIViK0jqyjwFVTQlTq7N3xkNgekKMLtAOvnzrPEFXqjDdW9hegtm0GYy2KpZR6bXGUcuYzlwvqPX7zpn9b8eh8O84fP0Jpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87bdd188e5.mp4?token=RMdzhHPkQp8Muk43jbp5iDUhBYvbp8po7MKnRq3z6Swq4s1rFwucEK7pjndThTCDxieQmW1B6hWvRn6DdEnl8dhMte44BeDN3WSUopSjYkXMW0IDMRYvbUfw3BtpFlCcJVkmgQCf4vDXbD2bDa7v6Nf93kEkN1x6Cq32H0qKARTX6CT9hz3zpJioYdIm9t34lLsMPL6CdajCpJXHquInqIoYXrrNi00RSRkoaxguIsm8epqZEuftGKjIViK0jqyjwFVTQlTq7N3xkNgekKMLtAOvnzrPEFXqjDdW9hegtm0GYy2KpZR6bXGUcuYzlwvqPX7zpn9b8eh8O84fP0Jpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
خب بنظرم دیگه از الان باید کارو تموم شده دونست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94860" target="_blank">📅 13:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94859">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDCn3Y3Gll8DNsphJ_w_jxKXG9_-rdXQERRwBWmdDQwZUxvxXRofJDlh5DNWL-gCM9lGN4GG8U81Dy_5JdJUuq4Q-O-TiZB9hs-Q0u8Ym4t6vAzkDBUMXw4eGXBFgSPOSUE3K69Us95NZkncqpTaJKugWbqQcvUYgDthH8o4JLJTXxXtr7-EX4G-KjXtrfVrN5ZnwH9ZmajgZjfFRWkgKLLTuW_i2D4AcNE7UBAPFcRzOcqWsl5e_ElUlvBCWwDQiThSj6IB6ImbJ0_rZbgY2hoNP0lM-VqrC_XPwvNk2UyPRXvwhrLCGzf9vhZ4B8MHCtxui3h1QTy3Naf4LTG84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید از مدت‌ها پیش ایوب بوعدی، پدیده لیل را زیر نظر دارد و استعدادیاب‌های باشگاه همچنان عملکرد این هافبک مراکشی را در جام جهانی 2026 به دقت دنبال می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94859" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94858">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea2e5c940.mp4?token=Kj_3Rcfa5-O8JjRzJrxtuHOYnAEet-wMJjpI_EznlUCTPdJ5vh8qGkhTuLeLRJp0_fu48WJoKpHNIhUBoScWQQS-C0tqEvrDUPhpHN_-iWr4kS1_t7gE8crK64J4mwA7tjNF9ph1gGoQtKC1ts0QJ18FwIejPooMXZo-MUASPSGxXbY3m3kztRjDtz1mxysl5Tnb_hon3VKLMwT6KoiHOZKcZht4ZpORUq8EiffQj7xwLpOowin48-DrUT1NLRdU-7qmx45THtlFkaButK_xG2X5i8Q6oj1qc-LGko5aRTXpquovhjwYc-QKvna001N_aHt9ZPb-3hwJ35uO9C2mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea2e5c940.mp4?token=Kj_3Rcfa5-O8JjRzJrxtuHOYnAEet-wMJjpI_EznlUCTPdJ5vh8qGkhTuLeLRJp0_fu48WJoKpHNIhUBoScWQQS-C0tqEvrDUPhpHN_-iWr4kS1_t7gE8crK64J4mwA7tjNF9ph1gGoQtKC1ts0QJ18FwIejPooMXZo-MUASPSGxXbY3m3kztRjDtz1mxysl5Tnb_hon3VKLMwT6KoiHOZKcZht4ZpORUq8EiffQj7xwLpOowin48-DrUT1NLRdU-7qmx45THtlFkaButK_xG2X5i8Q6oj1qc-LGko5aRTXpquovhjwYc-QKvna001N_aHt9ZPb-3hwJ35uO9C2mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
روایت ابوطالب‌حسینی از پرواز پهپاد بر فراز تمرینات تیم‌ملی کره‌جنوبی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94858" target="_blank">📅 13:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94857">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7fgkBpmnqfQwz0tHuJDX_T4IQ_Do1ZAnNCjHEszR_U6rhuogtrTmUm9UV-qLy-dEymINrLRjXhHtLbKo2xgzPp0uXp5w0eRLcNpTuv-pGAHMWOROsLHaA2F0M2TdcQOwyjaVLpeP5IzrgtDNswxbfz28e0slf-9iUEFRU3gMctp2Iph3_0aZvZsBTLVS65Hkz1CQF52YTcd1mTeY3-oPE32WTGr84WwVJECEPicaXopEhhe9UC-JE36DhxIMGuqMzfFAd6V21-k6MymOzj8Kza9tzhCS2A-bJFC1DgW-3vtFioQ81aPti8wuOPkp21f65aFu7enxfD1xn0y5SWtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل درخشش گلر کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94857" target="_blank">📅 12:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb99b7cb6.mp4?token=ahi9byZbx30nSWlvsxchWkIPSYEP3VCNehoYuEOOqRri2eOyxB7wx-0mJ0W2NbWCpkx05qRLsXQohyIk6XWrF7jUc_mQ0YnQLDuC8rddtWrk5PbHikUqFsmJNYwtdIy-aWcVzsP00W0PkC8y0xdxv8zhRIg1z66N7TE1DYnjS01ErQzfFeONWjPv80PYexoyXIOjZgkrU1k2MQ0cPEnQzRfRz3OqIjvzqNscIwZILQ_D1jIgdwvJxb9pLqlo5ANYssYLKPJQjqr5t9EomgOGZhpi43Ji54CSVaYRouBsK6JstODkNNafgivaS4m4ACXbnhna9Jh2UJXXquB_H0C6dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb99b7cb6.mp4?token=ahi9byZbx30nSWlvsxchWkIPSYEP3VCNehoYuEOOqRri2eOyxB7wx-0mJ0W2NbWCpkx05qRLsXQohyIk6XWrF7jUc_mQ0YnQLDuC8rddtWrk5PbHikUqFsmJNYwtdIy-aWcVzsP00W0PkC8y0xdxv8zhRIg1z66N7TE1DYnjS01ErQzfFeONWjPv80PYexoyXIOjZgkrU1k2MQ0cPEnQzRfRz3OqIjvzqNscIwZILQ_D1jIgdwvJxb9pLqlo5ANYssYLKPJQjqr5t9EomgOGZhpi43Ji54CSVaYRouBsK6JstODkNNafgivaS4m4ACXbnhna9Jh2UJXXquB_H0C6dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
محرم امسال یعنی قراره کشته بدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94856" target="_blank">📅 12:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed1dbfcf2.mp4?token=IfuLC-Zdmr-cflcNSnDIOAX16gwd38tTfSKXdagIHInRYpvHrnoCgdZ2lmxViUylBNGpBlN3eVVrfUZ6Yl0cXSo9OwoWgxIZw_iiE9Q4b-6ede73fdK5jWLwIymlZVBNk1nKx36j9U-8e2R4a5QstUtR6MlIZPaBj90YGyoB-A0umyhve9_9JzFge5_i7RtP8TUTtp8-oljbsP8pWoSlDLwls-eygpuz9X36DRJpnriwJiP2SSwHwab3c7DC_eyvRrGlPfvTye42SwptKqiIia8XJxeJolJPfUSf-uWaeM6dAatWgBFKSwOxfWNcHQMojXhkAuMOxNoznf9jJClzyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed1dbfcf2.mp4?token=IfuLC-Zdmr-cflcNSnDIOAX16gwd38tTfSKXdagIHInRYpvHrnoCgdZ2lmxViUylBNGpBlN3eVVrfUZ6Yl0cXSo9OwoWgxIZw_iiE9Q4b-6ede73fdK5jWLwIymlZVBNk1nKx36j9U-8e2R4a5QstUtR6MlIZPaBj90YGyoB-A0umyhve9_9JzFge5_i7RtP8TUTtp8-oljbsP8pWoSlDLwls-eygpuz9X36DRJpnriwJiP2SSwHwab3c7DC_eyvRrGlPfvTye42SwptKqiIia8XJxeJolJPfUSf-uWaeM6dAatWgBFKSwOxfWNcHQMojXhkAuMOxNoznf9jJClzyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پشیونی فیروز کریمی از حرکت عجیب نژاد پرستی که در دوران مربیگری انجام داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94855" target="_blank">📅 12:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914049796f.mp4?token=t8krQYmmym7wye6aEPegeG5EEy9kMlu228_tx2qAFcwBHnefPF97C7JErkboPyZihCVmSQw0s7JQajdfkRbh-6g80LIlPtGXx8vwtpiys4s8wSYjMjhReBH0HSgjzXfA7Al3cgM9rc_QdtBPpFaASigf8HGkwhU0drNHI4EGGIeZ_StPzX6mU_ohllQomJVzSYcVIZEfR_zcLQmtq48FwzObUPRKRIsrSeKby0hHttXk53Xu1tOzooDpF1GOc2mkbrXOeLvMJAmkKmQCFR7EHY4fbbQkBCD2QRFs4y1dwbYdbQG4ZR5pzp1nuYHLgxGZdMr-ZVuEOd9Hrtta3Q98Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914049796f.mp4?token=t8krQYmmym7wye6aEPegeG5EEy9kMlu228_tx2qAFcwBHnefPF97C7JErkboPyZihCVmSQw0s7JQajdfkRbh-6g80LIlPtGXx8vwtpiys4s8wSYjMjhReBH0HSgjzXfA7Al3cgM9rc_QdtBPpFaASigf8HGkwhU0drNHI4EGGIeZ_StPzX6mU_ohllQomJVzSYcVIZEfR_zcLQmtq48FwzObUPRKRIsrSeKby0hHttXk53Xu1tOzooDpF1GOc2mkbrXOeLvMJAmkKmQCFR7EHY4fbbQkBCD2QRFs4y1dwbYdbQG4ZR5pzp1nuYHLgxGZdMr-ZVuEOd9Hrtta3Q98Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇶🇦
جام‌جهانی رایگان برای تماشاگران قطری...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94854" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43cd2b800.mp4?token=G2BebSu4hvW44sL03gJJKQdg6G202ncodSJ12_2ryAYXYr2cpTwksYojA14UdHR0es_uNIVs--6otn5f_edamf6JHWWUrxekchs9An5-q3T_ufPAFgyRe6-Ed6fNyREiS1YylHIwa3Op39PQ4fq1hxBAQL87NpuvMYO1ZBESTq6PUXTlwXpYy_I_jIh7XEK54XiIT1nlIYrf5dlO4RVsLjNYrFuAwoMhClYDaW9u4aULqq87LzarDxXRFo1q0wNQ43jJd1YZYH3Tf7BlWO9xjKg4UCLf7s2rW8DVXeK7uyRIcBwtfsCz7Jg6MTrxjGIMQ4pzYjCwssXzYxVH7rE2CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43cd2b800.mp4?token=G2BebSu4hvW44sL03gJJKQdg6G202ncodSJ12_2ryAYXYr2cpTwksYojA14UdHR0es_uNIVs--6otn5f_edamf6JHWWUrxekchs9An5-q3T_ufPAFgyRe6-Ed6fNyREiS1YylHIwa3Op39PQ4fq1hxBAQL87NpuvMYO1ZBESTq6PUXTlwXpYy_I_jIh7XEK54XiIT1nlIYrf5dlO4RVsLjNYrFuAwoMhClYDaW9u4aULqq87LzarDxXRFo1q0wNQ43jJd1YZYH3Tf7BlWO9xjKg4UCLf7s2rW8DVXeK7uyRIcBwtfsCz7Jg6MTrxjGIMQ4pzYjCwssXzYxVH7rE2CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
هوادار ایرانی حاضر برای بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94853" target="_blank">📅 11:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔥
جمعیت پشم‌ریزون روز گذشته هلندی‌ها برای تماشای بازی کشورشون مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94852" target="_blank">📅 11:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06e2f5fd73.mp4?token=bVP8AZQK6AywGyGNVX1_-YTF9aUDy6CvLUXUA5D9GKQ4qh_RyylxtnWpMaBaFY8tpZqlowYKZxfHbQKqbRPi-KgfGAP3aCjsEKKKQ12Fwu5Nfr8PzQ2rOpP4nF2c14UpXMxx_dx7NaorgRBCUVO2OUUXX7scscJqjTo9_7cLwyDyKtTo8DrulBZVu66evnE3JNO8DSh43Mr3CWyXlZEhJBH_ZZz66s04mTG6U1U7JCb3iYpVQKhqpvg8MkBGRtKZcMu0y-k1_L2BPMDYXYwQDYHMsNv1lVPmFAlWutrF_FgQBWoDnwkGdSfhKH5pozQSX6ezBH8-NdXCFViEDLrr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06e2f5fd73.mp4?token=bVP8AZQK6AywGyGNVX1_-YTF9aUDy6CvLUXUA5D9GKQ4qh_RyylxtnWpMaBaFY8tpZqlowYKZxfHbQKqbRPi-KgfGAP3aCjsEKKKQ12Fwu5Nfr8PzQ2rOpP4nF2c14UpXMxx_dx7NaorgRBCUVO2OUUXX7scscJqjTo9_7cLwyDyKtTo8DrulBZVu66evnE3JNO8DSh43Mr3CWyXlZEhJBH_ZZz66s04mTG6U1U7JCb3iYpVQKhqpvg8MkBGRtKZcMu0y-k1_L2BPMDYXYwQDYHMsNv1lVPmFAlWutrF_FgQBWoDnwkGdSfhKH5pozQSX6ezBH8-NdXCFViEDLrr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیس‌بک سنگین جواد خیابانی به خداداد عزیزی
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94851" target="_blank">📅 11:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94850">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94850" target="_blank">📅 10:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUKScGV2XLrDceZTVKWmM4JzM6Xi0NWEJNoFuizCc9VsSQ6rLucv4sFgmwuqxTjsK9FR984JxhVIbu_Gf1ve9YrXdOTpz7wiEaAyr7Cy19xhRSgMZQt7ykIbTmwMMvw7tTjrZJqDNqvQFmZ_xeUhke3X_jUqOIwZowNNsMnfwSgEVL9LU2OlnxoPbz0UCHUIYeLT_mt630-EndDwofFADvTFl7Za5CMeGwJ6NsI_zDRbGeaSXHhJ_Jk8v78tdPhh55UJe6cVyYDavbtokKnYF2O7n7rkX71h2zAxzsWyNjaYJlBB_grbqFk6ZoP7lRqSnqAbpnG-_qecRGz9f-5q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
زوج‌هایی با بیشترین فالوور در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94849" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIuKIrpgcqMUFlmEkbC-Y3ADOnQ898duNCNhIUmejx4k-M4hZvGpEsVm9QDd8N7i_xhwXLbjBCusm38HOUGmcV1XTe8uJ-II0lI-a5UZPiurUVoIbW7uVazu502L-wUpK8XCJfuitHy3QUxeRAOwxRZewEHLRcsR1vD0koeeFOZEJMY4xUSDlkhlXxMqtSvPTmzRz2p_u6wEc4EDFl-ZMRa0RrDLVq2PD-YrjdA6XtjcQrkW9lOEZFLs3LEx-GjMNuKyIFzLiN7P-3IXrbrK6nq9Ec6jUzgPBxtN-JXPEglfp3U-L8EuxhPo99S6IpOaJ9rM16slGHbUldBjky9OXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
ژاپن اولین تیم آسیایی تاریخ شد که در یک بازی جام جهانی 4 گل به ثمر رساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94848" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJL-Ya6QJtPohzM1elYHdo-elMr3jNOiNlZa-ED0LvAdJWJGo-rJGc8GHcRjwLbG7tC0IhRRxEj9F0jXYD4YP4hblnAm7Wu_DPv_TUG-HlqngxSKGzOC6FjjDpWKegE8wKnOTdVKK-RZYX1Fuxn0CuYn7PhwohkI5rIE8vR363YDhUY1G8fhCcDGMonEUTzQwbA_LDZJhEPXMaAEyI4hUl2FkJWKsiuE1henBSckOSUiTm1XzZW3KwZ-KPwL6FjKJ4tRd4GUBsYgsruM8OU8s2ZAwfjXHTxxkn2s7CGCuIeO261XgIv2BqsJsjnqOJwJ_GaemsckGGgxIMNhQ2ehOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیشترین دستمزد در بین سرمربیان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94847" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94846">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94846" target="_blank">📅 10:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94845">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94845" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVUvLOtggRG6_OnRXSaRmrrZRDuVPsYd_W0-BAITIcjILYGCSuRmtaNazMXizukDghon1AUPh8Nt-e5IFgQMfoMq0X7ADTwvP-OSb_CZbwjEH8U59tpudF8sl78h98Mwzh16dLmphbyrgkFEw-dq3qVCzi3Er5cPF0l_b6X1Zlz6-UhstDA5RBYML1hpmmMI8SGao641RdQNiUTKyS4gad1k1PxpXOCHdU29dHgCVToVh12wYa97KNs5lEpdgdvHkJpEHwJ3gXLNKxqsDk5BcIINhSZczv0qO0CivgVz_mM9dWDkgqC7rwo8n0EQN3YnNoEraC4bnw024SHhPOeDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام‌جهانی در پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94844" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇹🇳
تیم ملی تونس رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94843" target="_blank">📅 09:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94842">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/94842" target="_blank">📅 09:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94841">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94841" target="_blank">📅 09:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ژاپن چهارمی هم زد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94840" target="_blank">📅 09:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94839" target="_blank">📅 09:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94838">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94838" target="_blank">📅 09:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گللللل ژاپن سومی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94837" target="_blank">📅 08:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY65i1kZU-7n0m54t3o5yzJNhfijt9zARpS7TkxZlyovsvWwjYet2uHvnb0r2T-tqq529XiZ-o6YXWxVdh1vqKyxXZoCkknhdIu1lolyZuX-Zt8WRit19wVJOJS6t8NTDIiCG23E2oPnzLhhIRzUe_4yMl5YT6rGrwiWUL_Pmh90U0l5lYa7NauE4LS0McMtc3s-HdubmT0iZ8Xtaun4HBXuMRMORP9XvcFvfn8B7fakQ0HjdfM5f7rB3FOCwUNdfeT7arbK4kIlfGapS6w2nQm5JFHBv8OqBeYzjVjWYCjIAxCdH7ref9naS0vLIU6V9ObTNhKCl6cAcyF8sEGa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الی روم دروازه بان 37 ساله کوراسائو تو این بازی با 15 سیو نمره 10 گرفت
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94836" target="_blank">📅 08:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پایان نیمه اول
🇯🇵
ژاپن 2 -
🇹🇳
تونس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94835" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از فوتبالی که ژاپن بازی می‌کنه آدم لذت میبره</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94834" target="_blank">📅 08:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94833">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94833" target="_blank">📅 08:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSXWxpSbJNuqjgaYef8AKA06rmTVwgoQg-26dWTWDOh8dGPnjkFGzpvnrhdsz0ChwFvX-_Ba5BrASG6CazNk378lsD5WPnn6XnXIsmxo2QyWcLpZwL1PtOQKE9agiwjZJryE3nUp1pAyD08EOXa477gmIE7--8F1DjPhLgsLHaAyfx4EWqk3RFa1NAfRQbumEsunLx9aB5CgXM0jyRPD4O1Zyx_XTFRVyz3LWahLxRz-ep3ezrSnTRVSIrlnCPFsK5HZI6rENIJUWJk_36VsH9k6WxzyzDSlItyvSk4ARPBPZ9ic5ZovOimjFiektCvQBKljfJ2dU4wTV6XiBuqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صحنه ای که ژاپن میلیمتری به گل دوم نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94832" target="_blank">📅 07:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94831">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94831" target="_blank">📅 07:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ژاپن دقیقه ۴ تقه اولیو زد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94830" target="_blank">📅 07:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇹🇳
🇯🇵
برررریم سراغ آخرین بازی امروز جام‌جهانی بین تونس و ژاپن</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94829" target="_blank">📅 07:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94828">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94828" target="_blank">📅 06:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lgf0P2MXBTIddTlYoERRtQhy2XIemmi_L8qPne2vwdLlEjbBO_jzls9EIVIUj2gDPONbuY8gPTxYden9Cgxg-nQwecQL2rPPkk-Mnv616XFDYXsZw7SKcl89K1GsWe9B8tejT7aq-JT-pvn_-P7C68SJ_OIiHf5lJzW3LaTQVND0T7HbXjB93WJf9gl__dC0jmy4_ALr0Bd28ZZnzraFKYLcbWDFCoE8uvfB0AiTFNNkEZ6x6qoEEXCi_cgvLaMraeyYyyaGTP0KI0XdX08HQVd7Z-YiqkXkLFruNeL9zXaE_6fTyeMHhDDCQof-yYfEblpTzhOzqc9FHQ2qXtUzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇵
ترکیب ژاپن‌مقابل تونس؛ ساعد ۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94827" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bvt2lkd-XA7fuQ4ykozg2KxraGsn5L_pjAGKNp3UIJUT3ABKZxmkeGBFOUr4EbATJB7IJwF4J06uZLiHQxVo_ziy8jNPn3juFusM8zTRw8kGbMGAm1XTNC6o6WoiYLLvxxTnG49qp6vVbGpFWMzzm1siJWMg_9O6kJt1NFbjK1j92kAKdduf2nZROh6VoYQXXTsGEnHvJ4M9hk7oXwSMzZpsq3Of0Wlt2N9Kwdsx4knl6extFuiAdd_PbaemfvJTFIPwzxU1EKiWU9ByIicmiKoVR0ZLrPmsGCyl5C6anzJ8BIvEL3lk-8y3-i55xpp42WkRUFV_sUevqFgo8GtJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇳
ترکیب‌تیم‌ملی تونس مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94826" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzcpvDLFVteFG_OyEwja1SSiKN-Rij7tyNJSR7Bt2Lkq_szTmNLSs2gzHoo7Wyh2NCs3m3wxEIUQcv924ESUicWMSffI6O9lzsmg--PKlH_gsf1mgtA7RKpK3mQpXnN1jeV97Fbov3CO4RXzZ6i4FYIisNnpEY0wE976-uDFS0Xcifqz2qIh7tSNSVSvUqayv_RPvaODnvVoqGCNlgr44qIqqWTNCn2boQ4-5MSHybHgTcQlM4Bbax0nnNzRvSQm9YlbxnQFnW4zvtgWuC3uysW5Nag5i4yMfHa1avv5vKyBpUgSuMeo2Ayd-o0n0RVg-WpDEOaVUEJCDkDLcnK3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
کم‌جمعیت‌ترین کشورهای جهان که در جام جهانی امتیاز کسب کرده‌اند:
‏کوراسائو (۱۹۳ هزار نفر) مقابل اکوادور در سال ۲۰۲۶.
‏ایسلند (۳۳۰ هزار نفر) مقابل آرژانتین در سال ۲۰۱۸.
‏کیپ ورد (۴۹۰ هزار نفر) مقابل اسپانیا در سال ۲۰۲۶.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94825" target="_blank">📅 05:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHtRsiwMLj18sOsnWg6prsFHQi3KsgHAEfaZA7XbMTw0e9kuV6alMvpudKZ9Q1zGmO8yLshPjnb9dbaDYgzr1cwlZR_T5DttpYh0tcMfQn50Tax7-tON0tV-LqtTtQj73HWx3ZJSHZEbkfFDa03a5k-NB_GXJK_BTbybykaDnbpLkyYVgWnnTwnVIdSKGsoOXuRHQBpT94rdLu_-Jfcn38uaatEcls4fdYWgMyCYJOYMkcNhDa1K281yE9LANiQhEPay9KhA2hyzXkkUWjoWJwgaQvoY-lqw9L_xSLQlJ2JllL5VmxcS6-Nei1Lj_FtDmO660U_pPC0t9cVu9URZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EB2X7HJXmmPstN0C5SwgF3PcLGNOOD5uXasp4xgfNf5o9LZQDsnWcG4HdA20dFeYFeAcZdeXAHCb7RbhUhuDfJh3BcvuE6XlsLnpQsdj6KaRgQf2MTHp2h8wgDLWBa1FCsMJboL0wxYRkIjYCk0WzQzivV1QOQTjPSWf3sOGjipUQEYgaxAHAcauo1JhP3dcnCAhSwKa4yvUBGkCdtQFZ-prUtIDz-UPBcqYxHWIcIpHrc3JuyRlJ217aeIpchyQ2IbcotFjAG34x9pHWibBJlqGcyBJfZxCgDcTGqq-qEECWKl92_pPzvPOF00lymZtjqKYFeXfYsrR8PTj8-7HWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در عرض چند دقیقه 300 هزار فالوور به پیج اینستاگرام دروازبان کوراسائو اضافه شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94823" target="_blank">📅 05:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9LojSjxuD1gfoZDtv-PdLjlUjYQcBtZibtSVMnZXu7aZyyMA6lQlX56RiiZTyq9shxui5ZDFZAf-j7UkPnKOcAQYFRRvyIWcGY2wdTFyxtm7gF0idgO5LIjYAxM646TWDqCNQvWJgfU7zaLeLJdKuVlTHkr3IZG3cr8RsRMAxYQ6XbaPHyjFIENRlFqjRBQBz2vPZe0fGa8a_1nJVHf6OHmpPtL713cLMg6FQYNdKRmTRzqL7riGlyS1OEhdWuwGLR3dTNJLrCymswEraP07_UCPYpbMnVt20V7lLZv0r1g15obit1PnAHxEabR6dPreltYNVB2M8YIeJ2CQY5DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همچنان شگفتی‌های جام جهانی ادامه داره..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94822" target="_blank">📅 05:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lII8kPWu78rFmboqs4W8_8n1lsYM8qMI8DMaYablmmq91JJe_ahgikgpjFXbVTDKueTIpAygfRvkYRp76MAv6AjuTvAcGb8bDFfLDkoFRc5Vv_-w6gL3a2CWCcCyYLW6y31McMGuEEmGDV07IpJbWfT44ORHertIfXtDJoAnvItI0z1-SNCcFVdKDa9mL68URCmJhPEg0NxZddFEjoV8iuNV8egmB-IT7daPPozwvRn6ncBMdfwqQsV4flvwcdFU2d3DsSgY6_kPMZejyPZN9RdSz1eBQ_XAN9oWfL3YE9cMNuHbI6BjTOwreBCEJaKPszmUKzto0MBOQegJreIgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94821" target="_blank">📅 05:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gehljW6-rEfq2uMzWBXDzoyZMztrooqP7wfcR1avFzLREUnMNab1SOQ8t8aFYer2cCF89hX9TZvSwR85-bHFdz5dUk8vW-wXhaH5LVkEdzwcvhE4FMKhfzz6lGTaPxuZMx3BoAYmN4KdWKYXCDfsKtyouft70ALyV0YMiDAbJYJ5LczQ9fdNm5FnNb8dCdZ4tAGoN0gX-TRk3sELVpCLw6clvKSD_j_C6o1BwBnFJcNP9inRVaScZZZuiOJay5W-bSOUaoorUQw7XUQhYk1hocPOP3Q9tlXEax2x_ym5Uh9XNApyExHAf1zdkB_o2mj4JyruwI6rXXhS5NGyko63QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه E مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94820" target="_blank">📅 05:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94819">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94819" target="_blank">📅 05:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94818">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPJLVtgMiE6seC4A6nFKuCeAns0xALJGMs4nUh_ONtDcj6pSdFJ12GclvJhlN8C8xHzLcsH96QxzjbxCHuuGCVNCEYPu4XzabqjMVpBfvzkhXWXhkivLcbWBnuTf8j8BlbNeGf5AyL6OIRbkwQSvyQsJWNjVSvobpQjhLEkPUopfmW71V-ULBjbtS1Zu39NHFNDBX_ZZVYkeasOYSFXMNP7bOyg1XJHbDGBQIZQV9M0TjvFBPgFrurTW5zM_Lj1j_G9Sicur1fpLCAYz29EJGk6JwUioxGYD46ukypuNxBPMMBY2IQ-ssaQgPvFEtHSrlrPw6ibGikkneItbO3WwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94818" target="_blank">📅 05:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94817">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS0EzlH26O5qfU_bsGXZeXcHIMsy-XwjmLYspafGw3r-oGEViwgP5yYFMVPFzWcPHmN6KCoh90FzOmSbWL2oTTmZDNym5kZbjGKwwKCzo-J3RzCpodNAsuN9UsI4n8O_4kNs2D3xIpfJuy_BiSaOYukENHSmUiUKFrUszciDqV_piHg15H8cTYWtk-ix_5ugSBsIWZ5KaiEAmGi7Gq1XHho7vWfDxmr5u_Qzjevq4iCqKZVxxv2iep4xGn0bI514rGlEEuijbZjidlK2BMF01QeSOOIUSWMYIhuKIjc-9ftqnqUcTir7pxuuVppIdXeTeCzZ4Rz6uJVjs0NxxjUFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇹🇳
استادیوم محل برگزاری بازی ژاپن - تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94817" target="_blank">📅 04:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfQbZoAKbv6UV2KW2WZfhVVzx1sB4DUhEFA9cWzzKWa9Zyu2sx68zJwT1j4IzGnrMzkdn48xL98Pk1BQtZxHsXDgfs2d6UVTOTTuYysAUi1tWnI-mC-_0YTndRDs-t-W3QwBSXKxwqeqmVeivK0MO-cgVwoq4UzwglmvA_sIJ9T7loM6Ar-VxBWUK_6gNXh30Ds2fxs8VeWHaAtD5ujqDkiTk3cUHIHMDg7FdRwolzcM1af70uyhQvE2aGOYzDJP3LkCRT1T_kyHkJ_GyE1CTyG2LJJOf-HidJB-sN4lYTzw_M3ADSDxEKaXu4CINLd6yJs2QQ5cQKwkf3KyC3s36w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94816" target="_blank">📅 04:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیمه دوم بازی کوراسائو و اکوادور شروع شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94815" target="_blank">📅 04:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=E3W2lgYcJTDdNmiP3kcupk1eW7TWEmbiLRMz8nOtnbR50ZREbJPkMOiPR4bczUbx-ZKTbczeRM2cFvdZyqAo5I08VgDxhyu2XVNPuWPRwTmCJKjNPPh8qLTQi6vDFEEdgu00ZODyPeNt6pbPSa4rbXScm0eyB-kW2vcjdXrT9wQ3kGGyCeY9zfISmigMbzoUpJbPhdxiduMFW-0Kg2FtBCyDBPi7dZc7vFq7RebNQdvXbaxRpk6TXIRm9cfo1rqjDOavWqH69GkoFxp6KrPqEVsJNBaxDMWI76X9ns1BtpLt7GBfmdYfvFwEbpHEhYgQA1NvjeJ3D8wJ9dkRAcJg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=E3W2lgYcJTDdNmiP3kcupk1eW7TWEmbiLRMz8nOtnbR50ZREbJPkMOiPR4bczUbx-ZKTbczeRM2cFvdZyqAo5I08VgDxhyu2XVNPuWPRwTmCJKjNPPh8qLTQi6vDFEEdgu00ZODyPeNt6pbPSa4rbXScm0eyB-kW2vcjdXrT9wQ3kGGyCeY9zfISmigMbzoUpJbPhdxiduMFW-0Kg2FtBCyDBPi7dZc7vFq7RebNQdvXbaxRpk6TXIRm9cfo1rqjDOavWqH69GkoFxp6KrPqEVsJNBaxDMWI76X9ns1BtpLt7GBfmdYfvFwEbpHEhYgQA1NvjeJ3D8wJ9dkRAcJg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کابوس کوین دیبروینه شب قبل از بازی با ایران
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94814" target="_blank">📅 04:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینقدر بازی جذاب بود نفهمیدیم کی نیمه اولش تموم شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94813" target="_blank">📅 04:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=BUGa8gGLtuZkI-UuOlUlixGdwSMcW0_GWHexGS6WcpGEqbhW-9MOX7jnyQs76TzgSjeTvMb2KJv-c_mj5TpmFBBjnUmlUG4SDo_EVvY9yA5I7g4dYW1hpXMYHrvUh5NVQMRWBBW24s8Yy3nXIDnhFVYLBFMvw7KuVnIOziYAvmHda45dTj_8BGZUDWEqNf-KdE5FHuWimT6dqocCUuVyuHB3qiGDdGTYG_1XwJFtiWvVaiwVibZ87b9XEnNgHsx3upQfQlkyFnNB4rqo6QMjWn6SHrggtZWVwzSO6qq8v8Q-wRkFfV1FQbt99Q1UeJhK8mO50DhDwqI76I18RmlKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=BUGa8gGLtuZkI-UuOlUlixGdwSMcW0_GWHexGS6WcpGEqbhW-9MOX7jnyQs76TzgSjeTvMb2KJv-c_mj5TpmFBBjnUmlUG4SDo_EVvY9yA5I7g4dYW1hpXMYHrvUh5NVQMRWBBW24s8Yy3nXIDnhFVYLBFMvw7KuVnIOziYAvmHda45dTj_8BGZUDWEqNf-KdE5FHuWimT6dqocCUuVyuHB3qiGDdGTYG_1XwJFtiWvVaiwVibZ87b9XEnNgHsx3upQfQlkyFnNB4rqo6QMjWn6SHrggtZWVwzSO6qq8v8Q-wRkFfV1FQbt99Q1UeJhK8mO50DhDwqI76I18RmlKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیگو دالوت در حمایت از رونالدو: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94812" target="_blank">📅 03:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHT7PP4PUznUxTl-_ZTpEYeYMILuFmihm4qnWpnZKfYEtfeqWNBWZQsgTGhVviNUcX41Gwxwt5q9O90Wc_YjIJ3Ip3WWWE-7JpT_xY3wBD-mmuG_fWNqjJjm2f19xL1r9SZtZyqsidRQa6fvs5SMhOeWSzBOtIbqQdU11OqxZ_srzp5x2SDA0o5r41XwJAmO-WwPUSfloNfltpEtVpHCQBdlKw5OGH1hZ-ggLIaxSoE9-3BqfXTlgAkG5xEc8VDbrlJFsPqkUb6fmKNo7DwXwNAhdNDQiVSIqau7jEJmgwYDopd1pSJbiV38IRswfjwq5YaSlp2Aq0wOMz83lnDz3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رفیقتون بازم اومده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94811" target="_blank">📅 03:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJWk8MhvX_2hR0Yn8s_yoBDV7C7I4eiLj0YyVZTY9XGaxdjyvr1WrhwqSXjttpF0b_NdXkdoe-CrBYy9w0JKgG-WWLSd_sxVeHM6MC1JPGm925x8A28TltQFHU7KyBt5SMz7CAHykWC1Nc2lcHLDJ6AW1EnFhXm10nT4Zog2DYBZAB0RFuPXs-M8CZl_POTTMFR-ypSgyhMdxHiumV-Qw2TdpzW29DBXJmWTLEAAOYeHkGs1hjFLw3lsm25WV_gaVu1Yp1TF5RurGCdbg-saM__2FhGOeqNHy8NQEIKzS338LOcw9oySpY7B1DbKIM_Li1BnHE0Ojlf9JkPiU7cn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94810" target="_blank">📅 03:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ7rUzozBrvix-GSrwqvwTzNFtZM8m7SC9Ipiq1nLq50gs07hO731fxCjSpdG5-bj8XIO4H5tX_Y1qkUy_zkPQo0ZaR4GnL_v-Yf3iuIepjC-lgsABeAF0qoT4FKUhAfyt0rJAVpCNtJnyfqb3328hi10ZPscDlBKl2iTThhMJoxPI9raleAFnaDi2yU4tizCndFvTdDqvwSioH6FrCvi1gtTSL3iMvcyZcp4sqAQgFU5VCSmepSKxk2vTejOXhSw44f9noYv_gM49lR3cm_BNIZez3d6CWhuLSlCEpYeY8vk-dTyHrgtQglYQmIrl3iqIQDMOxJzve2z6eBIogO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اردوی پاور لیفتینگ بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94809" target="_blank">📅 02:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=UYP94FC0-zxTdJCmni--inwsA7wTIJa5cNdoR88hYtOhpLDPo1jMa3Ji1wB3SznW593gsImTe-mSuWvhNO89Smq0hsau3VoY7vfJq91M-1y704SeC1QvRyAyjx5FQZoOt_yluHk9_L1juD0w-xvzL4Dsjo5tvhnyfSdl9yKf4Kq9h60WiFTfGFsm8w4pjZt2j-7mxL47VrmYpcEYOKkJ5iCFbdEPipj6Ak5IBXdjj3mBzXilGDK-f6XI8fRCvpdpF_ujfmagMP-F3xBegW75j5jDLp35uL-_zLEgyIeJpvReUY6eoJpaCjh4j0VFzqMf6romPzE3Q_j1NY1U7RAbEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=UYP94FC0-zxTdJCmni--inwsA7wTIJa5cNdoR88hYtOhpLDPo1jMa3Ji1wB3SznW593gsImTe-mSuWvhNO89Smq0hsau3VoY7vfJq91M-1y704SeC1QvRyAyjx5FQZoOt_yluHk9_L1juD0w-xvzL4Dsjo5tvhnyfSdl9yKf4Kq9h60WiFTfGFsm8w4pjZt2j-7mxL47VrmYpcEYOKkJ5iCFbdEPipj6Ak5IBXdjj3mBzXilGDK-f6XI8fRCvpdpF_ujfmagMP-F3xBegW75j5jDLp35uL-_zLEgyIeJpvReUY6eoJpaCjh4j0VFzqMf6romPzE3Q_j1NY1U7RAbEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت تمرینات و سطح تفکر اعضای کره‌جوبی و ترکیه در جام‌جهانی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94808" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-pCOX99CY6b9737dYHix8Og5rG52PDmUOSv3kK9NIQuYGEprD2btCPOdUhBllOzaqkkUujEe4fjZ1tt0fAdFUKQwJZhJV0DMPM6_BP2yK5hCDWNjSQ5xyvIv8ine_HlYCyY5TVMWCqTE-oA9sGWKZJEnFTk9cU_1JdjGWz3rVeDXArS9XENzuXFASTsdOUmi2Dmu91-1Ii7SoRO2ykdS_6sJezaTDLMyg_Et9me3kme3BV81Eq4dgzWrK6GP1jsnHD3714i2jLYtW1P6qDz7Q9yNa8EYhs1Qvg3avh2uL9Z0JqsMjn0Habz26K73YrExeTV_UQ5r1Z0Brax739Y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 2 دوره اخیر جام جهانی هیچ بازیکنی به اندازه دومفریز پاس‌گل نداده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94807" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94806" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94805">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ci44kcM3mxDwYvdjxg_Ie4fZsAhVTxm4gaqtNN7L6p68ewI80rut06iVVHLw0FKTzw15ueFSBCD3xZSbdlg6ZoLF3jTPna7tfqt3amkZZB7aH4nVA2_pBZRUOSCvAbqVUKGygyPQt9AoOnODEA6oUe-S1oZ2dEJUX7EChjX44Zna7e-IhHFBXraMpl_OpdHGlQbHx--kLqrxbFhGYz-g31CIuvZ4M1IhV4rvJXiGIBbUsbFPxHTmCov3huK4XoD9hvzPAnXeOnfMkZHRGLljTRWoSo8_kZCoakUpxnfuZGqIN1SyAkQ4dBnehIwDslyR5z3WkwOrxbimZzkMyqwOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94805" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duv4tHaMvqkeDaihMI9SfeCtf74Ec8oTEkWj1EkkvFIVDlB4gCk552eAVdk4ffOi8hpDIduuqZsbcQjZCbiM3jnq3XClM9XaRCszcmw71DRiksCMio-DT4YZFjO7bpIEs7oK2mKM6cOJwyCCIgrozjIG_CibUgFtrfSc0IM9A6R1NnNQHZGGCqY65Grk8LzktOBKpOke5w686QFvU8tGDT3CvLdEcRzD2ND7RbqIU2usmfoopks62YIxcHatIof7VJ2kJD6O_PPCrUJ5e4VJK4GGxtnKbEfl0b4dIviWT_UxUL8-jP16vWtSTvLiAJ9VsPM3z249c7ESI7nMh_d1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1X8CCMkpdN4x00V_5LnPUfh6L8UXg_trEyD9692qKjGZ8c1sw2NhBqeyNxBKepevS_3OhxFhpH31_mG5Y7U4XWzT208f97MzwPA2M6ldP-GWWcYcopsLuMRX1faW5bOr-RNQyKN3Ia6synUrR9Mq2aHKvvsTNVnx9YDLfQPQZKwQFABOpklQD3Ja3bkKdKFYYGAnllRY0j-HKffkJEmiKnBA2Lw2JNtoFowFLjCYNG-fHN7W0oAhfXMWGcQluXQEwQL4DlpXjEIW_LosNT7YPNvNR7Fdppjbb63ax7LCSrEliCzws5OqtVg_5ezRTj8b2UnY5O53AgbIq_6-5eglg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇼
🇪🇨
ترکیب کوراسائو و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94803" target="_blank">📅 02:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
ناگلزمن: به نظر می‌رسد اشلوتربرگ از رباط زانو آسیب دیده است. اوضاع خوب به نظر نمیرسد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94802" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_bTROUeSRlukH7_hdK_FGmsrB5nyvI5D7Bfu85Y0LnTaAUgUvf_fKo-hx-Q40CzccK2tlSfGREvttrRYU7KKVB94EjocgVNjvcoxXkuyRrAIIs6qclm_iARl7CsI5a7JYFnIglBOZUue_52i9zlIUKtjSvSzekBaNtmg1pp6i_UgZavJ8ux0Q4eqP2iHV-Emf7aATY8151EcsuY8L1CZCuPPFB2FbjdDaEJxykvxR0ZR5TuDUVaSQG3qTmojs0MWTfxLx9uUmOpZsmQTeB-801wuL5LPBggamGqmBFkRP-q2NSzjmVB4-9XmJDHBehtgLhsDgsECbOztbBWlWX22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار پس از جام جهانی 2006 دو بازی اول خود در جام جهانی را برد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/94801" target="_blank">📅 01:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIwUbnAGhc9014cWGIlBWTnm9IJhDZq5MSF8oxzUMP0ovYOMoBK74_8AhqHKc4ZSsi8y-TJi9wS655HQ3E4R3pPS2B4m_UQqImYMIrhK5FKvTPIHr2XWtRwUomw0kH-wD961_sEIcLnQYJQs2A4HtT8pSEGWSd-AJG1LjxCqPC8QPoxzWWYOhqrwwQroPab1ARCkca_I6GkO-PRTcKIUnrHJ1GtiTvVQ320fOd2buMEqTH5p-1GrtuafZQKhqjExKL2WsRDPChfAn1_VkPJJdB2J_-E9o-gFoC9bGh5WgblCfZ6ACkDFR7yxs5WgxAILoCejd6THfmTKRBIJprHBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/94800" target="_blank">📅 01:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTilpLtGP9TdCqS38SeyqSmupBMeaiNwSimxCDicIoc5K43aKo93DL8getWFSWDjcD1h6P0bMiaQ6CMmCl7WicxLgH5V-g59gV78d6ROc8lf0qY-mStcuJf7AFSP48NMZgJOOKl7E3d9Pcg7-NULKOorLj-maY_T51dztoRBsk0DoTlLnb1JdbUemuuENUqlg3n7R_FIlvUcE5Rt9Cf6je0GbO_KzBIr_AzRb4BT5Wkk8ge3nBMidZecgzJUDORzVhOjEuFfBFCT8cbs3H4CXs94auL_ngkqj0oSXXGUpMq4nL_ix9ymsGMXOmTj7qcAvPs-1HsbE2CAK268fDxctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آلمان به عنوان سومین تیم به دور حذفی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/94799" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APro4G4Bz_oeeyx5knQ09gEdwwxAUZe3V7DOd2LwG3ODQOQ__wnHjxIHsOphd-gJyfq_5xwRdQb5uXfiIwd09a5bfWKNEDOcXrGTzxKYIBx6jDm-Pa4vtaBgUrgd7IIF9UdLBOiB-aJXmRx-_ChZkLxTyh0iBuLpstg36Fy-W4DcOAFFZ5nMstUbNZith8EdUcfOTuKa3k4nKq4C_yWllccUHlmOOgkHy9V-PgtnFCQzyGv-zQvHMJFU3i3i4f7yaa30MiYUjcevKargBjTSYEhRlRlqkNlUZgMPRyrgqfJuGeR-5YTFaTSDJGRhVczhQrINVDyQK5KPoidzLVDgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک شاگردان ناگلزمن تکمیل شد
🇩🇪
آلمان 2 -
🇨🇮
ساحل عاج 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/94798" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زندگی سخت شده بچه ها   میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه  میبندم روی برد برزیل مقابل مراکش میرینه  میبندم روی برد پرتگال نوس و رونالدو میرینن توش  میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94797" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=np9fEX5sUou2tycTCGVPfnENnnclE2_lFmDucTwVhFFUVKdywipJXL4RdX9xUeOuzaeQe9GSiUPQ5I2rzJT4B6nS20APDK6GwM394FFzyybJKlt700aG1KFLw9FhlRZk3bE7WtceQFtcT7p1KjlodKq9vu-o9DMeaeqAzNSfSK_gyNcDP4w1PAyqx5D57rDazvC52xO2j3dLp2sBQyWl0AvxMlRVMCwPvi8kwz7pT4h5NhsDAqBehb1vYYWcAMJ17eZ588mZH1QmNNvEecHE_xo43Idw-aWsfXluusNuk2x60SC_lLPLRYyE6Rlo6j0FL4xjqlTgSYRrC4mQGK2H1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=np9fEX5sUou2tycTCGVPfnENnnclE2_lFmDucTwVhFFUVKdywipJXL4RdX9xUeOuzaeQe9GSiUPQ5I2rzJT4B6nS20APDK6GwM394FFzyybJKlt700aG1KFLw9FhlRZk3bE7WtceQFtcT7p1KjlodKq9vu-o9DMeaeqAzNSfSK_gyNcDP4w1PAyqx5D57rDazvC52xO2j3dLp2sBQyWl0AvxMlRVMCwPvi8kwz7pT4h5NhsDAqBehb1vYYWcAMJ17eZ588mZH1QmNNvEecHE_xo43Idw-aWsfXluusNuk2x60SC_lLPLRYyE6Rlo6j0FL4xjqlTgSYRrC4mQGK2H1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/94796" target="_blank">📅 01:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چه دقیقه‌ ای</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94795" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آلمان دومی رو زددددد</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/94794" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/94793" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آلمان چه توپی رو از دست داد</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/94792" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این وسط هم آلمریا تیم
رونالدو
به مالاگا باخت و مالاگا موفق شد  بعد ۸سال به لالیگا برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/94791" target="_blank">📅 01:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d006b86423.mp4?token=jAZU1MWvU1jEfojqQo3G3LlUb8BiyAeyIaNSn3z4BH61bFavqXGacK4YkwkT6PfHJ39rws_pd6vsm4yQSCEqgpgchDU3OeBVB1yzqQJSItUXhqMbfdLlI4FYffFXRSkBK2M1eJUFQ6hyV8FVx4fzeTwklAF1-mY6rfed6u0UmCGjD8yuWIz5Awe8YVsxezlOmmg-exMiuBEdwa__koewc2eGHrBMo7fN1zULueEdU2QtjwHSU8pAnyHU-UeTXwmxM8-vgPAQT_El70pg4cwEOw_oNyuHnYGV2qoNhnK6DQw2kT0VuXRgGrcvIXh_cbp1Py48nScpvI9yl9-TsIz0u4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d006b86423.mp4?token=jAZU1MWvU1jEfojqQo3G3LlUb8BiyAeyIaNSn3z4BH61bFavqXGacK4YkwkT6PfHJ39rws_pd6vsm4yQSCEqgpgchDU3OeBVB1yzqQJSItUXhqMbfdLlI4FYffFXRSkBK2M1eJUFQ6hyV8FVx4fzeTwklAF1-mY6rfed6u0UmCGjD8yuWIz5Awe8YVsxezlOmmg-exMiuBEdwa__koewc2eGHrBMo7fN1zULueEdU2QtjwHSU8pAnyHU-UeTXwmxM8-vgPAQT_El70pg4cwEOw_oNyuHnYGV2qoNhnK6DQw2kT0VuXRgGrcvIXh_cbp1Py48nScpvI9yl9-TsIz0u4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/94790" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آلمان گل مساویو زد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/94789" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94788" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUkn4WZKWGXiZQMKjPk1d58QekgXel74ZFQY56xWwXQitRtkKtxVGNuKiYz6flzhOG2HKSY-1FSAqfQnMNKLHSqDaAhx0CtOb1DHtKudzMfIiWZ-bkkmMu5jL4qyzsnv2294yrJcfQm-G9gl9ZAETGC5l8vtky7clP_LRfpuWphnlWewvW1wg_eMGLbi7JmQ4mRQDYllQML4P5YtftGlcA6k2IACvAGl-LzkAsjUWwx36t8Uy-5uqWGF7Tt4eVac7wr8ZRvDyPxJYhheA0Wd6zdrfEXxwDXA4nMgPnYPCU5kmzmOnxAuHK5Z2DfhylVEB27fFtDIqHmYcx_j95mpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلژیک بترس که اعضای تیم ملی آنالیزت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/94787" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زندگی سخت شده بچه ها
میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه
میبندم روی برد برزیل مقابل مراکش میرینه
میبندم روی برد پرتگال نوس و رونالدو میرینن توش
میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/94786" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
