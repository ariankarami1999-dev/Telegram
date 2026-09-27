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
<img src="https://cdn4.telesco.pe/file/v4J_wmhnvi09g4PHGHxRke6JOJlFprpkYMSt1zDkpwykMfmF55yY05Fx_n5MifjboSFUPr_dKeFYVoAwKf1ldcWOmebw-MLgctbYFkUM29dxttgdhcA9KUTh0iVJF4ZoGiH4OENvQY5xrk5aQx_zR3C3XPiMBJIEx8omsYVykXF-32ZZh_KOpbolIv9yTBHz0_7gy0z8M5GnDG9er24s8-zc8mwjqhjdCg67dl2ePTAwyEpjpdW3U7Pn1QA0OD6lk1i82QbIq2FBzOeLENhv4lA1zIY63Ev_M4M1sBWxX6zZACZYpTrORaB3ZR9i1OzHwuIoerkPWGGFy9VufIc1xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 05:06:40</div>
<hr>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/84083" target="_blank">📅 03:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این باز مست کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/84082" target="_blank">📅 01:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxVWVEIB5tZl1djRwdvbRhJXD2EVDBe0vYdzt0Q-Zo8Of6dGAJ3M1r9MEb4rvIBpPxtnvOsAxBhv2ptM9VzApz6_j_q3f7NUu9AWvhv12zgsUFoVIzJUCaThvRjy3gXFGkjkgmnh6aQkl2stfpG6HbrG52gLMjjUxKRUdj4bPpohrV9ASjenjdIfl25SbbiJfMQ1sFraKe9Mj8C2pE2YASQvcLpB77XZoC3KK9i2EsqA5ofaEUufedyFgmG_xVvTTg0Z3emUs1xNp-nEvB_y5K01lSlSIp6EkgdJ4AAQcxv4tJPDrp_G6JaJ9jCjw3AuT3Hhu0g4B6RJM39OWD0v9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا رسما هرچی تیم اسم و رسم دار تو دنیا بودو تو سه چهارماه گایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/84081" target="_blank">📅 00:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تنگه هرمز بکن بکنه</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/84080" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkR2epQUmE598eI_kI-Qq_85oV1rIu8Yl32vFRmE1mvdCCQP01f_n1xcfDsyvx4HEIJugTv3SD7qjovT_bxGfKPI1jOLPTopp5sVC64Ymtz27BYNZIp9BFY0ZrmBFFx5q9sZiWMkdBMYX6KJjQYPjQk5b7gAMpI0Mvy7sp6aX7Sd7lRdydDq_i4_jY-lba9SFwi5KnQ51rws9vdkrdzbaE1vokHYhNroliSIs39i0z-AT0xFf5hgJhQvtD5d4zlKOt-wkKdl7Br_DnQIawHJ3exjR1JmMCgx1H3tqmDHAD391_tZJ4UhFIJ5zItHWjlMqAbpcxT1OpVffSWcbu45Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مترو مناطق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/84079" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کوکوریا زنتو گاییدم</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84078" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84077" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بابا کیرم دهنتون بچه ده ساله هم بلده که همراه با یوتوب از ساندکلاد حداقل بده بالا، شما با ۳۰ سال سابقه بلد نیستید</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84076" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0fwLv_wAnzm6chxvZTVt6aWWmxX4VTKsKLVAJX0KzegQKgmLtUjxIbWW4SiqzbBScTV5vQm47wkAm9HEz4YvPuDIynRDq8tMNozAWJ7tHc7Lg2K_NRkIF9uUdsypCyNc6gJEwQH7t6CywAvOg33X-7aIjQRfKuawGL99sq5SrALU-A360GH1ulEpw6DE8MKupGFs5iFiuFO5rOVhbLDbY29wwWzvAKyUssQtfET6nFHJZNCDYQbUFUd7bk5MAmzc_L-IXWMuK5S1FBzpwbWqKswaFXpzLOsedBVa0QY5gIq30JZzpRdTwdYwrmc-Z7vJ7PIDJDeiFYkjKxJDbzQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84075" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان:
نتانیاهو زورش به غزه نرسید بعد میگه میخوام حکومت ایران رو عوض کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84074" target="_blank">📅 22:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=b8H7n6VpY2ondTKHduEqcDEdD5nGGkqiNK_glrorSkquIgQxnzheorypvMkjRw1soqeXYNwxDP5P4_JX1TJmI8HH_uX2Fx6cKvk98DMT3VjFXDPUTE7xafGyq3dMpdCzKLU1S0KDjM7YXWqPQYa6soX9oc061YWaECRbgWrQIbNgy8rgXw_7iNEne7HJvIPf-2Xi4VlBRM1ARbGpx6fQD81yvUYmZy86JR5Sgw1KcT7C-3RyxsQsXSIoKwrVfDh38BQH0yw9x3zkgq3DSL_nTHF5S8xlQsJ9A0d8CDN-aEb5tQtfKJdL8H6sYuHORAJ4_9vrAyVjCK5gNWaLmqGxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=b8H7n6VpY2ondTKHduEqcDEdD5nGGkqiNK_glrorSkquIgQxnzheorypvMkjRw1soqeXYNwxDP5P4_JX1TJmI8HH_uX2Fx6cKvk98DMT3VjFXDPUTE7xafGyq3dMpdCzKLU1S0KDjM7YXWqPQYa6soX9oc061YWaECRbgWrQIbNgy8rgXw_7iNEne7HJvIPf-2Xi4VlBRM1ARbGpx6fQD81yvUYmZy86JR5Sgw1KcT7C-3RyxsQsXSIoKwrVfDh38BQH0yw9x3zkgq3DSL_nTHF5S8xlQsJ9A0d8CDN-aEb5tQtfKJdL8H6sYuHORAJ4_9vrAyVjCK5gNWaLmqGxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کرمانشاه یه مخزن سوخت خارجی F-16 Sufa اسرائیلو پیدا کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84073" target="_blank">📅 22:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84072" target="_blank">📅 21:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=mzu_OAbmKaQv-OeWBZtYo5o5izz42QDeMKHOTj5cc6P4fx2yrk-dvGemyH3Vd8o2j0pS2zXTgfHFE6GQfKF1D4IC_cDg8s-vhcDwtLhayW1v3JFG5EH1Vdl24ZqxDsE1fgeS14DfhbTngwcYOPoAkE_hxEkQYjZ-lYriHjHrFCIockxk-bKJpXiBVxuWeMk_YhDxg9wuVTBdiGBzWoLNxTmAeblSUnLJu98bQn-UT3b9IKVMLr3sNi_2IPLD4bUzEPX--fpqUihlxAyQmuXjlnU2OJ_W4HlBosG4XMkqYpN2EVDHizcJ-jd94dqhZAdxJkpIPNl74OZdpb2L652RRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e520cf397.mp4?token=mzu_OAbmKaQv-OeWBZtYo5o5izz42QDeMKHOTj5cc6P4fx2yrk-dvGemyH3Vd8o2j0pS2zXTgfHFE6GQfKF1D4IC_cDg8s-vhcDwtLhayW1v3JFG5EH1Vdl24ZqxDsE1fgeS14DfhbTngwcYOPoAkE_hxEkQYjZ-lYriHjHrFCIockxk-bKJpXiBVxuWeMk_YhDxg9wuVTBdiGBzWoLNxTmAeblSUnLJu98bQn-UT3b9IKVMLr3sNi_2IPLD4bUzEPX--fpqUihlxAyQmuXjlnU2OJ_W4HlBosG4XMkqYpN2EVDHizcJ-jd94dqhZAdxJkpIPNl74OZdpb2L652RRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا نه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84071" target="_blank">📅 21:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyf1hdgO_EO_BwFhQ0UgO8QFMe3UtTjLq022F2ZS6FjFJKFdUt1OOaKNsqGIWPtnXw_TUqCiqFL7GeWEg-TuJMTAnaxct_wetwQn30YEsL_ZGqm1JTztIHmmNuq8MZ_IKQzrRnAddb8YoZFnUTM02RvDppYD_-QISuR-iRGnIYgVP91h1R8toE6bClpIxRo5LyGy1otz3tPJuzxlPRHRDcvaU7ykoQk8XzVNs-jJoqObLhN4j1b8dWdAhPrGpGSbTpP-8TUiJFZKEDFdzBf5bJKnbSvWTqW5pqUfzB9PZSxm8Lw66ImXhGI7PMiqy1ku7neosyLBDgn53pl8C6Vh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا نه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84070" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه مردی رفته بالای ضریح امام رضا گفته من ۱۰۰ میلیون واس زن مریضم نذر کردم الان فوت کرده پولمو پس بدید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84069" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152539b735.mp4?token=MmpmhS2V1EIscqjxJ6jeR5a_t1Zp6oqVXyZUGWIHBdWs4BidqPjh89sj4utvXoxsrCXxA3NSRLiOWFfh9kpnSgD6FMk7u1PnyE8pXoUMZTMUtaKJMuKJ67NC1Mk1NtjkVTdxG5vgZdqGlkPHqkFc69Ngc_KhvKEz6ljyXZYUmhEdUn1MZoQgXtl5yT4DCj2NSe8nBB1D6dXE0jnvirl29ybPjjfOrWgvbUtaSLxs7TgAJA80M5nGOrrKuOkN8f6SzcqBRF4O8tuc3FvKXgZQIEma_uNvs4YDb92wg1EKPmHImMX89EjFKYTZ84ddE41YRbdbhy_dxlOH6ZRfigxPzUK_TPXgBYHO0H6Y_WEcsdkAwgj1ClJtyr3J-kcFl43nx79svBgnLvaxvk6uU2gIBlp4WthfYUZZuQch0zQ8qtBgMLlmv_GATAkhSeX0vnTsgopfQZZzS1OfT3RdgE7svWUI-NcQTiOsV4so3JuvOphRjKWGvDu7AT-UqzqeomXMw2v2VYZPBg1szrQveP8gyctBEWcCJ8vzgSIZnnfSaJc4hxmMesW5-lJ_lAobsckgAN4GugEFku8EubHqIu6WDRpzmbnG7H8ht90cZnomfyRZjbmNnOXYroHowvrdlZ3EnF70KpO5eyGlzgp9VxDajeqsFHXWJmlFUg_r_Rg_Lyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152539b735.mp4?token=MmpmhS2V1EIscqjxJ6jeR5a_t1Zp6oqVXyZUGWIHBdWs4BidqPjh89sj4utvXoxsrCXxA3NSRLiOWFfh9kpnSgD6FMk7u1PnyE8pXoUMZTMUtaKJMuKJ67NC1Mk1NtjkVTdxG5vgZdqGlkPHqkFc69Ngc_KhvKEz6ljyXZYUmhEdUn1MZoQgXtl5yT4DCj2NSe8nBB1D6dXE0jnvirl29ybPjjfOrWgvbUtaSLxs7TgAJA80M5nGOrrKuOkN8f6SzcqBRF4O8tuc3FvKXgZQIEma_uNvs4YDb92wg1EKPmHImMX89EjFKYTZ84ddE41YRbdbhy_dxlOH6ZRfigxPzUK_TPXgBYHO0H6Y_WEcsdkAwgj1ClJtyr3J-kcFl43nx79svBgnLvaxvk6uU2gIBlp4WthfYUZZuQch0zQ8qtBgMLlmv_GATAkhSeX0vnTsgopfQZZzS1OfT3RdgE7svWUI-NcQTiOsV4so3JuvOphRjKWGvDu7AT-UqzqeomXMw2v2VYZPBg1szrQveP8gyctBEWcCJ8vzgSIZnnfSaJc4hxmMesW5-lJ_lAobsckgAN4GugEFku8EubHqIu6WDRpzmbnG7H8ht90cZnomfyRZjbmNnOXYroHowvrdlZ3EnF70KpO5eyGlzgp9VxDajeqsFHXWJmlFUg_r_Rg_Lyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثمره های اون میلان رویایی ۱۹۹۰ تا ۲۰۱۰ دارن میرن دانشگاه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84068" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84067" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=DPUfgVwwqegvGYLrWQ2THQGUPq_YqNipSpkqzIhKheAQ8pjQb9CcZLegkDKdUN-M1cfE05YDT5eojQDnTCa5nDkZNNaoqtylshhJq0BPmkpftCAT6Zq_Bf8MvC9Gx7flD9j33ahZT8qiHo1ZmEE-NcY8FmxRzcq7pQCmTSYWEOWoMGDgoOaLGsvRBXyj39q1vc6nTVabPP4Gn-l13noe3t9wRAKB28VI3IBetCP1jXXuDR0y5gNZ4A-As4GDnVRiWhOZl7RlYCLWnIJ3_fKJ9pWie7TRsYJtL13AECsdLp0I_bH_axUWL5wKE_DxV9KGYbVc2DHm2PRS9OYU-xSGFZRt07TEcSk0HXjEQHQbaK_3Sn1rGFuGcJpnpqn3Ok1HZihD6hEIHDd99-UY3w4C--k1SaxUOjypud3WCd_gRFPxIFju1OuW_NbGkCM1yJN0aj7ijKdTZKyE68IEIF8ZUYr1ieLEzt5K7bBvAgHaadI9xR0STG64tv0UHb52GoONoFvDi5OqHkzVTaSifO3GzfTy5LsEY8b5XpQvlG_T8qkSg_b1dcMHMpxyakSTcwO3R--VLIEPlae2aWWLhuZWELwkJATBKYR2sCKt8mh6tbBdlA2JFQlVVsyeloW8UaRcqJAHy4Lshm8WVWg4jmi0MfZdnjZgP7gvC8CLTBk10gY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5a082c92.mp4?token=DPUfgVwwqegvGYLrWQ2THQGUPq_YqNipSpkqzIhKheAQ8pjQb9CcZLegkDKdUN-M1cfE05YDT5eojQDnTCa5nDkZNNaoqtylshhJq0BPmkpftCAT6Zq_Bf8MvC9Gx7flD9j33ahZT8qiHo1ZmEE-NcY8FmxRzcq7pQCmTSYWEOWoMGDgoOaLGsvRBXyj39q1vc6nTVabPP4Gn-l13noe3t9wRAKB28VI3IBetCP1jXXuDR0y5gNZ4A-As4GDnVRiWhOZl7RlYCLWnIJ3_fKJ9pWie7TRsYJtL13AECsdLp0I_bH_axUWL5wKE_DxV9KGYbVc2DHm2PRS9OYU-xSGFZRt07TEcSk0HXjEQHQbaK_3Sn1rGFuGcJpnpqn3Ok1HZihD6hEIHDd99-UY3w4C--k1SaxUOjypud3WCd_gRFPxIFju1OuW_NbGkCM1yJN0aj7ijKdTZKyE68IEIF8ZUYr1ieLEzt5K7bBvAgHaadI9xR0STG64tv0UHb52GoONoFvDi5OqHkzVTaSifO3GzfTy5LsEY8b5XpQvlG_T8qkSg_b1dcMHMpxyakSTcwO3R--VLIEPlae2aWWLhuZWELwkJATBKYR2sCKt8mh6tbBdlA2JFQlVVsyeloW8UaRcqJAHy4Lshm8WVWg4jmi0MfZdnjZgP7gvC8CLTBk10gY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند در فصل آتی فوتبال محیط امن و حرفه ای برای عاشقان فوتبال و هیجان
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84066" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حاجی جیبارو بچسبید پیشرو میخواد پک فیزیکی بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84065" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RogGRB34rEPoBNMWG6T4txf69jPJakHOGbwBs5JPbg1vRcBYfX8wuf8in-NSw45FWEr-7z1xGS73-0d6-mmBhIEJ3alVlBGvcpuOhZ_K1ekYjHQGuLVkedA-6wtKqNtLHhVkH9_LPG9OxJAsXPMGtHiymDsLm7a7QVm2jxb9XG0lhEbSOi_Yq0MpmhI2_BiAE_B995jpbfYQEKBOYD_fHmLlk41V-tYU-PkT-gQBRAvYJ5ic5WcCUTLNMAlvu6_Pxj4A1vBFQi61A6U05WwWyNkv5MFnrk-aqRW6N4QeodmIH-9H48eOPIEiS6uUpSbDg2CfuF1E1EnhJx9NQyqnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یچی جدید بگو پیرمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84064" target="_blank">📅 18:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رضا پیشرو و تهی امشب آلبوم میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84063" target="_blank">📅 17:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUvMVq0hKgjZW_dnetzYqWVcINYAfoCTcs7wBqva798lZxkG-Tbyd2vcUiLCfscVyXTs8Eh6P7qIETBmyo2AvKQa09MlFsKJPdxUZxsi7YXynNAKhDql4O-W-1cI0JqAJ9Iscv7tYMynWbPji7I87uxHd6AWNW1m_b3B5oLuLVq080ZqCaLB8B8GebIi7UdFGijwZJ0Eh_njaCqjKbVEX9pHLGkkgiQ9jxTmBu1XKSzA2ZinaZdzDglIPhedg0faYI-5as4ialeI8YRaKf3JMVgoAmIZr7iNcPe8FX0XHNJmd73YUYqVw9UktwbBlBjL_bWf0Zs1It4w6x7vlVN_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست بسیار شوکه کننده و بحث برانگیزی که ترامپ دقایقی پیش منتشر کرده است.
طبق بررسی و تحلیل‌های بنده، حتی احتمال تعویق هم ممکن است وجود داشته باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84062" target="_blank">📅 16:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">داریوش تو فری استایل جدیدش تحت تعقیب کمپ اعلام کرد بالاخره ترک کردههههه
🔥
🔥
:
انقدر پاکم می‌گن نشیبولوسعتاااان
🔥
او همچنین در ادامه‌ی بیف قبلی‌اش با هیپ‌هاپولوژیست، به او چند تیکه انداخت:
کونی، دکی فقط داکتر دِرِه
🔥
راستی فکر نکنی لندن پارک‌ها سیفه (احتمالا به دلیل افزایش جمعیت مهاجران غیرقانونی در انگلستان)
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84061" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اونایی که فک میکنن سیتی جریمه میشه یا قهرمانی هاش پس گرفته میشه، یا نمیدونن شیخ منصور کیه یا هم ایکیو زیر ۶۰ دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84060" target="_blank">📅 15:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ری اکشن خنده بزنید تا من یه جوک پیدا کنم و ادیت کنم اینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84059" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=sWtOOig3VhWsH9U1sluU2Dc4z41u4fmDoc2mM3nkBdgNmGwVgd4OeFoaJhmviUxse9RT9JVzumquUMlj5yAtSzIL6i9CI7HTJcbP_53yLVwKUWrn9v6I4osLZTnMDRbwbF284rb0sDjhT6Wf8FJStiACCpwFw7C_I23COtmHFZRpoIyz1HBLq8vvLgZGaHEK6Q50qxUB2VSR4cmzNDDI8jd7NoAtIqmLsgH8lfXS-YplOic7Zjpynr6FRNnCfEyoL0jmBJmrcwA_rfJHiiLNfDuRrTJeFKiwGq0e3TzYg2BdJlj8isZytWdXrXxyKluLhUYM_AUC-5mnAJLnwbc3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6696481c.mp4?token=sWtOOig3VhWsH9U1sluU2Dc4z41u4fmDoc2mM3nkBdgNmGwVgd4OeFoaJhmviUxse9RT9JVzumquUMlj5yAtSzIL6i9CI7HTJcbP_53yLVwKUWrn9v6I4osLZTnMDRbwbF284rb0sDjhT6Wf8FJStiACCpwFw7C_I23COtmHFZRpoIyz1HBLq8vvLgZGaHEK6Q50qxUB2VSR4cmzNDDI8jd7NoAtIqmLsgH8lfXS-YplOic7Zjpynr6FRNnCfEyoL0jmBJmrcwA_rfJHiiLNfDuRrTJeFKiwGq0e3TzYg2BdJlj8isZytWdXrXxyKluLhUYM_AUC-5mnAJLnwbc3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84058" target="_blank">📅 15:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=kkO5sb18jQwdYIK4MECDig_A2NrWmmf-mfdG2Ts0HxfDR5auquBlHpJ_uY-DeMjyB0EzsYyizisIraOqoB8RMqAsrHHkmPOXTYzERLEe788teqfXgPxxyIEcROGA6YxkpbHnJgFwHieSxjHgZ3BSpDb2KGVjRmTgFnRY2Gsgk53erVoWDx1CqtMgBIz1yVpXC-P_C8dU9RXOFu2_tmHvlTs3845gZmnb7pvPg7dAH5Fnnwp6tTHlgMVNuPaSny1l7uFUj9ja0tIDJfaKDF7a-jjZoua_xpQFy_AOKcrV-aZXlu4mtUiY9_BY0G2ESBtgPKnKWLPwFyDHUId2rxH0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd947a5c3.mp4?token=kkO5sb18jQwdYIK4MECDig_A2NrWmmf-mfdG2Ts0HxfDR5auquBlHpJ_uY-DeMjyB0EzsYyizisIraOqoB8RMqAsrHHkmPOXTYzERLEe788teqfXgPxxyIEcROGA6YxkpbHnJgFwHieSxjHgZ3BSpDb2KGVjRmTgFnRY2Gsgk53erVoWDx1CqtMgBIz1yVpXC-P_C8dU9RXOFu2_tmHvlTs3845gZmnb7pvPg7dAH5Fnnwp6tTHlgMVNuPaSny1l7uFUj9ja0tIDJfaKDF7a-jjZoua_xpQFy_AOKcrV-aZXlu4mtUiY9_BY0G2ESBtgPKnKWLPwFyDHUId2rxH0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84057" target="_blank">📅 12:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=ZprlLVkiQVqQf_TU4Y1jwsifoa_HSbhqJmuiloi3bVzgYAjupwsuR83ZgndLFST5TVJkhGlppXeiiK59UK-UB71-z4MHQwE-MSVWjHkbmgX2gmOGG_EqJF4YVdu7YuG0fRH5k6br5AmeiUwH_VbScgqbaCL5wH2dy3VuRaArqNzqU5ajk687O1dMYlHIivaNjrxKJlW-KpWo9cdtSAHkwF0eLBnDKBKWv4sYIcg4gQyxMKVct74JkBZ2aTPNFC30sKKK0wwEGUulvWxIcRQPfR4tuDkc5y5IJclVWXYBz0f5yS1WNEhIQyGdRJ0EuTK2mUVHdalriSuCaHHBTZr_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534ba3e4c1.mp4?token=ZprlLVkiQVqQf_TU4Y1jwsifoa_HSbhqJmuiloi3bVzgYAjupwsuR83ZgndLFST5TVJkhGlppXeiiK59UK-UB71-z4MHQwE-MSVWjHkbmgX2gmOGG_EqJF4YVdu7YuG0fRH5k6br5AmeiUwH_VbScgqbaCL5wH2dy3VuRaArqNzqU5ajk687O1dMYlHIivaNjrxKJlW-KpWo9cdtSAHkwF0eLBnDKBKWv4sYIcg4gQyxMKVct74JkBZ2aTPNFC30sKKK0wwEGUulvWxIcRQPfR4tuDkc5y5IJclVWXYBz0f5yS1WNEhIQyGdRJ0EuTK2mUVHdalriSuCaHHBTZr_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخیر.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84056" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نمیدونم این چه مرضیه رپرا دارن، اونایی که تا سگ نمیشناستشون عالین وقتی معروف میشن یه گوهی میشن اون سرش ناپیدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84055" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=Hurup6ihW9XHY6z-1zx1p24WOkPf5y3UNoeeKh2ULcP-jHHEjn3BI2OJ3oACCH0e--Wmvp4VhZj7eIcOAlvxXMUSVipjOsPmpxa5B68UnN_g6zWi_IK9ZboR8nTg_DvL0vm8b0GBYhXNZtIBj7JcPIxfJRUTpQpatdGld_skhpYGTrB1Mte6ChLI20zUZkwo04CbrqrLNDEuayF0U-seLFixhUWGUWAInrqN5XCeFR-kGPQRV2rQPirakyNH6X2bWx9RTNc--72NRz0DmF7Vj6lelyVt-D7kiMPO5UO3baUBT-Xc3_7adA-h2BD85aod5BltIOHjZnszox6_N24DVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=Hurup6ihW9XHY6z-1zx1p24WOkPf5y3UNoeeKh2ULcP-jHHEjn3BI2OJ3oACCH0e--Wmvp4VhZj7eIcOAlvxXMUSVipjOsPmpxa5B68UnN_g6zWi_IK9ZboR8nTg_DvL0vm8b0GBYhXNZtIBj7JcPIxfJRUTpQpatdGld_skhpYGTrB1Mte6ChLI20zUZkwo04CbrqrLNDEuayF0U-seLFixhUWGUWAInrqN5XCeFR-kGPQRV2rQPirakyNH6X2bWx9RTNc--72NRz0DmF7Vj6lelyVt-D7kiMPO5UO3baUBT-Xc3_7adA-h2BD85aod5BltIOHjZnszox6_N24DVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی: بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده، توی تونل رهبریشو طی میکنه و توی تونل رهبریش به پایان میرسه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84054" target="_blank">📅 11:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTtv78NdI0e794vYxmRaXVxRWaBGubb26wtzkJq237dltXquN_xWb5ZQcgs1acrnifOPp79hwWJLtKRwWlnyK6XKDa5YONjw0wUvjJTwklBMu_X4MnKLxz4r-mBX-uwfznoH1Gu8clV89YdDbS2XGI3WasMKf0ObSILRgoPSCuAlqFnXb2lz3lQkoVxQlrRW2ukXkOuETD5YF_W7gfkAwljRvZfwv2dhJv439BpHTv8WcKyUoyZzjgxABBLDoAQWZekPaGIUH50zbw2pns0kh9AhtjBi8RO9-cyV86NAWejX55R2UCx2yP7MGLN4Pl5VPCLvdfk4vJlTNF2OMqT8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shgy9R9PMF-l5vLPxhD3Rx2VKe6cqsp0DTfq4HCqVG-c38TRirnnW-I5ge-5EV-NjGib2Vhqwlt5mT9zktuoqGbbFP74W_EuvAL8W_TbW-WuNNKvDlkbj_9kE0zEjF_eEDOADuTA2XcIwjBG_JnA41uV1dOFNEqvi6azmO3VJTkckvIOFqqeDZXRWh_PJxkmROxgQtoKD6txVVMNyJv5wfp-t4Nk0yslkyoHRMzdgcXLgIWp2z68vAYIlOEFHZcL1jQEsIS3xVG53KeiZryVDBK_UPv3qYKqgh_j7IvlF4xblpX0lZrJn3N-gDWAVLZJUXP_IZYE2-PjQjrLZvt2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THknNDrVtADNpxfDizMaU0KiDFHai_eM69zJquuJchLixLu9ET54Mpw2djbuvd3ZM9Kk0AVFzVP7zePr2U073XgGP-QR6LKySuUyIuL9ttY7XHk8eYJekaQeGUaKccNj3fbyCCUhNO_sj4XrBjgIZg4P9zpgCjDqJMd4py6bsHshG3tuK5XT5SkVoD5YSmldGDbZ0bwhsJVA6rXc5pMh14ykQjC3lTy-N9__gvk1EHIBEshONEowElIADTMEUbHj67h5Xo0dUOd_rNTQmDMIeWJb12gkSqfjJsjFLYylCGGTw62i0n5R74V6h1ZJrICpFun9A-9Qbt5aYel0iuuW6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت بازی آخر بهترین بازیکن تاریخ عجب چیزیه
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84051" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84050" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84050" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flo0brBbjrBT6IDgC7qXREagEYu5aFVa71JeJ9KpO3A7qsprquLi63mgfDu51bjVs5LFB-Qt8scivxn1fHvnu-Hd6RDz_b3rgwaAhMGMLPvB6wxcCd26DSC8xyYUueICfqY0UA44SCEaujKs_DJFc-U00A62w9zbu0aXjBF9aXvqAv8nRyuOQQi_o0ljpLCp6lM1CluY9lcFWY9x2HkjAQ5mTOXakwPHySpA9TAzfWDhkfWsgKo-jmBD4VUKVdGo9Y5R2CXQp3lvhg23i8doMdB_TTTUlzLS_dhdc1pOKqxot7C0u_1PVF84MlTAQ--2lmQI4CcVap7N-lwA2sRLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r4
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84049" target="_blank">📅 11:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUmTY9oCUhE6i1Bq9G14yKM6CHRKXvtaoBsdzl1tIL_vAaigwWOHbHHnQN96IjUrRJTL5PaI3WkP8NkzgbTtTix9jLSsaUpoR5ZZsElGkfmQRGesi1UWxL3fvm2y2NXtON3MaV0RyJ71lO1-dTPFbkHIEX0UDptgCYiZJOp7kUWr1RUohTPdHA84YQgeiRKFbQhzjEx4V1QFmFcMABtiEsf3IbEhSQ6m2o0jNc0hw8xaJsWpyKWyH_AS0y0jkFihvnxw8LWvIkS5h5uhDh2KkEqHuQNfG6onSZf0Y6Q9-uBF9XuG1qGMEIA_1orfAv9fukym-vF5nsS2YO-5Kn2dKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا شیر، ترکوندی شیر
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84048" target="_blank">📅 11:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=Ly7jjwLFXp7k6_PTEZRCB6b4sv-0NpSCLhdR_aWoIQOzncVD6mCsI_sxtzX0NIa88_XlL1MQA9e6eA6IK20Bv9GZoBSVCJRESpOx5pYh3rV6xiT33acrZZfyYmxBauAaOljtsIKWj7WoiKqZmhI5HCK4uVJnjwPO2mjUaNk3jEIS0RADS9Kvw-B5nY5evVRQz_VJZwK-I1o3a1UuX9uU9cWT23qxX5yB5_IXmbHBRBICDnbYLDMhg5i1fpXMyBz44X2U-NSxvuN77pSNShSTwI4ntrwO9aB2Jg6X9-gT3BxYmFuJVwJOqQDIvp-c5J7f1QvRswH2Z4ZALpkWHDWX-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=Ly7jjwLFXp7k6_PTEZRCB6b4sv-0NpSCLhdR_aWoIQOzncVD6mCsI_sxtzX0NIa88_XlL1MQA9e6eA6IK20Bv9GZoBSVCJRESpOx5pYh3rV6xiT33acrZZfyYmxBauAaOljtsIKWj7WoiKqZmhI5HCK4uVJnjwPO2mjUaNk3jEIS0RADS9Kvw-B5nY5evVRQz_VJZwK-I1o3a1UuX9uU9cWT23qxX5yB5_IXmbHBRBICDnbYLDMhg5i1fpXMyBz44X2U-NSxvuN77pSNShSTwI4ntrwO9aB2Jg6X9-gT3BxYmFuJVwJOqQDIvp-c5J7f1QvRswH2Z4ZALpkWHDWX-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا همه خفه شید فقط ایشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84047" target="_blank">📅 00:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD8Ubz_lJ_i2OJQKoQGDIe0Ay-DeGRMLebPoLIPQbjx_-Y4XHwcLMIUnRRRVF22LPX24o4KxE9RK0Z1yYrv4xYFrG9oIt_cXq0dqoaRPU2yw0Ae4g_6u3mnHa3fh8x9dCPmRpXGyZ_GDe8H5Gsu3JS_kaBAlESfXyZshDSfUjGoUrVRj0YzXnbI_x-IJu5GzF5PdK8R_slf7rk2T6o2my8l6OYea1MRwZJ-cw7sG_UzEEdkr90Yfm4xO0wzSToSoTbEoWGDVrYV-iy0-XDebVR3KJ8Woeo-qkTYaHdIWMBp0IiDfkV_jSlZA4a1i37stc8d1ssFga-2fdDGjjFsxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84046" target="_blank">📅 00:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N15g5y0KSP1HVoin8i-gvIR_ooXT0ZCdadltE91YbOBwjK7rOoJqGAEBsxqjqTTOJjCCtQtz5FZgEgUzvl0FKVSLaPtqrMU05uF8j4bhu9MCXnJWmRQWDdarGWXN6emPaEPXdtBpVNphjWxnFYDIhjyuDq2LXD9aJlDtgvxRbMCdJpFkD-Kha32ftoj9gggTbM0jAstMcHtgubPzCz9J_cBL91lH0PAa6L2dxopj11zyeMRargQIP0ogQW5YsHw7O_c-vm04Os-18KeXHz5HNWUGcDtxgy34DZ2IuU0pmtqmtO17W5_4fCGVD7I5ZBi9VEdZOk9KHVmfQM60m6-kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-GhCjdZkdH_uh4zRP3kUhopoxakACwzaCyG3dTcqNZ9gflQj3hT3TrkzUNnFOb1v5f-4kDyZdb0JymOWmhNZegz41V5NOG55TtJpcyndcsf4-AH2gWBR8xt1LxLLFQV_pvcRiHK4tQWNU2EyZNREe5DnHRIVmac-Ax5OIx7PQH6cC-kowHqC4S6IZD9BRlI7malI_I6UYtPutGf1S-cVbCGu_0MOEnjZQumKMUrsrMQ5VIdxBpMHdaL66ysq5QiVnBxEBzitrSWSh3MxDLvV_QhD6rw3qNv-3qydVl_GteUS3CffT4rAMU9_-X2GG_Gv8Ruu1XtvTur3Tye5aCQmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط نزنیم حرف خالی
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84044" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAZfzWvWemmo7yLLcLT9Qz8aBgLetTMyveMf_hFfT9ql6kDPAUN5SdKaGMOCF_6vHCesKL0-15_REB8B0m9-3C5oyhg0awebLsBWEN4DroSbqFJH2nxeRROgzic7u6y8BnnffI6TRSiI6mIDxhd3qNsHUIiOUfCEH0bNFT5MVfg_B9l83g9H7rbn5Oruumr_EONt49d8i0e2hZAFrGavQH0OlBJOl9tAhQbzhXTMTS-9QYj4IhPwx1n7n0p-4fuPemvtQGk8dVpOo_XH6CCGFVoYJWTX4g6PyDr7IUhyFHMYcYs7SS2ofpf9xs46Mz_wOuhYEI3qp2C3xrmHGB8MBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بعد از اینکه پزشکیان بخاطر سخنرانیش تو سازمان ملل حسابی بین تندروها محبوب شد حالا بخاطر اینکه تو مصاحبه با فاکس نیوز گفت اورانیوممون رو میدیم دوباره داره ازشون فحش میخوره :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84043" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy-MYPifnsKZ74doXZfy1Zs0ScxOMLhPB-OfPmnUf5UdyOK2YWDA0lR8-gPHPxUVX_ZqSq03S5_wfL0ffuzA__2-jtNDQAb1fa4wBBQtSGFpjY9FOUJ9k_vGEZYfnbBdOkyxwrVwVFdZsPSPtqI_HbnCeHYoWEfXz1BwrVOdvGB4etJi-O-mcbNoDLzRk2iWFJH6RobyqwnqFtJXJUdz4Q737IcumQUaLVqoMw_GjWoI2TKm5prRnT5eNt5-87bihwn0JyXslq8S3hMzXa7bgTZ530Sus5jggENBWaPLPYQoKt5VlxX10VBaHkUHLsB7VD6QcvXZ7bv7UsFf1Zs8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی دیگه پول نمیده فقط یوتوب
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84042" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84041" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-PRbVyHXfwp2mGK9zY3noR9YRCZwuJvtmeU4Sfz9OJfCNR_G9C1GhtVHc6CdEeFCI7l0L6nR9wVSqJxi7PlWVxJO8LfRaoE-HM60a_n3p77TohFzdCZKhx93WNID1gkEnDcpSP2GKwf6-xIqFCdxw3GY7DcWPDglTeplNM0dbQUIJPayVFFAw410LwnkoLN_EEzGTCDetK8pczXFdbAOfdbkFEy98D_wDM3JSB3DCtC-R4EUi1qG3UrYvDukR6DsMyIkRW1AhZKUlSgG7BZyMds-6SMvW76PCdRTGIi4tjWzizrf1spaotDvT2-xdDP2j1UuJSFqPvjzOcJQAJnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84040" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84039" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84038" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL3K5bUtGA7vyLvOzosb6LWhDsU7WhZ3obtuNUg4A5XpfEE36papZ2H3ViCpK7qZyH0a2BEkKULm5K-jMilai-ZfiGfOZxDAiDUT8KkFZAXFQ5gjNkfBWOgfjKuEYXP7PiLlZrrOjkUP4KgvAgQNn3zHlQf1UhyEPKCmsDACTXth0FH97m-YpnREQ6x30tdq6ZBFkUQPDs_Qufk1HfUX7ql8lVABSmJA1ysfZ7mMlvbMcKpSCU9beUv6cpWBW9po2VMtV7zJ1cAkb-_6a4NPdMvQKsrXrINQ1Hn8j7IONdRzZZG4m4q_2V5BuCpglHbB-M_edu2c1jjaR6n3ja4twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84037" target="_blank">📅 16:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=EStLFZpkA7S5hCh772vdJAIhRa_iF5PGOZmtRi7he1IbficXkOPPxSqDGlAjZ2wxU_ZX4mcOi_uwKsjtDzXJ7SneNBduuuUVWvo5i9CaYO3PZtVsNVSkXmzP-RMfUSNslswy1Ah_RTmTK2joKpToLKF-gdaBD4e7NmK1c7YGpGGYXQIqbck6OgkA_BGyRufVABWS37l8rriufSjO16QTMtULbn1eGyOH9zO8ywtvvjwNgHMU5lNDwgVf7mqhFTMZhCaYpPJcvVN1Uyegu_O0pjdvhdgsojVEtyC4WPBG1kr6Jd9EN0ciD9DAKb_fgzWJt1LaXYbwoviSZdIKWM0mhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=EStLFZpkA7S5hCh772vdJAIhRa_iF5PGOZmtRi7he1IbficXkOPPxSqDGlAjZ2wxU_ZX4mcOi_uwKsjtDzXJ7SneNBduuuUVWvo5i9CaYO3PZtVsNVSkXmzP-RMfUSNslswy1Ah_RTmTK2joKpToLKF-gdaBD4e7NmK1c7YGpGGYXQIqbck6OgkA_BGyRufVABWS37l8rriufSjO16QTMtULbn1eGyOH9zO8ywtvvjwNgHMU5lNDwgVf7mqhFTMZhCaYpPJcvVN1Uyegu_O0pjdvhdgsojVEtyC4WPBG1kr6Jd9EN0ciD9DAKb_fgzWJt1LaXYbwoviSZdIKWM0mhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون دختر که دریک سگش شده بود گفت استپ فادر ایرانیش بزرگش کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84036" target="_blank">📅 16:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84035" target="_blank">📅 15:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84034" target="_blank">📅 15:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meogFLKU_L-OMcLFi3dL6LkkeS9hrBkSn3aTJr1wPTp0mDnuzy-_isGnjWclZjbj8w737awGaYV9dvIPQ5MWNrOaZHm1q8-7PqIZJ410Ba0vlWyoDUn7elwkWlc75DOB4ZzZ70snM_2XdoHxbzWHSHi9xkPSVZelJ4FIZgtOhJhAk5dzdv-cxj78pOkUyOe_bxRftHFzbRDKXotcFGUIsqZQwT3-J8UWHyKVVgkRmzm4z_ir88bark9R4Zvfc9HHUq5kr0TWpCMfpGxxfAudOI096iG6TQQoSQTMy_lsddcI7Hl25vVYHscwa_8YXbU69ananypPUsJ0DW6LM2bPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو با اون بیفی که کردی یچی فراتر از این حرفایی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84033" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXXPJQYiUIRygM-9brvrQDujGD81y6B7Ffk6n05ult2Y8tH21PXM2ZCTZLD4HxyzBEToLwrAahUOSMQdSaGKjp1kpSP32gWLGzCrjG_QemOs26ShulTr3IVm7eaNIrWASXanNLObx1xion6x72VfquHY5VljZnQATuHIi01TBYG6rLMGUnwBqGMfLLYYF0c749ri5O0V9RpUIJvVPUPqd5fxDJe9eov7Z0Jf85HE-Ag5X7sYIJhFbqYuzxVi3SQTUST9XWqIq6VXLtmISU9mBF7PgNnJ7nnZbt14nsAWlMGy8bmVjHyxXqpDdDIh76vtZSVYyzc-7sMC7CHLouYL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کصشریه دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84032" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لایو دیشب رضا پیشرو که بیشتر راجب کصشرای کنسرتش صحبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84031" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/84030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آ
موزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84030" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgQQbQXqWlqpTZC3TjRfUDhdo5LOeGFz5_ybNCohOdFrDu6KWPKqVySnnGKsmaRc6okV4LNt3jko9O0ivZsrIcDgNDl_ezkXMCaywwawFjZKtz-Ri667ucHDxAqZW3wOj0GRwUGSR6EHtMScxfnPs5_-nwR2yEtoL5eAz1lfmtfuX41aCXfCbSRlm9RZ3Ss9LeQNtzeAzco0vZlV0wYnorG-LD96USaOf56aYhpao18ettwTqmun_QOV-KGuV9A8w2jAvc0YKJtvESFq53chKBkK3qDXSuJad_eaRb8IRK_Y2aM6MXpYxTqWKARpUM2FzwD96717-BVAt7FwrIDWZIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgQQbQXqWlqpTZC3TjRfUDhdo5LOeGFz5_ybNCohOdFrDu6KWPKqVySnnGKsmaRc6okV4LNt3jko9O0ivZsrIcDgNDl_ezkXMCaywwawFjZKtz-Ri667ucHDxAqZW3wOj0GRwUGSR6EHtMScxfnPs5_-nwR2yEtoL5eAz1lfmtfuX41aCXfCbSRlm9RZ3Ss9LeQNtzeAzco0vZlV0wYnorG-LD96USaOf56aYhpao18ettwTqmun_QOV-KGuV9A8w2jAvc0YKJtvESFq53chKBkK3qDXSuJad_eaRb8IRK_Y2aM6MXpYxTqWKARpUM2FzwD96717-BVAt7FwrIDWZIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
واقعا چرا ریتزوبت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
ریتزوبت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
⚡️
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84029" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX9JTIIkq2fiE19qhqycwhv1_OsHQnJ5HCli7n3P1Hr7rH_DYTDwqb0e5CKLn-F8shMVZnqXiw6nMqK_woFLquOczZrl5TTqcP4rZOsNARUWQlPJabtX2VSwKrHFfsvhfngHqyW167dWAkYaCgMfAf-fAumQOK_lWVMq2AowJOdlOcOEXpbCM3YaDFiWMhJPkBNBc7D22ozXDi6eL_8oMPLZV_JNI7lhzdbcb2qnqBeo4goT_Q_ihp0J6qsVFVHgryhzieDoHjIsRCEQSlHDW3A_f_8qzlkGecZPj8hA9fqzwzkJuC5sXBxumMHH2G4JI66sNxqubALLVSCB1pz1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌همه‌چیز من این فیلم رو واقعا دوست داشتم.
الان با چه رویی برم دوباره ببینمش و به بقیه بگم سلیقه‌م با بیگ‌شگی یکیه؟
(اگه مشکلی ندارید فیلمی که می‌بینید رو شاه مشهد دوستش داشته‌ باشه و هنوز این شاهکار فرا بشری رو ندیدید، همین امروز ببینیدش؛
اسمش: Léon: The Professional)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84028" target="_blank">📅 05:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=fmxsATyxJiqmsdWOy2eYUF12--J2G9X1SP4TtVSz9FK9L3KOAHjDmPQ3lecw-1dXRemCL8bR_NLy0apHjB2MH6N9uffOiIQeHw68VYlwaN_zyvsfype6ZVo_4rNg08GyMTj2pkmsgJ-yl3YCqzncbSiRJjW3tmJEY4kUQGkZpvmPzQLOqM3m5VQLxk6Szbf2oikiLRw2leb_4inNGRwrA-bo2p3fUeMqsm6P1XqlEgotvZjqjgGcxX4uZ_oUvumwSRpWjRaL-9wH7M1r4xaeJoALhvjx3Skr8kWY99brlhkzbXYTHjXESUDihVKCXu4wjnctc4vEELPq3S9sT5KRGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=fmxsATyxJiqmsdWOy2eYUF12--J2G9X1SP4TtVSz9FK9L3KOAHjDmPQ3lecw-1dXRemCL8bR_NLy0apHjB2MH6N9uffOiIQeHw68VYlwaN_zyvsfype6ZVo_4rNg08GyMTj2pkmsgJ-yl3YCqzncbSiRJjW3tmJEY4kUQGkZpvmPzQLOqM3m5VQLxk6Szbf2oikiLRw2leb_4inNGRwrA-bo2p3fUeMqsm6P1XqlEgotvZjqjgGcxX4uZ_oUvumwSRpWjRaL-9wH7M1r4xaeJoALhvjx3Skr8kWY99brlhkzbXYTHjXESUDihVKCXu4wjnctc4vEELPq3S9sT5KRGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84027" target="_blank">📅 04:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUMSEC2MlNM1qgOnsXftqYwc4LZVDWlvB7NA68j7vxh9RLUhP2HuEzJF2MkmxbzbPcyZX7aR90mHKmiZrhs_LQh2mTbAWMrhUcH4TnvNoU1rwvBe2icELfNpZ5vP5g9en52rezpNtROTD7ivdxyeFV7ENwWHUJzKxuHKFyFnKQSHaxNdGA5N--e5y2Btm_ofd5_MqrawA_9f87JtMpppXb5RSdnJ4aPr9UlT8uw2uaauBevpgewTwkVM1aDhWGc06jCW7df3XFbxWNgU-atGhii_RT1A80jpyjFqBH2hdrWvJugFhoVvqHRHt38l0UmyqwX0n5wVcaNKyV1f6h_OJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84026" target="_blank">📅 03:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پزشکیان: ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود. آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند. من عمیقاً…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84025" target="_blank">📅 02:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d939cba.mp4?token=YjPhLoiAQ8rm9evVho1nsukhavfyUdpgkLtihK4_TeKGX57P18ff2Pt6AeKjGB1ER9MNlj_6Q1jsizPDi5FA2NbiUZLWtXWmTvlHwaDDbyYlfnMyqELF_935QXXN2jT_9TbkXkvnxYwxsUR4rBkz_Fd8TgoS6hU5tpZMdZaYA2ovwGNh1hMMxV3PkUdEbNDLNGOWj0g1or_LRWHcq_9CzQkZwAMvrtWMFptk3l9hmXoNpjLSeAgzGdrfZFsgt35S13VIPb_V9GAOoJjH4Y1bfXbIZWeGCrafFrcba5Yh3eUkoflDy0aW6qTbipmQZTOg6wBR0wnLJn0IcBY7mXlqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d939cba.mp4?token=YjPhLoiAQ8rm9evVho1nsukhavfyUdpgkLtihK4_TeKGX57P18ff2Pt6AeKjGB1ER9MNlj_6Q1jsizPDi5FA2NbiUZLWtXWmTvlHwaDDbyYlfnMyqELF_935QXXN2jT_9TbkXkvnxYwxsUR4rBkz_Fd8TgoS6hU5tpZMdZaYA2ovwGNh1hMMxV3PkUdEbNDLNGOWj0g1or_LRWHcq_9CzQkZwAMvrtWMFptk3l9hmXoNpjLSeAgzGdrfZFsgt35S13VIPb_V9GAOoJjH4Y1bfXbIZWeGCrafFrcba5Yh3eUkoflDy0aW6qTbipmQZTOg6wBR0wnLJn0IcBY7mXlqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود.
آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند.
من عمیقاً باور دارم که انسان‌ها نباید باعث مرگ یکدیگر شوند.
ما باید موجودات برگزیده آفرینش باشیم.
وقتی می‌توانیم مسائل را از طریق گفتگو حل کنیم، نباید به خشونت و کشتار متوسل شویم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84024" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=orQ55VTHuixqIk3EDB4S3TsDPgtbCrszbg-Y09HS7xQXOlU9RMA5rSs6JjxAI2dTT4Oo5_PizwCntheE3knbxR6Sy4leUtsDFCWA84Z9jCvD-yTo9iTQQxC8jhYc1CuW8_BVR0_1GvYFcALluQSXj-FrH5hUGW7TBEB-rYOrubgo-huCIbX55BuopQ9ckfUN7r1dTBSEn9jjn2r0IXMh_GEweshBRCtioaZ9Yfy-k24KrSvygwkeq6woyvozEfj4bM6LXaO04cngqsFz-iEeEqA9CRwPi1guNCypeBrFOPhapoWfObwsEYi3VtBHC9P-GE6rvaJ72VUEfQfIW1U5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=orQ55VTHuixqIk3EDB4S3TsDPgtbCrszbg-Y09HS7xQXOlU9RMA5rSs6JjxAI2dTT4Oo5_PizwCntheE3knbxR6Sy4leUtsDFCWA84Z9jCvD-yTo9iTQQxC8jhYc1CuW8_BVR0_1GvYFcALluQSXj-FrH5hUGW7TBEB-rYOrubgo-huCIbX55BuopQ9ckfUN7r1dTBSEn9jjn2r0IXMh_GEweshBRCtioaZ9Yfy-k24KrSvygwkeq6woyvozEfj4bM6LXaO04cngqsFz-iEeEqA9CRwPi1guNCypeBrFOPhapoWfObwsEYi3VtBHC9P-GE6rvaJ72VUEfQfIW1U5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما هرگز به مردم خودمان حمله نخواهیم کرد.
مجری فاکس:
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدرسه میناب حمله کرد؟
مجری:
در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
خیر به هیچ وجه اینگونه نبود، آنها همه تروریست‌های مسلح شده توسط آمریکا موساد یا کردها بودند که به قصد سرنگونی و ایجاد آشوب می‌خواستند کاری کنند و فکر می‌کردند ۳ روزه کار این نظام و کشور تمام می‌شود اما ما مقاومت کردیم و نگذاشتیم اینگونه شود.
آنها مردم عادی نبودند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84023" target="_blank">📅 02:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مجری فاکس ‌نیوز: آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟ پزشکیان: هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.  اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم. اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84022" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5add83729.mp4?token=TbzpzGD--UDEAfGy070d8UsSPtv2szdPJIwuCz2MCYhgBeqI-12oMNrTWQp__3xbZ2B_epQQPSSSyCiC7nXUCxq25c-g4hnantAzsiiyGfUMME7YMlCYPbDqGYXSMQhPIG_-QtjliQic92gzjbF-wIs1pyzTZz4kVPWzGq7UImhq7YMGOTqlVDqjz1C41tfgLERMcepGsvPcDuruAEX1ejthH7aQNyTehQGU8x-dDr9O7t6K1bKn9SHpECuXxmmhKMy5i685OLU-hk1DkcDc1MwlQZW_QXtEzn1k5YsOFdwYfIe34HBfdgmcwikKHcZR_YWddmXO8XKAFEosKinVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5add83729.mp4?token=TbzpzGD--UDEAfGy070d8UsSPtv2szdPJIwuCz2MCYhgBeqI-12oMNrTWQp__3xbZ2B_epQQPSSSyCiC7nXUCxq25c-g4hnantAzsiiyGfUMME7YMlCYPbDqGYXSMQhPIG_-QtjliQic92gzjbF-wIs1pyzTZz4kVPWzGq7UImhq7YMGOTqlVDqjz1C41tfgLERMcepGsvPcDuruAEX1ejthH7aQNyTehQGU8x-dDr9O7t6K1bKn9SHpECuXxmmhKMy5i685OLU-hk1DkcDc1MwlQZW_QXtEzn1k5YsOFdwYfIe34HBfdgmcwikKHcZR_YWddmXO8XKAFEosKinVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس ‌نیوز:
آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟
پزشکیان:
هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.
اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم.
اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست و قانون کاری انجام دهد، این امری متفاوت است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84021" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرزیدنت پزشکیان یه مصاحبه تصویری هم با فاکس نیوز کرده که الان پخش شده و با دیدنش می‌تونم به جرعت بگم که حجم و سطح طنز پرزیدنت ما، قابل قیاس با هیچ پرزیدنتی تو تاریخ بشریت نیست.
واقعا الکی نیست که چهارم شدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84020" target="_blank">📅 01:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جمهوری کلمبیا اعلام کرد که روابط دیپلماتیک خود را با جمهوری اسلامی قطع می‌کند. این تصمیم به دلیل ادعاهایی مبنی بر ارتباط رژیم ایران با گروه‌های تروریستی و قاچاقچیان مواد مخدر در سطح بین‌المللی، نقض حقوق بشر، مسدود کردن تنگه هرمز و همچنین جلوگیری از بازرسی‌های آژانس بین‌المللی انرژی اتمی از برنامه هسته‌ای این کشور اتخاذ شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84019" target="_blank">📅 01:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FktBR7jfnu8dgn31XIrJ5xg5aabWFdm02W_NpHE06sWGpVD9HybCnNDoPw2L-q3VqRJFoe4qXBlXXJRDTXXHRrZQNMJdibaxlwlTbSzo8x8fDuG7rkRsDVoCXm0TC77DzkA06gduJP2Pw7Z0MmarGaduxAfyl6utpenDbd9asIBIFDDPzxeM94mLij5tANWHAcrQcqSwoQGejWy3bleFwlIPu6Rr_Q6lxNJOAXzGYeOfk0Hg_OBUfxaLXqlcpq7Ijj_76aXIChUmdpLUwntyIZLZhcrtlvGQvH8g82Ei2h6WGf-fuME4ORrUkUGajUvNDnsCx6bOgzrqt5p8o_w1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت مسعود پزشکیان در مصاحبه با NBC News:
ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از
اعضای خانواده‌ش
رو نداشتیم و این پروپاگاندای یهودی‌هاست.
برخلاف
ادعای روبیو
، ما اصلا دوست نداریم جنگ رو تا انتخابات میان‌دوره‌ای آمریکا کش بدیم چون هر چی زودتر تموم شده بهتره.
ما هنوزم به توافق اسلام‌آباد معتقدیم و امیدواریم آمریکا هر چه زودتر و قبل از انتخابات، جنگ رو پایان بده و به این توافق برگرده تا ما هم بتونیم بهش برگردیم.
ما آماده‌ایم دسترسی کامل نظارت بر سایت‌های هسته‌ای‌مون رو فورا بعد از اتمام جنگ به نهادهای نظارتی بدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84018" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=wBHrOaKEgFDpzE-ARGqPSpFfAEEQVuds1pzV7cZl0Pc7itIFy3nxlx_8yqfhBhV4o099IlJfJFBKq_Et367f-DYQ7hSbr6gZseAkVJxI4W7zkBH4fXnTsosAtPIll2IbyHjqbyxioveLNunAKRD8AvwMtE7SvLfn-hfcGzcfixlRDvKIpyx2CffbzJ6qbzTBUWoxzul6y3h3owC4EbsxrkY7vVbwFPQQVV_uqaQd6p0osHtTXAUWM_gYIAXqHZ2qPReZbNbpRZqxljMccNNrlsxBINoQpp6-fP_sx3d7TdlR-2Qd4hAtuzbxljmKjFeQnEf3mbn4mDcgvKBuo7uM3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=wBHrOaKEgFDpzE-ARGqPSpFfAEEQVuds1pzV7cZl0Pc7itIFy3nxlx_8yqfhBhV4o099IlJfJFBKq_Et367f-DYQ7hSbr6gZseAkVJxI4W7zkBH4fXnTsosAtPIll2IbyHjqbyxioveLNunAKRD8AvwMtE7SvLfn-hfcGzcfixlRDvKIpyx2CffbzJ6qbzTBUWoxzul6y3h3owC4EbsxrkY7vVbwFPQQVV_uqaQd6p0osHtTXAUWM_gYIAXqHZ2qPReZbNbpRZqxljMccNNrlsxBINoQpp6-fP_sx3d7TdlR-2Qd4hAtuzbxljmKjFeQnEf3mbn4mDcgvKBuo7uM3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده‌ی اسرائیل تو سازمان ملل اون استارلینک نتانیاهو رو برد پیش نماینده‌ی ایران تو سازمان ملل و خواست بهش کادو بده که بیاره ایران اما نماینده‌ی ایران قبولش نکرد.
💔
نماینده‌ی اسرائیل در سازمان ملل: 1
پوریا عرب: 28929853059-
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84017" target="_blank">📅 01:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو یدونه دیش استارلینک اورده بود با خودش، به دبیر سالن داد و گفت بدیدش به نماینده های ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84016" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=j-Xiso8YHGKdjFAwgt1CjKFrQvJ3nX8MMb5JR5czVTzPtqKi9C0yO0Z_GgqbVreHlxrXdDOZ7L34TMf-bPY3B6qoDZFHfrwlVd99cPoPIyXjFOVu0TTEqxNH1TJQa-F2CiSULcszm_3tckKSLt3LND2J4yBxVKgGlgsHxHQxHT25K6BM_kiyOwM7AHkrRkud6jau-ST3ZF9ME4S82mh_jFOJnUuIXNobEgyUL43xmx7asAdA9ImqFPGCya83CmAnADitHGQZoPwdQm0gsil09WIOZUgZmeXMa5gMvGFULydBf-_Qrrvfvj-tNCazooc4beNKjT2eWFlVyB6PiAlIS5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=j-Xiso8YHGKdjFAwgt1CjKFrQvJ3nX8MMb5JR5czVTzPtqKi9C0yO0Z_GgqbVreHlxrXdDOZ7L34TMf-bPY3B6qoDZFHfrwlVd99cPoPIyXjFOVu0TTEqxNH1TJQa-F2CiSULcszm_3tckKSLt3LND2J4yBxVKgGlgsHxHQxHT25K6BM_kiyOwM7AHkrRkud6jau-ST3ZF9ME4S82mh_jFOJnUuIXNobEgyUL43xmx7asAdA9ImqFPGCya83CmAnADitHGQZoPwdQm0gsil09WIOZUgZmeXMa5gMvGFULydBf-_Qrrvfvj-tNCazooc4beNKjT2eWFlVyB6PiAlIS5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره پروپاگانداهای علیه اسرائیل:
🔺️
می‌خواهم چند سوال از شما بپرسم؛ کدام رژیم نسل‌کشی، یک میلیون دوز واکسن فلج اطفال را به جمعیت دشمن (غزه) تزریق می‌کند؟
🔺️
کدام رژیم نسل‌کشی، توزیع 2 میلیون تن مواد غذایی را به غزه امکان‌پذیر می‌سازد؟ این یعنی یک تن غذا برای هر نفرز متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84015" target="_blank">📅 22:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=ZVi-rv4tOW_cTlhaB_mJsQlMbuSgCCtyyDnvsjY7IrO-MVDa1xeVIT2L0MljkfYbcD6a3WR2iJP9sFZvqmdny8Zqy80s-vYQc5j-y62AQeK5ouoBW81fMAlGHzcp59eUXABO8EQvImGiEVMhHYwkeDJy-ApmlKEEz00Dg0JIHRQSu2yzb85IPoa-GQgIMF5y586izZC_ul_nRjybgJj64kOA7qddc2vOBEJo_uylqCaYIlA6LJNW5RhDXOruUUCs1j_p1mZJEi-xnaA1RVIl7wZQU9drKTkYw2THcZwCG725tnKcqBuWH3TUwTRynyZRGA-DIXo8wMEHHB_-Me2iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=ZVi-rv4tOW_cTlhaB_mJsQlMbuSgCCtyyDnvsjY7IrO-MVDa1xeVIT2L0MljkfYbcD6a3WR2iJP9sFZvqmdny8Zqy80s-vYQc5j-y62AQeK5ouoBW81fMAlGHzcp59eUXABO8EQvImGiEVMhHYwkeDJy-ApmlKEEz00Dg0JIHRQSu2yzb85IPoa-GQgIMF5y586izZC_ul_nRjybgJj64kOA7qddc2vOBEJo_uylqCaYIlA6LJNW5RhDXOruUUCs1j_p1mZJEi-xnaA1RVIl7wZQU9drKTkYw2THcZwCG725tnKcqBuWH3TUwTRynyZRGA-DIXo8wMEHHB_-Me2iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره جنگ غزه:
🔺️
در حالی که حماس تمام تلاش خود را برای قرار دادن غیرنظامیان فلسطینی در معرض خطر انجام داد که اغلب با استفاده از زور و تهدید صورت میگرفت، اسرائیل تمام تلاش خود را برای دور نگه داشتن آن‌ها از خطر انجام داد.
🔺️
ما میلیون‌ها پیامک برای هشدار دادن به غیرنظامیان برای ترک مناطق درگیری ارسال کردیم؛ ما میلیون‌ها تماس تلفنی برقرار کردیم و میلیون‌ها برگه اطلاع‌رسانی درباره حملات پخش کردیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84014" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهوی جنایتکار بد در ادامه‌ی سخنان زشتش:
می‌خواهم خبرهای خوبی را به شما بدهم.
اینجا فقط مسئله زمان است که چه زمان این اتفاق شگفت‌انگیز در ایران رخ خواهد داد.
قدرت مردم، قدرت حاکمان را سرنگون خواهد کرد!
می‌خواهم شما با دقت به حرف‌های من گوش دهید. یک روز، و ممکن است این روز خیلی دور نباشد، مردم ایران آزاد خواهند شد.
رژیم قتل‌عام آن‌ها، با دروغ‌هایش، با فسادش و با ظلمش سرنگون خواهد شد.
این رژیم شیطانی سقوط خواهد کرد، و همه ما در آن روز جشن خواهیم گرفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84013" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=V1FicNPUKt3xh-wIptBzlOKbR_nDS20zIRxOBvOcqaroPcLy9y9ySa6pgeQvguxC-fGqBjSV-ZZgPfD5zhqYsOmA6Ig_CsXNeAXecmHPS3BVt9X_fZTthdIGSxoplofQHgsRbsRkFuitaKbDyr-F6_GLRS84LdEWX3t3ru6h8kt2MYFJLqvRnic2yroU-QcHh5dvhbq50ysYBHcvGMyAa6RXDU_AbouP6h57V2T8H1VczrHZipx5eDBrq9YKsXcst7rMiR1uKaV1qEc4vLN_VUKS8iPPTGkuL0BfcgjKjPUpTD7ThnbDwdZ_mwnrDoKFy2-GHC-kQz64nKG2eq887g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=V1FicNPUKt3xh-wIptBzlOKbR_nDS20zIRxOBvOcqaroPcLy9y9ySa6pgeQvguxC-fGqBjSV-ZZgPfD5zhqYsOmA6Ig_CsXNeAXecmHPS3BVt9X_fZTthdIGSxoplofQHgsRbsRkFuitaKbDyr-F6_GLRS84LdEWX3t3ru6h8kt2MYFJLqvRnic2yroU-QcHh5dvhbq50ysYBHcvGMyAa6RXDU_AbouP6h57V2T8H1VczrHZipx5eDBrq9YKsXcst7rMiR1uKaV1qEc4vLN_VUKS8iPPTGkuL0BfcgjKjPUpTD7ThnbDwdZ_mwnrDoKFy2-GHC-kQz64nKG2eq887g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی نتانیاهوی جنایتکار بد در مجمع سازمان ملل:
از آنهایی که اکنون (به نشانه اعتراض به وضعیت حماس و غزه) سالن را ترک کرده‌اند یک سوال دارم:
شما کجا بودید وقتی که ظالمان ایرانی، دهها هزار شهروند غیر مسلح ایرانی را به قتل رساندند و سلاخی کردند؟
وقتی که آن‌ها هزاران نفر از خود مردمشان را به قتل رساندند و سلاخی کردند، شما کجا بودید و چه کردید؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84012" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVnWlb1_ime3PqkrXx0pe88h70fymps5S6hZ63ifs9p9WSiacJV69JjRunuBOq4O8sPFpOnrnhztp4Gi6lEwpFP_hRbZrL4_vQoqEczPs5E5P6qeq7c0IxdL-wOBItUl9r4Iy8hmbkPvzjmuPqfG2B6x6OQj6bbHL4IzEJ5dm0L7IjJ3igeBsgNINT91J-1I5zmDB6hnonQI5RQIsnmFTy5LLHoDMAejX5gqaGh6loHVrtYpAiUvHnHNyr93D1BWPX-3uzBj1ZcKeKtJm_GZ8Ewulhm-RmjmW-N2I_UmNFA9KegC1WVRUxCrkoY1FT8OM0ullmOvaKJwcCJEhVfmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84011" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84010" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84009" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXys6tt8U2To2mWL5qewzZGhaszCA8PAkVGeI0ICYOaojwmUfQHjQ0zm7OiRHqs2YDSGcKVOqE8aU8VPfzulQut_7c4tndSDtzg7X5LHns3bQqh0B60u-cLqNYfzjf0nK9uOCz7rn6lXHbV1_2IhDO80Mq26R9WhBHgIgNCyzXcQB6_Sj92vh0O63sAm4oiXjZmHPukU3YAzUFFExFHLUSa8KP1UiJ2p56yph0aZmHdZUICaHRIni9tbhFZqmtQJ1L2EEDP7aiYK1J4_MPuFUjsO6BudZAFshqRsdguj5Zz3B2QGAnsdS6DRlp-WTEdM8AOGPCRCXutoU4xKxbTzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
تیم ایرانی به رهبری دکتر عراقچی تو نیویورک دارن با آمریکایی‌ها روی یک توافق که جنگ رو کامل
(با بمباران اتمی)
پایان می‌ده مذاکره‌ی سنگین می‌کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84008" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد. SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84007" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_hqb-tugYCP2Bgg3vkqsv77vpFnbk9J2hioZtAKugUxdQs4XSIYxiUcZwOCEtKCBvqdH2AFR3MsINXce6WeHnuh3GVdxPx-wLx8Crk35328kZivDuokY_GqXU5sc4nwFZrANpepazNlnPLoKGqF9vxTC9SGfj4jR3gloWRYCXrwFJYgm6N92e1jN6ONs7akceXnEiKQu6tS9TOhPqc6398cN0_TiT36nvc5cZuIktFDYehWZjuCTmz-RsS083tBjMhml6wv4dLdrgQWIWe4APtVWf2c88VeuWls6q3TXLhwn8BYOQmnRxbGAi2sLrgfo-SQWjVayC4kkLhI1X8_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84006" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfU1nVJm9ZpaE1MqlgqEkVKYGQDZcNCnK316aiAcw0utmtWsarMl7z6MGXi7PbXjnSH-uVwlhg3f0ZEJvfVnd3YQfxBOmZDc08aMcp69htS54Ae_r5-H_8DHqSx_qo0kkAF2LFp-GaeKioyU5hCEgBnVnteGC21H8OSBGB0F4kK2A1T3ioVsdL4kPYPXYigeVk2oCw085WvkS9ip-AbG4bpr3h_OoPbJGyxZYcD9wG-ad5bCGB9y1QalBkCM0cMIr3aNpsdwY4udAuh4rWd2a-zbpNd0XsVBS122QhGe5st4S9ByXskTkvKYscWJv0-35_9Bn4NDUhtk9oMLiOcjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امیر محمد یک خواننده ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84005" target="_blank">📅 19:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZX2rnJo9Phx_X9PderUujmXoaseFCOXVSeOCyqd7wzIrpVYUdWV3TcGewp8UzQEa71yZgHy4kAfowz_ODzDbhc5VwWebK4MSBboBmD9Kn0AWrOFRntQaHSzbfMZaW_LCIQOS9HA_wN_dvZuZGwkhh9Z9zsxAHu-uqU3bqNiWtU-4sK8ssqoY0WPXFwAG_19sxe3oO5-qguTne1exyBLJOx3NdzsM2j6vZouzv_VuInnLlwWXRGIa8vrNg29QPJFc1ELfUrWRVyb-ex_TB_xdC09R8kSIta8SiTKcZ0f1AM-kkvCZN5uBILb98RBbSGZt0StFw9sSPz3tTkQY-PCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران جذاب ژنرال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84004" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=M-uwiqBmJwLU-fpg39mIoTHzIaW5LGz3gojcT92ClWPLyl0ZlzJ0p8ZjWJF2AciIGHgTif5B8N4M7EyhvJKwqW9-YlO1EGEceQ60uorXcb7cvxzTFkJqV9guIdANpDJAYPh_rs1HV2O6NuOVaWPdZ2ddsIBFeN0U-3x2pAAGgVEnP-q-nNGnj26xeHCTGoL3ARReuQnQfUUD1JKM3pansJcRSHfDNSDZESSyoRQvQ1OxbIM8n6zr6MadvCxDsFb3G0Y41U8pHQ5fYb_RK7km42K1AN5Ar1wVQyzQ-4y8Sf5vS0jO8OPBcgfbr9rbTPcSsc1mpzdBDNILg0UPHwjLpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=M-uwiqBmJwLU-fpg39mIoTHzIaW5LGz3gojcT92ClWPLyl0ZlzJ0p8ZjWJF2AciIGHgTif5B8N4M7EyhvJKwqW9-YlO1EGEceQ60uorXcb7cvxzTFkJqV9guIdANpDJAYPh_rs1HV2O6NuOVaWPdZ2ddsIBFeN0U-3x2pAAGgVEnP-q-nNGnj26xeHCTGoL3ARReuQnQfUUD1JKM3pansJcRSHfDNSDZESSyoRQvQ1OxbIM8n6zr6MadvCxDsFb3G0Y41U8pHQ5fYb_RK7km42K1AN5Ar1wVQyzQ-4y8Sf5vS0jO8OPBcgfbr9rbTPcSsc1mpzdBDNILg0UPHwjLpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84001" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84000" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9MMgApiN5yGrt2uLluBm3y92LI8JSR8TqOpBU4AO9RTViIRXNNHqDhENsjpxtUlac83SnIHLgb-ks3zxQl5TEZ4WdfU7-peGxLVRalWke2rpKCoiUzuynf7XRrDWO9NlIgv8ejPaNlp9E5xhtYMU8MUqkN3WesBgzr1kz4Fv6gWvtsYU7Fkj7SUQUmWlm_604BvVbfNaCNBnu3WIoIx_N7nmcJd4Q2j8etoJhYEbGPdKSWin3HynQA9chzD5PGOwvkpKJCc_--Cmn6FwNEhtB-QxjPFG9NxkQBtdRHzsyVuh70GS0I8pk1u1qnP8rdPi5KMjVmZrFfiThJ1dDBbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسی به هیچ وجه
ترامپ:
دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست؛ بهتر از همیشه. بانوی اول شی هم، مثل همیشه، زیباست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83999" target="_blank">📅 16:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید باورتون نشه ولی کوروش تو چنلش هنوز با پوتک درگیره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83998" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urfBo7XKu16Ho1HwhsmAsm71bb6GZ1G3x5Q_28HUeg4UjNbvYXA1fKktQDMhMnGwTsR1q4Au20sQVRGw4Z41Y_UbRzFlnv6EEyWWTKYFYdLSdrf2zn2yRfr39trk5E6sv0DjQaujAzvL6UlfP0TCCTxGiH42WDcdxQ88q_Bhj-Jki-gTH-hzwOigvrzaRXkEJ201wvmN9ZHlgOhbW4lNd8LFXsPfy1fVwk8EVkOZwembwywxmIV--0hlTARS8ZPJTiiz00KKperGtiMGfllZhc4fcXRiPuMnSg4ExJPE28M4lQ8XS-HcvYwzo7rupr2iSEnHDc3gDH7u0Biul57CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اینا تو وان حموم خونشون ناخدا بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83997" target="_blank">📅 15:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkZ7GPzOGdngHN9hgFH5jY7-9ycu-PdknFRIA4nuK3iyZJ-SwNNkgkdBnN4HS9xl1Lo4nJmSb3KQSlynmSRt7_WI2KGZoBpiNH8CGPrDyqk8jUWj4qGkNVER8h-LIokOqTHoQ6-PzrE2cRwbKVpM356GZwgHW9osLQDNLDxcrKdcZeP8aEGqoQYwLe-mKEBhWCqPNssad8Uc-AsRs-qeu1vUbYJ800fS89mNvyY9RPq-9KFSyEIaCw5BVItDyEm4IEJqOk6hKmKskXmDjndLXefiN44MEKyKGAVczOrEViAsEC6uRr25Hmz9TWQYZSyAW3xoaRORLoXV-7rTbh0aHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد به سلامتی به کدوم سمت انسانیت عازم هستید؟
حموم؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83996" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پس پزشکیان کی قراره بیاد بگه گور بابای دنیا ما رفتیم بمب اتم بسازیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83995" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=kHaLIsNG65rLpdg7Ogbsvh6z-17r4f57hgOQvomF3kh-EtPp5tjcr0KeoW7ehZ7cmze2HQCtiAxYWht60hCLOZzI6dUaKGoQRHSQFMU1vJng9e0iuSFaMk7qjrpBeCnwpeLoJBBgLj27_Hxz5PQYS7qxTUlRQRae2gWWeazR2C9k5mNjZ-gzXrqjjMYwGOEAkKh1CkB4RMZBHb6JoKV55VijegSCTlMBbNODrrAqrza8SqXAXj665KvyHsFNfzlymIkUfyFBb6RcyVfMBUek0W85gAPed_St2fJAtaHJBWJM4Y360zLhNTSilQ2-6wMuVXB5AWhLmiIwypo3iuo7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=kHaLIsNG65rLpdg7Ogbsvh6z-17r4f57hgOQvomF3kh-EtPp5tjcr0KeoW7ehZ7cmze2HQCtiAxYWht60hCLOZzI6dUaKGoQRHSQFMU1vJng9e0iuSFaMk7qjrpBeCnwpeLoJBBgLj27_Hxz5PQYS7qxTUlRQRae2gWWeazR2C9k5mNjZ-gzXrqjjMYwGOEAkKh1CkB4RMZBHb6JoKV55VijegSCTlMBbNODrrAqrza8SqXAXj665KvyHsFNfzlymIkUfyFBb6RcyVfMBUek0W85gAPed_St2fJAtaHJBWJM4Y360zLhNTSilQ2-6wMuVXB5AWhLmiIwypo3iuo7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=iIiBqWs73-1g0_YWcFQOnHwVRKx4lFZ8TjQBAj1aFDa7OkmZDSPAFFC8C4I52wMUey0pFhdbix7juPK5E30hVxtCm2qd1hXtF1k_ZO0PGmAHubjHJlSwRAbJjCIlzZ7MI4M5N7_6OxuaOXdmALlxGCuo-lzmuJkT-4QUrwkFxBs6uZuQKDSRKIzpj88LRDPIDBXcy5Fx2lNI2GZxY7DnJjUjWWOgNNm3v5uFaATju30LMVefMG5t3ys6tzBtA6SlN4E7sGjmfVcPMiW2yI0oOiQeHETQIDuH6QQeDDLgJMKC-oLpSE38dPPvxqwTqZXpL2mg0haaFKX_OgWvrwqdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=iIiBqWs73-1g0_YWcFQOnHwVRKx4lFZ8TjQBAj1aFDa7OkmZDSPAFFC8C4I52wMUey0pFhdbix7juPK5E30hVxtCm2qd1hXtF1k_ZO0PGmAHubjHJlSwRAbJjCIlzZ7MI4M5N7_6OxuaOXdmALlxGCuo-lzmuJkT-4QUrwkFxBs6uZuQKDSRKIzpj88LRDPIDBXcy5Fx2lNI2GZxY7DnJjUjWWOgNNm3v5uFaATju30LMVefMG5t3ys6tzBtA6SlN4E7sGjmfVcPMiW2yI0oOiQeHETQIDuH6QQeDDLgJMKC-oLpSE38dPPvxqwTqZXpL2mg0haaFKX_OgWvrwqdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=HIdFBUi-F-A2RNrO1EOd0KoCtQe7AUH1LpjiiP-iEf1MKgVDGYRjn6NGYzfiMxcgTsWZ_xpJJZ5gOmpweNZyLhcaqXHfgIY3JQ8lopdIxibz0r_aCiOtrnvbRZ_0rpEFDay-S8t9e1bfPgmX7yE8oS8akrhtskKTT35jiwXCouMBvgRyYzipMafsyl-p4W7M2svFyHQnp2rItgteM-lztCZJLR-_p99ctvBeOjESKC6kcSjSGb0W74v8-4vwpE4BUzpgog5eJ7QRLZEjLdpkzcj1xjzgD6kw6t5X8KdNdDz-naX8UPuTiz3uE-CpaMP1iSFrACnJ7--OXsWHRHI-Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=HIdFBUi-F-A2RNrO1EOd0KoCtQe7AUH1LpjiiP-iEf1MKgVDGYRjn6NGYzfiMxcgTsWZ_xpJJZ5gOmpweNZyLhcaqXHfgIY3JQ8lopdIxibz0r_aCiOtrnvbRZ_0rpEFDay-S8t9e1bfPgmX7yE8oS8akrhtskKTT35jiwXCouMBvgRyYzipMafsyl-p4W7M2svFyHQnp2rItgteM-lztCZJLR-_p99ctvBeOjESKC6kcSjSGb0W74v8-4vwpE4BUzpgog5eJ7QRLZEjLdpkzcj1xjzgD6kw6t5X8KdNdDz-naX8UPuTiz3uE-CpaMP1iSFrACnJ7--OXsWHRHI-Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfuQhILU-9XM61Ks1OAt8G2F5Owe39L6IQE7bGCh47DQgEiJ8lHnDdLJBWYx79Jt3IGZQfECravYn2dmJnpeEuMNOkn3CiPIWbVl9w8AfzQl_YFztt3EUKz83THDNRyXwH3OA9qv9c0FbAwYX2UHHzy8EwmGLTrE7Kqt6R366Bj9ReUud3yJSs7QHJV8QQOp5si00risAl4ZWkDKUFhNGPUVGpjhWt15pdKseQPouIS_L-vbkH3oYA7cpeS7jmtRd_J59BcNQrkc6SZT0DzNn-wppId4YvByZ6tP5gTR6WvpiZiEh56RmPZ7YOggoMhDHbJYaI5cIu9gzW3cpKJx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvMlOFYkpS32cCaGlvPePmg3rYVXmwjp19NGvcTEKU81AMH7GCwyhLEHcfXrmrEV56MoqBvoZ63tr0piK3H57tZAzCeF17kemHR7jh5Jeq-pF6AUylsuzuwno_UkFzpZom-e6riWnXHbDdFfO3IeqFsYQbnmmrsWa0ryVv6xr7FXIwPb8S7FrRVHsNUYICIYw6dFvWicE98DxHTqSO0SCZ6VYJBy3r0JQXovf-i8oJxuV5rNLFF-QHRMcVSH3vy8bwJEMVHiTC6REEAiEqcOFuLXquY9PUul9PAxa5TKiBEoo7iRMLeAwvqCKeOEIFSXtc7ePvh7G1e86MxQUB0_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNkpBbgkIWeAbzhrxtjNYy1NX2efCD3rst8f0WN599P62oHUjeTYwc2_0u0-K8EEugI6dRRKAc5Y8iJ8qpJAz-Nb44RprGm_6fp9snSkeAwFBLrA89zApCEN8leymuX-HSlBtujPfvgru781m380UoUBnEKiJk6q3kwlzMqsTqwEAcaz0nxdj1MhxttYr2cVwDbVTu5D8K6sG3e0t9p8PzKV9owAUWN2LO380_JcKwODIitUjZUoMiyPjMhdS01AptHSZkZyRgMOP-qGmmVBWU3sne4VZF47dYflkwjM1jDy4zhqo8EVjZcuJDtLtYsne2psGeM6EjpQ7Rn7a7QW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX5Yj7qNp6ne4LAUnXTdl5XnyiQ1AeE1XAawgr4DJe7hIuRA_SM3tgULCayCVpxHt6R9NL3xfQdkVY-bpECdAwUbrkMobZtgzKqhJxhqgvFe9j_dlbhkO2rb8_mOm7ArfiOnQE3CFAizyOse0ayuUysOnZO_gDH1G0iaxAgWjaqPpV1RFJqz6mC5xLbMTTy9HUSVDnA2PbQ1r9veNn5JgLZmxOsst7JtWSdKF31rrTpCq3cL-0V3kAjprNH4xiHk1Hl5hPKFIhQH99MpEclIbcQga1T4KfALRHTEMTVxhHQIcUS3-1u6ecjMzgTqnfqrhHLpKVtLJZkqXmvLmhB3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM_DfJJVE25i6SLGvhjcROyfPKsM18sj7nYfqVfSK0YRSZqB2VHHcfdBsD4c-WnrAYA9RIAxqCYUCdlMTmMS_zaDJ7mK-sbO3ILg9a6ygRM9Yvec0u68fKZPRLnoeRt4_grwmnuv7_wf-dwsfeT8QL_VVmGen8hwjxtWGyYbct3ibQdIPKXtkeav1d2aJvJMU9jc7yVC4FMRVFld8EVEMB4P7-5ndRnnZ_um4IeZPZvF5DtGhgk8O582PEeTJ3wAbg5igQtuq56nOtusCON0XyprcFNQXR6vshTj6MjSTEzc0L1v3hh-tuGUSVFkLCApFE2RtE05kqfWW6twyoaDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=i3EX2ys6H0ReJXaobUGYE8OH1U9MTHWAC_yrbtvJsZnP0jjVbm7lTzOBDUoquDsQKQD85Prv27MUFLaIST4bQBtsGRKmThQn0QOGrShZK2EdVkOxA6pKqthwCVBeKVZS5Qebh3kz9HDBPkjp3evxi-3LPd8z1rAXRmp39bSurmaWc3hiV8fD3pbdkP1AhKhj83iqtwS8BZjviZ3U6CxRYQJoZzR5kzpoWKBe7E4kFtQGRUK4hZVdOWBr4CIe-6qlwceaBcOzJEkLPcWWy2AlweHy-cOQ-UJg3X1nc5qtNgysLFJw4ZjyPSegXN6_fP0XTnn5oXUluLUdjFQ6n4uPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=i3EX2ys6H0ReJXaobUGYE8OH1U9MTHWAC_yrbtvJsZnP0jjVbm7lTzOBDUoquDsQKQD85Prv27MUFLaIST4bQBtsGRKmThQn0QOGrShZK2EdVkOxA6pKqthwCVBeKVZS5Qebh3kz9HDBPkjp3evxi-3LPd8z1rAXRmp39bSurmaWc3hiV8fD3pbdkP1AhKhj83iqtwS8BZjviZ3U6CxRYQJoZzR5kzpoWKBe7E4kFtQGRUK4hZVdOWBr4CIe-6qlwceaBcOzJEkLPcWWy2AlweHy-cOQ-UJg3X1nc5qtNgysLFJw4ZjyPSegXN6_fP0XTnn5oXUluLUdjFQ6n4uPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
