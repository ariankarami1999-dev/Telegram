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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-448381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطره‌ای از اقیانوس حضور مردم تهران در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 352 · <a href="https://t.me/farsna/448381" target="_blank">📅 18:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای شهید در مسیر پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/448380" target="_blank">📅 18:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFGhniPfqmcGUFEz6V5uh0wVkMX_r3NMelbVXEVDHe9Gl6uuD3hNKjTRYZMHdHIaSr0Y-f3xF__giAMeRVp5K0V2MK9aCBHdcpjcCVqOmfmwzHi6FQcL8lPfqaHGxqhrfe29IYL4cXWUkawCysKvHQbGbZID7iOVhb7zMbkAl1WrJKemroSRCznjUVr15HYy920JTqGCHHEiyb3cLcsc2TOaWSXen9qeUa7CGFbb_f_CKunEbWEPTCcRaeKax7bMHJT3bC2I3YfQOrtQgJGnaeyQqWXrqj3mveLNiSJ9yb4Nb-tPGNcKWQPc17oaD8hm74CWnEKZQQQjn0pBNsgOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سقوط مشکوک هواپیمای پاکستانی در دریای عمان
🔹
ادارۀ فرودگاه‌های پاکستان از سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان خبر داد.
🔹
طبق این گزارش، این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/448379" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اطلاعیه شماره ۳ آستان قدس برای مراسم تشییع رهبر شهید انقلاب در حرم رضوی
🔹
آستان قدس رضوی به منظور میزبانی شایسته از زائران شرکت کننده در مراسم تشییع و خاکسپاری رهبر شهید انقلاب اسلامی و دیگر شهدای گران‌قدر از خانواده معظم ایشان، مجموعه‌ای از خدمات ویژه را…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/448378" target="_blank">📅 18:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم عراق مقابل ماشین حمل پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/448377" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/448376" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار عراقی‌ها: یاحسین(ع) پسرت سر خم نکرد
@Farsna</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/448375" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و خداوند دعایت را اجابت کرد
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/448374" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بین‌الحرمین قبل رسیدن پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/448373" target="_blank">📅 18:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npNkNmtZxueIx3eo3W0ARnH62B4zdjAgH3n-UIl0ewBn3ZaTnbR3jlokbzYHInaylJhPLpkSSsGYFvsn5g-F44CmdcP6ShnPtoHHITPntQRQZS7NmuuKEQ6HR7pGwpbR-LUJedDwEPvjHKEvXdH-XZZhNt6UXD6Uri7hvQWc4NGvjXRb5bMo3xKsAhJfRr_E7_TzhIq7U7YXSTHViz3UB3yP0ktLuzxYQY1ht-SV4AvA19aXTqSW8UftV9zSG56mMgbKUprxFZjUpre9bTa9FWjAhjot1Cim1e5aJ8sqTKtayBu_oif0Sq2s7_PYPp85HREqDjGhU7HtPcQjN_yJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
@Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/448372" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
حال و هوای عراقی‌ها وقتی متوجه می‌شوند آقا ۷۰ سال کربلا نرفته بود
@Fars_plus</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/448371" target="_blank">📅 17:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر شهید لاریجانی در دست عراقی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/448370" target="_blank">📅 17:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی پلیس عراق به ماشین حمل پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/448368" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در خیابان حرم امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/448367" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت حاضر در بین‌الحرمین در آستانه مراسم تشییع پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/448366" target="_blank">📅 17:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیون و زاری زنان عراقی برای زهرای ۱۴ ماهه شهید جنایت ترامپ قاتل؛ هنگامی که پیکر او وارد حرم سیدالشهدا(ع) می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/448365" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVJ-cuoTMwdahAfZm3snku6mP7ahj4l4CvsbAuCSS8eI0zRG3_Wt7DICVria7ItEANY66aSR_7p1FY39IaVRY4upsBhqISWgnU0bvLNOjU7z8bYdkQfrbaZ_xXin3PA1MfPv4UxFdcGZhcsd9tpb-OCdeqRa2D-T6alK-NMjYHdTZRtWnSAFDibMmvAoicTiRWCx9OQ1SgHxsUcPMmgLKO4g14xlpChredQg5qIEKrE-92Mt9ICku1ARbYJrgLDBb5OKZKFHG9PSJYZkUJFRlANOQJIGY_uvre1N9AGNYQuW6zCPb_0IFddeCLEAmDsL51odpNGSTXDUckqBjl9rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری با تصویر حضرت آقا در بین‌الحرمین
🔹
هر جا عکسی از حضرت آقا می‌بینند، جلو می‌آیند. با احترام، با لبخند و گاهی با چشمانی خیس می‌گویند: ممكن الصورة؟
🔹
در تمام سال‌هایی که خدمت به مردم، فرصت زیارت را از او گرفت. بارها آرزو کرده بود به زیارت برسد، اما نشد تا رسید به امشب، به سلام و وداعی با شکوه در میان مردم عراق...
🔗
حال‌وهوای عجیب مردم کربلا در وداع با رهبر انقلاب را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/448364" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
گریه‌های فرمانده ارشد عراقی در مراسم تشییع پیکر رهبر شهید انقلاب
🔹
ابو حسام السهلاني، فرمانده عملیات شمال و شرق دجله در مراسم تشییع پیکر رهبر شهید انقلاب در نجف در کنار جمعیت میلیونی مردم عراق به عزاداری پرداخت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/448363" target="_blank">📅 17:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb212fb7d.mp4?token=WEXu629SdGAvDy1_G5s5-78GkEuvlFcMN3HQA3pnrwvAMMWk5KPugKtM2op7dJbVNLB7AhOFv05ck4cGWxpCAM3JJdeR6NqMfaUtmYos2x1uasUOKQoZkcsNOPUMX_NvrY4YrC6cbUIsCmLkHemYf0uGosbDCBNNTf9HyFPJilyyn_0FlwbaJofOi2l1EnjDfHXr9WAO47PtQJRVTbqn620UTcCy-poCjWigUTPiSw_YdDlaN9tXh-9AOAJc7r6E10Q3f4dfoM9-3nZY2tqdNmqROvyevU5_Je7BL0voBrGO6xQtx-PHUH3DmULigzTgd01N3rEM1HWgnNHkZ4g8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb212fb7d.mp4?token=WEXu629SdGAvDy1_G5s5-78GkEuvlFcMN3HQA3pnrwvAMMWk5KPugKtM2op7dJbVNLB7AhOFv05ck4cGWxpCAM3JJdeR6NqMfaUtmYos2x1uasUOKQoZkcsNOPUMX_NvrY4YrC6cbUIsCmLkHemYf0uGosbDCBNNTf9HyFPJilyyn_0FlwbaJofOi2l1EnjDfHXr9WAO47PtQJRVTbqn620UTcCy-poCjWigUTPiSw_YdDlaN9tXh-9AOAJc7r6E10Q3f4dfoM9-3nZY2tqdNmqROvyevU5_Je7BL0voBrGO6xQtx-PHUH3DmULigzTgd01N3rEM1HWgnNHkZ4g8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ۲۸ تا قایق [ایران] را منهدم کردیم؛ احتمالا امشب هم همین کار را بکنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/448362" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf84b71fd9.mp4?token=ankYa13ODMqaAM1PWKCyo8dekhQPorSRYK3F5f5PialsE2dZ33eOFL3cWH0pOPXenvwbWqAYshPz02CanmDE8loihuVMNoNnHjqXFV3ghY7mhngzb2OUuxeBLjv232prO4dgDVvjLU4Av0v0sfqt1VqAoGXmfADopgiC82WHaT3kxGaTLHhubihB6LD4GltotOLCC5agkDS-y1CuS9f5Qy1Rpm5rJFDoqtzyrYFKMmGNj5C1x0tRC6OMX4QS15logDvHqf5EDkm1-XEEbk4nOKVZbigGDtnBTbJRQJJDl18NMgU1r6O9gQKHHFn6XsvR46ShVN6u83Zax_u7gkt15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf84b71fd9.mp4?token=ankYa13ODMqaAM1PWKCyo8dekhQPorSRYK3F5f5PialsE2dZ33eOFL3cWH0pOPXenvwbWqAYshPz02CanmDE8loihuVMNoNnHjqXFV3ghY7mhngzb2OUuxeBLjv232prO4dgDVvjLU4Av0v0sfqt1VqAoGXmfADopgiC82WHaT3kxGaTLHhubihB6LD4GltotOLCC5agkDS-y1CuS9f5Qy1Rpm5rJFDoqtzyrYFKMmGNj5C1x0tRC6OMX4QS15logDvHqf5EDkm1-XEEbk4nOKVZbigGDtnBTbJRQJJDl18NMgU1r6O9gQKHHFn6XsvR46ShVN6u83Zax_u7gkt15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ دستی دلِ رها کردن پیکر آقای شهید را نداشت
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/448361" target="_blank">📅 17:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0abf71a9.mp4?token=agUG7fBRKkR6mUdJzkfCcTuvF3PYCMBAQVrgXNShL9twFLYDDkCbs1iuQHHeT0xwdic8qxRuYFGXnAbMVXatLswqOgo03M__y0g3DMost35DBdCmbvrciE6PEQMJWR_HBHAY1apL8UKFMoeeo22FACj4Mjc0QAk2VIag1PatqUXiNkjmpLNTbNw299CF6SjVhobLk4J-gGZq-zQgOQLoMVMlOYF8fYe2kDHitSFGVptyaSPHhGrmSxajjR9TAXNeE94vfnaWbuxIGDH6HWkdpKh55FvfmVKvrIWvYkf5FP6swZWQUKGIsd5Cmsr46RDdKfDeDuZQRiM7UGiYQYmfEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0abf71a9.mp4?token=agUG7fBRKkR6mUdJzkfCcTuvF3PYCMBAQVrgXNShL9twFLYDDkCbs1iuQHHeT0xwdic8qxRuYFGXnAbMVXatLswqOgo03M__y0g3DMost35DBdCmbvrciE6PEQMJWR_HBHAY1apL8UKFMoeeo22FACj4Mjc0QAk2VIag1PatqUXiNkjmpLNTbNw299CF6SjVhobLk4J-gGZq-zQgOQLoMVMlOYF8fYe2kDHitSFGVptyaSPHhGrmSxajjR9TAXNeE94vfnaWbuxIGDH6HWkdpKh55FvfmVKvrIWvYkf5FP6swZWQUKGIsd5Cmsr46RDdKfDeDuZQRiM7UGiYQYmfEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلام به بقیه‌الله(عج)
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/448360" target="_blank">📅 17:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448358">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a78dd2ba.mp4?token=FJWn_i8fPqzFgwCQ7sCwJfe80Ny3_maaiC3g87FGeFqSyd50pGqKARufZB6UWy1N7KEJ5A9Z5-_IEVvqzP_TbKVEgvlIO1zi89OKBI8f13ggZcq5lSsJPA8pbF6SpaaAxGSZwzn58tl3t5ACGEYLCYTuS85mLnuTrMYTTiWnhaJDQ9arNhpo9juOFRRXApQ7ZwAdW_lNddNfumr0mtOtEaPoeTgQ2kuwbV30VFUOfxKC7Xzl1uP-I0kugClTLubxZg9lL6b0g6KAKH9wfKUgE9z3Kp4Vr8Am_qD7PaXYVao8WLCy3vym-pRGnVCA8390whOlSr_82BSqqQladv1a9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a78dd2ba.mp4?token=FJWn_i8fPqzFgwCQ7sCwJfe80Ny3_maaiC3g87FGeFqSyd50pGqKARufZB6UWy1N7KEJ5A9Z5-_IEVvqzP_TbKVEgvlIO1zi89OKBI8f13ggZcq5lSsJPA8pbF6SpaaAxGSZwzn58tl3t5ACGEYLCYTuS85mLnuTrMYTTiWnhaJDQ9arNhpo9juOFRRXApQ7ZwAdW_lNddNfumr0mtOtEaPoeTgQ2kuwbV30VFUOfxKC7Xzl1uP-I0kugClTLubxZg9lL6b0g6KAKH9wfKUgE9z3Kp4Vr8Am_qD7PaXYVao8WLCy3vym-pRGnVCA8390whOlSr_82BSqqQladv1a9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید جزیرهٔ خارگ را تصاحب کنیم؛ [ایرانی‌ها] هیچ کاری نمی‌توانند در برابرش انجام دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/448358" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448357">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Fsfu4X28ur8U3p9f08S-c9T9fiWUnAo_dAuYTKvoudsleooAJVeQjwCmhiLfuE0-oBXarcWmf-Mkp744Iv01ePBlREe4mAMRHq4tzQ91L2aBANcfwoh3hLrMwgg0hPs0kqQ_sPlBq-fchtePEYdxfXG0v9ji2kcTqi1icK8puf7fv4U_ntevwgnCgWQ6fPpIqPGfLF9l78MRDeqDmUggr05g5MZcD7yiDzYF_Zam_HXPWXJvmLXzbj9tK38Sa2mTyZN8L9kjeOlzilY6Hntuq2mTMrRLdLst0DKEHiwGHhNykZzStqgpuUU8iP3kCYdJRt62fOTK6Si3Y_X_HwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده‌ای که از لندن برای تشییع آقا آمدند
🔹
آقای جوانی به‌زحمت می‌خواهد از میان جمعیت رد شود. بدون مقدمه می‌پرسم: از کجا آمدید؟ جوابش در ثانیه میخکوبم می‌کند: از لندن. برای اینکه مطمئن شوم درست شنیده‌ام، تکرار می‌کنم: از لندن؟!!!
🔹
اکثر خارجی‌ها شاید شناخت زیادی نسبت به ایشان نداشته باشند ولی به‌خاطر جنایات اسرائیل که در سال‌های اخیر مرتکب شده، هر کسی که مقابل اسرائیل بایستد برایشان مقدس است.
🔗
حرف‌های شنیدنی مهمانان لندنی رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/448357" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXkfcd9Fbj4HtCk_CNaMom4gRkd8MkkckOHAaJhcITDErs5qddL7sooyfsm9qu3mXTH_prlT_itZs6RLsC9m0xCLAZugOvkSwKr1rSKUyo7JOwxfNUGKqIAygpU1_1XvmhmL80bxz5w90Tf67LGOAr4nqtix5Ma052qxp_5hL0Vm7SL8Rua8iQpxCV2jZGiKjLS4jH5pTbPJq1VFdE9-CCJS84G_0y1LuP5CWOh6Il7qVLaprr0A8O8ONfGUadn_TLe4hpfGRA0zODjmbs2FY-fIFBjjso5_yGZ7cplcsMxYbm-fbKH91W5UJudAIItZRBDiJM9AvtWtyJVNOMJr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3CLGE3rQJVIOhYGkEmNe309iroMTjfMBN7IrbaNcg1xg5PF3boFwI5wuJF_OOMWDz9sp_c84DFalISTDVmtysmGn3tvePYR51OSTEhn0LzIWaQMh9b9VQbCXYDnD9wW69IppJQvUw9NuJLtZFkeFeJWFllFUeuvD2bK9tUp4d1p_ePkceDMNkrYhSkfvy-rUcEjwfarAe5nEskGRlJylJ6VyWBQvHBqJQTYAZ1s9ogay-lT_yOWQdPUAG3r4WUAgIVzh14oSwrt-Bi5p2_9r2fzDYcKLYYh2Icz5CUPTXPLYIEgAIsQfMayKuzlyxxYFKTmxaQBqaxlJx2EjHZ1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvSsrAORZSFErXNPtzYUc77g-rh0FFGN0nkAc8oWO-uijfI5fktz0dFiVj-g_lhnzvPJd8BPRR2YLzfoZuZOiVkCiwGqjwY6Kuepm3sAkFu9qWukdFNRHUq1sX43GuhjPz_3uJM6dMkgm_RCiKgDnqjUYR4qvyBETksVJPop5Bb_QURrWNRem09zhn-zoNEDZbMkbhtqtN5aqNzG8WY4f8F6SJFqy2yvLLFpvikhgAlmo3pckXx6LX3UESnzkrf-Pv76BEUAyBqh2ZnUsARvkbaOb0rHTYmpdd_OArT1rPY8KE8KwzT4smX5mOLm0qEYsV6eenjGJCRHkbU7A-P8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZ7WK4SpqtvBGgwEnXlpuD7xghT6kjFGxEJuJFWzLDnkAk5vWPNK5G2TGXX2xbyAe7_Dcpf0RBNiA9qtEkiObNO-lnKoZih8UN9sFwarJGq60TrUBcWHy31ccxD6RWEMiEgNwBB8IWHKhDD4ReWQVnhuXr-_1AL30nun5O1UXG1Sc_GjUJA9y21CEw4XyrYZYqqO-SSXphwkUG3yJi4emyqgMWhxyUrSDs9Bs1JzkI8oyjBhb4aZwz6leYnTEpCHOM2DPHRYzSKHiWE6OosE5Im0YzZmRlrotKfeBIJT4Fl6AMp9PhwxdrUkmBHoLhpFgbpCsU4KHRFJsMyeLC4V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JozfG4-pnjovl1nuiNVbQQSHz8LyXxFm7BXQATrM5Lk0SBpV_9bbGJkOZzBoH_BBlhCUwWdKzpaiXi4c5nRXzbgX-_FNmz8zFvu2oC0d_r32U-Jp7PJcQYryJkuLBIp9TCK6t4qv2fXSO22MzHdQCKjWiOfKXSJEILVOh3ecOU654KIjHgomsZzoqn_wgIXHxsHOL5QLpqmRH7H_d4HbkU9EXupSoKG8uqjQoiSSMim1NrqPuVotYO_3BWn8oQShNdibOLkb2tEbVg5jqPL51Yerlp3TMW-hAtvyGu5AdBaf8z-PReCBjIdlIotUyxdBIJBwl8KLgE1orX85N857IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7lsQzaUSe0gYwqSRxrYtORSFkFgJ5WR0iiVP1XTd2819vzuy2F2LkU_ac2o9C5G2xbA_2L_2H9-qAznBUbx1Tt45tVR-Ohzt_XBS58g--1rJo9svDkD0nwjus2kp3CJiuhThidylIHYeTzpmWym9zkzu4YpEWS050zgxvWL6rPCaeUYMwus-aUGUDBaa9iO0eX17NnrYItGwzAMN4h9go5ngrgHfC--S49mKxCKTBnL-swIUG2bjCoSUNMi1GfgHFWCrsWp_DLGZEDZ4Qhf_CBQwEE9XcWt7GmDag24V4P-wO6BVpelFuQ-HO4wN73tvqo3ysYSYQD3knTt3X9DdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین قاب از زیارت رهبر شهید در حرم امیرالمؤمنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/448351" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c9309d46.mov?token=PKQL3HiDCEwCE2QYOfOALs8NmX1aO0mVpKqc9zhO4geA8gx2eNglHcyOAkXYtnTO30XAc5QQCXZHPBgo2iAMRi6qzvgJateBGJyGQ_IbQvADF74IX6kHASzvLKEGLQPrFUcKTuPL5WnlDSW_W_2weXmLoWYVohRRAQfjFZl279Njx0FxTZFpWT7ETYNXmsQd2DbWS4AbwCwkaT0n4gNvIkaD_ydG3vB_cxSYN9hWl-DVg3JCfXhjBybbByLZGasBNzpML3qu-mcF9bUkLdwqqR9nne3_wDGdmMFS8mna-9v7tb_OlhI1lNKfylWYqAmTgzULZt97xZosjBKyKk2DoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c9309d46.mov?token=PKQL3HiDCEwCE2QYOfOALs8NmX1aO0mVpKqc9zhO4geA8gx2eNglHcyOAkXYtnTO30XAc5QQCXZHPBgo2iAMRi6qzvgJateBGJyGQ_IbQvADF74IX6kHASzvLKEGLQPrFUcKTuPL5WnlDSW_W_2weXmLoWYVohRRAQfjFZl279Njx0FxTZFpWT7ETYNXmsQd2DbWS4AbwCwkaT0n4gNvIkaD_ydG3vB_cxSYN9hWl-DVg3JCfXhjBybbByLZGasBNzpML3qu-mcF9bUkLdwqqR9nne3_wDGdmMFS8mna-9v7tb_OlhI1lNKfylWYqAmTgzULZt97xZosjBKyKk2DoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از طریق الحسین و مواکب مشایه وارد کربلای معلی شد
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/448350" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=cB7lrK3Vd59HQzz1tWyh7Nre65St7V8b10BlijKMs5f8_FHl7Ky34_ZDWEBPPpfQ1UxKLxFFsYyO2pZ8qCNf2RWh-UESiUjn2U1wr_sz0ECAymKJosNZy860XBrV9KzD4Df8rhAwLnbD9B83te7VOWb8SoVYDr6xGIAg4Q6GvYE824euhdAivH_A_c1Vt1Pk19YQ3IB9ecx2CAWvfw8w3YrEsZdc62C2zgkYxGmnFGpiA6FqmRTyVZZWMXz4w6jNIg6MTQ7WBMrEQVnTt3Pq9d2tjc5_-gXKG3F4pShkD1GPknx-xtoCUyUMpajejHlB_GxkfJmB_uKBPnGbmG0Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=cB7lrK3Vd59HQzz1tWyh7Nre65St7V8b10BlijKMs5f8_FHl7Ky34_ZDWEBPPpfQ1UxKLxFFsYyO2pZ8qCNf2RWh-UESiUjn2U1wr_sz0ECAymKJosNZy860XBrV9KzD4Df8rhAwLnbD9B83te7VOWb8SoVYDr6xGIAg4Q6GvYE824euhdAivH_A_c1Vt1Pk19YQ3IB9ecx2CAWvfw8w3YrEsZdc62C2zgkYxGmnFGpiA6FqmRTyVZZWMXz4w6jNIg6MTQ7WBMrEQVnTt3Pq9d2tjc5_-gXKG3F4pShkD1GPknx-xtoCUyUMpajejHlB_GxkfJmB_uKBPnGbmG0Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ ایران را جمهوری اسلامی ژاپن خواند!
🔹
رئیس‌جمهور آمریکا: جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448349" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73992baf6.mp4?token=nDbYJHF_cGuc1kCMbOXDFKSu0DVo6m7H-SF7gjrCcEo04CP4xxWJZByrtjtiWm4r0Z1MpOS_1rdmIRbVNbSJS0Ogc7ROLRYw8CWlZHQT2VUx8t97hwDaU3yHvVa-vSwTPZjOV9NW1n19JYY3cOiSNAFAPzg2XYOvjAncKImxf4Xeq2gwe-sDsz_apQzcNUtonI29Y69dHSOImilurWraQZExCf-Ew0AS7rdEa5aSPSZLhbtEDdKwIFa8gWj9JQ9Yyq3P6QBEw4JVlazLkNvP4I4DDlEsGD_8AUMVjYnZR1YCebfyQY9gVA-QOwuezF4DYo-Ot6Kn-0Xq7kYuYoy7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73992baf6.mp4?token=nDbYJHF_cGuc1kCMbOXDFKSu0DVo6m7H-SF7gjrCcEo04CP4xxWJZByrtjtiWm4r0Z1MpOS_1rdmIRbVNbSJS0Ogc7ROLRYw8CWlZHQT2VUx8t97hwDaU3yHvVa-vSwTPZjOV9NW1n19JYY3cOiSNAFAPzg2XYOvjAncKImxf4Xeq2gwe-sDsz_apQzcNUtonI29Y69dHSOImilurWraQZExCf-Ew0AS7rdEa5aSPSZLhbtEDdKwIFa8gWj9JQ9Yyq3P6QBEw4JVlazLkNvP4I4DDlEsGD_8AUMVjYnZR1YCebfyQY9gVA-QOwuezF4DYo-Ot6Kn-0Xq7kYuYoy7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف‌های دههٔ نودی‌ها با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/448348" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoBDkzwglaWk9zZUxD2yvrWopOK5F62lP3xxQVkpn_sLVJxO5bEB-sIxeTYidc8tCmHS5qzLPS3-0v4ndJzwIWBXjxn3Ei6Zn2svBByd4suuZPBaIO-sBIQXGIFEwezVfmea3_U7E3T1xP0DjRpfZ4zE6If9oZNh7_YcmjTRBDAqXjvoKyUG2JEr8HeZtpYbn2URSd0GaJPGO2Mo_l1cz5sZqUUZRaqv4hq74KQusGgHQm87TYPVtIapUVs7lrt2dzidj2mUPygmqFp-gphwNTwe3zun7ZbPWbJQWIk2_RMRyukEFrSu6ucG5gM5EHNLNNmsQvaUIGxwaT1gq3BBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: به ماجراجویی‌ها پاسخ فوری داده می‌شود
🔹
مشاور رهبر انقلاب: پیش‌تر هشدار داده بودیم «منطقه، محل قمار سیاسی کشورهای خرد نیست» و بارها ثابت کردیم که ماجراجویی‌ها پاسخ فوری داده می‌شود.
🔹
اما مسئولیت تنش آفرینی‌های تازه واعتراف زبانی به لغو تفاهمنامه توسط سیاست باز راهزن و بدنام اپستینی که بارها مورد نقض عملی قرار گرفته بود، بار دیگر منطقه رابه سمت آتش سوق می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/448347" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea2c45dca.mp4?token=Ut1BdPLjHIwng9r0Rxx0lcOs8SeSNa5wHGwSH7DVVITviPTuJc1GFMqktqm49xsTy86VNapm9CvIDLY9kgtUNWnAlNirgOFH2YbcJB6TrIxOsiKyedOZbTjT7n_qJeL4CGmuQcNmXIh-ohnYxsRhkpVW4Y-j3buRffHE0PoLZZ61piPzoTF1P27-4U8uxowxrAlKCzY5xyMAwbifuHob6WN4H35fPrVg8v8aBiNGHKgUUYU_MCLWUtWX-Hr2d9NOXf6xUg7J5AINKKro-DrU6gA7vD7cMSGZsqqo13BdUFv4C_Fz3CRB0HIASjHvIVvf9V0q8v_t2fQILexW412evQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea2c45dca.mp4?token=Ut1BdPLjHIwng9r0Rxx0lcOs8SeSNa5wHGwSH7DVVITviPTuJc1GFMqktqm49xsTy86VNapm9CvIDLY9kgtUNWnAlNirgOFH2YbcJB6TrIxOsiKyedOZbTjT7n_qJeL4CGmuQcNmXIh-ohnYxsRhkpVW4Y-j3buRffHE0PoLZZ61piPzoTF1P27-4U8uxowxrAlKCzY5xyMAwbifuHob6WN4H35fPrVg8v8aBiNGHKgUUYU_MCLWUtWX-Hr2d9NOXf6xUg7J5AINKKro-DrU6gA7vD7cMSGZsqqo13BdUFv4C_Fz3CRB0HIASjHvIVvf9V0q8v_t2fQILexW412evQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد عراقی با پرچم قرمز: برای رهبر شهید خون‌خواهی می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/448346" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448345">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=RgHNLsi-FM91BE8U5p6qYRiTJ5Nk2NHc_UpmHAcXra6ukKB0jH_6Hxyn3zh49Ob_hPP7k1B1S_CDMBu1MWuCtxu8uTgVZh3d66bkx_-YQdINQia0xtqDAcXxURG2cWjvwFawMHR8S8oFm-b5K9S1YdfEqW2DYIIXEFVXliwvqT9GrakbuXn3ucqSFGVgYY5g5n0lKK0GN6XXx3dZxxBbKAYGHF07aWCHdRc-0OgrqAKrsov1jlbfeAHlFydQGfA-9LHdEgxEGJqkmbr6tEqH45-hCiRllc34bwE18RTY0aElhcFtFb8gkf-sig72VmKp8GWnogjiz3hutH2O7Scu2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=RgHNLsi-FM91BE8U5p6qYRiTJ5Nk2NHc_UpmHAcXra6ukKB0jH_6Hxyn3zh49Ob_hPP7k1B1S_CDMBu1MWuCtxu8uTgVZh3d66bkx_-YQdINQia0xtqDAcXxURG2cWjvwFawMHR8S8oFm-b5K9S1YdfEqW2DYIIXEFVXliwvqT9GrakbuXn3ucqSFGVgYY5g5n0lKK0GN6XXx3dZxxBbKAYGHF07aWCHdRc-0OgrqAKrsov1jlbfeAHlFydQGfA-9LHdEgxEGJqkmbr6tEqH45-hCiRllc34bwE18RTY0aElhcFtFb8gkf-sig72VmKp8GWnogjiz3hutH2O7Scu2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ضربهٔ بسیار سختی به ایران زدیم و احتمالاً امشب نیز دوباره ضربهٔ محکمی به آن‌ها خواهیم زد.  @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/448345" target="_blank">📅 16:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bdb6b181a.mp4?token=ggsmkyF3nBEe49yR_SdgsF301tKixNJK7U5d6yl5EjMKgNs1cVyT08FlQoH-wMloQwAGwQoQLjKNyW9Ir_Bh4yNe6FkO2mMumI6h06HJnf3OfW4_aXu8RHwZPcSDkSTv9mYHDxK8i-betY7rTC9mE5wZI-5NUxNSkEbdX5HbRmroTk9oborNYIBVGV6sYieEdLHJVUDgWzPZTWr8qV1OGLLLd-LEGdTuD1AFMgL3DdrU3hT2yj-f-oc85YIBaYegenqv3FMUwxNY9-khmYAC3m0_LEPqVzdnEdUfMVxGV8w1Dhsywutg7AA4DJIzkCqxKHjtIvOz1mfHXJ22qIjwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bdb6b181a.mp4?token=ggsmkyF3nBEe49yR_SdgsF301tKixNJK7U5d6yl5EjMKgNs1cVyT08FlQoH-wMloQwAGwQoQLjKNyW9Ir_Bh4yNe6FkO2mMumI6h06HJnf3OfW4_aXu8RHwZPcSDkSTv9mYHDxK8i-betY7rTC9mE5wZI-5NUxNSkEbdX5HbRmroTk9oborNYIBVGV6sYieEdLHJVUDgWzPZTWr8qV1OGLLLd-LEGdTuD1AFMgL3DdrU3hT2yj-f-oc85YIBaYegenqv3FMUwxNY9-khmYAC3m0_LEPqVzdnEdUfMVxGV8w1Dhsywutg7AA4DJIzkCqxKHjtIvOz1mfHXJ22qIjwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق (واع): پیکر مطهر رهبر شهید به کربلای معلی رسید @Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/448344" target="_blank">📅 16:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448343">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0f4bec21.mp4?token=k7wWXeBwoCg3PpP2xgoq0S5M3TkSITmJOMEm2Vscb2OMO-vLrmuR9l5vZ1hXw_rgSBnSlnt4LRZJRCdzGaCK083mNNFinJOPcJSN7peJK3dNV1lD1kvmBkqvv2fY9zV0mV4xHVf0iFX7pe1Dp0xWIuxlrEegkNkoyMkJzmMSUus9csFD0RUR3cu9p-ytFnOkajx-pUgdbghl_rkrWKW6tz3Dz4OyXc03WxOgz-_9NeW4wLVUF7p9hqu24mnhYYJceSXvWbP7vMyBZnpAHd60BVQXl5BzgWgU6qLAUaO7qEi5NT2EHfJ53r05E06ia9AJvgeqZTcZ_-bbPDGnY96slw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0f4bec21.mp4?token=k7wWXeBwoCg3PpP2xgoq0S5M3TkSITmJOMEm2Vscb2OMO-vLrmuR9l5vZ1hXw_rgSBnSlnt4LRZJRCdzGaCK083mNNFinJOPcJSN7peJK3dNV1lD1kvmBkqvv2fY9zV0mV4xHVf0iFX7pe1Dp0xWIuxlrEegkNkoyMkJzmMSUus9csFD0RUR3cu9p-ytFnOkajx-pUgdbghl_rkrWKW6tz3Dz4OyXc03WxOgz-_9NeW4wLVUF7p9hqu24mnhYYJceSXvWbP7vMyBZnpAHd60BVQXl5BzgWgU6qLAUaO7qEi5NT2EHfJ53r05E06ia9AJvgeqZTcZ_-bbPDGnY96slw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق (واع): پیکر مطهر رهبر شهید به کربلای معلی رسید @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/448343" target="_blank">📅 16:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448342">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
بین‌الحرمین، مملو از عاشقان چشم‌به‌راه امام شهید  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/448342" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448341">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f378af4596.mp4?token=Q_M2PVEymK7SmefDpynRA3asR9W003cugd3cMvIPl48EvIjXkdcsjEaKiEx9wbQQwgHlHK-qYYkjHIsJuCBgcL65V3pSf5UWe7VxYx_pomou4V6q6-TMmj82A14lBYOfaA9BE1_0N7IT0rTk8rjsyJ8NBnR6nOixIRRVddJ1I_maMrvWBCOvK1sBQ5lHwReRwoIn5VliOUMFkSLBdtDlsDEhOB7WXIopoqPngIPCeuJmS8wUQoslgREGT1_eKR-1AV5MvkJtuD-58uU8TPJW45j6WdAd8RkYHFtakDhW-gfgj3Kkg_nkcmp_oa5vgLnZ_82xIaNph6wT_JCcLE2XPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f378af4596.mp4?token=Q_M2PVEymK7SmefDpynRA3asR9W003cugd3cMvIPl48EvIjXkdcsjEaKiEx9wbQQwgHlHK-qYYkjHIsJuCBgcL65V3pSf5UWe7VxYx_pomou4V6q6-TMmj82A14lBYOfaA9BE1_0N7IT0rTk8rjsyJ8NBnR6nOixIRRVddJ1I_maMrvWBCOvK1sBQ5lHwReRwoIn5VliOUMFkSLBdtDlsDEhOB7WXIopoqPngIPCeuJmS8wUQoslgREGT1_eKR-1AV5MvkJtuD-58uU8TPJW45j6WdAd8RkYHFtakDhW-gfgj3Kkg_nkcmp_oa5vgLnZ_82xIaNph6wT_JCcLE2XPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورودی باب‌القبلهٔ حرم امام حسین(ع) مهیای ورود پیکر شهدا می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/448341" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448340">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy6Ve-iYgCza9l_BRYKON5qtgESjtLg8OKA2GJRr7Ncod4Awh9sGJOwGdn1B-Ja48MBIEUklj3uvDGToWqqaaOereHxn31rv3Yd6o473_2oEojnlBxuPcvGTg_hs5eVujR-WoSSp_geZpnDrX7zrXNO0ek0DaiLtHIomHyDr8eQufKf2R-G8OfIKNbnpr5qGugGYkPzJXOERyyXcReVFDRYRa_1SHYqhgjnfFX3Yu0bk2E43y6d9Y8r6e-Hgq1Q0Xgyay8X0-vX9t_VYkpjIKFwgPtLDfgqlSoVRqyydhgCufWjQJzofthuQfYS0-bCYfsKzUj1Omg1FDl9HfGoZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینۀ حمل بار دریایی در تنگۀ هرمز چند برابر شد
🔹
سازمان بین‌المللی دریانوردی اعلام کرد با تحولات اخیر در تنگۀ هرمز، حق‌بیمۀ کشتی‌ها که چندی پیش اندکی کاهش یافته بود، بار دیگر به‌شدت افزایش یافته و هزینه حمل بار دریایی جهش کرده است.
🔹
حق ‌بیمۀ کشتی‌ها که در شرایط عادی حدود ۰.۱ درصد بود، پس از تحولات اخیر به ۳ تا ۸ درصد رسیده است؛ به این معنا که هزینه حمل بار دریایی اکنون ۳۰ تا ۸۰ برابر افزایش یافته و بیمۀ عبور هر نفتکش بزرگ بین ۳ تا ۸ میلیون دلار برآورد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/448340" target="_blank">📅 16:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448339">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff04b626eb.mp4?token=F3l6-xpP3kZiDeBCZ9BzffNycIxtFzjQPiZQTQUzUZoTlbcNU_grXQrv-GBhTjNOxYzIrXFOgWCei63iR3UeEPn-MuIWeMofg84bvgKM0eJ2uSalWjdM1izE1EJO3TjoMuOpnzfWOzS210kSlEwUs4Pi1XG5e4b8aPwo9vZeS1iigU8rZrldu9hgntXWVpekTaHOY95SjVnyPXrO-9ehroaXTpNfsBw4cHcPcY1o4Cskkgu5saS18m8BCuLWl6QKemLc5fp8skMgx1dwzH0Sz1P-zSVNQHW4DF4fMuNlEKcx8CrTRKoC1Bv1z7ubPk_nxuOHrcktY3EdU1ztcAGLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff04b626eb.mp4?token=F3l6-xpP3kZiDeBCZ9BzffNycIxtFzjQPiZQTQUzUZoTlbcNU_grXQrv-GBhTjNOxYzIrXFOgWCei63iR3UeEPn-MuIWeMofg84bvgKM0eJ2uSalWjdM1izE1EJO3TjoMuOpnzfWOzS210kSlEwUs4Pi1XG5e4b8aPwo9vZeS1iigU8rZrldu9hgntXWVpekTaHOY95SjVnyPXrO-9ehroaXTpNfsBw4cHcPcY1o4Cskkgu5saS18m8BCuLWl6QKemLc5fp8skMgx1dwzH0Sz1P-zSVNQHW4DF4fMuNlEKcx8CrTRKoC1Bv1z7ubPk_nxuOHrcktY3EdU1ztcAGLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ضربهٔ بسیار سختی به ایران زدیم و احتمالاً امشب نیز دوباره ضربهٔ محکمی به آن‌ها خواهیم زد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448339" target="_blank">📅 16:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448338">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45df1cc3a0.mp4?token=fD8asLJdmH0CQk4Oh0bqL-XatmeInSs8gE8nhIwwkyzMi30kyTakeknyWy-0YtTwSfxcil91cknY792cmkYrX6rk3PGdJRVrSmRSQfM3sSk8lk6eP7pIvJRgd8SU93gORsSegcsM5FRoFuDXt75QDud_wGXz9W2DwJlxC9cHnkgzQY2MBVVO3Vm1lIkoskTimNocb_PxEqtju8rOPwW3brHdl56WkOcPUrmTvZxBDYVgLub3QFO-KhwejCOKpfA78AW6tgYlEemj3dL0Cn3rydRgurnRzGLHTtD_zgRp-MXghjHVswkxmdsYT0dB71Z_2zAEl4W9FeajVMcKg5NjBnUum3h33Zj8zVrVcYJIc9CDW1ffZ-TzDbUyXUkp6z55CHJpVuYCIcha3BZJThFIEHhJOA7VknY5_JnQsSqPS9lki3pXczr0qbPzss8mQg5MBVRYlI5RHtm4hrGjH7dbAry-bfARUupkx0VL1MLoqc8PaMx_j45PbbiMjb5kx39V-O1YxhlBI56awtHr4L8SximchIKJOxHh0OLA5rrDWZPkRdn1_gPMSPav2grhawWmjSG32aM2FHyVFByRM71x9Ezu-tfNKfXjollXufoh2y7YZILb5oIpiCN7NN_Zj7wbe_ulSFqVE7N5NHC0niCOhVn9mDkhwfulBTeMFddh8jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45df1cc3a0.mp4?token=fD8asLJdmH0CQk4Oh0bqL-XatmeInSs8gE8nhIwwkyzMi30kyTakeknyWy-0YtTwSfxcil91cknY792cmkYrX6rk3PGdJRVrSmRSQfM3sSk8lk6eP7pIvJRgd8SU93gORsSegcsM5FRoFuDXt75QDud_wGXz9W2DwJlxC9cHnkgzQY2MBVVO3Vm1lIkoskTimNocb_PxEqtju8rOPwW3brHdl56WkOcPUrmTvZxBDYVgLub3QFO-KhwejCOKpfA78AW6tgYlEemj3dL0Cn3rydRgurnRzGLHTtD_zgRp-MXghjHVswkxmdsYT0dB71Z_2zAEl4W9FeajVMcKg5NjBnUum3h33Zj8zVrVcYJIc9CDW1ffZ-TzDbUyXUkp6z55CHJpVuYCIcha3BZJThFIEHhJOA7VknY5_JnQsSqPS9lki3pXczr0qbPzss8mQg5MBVRYlI5RHtm4hrGjH7dbAry-bfARUupkx0VL1MLoqc8PaMx_j45PbbiMjb5kx39V-O1YxhlBI56awtHr4L8SximchIKJOxHh0OLA5rrDWZPkRdn1_gPMSPav2grhawWmjSG32aM2FHyVFByRM71x9Ezu-tfNKfXjollXufoh2y7YZILb5oIpiCN7NN_Zj7wbe_ulSFqVE7N5NHC0niCOhVn9mDkhwfulBTeMFddh8jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیش‌از ۳ هزار خبرنگار راوی مراسم تشییع رهبر شهید در کربلا
هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448338" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448337">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=WYwMjX6Lwts4yWoUrrVMG2E_lzf-ou7VrEgbjGfGaKpXqmtbchwg7SxGpy4KM2qpLM7sXdnxPVgN5B4-HQoxMkNur4IM-a8SGc58yPB2auExhe5K3ymL5h3eLAfMXTbzir61CnhlACnWgLZW7kVVaoD_21yLMa-8_66N8mMA3DTxK-xP9ZD752diLZDko4Q0gPgNof2mQ8jXY86rszIGKBTR2JEr3Bsg4V5KyeNlL1gSdHr6GdFXEq16WZ40BoCxdl-rt0IrJrZBzmGcinewaXqPIXNL_kOPftBId59ke3zKjBd0i7MT0zCmnFcapWZpS4_qlQF6jjBGzGs6v72S8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=WYwMjX6Lwts4yWoUrrVMG2E_lzf-ou7VrEgbjGfGaKpXqmtbchwg7SxGpy4KM2qpLM7sXdnxPVgN5B4-HQoxMkNur4IM-a8SGc58yPB2auExhe5K3ymL5h3eLAfMXTbzir61CnhlACnWgLZW7kVVaoD_21yLMa-8_66N8mMA3DTxK-xP9ZD752diLZDko4Q0gPgNof2mQ8jXY86rszIGKBTR2JEr3Bsg4V5KyeNlL1gSdHr6GdFXEq16WZ40BoCxdl-rt0IrJrZBzmGcinewaXqPIXNL_kOPftBId59ke3zKjBd0i7MT0zCmnFcapWZpS4_qlQF6jjBGzGs6v72S8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بین‌الحرمین، مملو از عاشقان چشم‌به‌راه امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/448337" target="_blank">📅 16:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448336">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8caca61e3.mp4?token=DfLo85FTsbxTVYdTeigJUrz4DNp9B3Re4fYOd8Aiyow7ie58dU1B6JyBs4Z28p3WutIMPsc-vOjU50qRcn7TMYgni5XSIKVdQTQQneUJPq11QRF4oLyV-khVpTU2FKtIX9HDq4zaQG12ImsbVICrZsh7wvqNGLnzx7UOIdimASU8Cv6eAB4kFxquzpZrsv_aqpsPaJDiiu96DhqZOXSSnwPtTVhpciy7gGTC_WwwIPm9gt9P4DxNAIdQ7pjPGAzQskH3EXiZVLMzaT4ivTV5KCEfnuizubnuDAYxBGFqkmop_6dabfsmz1yZ_wB2TZ9vK-5QXv5XNycOIy7JcqDq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8caca61e3.mp4?token=DfLo85FTsbxTVYdTeigJUrz4DNp9B3Re4fYOd8Aiyow7ie58dU1B6JyBs4Z28p3WutIMPsc-vOjU50qRcn7TMYgni5XSIKVdQTQQneUJPq11QRF4oLyV-khVpTU2FKtIX9HDq4zaQG12ImsbVICrZsh7wvqNGLnzx7UOIdimASU8Cv6eAB4kFxquzpZrsv_aqpsPaJDiiu96DhqZOXSSnwPtTVhpciy7gGTC_WwwIPm9gt9P4DxNAIdQ7pjPGAzQskH3EXiZVLMzaT4ivTV5KCEfnuizubnuDAYxBGFqkmop_6dabfsmz1yZ_wB2TZ9vK-5QXv5XNycOIy7JcqDq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در کربلا با پرچم خون‌خواهی و تصاویر رهبر شهید شیعیان به سوی مراسم تشییع می‌روند
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/448336" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448335">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71ed0fd55.mp4?token=tjpxa9ibqHLzwVSRjcmI8fmXIqbBG5hMzV38w5FAwqTFW2RdfNm1BfGUf7KrJadA5W5ww3iljTEnaOi0qhRG9ztO9JZJKCNPt7z6XlgZioBSFQ8V5O_3r7wqDAktcEDn7am_X7GuD_fGMBSQhMIhUaExNxXfW5X9j7EoSy-FIWtmu3FdBO7WJV9bMkL2Y8eqO1bwgwZGoOPIuOueT9ecrCDTvu5s2SZEYsOMdfhwav6PxPg7hg-TJbK_tLPOi-p0-SccS4ntrVIWbqF1LnBtLqSEkfsZZa_yEuBystUablJ9f4BAHV3E4srfIO6tIpeg3u-d1vn5PxbagLI5jd1y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71ed0fd55.mp4?token=tjpxa9ibqHLzwVSRjcmI8fmXIqbBG5hMzV38w5FAwqTFW2RdfNm1BfGUf7KrJadA5W5ww3iljTEnaOi0qhRG9ztO9JZJKCNPt7z6XlgZioBSFQ8V5O_3r7wqDAktcEDn7am_X7GuD_fGMBSQhMIhUaExNxXfW5X9j7EoSy-FIWtmu3FdBO7WJV9bMkL2Y8eqO1bwgwZGoOPIuOueT9ecrCDTvu5s2SZEYsOMdfhwav6PxPg7hg-TJbK_tLPOi-p0-SccS4ntrVIWbqF1LnBtLqSEkfsZZa_yEuBystUablJ9f4BAHV3E4srfIO6tIpeg3u-d1vn5PxbagLI5jd1y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین رهبر شهید و خانوادهٔ شهیدشان توسط شیعیان نیجریه
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/448335" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448334">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912f4c8046.mp4?token=X3WHlQpEsJy0al3ww7sI3OdmhILVlDNcLtf0s9VLLJcRaDAexIw0Dgy8FVjoL_4Wz96DBDec5oZSEhu4TWRibUrTmq2KzawAgvcQll-IyoNWQ1rhh99UDyZ8SzL3UDCFhvyZXtYae-8KJ0i2tlnbSecBa5ERwYxjGjLHFL4bb0iWjSCuAVsVzZBtexVKErwVs6RTKEcbLwi8a4Gyl421y0ueO4hW8W5sFlXg8-ve1hCvwYavZFwcYJ1XyyrZ8YZOacbh5PHrExmHFCaJs-zqjS10PF7xjYWlJN5VKAB4u6YttBlf4ybI4o404yA50sXQ3t7TD07KnbulLI4KWpVqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912f4c8046.mp4?token=X3WHlQpEsJy0al3ww7sI3OdmhILVlDNcLtf0s9VLLJcRaDAexIw0Dgy8FVjoL_4Wz96DBDec5oZSEhu4TWRibUrTmq2KzawAgvcQll-IyoNWQ1rhh99UDyZ8SzL3UDCFhvyZXtYae-8KJ0i2tlnbSecBa5ERwYxjGjLHFL4bb0iWjSCuAVsVzZBtexVKErwVs6RTKEcbLwi8a4Gyl421y0ueO4hW8W5sFlXg8-ve1hCvwYavZFwcYJ1XyyrZ8YZOacbh5PHrExmHFCaJs-zqjS10PF7xjYWlJN5VKAB4u6YttBlf4ybI4o404yA50sXQ3t7TD07KnbulLI4KWpVqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی به سبک بچه‌های سیدعلی؛ محاله بگذریم
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/448334" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448333">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر خارجۀ آلمان : برای پاکسازی مین‌ها از تنگه هرمز به توافق با ایران و عمان نیاز داریم
🔹
قیمت انرژی در حال افزایش است و این موضوع بار سنگینی بر دوش تمام جهان گذاشته.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/448333" target="_blank">📅 16:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448331">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73768f58ca.mp4?token=OFh3zlDhSTBPe80d1d0Qn4cKHoIzdU9yTmAqf2MBrwm8E-7gGipiVkvrjTyKIqIdsXWKJfMn9-i5uR3aeDHNYWSFWEHvSpDy-jtDf1Hs36yOl4JVfyZYj3FXe0uE1H5jeIe4QcbH2g7asxe75S6NJiPn7H2ZbdMWH7keAA9PSRHRe2PrxV2mJGW572AFVzyEH-M7qX0XdKiZWfMGyYAA_09385AltInSMKDdu7DaX8MCPyyQLX_V888mMFTE_Pwmmj2ZBIE7AJrC4WJz3eb7F26nIzmC7uU53HwFfwOKHCgswL_NBsT5-N_6jt4Ad3IBT_wEZ5Xs7YTsqFbFkKyAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73768f58ca.mp4?token=OFh3zlDhSTBPe80d1d0Qn4cKHoIzdU9yTmAqf2MBrwm8E-7gGipiVkvrjTyKIqIdsXWKJfMn9-i5uR3aeDHNYWSFWEHvSpDy-jtDf1Hs36yOl4JVfyZYj3FXe0uE1H5jeIe4QcbH2g7asxe75S6NJiPn7H2ZbdMWH7keAA9PSRHRe2PrxV2mJGW572AFVzyEH-M7qX0XdKiZWfMGyYAA_09385AltInSMKDdu7DaX8MCPyyQLX_V888mMFTE_Pwmmj2ZBIE7AJrC4WJz3eb7F26nIzmC7uU53HwFfwOKHCgswL_NBsT5-N_6jt4Ad3IBT_wEZ5Xs7YTsqFbFkKyAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلهٔ عراقی‌ها در مسیرهای منتهی به مراسم تشییع آقای شهید در کربلا  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/448331" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448330">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Q-VuyI6iZWLGnP9k8ISWxsf0bHiJ_HhCO2xJIWaeC8VJY8fvon-jT08r-oDGM1OzgaxXyGzj2qwYDKJ4kbTcgad9ahqI4NA3CBYuXE5qbA_MLjC8gbnp7Ghnni5VR9ldUFbRbZrxcwJsvgFTNtk2IZluLC4xvxT8P8cOiLZTKZA3EDbptKj743ZrneO1C0OEZlyVHoQnUMm17YisZXyWS59kIqokR_r7SEWOpyZd0PRK45KwlVTG1MxMDvy32yXVvFx5wx9DYVBOrBqXIIvb5uSL95kBiJ4lJTy34VZWSfCx0WxNjShzbFz9LjVIjDRTbmo8zZJG_Gev5P7RfnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه‌های دانشگاه آزاد از دسترس خارج شد
🔹
سامانه‌های دانشگاه آزاد اسلامی از ساعتی پیش از دسترس خارج شده است. برخی منابع از احتمال وقوع حملۀ سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا تکذیب نکرده و اطلاعات کافی برای اظهارنظر قطعی دراین‌باره وجود ندارد.
📝
پیگیری خبرنگار فارس دربارۀ علت این اختلال و زمان اتصال مجدد سامانه‌های دانشجویی ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448330" target="_blank">📅 16:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzkI1TZc4VPo_s311hWMmuk7z8ECBJPpQqZVld4vmqJZIdK8cqJPgCi3uC-Lt8MPXY7Gclx_1HDGOEBLVmWHS5XETHLORBg9oR6Sq26Mp0EgajXPNfsff2UoJkP9lSkuSg0pNS4615Ty3zvlIEw8lkY-8JBejBDo__MYAXQXAtKEa46SvuWweqiaEjbcdxt2ChTOSe4ulm2Ed49zPLnZ47qF6HKnCy1_ApWgWB-zbJKwrmhk_7-fZAd06DxhNHkn6HVMGmjRWYCGwzRbpkXRpQ28zhX6onE_9S7XOLr00H8wZ-VqEnW-m89gBfueYGw4hGkFkW6Q8j0JCQqtTbqojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obpMEB3-l9dggZyhmHlqgW0851lvlBLbH7gfd453CvWPWLC2AnFV5eqpx6x3OjLJbxfaqsl4a5dVXrhs4_Lkh6OtiKREp2BYu8qJHZTUZAJOicYg0bcEx7q3txvofdTC5EEn03QMMvVUdSBgvRv35pKCpEcd0l2-k584uoE6Azv6Pfp_SCoVEKa0w2uNm78N5toWQT4bL4LdkxZNVfvJ7-4F9GBzyTee_IQolKFlvyLzvC5xDMnxy7M-3E33offWIMBfaXHWU-EbNaNu72KmMxe4h4rjeBSG4npDjXiawhx3JuDwrSW3E8bB9wbACDSAyZMKxN-ulkQf6TqFjRg1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAg52b-Eiv5OXwwaSs4jIXwZb9nlohWGhhd5TnhzbXlAVokk36GAiV45ExtbXZaUfBIRfRaVWlzwlqO2YCkHKvngQU8HvWOBJ2oeAnuvaUvzZ62f2z8z-43FQX_eUUeg2EmsiYzS-VuDD0ZEC1L61bIc_4iZkczQ9Up5jde722ZAYyuHeJC0_pgiX-BZ8MsXR-iGWktp6xuLdvTYv3JMNjynbXTJqw1zAcF71av7kODc99i0cm956UY8j3zTny9NdFLFV5aGXKA9d_K61Yj8dHTnz7klXirDJNEcTog0MER1PZ8ReOdpnKi6vuVXmR-_EfeJq46CGrirOPB44ki12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzXk4Oo34mA1Qg_V4tUvOtBZQfBa-oizzyCexdPfx2tAVfOi2enQkC7GjEyB0RhNHZMeZS4z4E3WQ7pPszlufIdCLsJrocw5wbRhCxGJ_b5i08QCjEBUm0EoCH4HtDVDPI7d6LQInQrtwxEbIbDWo8UuPacWHkGuz6Zs7_gFJJEZ9Uv0HP0GgJ2EkdnzC-H0XUgAnlngDfllm9Wa9rnkGtq6TmdIZ-pbTr0T6jFB6TLn6gqOObefT02HYWzDtyo-NuH_9E4SrfrHkBh29eUsLlRKhX97BFn7W_Ltbg0RSVThEedIXk1jJBnCuVOtdsBb0S2X8cyJwdl1RQupUaKXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsnFEBbB30SB5aOblFoN-ZgG_4SGsbj4FVXiuVSkHa5SBwpKROsHwMjcpzlibCEl2h3M6EpEfTx2lPmlLp6op2uPEtdawcuxlFrRFHFjTYTitcO_WqxHoNfvhRO_hoyHsEA-LJGGbjZRIKcWV9b7greb15jx_bBs7i30-WAZop26tDvh0Wiq2jQW3BmmuvfeCL-Bopex6KgwvY3u5rN8L96mCbz6wOG0uPttzqIdf3nuZG1FjEgp6sSEjgq8NgBenoaQv40hilIv2rOVeBGDAP5iRhq3rrE4ywXn0vOE9Oi1Pfs10oBAjrLfrm05GwQcmnFXLrdylF9hkgoG0Eem5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFDLnKqmGccMKoVVSBHRxjFJfrPyUs-5VjBgA0ZDKDotE9PLvp21jO4R4bl3XmfKN6aP5m6Wzb2Qb1ePEnAKDsTYdr_b1YXR54u2AAFOB9ilPIAn-PAFlo0Assfknsqf6S3TQ7raPEULJe0ymLE746BzMGV5bFoybZkqCvGHcbtJqljSm6YH0SjBkVgJfnAbkH52HfIeYwv2hr8N0y6Q0Nt1jkKrhx6TsW8VCl5lqnrScDBXqwPXh2rPD8Gio-FPg7m0KlJnBB8MI4uF9h2MZZ3js_vViB2ZoG1trP0qVHnI9_MS-HCBiuxq-wx5a04AEEPJhd6aOKMBq7amhZMbDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نویسه‌نگاری‌هایی از آخرین دیدار
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/448324" target="_blank">📅 16:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfhOsfWa5XF_Wpn3YKGx1_TI9BDAQCZVaFD533jXpziXV6P_4p4tveqRjV53AJRtkyWqTyfmnxC4rj1GzaEewNRNscHF3vh2aiv6dg68qM_e7A1VLtZlwP2-DcukA8qT80OiBZZrvqdWqhjboJeh7fTjXAi2_7ZfpKHGFlxLpT7FLIPUBI1CZ3PGUTyUdtAO5TB_Pw-yrji3ECC9AYveatBNwjZ6P0F9BDxy2pcllBR7ucj8PoH8wDpYqKhEqPnaI2o2diK3DvXElsk1jtzChlAkKZMTEhEt1LWnDdDBOP58l9aH1tcl2_LP50pD6MoyPW9V1jO2I_8-wNKToq19Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجز خادم دههٔ نودی برای آمریکا؛ بند کفش ایرانی‌ها هم نیستید!
🔹
«باید خدمت ترامپ عرض کنم که شما بند کفش ایرانی‌ها هم نمی‌شوید و اگر ایران بخواهد، می‌تواند نابودتان کند…»
🔹
یک‌ آن، زمان می‌ایستد. فقط سکوت و نگاه مبهوت! حال مهدی دگرگون شده؛ انگار زبانش بند آمده و چنددقیقه‌ای طول می‌کشد تا خودش را پیدا کند.می‌گوید: « احساس کردم آقا اینجاست…»
👈
حال‌وهوای عجیب این نوجوان دههٔ نودی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/448323" target="_blank">📅 15:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37af1d5cfc.mp4?token=YdyI0FOjqqnryALleSehLuxTF_DhxVeAamOae0zPkc5MEDyNf_bURjrFZMhBP7vEVo67g5AytZaCTAmy9asQ4wuTap7GeDFVEvPv0WcAo62apzHYxtNOfjPfjvlku1z2BaJnjBFGBHC0oDHhwx9qgBFlN9SgWhu3Qc90uKr-I6MvmdzmCxn6_tEJ2wV0HkJcawV1GDFhAH8qUGA2Lb891ExA4zZGkDymHpFVZISKd1T51ZXA_rbekJ4CvKBdZgTk3vFnvHTtyV2ByF6-joiVtH-J_Y9nOEek8kOQ51UBRTdMo-fUbZs3-DhYi0fjmdbDc01jnjQkstm4GWyJD4CpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37af1d5cfc.mp4?token=YdyI0FOjqqnryALleSehLuxTF_DhxVeAamOae0zPkc5MEDyNf_bURjrFZMhBP7vEVo67g5AytZaCTAmy9asQ4wuTap7GeDFVEvPv0WcAo62apzHYxtNOfjPfjvlku1z2BaJnjBFGBHC0oDHhwx9qgBFlN9SgWhu3Qc90uKr-I6MvmdzmCxn6_tEJ2wV0HkJcawV1GDFhAH8qUGA2Lb891ExA4zZGkDymHpFVZISKd1T51ZXA_rbekJ4CvKBdZgTk3vFnvHTtyV2ByF6-joiVtH-J_Y9nOEek8kOQ51UBRTdMo-fUbZs3-DhYi0fjmdbDc01jnjQkstm4GWyJD4CpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلهٔ عراقی‌ها در مسیرهای منتهی به مراسم تشییع آقای شهید در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/448322" target="_blank">📅 15:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIgQ8A3xfTXxyFHC-g6eNrOvRqnBD08TxsKgN9S5ETOmocEmC4ixii-y7yUeWUNUF0Juqh5GYxcpil6nDZyCgy6lnY9Q50PR-MOnMHGvghW1uAee8dgQZ4P-3b-4xVlMe9m3z-RHAjOx3lSedPdtoFTrF1OdXmXHT-ppYPbUJu87DYQdxrmdqnjndpqYuzgZB0o8qu6B7Q1nzkf9lHSoFAPLRx_Q_2d0OjP2KpGs74d07M71Zcq60C80sEznpFm1xJH_ifJORjiV2mjmz7wtIFnTcd_Q3wgSF7M3a-qgdqsUI5BIqjFCBBH2EzBCiH0A_CBVladutxvoucjSKg-tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIal9u0clg01ee3v4iEZrDe0Kw15QJF0sxpXV9Y6YwGrZO3hwbsV9Z3F5FhbJuPfAbQjAGFtHNZnQKerNIJJDbE44g4tPohfh9qNPUKJV4uq8k90SDrFEtL1XvXnHzxy-BPgM38jOaK4lr5gEyNAJ_XOaMO1MfENDF136W3hDWUKu23VLxANUcVkOZNOEyqs4f1BJdnI8YHO0hHw0-XGJiO96V4wG2eU-yHLMZTquNOu_cJUZTnQbnFEHW0m3XxtGlMKrLgOJXc-XtsmBJD-QBpjEdW29Ee79U3d4hrQEa54BzXHg23JSt7Hpo2vUNEjTddTygMLdB2OmnrAbqytbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3wG78r9-_MUpkT-aF5TPTKpTvbyFfAQuyTPfRXRVVw1Jb7pD968LJCv3deWk8NRoxxDFZix3iB6GXGTiDM3zNk9QTgtA6bpWFGlcHjLzD5q_pIRrQPLWe5zVpaysWSBMAlpQrcXdSns3tIAY2n0oIpqU0jJk3px8yAHkkgk-r0SPVyIgJmQBqI1EqO5k9lgA2slhrHW_uoyBaphNvlCMudlKxB1yKXgTgHKarlLwh5QwxYP5pLj55yoHyZn0i8tOdjn36C6QNxJpnPXbferaLSoeb1PaRx7SpKpGi6VN4xW097y9B1pfAoAlPp76XZReb1_BbiacNT2Gl4pbz3s2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzHHRWwrahClYQQraCArqtbE7mjaVl422F49HHNrXvn4RLRiPz1QzfoCplg6dRmIJNLw69y3AHiq5QyOFirs7v7PylJvWsZ-Dabwp5r93oJAOG-wPznLDomT4XUFG6fcvVNlLGFf2q8b3QiELZ5z8SB4hbIMcakcJ_g8M-p0o_rfor6Z2Od8h2e1uuFnNZKX46n9IZhHIYD5fOfcQxcMdMElhkDKqNEE5RDdE88I1tvqxtH89iHUVDqXJGcc4Lh--XoeRNCO8svviILOL5udhHGjXLw1QOHkQqbELFx53-yvgn_sWOxW_YsuezvHmQYwO1b5XEbEriKcQxiNuLW8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKqYhji7KlekGppJ5yYy2DfNqZLjEsRaQmQA62emsTdrUf6A6bWeSfFo5TyzFQThM3GuhU0uXhUjOhAkKdPtvNSmpMWTo3EdAazKKzgElg51lBpJitCp2acMP1UMAaPsJcKoAEm0vSdIQ52XMVNzMdV6dwqyYcUv0XQYN7AaUTkg-2NePmFXgdwEtiusSFmPj9488tqIUzwCaY_spyyq54CXco4ztbBGz9kA1C4bLQ3pDc-1rfJIm12xF1yQz7OXuBBgEfct_sBTlzOLwCSPZtO0kA_30IyfTQvGvDKLmxjg8AAdHATaN2BvkDMZa8sR2x9aCTTuTvYQcwxHvRqGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsywQqIl82sp7mqu5hRG-W-Sz3yL1UHEiWxI-sCccOSWYaP8HIcLDHApFnPomBP7sSjXe8EvVbgT2wcpD1PKGZ7UKznLcMxqIlfMJb_4kwzbWf7s0kTNcoS-gApFOw4-06zyPadAPGUo2ZzzPMEvYWotYssIGD_y8jtbDNJmmrWsEXcRrWBgsCM1gULCTxfIr2Ub0YdpcXpHXCnLR-AOQclH_Rdo8xBV_7DCoxuSKyzfEe_zROLLr0-abfyD7ZrPgeorO2oPp7naq3L_cogQQBXg4LfhdgVoIkX6Hnn2Pa6GFXneKIXud_Gcz_3ycAbJD2WY7EE3NM4_bPiA-QoWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPfrHLS0E5M7RQCJkBVEpWUkgcA0eSADeWB1T4BC0A8rZVebc4gUqw4j0T6YI6Tvu3L13-hvVNtMZP5zuA7hixAJf7VxcBrxM-oRhKA_Ic-TCtkXRjerqm4vlb7seNckMJFZqF0OZVcgvPQrlASR9uL7b6nhImF37CKpGj1OuYui3yvGuNhIYu7NfQDciHIxrkZGzGLBZe2uhBChPtCFv_dixJLGCb8yqnocLHpRtADo70Bj_e3hKQxyH3zu9ae-9aAiQW4Qual-6xbh5h_A0aVEwbLUreCNPvf_IxKMBACKMI_1tOzbDhnw0Wh_SVSHDPepFHGPHgHvnvz7siRsWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر رهبر انقلاب و پرچم‌های ایران، عراق و انتقام در دست مردم عراق هنگام تشییع رهبر شهید انقلاب در نجف
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448315" target="_blank">📅 15:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59348358a.mp4?token=aX3veZeJl5Hg0BNPJB5EQ6TJrImAHfGuQkxd5zONdD82Iue72U6xUCztIOc0Lnf8H0NKbE62PZDu2ANk_O-chwxocZXQbIGOcUWE4Jh9vmVGrwwDu-cBTMm1L4uxTkh4IhoUGNSxYzDyqnOi5TX-4hKsWUmSiz89N4ahczUxbgiNpMCnLIH8K-K6ba2UZ_FRzTczQDuJjHz_AQ6ex3xxfbYp2McIcL8kRR3m5cMUygzy0p9GEBxmHTjzqHPgiEv6R3o78wh1q-_Anuerv8JoB_rndSCVU90hAbcJTmieUX29cAdbDM6mP55yB4_UQDnAV6QdhWiAp39NsCXNbLDbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59348358a.mp4?token=aX3veZeJl5Hg0BNPJB5EQ6TJrImAHfGuQkxd5zONdD82Iue72U6xUCztIOc0Lnf8H0NKbE62PZDu2ANk_O-chwxocZXQbIGOcUWE4Jh9vmVGrwwDu-cBTMm1L4uxTkh4IhoUGNSxYzDyqnOi5TX-4hKsWUmSiz89N4ahczUxbgiNpMCnLIH8K-K6ba2UZ_FRzTczQDuJjHz_AQ6ex3xxfbYp2McIcL8kRR3m5cMUygzy0p9GEBxmHTjzqHPgiEv6R3o78wh1q-_Anuerv8JoB_rndSCVU90hAbcJTmieUX29cAdbDM6mP55yB4_UQDnAV6QdhWiAp39NsCXNbLDbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش ویدئویی از تشییع و بدرقهٔ آقای شهید در شهر قم
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/448314" target="_blank">📅 15:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYJLSOmHJCS-3ZB2NhlEBXT5vkTcOLvaNoUZxS806AlA44VwI8-yhFWsEhz14C4Egq_eVU80xICMWjkZSRYFyq3qcW631WheSwmGFgAAZEG_OQwik91QAXBFKCfpoKFCQyNKSZ7vzweDTouXfVi31DEo0RibiPaacBx9vG_Vgy1p8oD-V-zj340T3w7l8qD8CUV75ur9FPaEvnrr0unr9b9syHk9ouoi_3n1oLhW2EFqt5dPdF9YL78fp6CUh_l6kAWlqyk0D9oZmnkvkkbegy0yl1SzjpcIOmH-ieHZzpp1wkJK5rRegsRTEk-1fKzGiVsRzzDmwSti_-OeMg8z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌های عامل فروش ارز اربعین معرفی شدند
🔹
بانک مرکزی اعلام کرد بانک‌های ملی ایران، سپه، ملت، شهر و گردشگری برای فروش ارز اربعین به زائران آماده هستند.
🔹
جزئیات مربوط به فهرست شعب فعال، ساعات کاری و نحوۀ فروش ارز از طریق درگاه‌های رسمی این بانک‌ها اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/448313" target="_blank">📅 15:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57aab4ca1.mp4?token=pwirxfZ9xI55JcJdjgb38okq8jTE51VW3B7jJMC9Gyw_EkRZTga4ccxfzvwkjnTr-Mig08x3bbXfMySVBPq0lNay4h4n4SDe6rWwABIhtnt_oqJI6ZB_Pero2x2ZtCYn7NplsXGgcTLUvITi-sAZv1sdDWMql9c7ij59nO4MUiyZBhQcgJQfsd1LmnDRwyo50Yqt8m7rMvsD9-E2qXb0RyPTB-lp5U_psRvN31aZuM5wlXPDELWB3jQ4-piNUTwpIb2gX0QoWS6AzKHzkki_yBIkmuySdBbX6qUBIKRLwysWTCtlmcrZTTlYPnG8YJsBtGU8EWPJbjcMtetxFBTf8q3obXTgoknygYsBpl3EK9Eumx_Y1Q-1WjcwnuZr6BLh8C0wDP7jw8_mezQCh7f5SFr5d-nwcx02TwWgxUqw1ehxEmF5kOScurbdOy4-KWRlrns5pA7iW7FalHPustVII5YIk989s2_e2xdNQjO3bvBjc9hBPQwafJ6TQZ_nVawbzVJGogGJWpuXYIizL0xX7dHyAbt7PZ3LKXoAEnTMCi-bKUS39UlDubMpePq7jzY7qda0t7HGX5fJU4sh4x3DgAu2z5Ddguw6Sm_9ASBO09EEILQ9obwjQxzAMlTl6Umg2SsTwV5rJP29iKezAykALd9__1PTLuvHMGM1v8jcxDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57aab4ca1.mp4?token=pwirxfZ9xI55JcJdjgb38okq8jTE51VW3B7jJMC9Gyw_EkRZTga4ccxfzvwkjnTr-Mig08x3bbXfMySVBPq0lNay4h4n4SDe6rWwABIhtnt_oqJI6ZB_Pero2x2ZtCYn7NplsXGgcTLUvITi-sAZv1sdDWMql9c7ij59nO4MUiyZBhQcgJQfsd1LmnDRwyo50Yqt8m7rMvsD9-E2qXb0RyPTB-lp5U_psRvN31aZuM5wlXPDELWB3jQ4-piNUTwpIb2gX0QoWS6AzKHzkki_yBIkmuySdBbX6qUBIKRLwysWTCtlmcrZTTlYPnG8YJsBtGU8EWPJbjcMtetxFBTf8q3obXTgoknygYsBpl3EK9Eumx_Y1Q-1WjcwnuZr6BLh8C0wDP7jw8_mezQCh7f5SFr5d-nwcx02TwWgxUqw1ehxEmF5kOScurbdOy4-KWRlrns5pA7iW7FalHPustVII5YIk989s2_e2xdNQjO3bvBjc9hBPQwafJ6TQZ_nVawbzVJGogGJWpuXYIizL0xX7dHyAbt7PZ3LKXoAEnTMCi-bKUS39UlDubMpePq7jzY7qda0t7HGX5fJU4sh4x3DgAu2z5Ddguw6Sm_9ASBO09EEILQ9obwjQxzAMlTl6Umg2SsTwV5rJP29iKezAykALd9__1PTLuvHMGM1v8jcxDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین جمله‌ای که امام‌حسین(ع) امروز به رهبر شهید میگه چیه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448312" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd340a6da9.mp4?token=KBv1iqRfGI_CVOC3eiHWoGwallWiTga-iHKWY8zuh_VUmIlJWwD1mifgYMCmOGQLyXsLdh0e0jeiSjWbfu9nwC7F-9kTRNAiGMiz6dDB_V-3p58AmnYJi8H7N2tc-h3VWiRyTWzPjEnRoS3TAvGT_HZ0MRXBlGMHAvcYdUi9HazyEHulLQWM-5lqzhfEBmw97E-jYcodKibsJrfoymMRql1KeKVAU-yBlekCOABN7v_PtwFcb6iz3_3bbQM7u5d2Qf9W108A7FPICyjoRrq2PEouUgEdP6OajxQuE1Tljz582qZcOASDz-gtWJPY2NzeZesRVpf44dsqokmlvjnf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd340a6da9.mp4?token=KBv1iqRfGI_CVOC3eiHWoGwallWiTga-iHKWY8zuh_VUmIlJWwD1mifgYMCmOGQLyXsLdh0e0jeiSjWbfu9nwC7F-9kTRNAiGMiz6dDB_V-3p58AmnYJi8H7N2tc-h3VWiRyTWzPjEnRoS3TAvGT_HZ0MRXBlGMHAvcYdUi9HazyEHulLQWM-5lqzhfEBmw97E-jYcodKibsJrfoymMRql1KeKVAU-yBlekCOABN7v_PtwFcb6iz3_3bbQM7u5d2Qf9W108A7FPICyjoRrq2PEouUgEdP6OajxQuE1Tljz582qZcOASDz-gtWJPY2NzeZesRVpf44dsqokmlvjnf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر شهید امت تا ساعاتی دیگر وارد کربلا می‌شود
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر رهبر شهید در کربلا از خیابان ابومهدی المهندس تا حرم امام حسین (ع) تشییع می‌شود.
🔹
پیکر مطهر آقای شهید از اولین ساعات فردا در مشهد تشییع و به خاک سپرده می‌شود.…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448311" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تابوتِ پدر می‌رود از دستِ یتیمان؛ تا در بغلِ شاهِ نجف، سر شود هجران...
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448310" target="_blank">📅 15:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448309" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه در پاسخ به تجاوز و عهدشکنی ارتش تروریستی آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448308" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر شهید امت تا ساعاتی دیگر وارد کربلا می‌شود
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر رهبر شهید در کربلا از خیابان ابومهدی المهندس تا حرم امام حسین (ع) تشییع می‌شود.
🔹
پیکر مطهر آقای شهید از اولین ساعات فردا در مشهد تشییع و به خاک سپرده می‌شود.…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448307" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1A6-jh32xZzERt9P1x_q2HYXkRrorS3wobAshJd1zJ9SiCIUENsOcF6ItrHYDOYaxcZDLXA3PeZhyGp3X_F1p-mJVzEGKRVXNN35c4hZcXNBVyuOG4tGtk47sodHwWWBIQeisTSxjbHjW2tQEPSd7447EasegRUdkshuKoW7SEcTJXWxgyjOC-DrkC0LqMN6w2tNQBju68Ir4mvsNWCxFPtjRNql_XxHALOqSLSRDSc91Dos6c-g6fpEK0AQ3it53ExbYyTMUYgCUVwSxPav0yOYqXsOHdgaxpKs2QTUyCZQIFFFs1owEVxPYXuKPsOLikVlawRC8jSxWcU6rMe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید بیش از 563 هزار تن فولاد در چادرملو تا پایان خرداد ماه/ رشد 18 درصدی فروش
بررسی آمارهای منتشره سامانه کدال حاکی از تولید 563 هزار و 27 تن فولاد در شرکت چادرملو از ابتدای سال مالی (اول دی‌ماه 1404) تا پایان خرداد ماه 1405 است.
بررسی آمارهای سامانه کدال حاکی است از ابتدای سال مالی این شرکت تا پایان خرداد ماه 1405 در مجموع 4 میلیون و 368 هزار و 576 تن کنسانتره آهن (خشک)، 668 هزار و 436 تن آهن اسفنجی و یک میلیون و 747 هزار و 812 تن گندله در چادرملو تولید شد.
این گزارش می‌افزاید: مجموع فروش چادرملو در این مدت 505 هزار و 187 میلیارد و 283 میلیون ریال بود که در همسنجی با رشد 18 درصدی نشان می دهد.
5524 میلیارد و 838 میلیون ریال از فروش این شرکت از محل صادرات بوده است.
سال مالی این شرکت منتهی به 30 آذر ماه 1405 است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/448306" target="_blank">📅 15:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBM7EWXe7waE3JiDdc3YE5f0IdrkrIq-3wdXXpJIj_3KoMrB_FJU30nVj0x659-a26YkJUxzky5a-B6Xe2K8dnG0r-My7GTTXPMkv9zOAleij9dYIxVVp2dOmE5cv6AJlsJax1fLwfzCH5hGrfviQ17PBsHpDz6JpbKPEM4rXammXqCEwqtBLZW8juFAq08NqbpZms1e7FVlNAiVCJqUp8kYoWSarZf--_Ck7JWN5zUw32V8ENgHyn6cyokkjerZkzgi2H2NhQx5h9l0zwfPkI3SCgEhK0pRxwjPFJ5me3RFYL-5MFjtkld-fjI_TyLyDCpnD9AvctjwN59x6nvqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448305" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448304" target="_blank">📅 15:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره) که برای نخستین بار و همزمان با سفر رهبر شهید انقلاب به کربلای حسینی منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448303" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448302">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران باید پایان رسمی تفاهم را اعلام کند؟
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف،…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448302" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b4b4ed9f.mp4?token=JoCjg95rPh1D6gRiFe-h0h52IoV_ZqnZvwDuNVmWjoUPbgN2Y34qjYohCjSEoTAqUx52KZw99vJSjEcAJ2dn_QxuSMtNqxx9JC7ryhtYxl5N7mBSJl0fit0lU7n2rVet7eFMATqadS6RojUg1UrcTkJDalIX4hPTxiSrFtZcpmvx1FS7Rund6CrD9iBEsV6sMgSzDkwjGIRniF0gkFieNYTfmvmsrGAVxmozs1eKKWZ9V6IqiFxMiZ0F2NJiJ15d3okOWPJGR0T173aUAekZkNH0Alw_E6_iahYbgSZo0FULp26IG6icK760l6lGFSiScJTroodGl0qOAwUGbAV0spy0wPB9X77o1ItiJPqPBQgdaEwTlQ00IU4_K1eJwOSTVglSlDYQszh3NStLs41xN-Dm1CpxlJwvUyoUhf3fQHMSseDw8q9gOoTKDsKkFToPT31wm7g8vioVvwMHtPeFbth2-L1J9g8j0VGGjBPpR1wif0xTzES4BlpiEPJW3j4Z5uYjTLALtCX1YYNq67J2K5NoCDQE4EcQXACjEGpvmfHXAlqdkOlwtukbwx-aNX7F7TsBZb8eHBErf9RFnmN06DmLjl3OsNog1eIdHIipGpOt7lfcLkaLeF2IxWkAR4hS-VR5JrFM6Yy6FAcJHk1nbp7WUkuKmvntcbiE-ySSQ3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b4b4ed9f.mp4?token=JoCjg95rPh1D6gRiFe-h0h52IoV_ZqnZvwDuNVmWjoUPbgN2Y34qjYohCjSEoTAqUx52KZw99vJSjEcAJ2dn_QxuSMtNqxx9JC7ryhtYxl5N7mBSJl0fit0lU7n2rVet7eFMATqadS6RojUg1UrcTkJDalIX4hPTxiSrFtZcpmvx1FS7Rund6CrD9iBEsV6sMgSzDkwjGIRniF0gkFieNYTfmvmsrGAVxmozs1eKKWZ9V6IqiFxMiZ0F2NJiJ15d3okOWPJGR0T173aUAekZkNH0Alw_E6_iahYbgSZo0FULp26IG6icK760l6lGFSiScJTroodGl0qOAwUGbAV0spy0wPB9X77o1ItiJPqPBQgdaEwTlQ00IU4_K1eJwOSTVglSlDYQszh3NStLs41xN-Dm1CpxlJwvUyoUhf3fQHMSseDw8q9gOoTKDsKkFToPT31wm7g8vioVvwMHtPeFbth2-L1J9g8j0VGGjBPpR1wif0xTzES4BlpiEPJW3j4Z5uYjTLALtCX1YYNq67J2K5NoCDQE4EcQXACjEGpvmfHXAlqdkOlwtukbwx-aNX7F7TsBZb8eHBErf9RFnmN06DmLjl3OsNog1eIdHIipGpOt7lfcLkaLeF2IxWkAR4hS-VR5JrFM6Yy6FAcJHk1nbp7WUkuKmvntcbiE-ySSQ3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر آقای شهید ایران میان خیل عاشقان در حرم امیرالمومنین(ع)
🔹
پیکر رهبر شهید مستضعفان جهان، با عبور از رواق حضرت زهرا(س) در حرم حضرت امیرالمؤمنین(ع)، به‌سمت کربلای معلی رهسپار شد.
🔸
رهبر شهید انقلاب، آخرین‌بار در ۱۸ سالگی، یعنی در سال ۱۳۳۶ (۶۹ سال پیش)،…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448301" target="_blank">📅 15:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXuILknt6LwWJEpHbIQp4peN4NQ2QRovACDNIdwsyZs9_QWlryFhmUM1fQ0iKr33IUnjy0qi6YskAbZ-McTF9WkwmM9ixc6_niTnD4m4rDtCIPzKYyPMtDWPZ7DNr4H5G6LMt8U_n1KKAKLtHO8wcbJv0UbKUygK8da5rPejcy7PYLPnJLTLSL66pV8TqdSJbAs-R1IU2qGM-1orKi_wVEqbVN4KtcFy0p0LbVN7TxnLYW5s1Im_4E1iRxNCkLgSD8Mj1eGWXbB4m1m-vcaZNOHJx3U9xg4tx9aJ8bpLlEXL3-d5ItU1cuwFJg3jbkRdMSBJFMb_AmF_5EhAaqIVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ایران باید پایان رسمی تفاهم را اعلام کند؟
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف، بندهای متعدد این تفاهم را نقض کرده است.
🔹
از ادامه حملات اسرائیل به لبنان و توافق رژیم با دولت این کشور گرفته، تا حملات مستقیم آمریکا به جنوب ایران و منحصر کردن مصرف دارایی‌ها، به خرید از کالاهای آمریکایی، همگی نقض صریح و آشکار بندهای اصلی تفاهم بود.
🔹
با این‌حال، آنچه ایران از آن بهره می‌برد، فروش نفت، رفع محاصره و فشار برای کاهش حملات در لبنان بود. از روز گذشته تاکنون، اقدامات آمریکایی‌ها به حدی رسید که حتی همین منافع را هم از بین می‌برد.
🔹
ترامپ نیز در ترکیه تصریح کرد که تفاهم با ایران به پایان رسیده و در تازه‌ترین اظهارات توهین‌آمیز و تنش‌زای خود، ایرانی‌ها را «یک‌مشت آشغال»، «سرطان» و «بی‌عرضه» خواند و مدعی شد ایالات‌متحده شب گذشته «بیست برابر سخت‌تر از قبل» به ایران حمله کرده است.
🔹
باتوجه به رویکرد رئالیستی در موضوعات بین‌المللی و لزوم پاسخ هم‌سطح به نقض توافقات خارجی، ایران نیز باید پایان رسمی تفاهم اولیه و مذاکرات پیرامون آن و مذاکرات آتی را اعلام کند.
🔹
در یک سال اخیر، آمریکا تاکنون از مذاکره به‌عنوان ابزاری برای حمله استفاده کرده است. همچنین ترامپ کسی است که سابقه خروج یک‌جانبه از برجام را دارد و تجربه دولت روحانی نشان می‌دهد که باقی ماندن یک‌طرفه در توافق و پیگیری آن از راه مذاکره یا قوانین بین‌المللی، سودی برای ایران نخواهد داشت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448300" target="_blank">📅 14:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=WUheEtuGkU59g28W2Sp7Bg9vGqmm_qR8hZp0Vo_vvlUPG04mqsZQ_UjsNAln9WX1LqegG5Psgof_D4ANHAmL_lndiOsyoPkX8EHG9HnOsyYLPUv4AJKvlIbMfELSLUnfM8_25LP_IMiaYvOTDL5aFHbNVjqFsmv9N6A9fVjJtMqK1gahseqRODKCPVM4rKD5sVrMYrXeVJ7o1C1QxXy-2Qc6mVspIF6Cbr6JBu-fjTUjz9l0H3TknJW5AW4F-Yc2nAqhyQC34RGrDTkXxCjHBru-T6vR2FPqYFU-VRrjb0rSD3en5VVnwZiOtTfZUjI94I08nT7gyBbAovc6qeGYhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=WUheEtuGkU59g28W2Sp7Bg9vGqmm_qR8hZp0Vo_vvlUPG04mqsZQ_UjsNAln9WX1LqegG5Psgof_D4ANHAmL_lndiOsyoPkX8EHG9HnOsyYLPUv4AJKvlIbMfELSLUnfM8_25LP_IMiaYvOTDL5aFHbNVjqFsmv9N6A9fVjJtMqK1gahseqRODKCPVM4rKD5sVrMYrXeVJ7o1C1QxXy-2Qc6mVspIF6Cbr6JBu-fjTUjz9l0H3TknJW5AW4F-Yc2nAqhyQC34RGrDTkXxCjHBru-T6vR2FPqYFU-VRrjb0rSD3en5VVnwZiOtTfZUjI94I08nT7gyBbAovc6qeGYhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل ناتو: حملهٔ دیشب آمریکا به ایران کاملاً ضروری بود
🔹
فکر می‌کنم بسیار حیاتی است که آمریکا با قاطعیت و قدرت واکنش نشان دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448298" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtg7h5RmbI7JlDOmF_tta-DDxgZFw3NVUqD3CfWK7KRMq-4rvS402phaa6KNSQD9jmt9yNrGPoEK8OIu-kq7qbluSvFgEdSeFPR8kJ_xwEnWposH_RGrjjVImWi8keF-Wr2zmYC14QuykJfnfDMLrAII7HdJxaE7o_04cl1VtLnvw0qdRmxkvRga8V4b-9-AQ18aHRlg-bszO0Vwp6CYdXiuLgwc8WD6jJJnvlpb-pBTzlPrSctEkch8rqhRgsOhgagY4v-9DQsQxbnzNLboK6v2Y3YrVszxsUNjo4jDIA0fJGP_LLuy-5iemqIkZcMZB4vAHi3ehQ9XX4LvDiKkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزامات راهبردی ایران در مواجهه با سیاست‌های خصمانۀ آمریکا
🔹
تاریخِ رابطه‌ی ایران و آمریکا، نه یک فصل، بلکه یک کتابِ تمام‌عیار از پیمان‌شکنی‌ها، نیرنگ‌ها و ضرباتِ خنجر از پشت است. از کودتای ۲۸ مرداد تا برجام و خروجِ یک‌طرفه از آن، و از تحریم‌های فلج‌کننده تا ترورِ سردار سلیمانی در خاکِ عراق، آمریکا هیچ‌گاه اخلاقِ وفاداری به تعهد را رعایت نکرده است. هر بار که لبخندی نشان داده، پشتِ آن نقشه‌ای برای فشارِ بیشتر بوده؛ و هر بار که بر سرِ میزِ مذاکره نشسته، در پس‌پرده مشغولِ طراحیِ توطئه‌ای تازه.
🔹
در این میان، یک تمثیلِ ساده اما عمیق، از مادری که چندی پیش کلیپش فراگیر شد، همه‌چیز را روشن می‌کند. مادری که می گفت: کودکِ دو ساله‌اش یک بار از پله‌ها زمین می‌خورد، دیگر هیچ‌گاه او را کنارِ آن پله رها نمی‌کند.
🔹
کودکِ دو ساله، تجربه‌اش را با پوست و گوشتِ خود لمس کرده؛ اما برخی از ما، ده‌ها بار زمین خورده‌ایم و باز هم دل به وعده‌هایِ رنگارنگِ همان دشمنِ کهنه‌کار بسته‌ایم. این‌بار نیز تجربه‌ای تازه ثبت شد و به‌روشنی ثابت گشت که علی‌الاصول نمی‌شود به آمریکا اعتماد کرد؛ نه فقط به دلیلِ آیاتِ قرآنی که ما را از اتکا به شیطان برحذر داشته، بلکه حتی به حکمِ عقلِ سلیم که تکرارِ خطا را محکوم می‌کند. تا وقتی این حقیقت را با جان و دل درک نکنیم، مسیرِ اشتباهِ گذشته همچنان تکرار خواهد شد و هر امیدی به ناحق، ما را به بیراهه خواهد کشاند.
اما در صورت تجاوز دشمن چه باید کرد؟
🔸
۱. قطع کامل صادرات نفت از منطقه
🔸
۲. بستن تنگهٔ باب‌المندب در کنار تنگۀ هرمز
🔸
۳. «هزینه‌زایی» و کشته‌گیری هدفمند از آمریکایی‌ها
🔸
۴. تغییرِ دکترین دفاعی در راستای بازدارندگی حداکثری با حفظِ ابهام راهبردی
جزئیات هر راهبرد را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448297" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZl0X-0CGVlQCwIJJDcQo5Zu3JCin9RoCDHP5brOO10XmbxERYIJ7yRy_xUPciIGVVQn4oZ10SKHPtgqYUCACFPjFUUz8HQKcpOoJVloerb2CY5XdcMqdUAwOdTFZW0rWYY9JlLSGRvFwQfUiYtiYqWtU6YeHPuaqswxMuQjPkaehf7urWkzfv9azzZY0-mQFXF046dYWRoF-0obKQ5hT2ZObpIvcgbg-exCkV6qjKOh7UJa65tSZVwcGg9gnUkPvC59iKIzdu42GSdos2V5plPWLOnryHlzA8mvWop8UfNrBagomQirMPLIClpV2kFC68_-w5SO1zF0lFrFYtZuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلسهٔ هیئت دولت امروز به‌ریاست پزشکیان برگزار شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448296" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448291">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG_BabfKh2jryfnXNuT4DFghYmC5vkShm2j8ACjos87Z0ZdsrZSuvVnjUg2yB6ghYfQuZOO8GVo-yMO8whYCN91WWwbJr6tu3nAs8Th2J0N-J0KmUpg1yaXSGJAH0o7D3h3Yc7ZVtiecK0RbwAtMlqq19Ubnpx5048C3hLvl0UywCdfrDSf606S1aisVWUAQdTUNnXFblZbwhRHkJI3ngBQ0DlXDB2GoJAbIiaY2AKE4cbTEOSRL4JJLPerKl7KHNJu2OlY1B5XHA8UEp2rEst1tcJIMztMbf31wLo-BCD0pg2kNW--C0-tsHSXqvEHSyZbZmGH-pXoBIBNie7VCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qupqh2WRCkfLOXGwJayGx8c-4KLybpk91oCZnRJH66QsIz53fvlAMVte0yQSojoh5kbxosOxzd7p7mfs965SmeqiDg9y24iiQ4_kjKBocApYX7dUWtAE0-l5Wy2glZm8An9eFNChr9QJGSsTGuHcGqGVqD-JQ7FRx_5t0q15OomwxrBqgrrR--1UfNvldoy-W0p1L1eAVOuTO7mgHhkv0JYr2BtPfUOxof0EGBap35FYujZWUyW1zZSv2SCh0QxobOkuGOC5odEMhV-yIz8StWi8Jzn8PNnmGJ7OTd-9ifdrSL7rTaiL2SZLIXZFy4iEoJsg4GrqgfWBEo1dd9tzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF6CCEu0YlPEI1Ef6JUIpnzPhSL6nkjrl4zdkZaxZktDslrT7AAe5wUfrZoCC8UD47qZhS3fQ82VZz24Rw5TvHnglmvIfSZLnbN1RTqICKDaEQ4dhVhBHlniZzxjjt16JrjJcB3Bz23hNHLTUP6nzTKlRrzeEWEUoTc7z8oFlIRmWLyc0SZcU9oWT02tyFL23I2lxpL9QjXdcgM75dBZgTYiyv9-LACAOETy7pFmuiubBhRrcxQ69EpSTbl0WP_iIg9uucOOjCP6Qz3pzozevD9MqVpdvyoJnPAJs5f9aBo_rYYezb3Uwzb8N0DYil1nbHuH_K_snycjzv2MT84QqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZ1oHKKif-l1ezMA0EUWEhDNDSpsyZ8NwuPWZcO286-8sQcLgzbFDlCIwQo6FAo67mvXrWX4RGr_ooHqFtWP2AbkBJNRup-u_2DHKvf7E-hJcFFsdt_ymi7whxmKrE2lapPhK-IlbzL_INKAVHkbBMTbXGPiFZg5P2Y5esyqD0g1oBS56t4e2TQJ5v3MwSWTUdtyrsP6I922I198AhcBzMO7hKix6pozmuqkOyyQ8fKBla2Tzri6ewz-eM8gCUsR22co0nfwNF6vT_vO5uHLKeWse3Nb5Xp5cgyW7YmWU1aTNevnVdU97Su_b-bksf73ldP2TvUEi75unoJX1WX_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWW0uJqXkepGrokSB9if44kQ_SD3sAGlVvGrY4Nfk5hwU-i9BhvMPPwJG2eoFhFsOPv43HGFEzBaJSj5FFV3Jo46nzNtHQnYj5bE90MxUvwV6K5jRsQDmR-HV_9oSVvVrljflW3idfMnIYqWjJrAhjU7d60TVLtpAZBXryuB7LmRKrfmSK7NcXu2lxfRWWvE7t95rdkqy-S4IdP_SxWj5WB-j7Bn7DJyNti-cpWewp4vFp2_-giQGyFtPEiWkSmzQZRgpAq0cy2b816GW0SmJAtneqih2A0c3cUZHKWSh1JhpqIioct3GphQP5yGvko6zjLQBKUfNV_IIolIDzXcMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسهٔ هیئت دولت امروز به‌ریاست پزشکیان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448291" target="_blank">📅 14:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448290">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65b53704.mp4?token=OG5zIurWuTP5ZCjqamw9-HX-6MNh96HxTQkVYrWoYSHtCZ5Sk5F0D1-EtOHGCSxH4kPoVTuA3p_Yy4K0t-sgo5WLTZhyxkcJk82590YRSjx8NTOJ9ZzZYhfO_NymNFK1AcgwkMpnW8HSHMIuZRF3ixqnV3IAztjxUrjFBvY_mfhzXoX7mC4F1KS9LBKO9xdk7COUjUd1cYhq7N6L5l4dCo7P9bgrmClBDsbniz4tssiwzabGZ9NEzyUC4NhpLVGkzNrkjNKpsErDILHqz_dAhURlBNDRKAftCJ_DsVx2h7T9huBYJNYpqtEvNzjRFrvsRGdaC9w97kUs53aVXzcokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65b53704.mp4?token=OG5zIurWuTP5ZCjqamw9-HX-6MNh96HxTQkVYrWoYSHtCZ5Sk5F0D1-EtOHGCSxH4kPoVTuA3p_Yy4K0t-sgo5WLTZhyxkcJk82590YRSjx8NTOJ9ZzZYhfO_NymNFK1AcgwkMpnW8HSHMIuZRF3ixqnV3IAztjxUrjFBvY_mfhzXoX7mC4F1KS9LBKO9xdk7COUjUd1cYhq7N6L5l4dCo7P9bgrmClBDsbniz4tssiwzabGZ9NEzyUC4NhpLVGkzNrkjNKpsErDILHqz_dAhURlBNDRKAftCJ_DsVx2h7T9huBYJNYpqtEvNzjRFrvsRGdaC9w97kUs53aVXzcokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448290" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448288">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3fec6920.mp4?token=ONeCHlbXmoI4zxYbStqYVlz0Kpm4BTKu8GyOB7B3qYRBOFJZcoTMAqB9dYns2sOSXLtHgWIhFeLQMZQKz2dbdlv5cBhcv83_FmC_utOyvsIISo9PPFNB77CLBBojJoVrY_0U_96g8rNQK2z-Q2He-L7aVAQYoM3Der0FuGGZH3fVRt7N6IIYVmh5TV0KnZBUwfBXt6k8mrhupCN5wryl5wTiMXDDyMu19y2MnS9sQ9MvlzyZFTDeadmNNKTZZycWwpwo3GQ51Uh_xeep0x2TBKj9UAcUw8xvW1ODIFbj6OsFykTVN3mc-xg1ut3BzZ8Yp5wYmUPvDhdZr6OxnrozU3WbCcFhNdGPWQ_RdvHFECZpzR6QdE1djgyYge3NjPMEj-IJIibVu2bQNHMCUqKXUfiZzkgVVBRBiYT_sWwN8hW0lczbSoXVPy_fqhGIoBq8SbpcRgaUj1BEBRpz0boaaEBiROlsCnVhyWDuvO-Wbc8Xiorz60zgymvAooF8VtXVCHtdgIsNoFCrjbG_NOEOXYknTQaIuyoEUiua051EFJXUnzsEYdNzkdj_FKqYfrPZ_e1qzC7gXutFyR4hnTCHFu-C4uF1tOZjZjKHa9Wm0T7gwt9TchtgmDA_1-RlUBxyzBZeNwuepgvs9-n3y8a_xZpcakAbgtjUH5P2LPQtFTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3fec6920.mp4?token=ONeCHlbXmoI4zxYbStqYVlz0Kpm4BTKu8GyOB7B3qYRBOFJZcoTMAqB9dYns2sOSXLtHgWIhFeLQMZQKz2dbdlv5cBhcv83_FmC_utOyvsIISo9PPFNB77CLBBojJoVrY_0U_96g8rNQK2z-Q2He-L7aVAQYoM3Der0FuGGZH3fVRt7N6IIYVmh5TV0KnZBUwfBXt6k8mrhupCN5wryl5wTiMXDDyMu19y2MnS9sQ9MvlzyZFTDeadmNNKTZZycWwpwo3GQ51Uh_xeep0x2TBKj9UAcUw8xvW1ODIFbj6OsFykTVN3mc-xg1ut3BzZ8Yp5wYmUPvDhdZr6OxnrozU3WbCcFhNdGPWQ_RdvHFECZpzR6QdE1djgyYge3NjPMEj-IJIibVu2bQNHMCUqKXUfiZzkgVVBRBiYT_sWwN8hW0lczbSoXVPy_fqhGIoBq8SbpcRgaUj1BEBRpz0boaaEBiROlsCnVhyWDuvO-Wbc8Xiorz60zgymvAooF8VtXVCHtdgIsNoFCrjbG_NOEOXYknTQaIuyoEUiua051EFJXUnzsEYdNzkdj_FKqYfrPZ_e1qzC7gXutFyR4hnTCHFu-C4uF1tOZjZjKHa9Wm0T7gwt9TchtgmDA_1-RlUBxyzBZeNwuepgvs9-n3y8a_xZpcakAbgtjUH5P2LPQtFTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت بر دوش زائران امیرالمومنین(ع) تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448288" target="_blank">📅 14:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448287">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa5a06b43.mp4?token=MD6X-Ph0ENglPcAwRM3XtcDqEbryef1HdXWGUmYKPdRwWpi_cBvhADdKJbDudzP3ADh3zwBSuQbGrQQ_PyL1K3Zv-LdWf2QyU1TWK3F5qCAVPh7sQ1Ueb3DmB-Zwm66dUSmRw_-cOMoO3LtPImxOviFaDIYvYHeBMeYxFimuUVsRAqfCkH3tUe5Ob5nLmljOOKqB4p9EFOeY02ftUSX133sdf_s6zmq1C0t07bDfYhNt49M0zQgdb81bksSH0OCefFDvnXOg3r09jzZf8dfBNheozaMyrAMfAv2oESWTWsI7f_1pEVRAp-CqS5FoNS8iT195XYcgRG8wnASmQ9ZASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa5a06b43.mp4?token=MD6X-Ph0ENglPcAwRM3XtcDqEbryef1HdXWGUmYKPdRwWpi_cBvhADdKJbDudzP3ADh3zwBSuQbGrQQ_PyL1K3Zv-LdWf2QyU1TWK3F5qCAVPh7sQ1Ueb3DmB-Zwm66dUSmRw_-cOMoO3LtPImxOviFaDIYvYHeBMeYxFimuUVsRAqfCkH3tUe5Ob5nLmljOOKqB4p9EFOeY02ftUSX133sdf_s6zmq1C0t07bDfYhNt49M0zQgdb81bksSH0OCefFDvnXOg3r09jzZf8dfBNheozaMyrAMfAv2oESWTWsI7f_1pEVRAp-CqS5FoNS8iT195XYcgRG8wnASmQ9ZASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر رهبر شهید انقلاب به حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448287" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448285">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14423561e8.mp4?token=Gr-lfraBUCiNLKKrHgPi5AD8CtBxxWfDcYi4dOnlm1n3arwDzBor-gyAU2hzGHE8Xe9TtfW04me2QCvIafC_3l_nz4XKrvhweVWlcFxfNY7nAFEyz9y084zXv9mZhdexfFjGjK5cXHZt-mee3xrNehameT3-I1k7CE2j6nLPqioAIigs7qB-pUwpY7ygJQznXLqd2Kg7yUHPtZhqzjv8UpNYNK4HtFCbF4RjFs4y9R4HZgrbqSFbn8qs1ZV_zSpGmXS1gSKDT_dKGh1U0vxASAmgASr2GAwRrCELE5iB65UUm3KQP0IlblfEZZKCv0d8JbRnTCVujJarl8tbTCXcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14423561e8.mp4?token=Gr-lfraBUCiNLKKrHgPi5AD8CtBxxWfDcYi4dOnlm1n3arwDzBor-gyAU2hzGHE8Xe9TtfW04me2QCvIafC_3l_nz4XKrvhweVWlcFxfNY7nAFEyz9y084zXv9mZhdexfFjGjK5cXHZt-mee3xrNehameT3-I1k7CE2j6nLPqioAIigs7qB-pUwpY7ygJQznXLqd2Kg7yUHPtZhqzjv8UpNYNK4HtFCbF4RjFs4y9R4HZgrbqSFbn8qs1ZV_zSpGmXS1gSKDT_dKGh1U0vxASAmgASr2GAwRrCELE5iB65UUm3KQP0IlblfEZZKCv0d8JbRnTCVujJarl8tbTCXcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد شعار هیهات منا الذله در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448285" target="_blank">📅 13:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448283">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb35562f2.mp4?token=DrrYvUzcpFFrnksaW7afBDAZdxiS47dSEDKiyUlfGgpA0MXBGex2GsmFqXgu_ka1Ass_PkpbCWZbIPfFtwCrxHMXMQ4ezETxOibgoJMFnmzGdiPYQ5AuykMbQOb2bHYcHMisqe88_MkYZtWwqALwfuhLZY3DxgD_kpTMKh1Xlik0UVlPbgb1U6Tf21MmGYM2Y3Tf4XxSrZqErYCzDWDesQKu_fDsa0Z0l5SIRMNHzHJ52HCYSuS_v3AAzoZOzu1YzJSDCb3iC-1C_SHJSVusEdXhavcO6R_LMAkdNpv2-7zps-En0exMMhnttZHmfHVjci5m1nkFc0VcsJzXp0aW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb35562f2.mp4?token=DrrYvUzcpFFrnksaW7afBDAZdxiS47dSEDKiyUlfGgpA0MXBGex2GsmFqXgu_ka1Ass_PkpbCWZbIPfFtwCrxHMXMQ4ezETxOibgoJMFnmzGdiPYQ5AuykMbQOb2bHYcHMisqe88_MkYZtWwqALwfuhLZY3DxgD_kpTMKh1Xlik0UVlPbgb1U6Tf21MmGYM2Y3Tf4XxSrZqErYCzDWDesQKu_fDsa0Z0l5SIRMNHzHJ52HCYSuS_v3AAzoZOzu1YzJSDCb3iC-1C_SHJSVusEdXhavcO6R_LMAkdNpv2-7zps-En0exMMhnttZHmfHVjci5m1nkFc0VcsJzXp0aW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللهم انا لا نعلم منه الا خیرا
🔸
لحظاتی از نماز آیت‌الله حکیم بر پیکر رهبر مجاهد و شهید انقلاب اسلامی @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448283" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03fdde108.mp4?token=AUT1Qu-8FbifXbcdRQ11MviANX-kMVXNn7P7NkyaP4W5bpZQeJNC59kumVd7fcYzG2h4k1OXRFQpmN6UijXLJwR2cEKtJ3R5_sv_V836bzdr3fufWb63fiY1EngxbG1R1s0dDi7F96My-ZX7YRocBq9o5ulCp6fGISPCE7ACVGuvHmoNCmpMlmjYbW_OPGAPzLz8AYbnGrQtBQg_-pHg_m9tA0j7czxkxJItd6yX_yLsKYWGVE_SSk5F5x54Ge_dAKQzLtYYnXhWSHff4G2__QuAgqmv1Ub5z0tVgp2DIXPFEmFv5OCigpiZ5gjCBBwUHaovEbrYa5VU8i7UmlW_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03fdde108.mp4?token=AUT1Qu-8FbifXbcdRQ11MviANX-kMVXNn7P7NkyaP4W5bpZQeJNC59kumVd7fcYzG2h4k1OXRFQpmN6UijXLJwR2cEKtJ3R5_sv_V836bzdr3fufWb63fiY1EngxbG1R1s0dDi7F96My-ZX7YRocBq9o5ulCp6fGISPCE7ACVGuvHmoNCmpMlmjYbW_OPGAPzLz8AYbnGrQtBQg_-pHg_m9tA0j7czxkxJItd6yX_yLsKYWGVE_SSk5F5x54Ge_dAKQzLtYYnXhWSHff4G2__QuAgqmv1Ub5z0tVgp2DIXPFEmFv5OCigpiZ5gjCBBwUHaovEbrYa5VU8i7UmlW_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران حرم امام حسین(ع) ساعاتی قبل‌از آغاز تشییع
رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448281" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=XeiVC9egfaDwUwhCaGIlTrFtSOFxtFP2Cv6IJ8GH0-ruYk7xXxA_ykVID4hJNgNgZpKgC22Y9xmb9cRdXOdkW3PvQn3pAzkKJvUD1E_OiVdwqv3hW-7r7HI1NaDuKcGcgoeqBclRY1twuLymZRukSg0UInpv11kW4aoT4gxz37y--GtnjKu6DJdGoLdtkM1rsnsUoNI3RvY7K1FiXIT8K7zH0Ej7EoJOR0ecgTnsGtPo4Ghd0SvjDOrJjKZ4zCv4ATp5quEJqXxJks-ITqouZf4pKCcx-QIE7riha7xxeVriBYJ4QzTmEKzHKhBoCIUz24C2qDkYVifb4qM8xOdQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=XeiVC9egfaDwUwhCaGIlTrFtSOFxtFP2Cv6IJ8GH0-ruYk7xXxA_ykVID4hJNgNgZpKgC22Y9xmb9cRdXOdkW3PvQn3pAzkKJvUD1E_OiVdwqv3hW-7r7HI1NaDuKcGcgoeqBclRY1twuLymZRukSg0UInpv11kW4aoT4gxz37y--GtnjKu6DJdGoLdtkM1rsnsUoNI3RvY7K1FiXIT8K7zH0Ej7EoJOR0ecgTnsGtPo4Ghd0SvjDOrJjKZ4zCv4ATp5quEJqXxJks-ITqouZf4pKCcx-QIE7riha7xxeVriBYJ4QzTmEKzHKhBoCIUz24C2qDkYVifb4qM8xOdQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شروع نماز بر پیکر رهبر شهید توسط آیت‌الله حکیم در حرم مطهر امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448280" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218707fb30.mp4?token=FTHf7604BfY7u_2ri3GazheMB5CWziHIRvlOvZzPu7O6pwdGSooQySHYp7lqLlLqZjXISONg8fTI70kY-nBmeroU43iNKCXRIkowsj38Bl0lf4dXWXJuHFe22eD3A1fwIiR_Qlfk7if24x1UvDp9b5HRVngJY-tsreYxBG5jKwGw1jGaLvcDUMkzCI5EPhwbC3pZtS6CSvtjm8RY06t42hEOgOdFyswD8_zqZ3FxlVYfnBSmk-fGnnaDpWZ5mSKewp7Ek8HcqQmWt3glHvG4a26s7JESoDVo34DGaos1_SLRKkA3dSwcULvECnnXiwdDye-z2l37wVCB6CuDM9zFxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218707fb30.mp4?token=FTHf7604BfY7u_2ri3GazheMB5CWziHIRvlOvZzPu7O6pwdGSooQySHYp7lqLlLqZjXISONg8fTI70kY-nBmeroU43iNKCXRIkowsj38Bl0lf4dXWXJuHFe22eD3A1fwIiR_Qlfk7if24x1UvDp9b5HRVngJY-tsreYxBG5jKwGw1jGaLvcDUMkzCI5EPhwbC3pZtS6CSvtjm8RY06t42hEOgOdFyswD8_zqZ3FxlVYfnBSmk-fGnnaDpWZ5mSKewp7Ek8HcqQmWt3glHvG4a26s7JESoDVo34DGaos1_SLRKkA3dSwcULvECnnXiwdDye-z2l37wVCB6CuDM9zFxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در حرم امیرالمؤمنین برای آخرین زیارت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448279" target="_blank">📅 13:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77adac8641.mp4?token=kFq84Y30fFIfhqJleLGebJHHkte6rArA8Lu5PutCPX_IjMjwS1NkpZMke6CeJT9NLn58igsTvBcFLhqURp4dHTNobbGJnWW-cFZF_jRwyQSsa6el6R85Lyb8mebB643FSGQfZ3oxgCPmHtlRCH4ezKjnNHk2EZbD96F8dRv3fQ7oA0PUQXhlcPYad-iDjTWyE5pF9EtHbnb6-F-dNgz_B71Jmq4KwVB82WedqYWHPoYartsAk8A3ilqfoGgxjY4krYnQAf9PnNmTAyqtLvPjqCNfr0iBLWSi04pfA2wlRaS_5zHRT-ZH77FnxNBH6Dej_mxmQqK07D862DDd1j9-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77adac8641.mp4?token=kFq84Y30fFIfhqJleLGebJHHkte6rArA8Lu5PutCPX_IjMjwS1NkpZMke6CeJT9NLn58igsTvBcFLhqURp4dHTNobbGJnWW-cFZF_jRwyQSsa6el6R85Lyb8mebB643FSGQfZ3oxgCPmHtlRCH4ezKjnNHk2EZbD96F8dRv3fQ7oA0PUQXhlcPYad-iDjTWyE5pF9EtHbnb6-F-dNgz_B71Jmq4KwVB82WedqYWHPoYartsAk8A3ilqfoGgxjY4krYnQAf9PnNmTAyqtLvPjqCNfr0iBLWSi04pfA2wlRaS_5zHRT-ZH77FnxNBH6Dej_mxmQqK07D862DDd1j9-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت سر رهبرمان آقا سیدمجتبی خامنه‌ای ایستاده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448278" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32f5bc389.mp4?token=P5fyrmneAN0573fD-pLZToTR-NnCrTH09x_VZUb2EZh76xKa95iYH_1g0BiuRkH5FzdSEMcpFGSV7q6SaUdAZQvBGgavorf-lgC0cxcClrXmKabqnZR4GNlgTBKU4VzxjX4eljfB1s2ln7ZR297hFJPfkXHH-PiUrlvUC9zMM6eSii0THzGcXdzXw__iIa6-X2O7MlFhXQhJS-JE41Q-6hjxLeOJDCh3asitSdD91PHTr88Xa0-rPDVJHcdW05bUvdAMQowgKAmHK9_ZDA-BKjn5Hw_tPiV8cGqYqt8wTAC6Nq8lMHaZ3DhaZj8FOixJS9Os2BI9uaLP7weyQEb4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32f5bc389.mp4?token=P5fyrmneAN0573fD-pLZToTR-NnCrTH09x_VZUb2EZh76xKa95iYH_1g0BiuRkH5FzdSEMcpFGSV7q6SaUdAZQvBGgavorf-lgC0cxcClrXmKabqnZR4GNlgTBKU4VzxjX4eljfB1s2ln7ZR297hFJPfkXHH-PiUrlvUC9zMM6eSii0THzGcXdzXw__iIa6-X2O7MlFhXQhJS-JE41Q-6hjxLeOJDCh3asitSdD91PHTr88Xa0-rPDVJHcdW05bUvdAMQowgKAmHK9_ZDA-BKjn5Hw_tPiV8cGqYqt8wTAC6Nq8lMHaZ3DhaZj8FOixJS9Os2BI9uaLP7weyQEb4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید به‌روی دستان زائران برای انتقال به جایگاه اقامهٔ نماز در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448277" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448276" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edb7d3fe4.mp4?token=VYfLMmkDuXhgSs52FpGJQCuKCR-vaZST8M3L1aR67c4HRvsdjP--tl6odfSDusqAFQY4sMgorEinG1dyAAcqKJz1QQbceIYPzA-xdX6r8ZfVvhEnGHntJS8FTrm3fUbj6ExHirUOagEC6i_KRfQsinLFUA7FCbn_abkqseJrmNfhDZtq7ZHsXhHYEP9E3jZLDgZkctP-WuGJwRujmuabGBKxMog9V19-CD_PstQyMRn-N9-NdOJVhRLqJldJL6rd6UMT-zcH0i-6YOM1mmVs0SxRP6rCV2HXdLmLI-1xxCh8WxtmzHqwEhorrwhg6ipPW2RVlAC3rhKS1zb_sjyzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edb7d3fe4.mp4?token=VYfLMmkDuXhgSs52FpGJQCuKCR-vaZST8M3L1aR67c4HRvsdjP--tl6odfSDusqAFQY4sMgorEinG1dyAAcqKJz1QQbceIYPzA-xdX6r8ZfVvhEnGHntJS8FTrm3fUbj6ExHirUOagEC6i_KRfQsinLFUA7FCbn_abkqseJrmNfhDZtq7ZHsXhHYEP9E3jZLDgZkctP-WuGJwRujmuabGBKxMog9V19-CD_PstQyMRn-N9-NdOJVhRLqJldJL6rd6UMT-zcH0i-6YOM1mmVs0SxRP6rCV2HXdLmLI-1xxCh8WxtmzHqwEhorrwhg6ipPW2RVlAC3rhKS1zb_sjyzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید به‌روی دستان زائران برای انتقال به جایگاه اقامهٔ نماز در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448274" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=UB6yujeCDPe5WC59EOlAUoPJaVxpeBkq267LN99t6PkuszaYJ6KyGpkA-1773__OoMCfEnjjXUBvUkNX2-nBVjWrBjpSECCAiwNaMJX0vbJBR4VO1DicHRAbKbV5mHuKzoXXaBhR022quqWfsshmuLYcedn4Jzqa7IxdwPg-yhb_WxWj7HG6uOWvStZW75UuYuA3dnovvBRclHSzIaBK35PoCli7vM_NAoIeSF-WLB9uajODaLVAygVuA5SVo4a04HuY6XRfR7Eg4yBRlodaNKeGBCm6H-RwMbD9l8GsYi_D8_E_jS44iuOAPfMrzqpdnBoTU1ZaJJg7nynJIPIaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=UB6yujeCDPe5WC59EOlAUoPJaVxpeBkq267LN99t6PkuszaYJ6KyGpkA-1773__OoMCfEnjjXUBvUkNX2-nBVjWrBjpSECCAiwNaMJX0vbJBR4VO1DicHRAbKbV5mHuKzoXXaBhR022quqWfsshmuLYcedn4Jzqa7IxdwPg-yhb_WxWj7HG6uOWvStZW75UuYuA3dnovvBRclHSzIaBK35PoCli7vM_NAoIeSF-WLB9uajODaLVAygVuA5SVo4a04HuY6XRfR7Eg4yBRlodaNKeGBCm6H-RwMbD9l8GsYi_D8_E_jS44iuOAPfMrzqpdnBoTU1ZaJJg7nynJIPIaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریادهای «لبیک یا حسین(ع)» در حرم امیرالمؤمنین(ع) در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448273" target="_blank">📅 13:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFw0U-UKcKoUqK1Qm2uj4dcth_sj1L7diXlE0FAHy6p72P8Q-gB0RzvWMGPH9gKNPHcsUwklvRTLlH9uCSJrdsUb1jZ2RIJSqdsomGPH14SGHUCHDgw5mBK-LyNQL57VdTOeNAmC50uXfVwP1RX1ikTQ4dgvc-6NJn7lGpCDc3ZvaVslOQIG-7DgJtWmeMCTo_TRYgWLxie4u5Q58INKgC2kF_65Zr4FAKh1o7mYsCQBSQwYfPspLgJ4fOlIcU-cHySyHPUX-ufaLlf8agcW8sUzUmxRQOHGf9sptkdURlrc9iVCQzqUeEBdHrr9rgfIluAWaPAqi-ITE0bvxtUdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت بهینه مصرف انرژی در پارس‌خودرو/ کاهش چشمگیر مصرف آب، برق و گاز در سه‌ماهه نخست سال
پارس‌خودرو با اجرای برنامه‌های مدیریت مصرف و بهینه‌سازی فرآیندهای تولید، موفق شد در سه‌ماهه نخست سال جاری میزان مصرف آب، برق و گاز را به شکل قابل توجهی کاهش دهد  ، اقدامی که در راستای افزایش بهره‌وری، صیانت از منابع ملی و حرکت به سوی تولید پایدار ارزیابی می‌شود
بررسی اطلاعات منتشرشده در سامانه کدال نشان می‌دهد پارس‌خودرو در سه‌ماهه نخست سال جاری، همزمان با مدیریت فرآیندهای تولید و اجرای برنامه‌های بهینه‌سازی، موفق به کاهش مصرف حامل‌های انرژی شده است.
بر اساس این گزارش، مصرف گاز این شرکت در سه‌ماهه نخست سال به حدود یک میلیون و ۸۵۷ هزار مترمکعب رسید که نسبت به مدت مشابه سال گذشته ۱۹ درصد کاهش داشته است.
مشروح خبر را
اينجا
بخوانيد.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448270" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448269" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448267">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384f20b858.mp4?token=Sy_KgWNQoWaKvM1a8VkLmFETtmJ1Hngx1LY-qNDkSqYaXK7InUtFWlAblUte7o9EIRtQwa8o2uv5rbidhPpmGK5IH_jCAguAFhY_s2rl6jlP1JFAfAtSDStIRE2Y0YthEsShGw6YzSlrcy2Xu5qTEb3DxElJvT4g9SzFWHSta2ZXnQHCrFjfFAgJil2vN0OxUc-SlcsGA_edyOaGT1u5BXaum0H8QZRxeABGlqUUiluciT5sh3JyTXdIuZqeYAMMwaggDDw21QGJz_4uqULlCqzStioVaHeAzI_GhltevS-PWMoTMEIdMRBYVKxkAAuq53B5I1cGxJEGNc9wvKOvQEcd-2f40JX5C_snHZAIuBZMxKCzpb4IOhalACRVfWW1RplAyMQTWLc80hui5L40f4bxd63yZOJOMksy9vNKv1E6DVLSlfGxRW8nzLOglxR3s3TkHYAoDCZwkNuBdIiS-qU4RCgrl6QXWZ07BdTowjIkh0lBEbTlHdbtVCM5M80N-DOYFkYIF12-2G3M3UVFgYs6CSO2EYJv_yUDG_A-iPrhxZQwCtJhDbKkgNaXDZlUqfVMrsZaiKvM7mh24-M47mP-KBtbWM8ntVu019uns5xy7OUFkf-eT-TOdNe5qqZCD_Y5OIXEG6rL6MWbzU3ZQDo5-oj74Sg729j-3LK7yuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384f20b858.mp4?token=Sy_KgWNQoWaKvM1a8VkLmFETtmJ1Hngx1LY-qNDkSqYaXK7InUtFWlAblUte7o9EIRtQwa8o2uv5rbidhPpmGK5IH_jCAguAFhY_s2rl6jlP1JFAfAtSDStIRE2Y0YthEsShGw6YzSlrcy2Xu5qTEb3DxElJvT4g9SzFWHSta2ZXnQHCrFjfFAgJil2vN0OxUc-SlcsGA_edyOaGT1u5BXaum0H8QZRxeABGlqUUiluciT5sh3JyTXdIuZqeYAMMwaggDDw21QGJz_4uqULlCqzStioVaHeAzI_GhltevS-PWMoTMEIdMRBYVKxkAAuq53B5I1cGxJEGNc9wvKOvQEcd-2f40JX5C_snHZAIuBZMxKCzpb4IOhalACRVfWW1RplAyMQTWLc80hui5L40f4bxd63yZOJOMksy9vNKv1E6DVLSlfGxRW8nzLOglxR3s3TkHYAoDCZwkNuBdIiS-qU4RCgrl6QXWZ07BdTowjIkh0lBEbTlHdbtVCM5M80N-DOYFkYIF12-2G3M3UVFgYs6CSO2EYJv_yUDG_A-iPrhxZQwCtJhDbKkgNaXDZlUqfVMrsZaiKvM7mh24-M47mP-KBtbWM8ntVu019uns5xy7OUFkf-eT-TOdNe5qqZCD_Y5OIXEG6rL6MWbzU3ZQDo5-oj74Sg729j-3LK7yuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پایان فراق
🔹
مرجع معظم تقلید شیعه حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای زائر حرم امیرالمؤمنین علیه‌السلام شد.   @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448267" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448266">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdXuC8AqY65RJ1V6APGtUHb7h3AoxbXfbrfdcQYK5-1OTN_-OWIpYwhzPbuJsUH5OdvOM9aJ4DeOu9aNwq3vHfqzDleyv9p5ttgn_AdjyCHn6djvp3VzaDISF2me6ZHjcyJRrJjABZOr02qG23Y8ggGPL2hpMhfWiOgZb8boDW3O8F69-2GwJPiosGZ8HydbDrB6nZPr8wquIH4U6pZsgz5_gzML13ApVnk4NK6T2GhK9V-PzPDeCBJrQKQaEmy47HMyGvMZJL09KdA-FpnN4g6-9ZHriI84MkFp-6p83lbTwhH9jyVqU7yUAmGxM2T1R08z5161dWLkv7ds6yQdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ما با قاطعیت بر حقوق خود ایستاده‌ایم
🔹
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی بازتاب‌دهندۀ سیاست خارجی شناخته شده این کشور است: زیر پا گذاشتن قوانین، تحقیر رقبا، ایجاد موانع و فریب‌کاری.
🔹
ایران چنین بازی‌هایی را رد می‌کند. ما با قاطعیت بر حقوق خود ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448266" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRKfoTlLa5RumUZxT0FeVdZ-BJ-7edHjLmfyfMs-BswjmaozlPjSNcTntrFes6ktSqhE7_MDpU-Cc-LtWmNmfPWV_Lp-Mil_tJBWzFXtjMAEK9nktW8TSQ6O1HeQe4T3hf_KvT4c70a4_ri2DE7IT7OUFw-08QFO0zbW-ES2VGVe2eme_2kCtTyD5I0UdQWh_I3nGil2QhHGdHxYlaaMwX4oBSWDEKGXLYWfEOhjebNhcmDc_iUnX2llGqdFdnZdP5L6i-qSzMSGURE9sDj80gaYD0NU5-rlJjaqEc4FWUtowcjXu8yPS_VXXHHDHSMoqsfvxN6D71LIHT9P4fCKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تشییع پیکر رهبر شهید انقلاب در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448264" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_hioUfShc6cNieEgCCW1JKbMI88kBk1v8NyHJwgzOgBxekVn8XhRnKNSjaDrA82G3WdxWyDmZYLdcN6x5488f86-wwjewZr750sU6-5GfVm0o4apVaTWJgLDrGxe_pRr2musDdvDlQypFhASwerrpfPTXHMguC8yqB-T0_g4dacuBL780W0Q-GV4SxB0SJdP8qeFd5858TRO8DsSiRqtWHU95y2D3_qnjSI56194ogCoz_l7_MTtqYHqjuQhKl779Oh2IoEcWFPoHWSdHiiTe3Qsr-faKz71r32Kh7qu41RQ10SdjcKd-ecJTZfvD6QUJDRWZ3S6rAY9DmouXueAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۰ هزار واحدی به ۵ میلیون و ۲۹۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448263" target="_blank">📅 12:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIdLdI5tAiKVzlHWINMDmtTwWSaAni85KOqRRuZ9RyRAze27g-GKrQ-iWrSy7bAfe1SSCmpfs57ZA9-BrbsM-krhGeyMqUIxKt0A-Kd2mx1vrxwvkr21nIKU6Ud8z5FI8Hx3IGLYa17CofYg3C4wKVK2OO7NTp-qf4bWvB2OzYCj1kBMkxxHM0LHRLHhmfK-1ZmpwcTUWPwjwcNVAj6AnkAm9R58teRF7B20svxvNmld7CsWNKq_2uWKeKYNs5h6Lsl6SydAB8svIO3ya2z2agEdgkBu9ahY80CbB1lg8CZ6qtsnNTT7HehtdXQZukn4UOxUoo7WhQflA19O29uifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ آنچه لایق خودش بود را به ایرانیان گفت
🔹
رئیس‌جمهور آمریکا پس از آنکه ارتش این کشور با نقض تفاهم‌نامه، خاک ایران را هدف حملات قرار داد، اظهاراتی توهین‌آمیز علیه ایرانی‌ها مطرح کرد.
🔹
دونالد ترامپ در تازه‌ترین اظهارات توهین‌آمیز و تنش‌زای خود، ایرانی‌ها را «یک مشت آشغال»، «سرطان» و «بی‌عرضه» خواند و مدعی شد ایالات متحده شب گذشته «بیست برابر سخت‌تر از قبل» به ایران حمله کرده است. او همچنین اعلام کرد که یادداشت تفاهم با ایران «مُرده» است.
🔹
ترامپ گفت: «دیشب محکم به ایرانی‌ها زدیم — بیست برابر سخت‌تر از قبل. یک مرضی توی مغزشان هست. آشغال هستند. ازشان متنفرم؛ هیچ‌کس دوستشان ندارد.»
🔹
رئیس‌جمهور آمریکا در بخش دیگری از سخنانش با لحنی تهدیدآمیز افزود: «آنها یک مشت آشغال هستند. اصلاً ازشان خوشم نمی‌آید. وقت زیادی را با آنها تلف کرده‌ایم. بی‌عرضه هستند. بهتر است فقط کار خودمان را بکنیم.»
🔹
ترامپ که مدعی است سال‌ها هدف شماره یک ایران بوده، گفت: «آنها می‌خواهند رهبر آمریکا یعنی من را ترور کنند. من سال‌هاست که هدف شماره یک آنها هستم.»
🔹
وی در ادامه با استفاده از ادبیاتی تهدیدآمیز گفت: «باید سرطان را زود از ریشه درآورد. نظر من این است.»
🔹
در پایان این اظهارات جنجالی، ترامپ به صراحت اعلام کرد که مسیر دیپلماسی با ایران پایان یافته است: «به نظر من، یادداشت تفاهم با ایران دیگر مُرده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448261" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2152e5282d.mp4?token=uk_I6puEsQEcXqZzEBiR0Ru9kz7HMVlXqVHF46cS4bIZbNfGoIf9D2DOxhs5eKGEU0QRQEtExXDGLAxDDxXxdS7Ymck5Q-VJw3Gxo-UnGRS4LDg3cXWfxeoi8k4OrxR_bTDjsU8ctR3Edu6ayQ1OCRrg8CukZX8yKGO7OTf6p_u0S413Uw7tJIV7vYvZNgATA7jLC-aoXFkfwHRhdz-aRxQCdFkr2wIEtcfULbQK2x2bz-OzSIzUFEfRI5DopYgEQjjwRBM5I8BW0mm93j4TgcsKTH-aZsPlteHonBJDUEwse7ycaIvTcoLsHHt8k-UNqfkmbeFJSo0kWuY3PrOTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2152e5282d.mp4?token=uk_I6puEsQEcXqZzEBiR0Ru9kz7HMVlXqVHF46cS4bIZbNfGoIf9D2DOxhs5eKGEU0QRQEtExXDGLAxDDxXxdS7Ymck5Q-VJw3Gxo-UnGRS4LDg3cXWfxeoi8k4OrxR_bTDjsU8ctR3Edu6ayQ1OCRrg8CukZX8yKGO7OTf6p_u0S413Uw7tJIV7vYvZNgATA7jLC-aoXFkfwHRhdz-aRxQCdFkr2wIEtcfULbQK2x2bz-OzSIzUFEfRI5DopYgEQjjwRBM5I8BW0mm93j4TgcsKTH-aZsPlteHonBJDUEwse7ycaIvTcoLsHHt8k-UNqfkmbeFJSo0kWuY3PrOTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس با ایران تمام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/448260" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1UBzRxvixp_J0ae2nTbegUIskaDbPD0MseCo0J8803NW2Kou-41QqP0F8jGU8w1J7q9v8fBl_UYeOwIa4bZoeadETtKlcwtc8-xpnf9pzA6UGaCkmAclEEsrBMICuyz8U0I_bbu1QYMk-kajIxW8-0sATygoxuO18eJBK2t8TyO7s8z3TVTgB9YqApPRpeGYCt_Wtz7ohMrT9dz84Id3bd-fAiGjbUEGcawVzvu1yrKS7h_mfmpbOD3yO9xQP6Qyt3FdBb2pcZlkK-aQkM4qE8PuposRpRsukSZfeeuO0cTBTWJ1KbxBKDFWuDIXdylNsanfKijkc9dNmVSdATF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور فرزندان مرجع عالی‌قدر، آیت‌الله سیستانی، در حرم امیرالمومنین(ع) برای شرکت در مراسم تشییع و اقامه نماز بر پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448259" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941931326b.mp4?token=Lwva1DHRrqdwDz400eJifeFltztdTh5hyeKyLIvB08lzf14y-Zkz-_4rWGSiWC74He7txjEGAelJvuctqwXVbYPQ5IMNwuctVEItn0w2m39658bvjYQweKdJy4t4EFP_3hRkEzFObigd0SwOwQoeCv9ymKIsliirBZXUzv3b2B_MuCmrmaTf1gUusxdQmOfYK0rpHeWhZy2R5PYsNHkAdVsohrdxcwv4jjEIddlk9AmKP0IyfP6eroRLcnbkMU9k0Q9QLxYPBxw81l8z8DIBAaxULp7ubk5Oy0LB0sh17Ig0swgi6dFHUF9a5hH-Nt7sxKnNxKcxOpiqRi7sbnMd86iYxCzQ8Ppvb9aTZKvlskD3VOEKP1EZKbq9dSl2weHYVjGKEY9AnkpG8wnszMT5ejlyOrYrzlJ5-EzM6spubT9i0PkmyPGRLZI4hUCCFsDAbdMhRivAbjllCx8VbHeDwvcb04x0vMNrhV4pRQG-knEhFYlV_wy_EAX7gOoowGowSO2e2MtRnTs7lm6lCFYtRfLlOarXrDPUAgEG-jEO53DBGpR1C8mwI9EdGYhzMQc4YNZRqLeDzfLt-B4mmVceaqEjggC3MfgzTukhW6JlXs5FwS-oLKKohpex-PY-m9VfCZFkoyIiZnvPyC09b56WCodkEmytffqc-hirDp-h4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941931326b.mp4?token=Lwva1DHRrqdwDz400eJifeFltztdTh5hyeKyLIvB08lzf14y-Zkz-_4rWGSiWC74He7txjEGAelJvuctqwXVbYPQ5IMNwuctVEItn0w2m39658bvjYQweKdJy4t4EFP_3hRkEzFObigd0SwOwQoeCv9ymKIsliirBZXUzv3b2B_MuCmrmaTf1gUusxdQmOfYK0rpHeWhZy2R5PYsNHkAdVsohrdxcwv4jjEIddlk9AmKP0IyfP6eroRLcnbkMU9k0Q9QLxYPBxw81l8z8DIBAaxULp7ubk5Oy0LB0sh17Ig0swgi6dFHUF9a5hH-Nt7sxKnNxKcxOpiqRi7sbnMd86iYxCzQ8Ppvb9aTZKvlskD3VOEKP1EZKbq9dSl2weHYVjGKEY9AnkpG8wnszMT5ejlyOrYrzlJ5-EzM6spubT9i0PkmyPGRLZI4hUCCFsDAbdMhRivAbjllCx8VbHeDwvcb04x0vMNrhV4pRQG-knEhFYlV_wy_EAX7gOoowGowSO2e2MtRnTs7lm6lCFYtRfLlOarXrDPUAgEG-jEO53DBGpR1C8mwI9EdGYhzMQc4YNZRqLeDzfLt-B4mmVceaqEjggC3MfgzTukhW6JlXs5FwS-oLKKohpex-PY-m9VfCZFkoyIiZnvPyC09b56WCodkEmytffqc-hirDp-h4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت وارد حرم امیرالمومنین(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448258" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-Fb2IsLSBdf2lKfWf5xmX7-H6ZKVH0SQeWBco-rdBkGFgGVmXtolbBg3aN4rjC3W253y37eh5qIs0tYIcEKQIQkr5QURoB7oFuZby5EKxApXkaNBXSEgtMsd-wql9ck4fLofVqjFDie29tLG4Qas92T0ji2nyULZTAbFtmN7d58_2yaZdll8I5DT6MjbROsJEnGED20S9sNjMLankpjSqmLMQojyyUibtOqe2RGvu7BYtw-nty3tnaLXh2At1zybZXXPyODRg2dxUrtm8dhml1T4gn8wcwp2-16-n3-UiXrlLpSsYuoTv1jywGL2cVL1DnpksmLdtFFsOeOvAyHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKHC6zbPWWD_Ps96WuD5f_nlhJW9cPK2EtjbHvyUcBaeGZw2zcvjZBT-6Jb8aHeSXhIuizEww8Fse_2hEvoQQdcv3FCxokgct65m-Z7hMtpepv52lgMjFGXtKolU2VdgzzVKclyqTc3m1SZrr6hnQmlh59Q4Kfh2yF92PdLwbHp3KXEMCj5l4EqskQrhlnjLjcZauVFTcrx03BmFhP8mc_7kd-M5ROC2gCstWbVSEDVHlmgtZn-MA2PCCHe7l-OlqY2_IpYqmP6J8MKUwhXbOOCRN2lSEGBdrRc7hLhrJQ3zqOp5jcKk_Q03cU3658r7lxlSw3giw4_V9nsOvIkfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RapszbVn6tn-qjzuoGVujQo5OY4lI9HwkLzj2TrAZNEMbg5s5DW5fawNAgYV-t-z6LybtqHqwMXEgHAECsJYc4wNI4q7y7h-cXZ-Y1rPa3pNnqpNATLyHbQuKYvoLatk338EJQh0gFnTwbiqJKibait9kb2WBGCN1D1CbFtLx1YJS5YKueOIzSYGrBnZuhJAZ2EnnJDDEuBnQWsm4P4XseP7vRP1xEXJszb38-AfoxgY4PipvCMRFY0stoFE3hWeByEA6hz41t82YwKTzvdzA1qeXVumKOYKF6izPnzJjxhNMR4upGZU7Ep9hOiy87cpsTLcaaeS-28o-YwR4w6Mpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
🔹
سخنگوی سپاه پاسداران انقلاب اسلامی: در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448255" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lir8zXa1SD6GOXOAqnpBRj52S4sbp_3nv8C4h6i27kqRjxkSnNnHvuZmQJfWpRTftWYEoDealTo20DTgt0JC59j4xefP5miqEvzqSYL0EvEK9XovlrETxd4XLoz1S6eoRnJA_UfAASStNL-LhZxBoc8PjxybxI87YK6Ku8tjhFGtxV7-c1jE3_-wyp2VqLZqvCoq0iU7snto-TFeUz3DfbR4jZWApLe8QT6b2WLJSkoExM18FI_GO5PHE62BO57AXLJSlbGBhjDsVP_MPQ1-OGJxuBTHPUSWKv0fxo9LIJJX0-YZatct0A_qdrMhdmkOpKgNeLxMkdTgwhQ8gzp7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عراق، وداع با رهبر شهید را روی تمبر پستی ماندگار کرد
🔹
وزیر ارتباطات عراق مصطفی سند از انتشار یک تمبر ویژه برای ماندگار کردن مراسم تاریخی و باشکوه تشییع پیکر رهبر شهید انقلاب اسلامی ایران خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448254" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c7638b76.mp4?token=X2l99Sc5RKHaB8PT-ARg2v1ueCaM3BsCIxmaabeeYCv_cigBCOvLmIpT2DTbp8u3AUhkQIDsgumbgotPnxjmowJU4KhZ94z1vyHqd8tqFm6Q9nwMpyRsfQYHaTEpObegGti1Z99OPtUWuZ0KYLRmfLgLIQxknr6nItyv6xvmIzOqY57Q9444N6b3zv0QT_5SM_5r-ToSGHJOT_Yp5KfgEr0gQQd6yNt7iP8lSsnsaqN-eqBSPxwp3YbPhBVWubQLowPWpdSNgZfuZFrdSav06rJrdyyfy9zF716gok7qGM1a_7dVDqLY33E659gsodxaMnPGbSPVCzFw5lLqJZ4ocCqOrvGF3VVulszNfBdkffH0HplnWQEQpsHK4TqH3Nm7kpd8W_8gPKRbrw3GVEhhB9kRqLofAPIOiKtd45P_eLZ38yUIi4UL94PGPBephVqttpig4Nq-bf_IZjf7JT61tJYP3UJXdLCYaBPzbtmWaIsZWcxRmEszHtxauoxgsMP-kzmfGjAeCFhonsMIYxOK_BKaiQv-uAMh9iPgShXK5sjNTIQRbLaXA6ZO600_3Q8l0Nl-DfJ5QgAirW2OMl-p6_Fxc0o7jWR3ZfxVUMasXsYKkmwTz1fBRxUtB1_6Y3efcNxmBvV5V-0GJ8UY2w_8xqYYygmaijYUcH9zv66RCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c7638b76.mp4?token=X2l99Sc5RKHaB8PT-ARg2v1ueCaM3BsCIxmaabeeYCv_cigBCOvLmIpT2DTbp8u3AUhkQIDsgumbgotPnxjmowJU4KhZ94z1vyHqd8tqFm6Q9nwMpyRsfQYHaTEpObegGti1Z99OPtUWuZ0KYLRmfLgLIQxknr6nItyv6xvmIzOqY57Q9444N6b3zv0QT_5SM_5r-ToSGHJOT_Yp5KfgEr0gQQd6yNt7iP8lSsnsaqN-eqBSPxwp3YbPhBVWubQLowPWpdSNgZfuZFrdSav06rJrdyyfy9zF716gok7qGM1a_7dVDqLY33E659gsodxaMnPGbSPVCzFw5lLqJZ4ocCqOrvGF3VVulszNfBdkffH0HplnWQEQpsHK4TqH3Nm7kpd8W_8gPKRbrw3GVEhhB9kRqLofAPIOiKtd45P_eLZ38yUIi4UL94PGPBephVqttpig4Nq-bf_IZjf7JT61tJYP3UJXdLCYaBPzbtmWaIsZWcxRmEszHtxauoxgsMP-kzmfGjAeCFhonsMIYxOK_BKaiQv-uAMh9iPgShXK5sjNTIQRbLaXA6ZO600_3Q8l0Nl-DfJ5QgAirW2OMl-p6_Fxc0o7jWR3ZfxVUMasXsYKkmwTz1fBRxUtB1_6Y3efcNxmBvV5V-0GJ8UY2w_8xqYYygmaijYUcH9zv66RCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید در نزدیکی وادی‌السلام و حرم حضرت امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448252" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=tCpUQs-N5E7KT1CW3VXr-uZWHcE5kGH9bNygpmcl2BQjlVxLWaMmrjVGOyOPCw3HqFcQHht7B6vreaN0PYaFTfTve0YUuQQfhc544A6ehVaGujP_BrmK3gdQ3MgGZrMNUc4vQaguUqU1cyzHJY099GH2-E8Bb0rY-EDnqAE-laNV4IBnyLVm2h5Tvq_yUjqnv2GSHftXCPUiRdiDQe5jNdBV6EzIIVcxUrPphhd3gW7UbXdaN2NOYMcfrpfbEmmtIpH1kTLyzooCUTct6wYvBdCggIw-YJzA4STxuYekfa33dILXfmsGKy_yXwzgl7Ptq7dl4jQ6RSb_skqJnvn2Bl2Cnnthpb-l35zY1ZDA1KXTKw-Uiy3WI4sM8EEP1Z_0V0Ac-iL2f8VX31dI3Le4CbyhdD5Ko-qhR3cAyPGSxLmHqGeuXTWPKoPamSDh3qH_84-7ISTgDxym4RifCgIzxyTJYsjxs3kUyM9u7jE-CSRRVJlZMMZ9zYvDXgQc_ObnQvrvE4rS9X4P38W09FUDNKpSLKAs1M-l3zSLWMdtS89dBrUY97wvQ7yQXW847mPc1REFlb7LxauuVe7I9Ay-aIhr92C4uJ4Sc-Uf9mKieFklvfLKwap_bh8pZALQ8l71l7DZM8C3Fn6vqSnkfg429KG0PtEbevI18J8_cvxqoss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=tCpUQs-N5E7KT1CW3VXr-uZWHcE5kGH9bNygpmcl2BQjlVxLWaMmrjVGOyOPCw3HqFcQHht7B6vreaN0PYaFTfTve0YUuQQfhc544A6ehVaGujP_BrmK3gdQ3MgGZrMNUc4vQaguUqU1cyzHJY099GH2-E8Bb0rY-EDnqAE-laNV4IBnyLVm2h5Tvq_yUjqnv2GSHftXCPUiRdiDQe5jNdBV6EzIIVcxUrPphhd3gW7UbXdaN2NOYMcfrpfbEmmtIpH1kTLyzooCUTct6wYvBdCggIw-YJzA4STxuYekfa33dILXfmsGKy_yXwzgl7Ptq7dl4jQ6RSb_skqJnvn2Bl2Cnnthpb-l35zY1ZDA1KXTKw-Uiy3WI4sM8EEP1Z_0V0Ac-iL2f8VX31dI3Le4CbyhdD5Ko-qhR3cAyPGSxLmHqGeuXTWPKoPamSDh3qH_84-7ISTgDxym4RifCgIzxyTJYsjxs3kUyM9u7jE-CSRRVJlZMMZ9zYvDXgQc_ObnQvrvE4rS9X4P38W09FUDNKpSLKAs1M-l3zSLWMdtS89dBrUY97wvQ7yQXW847mPc1REFlb7LxauuVe7I9Ay-aIhr92C4uJ4Sc-Uf9mKieFklvfLKwap_bh8pZALQ8l71l7DZM8C3Fn6vqSnkfg429KG0PtEbevI18J8_cvxqoss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید در نزدیکی وادی‌السلام و حرم حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448251" target="_blank">📅 11:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4d5e4c30.mp4?token=Z8d3JlFozLV_xVljpyJcGaJsoq0xqJSAMBK7lykOY6h_CGPUsrPrgfLi8F0R8HSC0QLXiwPVc8hrPsUCiEWe7J7dFwLiLhZdU0xwePWDOKNMTYVNZXp2ma2qh8CtXGNNNnu7t_PfqM5IPtDRvx1pA_IH0NvbBeTPu2pXI6Opin9rgVEeEfdfQzjcu5kXHKOs6aRfcm_vCulWlFiMIzcFzX5mPuHlbyjnzOlzA-jcrf0O_5sXZHlQvuCtUXZq71IhNLyqSjhHAIbWanQhDk9_vZLBQGNwUhldbE2-2w17xQ7R2GmcqwBc9fQAcloOjQOIKcHd4waGUAHxOo21QseF2hXkZqULHxi_qRbOgd5-Grnt1LNHRH99WH3zc1utUwLtn2EJdYdQiS8yq2llUgzLuVp40spHXn9spxlm9YWwZFozRmiDbcNqkfryTK4qAdtpqAubjr0Ap9esgoqqLZ8BEuSCr_GrMh9jk5tjnlHiDY7YzODcmUjqCIxxTvxVwQ2OTIbnLV7KTZmRoMfktopmmA_Z8mOqn_fsPCsrZAcF4krSrO02ji4nJaJuCLLGdUXO47SsMcPKJ7dssceLx18KszYwY6cKM5p07eP7I0Q104cy9potLcKp8bjEUl6Xt1rgysYr1PFlWFrAN-z-z7lDgESaFh4JvaXa2NnEkBAVNu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4d5e4c30.mp4?token=Z8d3JlFozLV_xVljpyJcGaJsoq0xqJSAMBK7lykOY6h_CGPUsrPrgfLi8F0R8HSC0QLXiwPVc8hrPsUCiEWe7J7dFwLiLhZdU0xwePWDOKNMTYVNZXp2ma2qh8CtXGNNNnu7t_PfqM5IPtDRvx1pA_IH0NvbBeTPu2pXI6Opin9rgVEeEfdfQzjcu5kXHKOs6aRfcm_vCulWlFiMIzcFzX5mPuHlbyjnzOlzA-jcrf0O_5sXZHlQvuCtUXZq71IhNLyqSjhHAIbWanQhDk9_vZLBQGNwUhldbE2-2w17xQ7R2GmcqwBc9fQAcloOjQOIKcHd4waGUAHxOo21QseF2hXkZqULHxi_qRbOgd5-Grnt1LNHRH99WH3zc1utUwLtn2EJdYdQiS8yq2llUgzLuVp40spHXn9spxlm9YWwZFozRmiDbcNqkfryTK4qAdtpqAubjr0Ap9esgoqqLZ8BEuSCr_GrMh9jk5tjnlHiDY7YzODcmUjqCIxxTvxVwQ2OTIbnLV7KTZmRoMfktopmmA_Z8mOqn_fsPCsrZAcF4krSrO02ji4nJaJuCLLGdUXO47SsMcPKJ7dssceLx18KszYwY6cKM5p07eP7I0Q104cy9potLcKp8bjEUl6Xt1rgysYr1PFlWFrAN-z-z7lDgESaFh4JvaXa2NnEkBAVNu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت میان سیل عراقی‌ها تشییع می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448249" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448245" target="_blank">📅 11:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ ۲ مقر نظامی در بوشهر مورد حملهٔ دشمن قرار گرفت
🔹
معاون امنیتی استاندار بوشهر: بامداد امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند.
🔹
تاکنون گزارشی از شهادت و یا مجروحیت بر اثر…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448244" target="_blank">📅 11:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGLswwzln4f8MVZdnxpShc0LWfNT6qRIw3ZwrwL_hGxKhcCOWWQU_tEFq_-9zztttQdxgaxlNvF1PDm_YHtC7e_yTSGQk8a9gW3zPRw8882qRp2cIpv7qI9ly3Y306RoxTTiFLbEhqLiHEaT0A5L42VbUqExNtWypp9YxP4xhPPD62YT6maEAWOB7Vqa9aaoRxFtBiRDq_v9fvXJcCSwvFFQ7cBZXsuzMC0uLhC4aHUsKs-3pwdP8eolHa8FruqrltzSHlJ9LiT05jQX8opMuuKiwyvTLkRXb1S5BK3E6W9ulvshktljuizTPNdylY3eOUIVJERPE5UN8YamM-ypSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قاب ماندگار از تشییع باشکوه پیکر مطهر امام مجاهد شهید در نجف
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448243" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cab6ff92.mp4?token=DGKo_X1r2JoXAJxn-4ZmtQ-9zTRkqakWxiBAyaGSaiOlpK6I1YtKOlcvnfqQeMU1JLRLXE91zkukN5O8OMSscqmiG6b7QSQBtfeSJ3PZmHs8Gz69f_x5-wqtW1Bbxpu-FmxBab_1jArRxTswlAEePnuS-OI1Ptxg3blF_3VLXtIkDILPzFDEi5hHFpZZ9AQ2IPf-ey87-HpKjMG_m65vFSAt72-D2jTqrAEs7omNQzQBc1bXeqPSlUmWlir_9XByE8AWPI7TUpa1zRA8wK0x6NWyFygLk2rXZDNE3X2tzRLl6gAjmDT3cfHFF5BiF_vtOJhKH1WD-RpdE0DrpgVFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cab6ff92.mp4?token=DGKo_X1r2JoXAJxn-4ZmtQ-9zTRkqakWxiBAyaGSaiOlpK6I1YtKOlcvnfqQeMU1JLRLXE91zkukN5O8OMSscqmiG6b7QSQBtfeSJ3PZmHs8Gz69f_x5-wqtW1Bbxpu-FmxBab_1jArRxTswlAEePnuS-OI1Ptxg3blF_3VLXtIkDILPzFDEi5hHFpZZ9AQ2IPf-ey87-HpKjMG_m65vFSAt72-D2jTqrAEs7omNQzQBc1bXeqPSlUmWlir_9XByE8AWPI7TUpa1zRA8wK0x6NWyFygLk2rXZDNE3X2tzRLl6gAjmDT3cfHFF5BiF_vtOJhKH1WD-RpdE0DrpgVFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
| شهید زهرا حدادعادل، همسر رهبر معظم انقلاب:
من سال‌هاست که آرزوی زیارت امام حسین(ع) را دارم
▪️
امروز کربلا میزبان امام شهید و شهدای خانواده ایشان است.
@rahabri_plus</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448242" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJD50gdhk3MwA7vupgWYjkxWN5WKGFb29netAxsQrex69BtQv0G5pkpxyt5qxcZbw6oq6Y1WHvZXRIXGjWwW_1kzkF1ITDHgxb1E0y6KfKoSY2Dlay5Ntp44uIwyNC3_uc_DbHvLbHV452mM1to6CL_I5YeJCA0SPPXYHMrJyzOtISh_kXYvsDlnKuES4M4PeDwyhTmzVKbnufuT1cSayTSw_wpPfRf2eVSBM8LKTiyV9OFgf7lZRyGqlGMjuddTRIZLce3Vyi_n7UQbKWg-fYxYS9NFR4CbtJjEUWowAZLNzILEX9AwOQdIAbwxPLLqtLNx_RWQ3Arb3G6_KNknmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس نوهٔ رهبر شهید انقلاب بر دستان عزاداران عراقی
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448241" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
