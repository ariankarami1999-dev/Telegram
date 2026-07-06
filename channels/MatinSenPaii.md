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
<img src="https://cdn1.telesco.pe/file/sr3gaOzMvgDeWhQJXUDClLFKzDJNXvEBoEEn5q_dqbrWwZJocMeG-il5FTjldfrhx-UnPs7NJePW52iPM6HWP4lwdTEuWvCVaArXKK_rsSNP_YOeaNp336ttBPpRzAh1X0Uni-JHZiLkp7mfRuYDBOjZy3mci1aO3nrFhVfiCaxTybETwD3kAr1SvRbtRrkX0ggNFkhlzrZnou_HrE_MeG5f6tKxZPqAuMrxeZ34MjnEhKcoIN8cMdfaO0U7ZCQmF0WyIXdfWo-y2m22mN0DPAf0UixZrCcSVG70Fe21Kanzl97WcjEGDdE4CYu2IR5yJOeOmuvn7zV8wqKV0H1lLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQGTluMGxkYSbpqPCsFabXHK4Vgd7a7pbx_-n4YuNyMuvrYFiyZJx8BQr7WGWc5F-F5TqE8LhVHznXQf3RC7zMnXnl7jOXZRpK46wgqZBVFVPKWTB7IS_-Qmc50CoWhnz9lAhRNAC6L27tmvJexm7Xl4JlpP5x_bV_vqtojy9R0gNxd-V7wdraSLjOz_10qdAkZ2F_rd8Ud4NnLlFl_QfNkfznzfZ9gC_w23RL-pH4TaKRx0FXXtW30POSaZcYyJYSZTR5G-kI1qea9TnmdniNlvyyaAH2WivNn4FoxUqogi_UB8XKWenvlrVBwget8lMxlYGI_uvZGviHoZqx5U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAO54C-yQ278Uwc8CkgT5J9XyNKIdC9NtWPziziRdxCt83F_xgONtG7v6XTTOfuiEa5Z3bn22j60myHAw51WneNX71MKbU8ddNrk3yG_lt3xgoeL3Z88PHSPjwXUXxVqg0Yn66ArNC8t2rBqxAUPnueomo1l7RcnvSK_bHD6pLH0m7glYYov7qe2ncla-3qbXg90wK9M2F5lIkP0wobmsYympI6iDtC2qD4ze7LIrQfimN9i56LPciPN6Oyq2r1RoawmRhfIvB-_6E_fh6-zCXAebWzHXOtLC9W5Aa2qlnts0WH9qFWg7Kpe5MEBWgOu6uolxJNV7XzikTzqrZPPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKdC-BFaw8oxOkN-2-nVyCnWve0epuTuUmXKpR_KO52VEpRfCr_BSstJF8ZmT5DbpMlehGzlUGoxkVVsJky5_z0uSZCRiJC9Df8gRz5_TxSKQdI15Unu38bBR5q5kGsPQOWJ4PkB-r_YM-gdVrVgWUo-7v9QbBBmvo5YBLn3bxRTdlNyJTTRvozB8hayZw_ZwvAajol8v-4LS2BsMy4c_CkctQontvdL9LTsU2xnpCw1vbfjU59MncB42MoMfhRdnQ8y8unCUc_WzPkTQ1l9zgzKRWG1noP2cEy08RV5J2TwjdgcVK4_EtiHHu7BgzSc9ynIoU_UGJtAzkmYcaFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXAcxdJc6f6efVAK1r2LyiNABWRIaQpzKVF-QqWzlnUQnnyxLY41mv5puB2AMGRS0Ro1InNG1co2zbcTnCTozxugijrvRUI899Z1XIM8FqdYBynkvy315a3BWkQdHYHwek42TREuVms7bhQnK4I5EQ7U3GU_GYipClhcKmOlqqi0TywXRGerD7YcvqNJlEtJY9pa6VuK-vwp2BGXgQhYdIduMs2ggXZkxlJmtrkSxffuaobwVKPgK4qzjhp-DsMg1RnkMEAEUm5izhzo2Y1O80vu05OqPHRVeg9TKDxt_N-fcG5gGpX1RZTYYBxJeQKydWnjYj4Y__nCMXtCQvjcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4eKLe6ZArp2wIDXfxWwuWXrGgjrVKxsDHxIVW0ydy4tFjo3dln-eKC8Z6vCwJeCkzZ8J3x941b316VcqKrn6FjZWN3_QJoe37BDbxWVdcyvTQQlkJdqO9jGzM2iw30wWhvLwNQErAjZWbWmNE0K7clRm6bj2oDhozQWVZ7RLQ6Trrc8HjVajkZ_yUsADsW7pbja94m7VinPzI-tUq_HaTwFuW_cxZFWfDl_M4pfWjKyryDI88d5-ErGRBsDtgXd-X_bvnBG42ouVy3ZdUj9BsQFxV9z2CpX83Q2eXkq3DULF0wbVM8o-FzcVyg1jS4PkfoQs0LPFl6t13asZnueeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=vPZeTb1xxohKThxFHkCeIcJPZsnhuCv6_SFYD7RS9G_8ukYqpQL5otyW6x76WnITQbnWiBeFwX9snE5EJ0QPQVpT8gogdClOdOhrm7L-xsEdyYI6PLlPNfB7m6i8wNFPUw1Rw8Og7oyE-Z2r0IbP4dhNyHApjbhg6rnRPMc9Rbh-cekLM40n4oQPq8JONA0zZlDK7oARyQYPkhqk3LBpinOyU-K8GEd3OK7J5hyotlQUCAAGkSSd_LQ_g6reP0D7mEn8npBofCq3XsF0O6hqh11iYpqgPVZHZdkPHaEju0uMSd7krbjj82CBTZdPBLVFiTnKkAMz6J-kFsFUkHPe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=vPZeTb1xxohKThxFHkCeIcJPZsnhuCv6_SFYD7RS9G_8ukYqpQL5otyW6x76WnITQbnWiBeFwX9snE5EJ0QPQVpT8gogdClOdOhrm7L-xsEdyYI6PLlPNfB7m6i8wNFPUw1Rw8Og7oyE-Z2r0IbP4dhNyHApjbhg6rnRPMc9Rbh-cekLM40n4oQPq8JONA0zZlDK7oARyQYPkhqk3LBpinOyU-K8GEd3OK7J5hyotlQUCAAGkSSd_LQ_g6reP0D7mEn8npBofCq3XsF0O6hqh11iYpqgPVZHZdkPHaEju0uMSd7krbjj82CBTZdPBLVFiTnKkAMz6J-kFsFUkHPe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QRfwajIljXtAcLJ1bO7a-qKEdLPMQBu5CGqEGrUxKE0ALppGRlKYVcotbAWU--S_t68_j-97_fiFZqNXd-gz1Ma2VZLyeqi0GA59_RBWUShI8wHJOOAKdX3MIYA1QmJvGV_rNLW3qjvLyk7TmIcaRcK3ba6Xh7bwopOZxQjg6cgBhI1kLohSR2DOJfCaC8cKtt02oBMLzaI6V7SG50AHlEz7GyKoUfwRmPAJnazZgpber8_ioJJZqSAxu_5V7lhjrCkIZCHkfxSWyXn0z5RNiQzTjLuDVrZFUxKCQ92sE0mbEY0-96IlibMB0-kYu1S2n91pgH5paIfDQ7v5BjJE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M3j7CzTxPhQihw5St4HWrjO05rorYIZU5PaOjCT_sjH16CdVM06kIdJLEqwL84U9BEJsizGhQJsPVOynBxfkdzDXwdnH6YDUm5FaaPhq0psZ0rAPQny2WpFNKRzBrww8gu2sFgrcOuO2N0enhTGncjtCeWAgfmeYYHSlpPLCt6059ZZEo_ZBRQUApGMepOJWo5LoXyr3rwBUHzuPOgkS0T09ASu6t1Q_KuPqNr2Xc7DRb4eVQqlvU-fRx2ysnnRJsTaD6WbnaZKbC6zvhRx5o6_d87cKreeJJGcgNvDHjKiMtcWWGnscqamy1gpC58Z3WErNW0a1UPGxy9IqdGzAdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJRp8I2KNwS-lTIn10-thzs3uZESqVXQjvSbxMxVe_j9hR_7pqxColK0W_zO-hCwO_Z0sSJcr3_9UTs0QV7W4NvNQg4It4j8391DANH9PEPDYSeyoBalVJpT2eeTg641I2mRE6T4S4YRGhmF-RTb_Qx5BLbw-7z73FTCIqA-M0U0A_x0GRGF5Fq2e0cQjc3QOcNa_2ikDxPOwezS7_PJ0EAoBBoe7HZ0kzPAgjJaIjjTYkjWbwEAoPMbwRmky6vuz9Fw95gEcDU0EYuUMl_qSBj9ts9hc81_amrFYyVcTfX1LS-TnOrh3lxjAExAuHKX2SAcxeF0PohKM2pX-NjyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5V61N_If3MTaw3RajnexI38KUWQxochuDoQXEld0wwuyje38Ts5aqyZ6ytpanJPInwwAFBIP6JenpoVV4nEhJDHjuaFf2kHdHq7DvjwsAfeKWcRUBVLdc7NzRzKVTs8neN84uGlFQpJhQUftHvBdd0LxxTufROeiGV6cpNO4kOR7cHUMh8TB5fK5HYU7sPSNT9Omt8IO38_m12-V3UDtOTeSoh9Z1QAS-cnaB8jcMn9UKK7UZNEekBZEipbK4NDLMTCn9ZttrehWGOWJl_5JS7INGKuLoaqEA0NOm8sXA97qxJ3O4vesU-JJclM6FrEdi6_oB3su5zBYF9iM0P4xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RqXv4briiPQXyoqqownbZwLhAGls8HlSiPiJJ995PXguIFQq3b4TMzC8OmZFEsbRNxC1cPakRzkIuGRoZJxkIJxpcSMujJi5vh0wnYUheNPSHtqOVPCthwkwiJKDerTVMfGkNVBlR0XwmmjOWQlkRkYJ8VxdxVniKAIFF1AvRHgY3QFoQd_pMLxOitJGFBvJWFrPDR--Po1cGr8hxkwMp0Y6UMT2J4yNg0JWx2_pbsFWgR9OqAH4B-e1xwA7ZTs77W224H-JAIRFaYSqqtBKzJyL96OF8BFn_vKRA4oiW-Vkx9Mp8PN9bIn7ALr6zjswvc06Ss6pYYWAD8uviNN1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sFf5euDQVyAv4uMJtF-6UTWtqNXl_DFRcHKlnQFCyRfMyh9N3TVmjvhkvGjO9X9ppiYClKwiAbxqAONRHym6ULNBcPbsQgVjt1q4G3vUT2agxJmBqKqixSwz86q5cfBEqGJVGt830LrCvEowN3DvJmR_L6YEItBgSsD5w4DcubpGuSqkO0AhOM8dkEjxxI9be3KiqR0zXgJBV1ko7fFqSw9J5CYuuBQN9n--haw8dittUkRMzNzFfuOjHAN7krkpnAzgLBBrE3TBD_s3TgWd9aifveaNodOQFijfWCsi_G9-GtYR7wSupW2KmPEcw63ZdWp8K_dY-GqX0yERjBUdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XgNOwrVomkwu8NfaW150w27iv2sDqFxAxE6igThpOcLw2mPuueQtxvVSyZjKLEtOLzhhIfkKXH7Mx2WwjKv_vw5JcxtNwfIib2NUKyUbGOEUmJvw9xe0dfeeZLd_C9-U-8lk4_9UF9IG2FmKo_atrRs0dukQl5LHEcLiyM1i31ZW3E66Y15esnnBoWphizqUOKGr4I9pNtyMQ88cDhpXwdnQeeRQVv54RcpJ9aB1XuF-3drk4PmgNyrX5nm1BmtxR4M8Qu8wm8SozdFK2hcHneE0qbBWvZlcnQRrAE27_ByfbLQWHcUMB7GZl4zxq9DcTYASsH0xalw1hMtUsnEIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YKJE6bgOspc7U3zsbAQiybmbYBk0DNtLSATsnb91UQZTEFDC6-3i3xZYX052KbtLp5aE8VKh_TDq01QUwI_NL1YfVi6HshYbxCxQ4k5bMRx5pb_UhRayMkL2CZbdq_ZxIFncN3KXpsm_I87cfaZx6lLVxKGBjLrVH2G7yujcrRH8tOlXqzKkKwdJ6lhZrpjueDzMlk3zg1o8zMvHE-wnIbYEcf22SWT61hOMzHJa-RdPYTgaA5tJrzbl--trmgIihsEhG8psYyBg0fDiK5FsREvmgPbiXblMeNSaH56jPK_nm7Zas6ctCU7nN8CRBklmz44VnXCrTmleOFDZO_u42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t5-PCQc_aMOYVGzY_fpL1L_zVrNLJo4f-bUW4YC8sDznGfmA__t4YtRKMWNkjUD9-CeY0PFSnqDb8iw7rEsIlpCBEq8wNCLnvVWb-IqNkM1oy5I1NTnG82I_ENS7LdTmgnpr5q5iE54z6_uF0H3EteY4Om_CgnVj0BA5yM4xzgbabouA28NwupmG8aR3sPrR3lT_CzARTFANdTk14f_qKERqcmS-SVKgvYtHBYv1EH324presgS_lV2QA_FGc2d6KwQ1pemrUXIDoc2vtqpOKVOML1vMJqKyUUaMntvKyxEbe7ecugapitnc8rkN7UZPOJm8AF_zDDnInujnYksUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IDSE8S_2LDtUIMSahMvj6KNXS3YvB21Fyoq7MmK6mAa7zbZeID70TTOIvdN2Jf43mx-bn8N1SVVYEwvaCNkVy9FQyPnwPVaIYU22nNvhV3OdoyO2SoghOy6yKH0GR2JIfYkAgz_C6xbJfWf_JmsY2T1V4vvutdRD21CuG7IFUqLRW9lgUx78XZxJojiHwoZLCZ5doHsroDbo01gTEnn97Qoy7Nt2oylZG0eC_DnTSxzO15mNzMsApQKJZ96Lf9yaNcG-EnBfvNJtpfyXdZYtNGfoG0uaymcs-WOyf1VWxH1KhBlFASnVS3BhzIZ4Bhmn1KbhJTSvkAQk1VC3IxiQ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bm46kyKHSqeR_S0kcvI-XftKeKHsnidi6hxq4rRPw187vkRE123rzK1806R1I3UrP-6HR8n99YffGgCwvp9mnWkrVRNRAGqIlDSh0WpBceQi9q_tEMB0GiDgJKYLFObhPCaFqIora99f86JAGrqtzWj96OZR-z_M9RHwIvdqhM3ULSRhc5XnLsCXxpWTIQzRaKsKNNqa-4X_W4WLF7vUtwoaH0Ix6v-BzIOncnsCOlFfZ3ERZS9m83Eyy7R3bhZPSJIZwNvTtYGw4JSe1PT2KK2WaQ3kY8nhTLGORugHt-F4ycor-khiUoA7z2_YPKTzQIbbRMQrMPBukvRj7vkDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rJExzI0eRQc29zhZnkEpzxfrqXIipDRTpiZOKrH5yQ_cvXAeE3jeKgo4Ldeemnc-czQM52ER5ZyuvKTDcIZuCfn8gPugrMa67MuJcHeKBI3lqPtdA2YRAjo9h--rH5MzBWYON5TdIhUaAyzCetr85phOy5GQIaguHHLv5GaFgoIbtScJyjYmSds0FSjjCYckEBs0bDotV1izJccJic2BOFnPoM70azmo5T01kE6do3qq07obVeDQuDcKGSTCwnSfuRpORCywbuRc_Hh2U6iPKD832FMeJBlApYWf92UtMF69GMAjLA7y3QSb6hQ57yRJ1652kXLhiRpfS9j4S7JofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-OR18DB8ajawvL55KdN1qigspdFY04jmnUR65GqAJwZn-dslAkyKHIuyXgGk2o50QiONz0q4YO5PDWIewku6gjYIdVZ5ES6sc5jZvFw5TQt98QhCLcRPi3hfXJGXkWeVWFS6gf0ttodTA58IaPItnhYEQf-_gNeUR-qHj_1JYdYHv2frbeD8pQJD_D5BIOkpH-Hgfu0v_Pvu-jneWUxaXC4VDPxeZEPKi76YGoVc4QEb2JA8oG3U7HUePnpTMVLfFkPdCExN0RFrw_LNVIhCC1HYamXVaXpgSgZvRzrV_3u44SmD3K1WEHrveMN_kuEeYJofF2z6VIGlnWPE5z0Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHVIMfsHMv95b05IGcEhJhGWZrj3Xefp3w4WszmIA6uwcZ4Bp55U4WQpg0vrMH1c0_6HQUgqGgOOxs77nJDItTplKrKmJ7YBKbA95HXSH5XdJASdFLWP9WaqsWQIKu1U42t_2MHjTiDTUHGZN5DSljLztH7zM9NI1H7kZZ-4oM0NSn-7LWDw4Hwf2EhLCcF-N-AnavVFHk1beClzkeF3SXr5twr_Q_4zG79MOp98cTJHSjDHhB1YECveDeru4rfq3QAbqTiU1rJLMTzIqwA-hZVhdFiWbbgmwAKB0mD2WMRwyUQcqWhH7BU6LirdcTLJxYA8NT6Y0BHFZ38d85OPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=ixvX3oX6I0ZFxBS1fNbRbYMtwf4WLT5ltUEZ31yDehBi0JtaVCa8w970ULRANFvrICTD2YShT97EdFGDyRq73fH3fr8ZGsG8iPWgiheTw3JlcvNL-utQusdd1PdNbdujzury9M1pV085F2NytMCcqTjbHzJyMCUvbC0dtbWZxyBKC4YO_hLP1brmrGE_9Zzo7PCfMpCcBSxpJqmZqBFbQ6jCU8CjiBqB4K_WCMb8_FK10MeB2d965xndYcB8DFaMXLShnbOOm11NiBvE53pyvx37xDveZIFzJ5Q7okNkpRKHwyfA5pgIhfrkhYFuwjnTYyDrBjAmdLuNLB8KbINMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=ixvX3oX6I0ZFxBS1fNbRbYMtwf4WLT5ltUEZ31yDehBi0JtaVCa8w970ULRANFvrICTD2YShT97EdFGDyRq73fH3fr8ZGsG8iPWgiheTw3JlcvNL-utQusdd1PdNbdujzury9M1pV085F2NytMCcqTjbHzJyMCUvbC0dtbWZxyBKC4YO_hLP1brmrGE_9Zzo7PCfMpCcBSxpJqmZqBFbQ6jCU8CjiBqB4K_WCMb8_FK10MeB2d965xndYcB8DFaMXLShnbOOm11NiBvE53pyvx37xDveZIFzJ5Q7okNkpRKHwyfA5pgIhfrkhYFuwjnTYyDrBjAmdLuNLB8KbINMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qeJWXnzmMJ8PbxOQ9tslhhS8ZcvuVOA8KfPVr2SysyZwE_Bev1c9LXQGAAzP6Tx-CsNRj5cisckfs_bRTEfB148_b1DAqDb3XbgrccdIM6A82PW-0qMQ4YavEKkhSesSpMESIQPAj7nz8BtpPr9YOJDdjmKSM0TqKI1dN8Fow9OpfUFTeaMe5V4JhJp8g-z2AB871Nm7H4kELQYtFa1A6imHXnyR5xqDMtT8h0vp7DK51rZyKY7yI-40yu7lYFpSRZJ6X7J7qWpJ2x53yBAAVlTxgNVQO0WaArGIaySScQiANTaFrGDgN2GRnu-HdGAUK6mA0u5KDnKXPr8qkYn9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tw89Y55s9Ox5NiZ2vjylyqOAfLFUU-vLSfLCt4yj68xtEvAQKZs1sLQF-iWJ_P327i1n0lQoTH3FYMjndO_rRVaNdmkL4Bwy0ioWFU7RVGXL2KDZuG5TvUFyW013ppCdouy4wd5DEC9MI04TMMSwo8MIYTVxNemhYQuUE2Vi7x3RtLc0VsEnUr_J5TjiLuhtyTrmjcYrAAXdBj1pAv6Bggep5ACNx5vNHC9gMuuFy74Qu8QE2L7Vya4NfbWiL1rwnOEqLPEPUCUNWsuCNWJcH66MxNaBRf-6FvxXE9ITD9n2B7s_DwKLH-GW2iVepzxdcYp4nowgAM8N1gXLZ9KSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnKcfk8ekJ568bMtxIGwLRWLXCeJ_Xx2PxMjWPgmPDH7zQOyAtE1Y5D6UaqM5PSeJs3247duAylj0R0tN8W5ocNxEuXPJ8M5uQE2mtuAOqMkrnNL4HdA4uRt15xHILcX5lHVP79WPqHkIFVRlkRMQY6pK2fpW8oJfOzY8yr0nUXONhAix3WZo1OtvGD4O7CHtliJRXb_CMf_ui6EE3fJuG-vD7Ia3SzBUpW_F4Gaz0_XR_fvo9dVAshrbIGt74Jyy_1mIQi_S1IoQOzbwGYTWM-JQNEcNA0yxIPyXQcKKNuhkuZEZstojidJskWQPEHAqWYakcDtvQCdWAxdfbIXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lih7Tq1VvQ3O1Nq8ai_0A7v0Vdczy11l1lT1g59Oy5GqBlLu51jLk5nZKywCjby9XZ6RQ0b45bGRDs7eGrqG5nhfhkldBZTw70ZCzT3Vmw3rEH6VwAUs8BWS9LXMwKQnskneewHGwll2DHnJnH9Yqkch96nrLM54SLLs9GAMl7NUY1FCt1vzfH5h5ffpkdpIMR8rOJG9ai4mA9JgbIyfxNovC9zizU3nUBUZZayviikxCDD_rRthTOJ8FA8lBLWxL48uAiYhva1EOp9tOEp3mj8aLK-XaKW-l5IwfBK2HnHX-8qDL7svKIUW0DM7TEm7ie2U70_VArIMpERjVTgKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VNfv9Zd4KjAlYqNJR0VqsS_nHlaSZH7ryD0oHafpxn48-cdQMqjldrvI_mkN5I_mz8fGHBaD1SyjD9SplB0ZNzYr4A5VhBeK_fHpdcKTHxMbMnhIFY3vOhZB3Rald0p1F2NN49QzM9tzI2VF0vvvDgYHeLi7l240o6dhYtjNqy_X8Qxqlwujvsl-4oCFXG8tw81cB2X5xSFRE3nnwt6-Ghw_sITdqC3HITdjKN-Kyl5mB1jaVIhWCZX-dQgwlIuEO2G9i2CFWFgWuNU27BhSodB8wyJI7dc8gWf1pJ-bwE2_h61wGBYJxvkaxV3GHmbySFsF8nNZ-AfRu9iTJwYfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mDKoQDuM2iBJvkjO0g9dugPGwpovoRtE4799cEluLs8HgIx4GECDKpgWkbY-j4eZKpcZgZe3q0GDmW6c3PUBGBRvp3krMfJeKhgQfdpi1hQ4cesV-0xuvG4vBB3XT0z3fzFK5fN9_2fuJY4bzE8SsJ43OuloDwhwW1ZutPfb2ONEqGVOf9deZ69a0ExVFlTN5H2UMBQzTl8EBlMwjTp-Vo3J18VN6fkbaTvUaH3hrwORVPD11pgjJ8wXyHW8WqkDZqUikG6FgbbfNqNdfP3mEszi_CdRw2SoBjXoZFalZeOUlN8dNi5l1yMKOwPn6kMf9ymaQheD3lfrk-lZ4FI6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E3mb3ZEPgZa4gNY9WfTCrCqyS57NLDuaWeJ9FRZSebaBiJ632lOixVB0Rq_WpurKHCnkTMG_uN7keM7DkHcBQWHrj9rxBYlvEUs7QWQLFE1PL_LYYobRYlKWV9YH1TFlHGMEnrG2Sjbf3YNOaDWl7w02zxPs0uPW9pBpDgD4eqiSkxCGccdT5Ne5weBUnYY1lQ1IFqNRXpBEFQu3o3IEyBt3MhMjWKh2yIVlCtRQgZdLd2A0R49sCnp5jjGMDrKZDkD1JHdZAyJoMyoY12PV5r3dH6tJRSYs4MbQONpsYplD-Vj6G81KkMGpztuBNqDrE7GgRhTVbKLhEEfHAdZmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K30_z0HGIMxCR5ydCa8nMTE1HdL5PyWtX1kddDjiwcQQ8XgAfETTHSPuYdS1S1lMIJtCB9DKc4N50Zz76QRkEHmIVLK5MxrjWHyO1V69wTkjuUX9yEvCMKGjSg3yVak7Nx2PG8F_heyk9_5ue2i3s8SyoZxQT7JcCYdh1XaxT8zCmv8m7eyaLuMGEE8Nw1b0wgS7-x9aUqzNB_u0QJ9HxpLNoB4foKbj1Jxn65T5WCy5m0GFSf2cXojUcRQd9LQV_K_X4DzvMMb4GD0H_Q_Sj-m2-zab-FImUAKpwdlLmEbohpagtY_1_bh28PmNyV2uOpygUD0AZSbUcTKpq0Wv0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J66eQiijybznF8GplRHoW6bODqas71oNCVFTIRH-w-yM21u1YU-vLv_X74bMyVAYHUpUvsT0oHc7ZlqL7L4pf06dDtnEr82AbFaIEelBdgV9M05nHJ8flkKZStHBB7P0G0MjMVWIR1tCtT0Opw3GzlVQNjTERgO8rfY_j9mywFmwFWrIctYXhkvvwTPrWZ8QyaQQ20mxK9y7W-jfxHfc51_jf9WYu3inGdBHNmowwl9z_SNMaZTHzWma1xIgaQh5IzXlnJk5i8Yp8355RUjLm-7Nfx1abBdfckEQKs4ji47m3ISvxXEAIbpG5pkzgo5VcOQ_GiJlqw1QDMQtTeZVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2tHyVV91VWowN-tDHiWOeJ5jF_smqroU3sHLHunAzXMonLBIzAXM54D1oHAYtJcp3QrbSoRkM1QO-IXDe-9ACxAQ91bSj4Hf7jMekQG6Qn4kkS08RPsMaOpcXRIB6Wc--tdlnHnzuGVrgfmuPgJdbTtLSdlSkSF8III7QN91mbRWe_7ohmKTSpaeB966i-Mb7VFmmz28rMGmLaFfn4ZrLbLkUgWAKUwlDYi-zl-NmMdsM3Ep5QsrYTLUa-jOSmLRjlKBuXadxjH_FjLbjL3wXs_YIqEp6bnwLLcMTwYUeukh1JBXkuAhN8_0A6paYSM3JNkfYk1GiRAln67NTE3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrNASd3b5k5eEKtU0m2ABt4tfhbXq1_DHCcRrkFE2Yndsg-LBGnkdYtQrUqbgyyuVNT8eOShZRI214R02OYWpdi9oZXidsL0z6w5EKfYu25ZPuhoXCU8VxbbC1tYk99OUjr7WX9I5es3TenxpPx-5NEB8kKnGOHVKUiPw0LMVu7nk4vMcIKQaqZtHZbibxzlGStDP3KMI72C9nXS_hmo_olyqYQU0Q58G3F0SlJaEFhv0-dVnNQmpjJAzW0fUyLhiITIuZ8UyAeQe7W85p9poPA-BgDG_aKSsIkacfK41Lq0FMFuJSX3a9Mnmeax_FxHyjNfMByPL74WzyZWXX1cdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REDndIl1HHoucg92vsTNop-mDVElXP3V9ujff8K1IWMFlb4qKX23IxzL-RXpoX00n86gOeXZuDOD5o29v9DE-ClhzylNw4p19Bzn00lgnFQZY2wYPt4QWpSZ28LCm711nzLvVS7Bsj3S2-eGgGIi6jALY4L_1sNdFElMOeuQ-ENgWcgobg1Jbz1HWC8BysWa055QmHl3tVWBY6mgJKtl-hmSuLVI5X8P9LLMTXui5otJI46qKyAHCTs-ADX-hfvbFYQ06C_smh15jjv9-SMbVEiAwOyROwV_gumw9VfkF6D8nLlrUbVzdaTXeqyrsLVWKBpod43_3ShScDUHqx1iVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WSy_jGIHkUjfVhYA8WxGhikm-5cIwsmSUXdr0tXAQ1n_iN-Zg13YDxFNe0xSNPYTj0dZn_WfXaaZj-AHI9Jq5JvktWMkcqWx-wYlSFhcV6aCX2pv9oDGHMGn89CsdlwZoNloW-B1T5HRyw41FOyQToYzwG_MXVFeMf6xN0S4WR4D7NdKyTR0vdh7jEjV0Nb9zsx3aoltWYLeH3Sn3DYAjpoQDR42TbwhFWNwX-gig64ewSfADz_UYRps7-Kc27xFyLbQwFLLUJ9HenIU28KuYJN9PTNzkmIC0El6D_IZubx5EIbJxbpqTKq4TcFx63ncnGPD7uPsVoCfZDgWWJGjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMI0_iETMM5uPfuDb6TwC8kZTuC2uPYZTJ4zgYTwY7s2HNu8hxwObI4cV4po0aZDT4ww0AExjPHWEnt9xprqDPnd1af3EARkYxJLghhuCMn3DZBTJmtA7yzUy0tqzoBjfMU32bjmxSJxKKr9rbVH-zII4fFqpsUELfMVX_6w4h2PawVJ0ccOEekfewADjdDDugNt1Nzw6d7S5X64xVrg5OH4etDunbTgKQU03U7beBm97HSXHxZwogVqWTM3FxgM7IFo3drWDgNUVtffAgkhNk16xkzFQS9VPNSFgqIfwkZ3pK21wij3j_I7WbNTiEeBVm-PhfcC8CM9B2mYLC6MJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DevyNN7Tpx_TtTqPbXhJ-IAAffNyI_dIeV439CS9vrjbX8RcRVl2l0DKpTu_RnIrQbMLrbRh8Tu8AlcH7JecoUFXWxiU7cGGg2zk7NYG-wq2IyJPVjyD91Fd0aZiiLtIq02P9VFx9wJt6gOU5cImKcV9vxFqnM3FdxFIrVxxOJkxNsdZSyL359PpvxEx2qOUKwbirUKwZF4dK8OrZill1t8r1E-sEH9yVEc2JnqFN8-GCTgJjdBodNomQMKmGZ34E94JNABJZf_9izeVBTO12ychcJIGgEEaIuVoCCLw1sfoKaRSdPLpPoz3eIllgn59c2cjPdHbzCdCIEl4hUEV4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=t7v9dCI1j4oBK-PV203I537SRa0mz8esYFjH4-sDWRRAdnbnCK4eHD4mePUKGC2ge7iuxudZbyAW_1QkGHgd6yNLsg8wLMrYHNhx18nArAHSLRSEJ-oBgQ0VynnXfI_R0Hg-ZdetmznuEr_Ixd_hAe-hOGi8iPAODgZLRUPWGnK9XQDHb4rwW7C5E4vn1slfHAgP7Orpqa_L5OMyV0ou47NCboymBqh2WU-iKtRjPHPZrahrPFVFTS6pk_hdsoK5hPVrFNN65LFTHUZovlK7LJBamMauARZrc1pqtp8DPes8ultc2tPBu3BdmxqU945PqOeShRKGrvWN88mam-SlRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=t7v9dCI1j4oBK-PV203I537SRa0mz8esYFjH4-sDWRRAdnbnCK4eHD4mePUKGC2ge7iuxudZbyAW_1QkGHgd6yNLsg8wLMrYHNhx18nArAHSLRSEJ-oBgQ0VynnXfI_R0Hg-ZdetmznuEr_Ixd_hAe-hOGi8iPAODgZLRUPWGnK9XQDHb4rwW7C5E4vn1slfHAgP7Orpqa_L5OMyV0ou47NCboymBqh2WU-iKtRjPHPZrahrPFVFTS6pk_hdsoK5hPVrFNN65LFTHUZovlK7LJBamMauARZrc1pqtp8DPes8ultc2tPBu3BdmxqU945PqOeShRKGrvWN88mam-SlRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuVHCY3d7VT-OxrgE20DBCO-B7FMJTklh0J12OfOxNkVMst8OvFSxnbNyIZpPJYPlYBUQ4VWITSTNrghl2EfzXwbawGF4BlUve4A0bxqY1Lk219NiGqcnLaE4tTPlAEBBnJm2fs5thTGSl_HAmrIxQeLc2IK1JvjjaHIL_NpXyl9XYMoh-K5wwIBgUmekvEHG7Hh3vc53hW3SI8ZgozWM7PR2pK6H2ZCznfvGBe-jQ2EHLTpnO1pUqj717EyFRo2sojiy-ZGhsX523KSu7898BEP3y53apNhx54tEG4c8Wbv_Vh6rgtdEC2gK0mPbYSLCe_hG1OrAuagowvtPBdgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UEJlz6SI5SNKGDtLzI7VpYH0G4Hum02t351YsWQEuMdcuIWZKSNo2FN16FmOx4jDwnAPm6Z4Ikpe_o_ZuT7x1QcoJgaSgj0eCdcWjI4C6sB79iX1QwKqswiXNRsGK4YgjWxoJyN7OAdNksr7NLKJT5t-v9fSIrrgfj4ZPQP6fygo9SXPVAT42gmnJz9eJ_6F_8Xxnnmk9AMpc02diaXn9qI9ExEG1IVfb35nyVQMHdtMEOL0bP5SJEzONhQ2YAQ4FG71XIvHaIYUz5beXD6UUhzO4CvFa-hAJM43Ayw6f2jWFF8AXedGb55lDENThR4QxjV4IAiOyhS279-MBK_KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tYM15J-sJDuMejgfZ5RU8udYnfVql5YL_Zr8c6pthWsn5SSRtHlHaN1mt4Y91Jk5TjIKCwHpRKMIq62lHQK5kvpBDMhmD_Q3rALm-3xg6vueZT2OwrivXqqJ0rLWjpsecsyhFM7IyKUgkxzZYVx1h-PP3Ho3_nY0baDjfX_ew0NxNBeBWYcvnrdxZMjEzkzeUK8mXJWM6xqU2I7ZbQDidWhu9Hd_SGKzNmTgp6WdM-Zxc5PxNar2FEVmQ37G1KZt3ia78fFaVaFdRGBDIsY8qVHgiNGAjM-oYfcBJipW1DmCK_H4vbl23ixeVsJAxrzTvVeyl22kvKhrgzhPpZx1jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RK6Cv68KVUFcgHTi_x89EM_qiEIaNNkSZimFqlL0vIu8SAjtf1XKhzcSARa5ycTzxhz6-yMFawuWZCitV5fP8MEw5pli-JHMAH8WNcG73YzeqKnDFLGJ8UrjnSEJHbuMEwHtTKzP9Emnm-UCqHjUbctwiIEd_pBhdQgD2xEaFzpvj88cG4l_3WOeQIiVlokoktcgiGxUz67S5BnPyZBb6AXhBInJgg0A5dwilv2ep69p0NP_Py673yLEonZD28jEBrHX3CIv0BCANCsJMjxkoZd9SlFcs3vpc-YwBZmw0T-XH2MSUM-tNRnoaMfxaz_PVZVldtYDKVqp2w7QsoLu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6tYUzT9broVza1uQzgBd8qtuwWvEW7L88tS75ioR8j6OiFesXTnzuogYlDAPQv-mZAIiGy9-tVTXAcbuDbRe84T3zwey4vk_I3oTnnjgjJLtqrxysEcQBnErmH4KOxs8f_BHfYw9FdRd7a24eSwi4xQT4JdbHmPmD2zcNfBM6y0DkXaTFUaNcskxhVrYa1dAOk-9nmuS2qPspuH8SQmAxkil6HazM8Tawpa39weDC6azymdv_XcWcaLuX9gQB_tjzG0HZKmUS37_9Vds4J6IKOdcdfsOiEV3b1-Y_qOwZiWJ6XVxgfPpqv8a9NUWG9ew2DcCiAFU9gwHKDVSmlUzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GUIsN2fTP870jv9S4_ArOeYw6gLslRvkDWXoZgVidRyCw2NXjFNp6c2yTUGaPnJz6jcHHsX6gAu8AWyH5LsIRfmZt_STbEuV-4e9bVGB101r5OFiAcv1MV00E7yIMqXjxD6vZkuyTroVr18j57_efr_-rS5aQdKxMwidO-77Oh9QmW9osnk3b2q0JwyLCsDWhbjN79298-fOx6tRkbNsN6ZTY9aJx_P3JRRlRmyMnJDmsZqy79glJiPIfYpSOtNEZZQs22R_5e9u9c6JA0ALs1sO50HRLcKVmdOyCxnclzn0XBCkuUe187bE-PreIom5fvnBcIXhwuWRAwHosOniMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYdI1Xx4xDqsPkUpk_aC5Zu1G5ulcMJztILOG3H0kWrVXeZXx5B9zmrJlgEW01O0dZMbwkznE7prrD7-rS0zwgEt8wmio7zIvx3_tCgXSplz4Fd9iWpZsMTjtr60ogmuw-etLx2RybuobSeQBlQjNDPNi16vgOSUAvyUjQpGYRjleeAWrveb6ct-Pp-yjEZ1I1tkp9ou9GPNoZgfhz22mWVF1ctL8AQ5NSRIZ1T9axtf8ZwhQH2Ya4Ou-ziITNgwXJnWw2MDE34jY8warocy49emw-c_BGQ16tk7sv3vLkur6dCAiJp9df_5jRvgInLSrNGlKbbIBQcGwQrq7RUkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pxfCUr8STsp7V3KvaRulJwigHUulqWdZLOkKPPzTRVrm__LoreljC7Z7jViVAIKYcdglvEJ2txyK6pSDboxwIsIRb2qgSP_7DRK8XTYFunoJb3RFPzymDWRuT5YmRRJJnj7GUu-sUeZqZu80vLHjNL31fHPY7tJDBsHhwk8b-YdxXOO1sdDmwjgI-H_U3CPQeLQtVFa-Q1B5_sEkXqIUvBhz5_Gq_nL8a6oB7g9fXLh_j66Yasyux17GiExbh3SCERt7zsdFz6dXmxt5Z2zhS1Yb-rNyYbOtlSQ-NtuXBjzK2CLnGPkdGdsHdyqD5yjufme8bJOcKcCZoPkZH4dJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtTgzsMeMZdaVHohB7LcybdKmWNQlsaE2gtC5dJ45HNyR8DMcY1KWFBbysSyUTmUHnsElkl6XvxLHnkvB5zqxAI-HicEZ0hwIH5rmCCzpdUrNWGsfEo_vqgAStJDvO6lDbJimu79ywjWHCPrrBt00zXYmH34j4f2yUYTFTwHcHzg61UnyqNfLU4vTvaDsHs5nkx6YNaQQfkEk4Nq_POdmelR_Xs3pY9BdJmpVvpH342GLm4vie6XOhDa1q7_foKC9iN1bQaogb0CTgpHIusw2IYjrQY9oHEZaUdNsw6HfndLZlmUhUsE4jPeufrrJOAtPOgR7DpmA5JOsX4rghET3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZitY9VxaUBJo_c2sSPxYKms3vQPuom1PRlRlKaXtfM1DrUiC5UpDAevhMmN8r92oOYc9p2F-ijUa3SiBpsWCvkLeiNtHST5PIMbBxFGNfaxkxrb-_3EJJvg0dQ-Ws3_F2UxlDRm-Ta3SC_f7yp301JVHTrZn0cQr_Ww4_HoPD5FGl0pphUD5R5YpNcwVmHkSRR9mecJTHGM3yH6wQks__jHjlrHO_DcUl-EvGfPyo24m2w06aJDgIoQZqZWdLEu3MFc9vVWLfSWY-lDwFidyJbESu677GAcUb7-7Fyne6XVv5NWGCt2sfd7hAhAGmkWgdDE2UGhaDKEIS7dCMGPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hf1BZbMpyjW8xonhb7DuJrb26UTBGQmr-70857MZ0TGMo8P8RIT0L6IogQRIa0Q2t33Xglnpi5d3PpONRluIlcXPWTKd-xmwCRNcVfpXnGgXDEMmAacjLDRr27aMgm3iyv8OvmnI3IbXGjw-PJDeJsskvlqXL0MFsNuH21OvhHj8zSPeQSNyC_46aZuBusVZ18TOeDvaBSk3rsCEL9oX4DJaYV-8ZQUX5gAl4luvEYnASHMMSv8HN3K5InYN231Db-7g8LO_jrhiuADhy-OU-vbhGAkn_oZL774qVz0gcYFHL6xjrdV8KmkCgwwnxo4RPZSXxuH97JNl41PwiFen7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REjJeTtunqjYnyaWaD7DzRAI8cpyHZDOhxamZuR1u0NwNEYw7CyrxjCjRLJnCT38wpUwPbggxHA0Kix86g_MhUU9k6oPd3Cqf_sJ7VzuCWCicZAXZroA2sfvXtvwiK_B-h6TpTP-BPV26ua_EP1WiQKttoIGow0vRjDcd0UVBfnDA6uCRYbHX6ybc8sy-qS1SpwhBqTibTRLzl1WKDjS1RVcMm1m__4rHN7SRrVJf5bL612Mbtzwu_SFwWLTqxAQlk26LX8--bRshf3FZtCQAGFT9_EvYMWHQBCISUDuR3eiK4Z-znAzdhui0u2tBnw2vF0zLCILw7pJzrMbQJOncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTtyyx2WVUsmZWwoSY9K3q-7610ThYcZQm0QTR2lL-53I6Svfl0zoyzexlD9Idylhj8qxAskqtoXK232nC5f5WHoM6G0lLd8mLriE1FAEFeu-Q6zyPBLDzX1o0E7CJHT_B8xseeLVHIBcxpmAvm8JA1beubbpn2f2CzAw6EwswxfGuy2NwVXgA60RqDcGr-st9FEvegg6Uom-QgeVdc3RSbztu_loUvrK5DMDVMQXy_y0WEJpvl1_kssmS7AqkIrHecXUmxFdPsHYqnloVctYWNnNI3mlcsoPMx9X_oeG6_ngDyGceAr4VmQmL9VLwBkd_RivyAtTo-y8YhLaOstEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BGnl3nPa_ELLAAxpfJxk5F-4e8m2m64rV5u9orz2jfvGEmwm3rNdJWZE6NB3mHuqwl4lRf24F00KYlX48daslICkpQyipIgaNVIPMnimA-oYmwT58G82yQndtXju9CuUpN_AJCvwWyVSh3TkL_9DZlA6Nqe0P2I5Rjzw_7eoRw8nQT_4CKy6YyPu0XE8mHbtDBUU1htKzDPf7ue8kCTsgU_7AHcMsrfi_KkYYkrCN_04odE4jPXgssA6b6oPjQrrb5oEbrexjSXh3qCQooTn2BXyghLkJfzg2WpQxccieGwWnjHdbap_-SqOdq1t1PAZr6sN7dTI0rqx8Cn20hCD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nV5yUwpgU94_Dis9hCMllUiqHmE0wOocsmHC5cqO-7CXGSHauBOG7mAU22389Do7bDeKS24NkguCvp5ZS_NaInh560klG7VU1XVvUNaHZSB5Y6T7Zb-lEVywzL3KM8h6kChGTZdgXLfG3raNmgsFQ8VQkgP5OC-AN3e4JRNUSkeK9bcT-2osxbElCiNYwAB8px75ro5gmpBDL2NW1epnYt6W5oWezAIxbV76M2iQkVZAjY0DcgGqYtTKPu0wkvMSdlkl7g6d3rnA7lZU-ZRRqpXWt7a94sOaOhWX3XrqXDQsb3egw4bf-Nbr-FsqACb4Iv-Xnnnl0qyEFO8vxNEP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpba3KhE-vOB1zCkHGNlEE7U3nurECRET9aqoSQ0Yh1kwdB-YgdfcUpKXa_PsC4PN_UpHdvlI86YjXcuwNIcZwdueC4dU6kjCup-92NMBJIyq2ODknnvVogI_gyFwOBzCNvY7DnTX4okOEOw6s5wL_xPhLwCoqDMohiSrA191cBzW8bKX3JjYyWzJnZ90WKvR37_baW1S7pR1PAu7BA0SV5WrMNB_xlR5zuzQVhVNwgQXGlwvdGv0hgBCKAZZTZppIuTrqKXMbjTSDB6aOu9DC4QdUNQOoLei2oGu3e9gAjRLi498tT6iiLLAtwed-Bs_oFgq-dD8ZaJ35Z0gGw-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VG7uZ5IrLUoTgcwKfjqgUCQkTeRcRzMM-DFyeGO4nqgVXjrrx-qX6QdJjw655Dqhfzgoj0P0p3Rj-uoHioO7SJUuz8xjYA5xqERXG_2Jij40vrH-W7CUcEuLlSlMv1_lm-KDXq_v2Cf-56cn1lAC_2YSQ9ZsGj1agyg8-b9VzdT5B0eJCdZqDmUhPZJloLB01GHIXPTZdPrsQrRfBIFjf2WVvonxxDmjuqtgk7iXkRtry-Te_RFOg8HrqeZc6WaVkSTBNtThBvux9PXeqFvRYBNxAx58zApMNtbNLNZfbSO2Qi6lddqKF0XU7Ndy_Nf8LgZ6VhuDM5Ppey6-iolNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fz-AVnkyWal1eyUi7ITfH8Wdo4NMSXzGSeBOYg7yT6SHbNiheVreL6Z_kE33fuxewAOnSnBTSkZhmPmxpFTbyVVgPcPsESZCzw8Aqnme54Etn1cZJ-_sONts_y96N31n44bB0VhYVJelBq93lK5FpXOxxlLFO-h6WQrVMkY1alYR5zyajeL7TcXk4TPTcCsTaaxnb8wR_h-KaDe1q5sXSMQwBFo_YVQBePw_xaDy4CeSW6972VyvmH2Joei-kBMU3y3n-rAjgm0w5JDWFxbD_GsTF81Wkp_S0TmiRhdw8KXEZwe57wodRpN1c2synyBKEW1wrdcuu-m6JLVCXyTiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq54eKoNNCQ1d2Zyu-d5krZmWMyqkZyn3yfT4Xxuwg0IASH15Jr-4T2bcdfGuu5_iRUlfqe-HgnZv6bvTpHJTJA63HHUQNnJALfh9hAmAs7JU8HxPhS7cx_CHuJHoXTnfNQXFngY-jcMECSw8oIec8mKxJQbOywUPUMLo4HjjfRACItPRZvUVRTDmPeJhMLjgKzI1S5wVlGkG_ev0s_e-KJ38jKJ8uDgu3vpcCCAR2bSyMH5rK-OjOLgOr5c99PdZWIYdvx8uZ4rPHBBeENlAu_LozXdvBiJC4Cd63GoCN43qZLIUW1bSFXhCDyNNJ_Z-9BV_JV8_OOtzJJ_Th-GyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6F_GYfEUJWaiivryNPAAO-RIRa88FjC5yKkzq1DXBaz5tQX1Nb6JKmq_N6W27GwQW32ZgIjpkuSZZxFSripv6mABLsWWWOtxSm1dmXhGcAHkbFO6FzSOZcR9JnDJuUxDWxLREOKzr_5eTuNku_fPYVsM-EfsKBUdVmqq-XLuAFPlEJmO0M-TjPuYbI-OvU4IjOPq79STxJDwMTN8lXsh-9VmS7g5JIBf5pLeizUBSOTcQAG_A5tH-9gCuOBGSIag1ms0YcEjVMqyoKHaFdhX0NvYHf4zcagIOQj34O3DvwZyTmM3iFzLD3Adj5EDOUEy-PABvjd_XKo-7Bc08yeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EdHhfpXXKocQuOTXuaQYIPjssngyWByQpoX-g7g5-RB4AH9V80h0y7quAieIdCc6Xol6PBhZYcrBmNg2N6B9ki54B04XoCj0pM3yualPQYC_9rfD2PsnnECZpJ8sg2A_Ggj3l-0qGXYnzL_ftFidkQx7xEy1mtfqp5M7HiaTtjDxdI-Sy_VGgF7Ff0as9IYZpSE2R7V6rsKsi1iFSBD93WFRdKfuQkSG5jm3NUq-wUPxtRISjE3bbjjIBvVArM8ZJHdNHIgM0iu7m00ELNJ7Cx_HrUbm_B1Tw_qkI140zdjq1xDRvbNs0e1N18pJXdWr85vWoFZvp9bk5tz9hPR6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mIT4IJ-tEmVTUvSON1UMuIdiUYtzqQ_eyn9FnrJWRnAjgsPT_Zrx1f3oTw6URjoFF-l_Jeciuhtn6su03aGrtNxyVBXe0XC39pWkfZmFx4rgvjyqKV1cbYdc4gK_oatTKJoORUR1PKKt3egYRcT1a6zn7oLpaZioIb3SwouEFvvP-w9B5VPDJH05i8tFRvlJcLp3S71pbw1kVC-gxZBDv8GT0O_Xc0dOw3zuZBEQimkBlEkGSFWJvTln44OQVEj3ace7UMsNfm6dwenNWDKIcvsglqLVGpL7eHKLd8TbHF0VIdLQEM8B3u7M0QoQyWMr6S8vgIbRMG3FKtw8ztntHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nxEOEXrnKjoP9Nie7mkd9UHppZ-gzmbs0Mii2OpO-k_dfyb3KW-19zT-zgMlm95usPauRsWWQk7UPt90kjEweSY1UAD4Cz4giwvigWD5ZGvAyi7vFZD-RL4coalTRMTSAScEEqi8Kh15D6IYKwa7E55jxbdgtIJ3HgaTIqPBvg0kP3uT3UEkwp8LqBofqnCJ1Z9sI09Q9-LOjU1QVssz1sN6pcz1n7x-1SFZjjL4p8hcUtTJtF2DO5MWbzT0pvb3k6DhuJxN-Z5pWaYkiypOZFUNPar-fPVAXF9UovIWYGc1xPPfAPohc2dZThW01qfsyd61YwZI4rN8OV6_RtdZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=KBVESeo_0y461jqsFu64Y_DvbxtjucQvGdc3Fs2IhE8pFf7SARpTIhKZVwT-14hXMzvVtWGEgSEhgZSVgT3xzedDWp-4oedES2tYAPuL9ZsdQRZsgSQfSkK7Z19ECQkHoh_Bs8Z0DKZtvyZIyEhwje0w-ICwOR_8RT_JQUq6TaIze0e2T_Zw7EuWrhdMrq1_6CJV5T9wvAQ8c_egn3AkudqqJ9-iOF5CN4jmQrhtPN2HeVT3mJ7uksahFQGQdnCGj6gN1sZ7U_zReX4ShMb7kpGXO-GqO-pFBL-TrPQ9JlKPdAl4XhnmzsLsj2xpYFqRB0UvrcqtSPjLZPLswsmWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=KBVESeo_0y461jqsFu64Y_DvbxtjucQvGdc3Fs2IhE8pFf7SARpTIhKZVwT-14hXMzvVtWGEgSEhgZSVgT3xzedDWp-4oedES2tYAPuL9ZsdQRZsgSQfSkK7Z19ECQkHoh_Bs8Z0DKZtvyZIyEhwje0w-ICwOR_8RT_JQUq6TaIze0e2T_Zw7EuWrhdMrq1_6CJV5T9wvAQ8c_egn3AkudqqJ9-iOF5CN4jmQrhtPN2HeVT3mJ7uksahFQGQdnCGj6gN1sZ7U_zReX4ShMb7kpGXO-GqO-pFBL-TrPQ9JlKPdAl4XhnmzsLsj2xpYFqRB0UvrcqtSPjLZPLswsmWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=C559emgtIWgBW_7UQkRN6i7IdwTzhDWxHRa98N2WZNf-WSYbS1S2DqAofePof5UgSAurvbZs-UZHMNuiIMhS3bvBQeop1lyAxk08CBa10_zfxJQP1mbbFI8SUw3wbi5nYKACOp2Hr6-NrhhieliOcRhbapeGF7iFy7SSjrVJswA6NI4GzBNGm4sIP7IZfvJsZUGsHthmsnkEWNIa6Sk6q0qMLYvbvIKvYf_yCdF6lSh4mT7Tuy6KJ-C4qWbvxEeVoyGOc40TVZ0N8UKSXWfxbyPxEYmEN--4CGBtOweZwf6TY47VVzKYaDmjAYFkbyLcsRDNQqIuKUOfYMRN-fvI9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=C559emgtIWgBW_7UQkRN6i7IdwTzhDWxHRa98N2WZNf-WSYbS1S2DqAofePof5UgSAurvbZs-UZHMNuiIMhS3bvBQeop1lyAxk08CBa10_zfxJQP1mbbFI8SUw3wbi5nYKACOp2Hr6-NrhhieliOcRhbapeGF7iFy7SSjrVJswA6NI4GzBNGm4sIP7IZfvJsZUGsHthmsnkEWNIa6Sk6q0qMLYvbvIKvYf_yCdF6lSh4mT7Tuy6KJ-C4qWbvxEeVoyGOc40TVZ0N8UKSXWfxbyPxEYmEN--4CGBtOweZwf6TY47VVzKYaDmjAYFkbyLcsRDNQqIuKUOfYMRN-fvI9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
