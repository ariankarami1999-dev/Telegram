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
<img src="https://cdn4.telesco.pe/file/kBp2hlhP7nNusbHDRj09YtrK1v52AwtOaWJ2sh5w6V9w_OTxWRgFE-yI4f_zrqqY43ZoEsnTEoPReXrJhlPPOdZk7VDmflUtzfCsLPrmyNHDqpfPYag2qapdajrZN5lbMnE99lPN5Vw9DcOQEQg0CyGyIHBZ8pK4-heW7qB0u6v6xXB6TynoDnDgODIeMxmAVCX3Prb-vHmAsIjXJyiUi9Y96Qo7i2TJXYcBgGxZN5VXLrDio9m8-sSbC5ADmtR-sDUOpxrAsTBxA6ytXlyKTTg6qQgtFnY4N8o0uGT9UO1dYX8xRFZ8W6LV0T3bgOwA369cFzpESx8KjGpd7lFtVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۶ تا گل زدن یه کارت زرد نگرفتن</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/78155" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلر کرواسی رو</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/78151" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc2oQDv6Hmhc05dC0W1DgUYFIYqaSD6umYcY5V9ivGDJoVeDtizXmrNIqURyDBKVPYgsIpKqQ1UXcDkQ3v4gCCTTl2vdujOYq0j8gSwMH7rAZqZbeJnRoRs0wRE4spZGjsPeCVVwmj5vmlPpNPoC4_fSCwE-j_gYx6rjNI5KAIABLFLNSSCrTwSLzrvNy8GBw6BiJ0gFfb6xtn7uLJCUCzQM8eT41BGIeKSdzUxOwWKTKk5KwGxbu0XYUSuAUIwUeL_1CdylSYH-w_j-Eo9tDPf68JcURtYPYCPYhxAa0hOrxRvadIhQOoqB_w15mGe3yQ4Y5h4s7ULLPKR9OMdgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt8oQvlNambHC2bR9ooMLkrhSZymxmVR5cLJkLozFCO1SYIjz31tDIsDVBkTakausfkilaYYL9Xe1ijD2WUhr0EjGU8MzfL7CuOtXtMYEPHq1FZgvDzpH_otrE_lPhlLFQ4yI8nPeK7knEN7VqMYyeE6zAGhczkpTFtT5NhO_AKM9U9SIZDnJqXILWcP4cdqUasdf5vVuSINtwAuI3ltxaN0FL4MSVzNvZjqX8fY8PRx-SgrM5OTZ9_DyUzzXvgU7JQR90cTL4Z9nq9bfSta5w1wHEjf4lvkzUht03xCVLgZBctkJTzOLhyMn3XBDj6Fm7VR7-fOW_B-AwArzS4egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Don Toliver
📌
Octane
📌
Hardstone Psycho
📌
Love Sick (Deluxe
)
📌
Love Sick
📌
Life Of A Don
📌
Heaven Or Hell (ChopNotSlop Remix
)
📌
Heaven Or Hell
📌
Donny Womack
Enjoy
🩶
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/78147" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxGyPkAkw4sP2RadGzBHQyq_4j8fdzqNFPKCwtmUbSh_OxEDcSb7wWi63vI5PEhPvCz1e3RO_c4kzVrae7kaot4CjYVP15EKyOWb9wWxewnVZ79Zl3zoIAbSo8wOI7srwk-SSG1Mgafs9G2R1Plr0oyBToXkPhCKg125GTGTuvy_m8cTExo3oIjxcatLuSpcrZlNfVg16WipFSib2LCQZmFVeVN1nQnkdHaaO9TXL1EPsQ3E5UQ-p5TPbUtPtnoCo-9Jcub7fJt9DPZjzgtGwiQxabQcPlcVvyxhotXDP8i6bKzPXurGHA_Kq4-1twEzZmONs_sLICocvnpweLlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=cHAHqsTbg-YnpUjF60UTXDyD4mmFmPMmVy4-D02YtcHOkIo17Jix1O9kMkaUaUN5U-M2kFgba8BmN5zJK-VhO9t--YG35TCDL455H6XwTd1JBOlEnuUoLDiAvvqyiqOcByzIfpAmenPtftSfRUV7GAFVk1BUPeNBb5O97pi6T7KZ88x3hedQEz18r7vCyljhXmzQzjlVuTVHNGZ6047E81BzmBX31nnd4ioVeBC1Ik_QhFpcw9zmQR2IHST56h3LZ2TEhA9MJ7ERThuWdO-TdOn-Uk-R058tp6qYUR3QnxskE9fNZgTVifRcy3V74t6MlI31x-sU2khk0hG49EeFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7FBa0YiomJYnVZyTEKYhIZ2JCcW0OcuDi3RULWy74fKu3TJPq0CoFnTQNtNmH6xSElxqUXgYUn_yxovGVxoXcKUG38N-j-i41p1J0KeCYVyu6vo7cKNSCFvGOfY9B87ttEBB42YFldBEoImgsHpMKLxD6THbT7pBLP94dik8RFmKTKYyHB6JyplsiMSR6sHWcjqkHxUBKlHI7dm1_Nh2Sm7YUwCpZiFexCk7XuaX2DNv5q0Jc-4wIBh35Q5uqu2wwe8LpJ63ONDq_r71A8cD5_tm6kWbcF-4t4uISz2LD20niz0GKCqYX98hb9-ZykBFGwIdMTxEAGvBXIMcdbBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همون بهتر ک توپ نرسه به رونالدو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/78129" target="_blank">📅 22:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فقط یه رونالدو فن میتونه بگه ترکیب منتخب بهترین هافبکای جهان نمیتونن تغذیه اش کنن</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/78128" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بعد دیشب گفتم شانس ایتالیا از پرتغال بیشتره یسریا به کونشون برخورده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/78124" target="_blank">📅 21:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تقصیر رونالدو نیست
گذاشتنش نوک بعد یه پاس نمیتونن بهش بدن</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/78123" target="_blank">📅 21:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رونالدو مادرتو گاییدم پول منو کی میده</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/78122" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxh9wQdzZ1qROUAzkOQcbxFgnnNMN3Jx20kh3REqX1z26FQgDdTDfPIEvaV9-x_NG2_VgyNNoTXLOXBLnZtDfhqY9g23X5-MQmCccrVxas02JRB90wPgYAz_7CH-Mev9f147SaD64oktRTbTHQm7T_BfFERkPRQZFKV3rRzUicrgHuwamBndEILivmAXgAZtZ6ifW8qNgk8DG2fZ6Of29TPLHPHK52E6D76e7x5ZuvcuYAlaLqGLrrQPJHQnyFxn5ezbX4JeQBSC-Sn7pnr2irFbzziyQ1KPyOmn10WC8czjzt56020jZT5eQG3JlcYPwjuDxabtIFOkKhDP5QDBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=i7hjv01yMOnVSSqLAsMMyH6g8rEkHv-c7FJJIpcis9ulY5RtP9InCPV-buoYjpS52RRE4nGmCGabbPdewnmL33QSHRXDmD_LO0tZfyQHyTUUbesoZsW1Lf51uMAMlFbUs9GffNwU7PnJZoWoHDdkmkGm1Vh-g6gpPWrE-GJK1KxM5dxT1QuBRFiQFz61AeKD9ljTcn6jlSzsxrZF_nYYhEtCSldkuy1uZD7sU8XeT0xUXec9sqkGz7PqjeGnZz3k6Hs9wu7QNTUJ0o_1yWojjM2RVxEYYmGNAB0cAY7ldgzf6OWlF5ivJ27ey0Kh9exNHqUBplVFuNm0jjJua4Lziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=i7hjv01yMOnVSSqLAsMMyH6g8rEkHv-c7FJJIpcis9ulY5RtP9InCPV-buoYjpS52RRE4nGmCGabbPdewnmL33QSHRXDmD_LO0tZfyQHyTUUbesoZsW1Lf51uMAMlFbUs9GffNwU7PnJZoWoHDdkmkGm1Vh-g6gpPWrE-GJK1KxM5dxT1QuBRFiQFz61AeKD9ljTcn6jlSzsxrZF_nYYhEtCSldkuy1uZD7sU8XeT0xUXec9sqkGz7PqjeGnZz3k6Hs9wu7QNTUJ0o_1yWojjM2RVxEYYmGNAB0cAY7ldgzf6OWlF5ivJ27ey0Kh9exNHqUBplVFuNm0jjJua4Lziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6FXnXhFjYugzVNfbbZ0_zBnbkKpscUwOhytealOizezG43kpRG_Wh3jEVXIq2DuxdWfmVlxp8ZKUsX9jfWdHwyU1mNTlWxZllLvSPSiLW54Ki9dDwD-ErzGmfHf-Ifv0ySgn_cQPS9JjozcSKjbao8nPOdLpG17sh0VKZzn9oGk0POhJkuoCLweSGxOem1oSSZvDEJA9Qjoqpmtb8Ly01y-qJpochw2S84JdLoIUKJhYusmpdJKdtCRV19vPUIbrV_J8sWuFTs9XAegh7RTkHTLFPgWAeyR6QodJarkzcE_mD96nVKkR7yZFH9mThAbm-70j8aU18RcDhQ_sfSQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9tk1V1cYY_l3WkTGk-ZZ0Fn8OJxdgfUW-vT5S3O-OvPfe1Y8pcpkfsr4EEHBP_yF1UhrN8Zo7JkIWdKL3F1Gu_bmZPXkPrUGTROOWAkS_8m4ajZwM50pw2iopa0UZs6CrYX7zIdODrmQfnaTSgcV3LuqAVeXWZorxiaR_e8SVRmaw6iMrwLM6Mb3pZMHMjKgM1NWxpCr_mW1mkEYhDvP6I_AM04TmxnNrP0qv9AzYsGQCg6TihqoPjGuaQUQm87SR1KtZFxSQyWLFqiFcQSigyTWswOovvkK6UQSlmsTiqavXoUEMU96R3gIGmngX6X3K_Lu-kNjZoHf7vnqmcjcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB-4aeZyX8MV5_43F41SuCDSzEmGEgtD24WeiDVpW6vAxP5zx8OENpgTE7n9BXsi-8bdtsk0sNjpzbQpNMeGwfIFehSCaYJXv1KOwfKSY1FcX9IFpBJm91PUMzNnLzfztiFFDO7rmnF6idMzwdOMnKSmu65zkrmuq79JMxMvTAzzNAnqDTPVVEjEWdS-nI2EFNE6kuJZyl8Ugu1_qs36kJntiNvZxOHM0vcndHBjyCltPI2rBr4bq6SIVKyvb6ZtcJhoJHQJxFcAzEtw14NRd7moLc_P9lHkGzYtX_e6gtL3DblkTghzbR8vOQV2JyPUUKCo7fMWvucqKScJiKv4pQ.jpg" alt="photo" loading="lazy"/></div>
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
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu9lJP3VGcFq66ck1sI9OfDqvqKGMLTv8EZ8uzTC-CYQCDdz4Obx5vbNi44tGZb_AgZL9GRzAU2hY9XeTDU5HcGLFO3KNlUPuuDj3kNmqvGEH1ICgXCd0G_8pbpeK1G1YSXc3_RoQt3GBQaitFDTXkXq406P_44xwfjSi4NEDMrnqhsppqq2WCgv38DapjVzhZehhX3tJuKNisF0drtPsHbjFJ1HvoF2ikr7MwVC1gc678dS2pCu7lS4hgWQ7mwZhbUZ7iPOK2s9usEaXwNaCgp9w5meKj4V3RmuK71SIWUK6X4bvTWvFMTrIoEz_0gWXtUCyICaeXtsAoBbaGh5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=UE0nhpLyhbG1dlLRS1cbeCFB-aaCcRAVVc_XqyiZuUCCUoxt-fig-bJIGtAokqXeLJ9ipqU19vhpKp1n_l4Znxh_U3bHwiyxd_YeCGYwCrFeqwRGMPkoAUYRt1EaJdxNJB6TS9yAZyPJHbHfLacdeB85YwMPJiG2zgaMXz1SjJH0xb-hK7xk7vzoM5Huob8XEYwAN2s92JR16LAfkZeeivIW2517NRq7M9QdTQVUfZGVAnf9d4tm-iSFjt0GSoHofsC5wGsKcIpx6Vd5GAb2WS-YiHgSq7lYko3HRp_7e2BHEhwo1ndvLM9LAvmBso9qqAAPxe4FSkCf0LniOagT9IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=UE0nhpLyhbG1dlLRS1cbeCFB-aaCcRAVVc_XqyiZuUCCUoxt-fig-bJIGtAokqXeLJ9ipqU19vhpKp1n_l4Znxh_U3bHwiyxd_YeCGYwCrFeqwRGMPkoAUYRt1EaJdxNJB6TS9yAZyPJHbHfLacdeB85YwMPJiG2zgaMXz1SjJH0xb-hK7xk7vzoM5Huob8XEYwAN2s92JR16LAfkZeeivIW2517NRq7M9QdTQVUfZGVAnf9d4tm-iSFjt0GSoHofsC5wGsKcIpx6Vd5GAb2WS-YiHgSq7lYko3HRp_7e2BHEhwo1ndvLM9LAvmBso9qqAAPxe4FSkCf0LniOagT9IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78096">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اندروتیت ۱۰۷ بار تو یه صرافی لیکویید شده.
الان دوباره رفته صرافی و شارژ کرده رو بیتکوین لانگ گرفته.
اگه لیکویید بشه و پول از دست بده، میشه ۱۰۸ امین باری که اثبات میکنه تریدر خوبیه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78096" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=XqiuxEHN0Sdtf5kZuizvcXZc679Vl1H_MxnKd4uRzQIVEab8o8DG0evDX753bxQ-QWNTEtsYumjsHeb0WCoGGXTIdZ8BwS4Jnhgdy2zSc-cfFhJDIQpRMz4WSpy4CCF8ltMAQxQ-MyW7Ng_qSsKc1sSgZ86RTyk-4nXdZDIEKrkDdbPjloriA9jbALNo7Ggit6PhCPr7-t6cw3cfX8Tsux66jqEs8aCn_YDX07fvvt1Wlx0DjewyEGak_Orl8dxAPmxQZqXSP19Uuivtm9KckZXPWF7J9y88_oFvMpuNEb4iqSMl5EOdgo3jFlcN4--tOVHLU3HRKlnNDDdQIE4VmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=XqiuxEHN0Sdtf5kZuizvcXZc679Vl1H_MxnKd4uRzQIVEab8o8DG0evDX753bxQ-QWNTEtsYumjsHeb0WCoGGXTIdZ8BwS4Jnhgdy2zSc-cfFhJDIQpRMz4WSpy4CCF8ltMAQxQ-MyW7Ng_qSsKc1sSgZ86RTyk-4nXdZDIEKrkDdbPjloriA9jbALNo7Ggit6PhCPr7-t6cw3cfX8Tsux66jqEs8aCn_YDX07fvvt1Wlx0DjewyEGak_Orl8dxAPmxQZqXSP19Uuivtm9KckZXPWF7J9y88_oFvMpuNEb4iqSMl5EOdgo3jFlcN4--tOVHLU3HRKlnNDDdQIE4VmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3mr5KaO01dZePqUTotmFmirBWY1UPslLJ9EMmp38LZYpW5l8UAn5uZkYKJPW4Nw7PlcIuquT-AOVEfnc8_4-A9GZIJX9D1Rrn8d1ffvmSd7b1RZkY_QXSvlE93dvrunTZsJ21vPR9KSHVKTJ21FXHfJBveRsGulsNXbPGoqn6trXODt9P28lj-K0vgwAS1NLwdXuPyAaGp_xdoy4Bziw14N-WzDgwIb8uS_Zx95ZSARLQtj6gYp15AArBv9QrKnCYYIvs1YV83nv2jq51OAMp8fSJYZvUFUWoK9hHYlmn1aLSzZjZuA4e0YWsfDdDzo-GxYIrhV085JSoxj7QEbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3WBIInFxVeEEL2UA07DoSnLO2sKIB9BPdP76TnftSG7WOJ_7Qb5zMlFKjfrj8Xlxl1bptSxSRGxhocYa0tab4CAC571OLa3f9HmG5VyDaoNawf1o1i4bZuMOESzYmtAnbIE9lNuJnDi2OSCJD3CFWaQ-16m_uiQ-bKlak9sU4smw8YIVqp8g5GaVNuFwRbccl4htb6zwr7oKtwxWVdfPEK1KtU3sjx2bikaGjUacODItgy1DXVuRp2hqCJDNBPkDXlBazeszPn4nPRKZqDxuZRR0yDu9yijard3L4M86d3XRiEreuTWs2Ih7oUN933gSNFv_2iWkDlvO2MB8tfrOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY0pW9YKjxdi88fVXkRzm--BmiFl8Z-o9t-weDqoL67wz1p-ohJcU0PjoD_63b0ccAxey4pRVdA3C56onxZX_oGYKFpjZQwh9wk5ZXqsmWqj_iR_Qdyw6_wAlWrXHSpkn1ni6qQjEhZEQCFggApcRRMGAhpXz0KXOGE75t8JIeqqpGrKefYyKW0FDkrg1ioKORi8qSzTAQI0hpHSyQI0719pa2Xvh6KWaZiDcmnI_IRV7F2_QK3muNHSp0nXIoyAXFxO7vjuh4H3oOcScY7sjNPHTl3s_c2jMOJk0Ir5UpozizM9wLbfKuP2lgc_VFZBzxpmSjcveIQDoJRlL6FW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0le4qfJ_Z3MbL11ZQhkWddJRTTVdkbWTBBFx2B6oMD9AD0dVhYgJnlijKtpBqvrH1zQoo4jB_s8h2xKEUKcMyFksoWHc4-c138QyeX_csEaQgmjtFoEwdzhegVTG2xFetaVx-APe31r8Z2ROTiJncNydN9pUnB7H-O_lzThLNcAHvukHm_D3Lid6zp_WKz0f8ymu0mBKajqGZm0cSXM_YnrfbtiCJibh25FoW0HVcrdsjvCtho3CldwF--plQSFbJZr9F9fkELyzzmxdF1uzWirfnOj4R7rmBcbzWNnJ0qhaymK7DiZdZmavjjzyigoHPpXhiss21hAY0M1oR6oNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC35lJKy-vuwGBUsa866sf_5YzrazZZW4NpKshLG5CMwzm3IJbFp4UxYXmOW7qsi3t-UwRyE94zTqBKHAYJCDFKEqFqrijoNhA3kfTl0rUKoXRcQ9myo0eLKxg-lZuawxAImDTHWpaBNv3RB471G-mYR60g9fWREE_W0dRGIUyOkKNF9n1zowBvEkoffi_bHkNpQmB5V3FzvtupOMl6bQ8Qkt1HqsSB71B87UXsiPBAPLAUwbma90y7-TRPuP86VJjJU1b9kTozetVRR3Y8CDcrPawe7fGI2CAAAVXIuOKcMbYF6Vbch5ZONlyN339z2i2gYqJXQBEkBYN2CnnZS2A.jpg" alt="photo" loading="lazy"/></div>
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
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrOleftARbiIwnwGtBc9gKHuXgEgJVab2z1jLVYZ9GPhTLXdc20NM3RsScNZTWAPtgHSl5kHuMv1m8IsrgvHHHW2p29ati1JGJtwsm_xtRIg4mK4HDUpks4Yen9ZhTelA3ANbR_TYSwELuaZ60-ism8rVtZct4pYA7eQPP2j7kSqfkvdMnU3l6hiJSe3oBxVz6hTZz_psn_3ivRsgHN5PP6DsoBIU7c4iDtCEXDphc-GCh1OMLw0QG-zpeKRGQZdQ_u1JBfhG6PbWhFgvm4j0siP-5uja8G20bsI0Flnujl_Oo0jh8Sm5uqcckbN8sPXMkX48TN7ZnmZFZ_RdVCUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqPqsbit-oKzf-YQa8g35wbSKy28kcmtTnqK2Vmg9GtKxwEm23c-8R9lpjAtkGrIiPcZ3FGae_BuiKADkNHGpodmVk3XW_KJafBvNX-s2fvrMbrBYLPF7O70lWspIALfaizSRegiDzP1_sxOn2oClshnQxIWZ_GWQU7IXPOOXF3NE1_Ya9FKSeV0mfU0Rv_kMBS829Z9453sLstpFkw-v_dBoAlxDyRC5WfMmWr85ArzQQeyunYCQxhwFHo0fUMH4VZvlOgDJm_Dup7iSj5GsfTfw66_qnNc4NMfI09sFEqSh7jU01vHiKP2hlc5oA5pQDFtpEbDSK1wmuyF3BJM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rasWE6yfex987UzxolTOEtdw867nzfnsmCLfaG7oTx6LFHuDr0d9vZCaeXIrmPxojESyRXg4hBoK83gNYMOxddnqBUhIMTeLigfalVer_v7KIgtM_Uv9-vHYt6Q3W3SCCsAnl8B6_1Mol9dp8TmiBYdHOr-ldXZR1howtZCmgpzmyPEgpgMqYThNEwAjsasfyapT-lR4HMjLl8l3sjjLzUkHR7QIij3S2g7kZz1hX_3FbGz9kY22IFS2Ir-vIuuDDFIu4ToHetHQJS3pcgeKJC3kpmGCI0HPGPfDS9ZPGG2o1sPVZ_leJ5gu-pINqXAMmehcJe8IwhmL868PgTfOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9KyLLoxWCKyBpjX7uC4z49iCYyq60wqBwX7n2XNZInWtek6cs4L0IEELa0FKFz83_DeeL_Dv4kmLHUkqn_LyhiLBnXrn6bq_Cmu7u30oyMY95ZpcSjtADlvZu0NR0Qt3MfJYIP7bapymaGXrjiAe7q9F8RsPMiVox8scCgJgrVWDL7yXqZDbRbJo8W9sPsnoHIdZj4b1h07hVbBxu4fUx2H3Hrc54B7FrQxRMkIB0sTQZu4DC7qRbxDg0Fcn6Uvc7y5KuA_EC1bU7Bvc_qFj9Z0w-4Ml36bVkqJOGSbygYuBR1KUbvZUK713udI-rvG-B9Gdg-dxr0wpBPWF0A-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU--SKsF86XOG3kC7n98OP0388rlE3ekM9wZxwZ6M3c-G1xMvh1YK1PZFaxqdV--5K8Byqp769FfXKdk17KAzrDib5fgqnmmYwepSe_laEuseZVRL05iB5lt9N2LWjfNq9VlFlQks2fQzkH0Z4b05YRTB2JxbYKm3pFKUW27rvrNKO5KN1nNs1zLsoWnagdP0xYT_8X2HOiZdFE5aXp3S1NgzG4CJzXk1Y8voS_nUX15JPu0zxDqZ0aV4shLDbQjkI19tt5IzVzJdMf6c3puZTE0X5-jBHRtGq_na5LfHyX4T0Sjy4ImLomJEDiuqsGP4cBOgMA0F8T08ugEfhMGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYmJ-3HdjRwvfxVdWdEtxI08rfHkvmHUwiIjwgCDUhfbf3HNjMSVf-QHKrhtAtasJC0978Pvy5W22xaA8ZKi2SKMzI2-h_3FfLVmrHAqNfgvAUW-5hT7Z0oKZBHjY0w5RXiqeYF_9DnjFaMKTuk8KegkGyzY2LpMfi96w8JoPREY0arqdkbw_2u1QMPYhBLSwjd5DdyUnIwruM1CeH8IXQ7ht4p1dQikL3dOvNuPftO0063gNpoKhn-5L1_WZ8SDdCPcxATtus40pQtFJpA6vNs2-1TMRYoGHOANSfjJXlkpw7rqgzBml5UxUIAsTgxwAxaCa1S7pStZXhjino5Qyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZJCiw5jQEq9JQNepZ1BOmCQbIqfs5qKKD0b43sy2EkOBSN5QBmwykPZyxsElwGFqnggAXFffJcRs71ByWYthRvlpSMSPwN0_EMYsCoqMpgJDl8QAUSNdzz89IewR38ok1PD5Wg5o_Q1WSHko9UiJxPVRLZQ4FnZvEEyEuY9dHiG6FZ7-2FzsgD2_Utb8c5HLm6b3fN9zPNXHDNe2tydpUiyE3BJt8-rTqaJNUA4FXP1n9qeZ9sQUeIt2P7D6494kSdVAZRkX1SPF9kF9LaRXDp6lMQwHjGZRjSqXMpvZReD_zgzvltmlCHh15tvwtO2znwbwOfRjwLRRH_bpFSbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaRlC_M_PRYKR4RfzQDhahWg9IWYVwDxYfcJcrMIt9n6GjEJyG0qcja5ho6xLM8wPYLlCIV4OwbME87rx__WRh-JMNl48Fm6kHHefagjKmJLrEKnuRGlF7nBFH3xG2R_v-5gXsKldreC7BVzkgSfdSXC9ZM_51QFT52yax8Gx-Y5cggLpW8damUxfDZxowz8gpuMn2vsuN9gmszgJwc9Bot8-lIIU7rIpFYG8nRuZ3Gc0MQM1r-I-jBzx6jyealL-_B65Lq2CJ7ZQfBm64jVcxk4kWtJVvboYWZxRjTfZgz_RwJzivdV7ilNq3w1b8_JDpolk_5UHuhd7MW1erQZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixeDOZA6cR3jhmC1J-Me-cBZjUR1lUWsEIR4BUDfrdBm1sKCiXfIciNfF3rsIfOC3aynfGuYgAo8NyVQ3xMYrCNrcFXRjCU8YBieh4i6oQ2_yqhkjXcN-KCIqn8yAZvnTj1hw6Wo1QWremMXjfWuLLV-Lw39G4iENbuw4SUUd5cpJ2YI7l-a04WNIfnprRArYqMIveGe3V1xZYfqFv73iXoIEpfyvq8CC4sIGUrPTP0tuDN51b47faXRl2rsmJajPd9iR1Z0FmoCpdOJQb08x_PnFv8Ow9_rwtiSnnj_2_UDUQwX5CTreJqiLtdl5nsH4Dq7S8DOMmAtke9AbgML1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgjJ3qLno9BUb2xIOANZSbyijTky8Fg__ekoeE9rbctLtSlv_NOQxJoK6sifGu6YYjZR0KhwYejRAfELv2i9A3ChfqhQXPZrEUxjyhpjpf_l0nCxDZhiwdIoQID8uIGyA1Zsmj-PyVWnkJreCmOJ0ma1WXPrIP2c0bpxHklaLEULRb0uYTPGWahzUMYckR_RQ_d_MqmSmUxQfQz-_2j_J74Gz00LwzRdaxOs2dVCQlsDu7B83CyQ0WCecna1ge58VVvu1orDnakdmPQ5Lb72jxrZT0Y_CMswqBGxjSh2FXqoI1elWbdUcjXL97dvFTrEwj9gzb8BIhfoVmHJNq4ETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9l_giPf5CXNujFrYg9mxCrQay4Pl82FLYpOuGLsVmUdkKMNmueLlKLYwBYyDeJN0CX7pgrMG6IPHe6LW19RtMr9DY_mRHIQxq9-_GTf2tniYOqNqWNP8vZft7G4LUCW794iymxeySVXQX6oA_2Ksi1xJcaFj5MIAMAB552IkTx0ajY_wWy-oBxfjqxoigAUFn1bY8E15GtXL1v_jkXPEl10q4quZsFx3TX96p5n89nWyQBQD7MtAqs7RPB1njtuqW3boC9V8CtH3OyTGJG5dPvqc0LQGu49ElBuXr0mbLcuEHUcPDIZUU4P8JFFWZaqPRpFjymAUHOLogBsxwjDoQ.jpg" alt="photo" loading="lazy"/></div>
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
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=ZLoi93NK71s0BISEf9mzRclWibYpOn_3ExeCMe0zuhk2ey-Imxe-puOuDPWpzWiYp4mNYb3K-VCqj4w1UfV134I24yDjSShfbVHQ0v1K7dIuNj4_GbNO1kvtnVpNdQHhyv4qnLhjIFXCdpQVHD5fjJtTz2cIzp5bbkmOPEXi2ZBgB_YMb9j04Y81lN9EjLmi7WgPi57lJvilM7jxFWTrv6kwLHxQXH-sErmo6tFf2zFgT3-TgA3g3wqdxLOPmz1AXndE7BZCJgl64K--1AFH_2r8HfPlaPbOwivJKTpz9--rhW2gKmg8KS3gQ6aotb3nJZySq_8p3s_m0m2EVRGahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=ZLoi93NK71s0BISEf9mzRclWibYpOn_3ExeCMe0zuhk2ey-Imxe-puOuDPWpzWiYp4mNYb3K-VCqj4w1UfV134I24yDjSShfbVHQ0v1K7dIuNj4_GbNO1kvtnVpNdQHhyv4qnLhjIFXCdpQVHD5fjJtTz2cIzp5bbkmOPEXi2ZBgB_YMb9j04Y81lN9EjLmi7WgPi57lJvilM7jxFWTrv6kwLHxQXH-sErmo6tFf2zFgT3-TgA3g3wqdxLOPmz1AXndE7BZCJgl64K--1AFH_2r8HfPlaPbOwivJKTpz9--rhW2gKmg8KS3gQ6aotb3nJZySq_8p3s_m0m2EVRGahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOsf-x7j7rL6NetR6YFz6jYxyAxf64nDfwsdjBXM9Z2JSVQdyw1QyjhmuFZAkW0UNsV-cKM-s_tky51y6-SqEDZpg6VJ91DnseeET8H7jvwPN8LYceOpgcgGJ733sw2QqUh9ymlNARDkAGDFqz8QqyVOwnrUqui3xYfpqz70ZfGGTDQfMV2xBe3oHlgajj-iNn6sycrOPTHlPCo77fapzLN2jrG5uQzPLNapk8qOibsGSX4wYgFhkS50xUlMoUU2EbPs0I0KIALdy8O8Rg1HnkRAsdw_eztWo5igX01EJdV3aZapqdZmAa6SWvU2nND4lEzankiakVcoGRfrDJmmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=kwLhH_JAsfG60E_aPVluUEl8kj1ZEeelZXDjXxS7dqK-7mYwCNI7ziNlcSZaUIKwYXiYUfff8waRIvAEQw6dYsuSOe8uXU2Sjgk_cowlViV9mJvCDLp7J1gCqR-fX-aamN0-y4O_nztU93_gPiIbYsjLn3nqxcuRZoZ2lPipWuXwO07aVIy7DHQuSkzIPfcT5JNuvm5_bnZ0PZu5mL8uTTRn3kntj1YvCi2svKd1IIpiK9cKVFWPuYT-SALSg5rFgcjB-E1m_nIJ0SS4F4dioElZp_uDFunmm7UXbdiF3Hc2-FiKn4mH5Y_Ucsp2AQjcmPGts-eTpw_iX17uq1H6Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=kwLhH_JAsfG60E_aPVluUEl8kj1ZEeelZXDjXxS7dqK-7mYwCNI7ziNlcSZaUIKwYXiYUfff8waRIvAEQw6dYsuSOe8uXU2Sjgk_cowlViV9mJvCDLp7J1gCqR-fX-aamN0-y4O_nztU93_gPiIbYsjLn3nqxcuRZoZ2lPipWuXwO07aVIy7DHQuSkzIPfcT5JNuvm5_bnZ0PZu5mL8uTTRn3kntj1YvCi2svKd1IIpiK9cKVFWPuYT-SALSg5rFgcjB-E1m_nIJ0SS4F4dioElZp_uDFunmm7UXbdiF3Hc2-FiKn4mH5Y_Ucsp2AQjcmPGts-eTpw_iX17uq1H6Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORoAJCO2jm6MM2Bh-tkDeWTrWSH_okLp1Xa5WBRew8NvFSh7Uvg53LAYQ0iDJVbcjGv_vkIo5FWpsttxi-yaFEgqoty9xcanlITYWc3RG4wQDIqvXDSc7_Tu4dE3ilMI0GnHnnBf-m4ubRDwqNC1gSYAiSNCAHnLgFdzZOi3NW2d0kwG_KArfAMuqhfkrcpZKBimDDZdjFwA4zb5dRUOOArL1rBh9PtXL6pfVAuk1HwBItdAzCyBOph3Q-d-eQGJaGdRpoyGbCZ359NbTFIr8mavdmc245ir1wVkU1Gm6uOjq4tMkfWB-1BdwVI-BKLyDak4y2ThN68Su3XS6HDXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
