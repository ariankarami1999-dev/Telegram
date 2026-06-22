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
<img src="https://cdn4.telesco.pe/file/YnI1fTW4z5c5QNLGHFqp9BeD09X5cYMdChU-u8kGkF_ySypkIzktTofg2CpyD3YnsSb2co5-0vTsKbwbsEpDI3woqn9aWxjOD4UuukBT_Q3R3INCCgirxjTft7v8VjjKyHQsSAUNuAWh1al5u_sCkAWSu4hvpkSSX_evdlPxhKp3ij8APVt40rDBVpUz4-0BLShXHw1PizBDm9T3wWS1RNfHVY541ENF6xC4gHesWzlcLjyC4BYkFeL9Vp7UZWaCk0gWmSTpJPpkpQ_wg_OOWQoSbVGXpuzt_DOgkgszmQvEasevivi1lAVP6lAphOfIGo-2wlO_FzbuXXVtrdFYlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 05:15:07</div>
<hr>

<div class="tg-post" id="msg-15562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpIzPy5zoOru1u3mA973T2dIkhOoo-qIi4SUtyqJoVM6n2-L1-6dVJ3ntPwcSHNDQnP9rZk4bNNxFRXxXG_-6HTero2rxKDp1NrkBMbYJRW418iT4wgRBVLaDqioQ5T3F3fpsknL34sjQPjWhbRn7CQfH1ZdypspKQdZ6jxgX22gQG6bTVnm-2tGdXQFt8-NKMyq8hnu-Sfcq_t9KzIck3p0bZFn3l0plvoktk2p-pEIYgG_EgLrVfJQPTDr3ueaHCNADo5zOOZRtcLtZ-lMQzx8WT95c5JQ3IDQ8cH3Vk6UxXeTY59QcYTkERUBoVGDs_ptrhacdB8HyQ0F33ta0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه پوشش اخبار نیویورک‌تایمزِ فاسد و در حال فروپاشی درباره ایرانِ بسیار آسیب‌خورده و فلج‌شده، از طریق «حقایق» جعلی و ساختگی، به باور من «جنایت علیه کشور» است. من تمام گزارش‌های کذب و بی‌معنی آن‌ها را به شکایت چند میلیارد دلاری خودم علیه آن‌ها اضافه خواهم کرد. آن‌ها مجرم هستند! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/withyashar/15562" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗮𝗯𝗼𝗹𝗳𝗮𝘇𝗹</strong></div>
<div class="tg-text">درود عمو یاشار یه سوال ناراحت کننده و کلی داشتم چرا انقدر کشور ما خیانت کار زیاد داشته تو کل تاریخش</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/15561" target="_blank">📅 01:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=nDjI8Km1goItnqlTB1RNuT7z5t0s-B608Uq3EmvmiTTu2pz35KEXwKWt-OQU1Bbk71Jcu7AjM8SzQU-ksFU-Jv3ScN-xZdGx2AtLTNamgUV0NDxpXwuPN3ZUTaVobvnz-SsurGcN88TvP0HotoU-fO8kT5YV1g6Haa8EF326mvUZ4TDapWaYhY9HgSJJiOw9ZVllvUZjZg8LGWDzZmanKkmKv0sokyZHCLsEnS0RDhSp_HSmXWAonZjotC-TKOFg3oEn2dNfzinWac94sB85OM_IhN641XDL9NtPi0FoxISdrfTkCNOWBI7bNyndcNCsmb5Di_JyPf8gNaMc2H7elg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=nDjI8Km1goItnqlTB1RNuT7z5t0s-B608Uq3EmvmiTTu2pz35KEXwKWt-OQU1Bbk71Jcu7AjM8SzQU-ksFU-Jv3ScN-xZdGx2AtLTNamgUV0NDxpXwuPN3ZUTaVobvnz-SsurGcN88TvP0HotoU-fO8kT5YV1g6Haa8EF326mvUZ4TDapWaYhY9HgSJJiOw9ZVllvUZjZg8LGWDzZmanKkmKv0sokyZHCLsEnS0RDhSp_HSmXWAonZjotC-TKOFg3oEn2dNfzinWac94sB85OM_IhN641XDL9NtPi0FoxISdrfTkCNOWBI7bNyndcNCsmb5Di_JyPf8gNaMc2H7elg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه مشخصه من چی بگم !
🍑
@withyashar</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/15560" target="_blank">📅 01:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4Iq7-hWIPXV8HfpxAw47Wx2-4g_j5B4IQ6zILg3QnUWZk9JF5w4yppwR_avRZIn68vYb0tPd8NRlqrUUl0NQ7soSgpJJ7TI0M8DSC2XJOPCREQocxaV6WKPq17x3FJ8AhS7bY8sSdbMoHe56A28FgrLjs2Mjx4Z2edgk22ylzN6oFocXdnjvscSrs7VKIYR8Nq3e8Tmc3L0mudndcEkZ0HxX1WPGYasoNgqkSvhY2gw7FZ4T2usLKkFYU_pxGBfAbbKLwqzrmTYfuJGYfN-Rjnjv8WB1lO6EpekBxypmKTEA4leflrwU-QxT0my8GOOzBlf4eur64qkllvxNljnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زلاتان پرسیدن نظرت راجع به بازی ایران و بلژیک چیه؟ گفت:
نیمه اول نزدیک بود بخوابم
نیمه دوم واقعاً خوابیدم
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/15559" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خب مجوز عبور کشتی های بلژیک صادر شد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15558" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پایان بازی و مساوی در‌جام جهانی مساوی ها
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15557" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk9Q6tv20zh8_4p7oizwXN6C3moqC6CiA872FUQ_P3hFhH9lPDZ5vYwPziFyArrhwmrdKGzqRWn4Ls0tUeOrbv20Qnw3uD6Xy0Mu_V7OiZpWT6fFebyZ8A8ssgCl4s7-ghpOtvwvSPeIRI-TUewxK2Jecv6WsjJZZYxNjCXWKvQMb4fBNOI-eq1P9JuiwQuTcl8ykULtL1C8uvzZm-zGb2iYqONfFnGXRh_qWb7J9d1l6jVb9RMtUQFBb9DElvMPihcZ675gWoETorULhvayoJOYqIYu33O88APHqekTNFnNW-gKfj76f-T3l9B5Ib15w2YumP2rxk6p0j9iP6Tiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عنوان خبرها در نیویورک‌تایمزِ فاسد و در حال فروپاشی: «پس از تقریباً ۴ ماه جنگ چه چیزی تغییر کرد؟ تحلیلگران می‌گویند تقریباً هیچ.» واقعاً؟ نیروی نظامی آن‌ها نابود شده، نیروی دریایی آن‌ها از بین رفته، نیروی هوایی آن‌ها نابود شده، پلتفرم‌های پرتاب، موشک‌ها، پهپادها و تولید همین‌ها، تقریباً کاملاً از بین رفته‌اند، دو گروه برتر از رهبران آن‌ها از بین رفته‌اند، تورم آن‌ها به ۲۵۰٪ رسیده، اقتصاد آن‌ها شکسته شده، سربازان آن‌ها مزد خود را دریافت نمی‌کنند، تنگه هرمز باز است، نفت به شدت در جریان است، و بازار سهام و اشتغال آمریکا در اوج رکورد قرار دارد. این چیزی است که تغییر کرده، شما سگ‌های فاسد و غیراخلاقی، و بیشتر از این هم!!!
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15556" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آکسیوس از قول یک دیپلمات آمریکایی:
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15555" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بلژیک
❌
موزامبیک
✅
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15554" target="_blank">📅 00:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یکی از بازیکنان بلژیک کارت قرمز گرفت درنتیجه باید ده نفره بازی را ادامه بدهند
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15553" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=QWhxjaflP3gyDSTf4f56bVyWPkRBNLt3dC5mzpBhEJgdmN-i5LU9p3PadorbhWQgH7tErb-j6WKm43DFOJ37m2wQt78pm2nF2qzLoy8M7JqsawE42quhhsKsc9xMOzIp5FIVg_NUSe9aidTYzAuNLcy4QtI3f5pSLYimZdpZ7uX8phSAgsIm6F5Cb3PipjnjUPU-ZxJgyQoSUtOIVboNTwlHysVFu55zRKkdZ99veK9lvo4lQmNv1wDJ7Jp-DoeJ-aKPGOC2T8lGjYl1sX-PAoxmkla-5s6utPvuWKqYirlAmFuO8DaTzbUUef0u8h_MHigkIZiT908crO4pHbPOmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=QWhxjaflP3gyDSTf4f56bVyWPkRBNLt3dC5mzpBhEJgdmN-i5LU9p3PadorbhWQgH7tErb-j6WKm43DFOJ37m2wQt78pm2nF2qzLoy8M7JqsawE42quhhsKsc9xMOzIp5FIVg_NUSe9aidTYzAuNLcy4QtI3f5pSLYimZdpZ7uX8phSAgsIm6F5Cb3PipjnjUPU-ZxJgyQoSUtOIVboNTwlHysVFu55zRKkdZ99veK9lvo4lQmNv1wDJ7Jp-DoeJ-aKPGOC2T8lGjYl1sX-PAoxmkla-5s6utPvuWKqYirlAmFuO8DaTzbUUef0u8h_MHigkIZiT908crO4pHbPOmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
یاشار : این ویدیو نزدیک به ساعت یازده شب تهران در زوریخ سوئیس گرفته شده، در نتیجه نشان می‌دهد که تیم در همان زمان محل مذاکرات را ترک کرد و دیگر ادامه نداد.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15552" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=VZ5v5aYeVvc2tPEpTWXy_cFG3_icGMQdIYUqWwyirPdUo9fRv6jXsFO4VE6KZqTNDX73JcPDAMvcZv0Oy72xE20O5bZuJd_oYkHRvgcV9qPo0gzC_VDxPTn7h0Wca7BBl1K2VAb2M7AIRqrRalAZQXTUv6UCVMuu92BPpcaI41rnzQSgBUXSuyZA545-6KcwPm3bym6mxah9PFZpvXqFoOE5GSZMtaxqVsUrlwAzyTrNIkBjpWoTibS16D-MnbrQqJ4Mtp0-C5pF7mFymG9Ia0DtqSoXdQgulDGpkc9q4OwWa5Dm6IdeyfaAPMMtx3kK6YhF6P3QUNc1iLdfrc_OJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=VZ5v5aYeVvc2tPEpTWXy_cFG3_icGMQdIYUqWwyirPdUo9fRv6jXsFO4VE6KZqTNDX73JcPDAMvcZv0Oy72xE20O5bZuJd_oYkHRvgcV9qPo0gzC_VDxPTn7h0Wca7BBl1K2VAb2M7AIRqrRalAZQXTUv6UCVMuu92BPpcaI41rnzQSgBUXSuyZA545-6KcwPm3bym6mxah9PFZpvXqFoOE5GSZMtaxqVsUrlwAzyTrNIkBjpWoTibS16D-MnbrQqJ4Mtp0-C5pF7mFymG9Ia0DtqSoXdQgulDGpkc9q4OwWa5Dm6IdeyfaAPMMtx3kK6YhF6P3QUNc1iLdfrc_OJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که شروع انفجار را نشان می‌دهد، در این ویدیو می‌توانید صدای شخصی را بشنوید که در مورد محل انفجار می‌پرسد و سپس با «لوسیل؟» پاسخ داده می‌شود، لوسیل در ۷۰ کیلومتری رأس لفان قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15551" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_I0vbo5I5gs2TAGohH2kMpVOXYghNVwfCY-QedW5RmAd-unWcZpeynBuIReEDKLS89pgRCFZBmmPhqMweaYzg6fsf3b1bPQg9pR4FPsToEvPEI1X3QsPW7vl4u5u_-3AjBCuGtsJjiViebguK5EJolrE0TGBIOGm9EvsvSJP0MA_qjM2HMwoKTexzXvYiBye0drYS7ALn0jDTCUyXvCz5IAaKRzS0wwdeuMdhd-F2BOhYjxsanrW148b5kYp6ETKVO4q24bPXw3B6KbJgI87F2yUoHldgsdQnnBYdwKScseDHZXfHLfSbXNMQh-_5_WXjTeNp3tE4RpxW9ocEok4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایتالیا و نخست وزیرش پس از صرف تریلیون‌ها دلار برای ناتو، حتی فکرش را هم نمی‌کنند که درگیر جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آنها شوند. دهه‌هاست که ما از آنها دفاع می‌کنیم، اما وقتی مورد آزمایش قرار می‌گیرند، آنها آنجا نیستند تا از ما و بقیه جهان دفاع کنند. خوب نیست!
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15550" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDqNRNPApVwu0NW6pO0PQqWyYgLSq_2KvJzFIzNKTtVi2SU28Z-CKDgBVH7rl5nCTjrdMR_auvDJvHPqjn48jNHkRUM0t8ITHAfuVvL8wXzSsqxf0B9apKanqHFP7eLp7-uALb82ccrI_cWRQxw3_bZ_Bdddx3GSsaclKNqmJh1yHqvYwsYf-8Z766AmDdOwN9i20xP-y-vtml3R_Cy8hVeB5-IsR5khk_Z7E7TvdKb73elnexWb8RlhcEkPgOT1oq-OdPVgfLKXvbRNvXV18N4wvP4gjh96hxtMAppE2BcYes_gM6-0B-vKTBGsz1kcLlRFPvA2DK4OdXZMRYOa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتشسوزی عظیمی در مجتمع گازی راس الفان، در حومه دوحه، پایتخت قطر، رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15549" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گویا تیم بلژیک رو هم جادو جنبل کردنش…
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15548" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گویا استادیوم همه دوگانه سوز هستند
🤣
@withyashar
صحنه گل آفساید</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15547" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گل قبول نشد افساید شد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15546" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گل برای جمهوری اسقاطی
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15545" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8752439b38.mp4?token=IKKaG0Qac_1RoEQqvnlLEqDUCtif5yk3wGDtbsAYtKQUL0s_DsIKngEZ_uUSEc8K00XhMvIjK-j2peoDOtsCrVNe7bMqgd53f5hDCR0aXXV2C8qI9V2MFIQaLNNnM_bqEXQ5KKl7LR2G5r-yF6hgM3hFZlrSkre7CmPXq3wCfkshkgDXXWMcyiB58NZu65tX2323AaXyYzjtX_g0pNb-Kjs82eqpj-o6KYYsG0fS6bDmDizoPyyLS-JUcMxIFQ8yg-HyV4szDC7DkJOOfFJHwsjxYIxemAYplwrbtR0GaPL6FrOIHfckbrznr2Z9MeHN_KahWfNFxCgj_cqR87AL_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8752439b38.mp4?token=IKKaG0Qac_1RoEQqvnlLEqDUCtif5yk3wGDtbsAYtKQUL0s_DsIKngEZ_uUSEc8K00XhMvIjK-j2peoDOtsCrVNe7bMqgd53f5hDCR0aXXV2C8qI9V2MFIQaLNNnM_bqEXQ5KKl7LR2G5r-yF6hgM3hFZlrSkre7CmPXq3wCfkshkgDXXWMcyiB58NZu65tX2323AaXyYzjtX_g0pNb-Kjs82eqpj-o6KYYsG0fS6bDmDizoPyyLS-JUcMxIFQ8yg-HyV4szDC7DkJOOfFJHwsjxYIxemAYplwrbtR0GaPL6FrOIHfckbrznr2Z9MeHN_KahWfNFxCgj_cqR87AL_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمارش معکوس و شروع بازی
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15544" target="_blank">📅 22:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بنیامین نتانیاهو: به من گفتند وارد رفح نشو، شدم؛ گفتند به حزب‌الله حمله نکن، ما به حزب‌الله حمله کردیم، گفتند با ایران مقابله نکن، ما با ایران مقابله کردیم
من نماینده منافع اسرائیل هستم، نه آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15543" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/414dee64a9.mp4?token=pkVtV1FUO223I7bwSRXUdB-yXUcfKYTKBEl06g2X017jP0L3022zo0ntlDBCC6cK-kdhwaZgTbxoWAO0Z3fK-XdyS50nitZCCPqs3WZmrPViFieh4QkJ9MzPUXgRvz2h7ZtzoXbPaQhrN7mEbDESWH9tC4d1gP53EYnb98pCD76LyXTW2KZ4d8QI_aAHNsgcdg_d3RHcr-7ai-jHduBStpAuknyUepnbDawB8FKpkzmGSxpRRM5H-jR1WHL9Y7Qt1DIKc82MX_K5rxkA4XRS7nShgyYvcDhQPSJcT_RePeiEphZ67kX1gI9XHNHGfbNUTt1YH7bDOyn6AoTFLUO77TyvwAlZaM0f9m8S-BHMek_ZlBk8pidwWbnL1WzMJ8ulsXrorG3quKoCGC6UqycpCq0yVTaQQR2sCn1PcsZB93F9XuxsHForsSq9d10Jaf7Dvnk8jTZNDoCxyi10x9sI3puonxngcf2z4N8HbyQBVYTz4ZNMo1A3sDxqMWGe-JY9NYRXGxPgNCk6wcUy8WBeI0L8FoMGJi7zVdQBBgn2fAEranDIJxPavQCpxvEC2P7RNbvcFdBzEDlmp_x4f3_NqvBVEFKv2cn7PS8Ys7pqr3mmE7W84A-ZWUp6UyKa1gcNhoXk4tjOYsiAYTAB_UFsnN8PhYEYJHnkfEDUtMqxf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/414dee64a9.mp4?token=pkVtV1FUO223I7bwSRXUdB-yXUcfKYTKBEl06g2X017jP0L3022zo0ntlDBCC6cK-kdhwaZgTbxoWAO0Z3fK-XdyS50nitZCCPqs3WZmrPViFieh4QkJ9MzPUXgRvz2h7ZtzoXbPaQhrN7mEbDESWH9tC4d1gP53EYnb98pCD76LyXTW2KZ4d8QI_aAHNsgcdg_d3RHcr-7ai-jHduBStpAuknyUepnbDawB8FKpkzmGSxpRRM5H-jR1WHL9Y7Qt1DIKc82MX_K5rxkA4XRS7nShgyYvcDhQPSJcT_RePeiEphZ67kX1gI9XHNHGfbNUTt1YH7bDOyn6AoTFLUO77TyvwAlZaM0f9m8S-BHMek_ZlBk8pidwWbnL1WzMJ8ulsXrorG3quKoCGC6UqycpCq0yVTaQQR2sCn1PcsZB93F9XuxsHForsSq9d10Jaf7Dvnk8jTZNDoCxyi10x9sI3puonxngcf2z4N8HbyQBVYTz4ZNMo1A3sDxqMWGe-JY9NYRXGxPgNCk6wcUy8WBeI0L8FoMGJi7zVdQBBgn2fAEranDIJxPavQCpxvEC2P7RNbvcFdBzEDlmp_x4f3_NqvBVEFKv2cn7PS8Ys7pqr3mmE7W84A-ZWUp6UyKa1gcNhoXk4tjOYsiAYTAB_UFsnN8PhYEYJHnkfEDUtMqxf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون دیدبان اتاق ورزش در تهرانجلس
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15542" target="_blank">📅 22:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371017822d.mp4?token=ADvINxM7y_aXe3TmLD_F2FdFyKpDI9r4ZNb5QbkwLufnDlXXJVivLEMX5fx5xe-3sGMJ8Az_oB9ODI2c-tdNWN4zDnQKDwcwO6794N7GDL7amo9HX3G92o_jyvZUW02eCHR6w-Et-0R4Yu4qzt9cZHxbezFhUDaXRZW7-eDirjmK0p2R3LQeekrhLcAzojMCQEwYfE39Sxszc2DU7vWo4i9S_L23pEhELjbWKLZ8zk7r3fxl48SSKbXQk8JxKsLhyN8w9E8e08_rsCzPqv1dzqJcTbXyf5ytRxyFm8rynwfcXSB2Om_eHg7oNu2yiI6fvnJR99MECNzOr7geRFxkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371017822d.mp4?token=ADvINxM7y_aXe3TmLD_F2FdFyKpDI9r4ZNb5QbkwLufnDlXXJVivLEMX5fx5xe-3sGMJ8Az_oB9ODI2c-tdNWN4zDnQKDwcwO6794N7GDL7amo9HX3G92o_jyvZUW02eCHR6w-Et-0R4Yu4qzt9cZHxbezFhUDaXRZW7-eDirjmK0p2R3LQeekrhLcAzojMCQEwYfE39Sxszc2DU7vWo4i9S_L23pEhELjbWKLZ8zk7r3fxl48SSKbXQk8JxKsLhyN8w9E8e08_rsCzPqv1dzqJcTbXyf5ytRxyFm8rynwfcXSB2Om_eHg7oNu2yiI6fvnJR99MECNzOr7geRFxkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران: «فکر می‌کنم ما شرایط لازم برای سقوط رژیم ایران را ایجاد کرده‌ایم.»
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15541" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15540" target="_blank">📅 21:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2572e3b3.mp4?token=NcAs7ooWvJMw5eUoF9kcSeGUK-Ow-gAma3aUf-yLah-myDW89D0Bd_OXSNPUyW_ZhU9aBvbJM74W5YvLsY-r2hMJfNpArmWkb4qbVclvymT2xaerIuNxxq1pRCesn5RE35SB4-P6lAck05vF1P4Sp6cd2zWXKewbxUzvj6bjVdAD4gRqKQIf80yMH3feTcFoTU5soPDsa3vM_6IDLjePN9OJQgn876ToBfW-A5QCOHnWbn3vq9xHTkBkp0Z3cMsXGvAC6lI4xhNzsn2sWbpUkWdcU00DQeDMUrYlXELAC2bnjVn568BlwrBo3n9qMliLok4yyhqiDnayxxAuFrq0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2572e3b3.mp4?token=NcAs7ooWvJMw5eUoF9kcSeGUK-Ow-gAma3aUf-yLah-myDW89D0Bd_OXSNPUyW_ZhU9aBvbJM74W5YvLsY-r2hMJfNpArmWkb4qbVclvymT2xaerIuNxxq1pRCesn5RE35SB4-P6lAck05vF1P4Sp6cd2zWXKewbxUzvj6bjVdAD4gRqKQIf80yMH3feTcFoTU5soPDsa3vM_6IDLjePN9OJQgn876ToBfW-A5QCOHnWbn3vq9xHTkBkp0Z3cMsXGvAC6lI4xhNzsn2sWbpUkWdcU00DQeDMUrYlXELAC2bnjVn568BlwrBo3n9qMliLok4yyhqiDnayxxAuFrq0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد.
و در اسرائیل می‌گویند من هر کاری را که او بخواهد انجام می‌دهم.
هیچ‌کدام درست نیست. ما رهبران کشورهایی مستقل و با افتخار هستیم.
من نماینده منافع اسرائیل هستم.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15539" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">المیادین: هیات ایرانی تا زمانی که ترامپ عذرخواهی نکنه و اسرائیل از جنوب لبنان عقب نشینی کنه، به مذاکرات برنمیگردن
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15538" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu3WSB8nlSM21_039zaCnJdpk8bEqh4ib8kszZDaMt2y7AH0EMCl6DqPATXJvB2sgPsAhlZ0pEzYSiaMaOe6Q-cRoiTzYICMenTkamk0J6nvCnHz4LeQSLc-oDRBu0PpYpzPKhyZqyVIlD396JjNJpXp_jXzsdgRrg-upBUvo4FiOVPq_U0Ia3n19Au2tyxRXdx9dpSu7EIhXNnG_fBEVOnbXaGsEoj7jtFvTvATlXA8gICmTpfPfvd_jl2OjSxfylEBZMag5W0jESza3oYA4KIocgNDVS5crSNuo5zH2u31ROgueWznTOJzBOlVhOyT5DsriqTLTiC1L-eN0z0Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل و شین بت: یکی از تروریست‌هایی که کودکی به نام «یاگیل یاکوف» را در ۷ اکتبر از «کیبوتص نیر اوز» ربوده بودند را همکنون به هلاکت رساندند
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15537" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نکات فنی ارائه شده توسط قلعه نویی به تیم @withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15536" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COfRzPdNsEroWAtxuVAf_aXovROycCUmGQmNg_wER_guRnPwVBraSNOPyJX0kthhxqCI99IbOxBjR0Ds5YLQ5-rcwAMCm0xMCbgOmZU1DXcGY-C0beQytcV5BPKyVHTgJNA1JccZO1vwo2PvHjo31etAT1scPPA0xbexvgrQL0wEzciamQENCEh6vfVc5u27onVzdrl35X9K05dmERQCLgDQ5NeGU9Jc7cP4MgbMDJ-XDEEWx_tP5ofNIHdmCIOofyvdEW_ezQp67gZ82_O0wzDfoM5hbmon_8-NUoAL_W9ySrgyQ7S5aN-QCFkTtxWXBUaef-hJ_vkGpTqovGk4zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکات فنی ارائه شده توسط قلعه نویی به تیم
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15535" target="_blank">📅 21:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی‌برای کاهش تنش تنظیم کند
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15534" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منابع «العربیه» اطلاع دادند هیئت مذاکره‌کننده ایرانی در سوئیس به محل اقامت‌شان بازگشتند اما گفت‌وگوها از کانال‌های غیررسمی ادامه دارد. @withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15533" target="_blank">📅 20:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">منابع «العربیه» اطلاع دادند هیئت مذاکره‌کننده ایرانی در سوئیس به محل اقامت‌شان بازگشتند اما گفت‌وگوها از کانال‌های غیررسمی ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15532" target="_blank">📅 20:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کاظم دست کج : لوکیشن هتل رو یکی بفرسته بدم وانتی
😂
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15531" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هیئت ایرانی : به جون مادرمون تو هتل زیر پتو هستیم داریم کامنت میخونیم
😂
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15530" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس:
مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره.
@withyashar
یاشار : این باراک درست نمیشناسه اون که مونده کاظم دست کجه
😂
صبر کرده همه برن سالن رو خالی کنه</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15529" target="_blank">📅 20:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عربستان
0️⃣
-
4️⃣
اسپانیا
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15528" target="_blank">📅 20:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15527" target="_blank">📅 20:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سناتور جمهوری‌خواه نزدیک به ترامپ:
مذاکرات با ایران به توافق منجر نخواهد شد،
راه حل دیپلماتیک با ایران شکست خواهد خورد.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15526" target="_blank">📅 20:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فارس : هیئت مذاکره‌کننده جمهوری اسلامی هم‌اکنون در هتل محل اقامت حضور دارد
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15525" target="_blank">📅 20:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15524" target="_blank">📅 20:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عضو هئیت ایرانی در سوئیس به صداوسیما: اگر جنگ در لبنان پایان نیابد، مذاکرات ادامه نخواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15523" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahar</strong></div>
<div class="tg-text">ياشار جان سلام. وقتتون بخير.  يادتونه راجع به هماهنگي تماشاجيا گفته بودين؟ الان ليدر ها تراكت بين تماشاچيا پخش كردند كه توي كدوم دقايق چيكار كنند و چه شعاري بدن.   ميدونين. من خيلي نازاحت شدم براي هايد كردن اون كامنت زير پست اعليحضرت.    اما الان بيشتر از قبل مطمئنم اونا اينجا هستند و  كامل تمام حرفهاي شما رو گوش ميدن
مهم در انتها  ازادي ما و ايرانه.    اما خب  ما ميدونيم خيلي از حرفها و ايده ها و ابتكارعمل ها از شما بوده   (ايموجي هم نميذارم - قلب- پيروزي)</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15522" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فارس و تسنیم : مذاکرات بخاطر تهدید های ترامپ متوقف شد
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15521" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15520">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار صداوسیما در محل مذاکرات:  گفتگوی دوجانبه هیئت های ایران و قطر، بعد از مذاکرات چهارجانبه آغاز شد
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15520" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbsG-NPmRlVMEuAHks-9wx8x60nFemC0Usug8QhXNIjJ88-ccI-tjtiqDrHjpclVsIAX0dgtj5DijDHzw5ysjzT2C4ySzOqI1DinMccpekOHiRM7-8BhYvTUFwMNA8amYXZy7WINOvWYU8a0YnaN7a2lXjx-Q0HP9K5Mul32rJFy6UoezfPlH8GL1GN6uw_0ocInMBhFCWld-3-CD8TETtk-EkE5oalGTGHCLj_wxiFtyvRFVLgDXBlyD71-iRPC82oH3a82rpBUaJIqvX9yhjXW4G5s-XMehE-qyRCTzjc7QiQsTQhiimm4EJP5aBMy3qBZgwFMX83rhU2hWgbpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس ویرالی که حاکی از بازگشت محمد خردادیان به ایران است. وی در دهه هفتاد و هشتاد هم به ایران آمده بود. ولی در این شرایط نظر کار بران را جلب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15519" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFPiXNhZ5hdceR8GtG1RJfN0LBxI_zfIfvJLz1oN9rm_K2lo9A57c35zH0advGEZM-vVVw1eIgw9nYFHUf3U-wyIINCQzjVPBjLfZA2SJswcYZgTpJeRfMk_ArPzF8nv28m9PrBd3MGN_rVcERRFvjF1MSpnMGzknfbHl6Dky9ogcMM7PmgQW54-bcfa5HPZonZ18czo_VHSnWHF1OnRlmKAmtFn1CcJs2o8KvDRyrjVWAhOwIXZtTD-x8dw2eDZGWkM_4VE_fW8qoxNNGz89F5OTd4nO72eFLP9ISbqc5BgM0LiOtqbXcA8v6s8oJ6OjLnfeqjJ4E3eQfoc_G0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام: پیامی به ایران؛ اگر با استفاده از حزب‌الله به اسرائیل حمله کنید، سیاست جدید ما حمله به ایران خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15518" target="_blank">📅 19:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjfbCHgtA61g73l-oqJRiDVip4Pw1ExkccpKWCcc6hpipfyPGAceGTtiZ3KnghtFoj0dwQN083xbPrAP-KSKebWMenva0pKOnN7d85qbjWxM--oSzzs4d6o5lh9oZs0G7itc9euwCsWM7OqQN5GlVmgK9aZtk6PJ0iIx6HsR7zrkzi238Fzv--YlBZNhfJzCcTl5SKh7OpT5UkSH5XZCTSz7V9uuEonrBqkFo-w3wnvDA7EqI87duMpqGohsKMpvvb7NVkIPJnXnoJCb0ldtliBq4DeX5gOeY9CXFQzWhwiGzTHDLvPdrmSli59JWfoO27P67d5aOI_g-2PdPXRGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس از انفجار  اهواز شهرک صنعتی شماره ۳ پشت فولاد خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15517" target="_blank">📅 19:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش انفجار اهواز شهرک صنعتی شماره ۳ پشت فولاد خوزستان ۲۵ دقیقه پیش
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15516" target="_blank">📅 19:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfaa84bd6.mp4?token=GvbV3jmnGs1Ef9WdremAK7AzkEnpuxIAwNhIAcQ3dnPSi6Dy_9kCkNIOYbxi92gTvWLf_s4XVioNTXEet8L0N7NNvRD0128DdS5-9E_RWrdOKVlqvlfNyfHodyKS70SAgPb_UcS-QiSsDaR1-62--bRLB0koPNYd9erB6ZUoAcYw2dT1wI2oaIkB6Pdn3WKkEYH5LVzkmTHykRoySQWpaWGD0ArPkCWAAqmhAxWbtMXFcxvJQMGseGoR6bxmLAFsJmQLR0TDt-7Gy37S9nE2oMA8EEV-gKAIlWWrbCWSuIVw8TROeLPp3n7TBJVLZBpRtl-RwKTwZ9U6zblRgnk_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfaa84bd6.mp4?token=GvbV3jmnGs1Ef9WdremAK7AzkEnpuxIAwNhIAcQ3dnPSi6Dy_9kCkNIOYbxi92gTvWLf_s4XVioNTXEet8L0N7NNvRD0128DdS5-9E_RWrdOKVlqvlfNyfHodyKS70SAgPb_UcS-QiSsDaR1-62--bRLB0koPNYd9erB6ZUoAcYw2dT1wI2oaIkB6Pdn3WKkEYH5LVzkmTHykRoySQWpaWGD0ArPkCWAAqmhAxWbtMXFcxvJQMGseGoR6bxmLAFsJmQLR0TDt-7Gy37S9nE2oMA8EEV-gKAIlWWrbCWSuIVw8TROeLPp3n7TBJVLZBpRtl-RwKTwZ9U6zblRgnk_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
تا زمانی که لازم باشد  در جنوب لبنان باقی خواهیم ماند
و در مورد ایران، هرچند تحولات سیاسی باشد، اجازه نخواهم داد ایران به سلاح‌های هسته‌ای مجهز شود
تا زمانی که من نخست‌وزیر اسرائیل هستم، این اتفاق نخواهد افتاد
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15515" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOE8XvYY-r8pii86CnlrzbgjXUiDn0cSY_B9pgm5krG-auY33UaLLTkCrMSdKqTNFbRHlTOk3jx-hQiGjOtKyVHiEO9p-mPq0PyC_IXuRi_7v-FZzQlofVxn36ogtixYyWEsuN9cdQX_U1NNbZiv3NiTeLk-Z65YyDZFasLUWImZzIzuIYr5bccW0C4IXczgNujnBBgCXzIVVr2CdhvoHubfMNMUo5o0GQwgLVkA2y_W55FpEa2jKq0HTKjSemo7AUp2HBENdyOtqLWOFyChfP60inxU2dMbguDBD3u43WdWUZ2sz45J4t33LIv3qCCANQxOhvRU0bobR1PUdF1YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ۸۰ دقیقه مذاکره، مذاکرات چهارجانبه بین آمریکا و ایران که با حضور میانجیگران پاکستانی و قطری برگزار می‌شد، موقتاً برای استراحتی کوتاه و مشورت‌های داخلی متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/15514" target="_blank">📅 18:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f4a5bbf.mp4?token=hnKIRUh_EAvyuREJWAJts1hBuDk7njt3i9V0itlAu9nqh9YBB-Wv_z9X468Ca7Z8Sw8GCyrasGGC0bHOLP0qsLgsteo4XoQNyXNjzr9XyG0CuQ8_RyU1rxt761hrha9Pv9OlnjmEOlS9J6dKjCSqy11xec_8Z30ANOiKxz0P_oESyG4mNzw2UAt0UrqQdjZWOanWg-Uqq1rFr2kgA3O0SeMs3288BwTY5enma_M2gt2-o_dggTi3ZK_83CXOeOI0I2zLE28zs6xEmm0Geaa9FE7Ei3wbDxqZbNlUfcqcRmMHKL0DpmVI5MfBY4IxedkLHRVJUfOWxQHFt9k5cTOFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f4a5bbf.mp4?token=hnKIRUh_EAvyuREJWAJts1hBuDk7njt3i9V0itlAu9nqh9YBB-Wv_z9X468Ca7Z8Sw8GCyrasGGC0bHOLP0qsLgsteo4XoQNyXNjzr9XyG0CuQ8_RyU1rxt761hrha9Pv9OlnjmEOlS9J6dKjCSqy11xec_8Z30ANOiKxz0P_oESyG4mNzw2UAt0UrqQdjZWOanWg-Uqq1rFr2kgA3O0SeMs3288BwTY5enma_M2gt2-o_dggTi3ZK_83CXOeOI0I2zLE28zs6xEmm0Geaa9FE7Ei3wbDxqZbNlUfcqcRmMHKL0DpmVI5MfBY4IxedkLHRVJUfOWxQHFt9k5cTOFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر ایالات متحده در اسرائیل:
من رسانه‌های اجتماعی ترامپ را بررسی کردم تا مطمئن شوم که این آخرین سخنرانی من در اسرائیل نیست.
او معمولاً افراد را نیمه‌شب از طریق رسانه‌های اجتماعی اخراج می‌کند، بنابراین می‌خواستم مطمئن شوم.
تا اینجا که خوب بوده.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15513" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پایان نمایش مضحک رژیم در خیابون های ایران
معاون پزشکیان تجمعات شبانه امنیت روانی مردم رو مختل کرده و باید زودتر جمع بشه.
وزارت کشور رژیم :بعد تشییع رهبر، تجمعات شبانه جمع میشود
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15512" target="_blank">📅 18:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPZjH7FwLmdDAG3-Bb25I6XIcvXcDIMx2MQ3YfyZ_C07Isv2A1tKwool-Mxj6L9mg5_yqH__JhFtg0rAKZq95seEo3Qi4ppc0HjUkBvBf1LCZ1av08lLfmaeLi5kFGv9y1hig_ybNAWKssN2sYfPsbVwdqzPhbmnyZBBGQfyabL-BGvyOLS9VlKmp9uSA4e538tjZj-BCn2yFDn2_x2dU18QRZg1V6s9wVFyE291uAF_DGyP-pSBebFc5Jjgjf84XJK5csIJx4R4JZqaYXvYo3XVHAsKj3cvozxbFKSYzURjsuyc12oD8ZRlU7_4rPvO5jFEVEC9yCfNoNXG2sqnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی اسرائیل به اردوگاه البریج تو لُبنان، حمله کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15511" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
گزارشی از حادثه‌ای در ۵۰ مایل دریایی سواحل یمن
یک قایق حامل مردان مسلح به یک کشتی نزدیک شده و به نظر می‌رسید که سعی دارد سوار آن شود.
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/15510" target="_blank">📅 18:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شروط اسرائیل برای اعلام آتش بس کامل با حزب الله:
خروج تمام عناصر حزب‌الله از شمال رودخانه لیتانی
تخریب کامل زیرساخت‌های حزب‌الله در منطقه جنوب رودخانه لیتانی.
اعطای آزادی کامل حرکت و عملیات نظامی به اسرائیل برای خنثی‌سازی و از بین بردن هر تهدید آینده، که شامل عملیات زمینی و هوایی میشه.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15509" target="_blank">📅 17:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgV4_010NgZG45y75_ikW5IlfV4CHLgQzkMxGEuVS_ma5mY8l3p6eFfxO6o7rEv3rM-UPIxcwXpPS_r_hdZRIrm3ET5q9eR9GXbjOwfXUlE6gxGpn_u9nrz62B4U-n0LHo8-s8WgSc9PxltgcL2RdYMpzTU84OC5evaTdq7bZIYwepo7WuNHxJsIHdt3q630r7btMgD6teJGAvabsBz-RNodmii3l7DilAOEwfwJDXH0Km_p-KCgcbmCvpRs01upDchmWs7LIXl-tEYRWykK75LZn3elSA5vl9wr8awp_U8Cw6BxNqE9KZOA-xL2zFBsnUnwBoVi_eZMUxk2COC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر استارمر از سمت نخست‌وزیری بریتانیا استعفا خواهد داد. او در دو موضوع بسیار مهم - مهاجرت و انرژی (باز کردن استخراج نفت دریای شمال!) - شکست سختی خورد. برایش آرزوی موفقیت دارم! رئیس‌جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15508" target="_blank">📅 17:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل: آتش‌بس اعلام شده در لبنان «شکننده» است
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15507" target="_blank">📅 17:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: یادداشت تفاهم صرفاً تمدید آتش‌بس است
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15506" target="_blank">📅 17:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: از اسرائیل ناامیدم. اونا نمیتونن حزب‌الله رو از بین ببرن. حتماً باید چندین‌تا ساختمون رو نابود کنن. احتمالاً مسئولیت این‌کارو به الشرع و سوریه بدم.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15505" target="_blank">📅 17:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iql5Z_i64ZmnkPK9Qk9nfv82faOoN9t7pPsb4YtyNVQFsRvC4nbieF34Mg8epvBCXj7_5TE0afcadxKxkAbLgqYmcOvuPpSz87izqTA3wvcK53c2Z0U3Gdii7i6aVBPn6FtxuVXduPL0bm61cP9BFbjucJfN8Tc_5dxaA9iz41FWCDRxRnlZRJatvqgDQW2YwH_usyBJwyihbaQmgsrmSK-e6DEdz_J8I7q6GiajXZAifrTl_IEXF6AOGb91QIBNY2VMCif-yQmbJRLVlF5CRqDXOXlLgL9u9D5kHspzBloYyaZzrPMSMg7WcecezAVCITUmw2FRKj77-mCG6jrN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!!! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15504" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303a07dbdd.mp4?token=QHdljTJdmRYvmMcs-aUZ-gK9rMdhoneVkj4mS67LZxcxM-D9cYzpRXgDABo0uyoJjJt-HKn22INPDkDwHk0bNPm8_1LUrCYjS_N2XnduyKVeMgiiWolPzr5Cj8D9C8Pj7FmTGjhbE8b6j6sXDeDaRiTGFhj-n3ZhmTMuIKvGYAnHnanYQDu-AaSqMgNiv-BHZ0aFvHtUYxxrl4dLYV80tD3UYe98EPgCYN-7u-U9oR5KJZaPbQz5Rg-_fqSOl0FAK9Tm9F20L25cX1GVvAe9YDgMsqQMVo13alskl7WYqC5H4pYJeKRxTMwTbgpocqQ5sAt4S9zWqu7BMbe6fGDTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303a07dbdd.mp4?token=QHdljTJdmRYvmMcs-aUZ-gK9rMdhoneVkj4mS67LZxcxM-D9cYzpRXgDABo0uyoJjJt-HKn22INPDkDwHk0bNPm8_1LUrCYjS_N2XnduyKVeMgiiWolPzr5Cj8D9C8Pj7FmTGjhbE8b6j6sXDeDaRiTGFhj-n3ZhmTMuIKvGYAnHnanYQDu-AaSqMgNiv-BHZ0aFvHtUYxxrl4dLYV80tD3UYe98EPgCYN-7u-U9oR5KJZaPbQz5Rg-_fqSOl0FAK9Tm9F20L25cX1GVvAe9YDgMsqQMVo13alskl7WYqC5H4pYJeKRxTMwTbgpocqQ5sAt4S9zWqu7BMbe6fGDTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دیگری از لحظه ورود هیات ایرانی به محل برگزاری مذاکرات در ژنو
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15503" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa6a9c9af.mp4?token=DqoXkQtTkD7nqIdCDlwOsUStQviZ6cTZ4ScZSLTrHBkfY8DqNgQJFQZihpKmgWTClGJl1qC6IK7YYdhE4k3vh1EcaWUcjgRnvMHsX7pQywVSQ1z4OIXOsfCYeio2eaIurWAs7592hfk4sSzrfyMpMUhFSa4JpVsldp7044qdMM6KsruI6NrxkKqdk5AT3i8vNZ21NGQ3OPHqeFRW-w1ib6mwbQHm8Xw00ES0usg32mATvO3jU2DWwHv_4FYM4cgciIkMXSuOY0iikAL2M3zfz9JEjh65AMqyRG4j1h2XLXNfmBwZBhZpjuVY9q1fCI5PG10NT_2WqeE2nSw9o6AwSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa6a9c9af.mp4?token=DqoXkQtTkD7nqIdCDlwOsUStQviZ6cTZ4ScZSLTrHBkfY8DqNgQJFQZihpKmgWTClGJl1qC6IK7YYdhE4k3vh1EcaWUcjgRnvMHsX7pQywVSQ1z4OIXOsfCYeio2eaIurWAs7592hfk4sSzrfyMpMUhFSa4JpVsldp7044qdMM6KsruI6NrxkKqdk5AT3i8vNZ21NGQ3OPHqeFRW-w1ib6mwbQHm8Xw00ES0usg32mATvO3jU2DWwHv_4FYM4cgciIkMXSuOY0iikAL2M3zfz9JEjh65AMqyRG4j1h2XLXNfmBwZBhZpjuVY9q1fCI5PG10NT_2WqeE2nSw9o6AwSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکرات بدون حضور خبرنگاران شروع شده.
@withyashar
تصویر عباس عراقچی و جولی ونس در سالن نزدیک هم</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15502" target="_blank">📅 16:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ به فاکس‌نیوز: آمریکا میتونه بشه فرشته نگهبان تنگه هرمز و 20 درصد نفتش رو برداره. اگه لازم بشه، خودمون تنگه رو تصاحب می‌کنیم.
اگه معامله نکنن، همه‌شونو به باد میدم و حسابی لهشون میکنم. اگه نخوان معامله کنن، عوارض راه میگیریم ازشون. اگر تنگه رو ببندید دیگه کشوری براتون باقی نمیمونه، حتی نمیتونید برگردید به اون مملکت لعنتیتون.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15501" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تسنیم: هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/15500" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فاکس نیوز: ترامپ گفت که دیشب با مقامات ایرانی صحبت کرده و بهشون درباره بستن تنگه هرمز هشدار داده.
ترامپ گفته اگر تنگه هرمز رو ببندید، دیگه کشوری نخواهید داشت و حتی نمیتونید به کشور خود بازگردید.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15499" target="_blank">📅 16:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15498">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc459a9119.mp4?token=bDFXomXHuW5OfAbh6JQ5UkWRwkEpxswkb1zDnEuRwVxE2W_k1KeShFfxO2kMmrAsn-urQcfEDjtXjJbz4I2qOlxN1JgMoK4vLvUx9Zqoy4RvwWi6akZoRMY2V4AJq49USg4kv3oXKCVkEtIg83ScEaJE5tPJYLTBvuSErI32QZzm3iWB9h8BEoM_zI86q9modBp_9cbH6alQO8mV32ff7FdyFrTcQNZEoArnsAvgJPOsinT3ZTJKYAhmWWxxDauRf7-sizwjdkwwNt7keOZe-2eFTbDWaVAgz9XJGrEXH8wq6csz4vD-jF0_UT-QI5qg7crEmC4fsZlCwEokNzrG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc459a9119.mp4?token=bDFXomXHuW5OfAbh6JQ5UkWRwkEpxswkb1zDnEuRwVxE2W_k1KeShFfxO2kMmrAsn-urQcfEDjtXjJbz4I2qOlxN1JgMoK4vLvUx9Zqoy4RvwWi6akZoRMY2V4AJq49USg4kv3oXKCVkEtIg83ScEaJE5tPJYLTBvuSErI32QZzm3iWB9h8BEoM_zI86q9modBp_9cbH6alQO8mV32ff7FdyFrTcQNZEoArnsAvgJPOsinT3ZTJKYAhmWWxxDauRf7-sizwjdkwwNt7keOZe-2eFTbDWaVAgz9XJGrEXH8wq6csz4vD-jF0_UT-QI5qg7crEmC4fsZlCwEokNzrG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">..کشان آمدند
ورود قالیباف، عراقچی و همتی به محل مذاکره
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/15498" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جی‌دی ونس: به دنبال خاورمیانه‌ای متفاوت هستیم
وی اضافه کرد دولت ترامپ مأموریت دارد تا با دیپلماسی فعال، مسائل پیچیده خاورمیانه را حل‌وفصل کند.
ترامپ به دنبال ترسیم آینده‌ای متفاوت و باثبات برای خاورمیانه است.
نقش نخست‌وزیر قطر در رسیدن به نقطه فعلی مذاکرات، بسیار حیاتی و تعیین‌کننده بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15497" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دلار ۱۵۷.۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15496" target="_blank">📅 16:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ونس:  از آنچه در لبنان به دست آمده راضی هستم تنگه هرمز بازگشایی شد
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15495" target="_blank">📅 16:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه‌های عبرى: حادثه امنيتی جدید برای نیروهای ارتش اسرائیل، در هنگام عملیات انتقال مجروحان دقایقی پیش از جنوب لبنان انجام شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15494" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=uulNlnLTVwPKZrv4WWbHyHINStvFKte4Mm1A1NrIe7w-NJTtfpKkONhyoufuSCSOgnaJMQt0c7cq52vyceI7X6GuSqMEAWoUpx6y83wSNeOnQ5XiN8x35pZ7JufZU-SXAYgEULm3ECRdqENM2Cz0C2fk0sZdHnWeSk4GsiNOWOdc1WfKioW88oq8U10lPeHEU5tAHTGeH118SUWvypt1b3jXXeTxvBNXZXIjzb7nUixwgBKuq9ok4OEJ-9xBj3YExKxaPragP96H8zYaKkmZrUuvtSmNG6latYyXD6mfnY2FQwaIyuxHvRJu1JfI1I52PoGaHQZk26f0Ln9qqA6frQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=uulNlnLTVwPKZrv4WWbHyHINStvFKte4Mm1A1NrIe7w-NJTtfpKkONhyoufuSCSOgnaJMQt0c7cq52vyceI7X6GuSqMEAWoUpx6y83wSNeOnQ5XiN8x35pZ7JufZU-SXAYgEULm3ECRdqENM2Cz0C2fk0sZdHnWeSk4GsiNOWOdc1WfKioW88oq8U10lPeHEU5tAHTGeH118SUWvypt1b3jXXeTxvBNXZXIjzb7nUixwgBKuq9ok4OEJ-9xBj3YExKxaPragP96H8zYaKkmZrUuvtSmNG6latYyXD6mfnY2FQwaIyuxHvRJu1JfI1I52PoGaHQZk26f0Ln9qqA6frQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عن بازی همیشگی و انتظار هیات آمریکایی برای ورود تیم مذاکره کنندگان جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15493" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محل برگزاری مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15492" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWUVZfD91gEDLTvZVhw6Vws8l7kWS9DHZorFhpSbE8stR9ABpJdWiaa1M-o2mkWaZU8GtAdGuA2KD2jHnD4cHOSOYuEoooel_LFEmXA2o6aBgyKfL-4mxQGQYvNlT63aiz4n1Me0GWwE_5xSUvoIntW1ofgqece-hdX9gsj_-aM9uf_CacWFlFrYwgG9Ekq8zi8D--gLZjvBWUO6iiKKzCCVj63VXylvUycTK-4hbCadlJggz4cROpbVGV_IInsskqw8yjf8clMU5AR4oS54pjx6zKPAEfO-riVW4zbmYcGpPFw2l42IM85ePGC2VQz8O30RGXi8SvIQy3wI8J-WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
روز پدر مبارک!
کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای بی‌سابقه. خدا همه شما را حفظ کند!!! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15491" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEsNMawIw4tJIjdwxuUUe8UDdvKPwUu72Hi8i9GPGfWVWKYLOQqIN1acNlkKqVOAhuiVtfQwU3as3SjjPTdUoN-c9s_aRf9x68zCs4W9cZbc_j1Zc1eSMS8N8OuqIwr-kVemMwbmtQ2MiZgemxcvT0cR-Z-PG6fvkicBIw11W-wwYwd97Jho7qz9uJ50cnE6IV3YYTkknfvyTFXWQ_HiCQ7OF37kCxfKG86I8beDWpQhQG96v_xMrd2D7WZdATyqKY5o0rkVkptweKR5dg6w5yYC03ekf74MlsFk4sHDNxz3Yq0MVPnVEzeAspwGGZQcclYiqAKikAFUvDXv4tyipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت
جمهوری اسلامی
- زوریخ سوئیس
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15490" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15489" target="_blank">📅 15:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پزشکیان: مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده
از حق غنی‌سازی نخواهیم گذشت؛ آنها هم مجبورند بپذیرند.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/15488" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صداسیما: اینترنت سوئیس ضعیفه ارتباطمون با خبر نگار قطع شد
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15487" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پزشکیان: اگر تورم ادامه پیدا کند و به تورم سه‌رقمی تبدیل شود، آیا جامعه توان تحمل چنین وضعیتی را خواهد داشت؟
@withyashar
😂</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15486" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العربیه: شهباز شریف و عاصم منیر پس از دیدار با ونس، با هیأت ایرانی دیدار خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15485" target="_blank">📅 13:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پزشکیان : از حق غنی سازی اورانیوم دست نمیکشیم
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15484" target="_blank">📅 13:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محاصره ستاد کل حزب‌الله در جنوب لبنان،به گفته کانال 14 اسرائیل:
نیروهای ارتش اسرائیل مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان در ارتفاعات علی طاهر را که ایران در جنوب لبنان ساخته بود، تصرف کرده‌اند،
این مرکز فرماندهی اصلی که به‌عنوان عماد 4 شناخته می‌شد،بزرگ ترین پایگاه موشکی حزب الله در لبنان نیز محسوب می‌شود،گمان می‌رود صدها عضو حزب‌الله وسپاه ایران در داخل این مرکز گرفتار شده باشند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15483" target="_blank">📅 13:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسماعیل بقایی: موضوع اصلی مذاکرات امروز ما درگیری های لبنان هست نه مسائل ایران
@withyashar
بیا بد عرزشی هنوز فکر میکنه اینا برای ایرانن</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15482" target="_blank">📅 12:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=BYIwr1DPmbjWnFWh53zj6kpKrhMw496L6c1lcYH9VWMETZDRsCphL39ePDVts74_Ld3nTw9i9LLQTgQgzyPjGElz4_Ww-wz9uUkeCyGS1HYmva58KL8kLvTz84oy3jx_DOopWN-LhjFP_RcKzfEqqGdSwo5pNRqwk7iKLmgnMLTvBi_ppEOClZMmFf02BHGzerBFJrAn7o8ZQt7Kv0EFrjTay0jl97jf_NumWqSDrjw7zgFI8Co-xX_XK1LFnQDJZJqBC9LJl2U4WO1sc5xEu_BigvLTjxmSQKywt_hjiTWKWZKyzPcJg_WVqu0AJx1CVn0LWn1tEoRZUxKci56NMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=BYIwr1DPmbjWnFWh53zj6kpKrhMw496L6c1lcYH9VWMETZDRsCphL39ePDVts74_Ld3nTw9i9LLQTgQgzyPjGElz4_Ww-wz9uUkeCyGS1HYmva58KL8kLvTz84oy3jx_DOopWN-LhjFP_RcKzfEqqGdSwo5pNRqwk7iKLmgnMLTvBi_ppEOClZMmFf02BHGzerBFJrAn7o8ZQt7Kv0EFrjTay0jl97jf_NumWqSDrjw7zgFI8Co-xX_XK1LFnQDJZJqBC9LJl2U4WO1sc5xEu_BigvLTjxmSQKywt_hjiTWKWZKyzPcJg_WVqu0AJx1CVn0LWn1tEoRZUxKci56NMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسکو دیدبان اتاق جنگ در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15481" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=KiSCuhElyGW5dzSVCyHQp8rDpOyfX8BACasH74ejZttb0wEG7-RYrDRcxs70s8hTcd4WCgtM4O_hASiubRGOVAWaHMcN2Rxqx-zxdF1rjuFqah0dUoBRMIzflq09Y8GPkvSf6KC-BOsTD1WRiNwihJFjMKsgAWXu1svuNukiQnvbzEqNJijvoFHEr1CHFChP-z-yNB3AlpS-Hz7nThqriyp1QFmxaF78UbhDOVM1SJyw7wAkrEtFPB5hmhthRyG8IrmI-23dsunHcOH0-rl5MfqTz1eVXI-WPap_MicHQP8Xem2Ecv1-WvyvSysLJIKHtaT9s7JdWJORFOQZ9-ihXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=KiSCuhElyGW5dzSVCyHQp8rDpOyfX8BACasH74ejZttb0wEG7-RYrDRcxs70s8hTcd4WCgtM4O_hASiubRGOVAWaHMcN2Rxqx-zxdF1rjuFqah0dUoBRMIzflq09Y8GPkvSf6KC-BOsTD1WRiNwihJFjMKsgAWXu1svuNukiQnvbzEqNJijvoFHEr1CHFChP-z-yNB3AlpS-Hz7nThqriyp1QFmxaF78UbhDOVM1SJyw7wAkrEtFPB5hmhthRyG8IrmI-23dsunHcOH0-rl5MfqTz1eVXI-WPap_MicHQP8Xem2Ecv1-WvyvSysLJIKHtaT9s7JdWJORFOQZ9-ihXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15480" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15479" target="_blank">📅 12:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ادعای فارس: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15478" target="_blank">📅 11:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=NwXi140rS0rs24Ql-K3fLVRM3dYGkPRDvcA6jC4gW2Nl3k0ZxRVPF8-wj4rLXytNpJeVUyTt95x8hyQ3AtdB51Gg_7Ksx3sPf081kuv4ieUg7DrxdeztKk9RriFRsMh_Tbj_7kptr-8WE3DCLDneCQ1bXxBd9TKnJwX7OH_V9sZALF9VwwR6Q12EDUE0uAvnq6St35D68JdUMWs2vaOs2Wt0CMN2heHIwU-ap-ZAkofhtSYgsr0dCvDIgrm4kH9bFIBeNfL-XcPYCPnFjRLBteJVkarl9vLcivRzhcHf_oZtzlHUY5mUo9-W4toxQV7jRSWmG-lucBjgwNhMwaHlUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=NwXi140rS0rs24Ql-K3fLVRM3dYGkPRDvcA6jC4gW2Nl3k0ZxRVPF8-wj4rLXytNpJeVUyTt95x8hyQ3AtdB51Gg_7Ksx3sPf081kuv4ieUg7DrxdeztKk9RriFRsMh_Tbj_7kptr-8WE3DCLDneCQ1bXxBd9TKnJwX7OH_V9sZALF9VwwR6Q12EDUE0uAvnq6St35D68JdUMWs2vaOs2Wt0CMN2heHIwU-ap-ZAkofhtSYgsr0dCvDIgrm4kH9bFIBeNfL-XcPYCPnFjRLBteJVkarl9vLcivRzhcHf_oZtzlHUY5mUo9-W4toxQV7jRSWmG-lucBjgwNhMwaHlUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین رو به دولت ترامپ در ‌فاکس نیوز:
بس کنید به خراب کردن، بدنام کردن و زورگویی به دولت اسرائیل!
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15477" target="_blank">📅 11:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15476" target="_blank">📅 11:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رادیو ارتش اسرائیل:
تغییر بزرگ در سیاست عملیات نظامی با محدودیت تقریباً کامل بمباران در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/15475" target="_blank">📅 11:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15474" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مدیر دفتر شبکه المیادین در ژنو: دیدار‌های دو و سه جانبه در بورگن اشتاک آغاز شده که مقدمه‌ای برای نخستین نشست رسمی میان ایران و آمریکا است
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/15473" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15472" target="_blank">📅 10:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/15471" target="_blank">📅 09:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آمریکا می‌خواهد دسترسی ایران به پول‌های مسدودشده‌اش را فقط به خرید «دارو و غذا» محدود کند تا ایران قادر نباشد توان نظامی خود را بازسازی کند
روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/15470" target="_blank">📅 09:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک جلسه اضطراری برای رسیدگی به مناقشه بین اسرائیل و حزب‌الله لبنان به برنامه اولین روز مذاکرات صلح در زوریخ اضافه شده است
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15469" target="_blank">📅 09:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">معاون رئیس جمهور آمریکا، جی. دی. ونس  وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/15468" target="_blank">📅 09:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15467" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15466" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: از ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15465" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بر اساس آخرین اخبار، ساعت قلعه نویی در مکزیک دزیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15464" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=vCE2C7s-2PWVEpr0R7vq7nWi73ntfQ5iPttpJjUcM8wk9FZU5NsZ7p6l7rsyV4j4ucSv2ITCKu3UqyWbQfS43X98Umukk2RnZHbcKxgxPCIhGI7dEvvPDW98Sr518O_8GJnXUcuCcbgNDP0g5irwiCOQdwNMBfb-rFBvbfGKYPzZyT6JrF7gOgmbKoa9DV8aCIeprJTyFNucfAvR2XINHKDCqKfHLGMPWXipi1T4Ffy90uZ17KjD7CkOg65XH-NpiB8jaz1mon2dqlQbqCncv_2rmX49INeS2Tq_Zkm6c0Zh3nwj5_dzdTFEuQgb7vM_-ABTFn9lFFy2-lHWWUZQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=vCE2C7s-2PWVEpr0R7vq7nWi73ntfQ5iPttpJjUcM8wk9FZU5NsZ7p6l7rsyV4j4ucSv2ITCKu3UqyWbQfS43X98Umukk2RnZHbcKxgxPCIhGI7dEvvPDW98Sr518O_8GJnXUcuCcbgNDP0g5irwiCOQdwNMBfb-rFBvbfGKYPzZyT6JrF7gOgmbKoa9DV8aCIeprJTyFNucfAvR2XINHKDCqKfHLGMPWXipi1T4Ffy90uZ17KjD7CkOg65XH-NpiB8jaz1mon2dqlQbqCncv_2rmX49INeS2Tq_Zkm6c0Zh3nwj5_dzdTFEuQgb7vM_-ABTFn9lFFy2-lHWWUZQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15463" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
