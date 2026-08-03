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
<img src="https://cdn4.telesco.pe/file/azFqCb5rhu4rajNTvdQWqWIh57YGVJnggormibUFLIVcRr5B11uSjwToZjq_8MPSlrjgy3zWXX855umU_kYlNwJnvKE84xiYsuqSDG5X0lsA1CuiXmpg32j0Yk9m0TpLPWM6tABfu5XvGO4Qp7gJLhh9DO9zKwf1ioEH7nVbrlBhTVLcnKg7dQCpiS6pF7VkXYaOwsIIVOVYjRwnnAKbQKyJoYgRWayqWiaYgVV0GFh-rprYTjLTOn3-mE2M2anDOeS0-nYvva2T_PErlwj5WhKKL14rmJcDkk1-Xn9gFRJdDpdTJJ7-IgvEpS6l7kN_afTr76B3oC3zK-_G6v5YOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVRrG9l6UonsV_OkXTiu1wEtuaQzUdJ72BGTmT2_FZSm9JTy4_nYhLDuxdQ9FFCKBfJur9u9uBdBnYXTIrTnTc1q1n9iNKMZ0-hxFScr1l96trB_lmlwgyJSGfAbCXC5NEo1Z-YCCJ6-Sqd5cmnyptNw1Wqvf25HD0XXvvglgELLVs3zDE7z33qtaEXHk7GFiYbUre77RP_-PKfNhJ5p4OxZVMCkbJ_n3Mw9H-H_Gv7Nzf7Fg1iCXR7zasIiVBzcICIz0WbW910FZQQRE-HRbRgNtWLjZndaP5A_KePOPFuq8V7WSwUTTPJS-1QBdalwMNr2m7qC7BJUy5jEeIOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.2  پ‌ن: بهم اعتماد کنید و فصل چهار به بعد ادامه ندید و ولش کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/funhiphop/81740" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wHA8OeN-PDueHYVOR47cviHQLw93OQSKXw1HOngfVC4K6PQbZN9hP7iVPdylaE7nnKmv1wCGll_pVigMrSQwCcyph0DuO-UEwRAo4dUN8P-aGvk0ijEpOtWmYyTw1f5J8y1IsW1501uZRjJmuTQgkAhpXrruTjHpGfoHW7ZiqrK40K_zxrZighHlifbNRrTUAh6APTNbGJRK-7c0cUiyb-MkTOzuByaYqmQvftPDK3TfFco6sJbhsoyIvEpV5q7Z79ZueGolyqXgDdxH4GYxQLXLCl_SQunj18q0ufj_4q8tswZsa_L2COGSYfNScwoirMku0bKPwClH_qS9YQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هری؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/81738" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlGJotRqsS_SGPiIm2ZD2TjKkISQvUseHK5CjbZF1d2sCJcWpHPYsQ7GJI_P4qgcRxAdpUu4LLCMXKVlRfqeuRyWdNQElvnWfwMcsUcFBj3YO-JV-OmPUwn2CQ6BA8Lrmc_O63ZTVphokC0JUw2sP1qegQyk-FfvPCal0-APrBtl4r6AtMtX_96MCRGvovT1uhsXmzyWkdEgssnXF0sgQBaYl6Jav6DBE5f7bFVZMREbWurGAg5q0kfC3qboeCfHYxBCxzjpkwsTvlpBW_MDvhLC2D0nbS7u44V5hL9FVC4tzCvR7r4t8V0hov4CP6QRGQrVEnnVHk-A9w2VpYNmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای تعصبی رونالدو و مسی و رپفارس شروع کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/81737" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحَسَ</strong></div>
<div class="tg-text">نشور سفید نمیشه</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/81736" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maw_Lkp_9OoooBRfbbSV7Vx3FX0PZJPqRJJJOAYQuOFgtQqATOU1uUQCo8pJU21pN27m0RiSQgGhQ5qCrqHSfQKsKKvBnbNyAqQ6-7brXooTDTgum_b08HrTAPPM5B6gTdEKmoNvJeb0N1IoIrCqjaYLnMJbAYdKXSuD8iAzewR-gqjAz2ank2rgpoA5wJ6O7Ry8D5LXNShJiMA9c80a3UvJnjiWWgRd-4YdJJ-ckaNBTlkXfKGyaNOt44yCH13qXMV86EECO8a6wQTKcqvwV1PONF2gGrGxUCQS2bKE5Z1SHjxnBDw0-3VRDcNkxnDaFYZrA0zPzHQfo4pqIeCLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوس دختر وینی داره پتشو میشوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/81735" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ9k-HbjGASIPpG3aGu1qLrXqk3anhmt_kpJToByk3owvs9nanMX5R2xBhCd4m0O87l_1xVKpC_C3nHAU127jztHSzgH9JdyOYsZ2rrpUJOaMHNilxEnDvj5z-hZ0bIhIw45Hwld7F15FQPrlAYxKeMyvnWN1wZZEmAVseUt1IcuJbt_SBYEKdrykqnIUM2xugTzjBYMiDbQ0ky028-i4bgwh_c-lg_4-nGmuVEXrxf9vXaXQxVfFC1Z_7s4_ZMvIMK0_oiY6cJRQomnSBA53_n9F5POegWzSDFhEegvIrigp9B5Ipil54uLNJ_ExGCrYUszfQmhcquRaQIHXZjvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/81734" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">-خانوم جورجینا ایا وکیلم شمارو به عقد کریستیانو دربیارم؟
+عروس رفته جام جهانی دامادو بیاره.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/81733" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qQJbggvJEzLCm0n76OsljePD2AGwUbUA-cMUKGXEBFc_ijxElIhYYUettpc19re5BQfcjWtoFVDVAPigSD6Lm_saq_2AmAqcl90YKV7RirtEZkeNaLSwPP0JmYZfdx-m-fTEaUKEfKDu7fJO5QRleYEx18Ysy0DZDhUP5r3L221Ut1ILic8HIYJedBLfDhf-RzqcyTDiwnlhOpS-6tFNLbycBUT4T_2Xph6np1aC7P6usvF3fScCMwaylDfNtTOnr5U6Rr4N-qSKb7lNMYnE3GLgbsyBO_LFwpWolJ-BwaBhG_Lc9OkKdHRYgpwmbcB2FcegKg7vpN79dOGnwPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش هنوز انقلاب نشده ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/81732" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خفه شید تلخون ترک داده</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81731" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه
پ.ن: خدا از دهنت بشنوه اینا باورشون شده قراره تنگه تبدیل به یه سلاح خطرناک تر از بمب اتم بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81730" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqPzgFd9ZZVPoZa9iDKPXhSrMCr0odhMsHr73dYyx0CoJdCwBx77k1Ms6nN1QXwVFfkmI7NwstMron7SGpAZvQCEWwxcgNuUwXPmz_XPBh266AQoHCwQ7RcHnjocHZXi-IYowUn9TKJ_pGbBy9MDJvs7z-QBZnTqvQToO6Mb-LTy-gDez92GZWTjhMRESTIZg8A8B5ILRCwLoLILZSOaAzfx_YesPOLuFjjn0PQ-xpwckWo3aT6dq8gHy8WOc0-3QxxtqxfNVSZyu1zU2iq-Gn2u2SuSEQJp9KKzEqFXSYrdTeFU7idOh2Smr_VWN9l1Vw_K7xsYqb0-HJN6qLehQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر دردناک بود و جانگداز
امیر و رهام از هم جدا شدن و گروه ماکان بند منحل شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81729" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFXsyK0nyqw1uJxG85c-vrQlXmhKv9Uf8D6_7ZwP21L_bvRvSm-jaHGC_wtdMzNkpk3ugi8ut_jrL4qEUNyVjlLEk16h0VauCP7VoG9uLwVNhPVIjVC7uCXVC8RHB-9odGyrB0fJuz3oHKKASpMd6GxS9D8BuDb2_LoMRpjI0z6jCv7hcFEkZWLuiVtvVMKfnl1RsAiWbFcC5PAPze-iO5JTynQgG5Nd5Ca4o3Ukf7B4GQsazEZlyuz9a3X85DQLWK7bv6LLgZGkj-baGk6BupB4OsE7LgRF_lSZX4mmV_yJVnL8FQIgVNcrl9faXfpHdaMPktSVmUU2vnuK3Tv2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترک چندوقت اخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81728" target="_blank">📅 15:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81727" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SekZmEy9hLUk_Tz2LSo6bnry88hN66eU2qRszMtiOmXsO21K9mXyUl_SJopJdQmvCgPfWTYaBnKrc8-1Pp-G248FipUwZY4obJ83OqsFFPsrPJN8t8sPvQY-DXY8v_W0OBCppBh1sbCTbdv-r14hP3IistPYWilUw8gIONkBEdlX5JoGFfIp7Ql3hTL6uCSzANxAornPgsTSpfSIfyLviuVb0vfaR5wvHqrCtBgpTCzEgoiwoQxohJGJlcCYQL8VpcNa0lGSC-Hgo0z7kF27_BkEvLuSdjsIFPUnAcIxGUxMrfxAUZRBGDpCFYeZ35Sg-y2lXadd0P_qu5C48kcSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81725" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هرچی پیج تو اینستاگرام میبینم به دستور مقام قضایی بسته شده، وقتشه برا پیشگیری علی رو دوباره ادمین کنم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81724" target="_blank">📅 14:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFy3pacGAADUFRSBpH14JJ7jVa06UCfiYv1Hd2QZEO_s6EU-ozpjvS9fd_wwmgFYMgKuZEWhSIEqBejp-pLbekd4qiB7yz1cUOOBq_YBD602lTXrsy2_YUHsFB7vJYVVmQ1ffce__5mtBdtojAOTvmGpD6zQs66VaslmKXeI955Pe2FLbfjTUWAkN-jJXtbvLaajqBwnpKZd6VLd58f_LFqu39ZPpb5pwHFiUaGIcjG3Go1M6MJ0Wp7mEVe3FUsHQMr43kwaQToY9hXN9Zn8yBKrhmAp1Rjhf4Rb6_YFsfFSS3pUaQx59SIcu1tauZq5_YrMF-DhzbEt7QFpx4z1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا، حافظ ممبر های فان هیپ هاپ باش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81723" target="_blank">📅 14:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">با این حجم از هواپیماهای باربری نظامی آمریکا که به خاورمیانه میان و می‌رن دوتا احتمال بیشتر وجود نداره:
یا دکتر عراقچی پخت و پز کرده، توافق خیلی وقته پشت پرده بسته شده و آمریکا داره تجهیزاتشو از منطقه خالی می‌کنه؛
یا اینکه دکتر عراقچی به معنای واقعی کلمه پخت و پز کرده و آمریکا داره اونقدر بمب برا مراسم بعد از مذاکرات انبار می‌کنه که قراره ازمون یه سری یاد و خاطره و چند تا کلیپ فرید کنزو تو آپارات باقی بمونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81722" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTc-Cl2S1QDOFsa-lKm6GaEXuTXxMOCxS2ri-a4E8hoHF1Eh62142M2AvXMBsLx86m36gmeA8SBFs97_EoN6qgn0cHFovcCFGCDAbrIdFviBfnZb9535DcO5zhtRMNwwD2poz1VwgeZcl9st7XzR1oouLHOE1U2pBzuBJi1QTpT8sNHjtDNE3JiUNOfgvBtAK6cxsRp-QQY3umwR_sTj3pKhxevjuCy9aXRMrPopOuHwpCzGy7gYi42wljEPx9WYOR_gir9cOwUvwhR-nQ1SXVgY8uVRWoYbQVNmpdxAPOvcYV7pZrX9UeyyCi6t1qYYIE7S2exiwtr-V6Qc6-gRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره واقعا به چه حقارتی افتاده بنده خدا؛
اگه بچه خوبی بود و ایران می‌موند خیلی راحت می‌تونست مجوز یه کنسرت خیلی خفن آنلاین تو لایو اینستاگرامش رو با اسپانسری دوغ آلیس بگیره و برا هزار دلار بره هیئت علی ضیا کاتالوگ فیلیمو رو پر کنه نعره بزنه اییینهههه خووونواااادهههه رپفارسییییی.
جدی آینده خودشو رو نابود کرد این پسر.
💔
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81721" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسایی زورش به مذاکره کننده ها نمیرسه هی میاد فتوا میده که اینترنتو باید قطع کنیم، ولمان کن دیگر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81720" target="_blank">📅 11:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=BO9JKumGrDzImfeo_4RPNOlvUkMM7xk-xsQhlB0iLcuRYx_bBLfbj_srTvSsGzWpm-hLf6K55F_4pwHLDd1C3sJ9Zem3MJepxFR_r6vX2LKBP3gcGLJIrfPNJWne_cEp3A2_orHKBfO0MOHKR2L3wCD1NFUQjvBVrtZmqN7CiKvpShzPE-x0Pu2bT8LHD7R_hMJfTpFZuXierpIWggsLxPj1eQT6Ud7xFrFre48Cu4MHSY223IcOABPS0qmtYr-kazJ2MtC8ujLE4it5ak3jFXI2geqpeXReUUIWvjP3Kn_FCVX3TIvXmDN5faxQVbiv8U4Kcrb5_qeMjdevqb7qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=BO9JKumGrDzImfeo_4RPNOlvUkMM7xk-xsQhlB0iLcuRYx_bBLfbj_srTvSsGzWpm-hLf6K55F_4pwHLDd1C3sJ9Zem3MJepxFR_r6vX2LKBP3gcGLJIrfPNJWne_cEp3A2_orHKBfO0MOHKR2L3wCD1NFUQjvBVrtZmqN7CiKvpShzPE-x0Pu2bT8LHD7R_hMJfTpFZuXierpIWggsLxPj1eQT6Ud7xFrFre48Cu4MHSY223IcOABPS0qmtYr-kazJ2MtC8ujLE4it5ak3jFXI2geqpeXReUUIWvjP3Kn_FCVX3TIvXmDN5faxQVbiv8U4Kcrb5_qeMjdevqb7qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی فنات دارن اکسپلورمو تسخیر میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81719" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCm_LmPHbIcNjqwcPcsj9--6ENW4ZuqfE9JoS-Fleg6j_C-jyYxTG7Mc5G-YLgRKCvCwtusEAYvHu0gbGNIqchYTCOKIoDeIsYTUQBP5LUperWGt76kHxwPqnHAPIb2NZn_yhf9lQkCaq-qfAtcro75bBdwqSYTHvkPPcKOWnkoQ2op-ZsPgy7HUrCtsmEXdkVrr_O4FO6oSYYSvKHD7yCVttFVL2Y7lBeD74I9170g418PgVQiJQ4geBZOlBfbXxPRMYj_u5uVV2gj0_1wRPBxNLIsGG5VHCgcGBWIn7V7Fj4J2puNwprYjvp3WO44SzRomrqJE4bZpSFYwiIMN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگولیییی
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81718" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=uirKmYR_OpJyRFqbtcKxoLJZ87ek7Cy9yibcAj-j5tFquarEi4aSpMrriKQzILhE3smpx48jLsPwKua9PKHaGxoB_JMBoNZNGS7t5ZZkHRbjmW3vyBvdpvmVH9ijRwtuwsDCBrMkcfRhWgZhonzII-RzAj1atej4iNffZK96m--JbXefdziTGnzJ-czdZVjJgkqf5xAGPwPk_7thZUsXvGgOGVH4S4Xqt1UrHRZKo-lBY4Ux_qRHN4hGbmY8eIfZenYB-6LQAt6-SPuNfqvnON1mYhG85hJ_FoTZC9NNDru92u1acAygL016-q7EMjGxR7lerPOEFh7XkUWZnyOAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=uirKmYR_OpJyRFqbtcKxoLJZ87ek7Cy9yibcAj-j5tFquarEi4aSpMrriKQzILhE3smpx48jLsPwKua9PKHaGxoB_JMBoNZNGS7t5ZZkHRbjmW3vyBvdpvmVH9ijRwtuwsDCBrMkcfRhWgZhonzII-RzAj1atej4iNffZK96m--JbXefdziTGnzJ-czdZVjJgkqf5xAGPwPk_7thZUsXvGgOGVH4S4Xqt1UrHRZKo-lBY4Ux_qRHN4hGbmY8eIfZenYB-6LQAt6-SPuNfqvnON1mYhG85hJ_FoTZC9NNDru92u1acAygL016-q7EMjGxR7lerPOEFh7XkUWZnyOAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین علی گرامی، پدر تشریفات ایران گفت اول تعارف، لطفا بگو الان کی بهت تعارف کرده رپر شی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81717" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdzDLfI6QrTUtDbwaeSbUzsj8aLGsiZV5JxRI5PgJaomX1H6kF24fg3MILV2_ulcm5YgmnYC_ESZ_Yb6KvPoOvAmtqkdPosQYVblpnwLsC9wppNvMFRmCr2ZvRC1s5IyC9R4XGj6EnuOpa2vOz6IKst3CZQN4sZXACuPcbYV4b_PP9zx566HIGN8dxhmXFwooaw5uDSN54hgKwKBmNfl5z0EP8680DRXM52zZzvuZo4mStErQOiEKKaUliYks-FAeePOSqIVLc3OToRzqAoXkE8mW_1Sl69JZxCMxKavEvvH3KtOOCGRaEVdzqeUEQOJBgLkck2TH2YaOzvrvUeS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81716" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امید بهزاد و پویا صفوت، از معترضین دی ماه اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81715" target="_blank">📅 10:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ببینید ترامپ چه روانی ایه که لابی سیاسی یهودیا تو آمریکا هم نمیتونه کاریش کنه، رو اوردن به لابی کردن با کشورای عربی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81714" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: حمله‌ای که آمریکا برای ایران در نظر گرفته بود، می‌تونست بزرگ‌ترین حمله از زمان جنگ جهانی دوم باشه، اما متوقف شد. محمد بن‌سلمان ترجیح داده به‌جای حمله، توافق با ایران حاصل بشه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81713" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIJVit3K-agVhLt5e9ySeI3Djs3ntV6bxPfj3Ml2LMvHNAWNkjBlbSs6PCvLCU1q5D17wUZh23hvXy_jHRKW3vXQuIkr2kMBJOlGNB1Qfc0QvZPQ9x3UkBzvDaxhR6o9AP5m66DfanzY-FH-Nt4N78IB_tu-k42s52AjFshev6uiwEulaYdBqJpTZ_YCxfHvNWbcYqYTSOVy7IcL1693AjAUH3TM-cdlzFLz_QHOE3YkSEytS8jHJ4gf77rVx2HN2843UmN6RI8VAwP62uh381GzEd1GnpF7AN6oLOtc8nxZY7scMgy9ZJBYOlguseqsMN9m8R-w8xTXCGH6F5Ye2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینم کاخ سفید این پستو زده بیشتر تنو بدنم میلرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81712" target="_blank">📅 09:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW13vuMbGF4ioTo1OrLc9cPs5xvQhusx-c73TWsRgqyvnowQU51yb4oECCfv2WC3boWw-Xnk82QtbsRXIhZAvB82J4i2f-5pX-UkyO4gqsWaUFyI7GLv2vAvKTyUaEuOZhlzBEIoxJyGiMCoEAJwzq7JewMBGg06gW5-Q_ZjozMFVKVlUKbY7CGm_H3gvZ3KtKcUxOaPRy3XOf9BUrcfxW4c3pBtl0gbdOfmDOeVTh_nU2wIM7O5HeO_ETr0dPgtJLPX_IEpZnr8O5Q3_42l3KNatxd18ft73us1Q1U96FUiXAgNsS3XNiDFHBJJZRVZFuyqI6XqZxnqFjJMLdg-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام نه قطعیم لطفا آهنگ نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81711" target="_blank">📅 08:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوررررررررری
آکسیوس: منابع نزدیک به کاخ سفید تایید کردند که تا دقایقی دیگر ترامپ دو نقطه را خواهد زد؛ پشم‌های زیربغل و خایه‌ش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81710" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81709" target="_blank">📅 02:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عباس مگه صبح نگفتی تنگه بازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81708" target="_blank">📅 01:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81707" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsApK5Gp6I_1r7F41YOvWZqQsFxAbNM-c24QB57h8kV73LQqwShDVaQkQCKuWwiuG_PHNWQ2ON_DDD8CBXUwT_0bd0w1O7VFHDG1BDaZkdPHuo6uWzB_yPeslag9cOndIP4FIctSNwWXOEYZyq1bbPU4g0OQlF4VYX77CC0FGvDmAP5zrqa7Iz052jZLQRVQEuZaCanNfoku7uv6jFpVO5vxj_0eegJ-HVGqlJxoyeGa4sW_SOL9D1we6odlCr58cPAYuxctq6rnWthquGnA_30HXPCYHW2IFbODnvveXwbvuAJuNY99Sm5S5pAb8NoppKQifygB2w1OIXSaCM8ZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی کصکشکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/81706" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adGKT64zDj-QF-FtoEeskPI6vgLEUprMBfl5o8kVAAAB9XvJPJsMyxCGpXjjlZbpU4e6Ox7K7TZJjdOFbuEd_zxDopffXGuMnQza8gtuF7u94PzAVZRFHnx9RHzYdiWB-weyUpMBTjvJOatUb0BZt6gk3eBAGViWfTiJOMcNIa0viNrYPmi2PoG_7LW9i2cDnX3M15uOh6Ecfg6nG1aKnP1FevQ-8TC0IpBy1hz1zRrBy4PMF5WE6lQS5vXpJdH6Ei2CRs5_Q0XVIMsJnwBBXs2lN-LEmms7n5jPk54Zgdwc808aa_MyGBttn9tQLjCSsfPL7QF1-nJaYz5L6o8Nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید راجب اتفاقای دیروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81705" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY3d6KV8UIquTATiRJE2H6h36tRXrDkhzY4TBhGsCrksJ5Byb2XzxpJb1BJOb-AJzQY9fcNcu5I47bcmGvl3Cxv2rWryEXULz1ii7bIM0Vazy6uXTP_0Bb6e77oPW7-_r4OPTLM6N2r8Sa6wZiyc50Lb-llbaa6X8ih3r4-Jhk89yT7f_CMtze0R-cnbUThAdk5Ebm_RpAf4By2epU2eZFtm_2seBMSqYVHMtI8-d6oTM0VPS_YpYtDDI3aQsqDDm0fWljrznTUmvN7lIONgVkmi15IUfqFDMYcI8y2rkjm2BxhvHfu9c5iGUtDy-k9YxuDjD6mNA7Hr8dA9SlmwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81704" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حماس خودش خلع سلاح رو قبول کرده امضا کرده، ایران بیانیه داده که نه توطئه در کار است ما نمیزاریم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81703" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcYpssdcbWYnMB9zJOAL_pMbZMQ8ja1vtNMBhM28E6aVgcUg4NPv9QjIqPM3j7CbaXKy9_4qkL4w6W11NRn6refk5eRN_dGp5v-Pi0ii2nXGLeZi6-tS6gO9yfco2wpB1QbgC4sDyNiS4Kr9hhsX5wZyPyxud3oJumnnyElO-1qIzsrraw8RXfIS1Uy1C8pyPts-XKYY4DYB6_aIyK7Nv4FG2DRbvAih5jLzDACJ2B3ulJkfUxGfDyxZy1Sh7MALIC_Ht7HWrXDs3m9j7VtMWX8zKK4je3-ThZWWTOeuOTnNYsR9ZiMC55W8iI90bgRaU-aBs4ij8uy1PfOZR5n8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی ناموسا ببین کاراتو
نيروي انتظامي تهران بزرگ امروز یه دختر پسره رو توی پارک با گزارشات همسایه دستگیر کردن! حالا میپرسید به چه علت ، چیکار این بدبختا داشتید؟ به این علت که هر روز این دختر پسر میومدن اینجا دختره به پاهاش کیک میمالیده و پسره پاهاشو می‌خورده و فیلم فوت فیتیش ضبط میکردن
همسایه ها هم دیدن و گزارش دادن به ماموران انتظامی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81702" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmbBqx_DBJEy-agq756QLO6cfCfrp-Qtt1kd4ClwZ9JxB7br4YaDhhTYdD_COWPJlvuFCT6UPDU4F-KQlHZsU6eLknVMirqG_QfBt1MbAi0U_BPBl5clBtNyclLPcrXehA1WFQE67Eg-BDfjycRamOaqjf5phwsFq8qVzim8jzj-JMXZ6DdmDtxp7-rMmq9tBegMQGXsjHC5RQEu5Ssm2WgoHaz6rVmIT5aM77PHe-Kcu1JsJK3kF39Xw-v9iFcz1GObcDkjf8_qwpUp8zddoMQ4_JCEvGu9Xv_NZp0AtSVGKD-aRwk_VJdeTJ1b7f30Z4XHdRaSBQuFnf3f17Q1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- زنان با قاعدگی بارداری زایمان و یائسگی دست و پنجه نرم میکنند  مردان با چه چیزی؟
+ رونالد ارائوخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81701" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل: علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81699" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل:
علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81698" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI_Fff0gaWFzZZ-HkQpWum2apCQSjKstnQZKbZqySc-MUraoEPyEO8gFzohLd49xejpVNP9QUX8rsXmcGdf3MdIouowAvI1AK5w1_2qNaW7fBT2D2HeE6IXMABRSdpjzCSJARIH-wDaoEEtr1dcRVazTJ-AXB9prjGaioOvAi9B0PGc2KCWDJCJ-ji2fdQnN8oM9CTM3f-cfHc2SFP0Vcra6yNKgkRrrAOFzKGeFCdPGpAVb1OLz9M811YWe431a5sCINov9H-Dfrh8zbs4ChU9NQnHFShFVuP_ywpMmkDQYYp1PjyVFiWNaqSv5-eB9PWh2S4gX1NFa9FmIKjxf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاس زدناشون
😅
😅
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81697" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81696" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81695" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_yqPUWON-kM_A4OmLV5P-Mgfwou900wlofEvAzgMNfRQ5mI_cxsy1z1fdxKx9xddeu9KhUs4_I9TS5ejEQ0D_7eJ46NN_VDodLtCL7eiM9SLNzjc3zFw2fq285HE-GMQ9p7N6CmCKSCFmDmurOzG9o4SatE97Ter9Yadsis9eH9bhRv8ELePMa6XNuYbjsahK2I0605bH7WKi9mEBM_sy72s8Z5ESni4YiaRvWlgz14RPema-BhD1EhCR-q-wNqt2BPW0oSOPOD7xw3mFknSvdCksm9PpDYV5yhHUlTb6k1VZu3djD9ZAZJwqMWFnel6F3nUolLzeoA7hXS3ryrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHr4E9J2yV1Rj919vnnw9wMj3QrOv-UMCpdKdxQHo_uYzssOaoz18sVud12DWnDktSpMWMCb13CtpMDpgfmjCJczrvf95vEYvsH15iMd5TgVFaHFF0uPYszwvzaE2_aSYIVfsEJr4yhpIG0Yd-fO3D2CVkW2qfvYWjW2iHsDKsEPjJjJiNkvGp7uUJM9GYYUXMtNom3g2F5HnVXoPYWUmcjRQ9mho8dtgZr-H5I1qeK0zsLhkRzAc-hFG9wGFGRpeS26JU73O7urSIdhsozsJjYoHiIIHDmnOEFecCoSI4UVVQAqhk3KJHvUeq6E6LHqiF8dNsppVbb9bkvO9rGDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81688" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWUcFPXn2VRBV3I2k-s1wWKoZwmi_MXQ2W0DY4krfX3H03eGaKwdXpM3pOQvZp4HJHF4kARlPWC2BK4AaMDyTRV37v0uNXrmXIIZz5f_C9N7tCU9o0o1YitbEFax7j1UXV8JD024g6QeNMdjGfLUMs5cMQN-G0AYMafj_4U3pUC88IzyDad0tS9VA-tGON92yWMc9fl4FoxDBuNmsaSmYgizXy5PArRka3JYS9Ftl7-PV47Ew0o2AQ75j5X0vMFXpoBuqY20uzfQ0U741qGKgUzgVdBzPEhADWkuIOgZs1lGEzL0TYIu_vBkPqAaTrjPvbUtG9nYNgMpe2pBvh6I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81687" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
چین میاد بهترشو میسازه
چین به عنوان بزرگترین خریدار نفت آرامکو، قراره سرمایه گذاری های بیشتری در این شرکت انجام بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81686" target="_blank">📅 15:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Sbeobv1Sd2XPr9TwaBhEup5FPrtE-MJpbZJJpepF1Kjuq7rNt4rab8q_s-CjvjUydOcR4sngk1GxU2RaEaKUPxjr6gQ86VLuiyPxvHwIxoW5BuMc70YRWR2Aux0qUyV0ZoDclIENr1vNtQdGGM2K0hRitQTEWd6_nu_ZtGWtXZZAgl32JsMTBekiZrSHfY6IwvRb0bSXmwBf3uryaOo3tIWM8J6zCAOL33tJwRV8W9pIbVScQgG1hw5qJqJ980db27SqSFdORccUAuDT0ncrmw15rYG5vkt66vx61svA_X0AwTRlN6QBI2gn5ymlNTrxQ3j1mwdVt3OsKV9B_Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگا یکی ترجمه بکنه چی نوشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81685" target="_blank">📅 15:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81684" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
ببین ما داریم چی میکشیم
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81683" target="_blank">📅 14:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTqeSP6v3SWZKnw2MUJWwkBOeZKExHvPfzE0F2kOYAqEBnodOqHa_sq_Oirn_RoIzJmcd0zJTsIUPkyaHnvvNTLLllU_sh8XWCPoRwzfOJ7mPirSki-9rCt_e5ltB134gz3Q08MGI9N6oGBnzWu8JQBJtm7v-u_RgimXFamWSGj2ON7tTgUjd9z7vSnepB1CaPA2NMcOV19EnVs-Vgjjf3j1lqgXw_GHMXBtnjOa8ziOIf3hNWWigqN223gHxJf4kfjNwi53alMHAhmCh-DcQ3_uBy7wfeg48vhOtq-Uc-i-k7wJImfgRCSSWuxr1asca6x3GV6j68bRdab0NmYrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم قسم بخورم کسی پیام بده دارم میگه خب تو پولداری ۵۰۰ بزن کارتم رفیق شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81682" target="_blank">📅 14:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فارس خبر بازگشایی تنگه هرمز رو تکذیب کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81681" target="_blank">📅 13:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خاک فرعی مگه داریم</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81680" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bx_pVpyfbClmzZxg3XdWJ_JjSSbwJNpPsm2um36mBz7M9ygb0mjGE5K0RpOVbHn9fhY428D1pRXPJFuHIECQCXgjutIGYDH-orgMnNRv3PefmRSUsr9iQ1DeokDTNUZIvbZgEmwTqc4Frq9JkpIIKUozuBCXV9H5pnF-73D-j2xll_nJWlpCPeBQNJC1xQMA-mrzW_Jb37px963K1Z3Cu0TqIZ_CvaRer07ExEn_wAuFhsz98yCcs_DdYsR2kMr3rzUHIDqeLtLxscbwYv8SEwAGQUZYobn1nOynGPMaWosd_pLDtjVYyM0GcJZBNkiqxnqm9keRYXwTgplnnqvtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMtajKX46B4KI-BHazmiKC1oQtfEyJk7CQWsOpTe9VhUJvdXRaQVNtSIwtKZqJhE5MdVoGeKuvrDVq84TrzgvTVzCh_D_ehTrm6gBfbIVguDg5EdnjgUyBXhMShiyOMRzoSEVazY7z_DDvSyy2LRxVrY2V2JZnFyZVgEeRW6aGlKsvwM80GnSYNQwMgNlmYVr_pRLwbzfZrxTELZfsvU2Xhbhw0q3tWmsIbbMvR6kvFk5HSbUrGb1TJDJubOGkdokOdJ5zA0A1y6FVCPhun_N-uoXZZFHKw3wkESgQV2mW_xnHDU7DWJMIFErkVm5b4GeF3DODTanQsAhHF_-KXIaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسریا کسخل شدن فک میکنن مراکشیا به خاک اصلی اسپانیا حمله کردن
شهری که بهش حمله کردن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81678" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et7IxyS8MwplvryPX5VfGRfMdKxU5Cqo2Rm-mC0nJlbt4KymwlDlacix8MP5qN_FTXzEuzCldUc8Ws0zo59peT0A-3KIpUXRcmePfAGI-mOp4ZX9mTMqQNiXUGMjBIfrg3odnFy11dqiR3UbWgbYtQ-fqtrNu0TzXXyL-4VFlrvEaPDROwSMZySQD15MqGtbuXT8123Vx__j06AmtZBzJl24fyNDqBMlzSI0amQQaIZZGWF6nOXvLvhSBi2_WsRB6_cYdPkHFwm6XXAaqYBx7p_TpAGaje2RdniuE1vitAH6chbwOjkWAPxdEUSQGzNxgZAsYXjrutyzX-ZTKUKXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81677" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNwxhaQxcdk4ofcKATMAXkN3euMJJCkK402wv400YGXhkLqRTmu9YK1Dmr5OFhwvxD7cxkLIZHiSSv4j-y89rtUxmjMfWHBHTafom6VNZRos3PiLuLPxEF6SIMHmyyNyIFns3Wvn2FVq-INsus8JVTJKjbM8oBpkdjMU9c38i3tS8XDzZLIGo6RSKNTw6JoTq1Z8w_3v5PgDAQih-XA5Q0lJocyVFzvvE98cbhMIH0f96QnvXuEDiGzo1IcfFr7b8A_lceFGhwErqR72esSgst3xTtrb7Z6I00VNJYYZhetEoMrvnUpyZA0Iye_biDKjDamTrJMHka6YaibEgjKlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های یامال درباره فان هیپ هاپ:
اگه چنلی بامزه تر از اون پیدا کردید، من ابرو هامو میزنم.
#Arash
@FunHipHop</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81676" target="_blank">📅 13:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYv-zreGFG4-_vkpLkLscnhYFAs7t5ywp2bYjK2CrpTy1Hu5J4aiTgYsdR6ONBzKcq7U8j84rHdbPSxj-tlvacLUm5aKh25W5IHyJv6Jj9XwaL28yIe3hDtInxNMBSonezXDn64tJssgJJgqLTsO1lw2FF_l3684X-9mqkpqVcIyaQjuKBk0-uKytJUkGwcrSGnxzCuETpmhIjFKfm0kQffGGb68O4e3GqB5RjfQ647v7TyStybAzVt6ieyztsao1aOj9U3JwQcH8Q7f7i6UIk40y5PfEwMKk-gTzZKYbo09hXTEYFgMeTxZEjeqlD4SaO3AKG78-d1qtboCPGXC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ اسفند، چند روز بعد از شروع جنگ، رسانه‌های حکومتی گفتن پدافند ایران یه جنگنده اسرائیلی رو بالای لواسان زده. حتی یه ویدیو هم پخش شد که چند نفر داشتن با خوشحالی «الله‌اکبر» می‌گفتن.
ولی خبرگزاری‌هلی اسرائیلی گفتن ماجرا برعکسه و یه اف-۳۵ اومده یه یاک-۱۳۰ ایرانی رو بالای تهران زده و بعدش هم رسانه‌های داخلی کلاً ساکت شدن و واکنشی نداشتن.
حالا بعداً معلوم شده خلبان یاک-۱۳۰ ایجکت کرده بوده و زنده مونده، یه طبیعت‌گرد به اسم جواد قارایی پیداش کرده و به خاطر همین کارش هم از فرمانده نیروی هوایی لوح تقدیر گرفته.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81675" target="_blank">📅 12:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQqdC_ejTtvgfOx6K3-sbPDHaalyiXdDdUnaNQs8vjfOV1cnWvUL6ElICjRURSnDEW3lcUOeW3oc6r7-WFN1lPpy_Zu6cRi72W3jP8BT2P29Lmv8i5RrT3_CFvEkrUCMyLOp5J3_lw5gJntsnlsGZR7qVFXJ4gdgjdJjBAs6rZYJngqjzYzEXQwiDOIznD1sU7cQNeEtxeBdeoMg2kYXd5K7tYS2fnep6l3L_AO9uf3oWWLgunzUl0JdJTfCKq60Bv349YWmjDLth4UsdbjMP6TJUPW6twKJfhjqjuG1LJojKqu9s5lhE56Kw_4thVXtJ6R7ZT9f4zNjItrhlbRYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران کیر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81674" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیشتر از همه دلم برا اونایی که دیشب رفتن بنزین زدن میسوزه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81673" target="_blank">📅 12:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhxnZGo0mIcaJfTlODgXxC43AEmVuxyc4XvdWANkMb1dqj-oLe9xQflDxs7dfNwRQHGu88eL9jWal21rfB7qqMSzDkTlKPlBARKk0dgf7KfYYOYQ41-3Np94lywrwN_tB_ykiGwSqKyt_n2Mehod05Sw3qFMRicX7Jo414hHRgI35sFizLYUEaU8s8CfPUgdjxujJr8NMGJisek8dvT_B15VDC8YU4dQfB2C8aj1kpOSCV0IP3fNKFsXzNUfe4OK72FNCITnIx3H7YRwZbvyuisdvxtCAK2BAi0uaWvJmZfWx4nngTxeB60WAj1tSTB0amasOGLAUcLJKE3h620ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقبی اردلان این میما واسه سال ۹۷ بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81672" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=W7qyp7euEJRn7Q7QuIHlkhCZ4LEPKJwEIw-Uqer4Nl93PMtnZPe3tNL3ZfgK0EhjwfW4BZtxdya2ioOMZF7i9ejrVIEU9w5Suu7pPOxfUxvuU-PUqWJIOlKt1ybsjXkKgI9-4XSh9p8-36ldPyNOcI_9hYTaiqUhgd8o_fl9sO4bhlYy9S0huehaJ-BhZvqkTqyT-Ary1vXC1TgY2iDqB7Z7R4zrr314qKz_iCeJQfeGTlVjMvXgm7wSmWA4ExedOjBCTDJWsA-fys5uLwi4zYu9lz59jjSRVHnjCm1fB9MhihrS7NDtKduPyq1t2Tz8E7AHkphgBYZouCQhbHZBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=W7qyp7euEJRn7Q7QuIHlkhCZ4LEPKJwEIw-Uqer4Nl93PMtnZPe3tNL3ZfgK0EhjwfW4BZtxdya2ioOMZF7i9ejrVIEU9w5Suu7pPOxfUxvuU-PUqWJIOlKt1ybsjXkKgI9-4XSh9p8-36ldPyNOcI_9hYTaiqUhgd8o_fl9sO4bhlYy9S0huehaJ-BhZvqkTqyT-Ary1vXC1TgY2iDqB7Z7R4zrr314qKz_iCeJQfeGTlVjMvXgm7wSmWA4ExedOjBCTDJWsA-fys5uLwi4zYu9lz59jjSRVHnjCm1fB9MhihrS7NDtKduPyq1t2Tz8E7AHkphgBYZouCQhbHZBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صرفا جهت یادآوری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81671" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81670" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7QG4_EV2mOxO_h8d10p8ZMqRrRegIZnvmW9k_IpWo6plQp9BJEKQqFaJlHH_JUgWL7-DZH8zzKXpkzxCIrsAKfALi6n_QddAcK-ovF1oc1V8-ZSLHPhu4tSV_7XzHvOH3KPMD017kalLCYzFHhkg7Qqk3kEvTC8u-tZPPiwjuFQRKUPxrbkf2s0z9YPFkUMPjHyEw73msOQubXxbIXoOb02pQqktdEuTQdzePvgO7_KJNDZrjmr_2EA8gRaLLaopDqmZw3FGU7XHYZRtLy01r8b6qlfM0GbzD6x34PVfdQECYRbrC-4nybBmPf-jq1WK1h9ItNeiZLelTao-HKtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش یه سینگل میخوای بدی اندازه تریپل آلبوم دریک داری براش مارکتینگ میکنی، بده دیگه گاییدی
پ.ن: کوروش این عکسو با یه تیکه از بیت آهنگ Fiancée پست کرده اینستاش
#اخبار_جنگ_شرمنده_بابت_پست_رپی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81669" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بخدا اگه این مارکو روبیو رئیس جمهور آمریکا بود الان یه جنگ جهانی رو شاخ دنیا بود</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81668" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81667" target="_blank">📅 09:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLWVor8xOyQaTFYO7TLrpxNN1qX3zF80KSveksiMeXZCdWbb4gd7KMcPkMo2CHSACnidJ_M-HUu1_8pS821wpWCT2Z70eNw4-YqHusL6tVhRuckjWUqHzpM9uehIUV0tZ-rFeL-R7KACJH_KuRz_nlG_fUb7ySzhi2HS5pALYkqZVzI5iOg93Mc_b2F4sZhudokfUmBxru3AG1gfuah8C7mXsUGWALQMwul9QkNWT2tB-e25Tk-chM1YjWPzKyI08F8X5RoU1UkO8cU2aZ1ksxgvrVUhCEZZO2rSnuwsQzjoZeWR6fxmmzNVVxBJuazxvGYvyU1-pcIEJ5fzUkL4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#معذرت_بابت_پست_رپی
رک بگو میخوای باهاش فیت بدی دیگه این کارا چیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81666" target="_blank">📅 09:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81665" target="_blank">📅 07:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftXIpts3im3ogPFfjlAJqAzTu1jBiUG8W-i2fKQ9N_xXl0RHrDoLfa3wv1jmf8a5PktaR1quiAzVRFX4T44AIRGJmVMOEeZAzJkbfHhOIlOcEWnR6GFVa1dUrM6X7aZoEIXr_j4L497D9qRBCKnBYF_vWrTO-jYfVPkUAsk7ukHHRSWhSzJZj4dpsx77bHi53R906RTwFZVaDHAImsjm7VsZHBHjvkL5AiSueeYME62UFqzd5OMfyxYrUivwOFr3ayT7t59-sv80zhqLtoWx2PBrJPb5ma2hfdSOd9kWDisfh_cZH46dBUReX-sDWgXD_1eO2FgAuie594zUL8HC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81664" target="_blank">📅 06:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چتایی که از ملتفت پخش شده همشون فیکه و تو ویس و ویدیو هاشونم که چیز خاصی نبوده جز ی سری حرفای جمع های خودمونی و شخصی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81663" target="_blank">📅 02:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب بنزین بزنیم یا زوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81662" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81660">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=fGMGcG0wPAxfHNZtJajjFjyszrabaaeM7CD_qJu1hgRUo4IXauiAjQ_OswvNF1FPTw62YG6EuY2MlHw9CPOz-ByWXf0OhgW32SjhdzaLp0b-pWJo6PGfC5CiCazNCEFGFEmmAwQFnUL1D-xljFwaWrftGGxfrAZczxgHwoGSgXTlaInDG1HrV8MhhEVHDoBFlu5dRWAla5xFZ2TZ8WQz_GRNVGlOMekEuIkmeaG1AVgMC2TltLfnXMJFm9eX6yIlDClmXA-BmmlBeXV_ha_E_gkiTa5wYU5cZUAIfCeayu-NFmq6cIXYo1Cmk4g8TKgB-4zzVa0mBRvQLP8FIZGIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=fGMGcG0wPAxfHNZtJajjFjyszrabaaeM7CD_qJu1hgRUo4IXauiAjQ_OswvNF1FPTw62YG6EuY2MlHw9CPOz-ByWXf0OhgW32SjhdzaLp0b-pWJo6PGfC5CiCazNCEFGFEmmAwQFnUL1D-xljFwaWrftGGxfrAZczxgHwoGSgXTlaInDG1HrV8MhhEVHDoBFlu5dRWAla5xFZ2TZ8WQz_GRNVGlOMekEuIkmeaG1AVgMC2TltLfnXMJFm9eX6yIlDClmXA-BmmlBeXV_ha_E_gkiTa5wYU5cZUAIfCeayu-NFmq6cIXYo1Cmk4g8TKgB-4zzVa0mBRvQLP8FIZGIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی حتی به لوله آبم رحم نکرد، وصلش کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/81660" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dgl8Llc1YI22cuQEjEBACRssfCFcP4q-fpApZxeEPG7GhnRLAIRPASDoo8ucE9NjLOdgmmjtylGpJIQio9JJppOOn-DU4Da0IsZgkgHqZ6Z_YfHWmD8E78GbK8auYaDtFXP_jDXrGnPD4aE_psDgnI-Frr_T-CaeW8VPtLLaeZEJtVOx_eJPJRE7NMWsWiJmwhAu85XI6bl_gs5X2C5qnjcgjQIwHPWyo9WuHqYUwIXV19UbQakRF6viCkAldJM58SCEymLeBScpfTw64Wj5dek7k37INWpV2ruq1xG2ggTcanKIc_zn_DJA7rppukAJYwvGP9QgdG6Ye2XVwJ4ziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dgl8Llc1YI22cuQEjEBACRssfCFcP4q-fpApZxeEPG7GhnRLAIRPASDoo8ucE9NjLOdgmmjtylGpJIQio9JJppOOn-DU4Da0IsZgkgHqZ6Z_YfHWmD8E78GbK8auYaDtFXP_jDXrGnPD4aE_psDgnI-Frr_T-CaeW8VPtLLaeZEJtVOx_eJPJRE7NMWsWiJmwhAu85XI6bl_gs5X2C5qnjcgjQIwHPWyo9WuHqYUwIXV19UbQakRF6viCkAldJM58SCEymLeBScpfTw64Wj5dek7k37INWpV2ruq1xG2ggTcanKIc_zn_DJA7rppukAJYwvGP9QgdG6Ye2XVwJ4ziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویسای منتسب به اعضای ملتفت(تایید و تکذیب نمیشه)
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81658" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81657" target="_blank">📅 00:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه بیکاری اومده چند تا شات و ویدیو از چت اعضای ملتفت پخش کرده که نمیدونم واقعیه یا نه چند تاشو میزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81656" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBFeTWYPWdN85lchDT3lqKB_QvPyUqnrDPGz6PA9S6ItaV0o7_JUGS0aj20eT5doGeBLbvsUPpvt_6-JVQpIfJMP6z61FEF2F0htZwkCEZa9GN4TVE8oRsdqqqKMsfak9gG3yXMBp5rGqX-xJ2KT4O2CWoySWDb4m9Gc7YGVR70ZTYY7jnlUeMpSUencyMfEG-346uUicFXj-JS_gNu856gv8NRdZVhDArhCcjOqDKhYs2focTzOTTf-HSMXnNiU8g_RdaS--vsMYRbEGrHUpRaumDh3ZVdt_frPZVv3r0eF873tAxSaSsm6ryCmKcHo9TQP6NF9EUliZnSWsJyZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox5YOeZkDMuvKOcvtZuQTvxXStxuX-q5Mk18qqLtFEYlPkCquQpzg4cNzYJi6VldA1lhxN_V3gdrvy8n-AntLWpiOv4z6eaa2o3Yn6F4pRHEPOur1Flx5sYQwxBwC4zM_BMClNnMy9s3xRaUCYVc4yWQK71tcoIdq-opMYCzBsrsWGlpG0IEeFpfFSgoeMkHBOFX0TjSsv6Pne39LL1_Keup8qrWyOXVw2LIk16nyQVLOhPJoiTb0yyXaJR3EVvre_43092GFqNc-U8vM9OoNkOJ4D4dCbrdP3yeAvroagTv5X7lmpZYXAZDsmE4_OXhnsD-I0Th3RsGCFMBAO3mqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81654" target="_blank">📅 00:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81653" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81652" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">زدن زیرساخت های نفتی و برقی برای امریکا و اسرائیل کار خاصی نداره
پس چرا عملیات رو شروع نمیکنن؟
چون منتظرن مقاماتی که هدف هستند در دسترس قرار بگیرند
اون موقع عملیات بزرگ شروع میشه
دقیقا عین ۹ اسفند‌ ۱۴۰۴
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81651" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Uzvzs-9OB1Ie2LzX-wMOLQuKK9gj5MIAdcubEDFiXxm1iIvyhvzTtxGE1NHbcoN6N5xl6dpG23hf5IVtX0aqlT556QCmkd0AHF8yxgCTxFJD5MvQmr8Q9x90WNrHz2GKMEsy5vzYtIbFRa5PpV56-iSEARM7tZKyaqK26oUmpziqx7kIlhfJmDTAG3Jagcsg3ZlzuRCnOywl8VX9XqAgRgbRsLJSi4EhFJVK395MObPEZZZenNWdugzPzbL9BBByH1XIiMnTBwDFJ5VL6og-Lbpi2RRsTdLkjpo2zc3ptVVvVls5f2ufofkSVcKXdfbIRsctm5Ej9rkl5e9gWU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اکانت رسمی مرتبط با وزارت دفاع آمریکا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81650" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چرا کسی از من درخواست نمیکنه خاورمیانه رو ترک کنم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81649" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ_1fMik1XiSQ-AKeIBcmyHeR3qJRj98ltooMIYWVpGZI5fJ89xS9ovrtJK6qvJ13d_qYpOcwRdm1ZrqcscDhnHE4vLI_eNhn66tB_6g-LJCfshaYMuCo9ug1ovpWi9whGMNxa_-Q7jGsMeHZAFzzsR79_-yx55dsEa8DZK5a8-aJebCnZPvIoRLJxTLfAEO-rTAVvwH-fAvZRoVJblXG1IJsuXiQD46IwpQm3R5omBQFoUEmQxSsdG-yC7Gy-UAydxyBKzbj0NbGA9mGmJWXUJ_VVxajuFDfHmHlIRA4XOEwd3FFt8XwAaUNntuD3XjC1vmjRYqN7jKJtjMIAOKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpYj40UzT22ZFHYXyqrQVKEk4hTYsUUY0LtcA5L0ORYIFzeBL7WqQTDF_Rs-6FDW1bUcDQtvNkqzkscwDsQ4kGl8m-2ZLzoHAG_9Is5u4gPTrkN8ORKEXd0ujkD5B91Kxc4gdnJcVK27SrV7lcjpbcSSUgN4gLI3dC516y5amjjfLRrS6LyZN0SesNjK7FZJLZmlw_i7vkSnEF1TJrSq1806C8O-ATDus1iYSbypwCXj3VnBsk8xFab_LbpAN2OLmhBo-PhVi_hHp_YNNsPdSaz6jcq7MVuZBqNbvoX-amhWHIZgPmd7iifc-dgFIeZwn4XJk0Aidpn9GDRmR90ERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5q0EI72e6M0tmp-X6HWOEzsgluDo5hC8LVTseKk72K-vYV5mHiWqIZEX3retZH7URHtiFciAimVC6axmNukX7XBQ0wmSclDb9KRY9FasBuCact8SaoyBAC-HqvLk2a2-i4RIA5OKd7WwFCZnkuQa4LLK1xs0HD2t-yPXK4zxUjQayjzWAyS9-wLZl9qoQL5DYwGvTWu4V75eT1BwyfalMugqYu9_mD0nygRBmh-cyEqc2CDJSYiYoRsKkQ65TTDge1ylym7muAJefTabNKnInIUCwMWuGuYXWJGaiCzryEIksDVj5Wbkez-EyHkxxsZk5_k1jNsU_D_eI2UppUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSsinGnIxTa3mIXEinqLdFrE3rNV7MUVTQo9pIsdiZzQePH0Joy-vcDX8mDlvGv7AGQBJ7rOgagMwJsQ_vM7PeVboxotFWYKKbElQ7kMZRfXXco5kRAOLbEiAjJBRBUYJWNCmbtxA23a_yh1gU8FBdcgMN1jpm-hGFfnB8TVvhco2eu0Knwc_0DyLNIdApFGDHwCCVipzWjNEeT6qeBAtS8g-_g4vL6xdnkJXTalREcDzGfFoRvFwVv1Og66839MzN8PkNkQhgToVCO8Tlen2GqbfiOAyNTuSizxBmlDa8D7HEfWWVQyK9TxhCX0dqTULGBI6dP0820yyooeVE4xCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-B2YzMwmWNXV1mfqXWDVlxRAKx74M7qWjINDMhadcGJUcYK3qtw99YqlmY4FSGANbcXefdb5j2EODsALEA9HAf8y5Jwh5n9kPCP4W15pokcEKMuYFhfZHSx6zk2g5BVeKRBxfNggRCnSWbxtdJ9DNlzZU_lQvEeZMFlu15P5UZ4r73EAE5Uh3uu0z_IuumC6VWeaUQ7THirFiHYQEQQJi0rz_MoqDYXxpGRYK_A_1VjKJBZFKNOt6i5777s5aykZc2m_Bik6tbfmcaVPsz_xqPqgS7IEmoG8gQVuJqcM--tzsUVc7guiahvPnNLPcAZ3FH-xL1hDhq9p5gbTyA7Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنها فرق شوهر عموی من با ترامپ اینه که شوهر عموم، بزرگترین اقتصاد دنیا و جهت حرکت تقریبا کل اتفاقات جهان زیر دستش نیست و بلد هم نیست تو نیم ساعت 37 تا کصشعر ai پست کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81643" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#پست_دارای_محتوای_رپی
سپهر خلسه:
نیلو یعنی عشق؛ شایعه طلاق و خیانت درست نکنید.
✋🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81642" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81641" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81640" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این سری، این سری دیگه قطعا میزنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81639" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81638" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81637">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">لیست اخباری که رسانه‌های رژیم غاصب صهیونیستی تو یکی دو ساعت اخیر روش مانوور دادن:
کانال 13 اسرائیل:
به گفته مقامات ارشد، انتظار می‌رود ترامپ دستوری برای از سرگیری درگیری‌ها صادر کند، و این، ساعات آینده را "بسیار حساس" می‌کند.
کانال ۱۲ اسرائیل:
یک مسئول اسرائیلی اعلام کرد که ایالات متحده از هر زمان دیگری به آغاز مجدد جنگ با ایران نزدیک‌تر است.
نیروی هوایی، سازمان‌های اطلاعاتی و بخش‌های مربوطه در ارتش اسرائیل در حالت آماده‌باش بسیار بالایی قرار دارند.
انتظار می‌رود که هرگونه حمله جدی به ایران، اسرائیل را وارد این درگیری کند.
مقامات اسرائیلی معتقدند که ایران ممکن است در واکنش به این حملات، موشک‌های بالستیک را به سمت اسرائیل شلیک کند.
یدیعوت آحرونوت:
نیروی هوایی، آمادگی سامانه‌های پدافند هوایی را افزایش می‌دهد؛ سطح آمادگی در نیروی هوایی، بخش اطلاعات نظامی و سایر بخش‌های مرتبط در ارتش اسرائیل به شدت افزایش یافته است.
خبرگزاری والا اسرائیل:
در ساعات اخیر، تمریناتی شبیه‌سازی کننده شرایط اضطراری با حضور یگان‌هایی از آمان (سازمان اطلاعات نظامی اسرائیل) و نیروی هوایی برگزار شد.
کانال 15 اسرائیل:
برآورد فعلی این است که اگر ایالات متحده به ایران حمله کند، "اسرائیل" مورد حمله ایران قرار خواهد گرفت و مجبور خواهد شد وارد جنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81637" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK3BCq09E8CJsUEJk5fHrLSa7HY7jd0Fsqm2ioG1byhxQgAbvCDrtPKPslFTuncNA7xLe1XWFOSwk15NT2ZwCnNhikXBKlvKnZ1BfDeDwh8grwsGDxjkNPiVD9937gFEnA4liGh61xTtOdiIcvKsv0t_8PJXdyH2zWYzZ1Fd3-jxtXL1RvYHCXYUktnH0AkYElif6u2Lv8p4nzvlHTZINwkk5cZ6C3GyAqoRUi9E9WwvXXg1tt5BefbV9X3idVqRjuFTGfGhaCHvHbCdA5XOvPZG63aFkcGsTFZkbC8larDaCKb2lsIzWr633tA4gJAutuBRg4I3QToIZsvHuCMDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81636" target="_blank">📅 20:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYKACHOu1sAN5y58IJMiiDQd1E4WED0Qv0LJBfPFJQO1GdeUeyHrPActWTFAaerVBz3H5SvAdau18V9E3okui12UcvK_aqgMl0vNZnykmQ7ihOSpTr0jiD5A90jbyTQwlpmZEDWNIFevcvTib3XlK5ONkmhS029VQfqNVBJPlPn2eUCmBHo79im7P70JFbi0-Ya6x4vbP1zGxEjFEdiHpBnaiNCS7jOhOrTn5myLKosqyFMTA9YajoKJU2tZj6Px_XjBJhiF6S2NmATZyaOcw9qJxHssWil0yySLqF6iD4jDmFtmBrfeZPNeWIzqK22titQHEqpB4-eVpvorS4aO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که باور کرده ایران ابرقدرته نویسنده های این سریالن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81635" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6uuUtphR-2rI389J8-5BWoCamzVzWznO726a4WdKeTTJi7-X16YPdAtCOYAxJbx1JZ3a3ctmSjIcgGyJTZhdQMZelFj51-wQPasgFE1iDznMoLuQzUhdwjGuHeJa7ZkDrqxJ6iTrkv79EmJ6l-587HOxkhODt9C-tciZMatqbu32Ey6fVHaqWFJIIhWTDwt952HZ34tsMcRBkP5fyU7r_O0kLWKO-Wglx_OR4S76gW70kvPBNfE9pQ1KpZa6O8kquNSwamkMbkK_hZV_wEQpd7_h0ZC4cEjXK73XFhYUgzl725iRdPYlHjpx5Farj60TuPiZ0cZ_vI1ZvNq9s1JGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که این بویان کصکش اومد بالا مسی خودش ۲۲.۳ سالش بود، بعد میگفتن جانشین مسیه، درحالی که کلا ۳.۴ سال فاصله سنی داشتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81632" target="_blank">📅 19:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iROdTtgRrUPMmcxRqzM86jpNmpezwcJDIiwyf5QAf80iY4tdlE3PSNFFifrIIVSyrt78u-DEUV1iCLp7L8DnAJHeEV2wPh-ewwDnCIksRRtQXmbeHjWfWiJpiF2Sp5jTtGvvVV8hc305FVdi8iKXIJiJ-6UbyY9kdYtDx99hPl_32XwG8hmamEQFsrmNbdqwhYHnbcmAI4NN-qI068vRsP_vwL6Gn5JTufsvqoQPJhLhzYymao4M7rIUYE6S_wGwMQseIeIbpAK74YloUbwRzUixExIykuaE6SMRmtJuunByOdsB7WJCnhvVrFVzqZ1dDbeKmfHLTR0KFyklaF4bZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مرده که توی سریال کلید اسرار که قبلا از شبکه سه پخش میشد میومد پند میداد و همه میگفتن چه انسان شریفیه رو یادتونه؟ الان رفته پورن استار شده و بعدشم عضو یه گروه تروریستی به اسم FETO شده و تحت تعقیب پلیس ترکیه هم هست و برای بازداشتش ۵۰۰ هزار دلار جایزه گذاشتن‌.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81631" target="_blank">📅 19:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های نزدیک به سپاه: اگه زیرساخت های ما رو بزنن؛ کابل های فیبر نوری در تنگه هرمز رو قطع میکنیم تا اینترنت کل جهان قطع شه.
پ‌ن: مشکلشون با اینترنت فقط داخلی نیست انگار، جهانیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81630" target="_blank">📅 17:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81628">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pujqu4sKO4_4iThPqYVZSXTamUfZJ2XVPJfm6lrMaLmV5r8S1GitTwpJRrQNBpOQUBJD5CLlkpxw4I_GsC6vnI-HzPh90SW2N2vd1fS5aXsMpX8LO5ccpKmxVlKD--OkYiKl3GqgV0lnBSljrk8RyAJgUb2gYlGw-Wjqixkue9ORUBEMHsatp5BFOjyabYvnYN0CKQd2uK3XRSloRkxqiyaaFKx4c5H0kHz43EykWD1W375bANJMGJttu7Yv7M6v6MlArPyYBQfYavbHeKZIkw_vCz6gN_0LhS-qHuJX9wCOeYGjcgKt4H1btIegyIR1GEc1zhOnr5cDhgdeldeicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=fhxRa_VH2pg3xQoNRoyqDvefk2PW8Ltmr85LRnQiiy1Cm8jQi4sszCQ40x6jbIFU3Q6GDT0Q71GSMEGaWULHzxYgCKQznoyBSCoIH3Ft9OrrHZG1h658Ene3stAwZwLMfQ_zP2tMbMFlnzb3NbfH9RDCRL8vA5jxeDUCVj3J7fOHBaaTVQB6-AaSFD4ZuG598J_Vu8Q92HPq3vgpaAuZSu4BSh3YLJHFS73rtQZRWEDxwJ52tpAH-dUcejgUlYJUtYOyGGKcr3sM2PKJqicmveVUOno9zRr-dhN9zLBeSNLFVYyrs7ZF1cm3q_NjpVHIqFl1RXsJe0_nypwH_cHRxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=fhxRa_VH2pg3xQoNRoyqDvefk2PW8Ltmr85LRnQiiy1Cm8jQi4sszCQ40x6jbIFU3Q6GDT0Q71GSMEGaWULHzxYgCKQznoyBSCoIH3Ft9OrrHZG1h658Ene3stAwZwLMfQ_zP2tMbMFlnzb3NbfH9RDCRL8vA5jxeDUCVj3J7fOHBaaTVQB6-AaSFD4ZuG598J_Vu8Q92HPq3vgpaAuZSu4BSh3YLJHFS73rtQZRWEDxwJ52tpAH-dUcejgUlYJUtYOyGGKcr3sM2PKJqicmveVUOno9zRr-dhN9zLBeSNLFVYyrs7ZF1cm3q_NjpVHIqFl1RXsJe0_nypwH_cHRxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید سیدنی سوئینی برای برند لباس زیر خودش
.
پ‌ن: برا آخرین بار ببینید که نت قطع شه دیگه تا چندماه خبری ازش نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81628" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBfiPNiR9h-qfJruUf0KoGOOkuC7iVgxsOvY4G3GgG_oB9aQqDZBam7y4mlgvP5MSc-WWguElYWWKQ_Xtyp_a4vLRm8txBjTIVW6RT9pFB7HT8S5ebl_XzR3g9ej-uwJJmAtBjFz-v9AdDIWXsm-JCtrOf7ZWQSpaghzuzcmy3tISH7OdDnR2xNQRQQ72EEC-Ggg4CUmBu-OHgECxKHUQOyqqRDbYP7J-mkq7jP6BX3UtCmH8rgpWNW3Q5Afy9jySfrCZYuWE5s4qNJg4pXskBcQhlZjcYxBenbvSXb5yiYXzs68sj43kTqrr6e7WUgSuJVV45enAcBlx8UQRc2ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81627" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81626">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انتقال لجستیکی آمریکا به خاورمیانه تقریبا تکمیل شده، الان دیگه همچیز به ترامپ بستگی داره که دستور حمله رو بده یا نه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81626" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lxvu5nGKsfRcC1tljfeZtCNXVLEiWmhAO50wUtce23iqYdVNtKUpdnyFv6OHZdorG6UMGEuH8X3zbDILbX2OfEcMtg94JHAEbFTp7t3lak6JvHXbYwOoEAhBvqpbNFxh6242iSA_LYgdoZofYYggU04xi1zVVuNrKj1VzO-T4nMylgltJnObXwKvBCJFtJR0ngmkBgNSQVKcdL7OxDGJAf5MuSRWt_BAFV3_wMTD9KJMsKEMIruVuSIEC7z7Z9kIr5IjQ35gqKc9PUGxtBwKNwaypvp8iU0haItFocauW-swvXo4q8JziaVlqBgn2aT9iAWvfb_UhlDZe1oE4nCSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تانک‌های T-72 لشکر زرهی ۹۲ ارتش جمهوری اسلامی در حال حرکت به سمت آبادان و مرز خوزستان با عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81625" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز صبح آروین خیرخواه یک زندانی دیگر اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81624" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اول جنگ ارتش یه سوخو 24 فرستاد العدید قطر رو بزنه که منهدمش کردن و تازگیا جسد یکی از خلبانا پیدا شد و برگردوندن کشور.
ارتش گفته این ماموریت 4 نفره بوده و همچنان اون 3 خلبان دیگه مفقودن و دنبالشونیم
منبعشم نمیدونم کپی پیست کردم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81623" target="_blank">📅 17:00 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
