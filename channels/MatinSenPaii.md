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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
<hr>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=fWf6Do5bCg2tKYrkndeUWjJ9vhoNdPvgVVIAyKARUJ4Ut6kdvVf2h4TLT31CcDcR9mt_7y5Ng-Huedvwj7WR09_Cdd1MXu_YegtWE9LrNWu7XP-bW4PW6puYae8lAbVSedzrjHYCqENfjfZBTIVFzFH3IP_KhJvJhyR1K7qU032Jufk7_wERW16k4Q1vjdvXVoK_bxZ0enVEohbr1aAFV_V63qi5HbKPD97IJyaHarpSnkNjmS3MtPXlnALyxjnPLhCCKu3kPaAVqmPm2qn2RasNhVPhaoEltAiiR1Tax6cBlDIcOc98YA8PZGuS8cPESw8NGWanXDVtdhZhdzqMTViA5s277PiN-kr1Z9fY185XdS_rtbacbxbrkeSVuy1agBp9wCqAyjCR-we-ZqqM9Nw0cQxHTGB76jxM5FCP0E4wdFu64djJvSudmpWyn6QclvxaoPLrAOTYpplIJyh63aeF6w0vJL_mOo9ZDblrE_hKE0X1nlzJ37KXJoS9geKXtG1kd-0YXf1FS-J1mIH3mIaseToyk4k0K97wvQz2yvM5eRoEqmN4lQslyXZ4NubZl3oAEnmoNXuU0Ke-qs_VF7KMsThSHwBlxu7n9nmzsLqA3T482_YXd7ghCBnN6LnxW1Yk6Ht_-qYJdM1uDMHtUN1z9xDuQ-yRLAQc22_tf7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=fWf6Do5bCg2tKYrkndeUWjJ9vhoNdPvgVVIAyKARUJ4Ut6kdvVf2h4TLT31CcDcR9mt_7y5Ng-Huedvwj7WR09_Cdd1MXu_YegtWE9LrNWu7XP-bW4PW6puYae8lAbVSedzrjHYCqENfjfZBTIVFzFH3IP_KhJvJhyR1K7qU032Jufk7_wERW16k4Q1vjdvXVoK_bxZ0enVEohbr1aAFV_V63qi5HbKPD97IJyaHarpSnkNjmS3MtPXlnALyxjnPLhCCKu3kPaAVqmPm2qn2RasNhVPhaoEltAiiR1Tax6cBlDIcOc98YA8PZGuS8cPESw8NGWanXDVtdhZhdzqMTViA5s277PiN-kr1Z9fY185XdS_rtbacbxbrkeSVuy1agBp9wCqAyjCR-we-ZqqM9Nw0cQxHTGB76jxM5FCP0E4wdFu64djJvSudmpWyn6QclvxaoPLrAOTYpplIJyh63aeF6w0vJL_mOo9ZDblrE_hKE0X1nlzJ37KXJoS9geKXtG1kd-0YXf1FS-J1mIH3mIaseToyk4k0K97wvQz2yvM5eRoEqmN4lQslyXZ4NubZl3oAEnmoNXuU0Ke-qs_VF7KMsThSHwBlxu7n9nmzsLqA3T482_YXd7ghCBnN6LnxW1Yk6Ht_-qYJdM1uDMHtUN1z9xDuQ-yRLAQc22_tf7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQGTluMGxkYSbpqPCsFabXHK4Vgd7a7pbx_-n4YuNyMuvrYFiyZJx8BQr7WGWc5F-F5TqE8LhVHznXQf3RC7zMnXnl7jOXZRpK46wgqZBVFVPKWTB7IS_-Qmc50CoWhnz9lAhRNAC6L27tmvJexm7Xl4JlpP5x_bV_vqtojy9R0gNxd-V7wdraSLjOz_10qdAkZ2F_rd8Ud4NnLlFl_QfNkfznzfZ9gC_w23RL-pH4TaKRx0FXXtW30POSaZcYyJYSZTR5G-kI1qea9TnmdniNlvyyaAH2WivNn4FoxUqogi_UB8XKWenvlrVBwget8lMxlYGI_uvZGviHoZqx5U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAO54C-yQ278Uwc8CkgT5J9XyNKIdC9NtWPziziRdxCt83F_xgONtG7v6XTTOfuiEa5Z3bn22j60myHAw51WneNX71MKbU8ddNrk3yG_lt3xgoeL3Z88PHSPjwXUXxVqg0Yn66ArNC8t2rBqxAUPnueomo1l7RcnvSK_bHD6pLH0m7glYYov7qe2ncla-3qbXg90wK9M2F5lIkP0wobmsYympI6iDtC2qD4ze7LIrQfimN9i56LPciPN6Oyq2r1RoawmRhfIvB-_6E_fh6-zCXAebWzHXOtLC9W5Aa2qlnts0WH9qFWg7Kpe5MEBWgOu6uolxJNV7XzikTzqrZPPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKdC-BFaw8oxOkN-2-nVyCnWve0epuTuUmXKpR_KO52VEpRfCr_BSstJF8ZmT5DbpMlehGzlUGoxkVVsJky5_z0uSZCRiJC9Df8gRz5_TxSKQdI15Unu38bBR5q5kGsPQOWJ4PkB-r_YM-gdVrVgWUo-7v9QbBBmvo5YBLn3bxRTdlNyJTTRvozB8hayZw_ZwvAajol8v-4LS2BsMy4c_CkctQontvdL9LTsU2xnpCw1vbfjU59MncB42MoMfhRdnQ8y8unCUc_WzPkTQ1l9zgzKRWG1noP2cEy08RV5J2TwjdgcVK4_EtiHHu7BgzSc9ynIoU_UGJtAzkmYcaFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXAcxdJc6f6efVAK1r2LyiNABWRIaQpzKVF-QqWzlnUQnnyxLY41mv5puB2AMGRS0Ro1InNG1co2zbcTnCTozxugijrvRUI899Z1XIM8FqdYBynkvy315a3BWkQdHYHwek42TREuVms7bhQnK4I5EQ7U3GU_GYipClhcKmOlqqi0TywXRGerD7YcvqNJlEtJY9pa6VuK-vwp2BGXgQhYdIduMs2ggXZkxlJmtrkSxffuaobwVKPgK4qzjhp-DsMg1RnkMEAEUm5izhzo2Y1O80vu05OqPHRVeg9TKDxt_N-fcG5gGpX1RZTYYBxJeQKydWnjYj4Y__nCMXtCQvjcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4eKLe6ZArp2wIDXfxWwuWXrGgjrVKxsDHxIVW0ydy4tFjo3dln-eKC8Z6vCwJeCkzZ8J3x941b316VcqKrn6FjZWN3_QJoe37BDbxWVdcyvTQQlkJdqO9jGzM2iw30wWhvLwNQErAjZWbWmNE0K7clRm6bj2oDhozQWVZ7RLQ6Trrc8HjVajkZ_yUsADsW7pbja94m7VinPzI-tUq_HaTwFuW_cxZFWfDl_M4pfWjKyryDI88d5-ErGRBsDtgXd-X_bvnBG42ouVy3ZdUj9BsQFxV9z2CpX83Q2eXkq3DULF0wbVM8o-FzcVyg1jS4PkfoQs0LPFl6t13asZnueeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=vPZeTb1xxohKThxFHkCeIcJPZsnhuCv6_SFYD7RS9G_8ukYqpQL5otyW6x76WnITQbnWiBeFwX9snE5EJ0QPQVpT8gogdClOdOhrm7L-xsEdyYI6PLlPNfB7m6i8wNFPUw1Rw8Og7oyE-Z2r0IbP4dhNyHApjbhg6rnRPMc9Rbh-cekLM40n4oQPq8JONA0zZlDK7oARyQYPkhqk3LBpinOyU-K8GEd3OK7J5hyotlQUCAAGkSSd_LQ_g6reP0D7mEn8npBofCq3XsF0O6hqh11iYpqgPVZHZdkPHaEju0uMSd7krbjj82CBTZdPBLVFiTnKkAMz6J-kFsFUkHPe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=vPZeTb1xxohKThxFHkCeIcJPZsnhuCv6_SFYD7RS9G_8ukYqpQL5otyW6x76WnITQbnWiBeFwX9snE5EJ0QPQVpT8gogdClOdOhrm7L-xsEdyYI6PLlPNfB7m6i8wNFPUw1Rw8Og7oyE-Z2r0IbP4dhNyHApjbhg6rnRPMc9Rbh-cekLM40n4oQPq8JONA0zZlDK7oARyQYPkhqk3LBpinOyU-K8GEd3OK7J5hyotlQUCAAGkSSd_LQ_g6reP0D7mEn8npBofCq3XsF0O6hqh11iYpqgPVZHZdkPHaEju0uMSd7krbjj82CBTZdPBLVFiTnKkAMz6J-kFsFUkHPe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r0-HuRKvISl_13GjRPc0aHNP3WLbOvEA8HFIrWUiUYxbqSi-4q7uf2eof2Plx-X7lkNyWVHxLkk6hhj5_Sbln1dfPN4uWJ_2BzgXxxAqZ-R5xfvleOgdy-80Bcvr-Of9nAbSr2P955WT_UThjg9ECbjDxoiiFhC6iKyeV5XFG_z8f2qy0LtaXNz8-j6sKQiqmQNDnIfnyTfOyoD_FsC9-vQ-c_Pype5x2f7Dbw3qh_Uju8IKxFJwx2PtZq0X3eln7ayzCfWhn61whHRtnScAf5nGItUxnP3SfptRZQY9Jzsx498eCgBa8RShWgF1aT6mIzyflgtjzrGaqeAaS91aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J7VkRcrPqNduoaDD2U0fwmggVesYDXZRo1RRZY4KneJgsUyYApvz1XmhN6M52yxhmV5ZLYjsdyl8VOUwNBO-Mnr6r78ZnZkWAm7kRT2_sy0KScJHt7-w1VPEIBtneM_W5iTf0gwocfOgNd-vK9yiZJo_Iv5eq-AGkrBjDcqkvXCaRuwUQN_JbPUgmTwnBp0NRBOzTFB1ntmFhveQDW0FxZQ5ZYwayv1PGSW8gAqfBQM7V-zVA4j7T35xwuVmLslvmz0OgAfY1UoFHouaeVZtBWcijDdtaJVSvOjjyMNUyK-xOIsVshvPUpCjGuLUBEGzEcq3p_rbwjz4vmbwwkC_gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJRp8I2KNwS-lTIn10-thzs3uZESqVXQjvSbxMxVe_j9hR_7pqxColK0W_zO-hCwO_Z0sSJcr3_9UTs0QV7W4NvNQg4It4j8391DANH9PEPDYSeyoBalVJpT2eeTg641I2mRE6T4S4YRGhmF-RTb_Qx5BLbw-7z73FTCIqA-M0U0A_x0GRGF5Fq2e0cQjc3QOcNa_2ikDxPOwezS7_PJ0EAoBBoe7HZ0kzPAgjJaIjjTYkjWbwEAoPMbwRmky6vuz9Fw95gEcDU0EYuUMl_qSBj9ts9hc81_amrFYyVcTfX1LS-TnOrh3lxjAExAuHKX2SAcxeF0PohKM2pX-NjyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5V61N_If3MTaw3RajnexI38KUWQxochuDoQXEld0wwuyje38Ts5aqyZ6ytpanJPInwwAFBIP6JenpoVV4nEhJDHjuaFf2kHdHq7DvjwsAfeKWcRUBVLdc7NzRzKVTs8neN84uGlFQpJhQUftHvBdd0LxxTufROeiGV6cpNO4kOR7cHUMh8TB5fK5HYU7sPSNT9Omt8IO38_m12-V3UDtOTeSoh9Z1QAS-cnaB8jcMn9UKK7UZNEekBZEipbK4NDLMTCn9ZttrehWGOWJl_5JS7INGKuLoaqEA0NOm8sXA97qxJ3O4vesU-JJclM6FrEdi6_oB3su5zBYF9iM0P4xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bm46kyKHSqeR_S0kcvI-XftKeKHsnidi6hxq4rRPw187vkRE123rzK1806R1I3UrP-6HR8n99YffGgCwvp9mnWkrVRNRAGqIlDSh0WpBceQi9q_tEMB0GiDgJKYLFObhPCaFqIora99f86JAGrqtzWj96OZR-z_M9RHwIvdqhM3ULSRhc5XnLsCXxpWTIQzRaKsKNNqa-4X_W4WLF7vUtwoaH0Ix6v-BzIOncnsCOlFfZ3ERZS9m83Eyy7R3bhZPSJIZwNvTtYGw4JSe1PT2KK2WaQ3kY8nhTLGORugHt-F4ycor-khiUoA7z2_YPKTzQIbbRMQrMPBukvRj7vkDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rJExzI0eRQc29zhZnkEpzxfrqXIipDRTpiZOKrH5yQ_cvXAeE3jeKgo4Ldeemnc-czQM52ER5ZyuvKTDcIZuCfn8gPugrMa67MuJcHeKBI3lqPtdA2YRAjo9h--rH5MzBWYON5TdIhUaAyzCetr85phOy5GQIaguHHLv5GaFgoIbtScJyjYmSds0FSjjCYckEBs0bDotV1izJccJic2BOFnPoM70azmo5T01kE6do3qq07obVeDQuDcKGSTCwnSfuRpORCywbuRc_Hh2U6iPKD832FMeJBlApYWf92UtMF69GMAjLA7y3QSb6hQ57yRJ1652kXLhiRpfS9j4S7JofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V-OR18DB8ajawvL55KdN1qigspdFY04jmnUR65GqAJwZn-dslAkyKHIuyXgGk2o50QiONz0q4YO5PDWIewku6gjYIdVZ5ES6sc5jZvFw5TQt98QhCLcRPi3hfXJGXkWeVWFS6gf0ttodTA58IaPItnhYEQf-_gNeUR-qHj_1JYdYHv2frbeD8pQJD_D5BIOkpH-Hgfu0v_Pvu-jneWUxaXC4VDPxeZEPKi76YGoVc4QEb2JA8oG3U7HUePnpTMVLfFkPdCExN0RFrw_LNVIhCC1HYamXVaXpgSgZvRzrV_3u44SmD3K1WEHrveMN_kuEeYJofF2z6VIGlnWPE5z0Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=i6JkTDCrMSDkXWotdA1Yh22lolYJjv3JB5SiyxM2ps0_zB3EHgeHjb-3lyg0KArv5W8Ixpl4M6myFLpX_B8T7ZkspPuh87Q_X4k2Zsd-EWFcB_i1lNlJBh0pby0dKfSngOTeHuYaMjA-VlqCyEihTKueyRscpz_SvzrHIY4kcfuh2Uk_voK4rJcw2K99Z1ec7oUIAKGkrvj08Ej7WDPkYnvtqSKGCUw0D4zFt0Kg5kfJ_Cuuy4u_ogV_NSLU-Z9mvlxDU5oeYImoCB8S7vo5INNgdSBkN5P9NYaIh9eJhg6x_WiJoqzlNxwShHW5sH58-YwBCffJRzfnVDpP-9gBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=i6JkTDCrMSDkXWotdA1Yh22lolYJjv3JB5SiyxM2ps0_zB3EHgeHjb-3lyg0KArv5W8Ixpl4M6myFLpX_B8T7ZkspPuh87Q_X4k2Zsd-EWFcB_i1lNlJBh0pby0dKfSngOTeHuYaMjA-VlqCyEihTKueyRscpz_SvzrHIY4kcfuh2Uk_voK4rJcw2K99Z1ec7oUIAKGkrvj08Ej7WDPkYnvtqSKGCUw0D4zFt0Kg5kfJ_Cuuy4u_ogV_NSLU-Z9mvlxDU5oeYImoCB8S7vo5INNgdSBkN5P9NYaIh9eJhg6x_WiJoqzlNxwShHW5sH58-YwBCffJRzfnVDpP-9gBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TNgL3Oaab8QEU5LesBX8H4TFm7gDzBRyh6OkCjF3dHOVCEjYKxZzBr50lSxjTThKdfby0pqTnI5GiLEpDS_Kg6fnCg6NMHTqMplG4vgHm6sL2LNC4ai1bdHVTgix5Fx6WgUOsXhOXKvkadUhtBwMZ-6O3fS-n1lBtvi59EOZTfHsP53kN_xLD8Av3Fi5DyVo0MwWOovSBu_EaO9TWNCvPBwWEmYwVRSR37d8qxJr-vZgun7RI-x4fzQHpyYLvh9FM_4AAMsRQ9KLf68ZDkqvorH0Ns0aMnUVCc-r17iaOxDL53U7eDk9brrAlsLxOx6jH1Dwa5bSdS0AlMSGX9RQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7yn4ci7Df4OpH0LYOnIg5wxETRHiAy1Eq1FnjGFXQ_m8TiEl9SsyIx5Hs3T94rQChIuxDW8jUEFIUwR9-8iLcDPT6-pvr5QxIX77ymt8__nsfwu7sPRPBSY7Te_Wv3MQUdnvEoLWRGtbQKHkZ8RM-hkhpOqb_V8l_tgFgyyljcQGYGjrW3ECnFweaq6iKN1HtYIAwkhRLK2e-GV4ordmiCESE5cYOr4G0MMlfvmqJx91yVCl5HetfSgUL_jC2iQTt-DZBQnZWjZ_JNNJ4sZTyYMuEHdmDW8uLLdGaVRFK_Rh1aI8UUj36TC4oh9KL2QLQyjjaya6gBSQuOle5aSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oGMeuoxygGgLPRzM4d1kDCRQvKqtZd4MwogBOmll9dqiB8fMyPiDdDUvzw22Lj5VeQsMRc_7wx6Fkr1LE7MV-P24jM7Gku2MKeFLTRhLPXfiJXl18gNVsMfkwuWJMIKa4Yd_C7OOFS32fZEPVcgc_pZrIjON9LJiZCV2_2qeX8Pxr93M961cVTruy4JF9zEu4eP1JdwGVyER4bmTzZ8AoOs1QUaFKWlKhqZsUHhobqHJz0V_dXaetM86l7rY8y62SEn48W4UoaTsjJB4vELB-RJkh9JoP_UPWs7mlLwLTdj1Q3LHNQxyYoLvrzP1eZ5J1KL5XSd3K_J6vjDi08RQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lqeXuRCExLGhzRSaW4mMoIyg_mTliZgQSBufU9pbZu9TDrAFV6Y6GC5dJ8LUtabT3xBQo_Mz4vh1adg1EjwHkhlcLZwrKN7C1DAsp2NvyWlm6-wnK7kArEEZjkBii_lfi4DoyXpmC5-q1V-qxM88JwEFRj43ZiOJrXtyMEaHj82S2cjxLWI-gnsbZ1kz6uZXo1Q-jZw5ilJshwhDNA6_512_LeNeftoG9ndvm0rhiqaN326K7GqErVSTmhHM4dfWc6O9xEruMnAkQQ7IFm4bV1j-YDmQMSMb0DIq7XDxiPH50p9yLRI239KOJFhWx1jjrEu8IafIhRc_nB9-qjcjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/daxoyG8hWyuCuGJRStMSalTpfencnCGHGkfw6Zrqo-2d2w7Rm-_Xo8Es1xsQ5hxzYQA_vXJyzXCVvWZdWM4_10ZwuuPoX36-tmtRw_rBg97yX44AnrOmEzacKgDT95E5sPGvNqfekNpPTYuaIAdWtKp6jmWzslnLjG_H5FqgHwpvH3gU7NWE4__lRqUgNhnrBJ8s_USniGTE37sCWwQ0wWmYzeIeE7qIOzIdBLb011CRdjv4k69YM8XLNVzD0irR_j2tMdf8kZnZ3gRC9dea6xq_MmRmQXmPUtYCNebgeu85jrk-CwonMr3s3RH3PaT-GOnZE6Udww0truZWTNWhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q2P7UMGgiZThXbwT_XbKHA1POwYZLLRJBzVTJLce058ZGbgLyLh2Y5fbqHb-KeYH_VAEV5qvVcT4X_8wYjT0tnmr9h3MkLleedcgrkVVBmiXko20NlIOarSE7E5TrkDosht5vrG8BSOSRFPPTgAquv0qDEaH7ocekbYSR7OcDmjs9f14S_PDxYtCxtHuH6L0X5DxnCnD91vSViVPAZXuJMAb6hewgYXGgG_niE5mMRGN531oBHiOpzsqv_1VUfjGMlSpMb_BfCtITAZHNX0_FCcSRAzH9GZykSi82DvhiTto5girdn4q503-5eKQtFGIHNaQSSoklIob19CJJfy8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sLPkN3rzvFvC3t4hZCQkrOi3-Jy0wSpXGC4-Hw22Hy4GGeFPQft37rCbJm10QD6uLz6LBKfNeg_lk4ZJwBQVWvCjymDkO9ieNwXbgpxhSuzrx6nhUk-LsZWfXPGk3PEZa7hJkjiGnebWNs84TXBLh-zXB8Sa4fh5Cznu8xU_SXS5wdNVBId7mKGkodUZ8hybKUL_yMrnARCN64fAbvMGcGLnVymlds4kU24EkcLkLt8kHeUc-lRuWzq2Poeaf_VyMCZVhQkgzhNgVij8yih_DQFfzz5PYk2mTanb9tZfXDeVuu5HLKkevi0tvuBQLxOmyCxmFCTWboomMKYiK401mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/siXf5UUm44m7S3C_ozBbT0QvtaFoTunVUyly6JKCORHr2_xxBLhB4deNM8FFSSkEHknJ56i99o1U_CFApqO0AoxDkV99YM_k7TLTbbo5IMjIZ67ZtxBCbxNXIVcEeLOfJJKreBRVjWRlv3TYlQrCHCpjTPfi3u7CdIZAT6s2Veq1_QJeCTJPdqk8LmE0OMPKD91KnCRH3YaheGhp9tq5It_ug8l14F3JPGpWiywIPHtqz5PVnI9OeEcRjLPh5XU7nCTvfIqnoYRMz0mE9GxJNLwf7sBxetKSxFEp4VZnVQWfhoS4YZEhSkgyBWCt_iVanVcLbuJNCoVWe5dhMCP_4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3NNBj1douQs-3-LpyDr-BS4vP-6xyTpv2G8IPirK3TaJf6eWCKVaUl1sDbykhS2axQoPEpqYyNeYUWLYMEPIc6n7ygD-LlRoc32CFuAO1xXiwHIZrQxjpKRMav6S_6rtuWQdNfbynCogJPQDtqiL5vacumXTG7cb_1cXBZnpwjZ0JF4Yrqsu2jEsEQuATlAR2JpwbXb8BnCJGTeUtha-EWCys2ArhKPFMf3VKikqSDfGRMB-XrtenGTb7wbLdRpnWBerN-7SJRvmLRkW_Kg50N3-MTB5BvSOq8_9LtuBEG5eM8BOkP0jWkhMnWQplEynQCAn2YF32MUdsCCN3y9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sVGGPo2MnTmbxNLKCafYBv60nk5muYxxd2HZ3CUMesHci13vT8GTlRaMreXTbHqlLJww0N-0nFPFfNB61h1NxxM9I51wwk_yd8DGQXmmOTUoJccGUVmY3GayQpAsOUsWQySQzNF80FtuxCP1wJ0vklsl8PkFnCGQkAuldThVSlr46jOLttL-pG-hYti54fdgJv0OdO7ziGRxb37JYReQ0dk_HNeFDnIx3k17-ncOehLqs96mJXgfrfgHywyiXrAddX2zDVjXosWIZEfXTVtwQjAgtPW0MqaJ3yfbcRYh4kAkXnvEuER7oeZwnFcquR-vfImDvUYMSPBov__ywBuKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5-EMJvRiets37hqqyFvv_5jY-2IF1PGJaF6zSd7N6EUkm5u-XvVjPKF9pmb-RVzMkZd3fXaIzSvamuuqeTP_OYqS6A5Q5UaLt3Pb4yhsvVr61K4VvvaoQdREslvp7pcYYylFbvd9GCYkDbdxTQ_fmYWn-IEe7gC0xQx_3z7h_DBDKJwlxBwJInPwjMaQPSrmVeEbg8vIOhlGK12Za7sIsoxgzyCK97JhnfioQTDAOQPu1SpfL8fFf90K5FLxEpykGtBA-m-3svqzmqhmTNiW77UHX8U_dpkfFxE8LHL4faaL9cTo7r6SHNtGebiJNtB8Fxyeh3WJN8d2Z6XwGJEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eiu1tT_vVqGHxH8E3RATxNPmnHWpTmlK802WeeTemIJR8aqYAk7vcNKAR6CwU60zicU21aZz9vrtR5m66oFF5Vo3OBx6dt-eHE4uV8rT0lD2AyqsVELaaUlxIEt-yEqMfggeGekO547j4TPhGA2QMRnWt4GR7YqXbf-kGdns4BsfrpRh0eKFPAZhUWk-RiBPqXDghdnIqjBuTK8SQNnUM3RmGi9J4S_vP_h3g9gc4aMFXW0JLgcqG9J0aL6tqHEYHN6QT75giE8jsaVW-QOT3HQHA9MPDQBmgjYy94A5lHowZJLDb769i7510lPCu5XT3y-0SfdnYO9ZPhkTHkb_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=t7v9dCI1j4oBK-PV203I537SRa0mz8esYFjH4-sDWRRAdnbnCK4eHD4mePUKGC2ge7iuxudZbyAW_1QkGHgd6yNLsg8wLMrYHNhx18nArAHSLRSEJ-oBgQ0VynnXfI_R0Hg-ZdetmznuEr_Ixd_hAe-hOGi8iPAODgZLRUPWGnK9XQDHb4rwW7C5E4vn1slfHAgP7Orpqa_L5OMyV0ou47NCboymBqh2WU-iKtRjPHPZrahrPFVFTS6pk_hdsoK5hPVrFNN65LFTHUZovlK7LJBamMauARZrc1pqtp8DPes8ultc2tPBu3BdmxqU945PqOeShRKGrvWN88mam-SlRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=t7v9dCI1j4oBK-PV203I537SRa0mz8esYFjH4-sDWRRAdnbnCK4eHD4mePUKGC2ge7iuxudZbyAW_1QkGHgd6yNLsg8wLMrYHNhx18nArAHSLRSEJ-oBgQ0VynnXfI_R0Hg-ZdetmznuEr_Ixd_hAe-hOGi8iPAODgZLRUPWGnK9XQDHb4rwW7C5E4vn1slfHAgP7Orpqa_L5OMyV0ou47NCboymBqh2WU-iKtRjPHPZrahrPFVFTS6pk_hdsoK5hPVrFNN65LFTHUZovlK7LJBamMauARZrc1pqtp8DPes8ultc2tPBu3BdmxqU945PqOeShRKGrvWN88mam-SlRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuVHCY3d7VT-OxrgE20DBCO-B7FMJTklh0J12OfOxNkVMst8OvFSxnbNyIZpPJYPlYBUQ4VWITSTNrghl2EfzXwbawGF4BlUve4A0bxqY1Lk219NiGqcnLaE4tTPlAEBBnJm2fs5thTGSl_HAmrIxQeLc2IK1JvjjaHIL_NpXyl9XYMoh-K5wwIBgUmekvEHG7Hh3vc53hW3SI8ZgozWM7PR2pK6H2ZCznfvGBe-jQ2EHLTpnO1pUqj717EyFRo2sojiy-ZGhsX523KSu7898BEP3y53apNhx54tEG4c8Wbv_Vh6rgtdEC2gK0mPbYSLCe_hG1OrAuagowvtPBdgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JR_tDgTkKJFl9QKg6-kUVegnIMm84Ht7KCQQ1bo6GUNWiH-zsoEsxrL2AR82vUgrhc4Gc7eqnKaMTiE6mTqBtolxIQcmcB3qu8k-cbd60Ss72rUIPF5VtTFKtlreoJKNGPqIWHsPxuRaiiX0lY8W_tTzZYpEYlXzdQ-GEZX8XhJLL249Gh03QARHjyb5VV1YOvqs9FkG0lYEOxN-nn4tR5DpkhQA_PHljz2WZsWYdDSFih68K3UcMhX5rfy3-0VYrcaecUfa9Mjs8lgowaUs22z-g8ocNrmRGVmGe_d1jH9QxSsV7AUW5p6OG12dZcehz7bvO3WwhF2bG_fqCcjzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tYM15J-sJDuMejgfZ5RU8udYnfVql5YL_Zr8c6pthWsn5SSRtHlHaN1mt4Y91Jk5TjIKCwHpRKMIq62lHQK5kvpBDMhmD_Q3rALm-3xg6vueZT2OwrivXqqJ0rLWjpsecsyhFM7IyKUgkxzZYVx1h-PP3Ho3_nY0baDjfX_ew0NxNBeBWYcvnrdxZMjEzkzeUK8mXJWM6xqU2I7ZbQDidWhu9Hd_SGKzNmTgp6WdM-Zxc5PxNar2FEVmQ37G1KZt3ia78fFaVaFdRGBDIsY8qVHgiNGAjM-oYfcBJipW1DmCK_H4vbl23ixeVsJAxrzTvVeyl22kvKhrgzhPpZx1jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gHF0H2hLg0y2ka-73OGwxFYgzusitJUbso3s478tYMcPK8QXvrXtXOCXT4rPQ1QUDARDVcsMREpaxL1CvW-IwiZdCbjTt5HqBKmDUgBqL2RFFex7QcZ8bFp21mFSQiTIJgJpHaD-iSohoYZIUxdk9c6FwQLTgdOiahJUCUjjNN9ZjLAwb4zDIhvy0Y3Kh_XtXhcB-KLWWFxYoxQ6oA8ylsF1jLJ8h0imiAoNSGfDidgesARF3WFpHXfbIIMHcR3HcjuJv8mGNWQ-dr0CUDvatdIYgvwdOK1c4mm9N370lJBk7UgoBGEzF6PKZHjrMgXmsuNFmdYu1Kzah0jcxCsSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6tYUzT9broVza1uQzgBd8qtuwWvEW7L88tS75ioR8j6OiFesXTnzuogYlDAPQv-mZAIiGy9-tVTXAcbuDbRe84T3zwey4vk_I3oTnnjgjJLtqrxysEcQBnErmH4KOxs8f_BHfYw9FdRd7a24eSwi4xQT4JdbHmPmD2zcNfBM6y0DkXaTFUaNcskxhVrYa1dAOk-9nmuS2qPspuH8SQmAxkil6HazM8Tawpa39weDC6azymdv_XcWcaLuX9gQB_tjzG0HZKmUS37_9Vds4J6IKOdcdfsOiEV3b1-Y_qOwZiWJ6XVxgfPpqv8a9NUWG9ew2DcCiAFU9gwHKDVSmlUzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GUIsN2fTP870jv9S4_ArOeYw6gLslRvkDWXoZgVidRyCw2NXjFNp6c2yTUGaPnJz6jcHHsX6gAu8AWyH5LsIRfmZt_STbEuV-4e9bVGB101r5OFiAcv1MV00E7yIMqXjxD6vZkuyTroVr18j57_efr_-rS5aQdKxMwidO-77Oh9QmW9osnk3b2q0JwyLCsDWhbjN79298-fOx6tRkbNsN6ZTY9aJx_P3JRRlRmyMnJDmsZqy79glJiPIfYpSOtNEZZQs22R_5e9u9c6JA0ALs1sO50HRLcKVmdOyCxnclzn0XBCkuUe187bE-PreIom5fvnBcIXhwuWRAwHosOniMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYdI1Xx4xDqsPkUpk_aC5Zu1G5ulcMJztILOG3H0kWrVXeZXx5B9zmrJlgEW01O0dZMbwkznE7prrD7-rS0zwgEt8wmio7zIvx3_tCgXSplz4Fd9iWpZsMTjtr60ogmuw-etLx2RybuobSeQBlQjNDPNi16vgOSUAvyUjQpGYRjleeAWrveb6ct-Pp-yjEZ1I1tkp9ou9GPNoZgfhz22mWVF1ctL8AQ5NSRIZ1T9axtf8ZwhQH2Ya4Ou-ziITNgwXJnWw2MDE34jY8warocy49emw-c_BGQ16tk7sv3vLkur6dCAiJp9df_5jRvgInLSrNGlKbbIBQcGwQrq7RUkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOq2DNpEeCXw8XaipKNnpM0Vx-UQO0C5z2c20GkISdyv2wyCxUxIyNu9GMPwfSnmUMiDG4PkpeuRajnNjGSIk5R8r96qK4LDt2oDY4CfYGjBPnMNhYLfx8mnsw64QOYQ7_p9nJOfIwxphfNpudn_E5qGYuHQXdbif09_QsfT9Fqb-ccfMd-3YwEOUL3m8_QYK75nGYZ1kTj--i1Tas-gP78Mm4CsdNQuG90j-F0DGAlCE9W4hVNkbZpMjBa6Lkr0q0AYyh6M2CIb-RqkRimQqA4U-MvNBtP2WiUhTvtVZiqU2yDs-FlLwjYW0KtGiysb5iqKvHnJADxY77OXcYdTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtTgzsMeMZdaVHohB7LcybdKmWNQlsaE2gtC5dJ45HNyR8DMcY1KWFBbysSyUTmUHnsElkl6XvxLHnkvB5zqxAI-HicEZ0hwIH5rmCCzpdUrNWGsfEo_vqgAStJDvO6lDbJimu79ywjWHCPrrBt00zXYmH34j4f2yUYTFTwHcHzg61UnyqNfLU4vTvaDsHs5nkx6YNaQQfkEk4Nq_POdmelR_Xs3pY9BdJmpVvpH342GLm4vie6XOhDa1q7_foKC9iN1bQaogb0CTgpHIusw2IYjrQY9oHEZaUdNsw6HfndLZlmUhUsE4jPeufrrJOAtPOgR7DpmA5JOsX4rghET3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hf1BZbMpyjW8xonhb7DuJrb26UTBGQmr-70857MZ0TGMo8P8RIT0L6IogQRIa0Q2t33Xglnpi5d3PpONRluIlcXPWTKd-xmwCRNcVfpXnGgXDEMmAacjLDRr27aMgm3iyv8OvmnI3IbXGjw-PJDeJsskvlqXL0MFsNuH21OvhHj8zSPeQSNyC_46aZuBusVZ18TOeDvaBSk3rsCEL9oX4DJaYV-8ZQUX5gAl4luvEYnASHMMSv8HN3K5InYN231Db-7g8LO_jrhiuADhy-OU-vbhGAkn_oZL774qVz0gcYFHL6xjrdV8KmkCgwwnxo4RPZSXxuH97JNl41PwiFen7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REjJeTtunqjYnyaWaD7DzRAI8cpyHZDOhxamZuR1u0NwNEYw7CyrxjCjRLJnCT38wpUwPbggxHA0Kix86g_MhUU9k6oPd3Cqf_sJ7VzuCWCicZAXZroA2sfvXtvwiK_B-h6TpTP-BPV26ua_EP1WiQKttoIGow0vRjDcd0UVBfnDA6uCRYbHX6ybc8sy-qS1SpwhBqTibTRLzl1WKDjS1RVcMm1m__4rHN7SRrVJf5bL612Mbtzwu_SFwWLTqxAQlk26LX8--bRshf3FZtCQAGFT9_EvYMWHQBCISUDuR3eiK4Z-znAzdhui0u2tBnw2vF0zLCILw7pJzrMbQJOncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gTtyyx2WVUsmZWwoSY9K3q-7610ThYcZQm0QTR2lL-53I6Svfl0zoyzexlD9Idylhj8qxAskqtoXK232nC5f5WHoM6G0lLd8mLriE1FAEFeu-Q6zyPBLDzX1o0E7CJHT_B8xseeLVHIBcxpmAvm8JA1beubbpn2f2CzAw6EwswxfGuy2NwVXgA60RqDcGr-st9FEvegg6Uom-QgeVdc3RSbztu_loUvrK5DMDVMQXy_y0WEJpvl1_kssmS7AqkIrHecXUmxFdPsHYqnloVctYWNnNI3mlcsoPMx9X_oeG6_ngDyGceAr4VmQmL9VLwBkd_RivyAtTo-y8YhLaOstEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nV5yUwpgU94_Dis9hCMllUiqHmE0wOocsmHC5cqO-7CXGSHauBOG7mAU22389Do7bDeKS24NkguCvp5ZS_NaInh560klG7VU1XVvUNaHZSB5Y6T7Zb-lEVywzL3KM8h6kChGTZdgXLfG3raNmgsFQ8VQkgP5OC-AN3e4JRNUSkeK9bcT-2osxbElCiNYwAB8px75ro5gmpBDL2NW1epnYt6W5oWezAIxbV76M2iQkVZAjY0DcgGqYtTKPu0wkvMSdlkl7g6d3rnA7lZU-ZRRqpXWt7a94sOaOhWX3XrqXDQsb3egw4bf-Nbr-FsqACb4Iv-Xnnnl0qyEFO8vxNEP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg70zbDb2Rm1U7vh7_wFU2VLo9CM9s-dUjjjnZCd_5y-VMcMW1AlOWA8yvHe9RVxDREtVsbnTdi0qsAT1_5yKpVgAHbmixO_MnC7eK6JIbBlJ-glhbN7YSiiPWGxSaVUZnBvIc_0t0D0R1wEGw5uZ_Jt4bol6qbV1cwZGqNsurhpyN3BM4kiFJTlvMtRxC9EcfUBZH4C0jdc-7Io0uGPxJx4ol0CK70xwI-m2JkZqKKzrYJX9ZX2cjqBT5ghyuPSc28RBAVJ-lqpSO5LozPtYUZnXnhd25_QhcXtSdh7BNjk3pZR-LTxnV7u-JHXDe4uSOluumufB7aI41HuNmuxCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJRewneqvBkoyhvesi_RM5flb2ZnBI7lDI9fj4EqLpJLIQUZhsRGubA3J86qHC1fMMZbXcXFjlaahGb5tk5XR1sY1sKC_6gFMqg0yvWLjfWA_Oy4YyvKxqFUXRue4eDtoS5ID4gCLmvp7vzIha3wEj1BYZ7Qs8uWQQbnJLmMGJoAXCYJ_rK8s7so5fmRLaNSAQXvURKrYwrbZjjCm7x0tNiFAKbR8q7aXNtwayKaoze8sZ7aRZNSkHUdtEyOofAQebeRLz3A5yE4WxRSOWzh9eo0OyrnNWml8PXxPbjuVBgFl-hRt9H54N-QANjrWKuF6v3wZvpiQf_3GmiLeoeF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2Knw9Y5IReHjr20bUJuD2jC2BI1Pg4idPeYQ9L52UIBbdWcqIyhA4J3h7w6cNX5F9ZCxdH3prJEaHDqGmZniCNCwkvg3D3M8LM9TpHZW3ZbT8fsSGCbCpLpH1npYChsmECjSe8sbfVMXnBBmbjbimXlp8CQ29fcgiS-rGcg1b5MBNagpDXg1sU7xPZJ2r3MJl6BO-MjMdqgtLE2vp7kMGjjimAbE1EU3jCFQ80iaAgCtDpDfVRlPfgsVntjzID39FCMSCBm3D7hW8KU22J3EEqQcpD1vF5au8Iedhqzd4VlbWcwZq1N7iXIeTCEy6ia3iOp2G_7lxpTj07cFTAQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZLNIeBPRhFwJh8YGMdI8fXQ5RZqkvEYN6W4mhuYK6CRBsi306atcbmZikTZ7NHb6EAY4_l0XmzSv6ivLtmRUSP9leovP5qKwd1K8BTKaG3lvx95ANwtxK0DLQA5rdjDrRsFbHgHKYSWyMd_j8ONOykdTsHCYsl6NJGmaOIWw7geES7F-hqSr6eDkUMTq-Po0iT7hLGwg-1bndHVCtDOd7xHtwExJDK_WjEy4J6BGZ1NQw1C7Jg-uYDY_sv8CQrzAiQFV_pibMP7yqRTH6xOoUVFz9-S2Lu1pWDRwlgXqlT4JTi5qpG5f3Aaex50Q-m6FoaaNOIeUKsdUxLZmWdaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgppmT5z9aqHvYM1-fpboufL7tDV2iLv-z_NSTUWcuQ_DSGYV4GXSQ8azqZumxASftZ_oZsEQ3gNuQfj0nupNfxN36Z7nONCC4Ofkyf0Bq_FfPRu4sGUa3yinyxLM7z3BogB9blLFGIBofw1Bny3LEE0sNAj7inCdMzUr7JakW_dBP_gNV4c-MguvUEqT8WOp_HvmQXTNoTbal_ykIpfMeGBc6iqETw6VFEQFEXxZ7RXABsPawIOX1acxucoyIObzcIaZT7Sjk-1WAARsWO2yZEPqQT7llmwtXE9ezas5myU081N1tGWgUQerSAfZy1XT2GR4XtNUzJC6vE7tHGHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/POS7KS6CWMCI4uZ3P74teFFm2kvJ_PQ0pva5V-wJkl3j7VU0fcgvox_jd-hFgms6MpuVcAbvkbM2KrBRamhw1JZAbtxZj0eecgkjftTSN_ffXIZ0HIIQAdeVUMFz38NEpYbvB8NG8yfO1DXN_eDs9LD2EA_FiMMeXKdG5nkbdzk3v8ek4XrORCqQlsqCrW3bcB1DukthcAtV582JUNPow5HUUTWLSX8-UjFbHD1DfnueAQdXa4if-Dxou8dAq0-5vJ3nm4uJ60Fu8fL0bgQFc4EiWwEn9xo8YOcv7cbDgZ49UrREcdn6r_7IoD95gJSnzykyah2RngFDTwUw8g9XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jf4QDom25ofWInep3oP5dFTguet8uMONSVQtWxskonfp_jsKrwDScJcs7p9vV49dHWH7JLJwpOvtVsStoMtl0wKaDjAbDOegZY3EhhLqs6_moMv2EagGan74Ysn1aIrwIniBhX1_ekcq_Opuc-qhCddA-Ndo2r3EVtRzLr-7qII3qP49RPiZmb6YqYnhXuR1wXlduICbQKfXWS6ctoleUcpa9rmHROjk0DrvhG_cFPcZOd3QxiL-jMYO-7hJ9RAhDnzCrDOjTkQT47dAC-M-a44P-tpSR0oTeYKURse6AaRf4p_1D5A4_PIZz5VL-vOOKUQZAkp3w65D9zpm_t2bJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guuMOj9oArh5oL18iRUlqztcykSdZz7U3L7fPUxH-vFnuNTZ3mOBOBtXq8sMmYO-tXVEDQp9VWSTK6ghhkEWU2a3tLK6pnWl0oTe0fJfR5QBlxV6pFmggFH7_xl9MJfdhJWoLRo5xME3gA3rvN4AADFELpmo2mwbsdc3SXUZCvcZy9TpK8iciWWCVGHl23CO-UdFwNfdMSAr_YCkWVW4Z2mfr6D9zCYmU9ef9iI7iCNZypA61hgUqRqFoLchwDcqWZnkL6AotGnnK5CQ6NfySZ5AceaJNtSBlq3pWBQbBzraI1hw5WCNNySjCW77TCkMlARk2kLXAXEFpSyd0u_2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
