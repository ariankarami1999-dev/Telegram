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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 179K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 22:06:34</div>
<hr>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw2GjmN0gou1ASIvJInDjHrB5Kl4h1rXlbcK0poW35msQQA0EpJw9rBXcf8lpCMChYByPQ7aYN70cKTICeo_zc8jW-4AkqWmOP6xSRQomJqseycKDtuKubMqNx1kgSe3XF1YQGwn9GATv5aLw4xIuFL0dnJejylZIB0yCw-eJWk_vh3XgcZraXve-7g2QQYwc_zbfsIwQ9B5EJOQutc0bDdJo5bXB-HoQqDKZfkUexkyCJ5SYUptdBNsvwi6LzlChtif8XdicVg7ky_4J3K_cCxEk1gQEyR9MX4Z3HTGKeKSN6pABjqBuUi19KQvd94VRJRMVydbU2ZsQzr75bSAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnDIProYWn4nFNFP_jByLxOfSyNQLVwbDgsGwmMJEW9m8TDrOKuO7Pc2_Sw7pkPnRIyJ1v3T-jyFBVpoI_cTSVVSCW2VquxkqbDRvP5vDc6mW1gc53voos0fWafpEZnx5y17CIYJSUin9yHO97VpxywCJo7ib3cVISxHVMtpGBWKEXSW1AlWaur2hrMqGC3he4XJr469MbXu5XUM4o9FwkBBZvlE-mVaIu9t-dTUVX07GAehOPMBIWXuUrGGEsJUFhNH0kzl-So-ek0gvOeOGisLPNlrz9pXVUvgPhuz2tNRqlA1L7Cx-t2ye6FKxZUZ5fMUz84n2aTYY9MUIG6hMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnis9gXjq62ixFYn9xPoEDr7BqcF63LWynyzSjbXjRYZEEYchJW_HNGP9EouqR3MRLGsH9wRcUXCIxE9j6mkaLyHghHu1hJx-1CWAMDgeQzWYtIgOZg1kW_K2FHhq98BKV7X-U0KSCt_2-0f0xcHfkwRSpKAhlFCebsfZRGGOFOLrVvX_aqrgiWLFXl-hpE4ryGrXWtSrBu4un_-ua9POpqA4CQoIhEwCucYl12E1ul6MgGg8XzFoRRTm0w-TckcE17G4qw-kmRb6Cmhk88X7nVkKxq9xMGU0ZOZfu_uF6frCINtFREJ8NGR4uULfcUpKbUrxidawFJcFgIsxvZkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=ayWr8ai4KHiZ50f8ETEZeiGYNYmRQfGTM78pK3bJO84lUL-HSIwqsQtRaYyfehR_KL5aaxkPkBcC5nZVkL3M8q-0DH4SFGoPrqUG2Ae5n-OMmUfafox-Q5QToGk0zQoHfcgAmtfZed_BoJltXNzXEKEPLc9Nhyp5qHQIJTvPtIhjVTW0bZDrVtN3chfpZ52_EUjlPAaWXQFjulodsY9n0_zIeA3jm0zCXLSXZF1ZgX_vu2lREqCRMxkxFCYCxAhivXjXFmYWEr5hme4fsQ_UkqO1cb1mrCf3L_jYUrEhbffbSwYCIWwZdUXAIOjr4zR6oK--sn-oso8NB8dKJPYnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyGrXfNkUvyEg_rMLXIvMo7Ss4F7lshzepUYiz7WevBr3lQpxAl5hnQ-_3LS0gwKQ0BXD3q2vsasXyD7GL4JCjn1j4o6pKJoUohs4zP599VfYqvFyhMYOwS4JordIa0NuePIqRDC4NqmwiHXY489UE0Hpfm2fIm_FpYMJMH2Nvr9G4rAO-tCFvfqbwmCZyAHA79A45CCWuHXovlXs9wvejOT154Es2A2lGRj0f0wm2ao1QhIVUoSpma7P5vdwghGuo0SM2N10xaaz82_QS9-8iTnaXESjGGG14tdpLx_q5GzENEp1zdyeH-03LK-6WzUD38q60tko9HezqTh6s67SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPpvilauJpHtqvc2IQrKj6sWBzdgk_XwaMGRHArbLTGiw6MOCckdP-1LzDfL-oHXDDvxa1vJnXqbB_bw4YaojWVB1Ci6DBgl6Q74qfDFU0avqavIX19MPFOBxWJpTHl0hFJ6HMXF6XWCJ0Ahf8v6HjJee8ZqfRJqp1dVEPSe0nLKJ3dfm6ZlEB6U9BSMWihv89VyC5O87WyQVPGWsDaFYPRkZJIBBtcBsKem7UhQ9LfgYU1SrB7NMRljGb4LHytU9SSea11f2GI8NOilMpkXxd8cHxA8KtUgUieFvOiqh0Qt8XmkdhOBstszcYUtqnaJu8uKimJbHQeoBL0QAXOQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز بواریز
۵۰۰هزارتومان بهت میده.
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g9
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22489" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAj_yVlkhat0AjL7u5ERNx_UPtEjxf3tOx2CP7QRIikMVu0-wQTw8k57RrrsfWocYpvYmNVlNAXvuXb8Z922fdxKrePS7uutTQYqBSdnrIqy1nJ33ilmxuSBNm2S5s4IBwSHkS7rlF-iqijGmrfGBLU4Tn6PPIgxa7nR5CPZQYDJczz-JfHQETKT_t5zQHLT1uFUp_NZNV2jsXnI_SySu4CRz0RzTUgaLxK7o8FTuLcZSybWmu9gRrwrS0e6gftmosXGc5eu2eGVYxHZXijoO8H16C4f_G-uFFiX-iM6NPrAoL9bpZleX2HZsrf9_Z18YWKAmZJ-I4z0pKNKGkHIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4_0gv3ZHLoQ4zmVDyoBsibeTnVmDrQSkXloj_PbwML00isB2UGLpWU2cTKFMqiVGtKf7I_vcKrgd8zioN7jAeEHYDbVNVRRnfqXQL-oWvJ9QU0oSQUbAO4gk43bdhq5TBH5ujD97oD6wofBtb01kJtlK2PbT9UiPDZ8WVymDYFjJXaZvDV9igJLkfpCi-FtsdIXp6Ey8FiXGXOqH3gqXRdaLFNInLrAacv6jwmbwX4k5jDhzKpJ2_AgJvmLCrhJrANKGuNa8QSYGA8oQ5rL7Qzy1R4pgiSIb73qhLNhnMcf0hxZSvRjCIODS1ujidEmp8xNSFGHCqSLDfGlnolyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GgJGt--H982H2SB2Xpjh-Z3zwBpa5oM9NHYLhZSmupwDPuix5lMPG814AN9d09BAYO82KWzABYCt3R3r1bMG3ay4cRkTYAUgchQGBHNhjbsVy6oBSvJPo3ybURtU-o86v3fmci64mANXSkZOXGSMnC0mYa9dWZYJvPSsF6fV832GMpyQ5cY-QYKYG3BfpRajoY9y8g4NEEQySfUtAM3UH3J0jmiCv70xKRPgN5tg_umvT3I29xfI46vgO2W326SDuJ9qEAkjhps1Em1M-h49SAu9to0LLfgyUyyfXRe_DnbWHJ76IdP7Z0wMPsybPvETi6nboePbj21PNieOb4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATWwUcNBah5L6F9Ui5qiLrdhFbmFiFEaQlJl0_eYiuZUvLEcqXPC-q56amIBneYIkhoydTBrAfd_2mzrge-6Rw4owUyZS_x6z3dZU1Y19IdhxD7JOxujUFP55lJK71UOGlpWhhnjSr9JhJBfhOyOjohP_4QPyNSs7SFsMUUfJPxOIWmEEsb-b5xylkLeGjEvTvc3gKNRpafho3WsPh_fODfFd5QnK2VxvnKGuX9Wuoy1KCwoML0RSFt3EDLo0onz7M5CeqFL3KhJbQ2hXsszXbK4U2PlIGvD1g0brqlwCVqDUjqpmFLxXFEJWi3N6TDFp_fpIK2PvKZLNcSaQBI5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvGjygDAp4449rJEQW5fI8nqGJvMzSu6Zwa3okYa7VPaqFaNnUxOoFZCs1VwHlxAQiY2uaikTV_j4swllpbkKemU8ceFMVEZLNnxKfBCHjn1ruXzFbyLshXNISdnX2X-dOFRvMP_NjOlyFjcKj51cWGQGHuNbPeiJXzFP-HUXvKwd2jBR-sgzQu8U0D_CSoISnOPTPE9UxL0N8vN333woyxK7qcmx3UDgtlfb_peg_VkZe96KDJPeiIUNnNV1yGaGsicn4a7ZXCURx_HR7UmhGOH_GbA27Cla8nMWoktJeTMf9kcUzgFV4ZKID5Y4KQdILjNLoSNJTX2eJAsnbK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=TVrK46o9JczB8i2CXvAQxCJXwQU1MRayrmCBKDv6PTtyIDzLnxP7tzo5UI6tfY96TA8UgF6NVFysiDf7j1f-TumNvuWn7ad3ISB7m80EmT6NWjU2mfn2LGeld40OgLwckrgbCN1U-EzDi2WuoRVmoLJq1eues5ZXopd6elsGM3uXLNfxBMewYWBkdnKmYTWSxl5jJc8ZzZu-abSHDlxMTj2VH9gLiUh4NuoioT9UI0gvfLXc4l78yvUtCyd3MgiWw1SDMj64LBxLL-l8slpHAioWEv4ivULZT0IoX6DZhgwVPS7B94DDqCVP3C8abLK_OMt1YoPRaGWRIpxiY_UVbphO3UQcMZRBvhanELAH6ELuMyqxBo2srRF-J4gYpPORsbH4se5RJwUsWzjHh4LDHjMKKD3NehPN4wPpCCLArrmsJRYrBJ9wXqLnvKqEEZpKWbPSGiohRUa8Y1B05KH1qe4V9FTvwUN7rvLhglbBnpfhRaOAQRdJkm2z5gPyTLGihCTejdn3PNYuMIakUVb-OUS3z3jLhOBE9yshGz23BvVi3IOECRuo2W4v7mizrp5WHB094AlVPog3vzAYiG4usO6EfXC35Xbz9iam4LRG-TB88h5p-GOpvHa_Qk89zG4EphGum5T8VPqOxVE8vkvsf35R-OTAkAVyvvd6MT3K9MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDXDNySxefPQf5ya4bJWPWltq_6fBrG1dz9ugCEux-9Llr7ZGNHgROD3xGc5uuNNcc-ufoeJC1R66ntajX_efL7RVqsGyVVhNxePWwLgjS8KnQ6CR112ogI8mYwI1hY9MeoD6bUu8p2_hzYwN-14Z-JzKhIpux1DbWcq7P6gqYNsnWZMIH9F_obRJ78piv62LlOSqA-ZQmiTdpJZl1Qa-MMdEFKft7IAqPpie-YmgZ60pIxiPnI8T_2xeRZT_oCSQ7NapfEDo7h27pIQlgLHKNg3DbavtTcM0zKkJqM_MfxT1-pNsIAZREsDn4daEal_3GBi_B2Y1VzwvUVyB33m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4wiCrvO4MB_h-u25CsXKYKTtpah5zo59BdJrYlfv6gaOgVXJx6LSwZvoUGL9AwpZAs4poS4ZoeUfzHhC2j8a4unGZnj05FnUVN64I21fcNKl6hLoL0r0a3z1UW6zvsNyT9TVxdvKUQ6IyWJ7kqC0MEH4jMrL4ex7XtaF2vKiSUelmW84SbrT0nKQ9eordXYtdLhyX2QQOFt5tgGRbxQgpQrgxL61sO6rd0XWtyZkurdlNB53lAn90R14E41WvliZg7KP48o2hSqLKVG4ak8xQiqBKwHH9I-LywLWSiVfRwpWo41nZUn9-J7uD1TxnzPlkCz7qGMhTREu0P9b5r8AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyVZ3brrj52Fkr6XAXJ2QPB5J6jZh6vtgWN_ctMidwtt_z6FdIbe9cEsXzVDhJ8oM5YydOhNJPO5BHYV0k9mODZEyGK-Mfs66tmGH8RtFKLyEDFXL8PlvoXDqQpH-UTBoKBxzjS4h_S4Pg_Y59s0M18TlnoRLTRfgoyVdOyyNxIb7hpigVS347jLOjaB4Xgjqw5A7-sC6fYeTnWCLh45gUgKB7ih4pxPgrmk4TmUcSe5T2uURzyQMGWdc_XbiRG2Qc1yK9CxQCwIMo3XrPKEC9CJ3u9CZ5Pl9ka8wuwu57Crn3cSIpOFTmwvQdvn0ZU1ckkJtQHDhcn2uqrjwJiq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4TMCG43B5R0YD_9dHWkWZg1KO5v8O4OZlqIELYgUSiL9fawZh8snx23KcmRjguEb66mBvECB4TS_Nd3uOaWzaxNj4TJ2KRp5sWopEikcwOLHI-AlZ_8R8q6ZCCm1rWpQWpwqohggVCMuKhk19lH1TIOF6oNOkd4yN8jO-QgEf5RLhPPS00QTVqtbOtG4SdIQuCX2oKrzaJ98DoeDiE47Sd2yV-V82p8O1oY7lRWL0BkZbVLV7LVsd3OIsaw1c3ngnZUSRMYa9_E2AfrgCQX9w7T5YJ2K9vYUJhtt4n8W-pVeT7p-CvbtWwOI_Fqzff2IXr-6Fd1X0Dg_Kdqsa-6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJVR_vfoQhIoBLxY1_eveHIpEY6sXvLdSR8BD5NVPeSzysG23DB3mFxrK5q5bkVnK3U2i306627470zcN0pp8KGD6dS3Wm47orKHgu20nYt2-8QzqTa8l3vH1fWe4Y-WZ8ltThXVuEP4EBJk8lhOYus9R4yMLqzFuUOfOccmZVSaLKWnIhuG-u4aWVhTyCZ-7RopIWQn0cbGAfoTIYCK6eK-rigw1ZGtfoi5Kulf2q3cBlcQWp9LFmvQmwC2-JDDEkkzwXlh06TJ_aMRVmzrI8pXctWov5ohQtddB-2AGvwQNolY9yxeJK7fdDQqhGK3r_CzZ_-XeBJa6IIzfIzTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSslHzcbieHFbFtlXl71d4buDT91D092MQ5XAiKQmmuDfr3pUwFNodyLyFBfsrZaXd-QUbeV85x3ra3r2m589Dx3zr5IZPFzvdiR9yhueOAD-yYwD26hy2tGxxC1yQ0N1aaWPgfPBOCkG_A-3u0FdlsrWFnjfAXZRrO6LcJUjKaFZpuTBjEBF5NllZ-j-RrBisyup4ubWeWnD858FX4Swg1u27yQMc_l3Bw1aclMR6dYr8_NnnFWacSwnBJt2GUH945Ln0w_nSRZFbseJNnL_9za7qU4-40Y828CcJ-yx6swcWuxy_WQ3RZh6SPaDomemfn_9cvLkCVpg0bQ5hjerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijVv00mylK8iYRIaX7RkenWeDr5Y88yW5y5ylGtHjLThJC64G8SpY35_K1WzL4KoGsKKODMkBRJqW0E5wS4ToXOdNsV6rwNzNqbJMrLw6U9uMtNmGP1DEM0yaGUiyxuaAi9tPROXsCOBVVhFkQlkLleEza1ArtDf-fGeej3E9kTZt0rF1PYI8v0vBZ-Y1Kt6Y-gb6Cj4z4oM6i_suOBd6XGyOZFIOu35X8VM6mar0QL8Em3xa41ki8KFEFjfM5xGDcZnSfF1hrRha2uiNkJIO17exav_WHqYXw2vC1oqaxwVijwkQ54x3zaJltaUDs-m4k5UblYL9-lSsUsphy66Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC4apT-vrqRyxTPlQAj2Xb5o1KdCZeYaE_ZKxpMmhR9GcAaZJvQyvAgck8oaNyy8O0pYqGZpVqLmUoRw5j4rx9XKOe0EgF76fTTXHZb2AMeW9XFKCKZo41o56D-fQWm8yb5pNpMRdFgX75BXzSebOeUBv-fNZv7y6NSH7tYVdWaHqL0R2rQjMcAWkjIHclAep2-Z78zQKzUwC4rO762xiXfipu1kVxx9ywIDRa_jGud89PQ8nTRmhUXlCVotviVQyh51LH-OXz3PeMrRFfMcTg_ZCBdd39ZbtgKryMBzA1igMu80ZoCyP0VptVjnFNVjsAdhY5u-yEW7VSOYSjPjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_8YEVUzBRLwiezOaN7W35LhybP-eNrveihQ7Y1ns_4IIPhWN87J3t7Td51h-sGf-i8Dz_qiHJ8Aw7hYTVxf7eLlwOFIcPCQcI2GbhwCuCrmWMWNfhZUiPHKPojPCbN5uffAE40Zd50d9Mo9SEESX_FSSRxZ9x_MvGbkMYuKLlEk99lxTAAf5SrWfGXskgtljXX48CWjqdU6jyJtP652kGux6QH-n1SW34po7F_leFceE7zhytjofvFDgSEI3dh6sfEbD3QZUCMtS6WMl8ZI56IRhb3-JO8qxvds5dqPWqbD4LNGRYtRmjS1SzfK8xpXVhLqmiHU5sbFAWLHErj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzs1fk7IWQ9gydZLgyoS0lcEvxg5h1tpFwizdUh8P_EvVOVwn7QmrQdJE50SWMN8jzrRkwMdIA8eBvLGkIKcTMO1K3i994Uuh5C_nClOdASC1zXF4_2QsCEsweAL5BQiUXwuukEsJicqBdwW0hcT43Sg7KUysV_cckL1GQ28hVRWs9xcBh2-XdKyAkLSHhpq_2PIUGBkFqqnsimwENaXC4FMgrD6DaeG_D1biq0Jk16uS_QIYCl9X-GrtmZ5YmCxOUb2lXd4KSgcfAwYEPHpWOX83i3zCYFkEJDj37YELw9UhcPB-3S5Li7m0iQsCvbmwWsX1Tg4N0-XYFeRmUEYFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd5MsHg4XcA4NO3IZ-lg1AyZLU-MM8riS26a0VH3jn5s8kR_UtGOeVGzfXIRuj1Ap-Nz2E9GrKJ9ayhrNaBk9lsCY4u01DrJhZYxYBk0rvhz9YW0QmGj5oDNLxqwzYO6__-WIvNOX58uZPAewlriGJdbzdUkkjWsC_MnChX9NeOU_Qsh3l4fZTSATmurCfjSUirwRdilIiH_82VQpnFSPJSh4EbZRmfWHDvetBQ36rcYGgYBDvJrrxhkOkXZ_cdBDBdT2yQLEqDkdEemaoFz3sZs_bsSaSKX3m_bDQhtAiNS-3i08DjSWRwWf3rnCnrMuC0hcDN8qPQQ7jcX0uSHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg8DnA_iHS3FktPkk4uYMdQqMd0rHL-hpmTMBWUdUbb74h6n0GO5eBQq7Pbid2CsEAl0o-h7zKlUIwzbjWCTAPvLTwI009rSBRdbuWnVbK5dyjb12kVd1GZmMzKarXo55JSogW18ydB3doHzQoP34vITzo4_D334hmwagaGFvlT3oX1-sdCFvDllzTlc_rGIYDmMJ948Pkrs0xGHyIY9DSr1czIdeiXqt4G5tqrLN1GH4hbLY1CeimYLXBmYnZGw3mULjdpfpy4W889bNmHaTwDpdxjiyN74VgNEkuNjEFO4IPOeVLxWyCx-zwjHK5qASr9-v56DSi4fo5jOI64mIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgfvA2xbtt0DjikApo4rVoFWW48H6zu8vgPBPMTVhCBvcZAFmQwUpgZhLcgwae2-XwJxAn9Br-9NR-vSIfCaOxroXzWNz1hfOqyTp-DyJ_pvR6TogIGGAMNAtffC5llkHH0U6w5eVvC8_fh5QJoklP7b6UTppwKbN7x4R_AVh7MAEC6mJ4F5RGr7IpEiij-xiLGluUNRQTssbMr6oKdJRfGqM329nf2I6Gu2y1KvOXzMuuJcIBuCJaMLRWZ_xSjcZW-AS9oKuDzJ7XI0SfXG-FNRANO54kU6llWzBk20gBVSKJtG0pYb7niekAj5TPujG3CNUcDD43xRY0Aj5oJw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKD9DaavNKFv3Rtj2rkqAMWyRTAiJd5934ivTaFFOT-rUnwnbi6UDSOeUHy-AIVh7RMKErgiQIZQrcbIeNgUAEJu7TZ7OfHwYB10C-1tqcgrt9-DDvzt3QfHOnAtSmBSAJwWR7vthxor9akAMsbtHVf9RhR82WWb0F0DMGyG9rAgZ2ffw8D6RCCUVortRpS57_p0DpoXu8mZUaP8-V8XpueYBIBCFvY7xwabLuMKch-OyAC8LDJYzIUC5r5AZZ8Ecc1ANOC7u-MZut66eOUSho_HqDxRDlFuxt-BrpmBnnyBQE2FDKjQTmalMf0fWYA6h2--bWtjH9BSxg-UHQzSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjUh6VhUtHYjmz6s9wLaqjboijdntsvYRxpaHXeyDp4FmITp7_Um5eKp9XP7qoTIXQwmIe9zeflk3Xa2P_JV_CwE60kSE3QKJ56XPOCzkMKc94THVgjW9pMW2_Hn4_tvGuDe98g3OFdKCIqay97CYUH2GTFDqtAOmTDOrRnNDNzvQdLQyaK4Qb5rso1AtPo3dCE6HBCG8ujkAyuH84Xb-JtDWkLJ63yp8yGAQ2iC_ICQOWYlBEfZwzFSiyQ5Uj5L2zSwSOvihFjZIh3XBu0JYAn9N5kexXQ3jGdOzByfPtOMg1heSuSRn-jS5RJ8rlQaIU8R4VoQWGeWuyutb8sEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMRj07gU7_qnd2IpEMBQCfgk44NKRD4_e6kXjU093zZQAIFyr8D5iGUN44Eni-TsyUFIjgYNqW4nP3X8Cf9-V99hi4EDXcp0GVWAqtnIUoFXjc-zE8HYunHbtysglPqnY7xWn_LQfbpyti3C8Yp5tXwmOzmnPASZdHEmU53wjFxRJ8X64oewoHSRn5ReYD1RGxYpxQoWMRSeDeyzYvrxWRpt1KU8dSHDeCXTVSrbsI_pWf7P2Wp7Uh5Y5g4VN00V5aT9kmf5m_sYwjMyTMmgLI5WBaIG6hWWSli_nCthkm3orJaV9CqKe-0yEcyFCGWl-R44_GIIn97IzsYAu2462g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OocCeQCDrfVxd2KUE_fyBh9QsZpTKwfKBFfHM4olN39H0VUsf6PPGrtiCcWg50PF5aCOWBNW4508luMd7l5wBOwYb5g_98do4k3fw8x9fkbdluhDDVIX_OZd66HkG7rogMYXLqw5IZ2mzSK31hCoGHRLiS6OkrCt0W3v8pmW5SwoUzaBoaq-1QbLe1dPrmp12dpTmyl3dtuIlFt6iuljxyq7RZ3rHFtSS94N9PRH3QO6KyBOlRFKebj23XJzOQGZ4sNrgEpCV9c2UaxWL7x386mWzR23mSp1Hbj6gOV2ybjKTK9moc_B0mBt9zftFtZuIePL5todQT3SyBbgrZ3j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gttMrKAzASC3wUDqq_RH7BzXlefoVdhTlBTNV-h42eP-KYrdGjcUz6p95idaO9fUoU_UP8LQzKhPGKII4NSrkRkPVp64VDyRGVoMQO_EI9_T2oq5W2QRLyvP2YMjga2Zono10LVAl2O0F29EPRu4sfF7iHRIHgokz4Q0Ut1qm-aNk97Rlvy6gYci7iILxaEqsA3gFrMhWmYDNmDGR33Vy3DGpaxiIKJkcMGsv83NvDvvAwwSONMP__BcKQNfY7nC7z0Mlk7LazJJrGQUhhjzRuQ6-EEUA-7yZDEAUpq5WPani70BFLF_CiwQyNqS6-9xHmob5CJ-gfFs1x327LAatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJuqUxpxhNa0yDQDbX_eOT12neZX_LZSVm3GwVkFW4kT6AxxCHKLUSQx5Msq0ALOa5GZahYbRoMCr5nph8fKqohjLetoN1APMwM5W-8hTUTo6PJV4DhRLoaCXui1L8aE75NJ9NQy1VcsrmDKpAjXRX1qwCx2UDqPEj9JTdAEsTSR3oG31QEzpFGsQ_jz_C3y9w2spcNtqq1Tp14S4Xf97Qp0pneIhbqq-z3tdW2X1hce9PF2dbXOciY4dMejFgtF6C9laWgaSPtkDUX3NEgav6UOWboL3bPfIoQjJ6IYysUd9WpHvXaP34mfK1CqG98EfCvtRcTYPm9zIKGMZniwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoyG88oQmiO8JBz5wVzkCVBLpYLOZGWivpVn7Qz47Y_gYva3veX5WgKINpIhz9A-xC_m9QJIdMXRB9SrYXFgY8WUsU3pRJ3j-VcE1w8krwuUqLCWG34A4JGBqBYSeDuUfnctKQtUJPzXCNCm6gGaksQlrHqogm3jhESkBLg7KKI45qzPYFMsIuNhMpSZ9WxdxI1-3W26agTtbarLRCtgqlpaERqoNw_xsTdejdwCuS7iv6IjlGOBqtDSd4XKBUyT3yEfMHKjHlxiD41-pzIfEvw_EVo5qy50hQsBaN3OqfLkP0HdbdDMB1eIE9mNZrud0jkl8w77quoATfXcd7aldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAe1uls1JB_Oh-rx8PZCQnBfevPYW0uYDGEdGiy_n-cO6G8QxxCJ4usf27FEv2STFwyBaG7P36Loib12cyTNZO_TL-EcEnwOSYGvlMkxsI2uRAsTRAoRGv2XKJTw9om-D4783waVVMOmfwjCDNVX8oYdJXH18Kcw4ljZbajfIOP-lkYDbML2ZbMzj-YSjtbNHkIWEI6EOJrTuqpfHipk2qaSNG-HoDMrITDIdAnppKvSkdCQ5Vh84POGrDjp2Mc781Tuene2N923Higr46uCDuPhPB-3MwKrbmcN9eSmDpP_KDK3JbTj1u3T1TlDpzXwBOm5bUqHH1NjOY1P0DANOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeb3qghn-Nof_lx5JemUYWjRKToBdz2TDyznXdi0W23E3qMsKPK3hN5T_4RtZT31SI1vSYAFkk5R67ICzdaIfPCmWgXtnbxlHxYYE3WZE8QkpcHuxvT8mZ_MBLR0yIG4wBGKDyIs3gn97HzR1HHu84h6AOatcpXXJVk5e6UfQEynjuACR8tlrKfNGV1F_xRITqOPX7TZIuiD4fWWvSBN1IMgYMKXMpsavbmeFYWHavd7njoGkTPi5FvEvpFGuIsGEDDY1a2B3RDphFmisIVsTHU8Npkl4ZwXYAw0WoolMcW6DPM46efTM8VZAMOluejSEBz37eOct_l8TCACpGD0BVss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeb3qghn-Nof_lx5JemUYWjRKToBdz2TDyznXdi0W23E3qMsKPK3hN5T_4RtZT31SI1vSYAFkk5R67ICzdaIfPCmWgXtnbxlHxYYE3WZE8QkpcHuxvT8mZ_MBLR0yIG4wBGKDyIs3gn97HzR1HHu84h6AOatcpXXJVk5e6UfQEynjuACR8tlrKfNGV1F_xRITqOPX7TZIuiD4fWWvSBN1IMgYMKXMpsavbmeFYWHavd7njoGkTPi5FvEvpFGuIsGEDDY1a2B3RDphFmisIVsTHU8Npkl4ZwXYAw0WoolMcW6DPM46efTM8VZAMOluejSEBz37eOct_l8TCACpGD0BVss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=avotkdUaDpBpJK5X9BLjFOLI4Zu764FIMPaVB_JfA9mUCUocCmzwvrDGRRB4obQCMvAsygi07HGjbhIaIW3QqLsaJN6_O6dP5Eubf1FmO6JvnXE_S6L-tb2C4Q0120aAIX78JkV5hsaebYP5HmErR4WnRxHq_JjWPWag4Wd5znoWonwuQOGNvUw2c-_P35aqSD3jWGR6OJHaBFL_7eVwk0hUbe26spciHdjBkLTO8NjQrx3IIvNRXvL3W1Ey7fLrZfnc4K2XLsfQmf6MuYl-M2Zf2VZ4PjugbSSRk2-2lP0MR2Uw9Ps3dchisPYNcAfggN9jnzitYz0JgmLzWbn0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=avotkdUaDpBpJK5X9BLjFOLI4Zu764FIMPaVB_JfA9mUCUocCmzwvrDGRRB4obQCMvAsygi07HGjbhIaIW3QqLsaJN6_O6dP5Eubf1FmO6JvnXE_S6L-tb2C4Q0120aAIX78JkV5hsaebYP5HmErR4WnRxHq_JjWPWag4Wd5znoWonwuQOGNvUw2c-_P35aqSD3jWGR6OJHaBFL_7eVwk0hUbe26spciHdjBkLTO8NjQrx3IIvNRXvL3W1Ey7fLrZfnc4K2XLsfQmf6MuYl-M2Zf2VZ4PjugbSSRk2-2lP0MR2Uw9Ps3dchisPYNcAfggN9jnzitYz0JgmLzWbn0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcGTJ9KZ2AAcUKb_9NMtXg7IRwnGTWi1lyoq10AWpFIaAs8Hqk4emnGykbKtzlPTB3WpbmiaTU2GZJtaoN3TpGFHZ0ng6Uh1dEhx5cYYjxMCc9eW-JswdPOOu56hTbMsKdipDiqjELJKLUW4pbZ9Rf4sTFUcTT_JhvEq0WPyf1J8rO_xQwVAf-TU5i6hO4FYwOKlEHTz9F1a0cAlohhPqwIaRadhlhdyHZAmNa4tbepoDr08qn2ITm7_F6QiDyjh8Cx0de_zSE8hajQQFxWkCrJgi25h1dafgxg5T9654ZUMJ8mWJUPe-qmGCPzswc9hrsDek4aMKgheqqzgWXnUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi9ZWSkNeNOwq3sKKV2O89mIex1X-HlAaYSAHUggkmfhtD9fqjGddZEHyGQJE4Cihi8Vh97vDVlUPecHKUmoIgQtAJJhRTYrT-3qnO_kpIfdbPG05JFLAsed7ed-ZIKnIKbgzEbhcAV84pHlqH6SA0hSP_2R8T3XawM7AqvD-o3ufp86QqQKIiYWe9hGfnm3ZMvaHfrwFtRVIFeoB6YVDZJfc-ZLy0KEVpkpzKixzS_5n1CSaUMwjhlHKDWXzzRbfOHDvESrBzV6GTYfQ0QyM3uR2POR9TmVuMFd4XSzbyaQPPrjx-hsbWJpGnqK9l0xBId96GXQhcp6ygdQBi7NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7tXhIMaVaO-CUNPxUHWi7_C5veC5Q76bl-OnYmSvg9KYiIxQu4WNqMJ21YkBcY-p4Ci-8uE3BU6H70Olr9IFBkTolpjmsVqveUGPFj_VBu3cnjta7XR59169ZPFQ4sj3s23_SKd94xQPZ-Vi7UF9lrCQ10qSk-cDwbgh7mI8i3Ds5Mu8ty7ONp6sXrv3VyrXWAsLsvXAP8r3bqkQ8ZVBzDe11dBcn9CBMlwOYp5qkrQQizHtpYyRo34saFXQfOvx-pkHlH8N-C9pEqhhJqtiCDW7wtX74dTFOSSU85bjWxfyBneDNe2aI2ZLN0dCURZ0wfB3XDeyTdQvAPU-XuTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_WNf5zyKy27eu3cTX3dzRPYaq9RVoWYccz3-afbQPPjuBjqbOIS5oFst-hDCqx-4d1AjsV5yUe1L8Csqc3BjFD2jOdnJFNCiYogAMDbb1wboeSNH3-UtwpYVzj8ESxxpu6nlaVE6nImKCfKWm0t6JKV48LpEVm4CYPJhJzyij8tXE50xzqiCBCZE3Ge0k9xMa86sTXV6bVHpvBDnb-B0XA4EDCScBIocCnS1bn9vWIH_4oOznz3IzVhkv2nkpqN876uDTs4sARvhW5lQFZn9034qWBLaaQYj2mIQoS1cFZOOLJTd2ax_CEXAq149aTEL3pRBj7Shyjd25DcmRNYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPKpfBMwM8EHCkmm15eOsOsDamnMjbZs79Rbo38zjdwH0vMsV0fZGyjEm6Tp5twGA4hwTkxYprVz-X2Bbth4qAv-WrkP3vKKKEKC2_aRzV7rriIKT_XGNRlUZKbgd54NtJpu9tXasE7foIVHIHydzZkeUso8LxZEFK8nagA9zvuC_yGt9HkT8tOLq1YxhrmPjv3UfLBXRwt6U_XEC-QWgUkOkZQ0wnyyzcqZ7687xRO_ei4yFNkKInYZi419fduBPSnZiMe4jrW4C36ufHPYMgvofB9b9PS9sjozDzJklTuKAa6JK2-U4lvSy4belpokRldyp-I7PKYvUSEUZJgNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXgZ7Hf_NXzS2EawPT1ypEKuiq93guS5XqV7-o8WRwsGU9l78MnUobdYWXahOG7ka2HrtHpaPvFiDtv0jHAijB_RC9nKa0TRrRhHbIDBjnzUtk4M5s2EWWJtURaK0jN9Ab76JFRBMa_nvzVIioSFHb_N0SKoqLKvNO-phikC-cyAcBrVRaOh4eegqXokqCINY94gmZOHfb1pojYQq8SU_teGuChp3cohBX4gxw7AUY5pQs9rikpxhxsmDoC_H26z-pu94eSBvc9tJWIZePvcZWCy5BDMsx91YQ3K_J1Czv3MIWcVZqtbkdzFTc-zZSYefLSZuA71kBALycO2C89T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBopMrq21GlUUkREHZ75n8_OtJtGNSI5W86NJZBD_0lJOitSOaGRvV_DBhMHGCD0g6g9M0gEn6b6L3mX-5lHQHFgsuLbja9S33fy8I_9nA1hzpqInbRe6zAeFq9QGIVFCM7XDR74yJaSnfdVG8dpAO-XzqUPVJIGKnTzZos8rBn_Z4JL06AkoK9RTm5GuMKxAXpeZx6hbDUVInpu9T8KerMZ0kiXlvLt6NpJl86YTBqh4BbvzzwEglfYS4n9yd9oCf4ooHktI7z99sERL8S0OSJQeDmV5JHlAx3H4bKDFClAWI0bZKAD5cW_yBaJLus1c32OeCoaG0R63Pafxi6Txw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpOkSRnhET-gMeBLtcP8klae0UlXEdEHbZiXitHv_Bd_lUAOReccdRQkFn7CwLMhnf423guMcDuJ73V_NGvVp_DBigalN8kRSeqvKSBgCa1dEL62TMR7GiLg1TF7p6fKTl3h0KeIOJX1nUcVQZavURvfSpE3oyivLZjnl4eIZWE5vbE7TxYFJjTSzr8NSci6Sz1qBwCWuQGLQ_hShlhBRSBrYCpfnHV67SI5JWqiw3xNbEuI0bD0PETsb3MCwE5LaKQbTAbjV8vug1XHsPVSlobykTnUSwHhsy_DVOwKDHCq39fgSlJ1ZHBlxG9lCcm8-6mEZJBZRTx2vFXAH_1dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdD0mYDYuEiwh2Wgamb3fbC_4r1KaNoMaWvy3Eq43gg2RTUfqQs6H6ngTlSVuAw_A3ENmVp5ZEwivfpSNOPQtzmLGvlWNZOMJ7xczp0nQSX-L40w5DbaW-vK4tXZ5Xejw5qbUp7kTQZktbLH3aua2wNj1HwGSLfaXUksGZZggeo3xMFKSsWd2vMs8URqChSETSDLXYZUVAz5chpPbCam4PQtJuRbXgCOyBFZDZzwVX3YB2Tch7j3LbcOieEpMU7pXvYB_S24VaeQPxZFR3uec8B3wOwV-AUUOBUL7HfWg9bWCSqVaADOLWKd7qzwFS0jK8LfJ9zrpRSyxfTdY5Gjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMsm9GiU0Skm32iAVFv70sPVI1ustVKPFV0BKp4kouV9OrrlC-sGWK4pTVYnMb4_ADygCWuhSGM6m2zjeEROElbFJu_LL7prhEsna-bw7Bv7KXSezneSDW__jXmjLgUJUL1V8jmG7I6ZV1yob41-si_OQJroFR24PVB25lX2LHVXZ9VjBXeWeJQMlV3d9RYzVxUPXmClGsl5cnoNuaYkhy9Zf6oWtqUMrKFULCLdY8sqLQxlnL-EbUQJaICV46_2WTGoY1QsKG-xZjfcH20nWB7msgq1BXXEuKHNKqXn618OrNcvk4BsBg3rSNolPOReJnOq2KmJrh4GhA6oaXiC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDk84U0ZYl9BLeO5bkhoKVsLkNCDPHpjpgwnNH3sHpXPU-4mq8X2FTOBoPPNIxz06BrVl94KM-plb4mAJx9TqM0cL1yzE_vLe3K7buZBtEg7kRHESwxIv_3HujRTVufQMAUC8nL1TFqTn9fqSR9P5mhnn7f2bem6_bSyqpQBzmF6ODKQojBXDD5KsJ8ijwxlWp9CYtPFpCuyQMk7vXzqOnq70IdNuCOfxXGTC49Jo1ewBdSj775EH_gFt7WJ4qNKr-i6VEfLhiJnRmpsWEQONOW2bgZTS92Sm5elDn8dBSXhZgn5KUKQq902kbiva7O98drg7SVP7oXvGfEKglDAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVnQfq0DbADGAo29zIes84nP3fpaADVM-itibx4c-0Tn3AJeSxMgsJ5stkygLakjmAhWMF-KB3n95S3yuRaVmjFbnSz0wW3M83vfwK-P7gqemrklee4QUhRUkSUZzI366YlKd48EZH6K6D3dq_GX8qs9NJwhsXrRddFbV1QE7Q0Vyxzz8-v5yKy0Zft_3nJp7_MFGlm75IpHMDTNZ831H_1nDN3IzZYWaV_Acht0YCiEL-B8hFQa0eYowTB9rbl4Et54HTMdTrEuB7WQ4a6W_fGea1SWxsRKme7vP6lyePrhNIFzCFE1AJpWcHQJ30aujwqg0KItrh6yRlC2yZACbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4NtA_Xyw1TYTX3FwjpbgYkGXstoqWkBt9-1_fcypAmeujn18Cuhjrd7anqIs3Bo2W04CuXHcGsAv_eN76GPSreAKT8Gu5XLArpQp_RNCLu3IOxnUApYixOA-I8Ww3t7pRURDH_MlmSnPc62nqPrfsRKcrEcgzC97TW4ZDTYIX6qaFLaY7MOfFPxrbRCOapUEyLcrF_Yz_9jiKmHpZy-ReaNBGUrPpsoppJkZJ8aeX2FtKr2-CwVZ9EuzQnvYCtmLiePjt7gqJny5-6BZ20QibOtnNh-qlPE7Ey87sVO8pqB7OGtqNDsSh3YWFhNZ2BNbfI_U-nAtY__XQGwrojuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF_Jdvpqjqb7-4pVTdUmVUgz6-H2nVllLqiiU7IeDc3Iu-WMKfp74EwyTTZL78iKYMTZC-oLHFGRoPScCxvsu6ar5ULXW-KmPEk6wb707WnpcIsXwfxJ_8Sa8ICvSk2TJQ2WdJXl729VpyRmEaWsVpe4JYhSUq8awiZSl2-Y6wmnw19vOroRbGp94v6nDOW_D0Gbk0lcm_KGlJYVS6-eXhbdtwElrTV39c8aTR-grOBw6VEOWW09AVuqCmmLA43R8e7M1SV5EdIjWaj5p-SCXtvAnYdhaR06x-jYv1oP94L-qxJz5h3P25l-_r7VZj4UuoLFEgAhxaNz_89pnqybJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR7u3SlWp6U5r05GBJ3_kJvw9XnufFtebTsxCBFTrDQRxpb0IUPXPan7TRE8lcgORJuxnxy36_2D_LV1K9N48nHObmm5fmE01I_Epm8KKvcnA_9MdndFE1OMeyf8tgUytEPawfixTaKsI6z-XatOH4L8KTyV8xcmsxPpZHudPMqY-yip0cIKjZSpy3G05TaILGH40OE5WDTWGMvo9twSwONTd4xVmJP2NlsspnAZOSF-YOa1dWBreDrl6RNCNcCaINtPLdiITNy0O90jX3WCGkLwNo8Wr-kP_xzn8DgCTTwAgCBLXoHJusBvvl13jaQP8Q0WV5VzhESh41BkNWn3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZo9PHlWohEYpSK7Wnprllzl4p9ZmeYXQsQ39Zk03wGkTOan8GmrPiQPYONfcrwpB4aNYDZ3c7VsCH2UggZ0y1R96uRlg-ireRiBqrUVM6PbqfDlmA0DNf-EEVIxu2orqtP22AmCzq5ISzSLDfinvpUPC9T4Rdk9j2eKZ3PybPUJGT78-fQrnSWSJz6HT7WLmmu1HqLOlsamslcTZgIuqCy1wn4odcJ599YoFzAtXDdeOUqVFa9aZE7LRr1WPjm56S7Gu4fAfsRJXKpfZMrtxxZgyM3x9ia-R0Ysf69IiXJrieW6wSAx8-O15je90k1zylEq4ZzUkB439XokBOewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxO9g1lQnI_ZhnhZvDAHTY84wm_hhd4A2M5Ky5zYGsDS96ESo4kdM5uz2006svz2g-fAjOSR-cjPbx5qeMbD61l9gmC8ToI6RyXWR1Lc7n5VCBFkpTKbPmcAOa3uJdnTZ75yJxHhUTb7_7oe5VZTGCm53n_ZpSh0zZGeQbT52lwW5WxnjvRrzcTacppNUZjkHbUo4--e4YE4HQJ9xZm6W1vwvJxhFLQDZoPldLJx02YAYXHTfreQOri7digZSznw_piCaFCoN1hhOM3tW1TCrk2TAgDvNaCTvDdBuBYJB9SonO_AXMqJRw3pyKCkdbgTP1cXqYphf0ahv_Cw1x7T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=s92u_RV-xuqw-BferLqOwfP4rFDxbSevTxO3zERmPrS2eFM_jDT_4ouWCfTs2wXpM-sKZMNk8PUbFdcVZ3TQJ3ZMetQIf8bqQLIvkjjTYkNMIhyDZmuAca3yO7lmjoxJ6La5w3bE6iTgZxqsknLSWvd4_MloqdGJ1Qjj9luAbbSZ2jD_ZYG5-f6jnF9KNjKob0NZsfWYaGBc8mPvm3BLoG1RZHCiAMtl2pLqhI4EhUQ1cTTSF0n_MuadNyevCU8XBQijfEQJelwmf4M3eeRyVzkcIPL1_lFEIA45M1BHdL-yy-rTeMRYMY4EhhbzB2dgSGfJJbUWysiNAXNd5p6LjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=s92u_RV-xuqw-BferLqOwfP4rFDxbSevTxO3zERmPrS2eFM_jDT_4ouWCfTs2wXpM-sKZMNk8PUbFdcVZ3TQJ3ZMetQIf8bqQLIvkjjTYkNMIhyDZmuAca3yO7lmjoxJ6La5w3bE6iTgZxqsknLSWvd4_MloqdGJ1Qjj9luAbbSZ2jD_ZYG5-f6jnF9KNjKob0NZsfWYaGBc8mPvm3BLoG1RZHCiAMtl2pLqhI4EhUQ1cTTSF0n_MuadNyevCU8XBQijfEQJelwmf4M3eeRyVzkcIPL1_lFEIA45M1BHdL-yy-rTeMRYMY4EhhbzB2dgSGfJJbUWysiNAXNd5p6LjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHkJn13Hw_XYGVSqRkPVgw_9UTaIopOHV1RkTfe-XvTHQBMyN1ys7DNwAB5vfCuqoS-7P2hmdNZi3nursP43ygdb-ruHRnuCcfbHl5agPRHTOQrLpgRxwWLOVE1U56a9a-aJowvNX4JII-tsw8MliLIunn4WLZWa3FdqRBYPZKanmbPv6rdHFkfNAaB8AkMK2Okh_9IOrEOeU6QYI13E3hm7_K3oJETIeXUh2X2aSHZ1HpnhNTA2ELYuplgkNNK0X18NsXgZ8pwuEFjWQtrTD31DO6-JNaBYsKc0EHxj0wTQPJhTja8rq9au1rqHEFLCzb-SGbe5B4KEkdTQ4TeZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HgQXXMi0u_CNxuI29JMvjOfA8TLuueiGh3g9NV9iJOSZWpXFbs1MOwWnnPUKUjmVcycffKYhmPrl3eXTNWQ1SzOnof8RR0cYu3U8mICei4Cz2-RpENrq92y_ocX3ipZ1lrxrfTHrKmry8CP6Z1866j8bn-c8RB9ORqZ2MIkHb-eqP431IfJ0G2buO_TrGsgJt_1cuXM9k2RVL6eF7qIPwkKeANverVSg_tJPQbrtojqLMkkenGa7Oc-qutZftGzTIgEXKgrl_OQCPL_L0YFg7QDv6KLjQc7qHyBgzIbW7ZbFM2pAJx_uzaQZ9LRddVfGQKEMDz3kw7vgHui_oC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icbU3k0SRvoPptzZqRDpDUucYgqHOqFT8nZPP9HmG8gAOGn2oxaC8KOsxJJ8yo0txDIFUbBE0k2BWkwuqjKAZIxHy9Mg-dXzWIV54TxM_zA4VpHUWlCL8XJoPLTeuTlyh5asBr8RGGoMkDctOPFh6Tm3HavW_anePNH0aAOMgECYh8-utR_H3CUnobwKwetIjcehok8g1XIW5wH_VlSE2QNxEqp0BaUEZBdXd0tGkzKgZYIgKahLKtKOSJncFrCggBxDcnS_aFFsKFJ-R-MPfKNo5h5XZWo9No2NoaLyFjdKq7ww0tO8sV9hIbvh2BUwp0cWAr2c008FW8GGhheYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Q2DdlwC7ok7gbx-xtxCun3MfoUQILr4kuxjUA6BqHF_hQYyXgO7FhTql6Q7GzQtA7R-xEoxCpSLtrhoWb2X-O-fhUp7WWVhP81QVVnZRd19-N43BNR1XEV4-lVdRehqHvXwVQWEy3W3ZKkgmwKzQs3lbb61bvTCF_kZTiB6pQ7s2bYNUrlkrQf2ltRj21OuWPVoEwJ60a90LWwWqxN9-e7zZu3p4gL6aH7TnRgD0fsX9lFBPWfbL4K5gjfa_NImU0GJVs5IdzihQSBXQP4vV-BV4rev-0KE40oighpAG1VVUGRZRueA6nYpuWzYT05ayVkxENbbSKZUOsjgac7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz2cKzmIPJhKeSAAFh-uQy6MegBQVhaVn-TjAuuwBojdWwSlvwkiyppNrxiOFcUPKO4foCct6VNtYFWqcGNv5HwJTzPYYbQmj4RnGcvhwePwmuSmtQ9ffTT0tEoOP6VNx5Hpc7uKc0p3OIYEZeYgNeO1m3p-9UnL4g76x2MU2bL_uItp9kN5Y7SlwhPGVoLfKyDbzlN4H3EOQoPbPSVwJ9QRkljYKLTAUSTSETqZOe94pheNaMOr1CLTCJO2VPYLqfs_4RqYLAMgOdd2oZRiXmd1klI9XExpiGRGEESTwiGLGGIMC95qXhk2Dl4diMLUIyOqrX8uPk47gRy1jcRKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwYoQZAd3Tx7xuNAYsxncaKWCueMyNuhPp-weRmbAxu1TvqeldxAx2LEh-g0E6xPaENB_gxT3KEPw0H3cCIMOpwoj1XopTiknnqUWiSMElNwlxvo_E_IzNyWFOgbmMWtjznwGDrNUjWS7z5JBmDgVBHxjbtSQv6saECi5QgSmnAPxK5NSbC93pnFgqDzM8TOwXGudJo2uLN8kXIUuPtkeyhPQj18Co7yn5Xi5O1viZ2pyod80jRrABMTUheewjNu2hBeyB_qpDmrqUgNRXq6EHHriOdmTtpoVYis_Cd1Eu9iRUtZcBufSIySTxPYH6Sbz56ID5AEFoiEgKSVF7n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvJwEBdx5RgrXXlbgIngisQJwVNnqJG5LGp4_geEvzBhjUalDDUvX6n3lkEjOIFw1cL9PWBtvpt1RZ1I9fG-7G6lCCTxDe-1hEUFw7GtVUThbmbpXavZPux-owUEfrNJc4r62iQqjUbwxHlVJY6o_QQ9yUTnKdvYJ4JGydQF8es8PB9HHmQxr5Lj8okP8MNo13heR8SPwskyB5O5bkp1m2eL6L-8yr60WjIuQhED3llmnyG-Y9iZ1wgnKjdPpysCbECBtJsAYXFwJQQQNNzb1czGGhK3XDDEGJMuLb1S2zQesoV_vBK5QoJInE9Eh8QckyKngGmVtwsA6gKDM6xtwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twl9tZp7h-vNwUcVmyfPRv7qF7uxBqKjbyv3oePH3un46-av876k5zSZZtBZ1QuDWNCWeZRFVvYLrcn7La10yFZTEhKKdnzz62HUy9iMTC2PgiSHFJyEr2WggxmGu8c2rElmQMQWXrGDFgzwtqyw4mD82QVCk17t5ozJLlJsJLUypZIoU4T39-9AlrhQI1UvWFPVwT99fVHLCjZRTJ5VkbEXFdVRQweVsIByifgyKj9AT6Q5ZB-hUbRiWogKrXD7Sk1rhqDXzhp6jWFwcVrx6nGO2-sPqZFk_h2kyx2nZeh8srFamdGTk_G2HNcHDuvbny0wYX-hZKST59HewNhtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBcY3E4fpXIiapimxCwn1JmEPhySNsWMiJtLFV8FTk3ye-R7jYeXp8vqTVKS2ONxUMzgoXirYvFxvrl3a7Yk-rNcaa9KuseU3Ca2G-HH5sLHU0R0SZ-wYdWPT48PF6Fbe5dxseQfreWKS0w-RqRq27z9fS1IfglnIAGAw6zMcoSFhFfs16VFe_tvcwHbR-BIkcojfzkyivoAyUo0oVJ8GszSufbRMacGm_mqx71AE_UWruuP4ZkK73ypcN2wj_SvxRB9KF6bj-nlaAPjKKpjn0f3Btt_aAw0OyL4QAZg8a46zKdbtXV7Vi8xJ2v4cHp1Pk42s5pKPZ_ds-aoeDkAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaY6ZH7f30knpyM4g7T61s4hacvSQ2XXc92-82TKHFML77WXmRXC5iGYqjeb5Yb39bLxhExXcleMYVh_RhYH-InvHd_SlzsXzUy7cyYhK_JTZbgqsVxs2Bx-jUrZfEJF9smST9j3XeY78w2aK6DBOhIC8SrsIBWILubeWLVUPEyjyWwf-gRDjFnBSnZoaIWNP32PtFNAvoDUYouWX78x4ZWj5EY6PXsXe1MI2kprRlyShNUFWey0_kOop2q24STRl6gwNS6TyDgtMLwoom8m5nAHb-WgHh1KSgNST4wrE_MfSrYuT9o4AQlgh62-Q4NX17i6aAQIo0THb-ObmrCQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSmpJ2GJ4IivYKDJt0BqRGLiWOqhyw1gfzZncy_uxJDyhzzCmMwNmMRh2SHsNcv9AlfZ9ntMYY2UFUTESw2Qcbj7vOiY1dVfVt0y4wuM2SWM5Wg7ta74BUUSzIKXNG4uoAVzLlZZVT5zYm8wELt9ZJP_bp548WZcnZc8Y5MFoeNK6Pv8fS3jBKAO9zNT7smI7cEupE-9kgTrIb7Jeb6WR_NT4n3rXEXPWws_pnL6XtZKXMLcJNMX2c1wKm87bpaDZUiXw_FdxdIdPadKCIOfbnUcbC2PxiC8eQNeXjW_lLVhGoNdN8-pDOWtizV6MBPiFOopwJs2mcQ14TCWLIbGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLcq6FT_ErSvrGU5M3Y43JXtUyidgzlFsJ85R7loueAE44KiYiCwH8IO7nJfsiChJ-59r-C-XiFwTTsHpEJLzfw2U8s6ZhsfzDOtz-X6OPOGEzNpgqvI9bsfD4ISZS6gIxRfa35SZvxRTyIN75-ZrKH5VPwv1gYAxfnOM9u2F6Iy1DyLEc8WRinEkwE3DY0SUXvSvqYnZK9bDZriwmwTEr7t8GZYp2j8uufbisKJ4xr4l1ZoP3x7ejLsv-_lB4F0M5c45u9TyILYtgXNVdPxb5jJ-_NY9WyYymqTcGfhcSVSnZ5ST5s6GqONIkD_tvEJw4AqxLl2Dko4nrfh7QVZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=Rf2hPrAbYd14Tkbi6zWZw0IxBxTe1-Dj_LJqcJko1gtqRKjMA8WhxnzA3TXhfGPwtGU8HLKcEanxA1wBBkzZYg3s3E6IH2icGjMrf3iybb12hoGJPNEhu_fKV2pgGtsJRssZzYVN4AuzMOynuBuPLuVW9bOwDhzRUs3uYYk5RF0eu92qfbAOnQ2Gxg4FgwbA7KfLSKrUfmMbV90mT52rcRUv1mAvRyC7U8V7bojRQWGwPbdiKziyaf9H1FACyAGCJ4IALXWbj2lQjfjFHW4RFf9axCiQIoCsyfasuimthlIspayXhXFWc96_6uQozZOy9txnU_sav6Q4IkS-eOrk357VZszfMwOdikUm7H7cIPVFfKLLQHLRSRwUOkYD_KgeyHVc5CLNxuJLbKIhf9Jn2g9embJp7TVpvH-ywExHDBfHizLrBNfpL6vwjORGYa_zVWM6i2K8leoKeNzoTvqSS_bXP0CDO-gx2lUdsKYC1r6gBPO-9arwxenZtDpGv52DMTMCwz80ZKS5C4o-Io2jAjBec2MLb6gBEePZ3L6AnCB9lIFm_Xf4nzuVA5epJ6-1-HFTFeP1rUla32qovz2rJQpM6ewxoZrD19PmbBmgeJW1MN2jXps9ZzuBjzJqQ5jeAHvlx9etfSLbaDiQbByDKxh-9DFTaiUzquu09OKQGr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=a9HtRkhEL4sAn-ag7yvZXxnpG4b4oY58ksewS2yupgRW7bwPMlcOG400_DU75lTwvbxffqJbzi5l57G1Al340wHT0UZiVftfqjpvDWr9Cih2mhGYtDLTSaIkrdQfTnjcw4GjPax9UudFVoRTdIws9XYOxjM-V394f69sQME6p2T4DtYc8kXbDK-I1aKnkzj8zWWIqQn0ZCoyzGuwZD63ZSmXHfk0r2nn7HhbIaOzJFeoufYkQ3kYN3gak0PrrAUjXpEN-5T-GSR2l4K_f_cHBGiZVoiDSoBXgPr48VucVWSWDDWykFuYqUr5dPcbH1sQt_LwE6AHK5MmttsOKYTNAns33SnF7idJ8PoV3601TMaJXpTbZG63eGk6-mKiA1gURfMAVCBIOKlYCWp-yiNwZCPYLrbJKO6bYz_8Jkiu96OV7-XoNfNoGOVkqt9uveXbwJmiW0T8ppJdBTaofC6tFVRtndJKhsYm3m8WxTXlLic8Cx8Mg6QvNlSkzon5sgUJUF48ojS8nTQdwDr9r1T1k5cBTCjXp67p58THSojMzaIXS_6FFmjTmxsMbwI0KZK8XofliB4IT7RR9h0la3EAPnf6OEZW_fBg3Cf7fy_KlzMvbo11qqQaklpPoDZKHDD2ihpyg7UYaT7NmG-pCfiCPhYUjUe7kJ18PCotD3YTZmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=a9HtRkhEL4sAn-ag7yvZXxnpG4b4oY58ksewS2yupgRW7bwPMlcOG400_DU75lTwvbxffqJbzi5l57G1Al340wHT0UZiVftfqjpvDWr9Cih2mhGYtDLTSaIkrdQfTnjcw4GjPax9UudFVoRTdIws9XYOxjM-V394f69sQME6p2T4DtYc8kXbDK-I1aKnkzj8zWWIqQn0ZCoyzGuwZD63ZSmXHfk0r2nn7HhbIaOzJFeoufYkQ3kYN3gak0PrrAUjXpEN-5T-GSR2l4K_f_cHBGiZVoiDSoBXgPr48VucVWSWDDWykFuYqUr5dPcbH1sQt_LwE6AHK5MmttsOKYTNAns33SnF7idJ8PoV3601TMaJXpTbZG63eGk6-mKiA1gURfMAVCBIOKlYCWp-yiNwZCPYLrbJKO6bYz_8Jkiu96OV7-XoNfNoGOVkqt9uveXbwJmiW0T8ppJdBTaofC6tFVRtndJKhsYm3m8WxTXlLic8Cx8Mg6QvNlSkzon5sgUJUF48ojS8nTQdwDr9r1T1k5cBTCjXp67p58THSojMzaIXS_6FFmjTmxsMbwI0KZK8XofliB4IT7RR9h0la3EAPnf6OEZW_fBg3Cf7fy_KlzMvbo11qqQaklpPoDZKHDD2ihpyg7UYaT7NmG-pCfiCPhYUjUe7kJ18PCotD3YTZmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=BWEulngJo1O3R4tW7z68MiKEQSfh34OgsTePPP4WfO-YcYub3xQDCjRSkb5mZSMbIoX_aje4-K2JygBnmjsFuLvsBj98Vx3pGA_l2rB7NMMfRfSMshk3GKhD5aC02hwKgRMNWZArN5ntuzl2SA3SewjwOENRrJ_vPdz9oxX4yX1zfpdoBNvt4sRh08IC1KEl7xrZ3yI1rObPeKi11f2ZKNZBKzUPeGBPWCw4a2pyDikCxVTigixqp6prVrzyxgJ3KIqOyejHkh6JI59jLn6sHCZ65dTo0Zt24ywcqxCsM6uy_Jn8W_HgCGU77ummR1PKmnWUcdBpslWYN03V9tmgnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=BWEulngJo1O3R4tW7z68MiKEQSfh34OgsTePPP4WfO-YcYub3xQDCjRSkb5mZSMbIoX_aje4-K2JygBnmjsFuLvsBj98Vx3pGA_l2rB7NMMfRfSMshk3GKhD5aC02hwKgRMNWZArN5ntuzl2SA3SewjwOENRrJ_vPdz9oxX4yX1zfpdoBNvt4sRh08IC1KEl7xrZ3yI1rObPeKi11f2ZKNZBKzUPeGBPWCw4a2pyDikCxVTigixqp6prVrzyxgJ3KIqOyejHkh6JI59jLn6sHCZ65dTo0Zt24ywcqxCsM6uy_Jn8W_HgCGU77ummR1PKmnWUcdBpslWYN03V9tmgnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2ozVETuLpNPBGhSAizrIMDqId8oiUOACEbVPkI-AcDljFBBd1HdsO_-DUiEbC7Q_0EJZ9mrqZxfcdWERrMJgxg8vnON72JQVRbYNOgwax6jlEiIYDXv04PIRCA0PfEeLJG3dnfNgPG4KLXp49bALSU17tp8gvtW8cZoCpR1g0Z7kypiZpAM2EXLR7wB1Z_7SyLAd4iOfLqLup4LRBukwXO1j8uYqJBe68lCLlTF-iKL_wBYLyojqN0RWS3xLotm8ZqqKALgIfw7TTxDXJvYV9aMeABB2qpI581Eo2peLfN5omgatG_kC0GWgurnVLNfASo7qYcGvM129KKv5x22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdjqOZ5FL0POd80dNYp7oNgX67obomLsfRGaoYoiyaWrOl-GBM6wA04UIj2sDkJA_nIHXF7brYCoxMKNXea4QF0aF139mJZGEztLoN8v_2a3Q0GFycqfMqi0meLAlnuDi2tC0_Dr5ctZPLhh9tpIg3IGRT3w2-hoxru6NZRYfvKDI3Fdm9Ajduxk17kC-LYnOE0iurHvDPiD0sUJaW6vB_prfpnISaAE6mrfD9RVoChfpZQ5WLAt2bBucZYOE2K1V5YL_XZs_YRVpssfkXLgrLvX-Ie9y0Y1TqP9ifLOtJJITrVmo5G0HlEbluFnyaRB5OyAZEbZ7MMKZdKzzVRS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9m-Hdek7bNsi24MC3xJavWPORj9A4NLTV5cgexfw3VGWwDgtAaGgq_YnOLxyH6Jx_5KmS9BezulgFYA_fxWWkBBNgytg6Kg0Pjk9yU9VEx6EVb0TyNtsuCEQKIX3YHdolncjEwZoWh9BhUTTTsp0GaYWfKlREke2MHer0DVYobbEKkzJRjEMd3NcLMwQFrvuFiY_eAthZNFfYJC7fOS3yqrh9q1UPh-5S0MQ43-g-76zLtL4RK2Pd1qsLb3zzMraD8YqtYqmfujlBpUCFHA_nVdlIJygtUeizmLeU90km3FAzd0pgGDoA_SzKGdskyhIH2LzzHkDyZdq-429n-cKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX5O9lDb9NUB8M8_SN2U20vkMenYly4Qqyi1P9NdAd1KVjjv25CIlsK5y3Ay_Ple5JQR7b4SF1hb6QwrjI1lG9Defg4B39SyxNfTLe9VV8BkUFvrMNrIE0FoCl7NQkLi-xpwHTwnEODZrddQCkCaSbWVjKKNIvbfQvkJSalb3-JWiX3a2UsyAtI94duq6gdEEHJ69yuTc6ttaAogGTrhRSsCyAJytGJuigeUOke6NioATF_5HVnaggYErEnwPX2Q-9za6xYRuSj5CDjz9m3G2rd7N9mOAhDE8w6n_xg8kz2VyKyJqHL_l4c3uKsXNL8TM-q0DnWNGEZerBjMg5yBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvtgBE32Cu8gH9VQeKeCWTsx67ZJ-sDFztWn-ffjnGNl7qQWUNfxyVZ0C8eUWOnQSegfUKrafzjGUwgv2wEiGi93oMZMZh5OkaMoB8X9Iq8pEAmNtDYIzFxLpWrVP1ewXmZ68VQce4sbIl1Qn_x_BH2hQJ44rsudkIxT7fhjHA_dwdxBnrSILmzAZvD08uIlO1XtxvWHniUPeVbANKp8ouHkWO1ivrdt7FA7rmqKH6CC90iGxnJ_cOadiiltmPwLNfvFuDxh8VJifNe6FhEMf81lYEczDQrf3qnn5sszV4Et2xmmOUMhBwdAYsxIvO5H9HDZeWh8bszq_8xOLzEmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQs__Z8S5cdNSaFKGU7mrlZYpUi4znQFkXpHUo73FsLBCIyVzmwewoObKR0bjUh3iAbi3UeaOLBezsppeEhncoc3ZjcpBHRDq752vWnQL91qvAGMeI4mSGCPzg2rMmrgIpWv46YRck9plx5sYajac0GZ6eXgCZvkxhGq9s2EYcAY8hosPdPSwzff6zriSjDm2VhCqVzz2yYo34itcQ29XC4Rwua6QG-cbX3NcmE-t57flAxgXSgZG95TJKFf8Ggkw2XpPT1j6-g_2Ugs-05KMP8vr03dAq4FRCE3hIbIG1dxE0cB8auPhMOE2Qaddvv4mR5ic7e5NOeQ7PeSAq5hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUYXvFf-oldJ19On1rc2Ip7pUwk7TAwgRWZH3PjTyaYFcYjEKn7LnXSQ9evOBh4v4kEYdCH2DsII9cB0xBDoVqqYzmU1YswKISigj5Dij7Lxez17S-XgPtUbmzhIf4wOdvwmCpKYIJ_5H9J1sgSsTzL1z5YZt4XyYstst6O7xNvbQS-tl4HqwA_fYE2Lr55yAGYrt5nFMo_dYIPXhseGlmaHfw0j2kN8bXuEnT3GHnFjpVFrDxHUDrhgesl9MzYprrEHTJRiMAiifkETXhpQP8wsLwV9noaY_huawqFN1i0GuwZ1mAy_a4QNBeDdAckUz2cf65Ri6fboZnVwAWSAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDAUlc4VpZgkIlnNEIzyAXd2gE18bZm7IvxK6G-GMFFdYX21bspdycbGIVpTOfRRGikk9uOBG34gWB5gRCBuKzJDfdAh6XVFy-DgeWnSEOJeE3jJgMz7c7p_qTfpiMBXXOTeEj8J_3ChSBg2larjioTHF-NSYIBbNihiKIsAA-1sS4Ys6Ud-h8hMYwr-7DarFBvcr5qXaEMAgCkkhL-uKMEqAWRsbPq11JfR9KeOALCEELm4pmQHj3WMvKsz1G8fz_MnfmuFH_aBN4aHg9aX_WjBTFy8c7W5e7xBd1udkAPeLpBlvkmkRiY2rDgG1ZQPnoZ_NO73OamDWGXPebJdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJewwqTbPwLyWITYggOVylELNNKIccI3i-EWDclxeURZoyVzipkDmaahFIwhsZDZh7fsFTc_yWrWe17IFD47ISs7W0WDKslw8_u4sYQsUhZNW-ZXLKWRwhMMzTDaSYwBmheXXwdcFYjBt7VYnNufpG9-7C0TAnnj7HTm8O4y_GdOqb19TIVdeNDrya0WutdIShVdHcQaSPTs748hZlx4AZz4WquS-zNQfUwKqLhUnhQvSUGBJ8E-1gaCAFtzENPtaHoX2-5PoJMlH-QVRjQeh_EpOTWDveCOhQKsa4RTFK1GapFJoOvfob49_Bi6OfQxzspIWJ6FP85zuMV66TQV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=VMPg1izOy2JCn5sf0oaPNYNbeWdtytsg_rFbgQW_9TlHgv7lKk9b-PVbqsU90UWZBGLvqFVA3-6CNPzr8PON18kNHAYMcrPl4uzUu9i7AaVXIQAZXhh3OKRdCfvXdBRVNphUYluFBkIk3A1yA318Vb7w7otzGczamXn7n7ow9Iq3srRhLJItrtozegqofKDCRI_daf7drdL-27M9Lbc_4PxGHhQOxKPOhQVqWoAIYCrUBMEgIuptRu7s6mB8kePMVZ0amtr-oHmu0z6uTjPrOkGNab5HpxNrW9H_QxkYaBvF5y1bRbTF0mM2JwDR4Bjbte-M4svHQAgNUiOhVMODng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=VMPg1izOy2JCn5sf0oaPNYNbeWdtytsg_rFbgQW_9TlHgv7lKk9b-PVbqsU90UWZBGLvqFVA3-6CNPzr8PON18kNHAYMcrPl4uzUu9i7AaVXIQAZXhh3OKRdCfvXdBRVNphUYluFBkIk3A1yA318Vb7w7otzGczamXn7n7ow9Iq3srRhLJItrtozegqofKDCRI_daf7drdL-27M9Lbc_4PxGHhQOxKPOhQVqWoAIYCrUBMEgIuptRu7s6mB8kePMVZ0amtr-oHmu0z6uTjPrOkGNab5HpxNrW9H_QxkYaBvF5y1bRbTF0mM2JwDR4Bjbte-M4svHQAgNUiOhVMODng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCaSs8s1zWhRnrZywXzatnxyVD1GudSvbi9y9r3s0WY9_e641n8s_bNg_9Q4V1S2D5PWBgCqc41ZbyPAaJKLHOVRxFGteQZsL_STqHDQPcAHR75TW0Rx9nKCH9XCK7a6vLLto2OzE8Yvsd_UAc5E291AbP9vWUwNSB4-p7H9HfUVhYfkfrUzERp7DQytsf1xYQ3v9UuRDUXOSuL65W9hhApDXcnwymFtqAbSCsSowhXYxkrRivbGia6SABQmG_Xy7y38kCg42a70FFhhj1ugkN0HfOcZRyJUMijAC2m-5bCeZ-u6Jw6xULPuWJ6RpGgDx2vT3dA00b-HC3793-dY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=aR_-WXYMFjfubqpl-u8Cm0Lj5jYnyD5QkZaTDUD0058PkHrW0M0IAuHoPYFmAXLZlIU6RyfUcHuxAMb3rgApUChQMSRVARSOuGg-Heyiga11TOTsqTcvZs9TfGY-KaWwCkmbYylYbjAwgOwfFTR-L2E2fpgomivUWplIiC_VWcrNpAHtW2ExuLjHwuNSMqjMaD76LJWOwKPF_HfVHwVp9xLeK-bcYram2rnSHxD34OaFnIOGvmvtp8jDG-zIPYvT6zn42emUclcHsJIjdqF7RVJiDksQA7QRWlrUtryUdG0h3sTfWP5X3oyb4tdXy_SzF9msAUVqPyQV2_mz8dR7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=aR_-WXYMFjfubqpl-u8Cm0Lj5jYnyD5QkZaTDUD0058PkHrW0M0IAuHoPYFmAXLZlIU6RyfUcHuxAMb3rgApUChQMSRVARSOuGg-Heyiga11TOTsqTcvZs9TfGY-KaWwCkmbYylYbjAwgOwfFTR-L2E2fpgomivUWplIiC_VWcrNpAHtW2ExuLjHwuNSMqjMaD76LJWOwKPF_HfVHwVp9xLeK-bcYram2rnSHxD34OaFnIOGvmvtp8jDG-zIPYvT6zn42emUclcHsJIjdqF7RVJiDksQA7QRWlrUtryUdG0h3sTfWP5X3oyb4tdXy_SzF9msAUVqPyQV2_mz8dR7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWIxAEuIGhx-ulHzCmS8QzeLyZXweJ_eN-7DrH0WrRriadLC6Yrkw9cy9NLVA-eh0NgeROynvMt-g-Vt3XBZDbKefFnzLtNGMKK3SvTeT41X7oZtA7YB37WBGPhMYz0FbG9hyyMpqXP-OoIp0gVZppCtSugUQojemwK6dDW-NxeFy1akgPHHUydN2Ho2qRAn_ynSPIz80X935-cOQpflXNkuzUFMXqfUDtiHXYW6fDubabUaZGkLOZCevgUijpUvyQMxQZuRFwzH8GJhsp6Za0QD9-le4Tl661aNQwiVUYY4h9GfJCbOn92HRkolMSmT7avm99nM7d4gAoswidQt1AFhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWIxAEuIGhx-ulHzCmS8QzeLyZXweJ_eN-7DrH0WrRriadLC6Yrkw9cy9NLVA-eh0NgeROynvMt-g-Vt3XBZDbKefFnzLtNGMKK3SvTeT41X7oZtA7YB37WBGPhMYz0FbG9hyyMpqXP-OoIp0gVZppCtSugUQojemwK6dDW-NxeFy1akgPHHUydN2Ho2qRAn_ynSPIz80X935-cOQpflXNkuzUFMXqfUDtiHXYW6fDubabUaZGkLOZCevgUijpUvyQMxQZuRFwzH8GJhsp6Za0QD9-le4Tl661aNQwiVUYY4h9GfJCbOn92HRkolMSmT7avm99nM7d4gAoswidQt1AFhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qevXD1vMaVYZv2RVItChur2Uig6zBSPyGOlLMcfgMDIncUgp50sXBmQWNco3_f5Im-SU-AqrpfdyENbWMK5K5vygRNzvCGFOmGfPrsKK7CeDMi7OlgJuCkjDLdfKMku3cVk7vTMIb8wVmsxk7OdmGYMLZybRFk0V3R-18VL7T1asR00nMx6vU5qfXmFm5QCngGG-Z_WY3GrtvXk8VbkFGz7MziRc48UKLxp_3c9h50_kHl-wWked9iv4-zP-H1j3UsaItrhD00eikRRBNMRs0UE9KcbZ5b-i0XssskELbVszB8uKnHmsu1s4bWlibIxYUZUvDqgBuGZ7CG4W0QQLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMSzqVMxKN1WAz0fjyH_FRfxWNpd475aVpCxakOPDYSm9ntsXSMXz7T3AqWfOIKvaPaebfORivIHDbJHC6RHJ23KqObF93hpSBJavrE5BrcGs93_QzkhB_hVi-qo3vrcyST2MW0q8NO0tmMW1uFc5qzkwGUovYuTz4Nj37hDrUZFoHNOxfe20mLK9qVyB6QAd6Esu2McX6cUkQ1NKeaGSo9Lq-DJDMePuEzHviBrh2lGkwqeKHjtbRFZR2qhLzer4Bpxb4hCnNhS31Ly3SH0Ymrp0vr2pMkKvFi1eT3X7c_lKqC2LWHPIukhj1Z1ua6hb4rv1f4JMh4RL0uisTGYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf0bdoF0o0ZAmNUHI1o98QJuR5PbXUAvr2pu8yJi9xsfMC7ImtoniLdOJUhzwku-c4ymtnCqlHrFxhqY2u8MpO9pqW6eqdocj4qFvsRIqcojxf5baCZjtB_xJKha81dxD9-Y5Qr4RL9I1DqlCAfyo3Ggn-ukOCwb9sOMVHHGTC_p-JADCydUt0oWkCwYxyKJDWmZ40tDxDr2mJEHPxDL-5fM04HTVTv6tn0cn-HPC_nbuFl8O4gXjJ43iQ_lT63nznlN3jKKApbx_d5Hq0A7EOHOhfIHlAvPhw8bkjbVVl8P8suPuVGuczLnb-6OiXLHnEwRyDXYgEGdKaQkzYg45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJMvzqGnMc1cMqc9p7cFCzPbsxrafDkXfPZcP1ko5FkyW4DcCctziZyXEtfqPX6QZSeIdvKF748nVx6fbAwfe562MtoRVPcAgUaDd4LOFNM1yXN-fXleObMvr0tkpufezlngcHV7cdkg4RMONf81QhoDxDXoZYYwg8p0ogpuPgUB35Q8hlaZhLHP_v6BsiqRrkcbJMeyUVI5YpeAdEvGdC1jtAbAnncjVz0QSyvky2p-mkKTz7jiTeBKl0F_Q1NWzFHAVQHHZiGRDvxLgpUvQzMBLA2pziyMCcc2dmk5E480So2lcmnhl5A2hmcO8ncaizr68jcPvNsBka83sio7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8SDC-6M6WZUsO7caULZoB4QNfuA-xUC9leIc_E5CgUFowDZqCuLU0JVTGlE1LPOiq9Ny6j6qrS1-uwh_0o_RFF_wAQk_0ShzvZYKsLFn9EeJOUE_pSNly7f6aUf4P5_PREAcISRTx1TOR1GMtc_udH-qiX0AJ92xnQ47udwju1GGisi_CuArrE47p7S5GkW-lSqX1GG00X6ZKpHbAFbtpn_MPi3Ji8TM0LZLmNnwA_S5CDZ4Y3AQWt0IpIlNJAhLhpdPuiIRdhSoMGiJHIjynmpd827eeNLOlGCeJayppzCghzya5yVwqQcRinNPB47AQ9pYMzMHOuMsWS--RE4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmcMU99byZ9xVVYn8TLIb94N2GUgO4lsUBI7C0u7tQB2K3G703KLLXGIOe56w4c7-Qg5ZemYjWhqinNodVVsP2TbLd8zR09tU0fewk6IQRmeItRdwv6CHnJG3VsHt89x0rh60psfqoxGANJALtSZVIAETV7UOw6eszgFXAmOxR5hxzZpSafN-sW071SZeweD3ue57hEk6kcHkbBfDQPWUhadLwycihbF22PmFTVp_GgZ-kISbYD0SHtJXw8vfpRfUyWsbvN1YXVHUPUnnC4UbX9CzqZEujiBLt13RI2zmxW1Zg8IswaQwOsl-YnyOh_PXWehb-8Z2k0u8eVVlABDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=OkvhaVKfFlpj4Jr3WCcUKV8INKJUXw8MJQHKk_zrt0a-oO6Lh9uV77EyWTC1C0a_0QSmUVuSmgjRWapq6fD72mzlJZJJXlLcwQcyXBy-3oAyI-Ez2eSZ_X5cj8NX3x0u7n19a9qTGXLMASutdK2WmvaOCFXJRg9_ET3FJ0m6E_XrqbMzmLgUM-tz68t9QBJ_whkbwvit3o1eyI33uHLHwBgAGBzwwtXzItK6bxzQRay5fLW6Erl_g90IvRgcVbgeuVoiTQdO4q4dgEJCSA5J_o_Y5yq-MXPEL7nIZAAWVRUOTbi00u1B-x76-Apge5xCiFzIYteKe9gZ1K6NcCd6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=OkvhaVKfFlpj4Jr3WCcUKV8INKJUXw8MJQHKk_zrt0a-oO6Lh9uV77EyWTC1C0a_0QSmUVuSmgjRWapq6fD72mzlJZJJXlLcwQcyXBy-3oAyI-Ez2eSZ_X5cj8NX3x0u7n19a9qTGXLMASutdK2WmvaOCFXJRg9_ET3FJ0m6E_XrqbMzmLgUM-tz68t9QBJ_whkbwvit3o1eyI33uHLHwBgAGBzwwtXzItK6bxzQRay5fLW6Erl_g90IvRgcVbgeuVoiTQdO4q4dgEJCSA5J_o_Y5yq-MXPEL7nIZAAWVRUOTbi00u1B-x76-Apge5xCiFzIYteKe9gZ1K6NcCd6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
