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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 170K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXD-9APXbkff5q35CVGalgeaEGaNhOIRWKck1tQv4wZ9QLz_wPDK3sPS5aFh6dlYicGd9Vd7wASSIyOeTejZJQ0_aMz2sDVaegM2DsRbi7Ux7TZ9gVFs9Hb4Fks1kbpOlacMZeUldHwDBZu6tXH2mw9qZ_i2hZ-jFUuf-_nlQ9ZNi48YgWO2yuo6My6QhC66pRr2J5ycSWN3E7tC4ptVJ_XYELjXxkQq57dZzsmS6hvZZTSg28fKGLk9F2orEsoNEaQZNOOkT3YZA8c3mztfkqhCNAQJChr95QGC0-v69-DJwSlVmulzzL7deeAhKZBEpG961PvBzYzHk_UBnEvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QhhUIe8ce52IX358JgLGGj-d3Kb0b3IJ2B6kZZP2PmNP4NktrMKXpMI7_4A3O_Y-XAUYoApzsxMLAxAR1ZU38m-F-Ztoml98vRmQm4bdcAvoAUKLilH4-_CLoY9ztveXFp-3A-QyoXFbSHhafnSqwbLTWbi4TeLE4BMxmBGH7y6bdg1HsROQSH6wHZsgiIrOhOpJJxiGsaW8YWVFbiL8Qfjwr_eiW4Qzw28Nv2DiscA8Sqp-8zIJxH0_MwMNe_pdwNtjMBA4kRPy9K4PsyZoZUFz_wsrD-ZCioZAk_T4oMQ4-8E0NXMgFiUhs7buycWKsh_cpZQuKIHVCaUg05rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0MPrhWISxO6oYWhy4nGiRGR7Fx3tXst5lw3DiYcnsevXcD_lXSgOTKgll59r5gADQYe9X-ijHDU8XsTFwBIHsdXJOvl7kZuvrlE2euoSWDsqeZNe-oVFy3ExVb5tNL640kwil1PK0yxRwfbk0kBOCOaMflO7M1I8A-Cd84sJpcwfwMd8hebqMMzQRLl7gWAY_qLG8Unben2n6pL3Am6x0DUx-hB8bNVzLKLtFPJCqLO1P0aMBhQoGjfV2jifjcXpjQh-wAXnplQM0xL6npZuHBwH-3imRaM0MreqIxJHNx-2gR7dOqYFRxyvM_45UJrkA_DIhkIs3NEHj8clGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7q-rGHBgR5xIrV7cr9jpNUSnCKLtfqAgLMPG_QzjTdHEo9m1g9EGsoa6vCBD15KYvnvnGZL0nZ_q6yU8WJUuYoabt9dmT2TTCWC83oUSX7qeX8rJ_HOLI8t2Vtx2VN7ez7gEYjGd4GA7hcnasFNRfNHecx-Jdp-GLbWldBckT45XjPjqeW-cgX8U3Rrss3C-umQngN6c8CcFcssJ2f6CaG1xghb79l96HQa88OFMw7oiNVr26l7t8SpTmVFNsaP4A10503jYuSIoGVV6gLCDvDV8AzQ-WsdFd9BNj1MJQhP1mr_kYGNSb9cNb7DhvtMX6LcNw7_AIwjUwZCkP_dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3s7Pqn8dZkWsMbiqN5lgvl2TdRBTxonj38inyyxSbprHaP7iRW1iiaNsu7L4FJ_Ecn9ij8uEV_RwQG2-C7HF5NZLQmEkR0wAXtmomvJlilo_qpqRtrKNcbbXTIVP_bF99zc_QPQmKelEud76HKh6S5UYPLUjUH8_cwGsqsepEen9L-7JOG1zi5Jya8D4y1wLde_2XU8LeSu72iWDs-uPWXzcbmpev_5XYgABSPgfETZwRwLemLskbu2z-Ngy31Br37V-DX1jNSUWZnC1-BBnTyQannFTCXwm67VcfZjxQMjIYowchS33Zm35BUsjQEBheJFgnMqk_TZIT6dC-XJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51L8pvwybOBjv2Leig4GykKBwj4IHde_SQlye_pIahCAU1MIur3w0xGfFRWSk_M-L_kla3RqmuHkOexRu7v1X12Nxm-r6zMipfiK9tWrG47KqGQ58v-txZx_XXPrIaL8fV9bi8zUumhxek2-dVToQzgZUlf9ZW3XQAgEvLaTHipXmTp4IUDosWJArKbwJEOmtFiIEaGK-SZ5Q29Jw3xZszXr1tatK7vBZDGpW4Lvm49VByTas1K3u8-n1zFG-ob17V3a8XGdxnT0T0VACad9SJQYhQDDlS_L2zgJfuzodGsjOT_Dbms4hsuZZuTOK4aWg8DQGZ8WGDv4wc0WLLGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HroeOGKFzmue2hXxkbEN-2eETIiF5RmjA5G-uHooE54NdKWQKUpdY4a9DNu2MA6FfyJzwDf3PSsAM70e1PK4zGpZbqFBAoLoBiksAjXwrsCS1aziHJw9ETXcZqDkRoztmmiqBEvDxbzG-K8m9JQAPh2P8PJRJ_LSACSIplihPhx7w1aR9DEQeJN0NWBODiDwf76_eH5E-iFwKEfZ6os8wmSrOQ0C-ImIzon3-WH5lNzYU-9JMGh7iFsW9VkYcS7Xvg1PXrKoBavsD_Nq3n3KQPfqjhinhA_woJEoD91bjKUYjrhTRZNQrbTnpjWyXW1_cM-3WAET965VzP12ICa9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PChUvRqqhNa_4Is8T0QoRgpQm8s9rnmu6q3qV5FxN144zetcl0fvrMf2DU2_7MtTqhvPke0QtFy-SDRoQFsHAOheh0pLngdT7CTIO0GNyNAPKr4b0GKnej4CwXnXTM3ARj9SSGcB3mEVb18WHeInYJ38LB8fasG8eGIFkDxAojEfEvEYgsLloci-yfqipPIp5F31Yz9__D1dyKCxs7m3l4vIuI3OvmfsTxxOU2ck-6lEKycDUjFB2GWPKpNJaVb45LQZYxWHGTwok52tsZ6tFe_4A79r0EjRGMZ3i0s2ktnYRTArXs7piBJDzDOJoPHgB1wZjbUBo6C79qZiu_uRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTAKaB0cPjya096uX43_1y9KYKgPdLPY57GkIRoyipS640kEm1muxSBrBRyX0cBqcNS61FpqlMtUEo8p-z7TFhwvH7BoWN7VR2agKfNMLrOgU_SWY0B-PkrWWIJoGaUm_zm_vqbCyj_GgfCV_to0A2X3UmI6N2fvp2Lcen95mFkyLZPIGvRiyNAEfZDdTcmM4gceWIOzrTDXbOCO7vU1jX0-WYUwxeluQ4tXWAGeoVnMDzKzG7tlTOnquUQt1BQCGbIifup-u5yKusygJ_hTsGUUgndY6Gee_een-otYss1glHH7n5zdrpfUJQJSCtjbruTQlcQ7kUTQZuyNd-Owwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=u9YtXgU6LmwxFlv90YlXSjkatpQHXJg2oKb6QvOuFS-oB2M_roqVIU4jE2e8JLwVh7oJQcx7xwVGA7PbHhwrkOOjjzULOhtT9TfSCkuPERRlNNxvMwPnDV0KES-xpt3UEWOCsUlW-YZWUGnUhic2zpKjekfk-ISrORbIVJ9pPzJy6T8nuo5Is-uq9xjfIdei58Vz9kFzpSSTXb2Z57dwTkBepverwT7qbBY4fcyip1hAo3MecStKTL760QW5j-t2CelTSgFcCjmcO6xtQtkb5C9js8jl1ezGanUXwq4E29WAEq73LIDJdcylJt6DNEzuK9K_ZdbTVjJ7d9t0Ws34FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=u9YtXgU6LmwxFlv90YlXSjkatpQHXJg2oKb6QvOuFS-oB2M_roqVIU4jE2e8JLwVh7oJQcx7xwVGA7PbHhwrkOOjjzULOhtT9TfSCkuPERRlNNxvMwPnDV0KES-xpt3UEWOCsUlW-YZWUGnUhic2zpKjekfk-ISrORbIVJ9pPzJy6T8nuo5Is-uq9xjfIdei58Vz9kFzpSSTXb2Z57dwTkBepverwT7qbBY4fcyip1hAo3MecStKTL760QW5j-t2CelTSgFcCjmcO6xtQtkb5C9js8jl1ezGanUXwq4E29WAEq73LIDJdcylJt6DNEzuK9K_ZdbTVjJ7d9t0Ws34FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22982" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkeTgdkyu5iY03pN_dgYnPfCWS0WjxLcGG45WjUm6-4FJ93RWvgWa-Runxp5V57T481w764HJVtF3LCrDvbGl9Pxu9FE6PaBWPH90AkiepSjVFSU0pGT2v2k-mfO1B0ND_83bRThepfWpUcrxgMBX0yms85FDu0BPN15RMF66Izw_ctJVNrQVWs6jvyJttj3hplbTeOROXE-UCL00iWCsVGIBzty6ifO0mB3cRh5Jj6_STQtna5v2yKy4O1WPR6ttx5OjxT7pfZrJGbRVxfF2zXIPMDmBRf738BQ8U19tcvR-PB9tCGqcAe0k4BHvT2fIKeJ7V9wyNJ3YQFYZ_-YPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABFqe0H-uFihG2HaTn2h9KSkStoaz-YIQORI2yTLezkaEhx8kyo2Ip8gqUPEDDPdEfjuH52C1ADBTZ2xXpo32IVzvNId2RrPENCDTYfSr0TkDfAOanSDh5l19A9XUvuXBjw782c5arQx9wXmtH1J2JTDXZ05y719QlVpMN-RLkT6HtUYisvpI0CykOqmEnBTZelZbOWZrBCyevqlqmALDoGY8qZ5RPsU8uiPkHtZ2-C4qUXRaB5wZCOARuTr03umSZIDq1HZxqv1ACwJwcN92gSqiyvwAVBW63Ffol9miGfxKo9kHB-61y4WtE4-kmnyesIxgD_q8VUprFGNu4TqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv8Rgee0dz2-Ge-2QxPQUD99cR2ZcYtCHG6z-TafGruIaTwJhs4WK2_IzbLoSavBZGf1oajh3vbU8bUa9dfhuIK5kFuGb8uI0sHd2fTkiyyp_yvq6kVhSIjaMrMX71MJZIZILMFFlmd3369mFWbiv7du0Ylq45a89efL0r49rCn5ie_i384rwO0nWm2QSgZEM6Kn9pyFBSZ5UMqwhE6Ye2HGHZieo93odv1E42BhW8C_eoZ1F8aS8YprTQOdA8PKfcRTWUV-OY8Nx7Yg-CC4Gq5_atNK0iCVc-jsZaGEewlqxpLlvXVTVS6U7I6mnxxyCbySWrSZGRXpFz5C95ZZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7AJqvLLyk6ucyScAZX3zvBCCRTj_OGFjxYaVsBowjsJrTTPFzH21iYkTFti6ufwNup1eVgde72gQrNTmfu8iM72HyuUOPJatAcyVm4gKLs1SFYu-jBNCYeYT5LM8WGH1bXozkliu3TzkSvkgHsEPXcREOG9wBzwVZ_4n8gwdzxBtkdJ6mjOTEH32PiD9RJAqm9p8nPWiqCufMpdNimRFYeC6gMN7WHT2XjlH608K2OIgSBc17ExfWJmdRWGPZSWlO6yuALg8g_7lHTTh0my-yv6jL4p8rz6DdFSZ5zT0j2SfnBnyX5V-XWfhyhqoHbadyMIRxIGJkWwk2z3epjMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaQCrrPK8s2Qbqv19fem8IUU6mEpdT0F27Cc8hi8AW-PNkZ1UF7JEzCjxls6Icje2Bhwx2QYvTNLTmfQA09pqMX3yy2UIUxmnVhN1PkpA6nFHds5AWKZwBDf4CuAek-SdOponpd9gqRnRFSD1mZ9_qs6CLc3qrp7mYuBBrkrll2vMXK2-aLGHZennjpK-8CzfrucPas6guM3O-OvLHp3hSTIRQuz8wWDuKi483c_ll30_vZfFdfSkul3KESfYq9TSVJ5vau755acbMEtnLvRDz7yEUEHxtAXorUkhNoeTQ_UPmcNtyNQOjrK0kNTyTlMdjD4iQcEKwbeNrEll1rDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPK5-l4oajDV4YkZn2nCmcUfSuREYT3EC_HpBWaL7b6UZw08Uhz3HVY3nSBH7lQHElwsfwRkbrsk0ZANg83swtZiXfJYcsW2bIH2CXndxJAbnbttrZD5QCoQvR4H6dhbOQbJBbVINbVQA_vbupDtYtYrXnptUJ-Qvt2kZ7EV9psfMvDwlvvZzv137FBxGGMcP6YEfyEzz5ETHJhwuThB_U75ClUP9Q7mmNOs_el1c9JCBNGBJULbdC5djKxQvhLJjRIS_rDnbiIJoW1vOmWjWdJhZ3HhK1dIqigMni1ycc93ker4XwPziNQ9MFVWCaCIdjXDUJLkVnBA5T8MXklahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwChgIB1yH9YoKHyf7diiIs9S_Zdl9GN5B5aDrrX4T3bxLc7aBBr9J_WwQpTHV0tMSiLs1N9VqJpXhrtsLVcxAPWsZn-dSJKsTEQ1IUJnj9RwhXNlZE2t5l_cpM5XKtPzHraSmmDcCCnYQUC4W3yDQmDaG7iWiF_xXhktk58xJdwde9bhtkLQAHVn-jzyF7OY7aeq7Vd-eEyS_uLnKdyNA74DSYMPf2kzIso_eyx3xtRvS1yQBBuF10eXbCq5ZFotJ7-Ka6SqcRd9KMBzm9NU4tUnyL7c-kokWqwgVmsZYxexULF5rvy1JvmdCDpbDDmPoiu_MYbr7jCsEQx4Me8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrsl0_kbQgeW0PcUVtyRK9j3Bah2Kpe-40R5mkeAUzqQyLtboDCbnEEnibh-FSmhg9bGuF9H8aR38_ujdI-eLDUKyIBjeAoGHCjoj6XgwzYCeX1euva6JlFTvv8vjE2aIpBnqhLi9Aq-RZbCK5mz5iJua8-Lb9hldYIoGiIP6HsZIiaRrGzSuWn1eiUw-eJLifV3X8dXlr58HvM3InLmpb45eQ0uaNxny1PDgXx2y_lKhgDDHh82Z2FxyB3hVPTM4hKf3rXyYosU1kQ7JvruNyO-QBdBsvKF5445nLW1VScO3SWH6vUmqDM8uf7CPkFSZ0IvUbVWsCbrnPcumITKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsg8CEDKDyY1pUG7hP7_2DDQbG4mcF5iVS8GuNEueNSkInR6-_jDYxsiqfqBz395Wn7CjozIoTyX3a1ZoCSjekYyybx_4UqJs3hL2CSDfY3bQmcnL4_hN-lHo8uoN01FW1EltoXhH80PZhLEF62M3GTGyiWXv-PRHmxTm3YfQffl2t3btAV8pyaa-zZW8yndTUellN1WUPS4QFFNErpKMK3Dm5ycou7Xdg8fjq0Ig_vqLnwUoANQ8IMFhM-H9-uoybXRyPPN3woRpGDNcogrkv9cjoWz5PNgoOpBmFEQxv_8mY-e8zhN_kfy4w8oJ0CMYbggJEY7EpaVzBLixCKHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Du1wp7D161rIk9GaZQgiCvncureR6-OP4k4jX0pv9s62Dw8o5Ve66DFz3KaWpjWxx4igRsngEgmonRENPuljHmZJchX5rgjcGoJtXd-5hHL9g30cN_PTjTkAc6xHkybCy_zmCTGkOl8TnJErycKlwy7Lc9aTF3I5dfCmwuO-z6yuG6o6-y8RG7d_Hv_fEFbkb4UskUj_b3wLEyYz4F2HBu15q4tSDUnyry4HKN0bcdZcR5dsCzNw5Yxa_lYi95t1a9nBCDtCrVpzb_KX9M6paery7c4ZpxHV9iVIc7z079yH8wzBoO_Hi24lOuuQQbxlHej4GIOvuD3PluMJg50iACwZTQDxHijLdTPkcXAHlc1b6x6lyPAeWPY7vb6pttqxza5eSAEDEtyaf8zLERC4q9EZUrCQEP93NYr0zaaqgmuh6UdM9H9mvFWq8QrAEXN-lwuGeRKRx2t-4k5QEQn5zw4NEsDSo8glj6mvq1Jh-JLtClOweKzqrJ0jGz9cEbvAoSy2jQj-DravBLMClaTvoGzIttiRElzZycEbJ3RFqVte3uQH5kekX3JBvS68b86_oabtEOGS6bpOuxC54vITEHj2fkp1NRaHuRLSBziE7wWMYffm4cZEa2l7MxbudOhI1U5OkCJxw1ZnQdAg-XzFAUKL65epZXeSziK8Rc58zt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Du1wp7D161rIk9GaZQgiCvncureR6-OP4k4jX0pv9s62Dw8o5Ve66DFz3KaWpjWxx4igRsngEgmonRENPuljHmZJchX5rgjcGoJtXd-5hHL9g30cN_PTjTkAc6xHkybCy_zmCTGkOl8TnJErycKlwy7Lc9aTF3I5dfCmwuO-z6yuG6o6-y8RG7d_Hv_fEFbkb4UskUj_b3wLEyYz4F2HBu15q4tSDUnyry4HKN0bcdZcR5dsCzNw5Yxa_lYi95t1a9nBCDtCrVpzb_KX9M6paery7c4ZpxHV9iVIc7z079yH8wzBoO_Hi24lOuuQQbxlHej4GIOvuD3PluMJg50iACwZTQDxHijLdTPkcXAHlc1b6x6lyPAeWPY7vb6pttqxza5eSAEDEtyaf8zLERC4q9EZUrCQEP93NYr0zaaqgmuh6UdM9H9mvFWq8QrAEXN-lwuGeRKRx2t-4k5QEQn5zw4NEsDSo8glj6mvq1Jh-JLtClOweKzqrJ0jGz9cEbvAoSy2jQj-DravBLMClaTvoGzIttiRElzZycEbJ3RFqVte3uQH5kekX3JBvS68b86_oabtEOGS6bpOuxC54vITEHj2fkp1NRaHuRLSBziE7wWMYffm4cZEa2l7MxbudOhI1U5OkCJxw1ZnQdAg-XzFAUKL65epZXeSziK8Rc58zt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=eK62HnhZryh81AifPx1uis3-i-bXriXm_a7Vl1l5k5B2cxjItW3oshabWMW1pDMxabgX7QLgS6731WCC28-xSDvocVVVM1F1zfGT5Oy0lTteXazwcusLsasKJEtMiinAEfHP0jPNHkjrkKtqF8HB0SMukZkgvX9rwHrAB8lMz8pY5zHDuy-dKMWx2l0fIbjEonEZ6g1KnyNhN9jdSuGHGgoVzKfZ_ucZ_yTU2OLSR8b5xMcGmubXNyl2THIZtVdSnk1rwJ0MaJkbtPd7vySJntp71-AFFHP7jvWz2ACzLyPQcxIuL4oE8hpyLgtPvU1JEqpWv19m8ss5TI84vSLi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=eK62HnhZryh81AifPx1uis3-i-bXriXm_a7Vl1l5k5B2cxjItW3oshabWMW1pDMxabgX7QLgS6731WCC28-xSDvocVVVM1F1zfGT5Oy0lTteXazwcusLsasKJEtMiinAEfHP0jPNHkjrkKtqF8HB0SMukZkgvX9rwHrAB8lMz8pY5zHDuy-dKMWx2l0fIbjEonEZ6g1KnyNhN9jdSuGHGgoVzKfZ_ucZ_yTU2OLSR8b5xMcGmubXNyl2THIZtVdSnk1rwJ0MaJkbtPd7vySJntp71-AFFHP7jvWz2ACzLyPQcxIuL4oE8hpyLgtPvU1JEqpWv19m8ss5TI84vSLi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmp2MejReSlMWsnCOrJWPljHU0wQK7S-RHzoaKC7zAoP7SSSRi4xelXgqcx_kHirqLOX8FHvtHOzW_PGEUKdGKCXEVrUdsmN0fO7cMNR1zs1bORPYEi3VS6vr19pOFbmZz8UajCw4_Ulmk-r5MdkZr59thIGv4Eh3R5j-S1E9ZvnptaTCe1brj6kp0L8xPuourccm14yJnHiL1QNruCntHeMQ0SkJmnwT-snvNyzDh4DAVNHiU7hlIOdI4-mpA_65I4kIq82FTLXoiPaDudBW8J-ZdD_a5RnzwGjU-S4-KgFvlYNMgPHjbdEtbjsKTjaaNXpCSuVsmYYLeosWefbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=FZbNEaUIdIkpVEdRqUyDVCLYesTJmWl9y9rAoImoxlRZTXXmUaKQH8EJ2ZVxk26uWc04kbw_Juyp_9NSByNwyRJ46XMou0G7AE4Fyycuf01SqABgMk3LdXjg20UfrO4LW4SBfBCAMyBv0OyQabks3UrejJLyNfPR0lgNUtnvBiOlHVzPYzuebigBou-rYoP8bwvMJkU3EylJn3DJ8a9BocEtmaRwV44fJiHFJvEOvQ4hySZFD-EGe7XCHFWjf0Ag0YIgZ1sGNt9E6fj6y3SAJAl7QZ1AEJzIa-QDZ4A5EztC3v3y_wQx_tlVyHDZ9GZ2QsQ6GmJQDrVJeUjUh6BrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=FZbNEaUIdIkpVEdRqUyDVCLYesTJmWl9y9rAoImoxlRZTXXmUaKQH8EJ2ZVxk26uWc04kbw_Juyp_9NSByNwyRJ46XMou0G7AE4Fyycuf01SqABgMk3LdXjg20UfrO4LW4SBfBCAMyBv0OyQabks3UrejJLyNfPR0lgNUtnvBiOlHVzPYzuebigBou-rYoP8bwvMJkU3EylJn3DJ8a9BocEtmaRwV44fJiHFJvEOvQ4hySZFD-EGe7XCHFWjf0Ag0YIgZ1sGNt9E6fj6y3SAJAl7QZ1AEJzIa-QDZ4A5EztC3v3y_wQx_tlVyHDZ9GZ2QsQ6GmJQDrVJeUjUh6BrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjujOUF2IoclU5LqDPdd4gKWQpcv-9vUkchfE1PBxddlkL2AUZLPPgHnEnjYpN4P376UsZr0rRGSKp1WlY9BTsHAOB8HmYIWYF_xNcwlmMKxfxMxztYsqkAh-H22o0-UZQf_0Obm2dx3dXEPGHF54galHen0GidX0pRJAv2Ydi7t4G2Afa5K6Rxfo1hTEwkNt7SA4GnDEo1tYrXFj82bW2K5aoj7jvlyW7SiuIKSKh_hXbkbnQggbCmTfsJKsgXEfXONadGuUZX8tIfS9dTwKVQCz5XuitZwYPuEH3Yk5dThZDskVWLT8VHdKUl951uC7AogDsjBXirAImrsJ2JeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcS_L-RRfp46eqbAE0phx-kIHmy0HizRukJ-NAD1Q53Ty7ESfFe_47nD9cv1L4sTiukK7aiPRh43N5N-tp8Zp8IFVbjEHBJofsokitUi55onKXtLs265Q8fsBnBOiIZpw4-KPd4QHxxzK5SeKY-07bBxDIisLOf3yfIxqYnNnErMAfCABOBKENzQWu9wkmlpeKpAf7iVeah8BpoeggyrJ45kTdhPwG3jzgA6MDlM-k0RcymM6tQvALkKY8HrCOjSvIqV9b6to3IcdnZPuOFsva6Q8Im8KzEcID0E_9Zl4DdQ2x5kv2JXiEhAL3v-4qpx4q6ataTWpxaOcMzpLVhN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=BEjWffoYLt798pbn5hztNt99PjMS2S1z7p0siN_5aAQ--dIZvMMNf9knPmt3TReAADdXww_ipYqRN-QIjM7pVBxkkjmi94IWAdxfECqm5w68v-XiY9k_J5VZvQ9ciMiA4VY5OZGbbciT_b9K25XFnorW3ZXYeDt5nHwvxoRn_cZWcDbfB-X6KBOxsBuJxqk16MRHZNHNnph7TUqV0q8MzofdNdK4xI-bq4bB8oz7-AFRdjQ2NSK6qtHOfGC7R6CntRLrOTtLl-h44Fx4oStVnN-CLo5hEeZb02LCNOlZXRQ2CmYgbZZhdi5OASWncgjzC1DSbvEPeUDdBVjjxyRndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=BEjWffoYLt798pbn5hztNt99PjMS2S1z7p0siN_5aAQ--dIZvMMNf9knPmt3TReAADdXww_ipYqRN-QIjM7pVBxkkjmi94IWAdxfECqm5w68v-XiY9k_J5VZvQ9ciMiA4VY5OZGbbciT_b9K25XFnorW3ZXYeDt5nHwvxoRn_cZWcDbfB-X6KBOxsBuJxqk16MRHZNHNnph7TUqV0q8MzofdNdK4xI-bq4bB8oz7-AFRdjQ2NSK6qtHOfGC7R6CntRLrOTtLl-h44Fx4oStVnN-CLo5hEeZb02LCNOlZXRQ2CmYgbZZhdi5OASWncgjzC1DSbvEPeUDdBVjjxyRndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-B-c_FCZ_mes1xT_tLAoVzuzEVbJWg0vowDqcBn7BryDES8ZlIkVFmgU4FbUPKxliCtvnCdjN-YdDQH8yj335tSwxte-m8Ra4nZ98sXCsITbbYudl8mH4hUjwTUJr3RPLpvLXgqNezr5XyWADIpcCWied272MuiMd1bsnTzzTpbs5ouZLKlVACatJyyAjxQT2mtYSBPU3bZI9tvVAFdaQioydJdLKAOBbXdKhUhhnXAewU7iROp5u12kA581ESQDVbiOttK4qdcOt9oLHWuw0KBP4GnxLB680jzkX7U4VY9l-o38Pz5g7oCHLBUEYsuCyNdn9lflgSPGD5Od7_-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjU75pq4slZIh-ti18I7GipxzqvUjK9KW6EeXVihE4wCrtAOoANU9kLc33Z7eETz4Imc4GmrZvHxcOniFKa-pMWnTf0BbLZ8Ywp_dLHOJZzZV66APvYO8_7_0-TtQlnLk9jQZbj28XI345aHUOEortekZKVq6-7A7We918xyc63xvuJOT4pCi_gJQBPkKkcVON58MHqSecxOrppfDGkXWbEpuI2xODD9niIt4CGXtQsuznQ_24WirPLrNI0rYU2_Sv6n_4TZled2RtHNHqNpVcV4rDRRfLO9m_4hziRyVGdFuSxhGo7HtEgO-b_d4ZOBukYBLYinUlcsGnHvdIj_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCS7YZFlKMVRXOhMGySA0C30g6LUbk-_QtEd9OisOBQ40zri7BxDYS4H4uXd8zsR4fdkE7kKLOOcd3a8WWXPa31sJ3pFXMLMixe31SzQBXNGAo2KMflwUEYOAgHU-D7nMM5GsnNkiC27uDVrxRUGr-4c6i0-QY3BzUkOqj5oWaYF2F8UxSba4z2-oTi_EYnthHe6MXVuckz6Cllqt6OTGf2Ybgk950mDaZgsYy-53XGP4jos9eFJikrolyotUbPWGnGsQTCd0HtV0j8B9Mnn5ilWAcP5qN3xhvCj08RwX1MlwMGuI8xIrXRJmmM6jyEbBJMYsJAMFrGttfguDoBWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU_NX2CyKt5Yc10n9AylWWqTjYTqiRNZU5A_sWmBkS6DsrCkgBykoFuQScQtH6084BzpKJtwhNmzR7muYLImN0Ovx6bQIXrbSW_vAHQ4N2cGeNBmgNpse7Uih2ZiVDwZ8YW4BC-QCJM7MQPar8am2UMQ5JC5gmGc1qnjqSqz558OWjIYCjc4AyTjbTjdi00lND8_Pp5NU2SbzthPKRR1_Ie8bHm98eyr5Qjr-j8BRL9S7WVA64Hd1AdEIYIRx1hv3Uu2bEpvklcqbmkVfPNb5gPljciuswmZ9EhzR2ltU5-ISvjbfok1q1x-pNf_2sU7qeAh9nEVzpF61ZCtQp7o6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=ZOiRmW1c3qpIJYQeC5Ib6hmifrUINzlHWyDcNcb2mRw96Q9kr7G1pn3mA2QDwXnRMTKfoprPmegR6kOrA-9iKVW7oDAJlzz6vj92dhUrGyZ318DFoPmpctvPPpSQtkM_gpRri_jN6z9D5_jP6koIxJSLXf4aLevZH0DAZ4tShx2vWXm9j-f1pX8iM5pDE9XAYYRKELs2ri_PJ7omojMSJNIBK9L_dDvMTIhm2ZAiUXrwOU8XLeEB-gIcKv63p7CHZQ5PxsW733Vnx3wnb7dr-IF1OkAp9h9H0Yhd8MTTLqdjbelDX-_1r_Z_42aD8nMoaMsZwSXDRGzFDwfCjwB7_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=ZOiRmW1c3qpIJYQeC5Ib6hmifrUINzlHWyDcNcb2mRw96Q9kr7G1pn3mA2QDwXnRMTKfoprPmegR6kOrA-9iKVW7oDAJlzz6vj92dhUrGyZ318DFoPmpctvPPpSQtkM_gpRri_jN6z9D5_jP6koIxJSLXf4aLevZH0DAZ4tShx2vWXm9j-f1pX8iM5pDE9XAYYRKELs2ri_PJ7omojMSJNIBK9L_dDvMTIhm2ZAiUXrwOU8XLeEB-gIcKv63p7CHZQ5PxsW733Vnx3wnb7dr-IF1OkAp9h9H0Yhd8MTTLqdjbelDX-_1r_Z_42aD8nMoaMsZwSXDRGzFDwfCjwB7_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj-dMaHVq1ppn_UtaZ_b6wBVKQkvceXNQVSQVLj2xfG4hxXwbbMELRZy0Ljpvf4HohAAqncXDWVZ2H8PDzMjncyzDhY9YFNoSbw7JJkKtsmA_pk-L-ZWWjbxChG1wyqQKIhsk0DXTQ-a_lbSRjYmh3ELkVk-l2ASQnQ8TYzwLN1fZLEapvDTlzmHs0JljLpumgEUH2GhIrUNA4iIuT-M4NmzlUK2Q_NGgHtB4HD_6odVXe0qtQtK_8iAO_Fyv3jSCKJLiLcKUQpcPPOxtu5AQkapczrAyBIBCg_h4zaYraLdNeZAr2AohnwFZceSRt7rSh1CXvtz4ofd-dChcyi92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=vkfqwA8H1GawnR2HRD9W7AuABtvBYof_lcpWphZsqw8ph93U5KLD1IS80xL3sDxb32sMhWjlNESp2Wh8pGqr6YbODm9sqJc-YEXTjobDc5Jq6_dC3j-JdmBGfQ0FMDnnvlFq3zH6p-zSoYfcLXHbb0PPuKGv_N2cg0c2r350cFQ9-6cP_KAD3lzpm1ouCugYRa7zRQQHL65Z3r8nr9-AWTzLM3cRXv8roOtB9C5njG65ezHjKq2zoyWYKuIlq4L1-7a4vtoSa_G9KVPGWqXFG1LjI4-X_z9a-d9E87-uCfzlO7afVplXyqmaWp0jhzhxl3bPDzUPsaSi4TyHjQBwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=vkfqwA8H1GawnR2HRD9W7AuABtvBYof_lcpWphZsqw8ph93U5KLD1IS80xL3sDxb32sMhWjlNESp2Wh8pGqr6YbODm9sqJc-YEXTjobDc5Jq6_dC3j-JdmBGfQ0FMDnnvlFq3zH6p-zSoYfcLXHbb0PPuKGv_N2cg0c2r350cFQ9-6cP_KAD3lzpm1ouCugYRa7zRQQHL65Z3r8nr9-AWTzLM3cRXv8roOtB9C5njG65ezHjKq2zoyWYKuIlq4L1-7a4vtoSa_G9KVPGWqXFG1LjI4-X_z9a-d9E87-uCfzlO7afVplXyqmaWp0jhzhxl3bPDzUPsaSi4TyHjQBwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO1mCH608gCiSWpIqPr7eydEPEOseTfhVsN_WkLVRD0Kd0LQSmB8v46EIaYPdUVvUj9zmWd5b2p-vyu_3ecWia94odKb_Q2zUWAVdnnAvaM7XAx_DI0_k7stRIIOaroq4djKAQDiPQUvF1sVRtG0z3TbWdNDVvWxycvjTwSO0Y1zo6pBJLPcxg3nfsYGuDuUfr1pA7wLajoSBVkX_5XxTmeEy3OlwnDERsh_pcbabNDM4YOAeT_DuxOUgbrRfOSrptvMwJW7ylF1vwn9kLsqO8a3RaaJ-SwcoVV_oJmDciErb0sAzakq9684cvJmIAx21Xw33B0xE87fNKxgN2DFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKACrIQ5QdkoDA8PAFW7R8X7QPmju-Oeus_IBwRxQiP3500A1mJJ_6WAXPjAvsU2bD2ylPi7fUyri6FjZinqRPKaIMPlAmrXHN1O_6v06SELhy7E483_HGDTXtT8Gep2Ekzakv62Bnr39HxOdZjpRbqyhYSTp7Y1ncHIs1wa_bC-uovlvwXl4H7Y2BQfU5bjSIse9Ltzp6oRk7KkUO3mkhTnU8kya5aPFU97ybdt1inqv2yaxRF2LqSa3B2BndzU2ffpmAomcHko2F6_Ul52bkehF6ISUaagW2ryqpi287sZJMJQwiaoWJEfSbjodFwR_ScsKMtugvF61Uek6-FNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_UAv-H7nuZV9nG-2kvPqo7-JYkhMpoDyME7Ca8qFd-AblMPPaRuIez7rypIY4s1MJy6l5ad7WEopphH5m-oKzjMCfQPy9SSE0UJ3bYY-pEamLfEkXvk8vETViGvY7v8RuaqU_Sik3vOnVTLBqKm44wtrquQ55458j8BXRqUA0u7hUlTnRoKVe3v7wUfjhjxKB-CNJcbkPMZknN-K5_YiUMf2gR3gStVl-XPCekRAEKTmn1r1KMdPwkoqWK1_MTkaGEosycdoEIK2978ZDLARRBDnLL35H0psGAIBZiUrvsd016jDNaq9rahX8QwO0HyeSvrS7kz-W6s1w6r-cbSIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwvNJDCm31Xnk_v47HBykJhTE1URcQvM7Jblvu6IhdbbGuGEpRC1UuhEeWoKsKgSSxB1IsBrc0KDQMk6GuGEm3j8iVgQl9Ust5EMnEbWHVDdi9B4qfS0SqFDLgaHBQV2WtkGn3w1kmL471GSyA0strrdFdIzj0P_NHZ8o642Fab9oYmpUW86c1xPOwqZrU5pWZKKBKc1_3KCpbANxBLUOEIIqLquXlhZB6tS8X1rgHa_nDRy9_b-rAvYtYZDcYtA3iu4Zt8syvo0cml-XlEu2IW_-kN15gDHN2b3ZgBeHcLd11CkAqcplyid4Gb3wJ2VOKxJXJM8X-3Chln1wbsAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=c_qIJZkycvLTGpVqBOsrKimHSfEBRruJmenLMg7t-Zq8WlFZXC1qF-Tb66baWIqlSDpaD2abFKKY3F6vm3PqyVX0m9AXblgBtDBjP_9P0UqMt--nTuyrmzWXhruvrRJOX6uEju5SLfRPZdr0kX1SNYqqEYomuWqq1x74V_j1S22IXYIC4JnRyXng8fnjHyXDcajWMPVD284WGENdMwoxnKSTzpAZa5WG_H4EPMnJsFUEAxkEVJRPm0lgc5w8VLHSk9vtajmQ29OhJOJO6dm3_vrGXQKIZkMTYO6GDM_blpXBd4mC8S6sQ-CxkmMymFPoRgUva9_6jnRNLE0EWq4a2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=c_qIJZkycvLTGpVqBOsrKimHSfEBRruJmenLMg7t-Zq8WlFZXC1qF-Tb66baWIqlSDpaD2abFKKY3F6vm3PqyVX0m9AXblgBtDBjP_9P0UqMt--nTuyrmzWXhruvrRJOX6uEju5SLfRPZdr0kX1SNYqqEYomuWqq1x74V_j1S22IXYIC4JnRyXng8fnjHyXDcajWMPVD284WGENdMwoxnKSTzpAZa5WG_H4EPMnJsFUEAxkEVJRPm0lgc5w8VLHSk9vtajmQ29OhJOJO6dm3_vrGXQKIZkMTYO6GDM_blpXBd4mC8S6sQ-CxkmMymFPoRgUva9_6jnRNLE0EWq4a2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU9NbOWAjksnaUBXiKK-RdEKDX4odMPE3Chdbc1Wm3s4uCKtF93FTchsoyxTlqf2QsI4yzLWtThPbOwuKorw4vZWupxt3FjxpGa1wXmB-Ts0nEFHSYcq5j4Crobg9_yOIjWlZ6JmmwgBxH2Wgo9vu1GxkVJAZ6YbmxylmbTCzlqNDUOK8eqmLx5ktQ6hfypGZGTs8w-xANptgEQxCY_eC2dbhmKPlbAFDnjWIBnj5LgGlp-yqPFeGi3agwLO7gK-Hpc5br2-7JFCBhfXD_cD9ygN2bdxLQ7ZhtbXJ2e5t-8IyaLMM42_uaVEeG2ptbBf0vCELZBd0pZpB75ZWyTUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2Den4QdSd0QTY-EICPpo7-TI20kmuEj7UjJyzpzMDHgFU6xI0edHJj9sUHeS3wvSAcqRbHWhdSsAJSQH4ua0Gt7QKQEPFJDDyOJiALtb4Aq9mu61PJqPdTXJYL8Of4KOV04sBkaxQ1Mqm8ox5z2bGALtDnBsVxC-dLb95VGZyiRCWgDoiqYPqLqbT4-UnJ4v2RK8avmNUJanbhLnYj8Mv5LwS0-CMsnY1zDBVEM5eFpM-ciYUViqeLUIvSwavNqAGaAZZGu7ZrKMClbREsMHl6a0Rqfz9zxhjoHaQptW9T8VdMqICV4vH2Ot-457YFcU5VvbvqDDr5hHq24vaPMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC4IVPyX6TDKgnQT8C0ruOmDC2X96LHNXH62NuwdSSyJSyR7BePhe7JqL7akk8N4yEHc_FpATV03-QZW9AJSqlFU9B8Wz8QaYwP_WNWHp-19OKyq7qVJ7ss_tJ8_K5PBOFRnp6Mt8LTKb0lwxuY8etfiGQC3wY60uQXeVaKVgrSqc8Ch7Dyq7D4Y9mRw1QZmBpz-znPc5FBMjJEmDRYIZupnf9GfRMlitoDeXCGpaMHCeHFKNCOniAUZ7GxHwfQZp5Q3OmgSCqwI3TzSdOwS7TtJcI9ewY4YLA7Id-0o-VN1M1zjNeva5uA-YQ3yhSJ6eYfF_ycod2Ksbd3Bz2k94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=XdX8eFwN8ixdAUs6cPkHmblZ-ctGMJfSChdxsKoRWxPB88Cp3R0ocrePBZtBDpXIlJ5OmwdbAMHemo5NmJcCMiixVw-MZZKOFX08Mv2C8Bx1e07xiNPjxuEEUBmBIJpKpwNjtoqvHU7iyNKo4vN4BU_o1Zmif2Kk1Af6_Eo50iKuu24iou4D9M0kAaQ166I3275h9RjyB8Up6PhEmhPMlimrHg4Ttr1-3jOoeOGGm3sbbG-66J-NEhFLYSH619KrqcQBw8YeNAuNWbMiLWHuRMbFXZ-5hjMVLzV0G4nkABb1EwRFs8832RvELMWz69iwc9KMfSwhSuPU8c4igBbL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=XdX8eFwN8ixdAUs6cPkHmblZ-ctGMJfSChdxsKoRWxPB88Cp3R0ocrePBZtBDpXIlJ5OmwdbAMHemo5NmJcCMiixVw-MZZKOFX08Mv2C8Bx1e07xiNPjxuEEUBmBIJpKpwNjtoqvHU7iyNKo4vN4BU_o1Zmif2Kk1Af6_Eo50iKuu24iou4D9M0kAaQ166I3275h9RjyB8Up6PhEmhPMlimrHg4Ttr1-3jOoeOGGm3sbbG-66J-NEhFLYSH619KrqcQBw8YeNAuNWbMiLWHuRMbFXZ-5hjMVLzV0G4nkABb1EwRFs8832RvELMWz69iwc9KMfSwhSuPU8c4igBbL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvj2GOjm8b3_M3JsaimsjukRIOy_QXZyW9EPYJ9uarti4fz9RrGu6gEz1tBxhJlMDlmVcUvzyP_lPMMC18cN5SxYHmYTLxwm7zkC8FpmEuLxN-80z5pcLf825AImGhgZPffsgqOZsz0e1PiBvKQVuAaSmh0oNTLTbIVbUJydeWO941cQYRS4D_2i2H8hNLrQUzFYZ_dWeZd0KhK-ud-7yzw4pNgcNERz_AuGA35vS_pSFGmnCDPe_T4Q5UlCMB56vlnQptugr2vby-8YkSpluC9UIagMaW5LCSzs-Q-ehC5tN0rBbH4Q7YIw6sZ4Fgi6X43IyA-vzIIRPPtUWMwSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBxyfmA7QXh6ecsxIwl1AIc8tql1hZVKs_Dfa5Jsjojlaegu5Liv_W7YGiseAKyCKtOJSIA0qJxink-lMWL_UTGUB9aEwoK367EpxzhV2X84qymoeVhoRq-3jLsdEcmoR0RaTRD7Vk21WvpDR4EnXmS4utpAYZkdv9Nkj6EMITAuJIBEFdcyB6Hm4OHcpHH9c_8EPU6rDKYIRJ5JPj7mh8d4NP1amgwEKBiZWIuj1i2PnHweTk5f0fknAKNYbSsnC7uUWN3Cl4Oio4FwuWXd_xFHbfwqSZR9nO0JnQQdrRB-u0PVNKwyXsxZdZiiqGCLp2Brb8Fq7YZAt1KGh3T7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6rzuMAXVwwzhfA2w5DXRMEVr5vHeTEXAPt9JX2b2weIRwLnkr6U6YEseCuMfA0jna9TcDHpLTGoEJFw7OD103dKlREU7F_pRy4AsG5q-K2JVo3-LJX-gwE363qNUNn4T82cXvqm8iRpvApLRiQ5w4su92V_ryYRj_U-LVLrhvodx8SAQUfFBWQbY2X0Qyl130eODwoo2mwnv4Fzgnvfvkk_8JfwaTii_Hw9FFBBZQTvz4dN14FuNzKgjIpuzBR-xnPlv0m4zmjYE2LssHREWSImlRE3O80_GhGxd19m5QxAQR97P6rYjM96ECs1ptkJFCMv5cJGdtv5e34P4reWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=qrySUieDE7yH0YU2JzcPP7UfsSdo82GvwOL6w15OLPDwoJDAiLQ80g9m4OCZXxaYXVB2kc4Vnf4PS_2MgQadejzfMRQXROuhkJrSPmCIPS8QxB7QzSym8rREl8pxrL6bdXFT9byV0_kQymL_rR2P8aAQrgxn8YPBC6qIs9-rWs5TL3ZCMxhXBMbHPMYfK8HLniYmOHFL2ekeG_aPaWYD1BCSRCAnkDEoMIWOGNE5wHA8o2ljm3JITf5d0wsxphUBKsEorD5Fr2WPHCTja87i-F5FAQWH0M-VrSQxgHij7fMs_sm0fpmYP_u4VnU76Rbng7RZpu-dHRIm3XG_CRSGyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=qrySUieDE7yH0YU2JzcPP7UfsSdo82GvwOL6w15OLPDwoJDAiLQ80g9m4OCZXxaYXVB2kc4Vnf4PS_2MgQadejzfMRQXROuhkJrSPmCIPS8QxB7QzSym8rREl8pxrL6bdXFT9byV0_kQymL_rR2P8aAQrgxn8YPBC6qIs9-rWs5TL3ZCMxhXBMbHPMYfK8HLniYmOHFL2ekeG_aPaWYD1BCSRCAnkDEoMIWOGNE5wHA8o2ljm3JITf5d0wsxphUBKsEorD5Fr2WPHCTja87i-F5FAQWH0M-VrSQxgHij7fMs_sm0fpmYP_u4VnU76Rbng7RZpu-dHRIm3XG_CRSGyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTry0AMR8hHYnEYTTyDqh7OLmXMtEgm8awL_JewujXCArBJO0Hb3tzgKZXkwvRHWiAWfJBhR2NZK_PTTMhgkd56jbxdo2ciQko6E8l4Baiq5MLsNsoebFOecSazkddOw7AqsDQ_x1XmUqmXaY89Qcwp5fVwsir0bZE3bfBVOpi7Foqs1Ai4fqZAndXz4r6_wOFRyen74PAqo4CLvKXBVHDvlQ9yOkyo-GQLK_aUhrQo_ZwB_R-gRs7HDUtHk5tgSt3xviPLBr_NXarYovoSpwN-bxaJynZICa933mZlo5Us5STVMUMypirtjlAfCQfyRcUJ8J4wRcdpPDo9t2CtelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOXslD6Gny5DifFqn0vqb_NpbOceLbQdFD6nC13xF7ZnfecU47ctWestScsoupC31FOYWMyHTAnIzLP3Fz-HdaEG1d6oZNL3_suMmK6BgwxN5Z6OcFibQCowqqVw-FzbXrRlg7zIY48W_QFKA7Iw51OASHf4rjkayz-nmH5GakldJP4cSgvrYGS9DNEOYnnLjnm6-qIRd04dX0p1VHWH077uE2-5j8HJftUytZ5vAsL-apz9-ZaYNWQvRMaC2gEAXOAJum-GjoCR6WagCuTuZMF3qZ911tLl9z_CiQZrhfUPmX11BuGPRY6SWbYr49V9iZLMK0Hu37jRm9ZotOXBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQR3UoSC4VS1m4Zj_rYJYqmoSGRg1kFpEqkNQwx4TlPtDVe9fG9nUXNwALbnga4Mljk54O2qM64wXY7HJd8ES2OOlOwyTty3YuSjw1OAw6NTrFjNj3Uc8pPB_h-ghasE2yHyT_bZlLTrDTKS87EHB6Z46FZJpW7HGzFzEX6gbQ_nUpE6DfrxjfNXHLeoCfUpemZBP10GUfulXiexS9wYlRBByLcmJ0wsriajrbShz2whec5P4iLI8qmPJvUoRUG94bVZYiorCoBYZteoUtMRrn-utoJ0dGTxvyp3KWAq4Hwr082C-glGJIk6GnAa8feFH0qnr21hxGnLlZba98-ZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQVy1aR6ZqLi3SZrBLEhYED07TlsjN_tSbUkqj4CPInZZMGJNSeWKuCiqkrc3-Llwnu9Rs2b7fg0x0hCVoI0FuJ4anS-rKACCE7p3wqn8ZS6AyY7eWoj5CQHlI0XHcEAg6Y_7H_qsPXbJhQaUYvtLZ74WG7LPLXYhtv0rGUdIr9W4Ot1mlh4EXlMgDUhwQeS_HYT5H8_QQYi4nkJa3xnqCtb5QBocf2vIBkkn3b8muPxqGGgEVl5jjOhhLqfyrEiP5RzKJJ7HPTVnhe6dUco_e9Z3al45HhVQpD0EDDe73V_PIGUE9QnazmDOPurNdk_COEf9ZcqaIUhZji_CjPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7Q32_g76an7bu9Hw4j4iC9EIdXW--_2bIfvzJXhFjWSCaTYu38RdcdLpeWWfcSNUNZq7EPZt58HhCaIQbpbBFkhglTELM-Y7pg_wfZme9fGqX9y5uKi1dlVgYo_s0owXTvEKw1RZiZpuaSfYMWk_JtuVeAFHfp7fFhlFF8zBh700ObzO6VFqsCWCugLMSIFPFK0elJ-vzwQ5KV6wy3Xz1ClgCuXm3Lz6pM44KWcFMc1K9BTXLeD4dFr-wer3i_691ZecZ9j0Ib8p9fceD5vKeFfT6xyJLZWy49T-cUtUrW-TJTkjrMPAMum4BIUhNFZibHd7xVXIoyisZRijdwlmO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7Q32_g76an7bu9Hw4j4iC9EIdXW--_2bIfvzJXhFjWSCaTYu38RdcdLpeWWfcSNUNZq7EPZt58HhCaIQbpbBFkhglTELM-Y7pg_wfZme9fGqX9y5uKi1dlVgYo_s0owXTvEKw1RZiZpuaSfYMWk_JtuVeAFHfp7fFhlFF8zBh700ObzO6VFqsCWCugLMSIFPFK0elJ-vzwQ5KV6wy3Xz1ClgCuXm3Lz6pM44KWcFMc1K9BTXLeD4dFr-wer3i_691ZecZ9j0Ib8p9fceD5vKeFfT6xyJLZWy49T-cUtUrW-TJTkjrMPAMum4BIUhNFZibHd7xVXIoyisZRijdwlmO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJPZvMkM__WdCFKqWJXO5FBrxBRDXFatZl00IMbTaI-2713YgQ9VGH5bA_sp5156L-B8pqVBbhI4uCrSFIlAtZSqq2ljH5igtmwUInDvVY2DIIYtHDjJICbs2o9k4azpFun45BQids1rS564MLPyk9mYkd60txV-9-Yt2MwIEYwrW5LJLGHBuHrMANEU8OlzB7RwWTNrzwwVOpvuBPvt0SkIjFe7XllpoxS_gCJgvWnWQoeXt40GzQkheqPIKBAbhxBFOvktYG5Xk7ZmYkk67EjaA6q91P0ZQFH_CTNVmM_ruQ7yx32nGSwUr0KzZKXONsDKweXviL3sDHYUe1TdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsmMTHyPo0H3T9y24MLFaayXx2mBsrx1v4ZfAoJrt8Gp77BNx6dDrfD87DNuXb7-LfjXsb0Kxor8Lrg6gDzGWjIK38byiqjaYroW9YM3o6lEw7avikiZPzu45CMjfn74TsmplEgCGvqQZoXCIXPKNSodXO1IkutdZo29Zs4Nnoyq9EKYK-KnB4eM6hHHifCmS1EE-Oq2a_0Xl0WJAS0MBUjrrnJFEJoPJ9MqjatHvYbcldtqg7i-CfcyWWL8n6dzhTrFxNn1ISy7y1IhC51xskkA5eQor5gIAQCW3ZQ7N6joL_cchvYmMI7rgiRqrQ1nu_TtlD32wlxW2xIxtpJ3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGbn_u_uvZG3MDIc_eSjtMR-Fs5c5I4oC-HAGoBXKs05DIhHjvd5f-Bau1YCUUDfbsc76GCXsIX38KuX-JsGrtMmiGzv9t8jCp9b_8CAZXottB_eUJ929VYLqgjPqrHCf05SR1myijrwefAXjAYfmQuQ-15b4nZqckEL7XX54O2zidciuosUX92F0KE0zfiW_7WKQzfyIdrD5_e7Zmc7oa8k6Qdn0ovmBDai2p9iurqSxgYq2yyj9Za8R66LKabCU2kgSfgoooK6USzGgbDk8YUWb9GlnaeMvSNHBdP4EbA4MuhL36yn-QX47KXSjJr0-4C-YJoFZjQL4c6PoEG75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=aiG5sXW_IArnL7tkymp6-Y_QoszKWAYBXr4bz44Gju6dMNaysx_6pJqKIexfA76MsSqcPFo95gpUc8JFh2ExRVj6yxXuQJYfKyTjfAp-fy8JadaH9ADdnitKtn-wC8QMHFM-UHXHDKhxtmjfYd0PV1Ce1JwGeWUlfyvemKZezU3t7jlCuUOO3KcwE2Eyw4MlEfaPGN5lTQR-1ecAko2Lu6DYnvcfH6HF9438CWQDRg7_7Kd5ZiBzRoacBw4LnknH5JQApwAk2UJIMs502LQ1qZ6WFKSPGJGM_zyIkOwecfUIK5gL562ahr08PKA62h6AWYnhsl2iqzN6z1xVeKukzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=aiG5sXW_IArnL7tkymp6-Y_QoszKWAYBXr4bz44Gju6dMNaysx_6pJqKIexfA76MsSqcPFo95gpUc8JFh2ExRVj6yxXuQJYfKyTjfAp-fy8JadaH9ADdnitKtn-wC8QMHFM-UHXHDKhxtmjfYd0PV1Ce1JwGeWUlfyvemKZezU3t7jlCuUOO3KcwE2Eyw4MlEfaPGN5lTQR-1ecAko2Lu6DYnvcfH6HF9438CWQDRg7_7Kd5ZiBzRoacBw4LnknH5JQApwAk2UJIMs502LQ1qZ6WFKSPGJGM_zyIkOwecfUIK5gL562ahr08PKA62h6AWYnhsl2iqzN6z1xVeKukzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWagbzidrW2yG1VsCoMPrVS4jb_Q--nOzIRoYMtSMw_-OGt8ivInmDDdmfBDVm805rQRlg1kGdTc1dIloekaZdltC8faRu29mNdS1rWof_BKkFnPcBNDmkK-_OxKcMVXChwR4lMX_kNRRpVShLlc9VeWKbQvJRQYbp15XqisS-_2Smw93w29k0V2OruNDSE_LekRMYNpG2Yyq-m47Ke27srXuEAQpr-3KJAtLIdYw2rJAuItqiOK57BpUhRY9LZoJxyJTRDKOFM584DohHj_LmtqyFgce6B7qZqBdcvS4frgreKWlWTe-8CVgE8D2E3AfiRXZxhzZQ9U_1DJyHkqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-YXYhlHE0srFfmCknLlpsFrxFYvb3n69GqCU-GFW1fUOx6U4MpbazOd7rphRTnSj3TBvjrc1HQVFC_CkBZLrWSuWRDyPwA1SaVk8Tqx_J61iQ4yatLaQSyyLyIQgpIZLM7ye0dUa-XVDchwEc6yHe3A4uZIXJ_bIw-yQlXlJJBl6oT0tr2do1rHPC_-zyCXSlubcY7fvVzGV8TRxZjHdP7DV00rMtGgPYCvR9P1ZuwBeMEkdjTdL5-JtzM2CeJ-z4zxd_uElaTbX65NWcb-OrH2isAXMSrRMsC9IdbZNNhnC7LMV9hXxpsysHDd4mQob0dnvzf2xZm5MJbgITluYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FDuVPphO7XHoqqeya1U81A726sFzu4T_zsWWMh-TywtEJGcabNxVwPOoFozg5NSnZN8q7Mb5f85J-1suHcvYpDpi4su7L3kpDDdEJNScSbx8hBy-6Jbln1gRygLSe9F07B9qd-FoMCL34Uhrnz6h9x1_lpy_oNtHl4krDea_0PFKLqdD-QH4CLiJzSgbdXSwSdqz_8l8tmmc2YapSwEldM6T8ZyrnEREMqhmJCeSZ-tls0b8wkzrDNu4BjoT0gJEaYDl4gE68X_D-UCQ2WFoKc6ins-eZKB_Jm8l-OLrU8LY2_HEAkLCF38emXc-XpZOtE5CnWQylv-qnVBbHp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtR-xh9wipNjqLvZfuD_OXeDQBHyTRR6PBeh35lRcHrazomy7_P0SeZrWO13LwFaZmja-6U_ijWeWwUkhbHkl8_PUSUYoMJLKCLoZR0e_o__DyNkC6A6l9eAGpZo6OPz8-pOxd4iYLzlX_9ZNZ_EmU7boLXBMe-4SeDBScReG_vW9uOBvrcpli92T4bRgK8vyUupyd8YIYkiQQKzislUsvlPPZ6xpxTrWTpFJC6XZbvleyOXIQngsMfsOi7O6MpmGv6s1qD44Sqzt3rkrfsJr29hzPryIZmeyaFHDsYHvYhGEXpHrJUSom0lU8c9G-hvRmRsVCz1GI6rH28CX02LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1EmRNqZ21My3y9x-8DyGmmkM1edEDye-k0HTIEBze5Wz5BHNTOGZe7ci6ZzCzhc3Jvwe_dMdo6enoXp1AKsMnjueyOtzeUIT8SwvJ6iqEYkTpVe0SgCMs8hm8lsfEKzM_knWphdxvDw5CNTBy7g7YngSLyz9eWUnCF9iJ10Db6a6Hely3kVpzBDULH2PimvMD1aSMR4RaJ5E6cjpI74Ftvbybzz7txzaz26g_kfS162MZP2u12C8dIwAAxFyQSVhhcjesaj5pBcBHgaobGA00DNl1o-P5BJNP8N3AKhGx_QiBWnemgGJ-bb2v7CjXtGM_dreFxD25-bD0U2ThFUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kESu3XSdjFsMFp21QbHYbyk4kOQI8k-KPVYVVLUqc775VZvVYtApEVHEVGWbKNRaXjs0KxtE25DApIdrJLs03AAKpXVZmD_5oTg2QGRWPqxrhmy89UPGwWAOfakNpFyqNFcAnE7woiugA5xVCzNIcG8zpLiQ2HdhgpVNPi64l9FagW5YfBvnHOaT7LFf_1pBOX5Wz91G5gPKJO3xlvg8skFJWIeOED0xbDWFp2eEVtz9iPhAhyArzgGIV0cgSTWhivDPLsa8x73rXrcDQ2gqJ7raCGWwB3VrP5xuPXbc0PuqVi1-XZEa4SQSRUzF0I-OaPzWEzbiXOQ12yL9gtkOqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru3FSo4TzEkD-Mrh7uF7us2_xGR7L0OjoYu1uPWcFnMXWsh5lyUTfyKc4YrljyqgzjZGC_y_XWJMN8JLgYSLmqhPUUFpax7iYE-kULSr4Dk5fNEMdrrTEmlPLMSFDPGIIXpn6XPyCYD5A4FPKncHKHN0rvZf0DYbUCqoV81DbnoVYvmybK2d0q7xGK_VokAF3hrJAFzWH9gBavICepPPASfFrNujm1734cc4FP6uLT09u66dSQVRTFcSUxbU5D4LQl7FPoIJ2FxCAeqjT4Dqr5VGLoU73Nz-izdJ7WQV7FJ8pVLqT4IzwnbNUt_kc_x-h05BBnhOtuOPieAucTu0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDNqzHJZj4ImTr1Dzi8tmjfQr5cI-zCTB_9fexb5vUxx8qx3g8OgvN5Y2jVmf2osNi9R8vbjDG_jHeoQzvbjysbaNkV1WCWrVTSbxuGHd5F1x6lFtFCtJd9wGW3dytvD4Jxtwp2WSILkHUW8F_BMg_atv2R2DRgPkhG_k6e9Il01pXFYPGn9BX9hcItWdz_sWNw0zGI4MBtXzrpMRUBh_Dzcb87FsZsaDNIElpyaKImIpn48AsQk_S93GI9mxz1BhHbOceQK07K0UDNuVBaWhtFI7R4RVXRTc2oWBdaHUqyPPhawJqoK858onH2RO75CGMfRSZbJZr0p1BDYk12ZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rErCy1n9jf6r9hGxoQ8DRvzLMcltTlgzrOnqHLi5APQ1Wt56wnYnvDLkHb1r29s08pfdMyb_vhmXL2ikwNyg9L-uV-UGqXDW0qSbhyA7cXG4qAsERIEhrxFjqRJ8MTMn9uKgV1X6keg0bXZPxfpg9YDwcenLIuoQtUU8nvdr3XyQEomAbVZqvfY27nPz2m6T3LrtLQjxYiLcZAtrAqlA64zxwpmQp23LtYzwY897RdtX3ZGiXeMFG16Rq1VXHdsL4RfWHGW5mnK0GyDA82NVB84jNKfdAvXNoQp2OiCAuTHBoFCkDvZWGPuKu0xICTrywOmrT5B1pWaJJPZhmUaZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=OHemKf78hZOEgtQW76s2Yo-sghGyjuVXYDWtd_GYLPcD2n2V9PEDI1bBKvZyt9gfk22zgpPEX2mMZBK0nNvEBOpb2lMN-Gg4-7dVBgYkeLn4qWwVb2dKg7pBI9GnSY3GUK7NDuUyKWkPdlHRCOlpwwSc_G0jCxRSaZ-nlyOoCGFAVjFABe8K3gu9ZbC0wamxuzJaHPUJprGkomSsCW1UebYy7YHogntU3Z2iUJbK1RWwGPRBE-puMhbaYjuMOw8ZqOKWXAU7oKsfPQtkWBoxSLZTcevCiu3OKquxfyqZxy2ff9HxGGx2PBdfP_12YZdUyIaQBzGNqWmsLiKxtoV3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=OHemKf78hZOEgtQW76s2Yo-sghGyjuVXYDWtd_GYLPcD2n2V9PEDI1bBKvZyt9gfk22zgpPEX2mMZBK0nNvEBOpb2lMN-Gg4-7dVBgYkeLn4qWwVb2dKg7pBI9GnSY3GUK7NDuUyKWkPdlHRCOlpwwSc_G0jCxRSaZ-nlyOoCGFAVjFABe8K3gu9ZbC0wamxuzJaHPUJprGkomSsCW1UebYy7YHogntU3Z2iUJbK1RWwGPRBE-puMhbaYjuMOw8ZqOKWXAU7oKsfPQtkWBoxSLZTcevCiu3OKquxfyqZxy2ff9HxGGx2PBdfP_12YZdUyIaQBzGNqWmsLiKxtoV3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR2ECDgeGxbX3sS7hW45XcreL-Q1QpkVu6ScUnWPyIyWDd2Vt2DmRMNIg8eXMzsX23lFGI4t2iZttAEzMfdlBl8wstfr2E54-xzi4cghsEz6zITxzSREqnNypBtUQPSb5IqHvyDza15hX6CifB1slD4thQQ6rsJQ21hwEvoHCIfoyFLYjGHh9L7ESuEIanSHxNv9a6filq0wtMbha9lg-qqAcE8guzU3jspwo6cEd7oHCcXXoEolSjqb2mq0jp9gquynQC_7ErIoOih1gcAJcmmX_aEkPn3fZFmSWCoPnYUU2e1HqYNkjH4IVEZyU46kII9NVLrtBhKGxnnvfqbU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=X2z1e_B1cFBNJjH49szGg-cbcCmdSkM1LRPddz1tQ8X2G-E-NZJWeix9HS8usuSI6BjqCcS79I86zZ3wfpMPsgtSSv1JqNYf8wp514nFRFoznF-XLjR2k9y9ix9td7WMoPU8Td9WxC13ZVQT0uhT74mqj1fk5XPei2fBArKjUqeH5zVJFkJpwVx4qA4FnMxwjYbYegibacWIQFJ8fiwsk_mG0ErPMmDBky2LS3tA_AISmoqzucR0OMtsG_K0C2jRxgMhFBRm3kZgNIYesCt2nbWzGOnZ0telk-k-5N9zXvF2kycXq95E6Uem2aRnyCmtnSrazyQNj7SxL0KrwzJPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=X2z1e_B1cFBNJjH49szGg-cbcCmdSkM1LRPddz1tQ8X2G-E-NZJWeix9HS8usuSI6BjqCcS79I86zZ3wfpMPsgtSSv1JqNYf8wp514nFRFoznF-XLjR2k9y9ix9td7WMoPU8Td9WxC13ZVQT0uhT74mqj1fk5XPei2fBArKjUqeH5zVJFkJpwVx4qA4FnMxwjYbYegibacWIQFJ8fiwsk_mG0ErPMmDBky2LS3tA_AISmoqzucR0OMtsG_K0C2jRxgMhFBRm3kZgNIYesCt2nbWzGOnZ0telk-k-5N9zXvF2kycXq95E6Uem2aRnyCmtnSrazyQNj7SxL0KrwzJPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7d1huE8d53BTTASKT9Qx7QXcgYuDqjBwgReA1dqVrjguAPZedzEpxjM9dzGQgGGx7lj2xxPD0DdYmukpRPWz7TsykyVHtw2mQJDSYfhuwO5Gdat5kZasO9aBg_M5eaqXHfkzDH6p7D9qPURD5Tj0-rkU92j82BrAUOyVfvrhariWq22m8K9jhGCnSnEiJpRbG_Oy30TmWcpuOH7NCmgKzIS-3-tB3LxGLwhmrG5ZZAXAiplRcqBmtJe341fqbcU_vh-6qJ_x-9hmlE98o3YvJIZu6SB8HVSui_kMRSW8VJ72sxPGLWR67kOiIewYvk4h5OPMHuQKDtNzxJfbUzETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3EyZSE6xxEWTSSRblapujFPSTWfDEAiAh6NVWDakRL0gICKR9-wExvIVGf2hm8hHxtSOZvJDkAvZ1_HiiQ6CpU8Fju_Z7lgGBYkqrxY6aIzdREzLKQdVKemquXxugBQKS6nRDX6N8EDXk19rxXP9t01kXZwkRu5Isg4RTmTPowQOsxGIhwU1SqLcwgdrd7_DyGXiT1HKuzOgsQspbolkzYXY8aTHw0lMvU7KFGSK2ad-0xiCUyVKHeukweej8Y2y6DlW4R4V0Za_RUfLl1j6GONHI6gt_pIs-f_OsBJ3Ur-pHd06VDS0jHO2HTIKXqF1VdUwKIXiMDOoUXyq4pFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=TyUCCkrfl0BY0m2w-6rrdSoWN0QGSJKGwe9pHEQJwE3aFJ5q1u8IdMoaiBuBYif7qwOFhhgTcv9iA9iTw9QcVKhof4jv-UVFpHkSsK8G7khqTuZNhA-MesgRdIfeTRMpu-jM8FhGMGhg6BiNL3LkHOfAXLL7TNlai6WctB6AyHnd8n1MHKS4jqCBRmGiPq3jOlQFxILdHU9VRtUwcE7YMneAYnYM-U4b9yyqUrmbCfumIGjhgjm_1O9wlDFzy_WmSpI9dfMEXb4m1mOEnRGPUimkG_oNG24CCZUonz53l-lvf8xYixO5QcJOf7SW9RlgdCnEcbDwHpeWJnG7Jb_EaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=TyUCCkrfl0BY0m2w-6rrdSoWN0QGSJKGwe9pHEQJwE3aFJ5q1u8IdMoaiBuBYif7qwOFhhgTcv9iA9iTw9QcVKhof4jv-UVFpHkSsK8G7khqTuZNhA-MesgRdIfeTRMpu-jM8FhGMGhg6BiNL3LkHOfAXLL7TNlai6WctB6AyHnd8n1MHKS4jqCBRmGiPq3jOlQFxILdHU9VRtUwcE7YMneAYnYM-U4b9yyqUrmbCfumIGjhgjm_1O9wlDFzy_WmSpI9dfMEXb4m1mOEnRGPUimkG_oNG24CCZUonz53l-lvf8xYixO5QcJOf7SW9RlgdCnEcbDwHpeWJnG7Jb_EaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm4cXvO0_LAsv-Fn2MHA8DRTTy5Okn4bhuuKZNcRaoJBKV6-h_Dcz65kFz4TUoIUK2ek1-bFnjg4Hs8qFjnu9bqyFX5MWE-ekqC8p2_0tksfdoNb29xjUoRTMqfnP6nZJw1QCjRIOzdUL4c4kbPYzK53Qy0K9D6FSuL32EPADsqJJP_Q1csH6X3NNVfpmKN7wn74atxdl9Vh8lPydCm70I6F-0Am46AAyNU8yLWOrXP9zivajAoao_5uJMdsOFCmb_BRFY4sg2WGTCUwM0edHcqqcfnufZ4cfz619zCQnh-TmwgsPOOm90JYJgqwNUuHMA5PzQPxAzo1Xz-szW9axA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpI1VpkAarxes4s8Ryn3WJdWh7j2flOZCr_zNZ3TAN0shGDC_xsfr1ELQXFRmxLsLEHsQD7lzCHujwF4vH2Nt2s0M4B60jxVYm8UvHjotB94LwsORKEbumJM6Bbx6DG7W8GoxU3Y75rhCh7CdE0ukJbYglN3nXG7RvoXDetZzXiT8VIMhlMSZ1ebLgUdPpAaTRmqHSFyygvzGZEal34bHRnSHGgFxtocO-A8tJul4Qu1UqhHqAYdx5ySzo9_bRMpJe0DaYOLGHdJohjUx1vbkZ5nRLQwYgrIOCW1BNvPPL98bslR5SbFwO5lKAPIQIHnfDTs2icu5ecjrcZ5tiEQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdRr67X9sHx4x89Ic3xWGUaGfjqfCtX3Zl_n8aJOz-VN-6RplVLE0n3B7oDp6rFS57ipcJA72PZUAhDnzypTKAMOdTEekVHxd2xR2pS60NSj4kpD67PQXwwLPALBPo298I4Q83zh-ThNnZweXy9eksUT7oUFkuInnF8PynAi-PP4TvVCC2cy6UemZbL9B5KHdSso07Xu8ouNm5NIGF2VGpAP8Ea9Mu6g24N-uOsLWWNDsbawcvJKF-MWxJGmH5ju9QQWU34d38jiIKVvcyz6vvWM0ujlPhqeE9-Sxq_jy6QwLM-bnYzhJIWBvKeEC6lDJhaZr1dJphZMwGCclG9WOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu9HKhvUSAw3WHDVWSGPIvxE3sGg4rdjnxBmiVhKVBgxYOtNAd7hWN8vL4v4CG-9Az10k3boAGVprAh7uT7yHJNPd_Qf1rjybyUhA9KYi3YKi78d2G2kAa-2gEeer4K3dpD5zk31Jy_PSbBjCRTqwS0vf3gDSL2ug_krBK5evK78rp2VEI2bT1_pa5RfO9c1RB859TACycWo80hSpof5JKG7UJ9xrS3Vqvm3zsnNa2UjFgUz2Nmb7Hd9ErNzCg4jV9Me6nR8iriDCRZUEg7nZX_8GJCORIcMMaZF6jXJ1FDoY2ELNKh_qoqWehddCi3M-YZF1F10aj21ngfiIBvkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=RJlLFMjwk5hutbo6JhPd6l-kQ3uGElLtbHImuQemxf8lKYjKEZ4o9AZw8pcDFlcfJxi9Blh9WlvNVUDpzXapQMGrwcPZA6sIC345KMoEfFVIm33Y6EXW1R7IRI8KjCqQ1J211dwCAEnkWPyGKeYUcAUOp-JzTVY8rQLf_cbnrMrMqZQIBC3qHHl2J5kbqvAhFblVyBd7GptTZDlvZLjlBDFaAeXwcUEv1Atxxqba1pDEki9d0WD-4IBnA-0i67kjcX_R1z7jwH_3D-55XQDczQTXrUvTnLXGb6iNHoSEM2recRDwkAg2DKpnHmJQgkKM8JPhYkJsHVerE-dNrmD66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=RJlLFMjwk5hutbo6JhPd6l-kQ3uGElLtbHImuQemxf8lKYjKEZ4o9AZw8pcDFlcfJxi9Blh9WlvNVUDpzXapQMGrwcPZA6sIC345KMoEfFVIm33Y6EXW1R7IRI8KjCqQ1J211dwCAEnkWPyGKeYUcAUOp-JzTVY8rQLf_cbnrMrMqZQIBC3qHHl2J5kbqvAhFblVyBd7GptTZDlvZLjlBDFaAeXwcUEv1Atxxqba1pDEki9d0WD-4IBnA-0i67kjcX_R1z7jwH_3D-55XQDczQTXrUvTnLXGb6iNHoSEM2recRDwkAg2DKpnHmJQgkKM8JPhYkJsHVerE-dNrmD66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=loDcKeRi7_Ee1zl0F-eVAX1TjzPnHCCz9xiB8jxdHx78Hk7k8GoszRSQYBj9jHwrUKj8mZF6HeI2be7oDJRyUAWOFRvUaNiR3fUfdt5ZV0LBlgEzw4giGgquF_5RclK-qlIFGWFz7ek7iRsAorqk4nPyX2Edpx9aUKN1LYGTbs56zrIHu2Ao-EXuLbSVR7KUStJRPB3xn9CGxvVX2fpnbWy-vp1e1V7bgRLs50Za72JDDuzPZnJfQT45sQpummUUVYRWXFRSCC16UYhBF3J32J29ubyEDPHhf2W_mBkOXH-g63eTAzdjdbFUN7uQwaKYc2C9_Mg8RcudoBpt-yWolg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=loDcKeRi7_Ee1zl0F-eVAX1TjzPnHCCz9xiB8jxdHx78Hk7k8GoszRSQYBj9jHwrUKj8mZF6HeI2be7oDJRyUAWOFRvUaNiR3fUfdt5ZV0LBlgEzw4giGgquF_5RclK-qlIFGWFz7ek7iRsAorqk4nPyX2Edpx9aUKN1LYGTbs56zrIHu2Ao-EXuLbSVR7KUStJRPB3xn9CGxvVX2fpnbWy-vp1e1V7bgRLs50Za72JDDuzPZnJfQT45sQpummUUVYRWXFRSCC16UYhBF3J32J29ubyEDPHhf2W_mBkOXH-g63eTAzdjdbFUN7uQwaKYc2C9_Mg8RcudoBpt-yWolg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=BJjm1B1I-_6bMwH7LJS0ErQq2zboqqLkJ-mkOPJkkX9JGQQOxvL9ZPyH2k5G7ui-LNrWqYyjq0DBg3ZjWd2jXtdLVEOKN_k3hb3KVS10THXnC22kRipDec_MfNOoNTtejYpgOAHgXcemfA0TORWKBtCOdZBdkvE29_SMqOsGilxiOeCNAWTYKuVPVDOA2UQbPjWE1FGJih8TZO5pd8par2cQsPFxA2hZoKYyYpDIYsayMl5Tfs7oa0D5J1aiVGoV9aI4E3wjtu6c_ZGWac7TEAcrl50LYQlB_4912CMbZ-Ts74nNOhcuPuQGQ-XQZ-q8an9IyS1OMVVB6EnePYmkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=BJjm1B1I-_6bMwH7LJS0ErQq2zboqqLkJ-mkOPJkkX9JGQQOxvL9ZPyH2k5G7ui-LNrWqYyjq0DBg3ZjWd2jXtdLVEOKN_k3hb3KVS10THXnC22kRipDec_MfNOoNTtejYpgOAHgXcemfA0TORWKBtCOdZBdkvE29_SMqOsGilxiOeCNAWTYKuVPVDOA2UQbPjWE1FGJih8TZO5pd8par2cQsPFxA2hZoKYyYpDIYsayMl5Tfs7oa0D5J1aiVGoV9aI4E3wjtu6c_ZGWac7TEAcrl50LYQlB_4912CMbZ-Ts74nNOhcuPuQGQ-XQZ-q8an9IyS1OMVVB6EnePYmkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=n_8W6WBl4HTZxBWVR0OxX5pkaEkDYY15l_hjCl4sKxJIJlewfaLNAN9KRa3-Zw5A44LisFELu2OF-P0kecYsgB8ZAn-Wj3ZCKwL57Qdysnf2tIB-UwdD7Y6171dlnt8CdQdmbqMVUr0jM-5h9k4TMVisp5ts8tiK5YvICHGQkYmyG5ivq1iS3r6lu6A-oBTvGx7gYR8YeYX5oaZF40cUXQtnasNEoUMmT6aM56KWV_DF6XxYP-z0lr3h9Led6vgvtHfMKRmOy9MfF2MRk6OhzRRlkrKehByA8Kcm0PTYz4ty_sDtBFkNsClmoHSr_AhLnCytX8kBOskkecq2queVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=n_8W6WBl4HTZxBWVR0OxX5pkaEkDYY15l_hjCl4sKxJIJlewfaLNAN9KRa3-Zw5A44LisFELu2OF-P0kecYsgB8ZAn-Wj3ZCKwL57Qdysnf2tIB-UwdD7Y6171dlnt8CdQdmbqMVUr0jM-5h9k4TMVisp5ts8tiK5YvICHGQkYmyG5ivq1iS3r6lu6A-oBTvGx7gYR8YeYX5oaZF40cUXQtnasNEoUMmT6aM56KWV_DF6XxYP-z0lr3h9Led6vgvtHfMKRmOy9MfF2MRk6OhzRRlkrKehByA8Kcm0PTYz4ty_sDtBFkNsClmoHSr_AhLnCytX8kBOskkecq2queVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwi_f2Sj7lcF4atIStXAklCatKg7Czyi_wEOs0Y8YiUGyEwbQpx5kJbGWdwYk3fveavLNSIh1SW9L-NkYbw0KlEMQWInt4kn4-1PbMXUafDGpYj_CTz0zNJJEoCmArbN63lytzhJdExWqyubMHRwpaBYhuJAYLWAmJVlFh5XgEHxmPkHexXk2pm5f5DuCZL2PJUfaZ_K-8L-L0M8upvCYQT__ucap1sooHROHiIHhKPH_mXUlJXHfcVz1JeoMCIfFoW7sKlGx4UcobrT_sKPKOz3-ZXB8jMRkc09XbJ_2-igNEqmiNjqe3FqvXdlyrx_LdRSMaI1wTl8gR4ZQF3MRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRdQFygKStc2u32N6Su79mdYJEdES2JwHWj-1daJ3zpP9VBOv1omRMwjWwWbJbXfTtkesKaQ8T-C9skDN6yB5lvmWpV1UGiEF-Okerx-rj2OaIi7_86AaQm2LxWPqarf2kSFAmvNfFa1yesHIn6tr5aLU23-7y1IJ5rN0NmaoFfU0QQrRJ_yxtaQkAn6wtYaOCtVg3Zg8yJxkSRXhv4uBLgZBELXlOK9kJNdB82677YMpC6ckDXjih1WuJmSd_OscE0OT2rmpqzxmIkimsjVHMheQMv3OzVliGK8JRB1EqrnveyH0XC2ACinmjIUPtx3VP6yg7H11B2hfGUKlDcX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXDnCfEeqsYCo4BO4cciEJlUPX-0RYhI69MWB0T6dAe79sIQ7m_GysYsmUpqlwIhyctdDO_j79ZlBJPFj0AONVW6u5X88to_aG1OimyXXvtXrrO3Tc6e3-LXcggWqN8xC_4iPPyp54br026xVGx_-KelMjeG3rqRmwyXezyxG65G7dNk4Nu9G3KZEsyjLUyUo5U4znIkhRNghNeXkSW-hHgfI8HmjpSyozanD8SHIDzutS5Iv2paXDuR8PRjxy7euCKoOmQw5S3LnvQPuPmz1bOsRsQUXxkavDuA5eIiGmb9VNqoTj2nztkjUPnj-x44zoAFMVlECwceSkNxQzh_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qznJNs1rLY6957N6S3FOqk1RlS9uBLaTV0aBc_vin4CwhlDs25LmncTNldadQqZx5LgQYyJ-i9auDS4tvuLtBP82VW5ulql9DKT4NCr8wrgB5aokVzhw9_54hE9ZGDq2SVgHo3jzgsjGvfdY3P9kYdvbyVU6j7D2uZkU3UzuPKRdCQTf349MbwXef1nFJNvWjcgdQD-32OisjC90SNynbFBDYctXmORPYvhoVR5cGcL2HOzbya_RZhoBgDnSvDhqQK5ZJSKqED8SGGlen-DG-fvth-e7jCAvM9JjkVtRyF3udOylOeiPKgM1Ydk82yiyNAeKMHivEBBmXgYDCmIQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIILXHtu_mKCpalxANx7G7N_ab7p63rPVSk0q10YC3YUL4UF_Qndn2ICltBbl8WBGOu5pjCvLRWSYz_BMXYYGa_FHUvpjH99XAflAEsFQoxXEsx5JbpTmQgOwpAF8Kq87HZjX0YqvuiOjDLC0Tq6W5-3AYEdVtXa_CF4j-pSmBsmZiSmcSFQ3T425dkqMOtTJkSUM0vGAdDRTLzHLh9Ixfl8VRcWNde9yrVx_s7IB5Ic88fd5wGk3OL_c1UzezQeJbxNK7OW-Tv0nzZipyMznjzQMSqyFgtsCe8DgJCAMw4idwHv-XcNqsKeDlQBcdZCixyFSXpKxrpPKvSNrK3U1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3cSbGkg2gg-j_tlZ8yFw9C23HP2FICAtgOoMKxmccK1H6IWpatuOYkBstdslj4j7i0FHmTEVddduG8jshZlV466Kg5W6gXFsdnm92pj6Cr5KqE4udw7zEAdkf3a1UGB-qb8UluNIabrKsTCZwm5XoorFz4_461igk0-Q5x8UQTTMBBrleWneQcpypq5DsgAkSACN_3kH6uXG7rejmLAPAmOabghwMHdIeKvm1kgUnq3_O30I_X6tvAgX-fbO2QzJzIyym1kSp-MfQLwLo4ATzpR_cmPFjcF9truSvIeY-l0xQh6ZAb_i50XgODzLPg5FIJhWSfEUPtJ6z8EcUG2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9rGTj3V69ydaM4y1ZfJ9WdTxN5Ke6kfEqsXshFFR2S5NByUx4C_2SJ7l0xdF12NGvqiKHCx9iB1PxUe7tru5BfZG3NtfABqP0sKYrjDEA1Q88IkKkC01x_jrKaww39w8zZAQabyl_AG98rbBoYF9xSDWHP8Tcq_hwg4oSc1mNbL2qIH9cQ1QiPdBdsilK87ZQhT4criEvxEZ3BGnaDyfBNcQInPF3DV2PcA80_U27-j_o1G6b9RzUAA7JMwsu0qBi1OL_nlSRpU7PXOBCb5SPGmoopGlCeC7kYQRArnBhkp4olgFmU_1Sz6hnClHu3zgqXJGv6M-iE5LMorsTvuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahszPT0LFvy2WT8men2hFN8SYbqHKLdpP69y2YflKgm-Mvk62eP5KorQHq-eLrML2GTlAq92-SMRdXWh-c7p3OVs8m2MmEkhmtHrCJ18rLCY__Wb5n5pzoSRMEFcbJ4E5ZRMmo4l3jZ4o2fA3vI5LsMC-jgCwq7NOb0PhGnFZk_bRqJqHc4gtWnUNKbZfa41Ic5-Bnnc594AIkP30dtdKGgqu38ORlDXykHoIuMI_gGMhGS_Zd-Dzt1nbYgR57sO4448jP1ZfEuX1gOq-BuiLoxTmfH6ilXLu-WEUQfuFBsiQuFgi8q9dxsZmovXLJZL_7xKTwZqW4lIw1SBQUeOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=XAtWBqxhE1rP2zd8d_XX3jgZcL5ewuOvXGY67IPwlRYcHzvZhjZfVNrlLYWBX8P90o7z3tSyRkKfPziIXBx0w8BZenLzMtajLSE186nN_5r_B78w_YnxeQCydID2JfQML2ga72kZaSqNVSjb6Zcumuih4q6idO359BYFUKIj3RZFjsZbU2ePLcYQrJcVQHQd41lCuo8qxTslCz5TGunJjgurjeAvznWGLgD2mcNKuzbTR_UNI-rP3N1HV4E54TzbgKjYTFZa1RO1T1B_zAvSjayfj2wf6Vot7Lbnfn6roItOgqFQHosQ_wgJozuKaCw2TTpAmDn06hyWMoG90_E3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=XAtWBqxhE1rP2zd8d_XX3jgZcL5ewuOvXGY67IPwlRYcHzvZhjZfVNrlLYWBX8P90o7z3tSyRkKfPziIXBx0w8BZenLzMtajLSE186nN_5r_B78w_YnxeQCydID2JfQML2ga72kZaSqNVSjb6Zcumuih4q6idO359BYFUKIj3RZFjsZbU2ePLcYQrJcVQHQd41lCuo8qxTslCz5TGunJjgurjeAvznWGLgD2mcNKuzbTR_UNI-rP3N1HV4E54TzbgKjYTFZa1RO1T1B_zAvSjayfj2wf6Vot7Lbnfn6roItOgqFQHosQ_wgJozuKaCw2TTpAmDn06hyWMoG90_E3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDCKSm9DRiL0AH1_ESQ_pYUS3m_zHFElhoo5Cwi1Mv9pnB33vzZPv1tmNqbcVyVB7GunW8N0mLQmiwLJWBwf1GYQvA7S4qyKOYMbtK1UJrcmD0EjVXFiTj1-kpIW528wc7ecdKkyARDYx2Awu7IDIHh5PKrX_wBEMwljEpeIFKGPPp1Z65Lz16mQ2OdWcaAmho3qvDoiXggno0O_HbSIRKu14CEx2Uv5ZhUN7_HlzotvNwoihcbQJij4PcJSXklCmbcPihhc6o392O4ltWSJ9DDejISXnZ4Y-Rm-PL4wL3Wav60wT4LWwoCdx51Z_Bsf39Y_urjj4Y94oprT-84ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=ZMjxlHyCrlIZcEkBsUXuvmmOLfre4UIaanD678Oas83k00u5K0X091djHDFCkSDzpwQUn1c2r-kRijIJvWQC8N7CXlH05BIDChcMs2Q7TaoqiMdgAcMHpYxbSVYPsT7IPZngFiSLe65E4MHUxEjg1IYYkIneSRkOaGWIOtOO6s84JKSTUaYqf1hQWRDnz1Za55rFOmOO8q43bXAwnwPMZW7jbM-TUJfvxAOQeaOi3ooWPJqRTUJkO7pzKV6l7JQ9C5M7DXNlTHpK0TxkhDEtlbEf6Dq21Du7n_Jx6A1YLAMB2pJ8WedBOekx_74kRIYcRHJcY_BJUuYZzzMJ0ERJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=ZMjxlHyCrlIZcEkBsUXuvmmOLfre4UIaanD678Oas83k00u5K0X091djHDFCkSDzpwQUn1c2r-kRijIJvWQC8N7CXlH05BIDChcMs2Q7TaoqiMdgAcMHpYxbSVYPsT7IPZngFiSLe65E4MHUxEjg1IYYkIneSRkOaGWIOtOO6s84JKSTUaYqf1hQWRDnz1Za55rFOmOO8q43bXAwnwPMZW7jbM-TUJfvxAOQeaOi3ooWPJqRTUJkO7pzKV6l7JQ9C5M7DXNlTHpK0TxkhDEtlbEf6Dq21Du7n_Jx6A1YLAMB2pJ8WedBOekx_74kRIYcRHJcY_BJUuYZzzMJ0ERJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEN6eWtNQVwRdTe8xVijB8Fuo6K9vm9sOvSI3jEIWwN3JQJXpROPid8jCWsmBbyb_HzK87x6GJr__Vzzh_Oi9iSeZGVwOQFTvcuJuYetY7kT2snho7sOmwoo5it46aexxNqztLph0kXWEh1DLDwkfVPNyIkiPLnC_0bNb2OHg3tpUNmg48W4MmE8lgAuy5cec_zoMSsuj2OBwaw8CO7EnE1pxJVgViGO50NzIU3R1iMOXM8QzOjqFey1F58SrAZ04ZKckPcR4LA9IT6EEkQbXEsn67zmYH1_7Yq4SJR_XfFgO1tcI5DQvbtDhvHwkSKsMwhXYBPqGf_iKcsp4pbTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
