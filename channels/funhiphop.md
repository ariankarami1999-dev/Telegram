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
<img src="https://cdn4.telesco.pe/file/DKPasx_i3s3ut2xohVdqZou4gfQub5eBLa9_XINWO5BxsUChWTGq2JK9rB-bVqOfYO2azjGJnrdkCvmjMrkM09-Tq5wKFiRG4PWwrHg_rYx7tCvvAsb3M4B5nYXuELiczHaAy8sUJVnJHK6K_rBTCDGS21fTJQgrrKdp8l4LZxm9nCkvPW1rTWoWJ-IoSpcaApDAouEqCp44u7_NJXtwkD-8FK1TsnQ-MWtOgR2O9xHy139e81nsphjRCkHwhYxTHXCzCGDXHto1Jp2Zgd8Ra3DJltlgLyowoSXAerBiyMca1wcMl5xYRDmjp86GLUPUPZG5Ty8lGN_h_4l2q2kqAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-77333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کان نیوز:
تو درگیری اخیر آمریکا به ایران ۳ میلیارد دلار از طریق یه پرواز از مبدا قطر که تو تهران فرو اومد پول داد تا دیگه به اسرائیل موشک شلیک نکنه و آتش‌بس کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/funhiphop/77333" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/77332" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه
این پیام بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/77331" target="_blank">📅 18:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMnkKRzTyiQA2_VkEcJtDZUER5CT-11Q9oNvHIsAKAqdWQ1wEyATHq9-Lbc3q5Mtudd-DZv3s-8Wj1KC495_XsKocSuo-RHxoKUcK4Y1Ve--fG1DC8keBii3qXy07_ZOwSyN-XYWonCNe7Gyygq2Vv-XmiWJOUkc-w3JDDk_GOehve9RIH2rypdv-QrUfaN_9a7GdbRFDM64QbVfF2zERaZUoIgEUGwi2RMTA0nK-Ig5btzja-8vFcuy9JWQK_4s4NS2ar0nh5opAft4BItT_NsKRlYKX_o3nGUfhNGzAXA-6mPcKMDRYmeIQbVVx22-zMFqjSOT1dwklq08Asn7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد مهدی طارمی و رونالدو توی جام‌جهانی 2022 :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/77330" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/77329" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9l9CIvZ1TTvnoD5RAUjgds23GuvHnFQ3crjpz6MW35c13urgEBDZaA2GL7pbMdFaJTMEJYvugok2ebTb0HmSX1-Hj1jpjEgO8c91SUwkJDmi6QFc6qpU4lH4SW0nxa-OCEz0lsFOOTHksx8vvpAEknDcpQZoEru6txt7rI8Q0-fWzk9mNgpkC-VAWOc4vlD9UYPEWpZtdUyx5-039wtjBK7YvVrMxzUDaLnYv9GV-5V3ZDB4GyKB_FukvZ0hNmsxwXPkoOBftE0YDZHdTXXJeQ5bM-AWic5I9abs1m0B4lv3zQ_6kkt6SaHMgWdqIiFoP3YtvILW4oXl7hBBT6AKQ.jpg" alt="photo" loading="lazy"/></div>
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
کانال تلگرام سایت: g19
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/77328" target="_blank">📅 17:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی حکومت طالبان:
صبح امروز عده‌ای اغتشاشگر علیه امنیت ملی در شهر هرات اقدام کردند که نقشه آنها شکست خورد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/77327" target="_blank">📅 17:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/funhiphop/77326" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تاثیر معدل یازدهم مثبت شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/77325" target="_blank">📅 16:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یوتیوب قراره رفع فیلتر بشه.
@FuunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/77324" target="_blank">📅 15:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77323" target="_blank">📅 13:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=dlTAySJzy6dQL-h6-x-LLhKBs1B-Y9CqISGxJd4SaBi958QGntda_CzbXeFD-Qg5V52GBk_3VMzgdGvBwEZW_c33Fcsc5OyMoiURTeUeQ3Mpw_Jk_l8ZMfZhXRQX_voPF2IMaXVjLcrL1sNUHRv3xKjXg10eId-jviD2LYG8DZilKAJeDzXP9Sgl4zMnEllOt-oBpKHfs_aQkNH2Q43s93Jd9T_hi-jTu3HYbSY_lyB5UTA21sW0CIl_4gdvdiBfJ5xq6vB8GjgrF1EPrEAlzNj1h1K2Pyd_Xj2bG1loBKU3QH4ke3weIzdmZ4s9CNAf7aikWpLkOD-ETPpO-LFoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن تا الان یه نفر کشته شده 22 نفر هم زخمیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77322" target="_blank">📅 13:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو افغانستان اعتراضات شروع شده نیرو های طالبان هم هر که رو میبینه مستقیم بهش تیر جنگی میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77321" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if_N7PsXwbzsvaWgRKENC64A_W7k9R7z_Kcj0E4kUsIhP83fh1xALGCu0DNEB74E33APN-gsHOQ75xCdZA4KEBFcNwSw4ASKtgBHOEh8alc25gHVSh5XXCC_KGtEMOifAQipUhpAbk4hDk2s6lRtm-wFTs8oAV1x8hmR_q9tYHPvwwVFXR3X2DfxQyNo8j-0Uvq7y3_eo7T5R3JpxAE27yUip-4F5in_mcAYNXKM6oyTrSYHIEPUW1j_Y_p9z1WnYAIzkn7dIliyB81NjyFnjPbQJysoJTAmJO5M8PyFKM3kPW-K317ZaAWrgsY2o0GxpBjVLtJLUr1FfNsDCYAG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین حق‌پرست، از معترضین دی ماه به اعدام محکوم شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77320" target="_blank">📅 13:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آتش بس vs آتش کم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77318" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
ترامپ در واکنش به سقوط یک بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز اعلام کرد هر دو خدمه آن سالم هستند و کسی در این حادثه آسیب ندیده است.
به گفته او، جزئیات بیشتر این حادثه در گزارشی رسمی منتشر خواهد شد. هنوز علت سقوط این بالگرد مشخص نیست و احتمال نقص فنی یا عوامل دیگر در حال بررسی است.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77317" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شدم مجنون مشهور میدون شهر و کیرخر دهن مارو گاییدید.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77316" target="_blank">📅 09:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=IySSKX6BFHG0u3XT-ylFQQxSmd4zdki6izW43IsPi0Ta0hdhIMiDHBXptWgMeppsSWnTYf69aJHvMwvVZhjJdBddzBT4qu003yowSZ9J0uYc7NxIukn155qc8oBx6PP6xEwkaltN2lc7_kMF3_isj8MurzaAOpEF73i3soI3JVw_efdnzu_uzv4Bqh5stN7kIjWYon10HHLdFw_rvfQ0ZvVIPPp7Lo1NDI36gDtxk2KKiJdwjiCHXhLuzoZSrEytv2oGYip0s7SQDIeEywwWxdDWX6ZfMwr_yFH5S8BDKBEDAo3MRhhy5DCW-YxRhXxJOHLVxWBpeh3JaEJyRvr17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd5c51779.mp4?token=IySSKX6BFHG0u3XT-ylFQQxSmd4zdki6izW43IsPi0Ta0hdhIMiDHBXptWgMeppsSWnTYf69aJHvMwvVZhjJdBddzBT4qu003yowSZ9J0uYc7NxIukn155qc8oBx6PP6xEwkaltN2lc7_kMF3_isj8MurzaAOpEF73i3soI3JVw_efdnzu_uzv4Bqh5stN7kIjWYon10HHLdFw_rvfQ0ZvVIPPp7Lo1NDI36gDtxk2KKiJdwjiCHXhLuzoZSrEytv2oGYip0s7SQDIeEywwWxdDWX6ZfMwr_yFH5S8BDKBEDAo3MRhhy5DCW-YxRhXxJOHLVxWBpeh3JaEJyRvr17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از پیام حسین رحمتی به برنامه طبیب :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77315" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5AvldXVJe7ABs1TsSKzNT-x1sQKKmMC9fvk7FVpjU8Bu6T6vP868H8RYoL1urBUeAL9u9LJJVHLoJ1WIIGUGOYdrFNjS0Ye7gIDbWmm42jveCmLdbIbocHzqTZV6o-rLoq1P1M5lqDntfMPqb32hK0rq6kMuBxtazfe3c8efr9WrFpfQKP4Q48quNMzPErVhLpYS0Yafavml11ay2VWj7z6Sa7efaQSzzxOvymIWc8JPVBsWNIvp7waPdz1ZxNhmBbe6I0x7lXK1YmfwfzL6qLQLWuYMx0ZlYA0sZFaw60ionHltpe_uRtVfEcihQc89_aDncIFW3rwCQ94bU-z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
👍
ورود به سایت با فیلترشکن
R19
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🤖
ورود به ربات تلگرام ‌بت‌فوروارد
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77314" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMXuqdbaWwKz2W1_E0gYCH1mCYTK-W5c_9DPIaJCC2H7MklcLzDAbYTmMIo1iWPmWAdDQL5qzU9LKA9GNM_KRtR152SesdjqZVDZgbzhC-8oHSnDQcpoC2HxvZ4VZkehjIpH1ufjiIECMoNGIFyNS2gxIH-Y-jtnB2UPhIRF4ej5hQmk7SSQK0FuVZhKGDTirVYu6f0Aao96zdklO0Pt8G6_cnM5sHNzqDfn2LfXHHsG_Unmn13-1bzCe_YTq7uTblotRHZbPoOOqAUTjfG9bOso9HAPB-htbnZldCNRUAXYJQw3PX5-JKROY118DJsurUS22K4-YC0Q6LjHllSH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل این که ایتالیاس
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77313" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعزام لشکر  82 هوابرد معروف به شیطان آمریکا به اسرائیل
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77311" target="_blank">📅 01:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiCxHoeYv11iIkV0Pg4iHRKz1aKs8jB9VGvjMZk0Lr_Rt1fAoHMga0PEwVi8lr7O_7CKbtr9H6rEMv45-3e74idDJC2WL89T1emAw4QoD_TYSJ4SUPMyVKyHvcOzs4rk7-2SaG4RFs629uz-SQCmlZuFWpZo9intmtYptFNHRPsN0ktVt3S3W1lfWxsvAPZLkb0-S9ntbg5r45PHWyc4O7p6OEjUZ303_laAxZaIOSGT_AxVNTh_zkSx2KfkyKOtPMr9o3TQ0sNqRVXcOWhlehOYCbukscBxIWP0-h7emqQojpo0oyndCG9CEwmyM0NKHCD7j-DRS7GAsLaSx3cQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا خواستم یچی بنویسم یادم افتاد چمن و مهدی میرن گونی خودتون تو کامنتا جواب مناسبو بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77308" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران به شدت خواهان توافق است و ممکن است به زودی توافقی امضا شود.
این توافق مانع از دستیابی ایران به سلاح هسته‌ای و توقف غنی‌سازی خواهد شد.
این یک توافق فوق‌العاده است.
ما همه چیزهایی را که می‌خواستیم به دست خواهیم آورد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77307" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک مقام خیلی مطلع و بلند پایه ایرانی به الجزیره:
آمریکا مدام پیش‌نویس تفاهم و خواسته‌ها و شروط خود را تغییر می‌دهد و این باعث سردرگمی و عدم پیشرفت مذاکرات تا اینجای کار شده.
بدون آزادسازی پول‌ها و رفع تحریم هیچ توافقی انجام نمی‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77305" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
نتانیاهو برای بقای سیاسی خود در اسرائیل نیاز دارد که جنگ ایران ادامه یابد، و ترامپ برای بقای سیاسی خود در آمریکا نیاز دارد که جنگ ایران هر چه سریعتر پایان یابد.
این تضاد منافع پیش‌بینی آینده را بسیار سخت کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77304" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اردوغان خوشحال شد
سپاه به مقر تجزیه‌طلبان کردستان حمله موشکی کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77303" target="_blank">📅 23:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMYfpCanX8HaRzbvuVBrv_aUuUt5eEZ-B-CnIsbJ9MW1VLj8HUgG2yWk29WHRsFI3_CP9xSN9Q9b-mlPeWlQPnGyWBYsh7sFTQx4hy7Xa0IJcgjjCCuQ8gfqnXv3P92_2wD3y8IsAOt2jCL0KQgofwLpEUCAa3GnwkI764P0gQUktNzUHHPwNkiDNu5pnOLCOKX9_0wPu0msIS82NWfNQLMHZjjAwqUwvt9uWMoVTY_G_MCIyzzsLFec7g5Sg-zGp_-Ebvh8xCBQ-Rx14zQwCb9evPkyhQCquybIu8jNRT5Z3RIIuWmWquxYBEk9Nw_AKGFKcgn1gzAKQTE1R87Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر چنلیو دیدید که اینطوری میخواستن خودشونو مردمی جلوه بدن و بگن ما پشت مردمیم
باور نکنید، اینا مهره ی نظامن و هدفشون اینه تفرقه بندازن!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77302" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تنها جنبشی که از نظر علی خدابیامرز درست بود جنبش سبز بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77301" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یادتون باشه که تمام جنبش های مردمی سالهای گذشته هم راستا و مکمل هم هستند
اگه کسی خواست این جنبش ها رو در مقابل هم قرار بده بدونید که به هیچ وجه طرف مردم نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77300" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0pDo8m01_r7I8yFIwfxwbM_4_su_haSJ_N1B_van9Vl5qyMqrsMV4TBhnzxXKINZ_PqmEhCmnRQFbbeqo-hNaGCCQ2pLtdWCFmz1fnZVmVM_slfVrVoSKm8iLwFb3FTcOh5e-ZU0UZjceC9WlbsZdb_kJySphSCVSuT3q7wehC8M0bPZRkRYnJaeYz34623BS7Wl_uQkrVqfGt_o_rDXFCD5j4rAJf7HWw-Jhri9j2t56RkyOk1ecoicL80Y2RLkyXFDWLhDEq_Udt-R4KGPn4YqORSAVmWF4_lbQTzC33mnGRzCglS-tVR7mJ_t8YaXaJS-kpKYT3lzsRlYgp39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اینکه که گفتم جنبش زن زندگی آزادی درحال‌حاضر مورد استفاده ی اصلاح طلب‌ها و امثال فردوسی پوره، یچیز مثل همین اکانته
🎒
و طرفدار وطن پرستی با بیو "زن زندگی آزادی"
که همون قضیه ی ملا به ماتحته‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77299" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شهید واقعی زیاد دادیم سر جنگ عراق
که اتفاقاً اونا هم جاوید نامن و جاویدنام باقی میمونن
حالا عراق کی بود؟ دشمن ایران
۵۷، برنامه های انقلابی از کجا پخش میشد؟
رادیو تلویزیون حزب بعث عراق با مجوز مستقیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77298" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjnU2x5l54dojK_hWCnzUMcqXFwCcrhrKZJgBz4ak8v8bNN7ifDcdU61Wc0K0xvlSo5rdUBxnOnyHEpcJXHm7iA14Awp2bYeSr9EaDPs2vPE8cL2sv2f6hHarhxRZvkourMeJJxftTLU5TalTlR1J1HukFMZ8IvUdlQ1Yhw3r2vxUL8XO3J6NPOMzxKx6ShKVPZbH-t3hC03L5KcdhscY7cDWmXBLLGrQOhXMQiRYcFVDGklXyFjvtA2MMgZYicXm0OB6q_ZF5-F9Ab3yH5gy3aRjFqCLSm7aB2VPnjWt9-6Ti30wRF2lXMpsWxciekUU77Iu7rTaq2Ci11PxjEchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqXa8eeDGpKP4QrWoO1KN04b54pNjo0cmPZiY93_aAGJFAcOH8VEy_LWr_6sCzumPaigNq2iWKdmqxFeayyUJtJ44OXT-l5txEh_1EBHaIu9TVOX09JE2u86YIEgq9g51-kGANUPaTMsfST_jNYMdZkDj1M7HvdiKoqMe-Zu2r-OArytR2UXOCcohCtyl2ORe66k9CKfWZ35HY_4D6W3I8IYeB3uAfRSPsuu-4x46fNBX2QPnLO-csshHoKofm5kXugiv_vwkuZCKTyj3D9TQ4XyVQqJQ6f8daRz_Wb7750Hldj6ghSYY4QbgCLTs2aPje1AuQAZF56I8dgFK-aYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivQD3SqZ8KbDEu8JUNGkp-60LUOh_9_aJPub4UdQZ9w39nUNTQTTKyhuv-E9pkuUY87dcVr6Jxp1Ru2RHrovilbBd1R1_uaSi7sqm1mWFxpu6t4BoL3rHDHssU1A1kXGw0vXPYAmSrHSRgR4wApxP_XRpbcxHUU6fCQ90gav0T7BUD92SJV94bADrV3agdH1rE64FUxkj1PZaUvzTWLCGMdt4-DoCwFsCU1B_aG85wNMLGlmJcd8OkexzVbdp5_gZ_o4wlOKFhN67fipy7aVwJ4a1IecaYI7hNAQ4NLdFc_9Qsw1TrBDWUWevcj2lVU7eS1TwGkVF599o7NJ5M3DDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjddRPDSp76lZryzS73FpMJHol8v-JhM0G7MkxKyJWmvkyQ-r4hXYCa3JANcXYh6a4DJrrVLgtAndN-nOsSEhu6LV6YL0Vnh8bSJujcGRcglA4_CH03W0WYaZhvR11y4jVwyOfgkTPY64guBB6cu8RX6NQGB-WD4S-6MWM3Q-MK46tdeOEdbPbjJSYIOAsCs4d0atcgMFpx55S9czQ7mBJvzirNTMFYZ5b7yPes8ZH70KeNH9iI_1FW8yXUXkmX8ChRdgeqCzzJ2M1ad4jOnHQsGZlNEUV_kemQl90l-BOqKfr_HuRBvOK-GEDF5bSmDUjdZFubxGn5y9qPHuL4rJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkluMdRX7iqm6oPg9wO49BE243JN4A-hOJufb2fqfe3jayjWtsQv575PalbUao4fxFqarf4Zx2NtQSS024MyXFDL5Y8Qz7alAB1oWYGxvDcKl8nW2--G48yVPdf2USrwIZMUHSuKfczWHOFwgwYzRsUNf2VwjeKdffv2lESFbHaj1tuH7JhwZC9FrVu4Th_Bulr2U8g13mnCFgcDGJVhk6fQLH9Y8Lw2TvzsezRFVTkeIka0n1ZB_A5fJ5DZxSPPg5CiyJFJkKqM28oP3BJihyv3bTDS0NjROwhAeWfGRe2EFKDyYPd5yCGdwUmhWV_vgv79kefFUa7lJldHJniZgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🔹
ثبت نام آسان و سریع
✔️
🔹
نصب و راه اندازی تنها با چند کلیک
🖥
🔹
اپیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jC9pBPjf2Jcx7AYM_tiE2bNTTfs5_EGjG5MCmgEoDJDlQfL5mlBcsaCF0rGHMThaBr-9fZOLMvYIM8yxqG7zRxTlobATxBcBPyJHc2gsm6rCPsHJkAo44PBU8aGYI7gWr-IHKcboGb-XM9xi_DwXt5gjp-xWj98pYNWGlDzQpot1tbGrAPer9JPhCPQW8kWX-TjdhkFbwlytsZrjBSzq6PNdE3i5DjItJ-YllYUct4caUnR_VPRl8X0DwNaHIzZ-jZ2QY-D85O1GQPl4OrWaUU69tfj4Vfjd7pZlQIR4Kb7vOXA5av6ukq27xXhHcjmNLDxWvlS9jFyH9JZtpycuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎊
با لنزبت، دنیای واقعی پیش‌بینی رو تجربه کن!
💳
شارژ فوری با کارت بانکی و درگاه امن VIP
💰
برداشت لحظه‌ای تا سقف 10,000 دلار
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🎁
جوایز هفتگی مخصوص کاربران فعال
💵
پشتیبانی از تمام رمز‌ارزها برای شارژ و برداشت
🪩
امنیت جهانی و بیمه شرط برای حرفه‌ای‌ها
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G18
🅰
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oebJwouBTvd81uDAupBMQBfCoBdxPYr-LWEmNbZxeFvRp78BFd9H9PwSI5KwTXedc4XQq17T4E_N0XMYctaMFw_Z7iugGj1T6JdYEOlBlO8lX1-nLmYG0kkPLvE1Tpk5RQNs_Q_hu0N4CaUcFobgdv5cSAJzVq2-NvOMB34ma2ti1o5aaFZFAy2O2cdIg106g1GnAR2mZ2-4RBHokq_oW1qCkVTRCiYKKxk-tVM_Jkh1QZ0ljl1TRzZ1D5_RhU5DPR3nmW2XNacPrVV9m4MTiFdbbqtB7XJ7arKG1fsujLB6wKZXD6bOla6oU_H5kOLeIAiM9bqdIfb8tkXAgHc4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9kivU-R0iVA9nafmRufRWtMd0LHT8ngm3mGSyQ9WWByj26phH5LjtMbMBXantP9jsHpsy65UzH4b6jHyYNgevQa0wmZH_iFKyAGD7CSQ1h52vPFs6nz-RDaAsgYO4ZeWK3LQ4NcyWJ05bBfdI7l0b1ZnZYOZVnU1BE-mJz54n4jXPCxdmTkl9TRKBZZJ6n32asgGVrEYvoRjVrl-NU07pNQdBrmU_AdC0YGMMudiZErF94its0YfbYtCQwu1Mr7rDUsmTXxYz_-vXzxyPlknu2xyG2uol9VEkrl2nu5TgOTX8HZInXHBAx0v6FD1hXeopuBpnuSWPynUZp_3NdW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR9hpYpU7cvwhI9ftJgX1bwoMDTEjEVyLFRQRDvK2XEkCgnDQLzmGwAZZJb6hWrbyPZbbCf5Jg6h8DoaK5e2B8FQaJIW0-zOsolenVmVTzNQU5HyXhxe40xPKzPIIKL2s6_ukkUO5Xnzp5xLO2XLfgBR35rQYa5FRsrN2Rk_AgCvV4iC-ZnqlHysaNVX0TdVI3E1lOsdQPzt3LmTE-KqFjfrx76fVLcP4lwSHiL4LvtWW1fHIZDQfiMz9fRJXvhMZ65igBdrUO7xYI991NV57pTsma1swN65reV-t4SE58S4HCoxWzZfHf0joBir81wzBir1H4GFuGyAZeHv-_XMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alMqy_U2ji1ix3ZQEUglPRplIt1N4_zJi1Ohf7ShU0u7aDxJio1M9K7muVW6iHUiEc92TykTX-0fdZXYhROVbdLdAA_vvCUvJpeN3gh8_9lzBcKJXDYyCuH8vo8hxRwAPed0odJHQRQY4en83uyvGE3swhEBuXBD5Q1C12rxuEmvbpf0cv69VX1srC4QO98KiuK1Vl_NxFaCcsn_dZyUySwsmuIiiYnOomluZlVy1CENOpA9C2V_5463hUXYze4StcofFQrJ8UM5xx671xmIMJ7vBQ34qMoqiMG7Gz9r7Jzlgcd90C0K1Z6Y4EKRtYggObd8D_A3WzsrpwOuGx_qLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسرائیل
⬅️
لبنان
ایران
⬅️
اسرائیل
ایران
➡️
اسرائیل
ایران
⬅️
اسرائیل
فردا از اول بخون همینو
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g28uYuHXMFUKFCWIrFsimDaGDSkdPJWjlqQqyiS07NoD6age8Mjvq5Ne1mM6oTk-I1-Byal2r5fSMZOyVxLtUFyFmGRb6QSnTPudseHMJdkpg9xR_C1B61CqOhmKmrcI3PtMeafjamF79MP1FqZYR5CNhbUDs0gq5CTrgh0NUdHKuQB_J_Sjw5VrQOdh5Zy9BgwxkVxxDTr4J4MmV8ALsKGdHzKmeHWnu_IZEVLuL3GSG2upa_lhZapSEBVKmE4HBtOd03N0CUIyNrFFI1PDTrMp4P55xnepAxZI2xLSkssS2s06oqfFwjn2NCBN6iHslcGi5QaXr9mJBXAzcsaY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqAlm2hWBR8fzLzUrHz5VPO8uiFZKQifQglZ7OAh3wWjnfqO25CVT_NXS2E6JFYqqg2QZ4BNRcMm_SMqDYMMAFa0rVWsJ-Rt5auznrYXOqXPzWPopXR-1H-oCmhgiTZ20rFP4dUTEQHVPSLPYElw8LHGK2n_sSFUAc8yM-vDR4RU0-HwAutNvbOfkJYN21mpF7huYZy80iKZNKaaK1DleWMGiCvz06FmpVQS-MfA_79BcA7hl1bBInkw2iGxxtrszyAfwocYgVDhEXMrBEeTGzrC2pJgz2QVgXfg-tEZhox7hTzZNtfEXlX9I0c9uRTN8Fq2ROKDiCI2K1MpL0-ALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwHYekDdASqmCxD0rrcXtG1MWofst3vzNR8OHYRtWDK22OcZB-FUabqhqubrYlGdLXiP7s7LSU3J26bZ2ZEdVJq0Q41VFegFOTdwr8HhdfSy5Xrtsv3J2ma3_bsnDmnbdHVzSfgYf_W86o_RjWo4_uv4kEcHyJB1oG5IrvXQUrhjmS_IIQ6NFiCQuZoj3skYo4HOBGVpDc2vOY4UIvtME1AuTTIDfS9y9vGCEXhesk61Jpo9upB_2md05Tzn2y8mv0nVRT_UcaszjadagWvKsoqA10rhrbMwiUcyB9Bt_t1pWYriCgfN3McPS9mzEfk8KH_fr03DltMBvxMxJ4usNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7qK46oduF2IF3NZLpPXPUoLCQBQfPKmPl6RkTicA_cRDhjmnK9LhrW9Pzud0mh-5lI5AV1PFoKiAORw30exF6Yy2ILpva2SqmzoBL1mGPh2jr7gxmDpEn8AAiGzG0gUPDD_l1elckDcTzAe3o-Ow8SvYQgeWMLS8VnpawmzVKOtwWV50AHBGZBsd1HQyvxBc4r32QaOWwXG_PMFMrxu9gkYC23slx3um2-eQfgPnuu7mdtS2S24JGuD3L8yeeMgYpM-v7zfytxdHaAzqE8heb9Asnsy50LjuFi36PwKaDyt8B4JpCqSmGRMOuwpzPF-yDMV9bWIzsGBTOrBGCQLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWliALUdXVFTvU5O49oOEdmkOYtYJqACOHLLx24gxe-reUhTX5pSPMFq703mAEGSL38pWr9D0_y8mT5P2Agp7swYUdtIUIzOFlsSNf2VLjnq3kjlduMObA8BxO9-ojZFoC9xdKKcENEO3DURpmWKxrOvg6LI9ZYJoT5KW9Yx9dCjCd7R7UEJ8jQyIu-vVJ1v36dWHh3W6x_1S1ApIRD7vSJgQDTJ-M6E9J4RPpJ6QC5xKWlW1Au06pk37iqAn1ZNa5fy_BPPml649hmTF9KG6R6P9f1zld-Hz3KQHNv6p0HEDBbgH1uc24wOyeV_o8k0MKECggeQJtmuEVqOpe_Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj2Rttr2K6-NYRcW-PyHp70K6FRNo1EwdO4kP8R4Xlrg0qI9RbU6HkClot9naGoMmdcRxlG3G60pOeQFGSKHkb414W2W5VBQI_kcoqqnYz-Uu9wU-e68mwENxwZ11mq1HLzRt6RNmt_ie2kSXer4E3I6IhvtQNFZ4YqvHIW6-mI0T3xpE3w8dFVHvshAJMeTyzSEwkD7AC_C7iyhXI2s8RPZ5H55RCVCX0DqEGGItRZY-215T6kW4T6Q9tpzdbqngBr1WEjDNvAo29xjCJv8Qc-jY8ljnCImsacVV2jKK19oHI4h4rbcM16yw83gP24n2Tj2nsGeLHENYx1Q958iqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gashtam Shab</div>
  <div class="tg-doc-extra">Alireza Roozegar</div>
</div>
<a href="https://t.me/funhiphop/77252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ مناسبتی برا کانفیگ فروشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=VRnmOD7x9lfMlQXzm6pX_ZecSuBfxCafmTd3Asyewa2WsUhnA6ng1QR19TArpCqHgc6HcDu5fo2VqBaNXQauXyI9_2LUqPGbAL-ECVkipkiZWgyveQ8mNxMw0pFBbQBMwvfcLVqvBnM_XdZR3PzVkT0sZ-5Xcl-hm-kCuDtxPLm8-PL7PuGLua28eYDJnEAmRxHUbJOyRKUeDSo7F9X_i6F2kzvBw6UNrNafPSLo_ew2U02EmgUAZTJz4KFCpbHXeDSVK5XkhFYtwS4aWUxVq6_Lv-n_wMuJ6Vov5Qez7jfleL-XpCoHQl7urZpQNanVuZrsT4f1a83ETiAM2Cn5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=VRnmOD7x9lfMlQXzm6pX_ZecSuBfxCafmTd3Asyewa2WsUhnA6ng1QR19TArpCqHgc6HcDu5fo2VqBaNXQauXyI9_2LUqPGbAL-ECVkipkiZWgyveQ8mNxMw0pFBbQBMwvfcLVqvBnM_XdZR3PzVkT0sZ-5Xcl-hm-kCuDtxPLm8-PL7PuGLua28eYDJnEAmRxHUbJOyRKUeDSo7F9X_i6F2kzvBw6UNrNafPSLo_ew2U02EmgUAZTJz4KFCpbHXeDSVK5XkhFYtwS4aWUxVq6_Lv-n_wMuJ6Vov5Qez7jfleL-XpCoHQl7urZpQNanVuZrsT4f1a83ETiAM2Cn5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIjoZkLBUIst8LFfF3oW-Isrg64uSELH71_kCyoi2ZJiZAFoT2NW-ty1df0p4NPv0hOqyMyGvaBtdnXe-_vdbV0t4OIArtRLe9ugixWIEoEJz9p-x9A5xS8_x6UtUd4uxOYWgXteH3pH_Ej8hgmnFH847BqVpcX5ps6Vpx3Xb7YVFU3biIRHJS_mDGjL0gJ6pAk_-YKL7tZdmzcGNTIhtivgeaMPi6CEAgOzqIYAblm39ChaGdDLXv2dG-UlntVF8VqBZwoffw_YgajwuTiGEkrCl1dOcmT7zGL1FJNajh8Ppy5e0r8c8y0wSjrA55qEPJRtIJ4jhGpWr4dJwATotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVOGlPBHEFLt0ismpLxEQPJ-rGGA6QDgqnkJFvwpascNe0eVzfPwuxBu-qjgmmXLqC7YW52sng0WfYKIS8tkBx9Tgc1VP187QbpiXtkZzrWTAUSGnAJNgWfTj5fwWSJw7DPeQxgcTmNhYfcLsMTy4vgM6KmSh4L9ypJB1eH880-3gwX-YwUyt0O1qmzKrFV8gS41efo5oCg7sblbFuVO3TZ8XZETCuc-sA4hs6ZoPptmK2osDmxPOj0PFfccoj8hMgHEZk4rVckns-fE08GRFSi35KpkyBcFa73ltjQcI5YBhB-TTiDtEaa8bcDFnkIv7DAEja3zGHFhDWFf874tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYGtyFii_N9kTtjnpAaJXyag53jRrxG27O7UkHJO_xHLjV9j8y1r8-HaLhbXwmgBLuPdvPIrSUKCOlZ3I4mW3XKBXlALOu71roibBS__yJgq3XZUL3PzdHC7IYFep398aIn93F6E87WCsoyCx9OkKMlpYFmJVAtRiz4e0ehtRlkqH8aZCYXOREqllVugcdayQv-UwqLn-ZjSsirsvI35pqLnNk5RFOG19SoOPiFL2i7X6GVpFSEoqnB9cc9QFSVd6Y6peRpxTRkovlZvbjRovgSY8Hc4LxDmz1gMf8qXfYEaZiUfHjoS99iSmBP3dnbcuVP1AdMj8s1Zf_jy58Gmhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=t5QdY3liPoYjEaSs8HI4e2qtgvBwbb4cdqNzbP7-QtowE2Wcaj9gA1MYFKHstGTnGp9s4cbEtnzHApp4S0qGM3m5TVa-AorJhKn8NUk5YkaTOsqm1IMLoryZPLtgZ92G1f4sj3PGFGekFuXVayXefpSD9EfvgO4dg0hVPdWhxERwsNPjckyIHMdvnKcQkxpADb8XHGc_C7WgMSUgHvq4_En_Lftj6HYj381XxUNhLyasU_KSEAb5Mh5Rx8jqy7nLulaSvQ2OagWZzoVR44ODJZhIHZgkeIGLgco5nB1BBD0JAtTOqFX8V4YO2BHpuc7asjzaHfRpVRwVbGesbWGaog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=t5QdY3liPoYjEaSs8HI4e2qtgvBwbb4cdqNzbP7-QtowE2Wcaj9gA1MYFKHstGTnGp9s4cbEtnzHApp4S0qGM3m5TVa-AorJhKn8NUk5YkaTOsqm1IMLoryZPLtgZ92G1f4sj3PGFGekFuXVayXefpSD9EfvgO4dg0hVPdWhxERwsNPjckyIHMdvnKcQkxpADb8XHGc_C7WgMSUgHvq4_En_Lftj6HYj381XxUNhLyasU_KSEAb5Mh5Rx8jqy7nLulaSvQ2OagWZzoVR44ODJZhIHZgkeIGLgco5nB1BBD0JAtTOqFX8V4YO2BHpuc7asjzaHfRpVRwVbGesbWGaog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=dupF-U7fMrqBbJKT5CMh27yZd_CcYrSM_6b2G0CH8Mk43Nocq8ViQzVrV1tSabFivLFuc1GcVyhm3NXQg6UupzAyFlY57fv9JeXpv292FPK3mp2HvhoE3d4rj5sGFpv3fS08QrP_sS8sUImEzVXSAcn6J_SU0o2nfmTzioRmUMuizcVD2mytiQzF5CfZ1EMLBUOMR-thUndbUCd8lwU3vPAQtrWAykIYqKmmTz5sjPd01X7wrntKy33EkZ2fYpMXtCVuYzF4rhuZiVVkqQWf7GahwklhGx8zaGI2v-h55Ap7tkLNQfFMOfFZzO9qlpzTf4w8-t3mWZNext7oKuMvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=dupF-U7fMrqBbJKT5CMh27yZd_CcYrSM_6b2G0CH8Mk43Nocq8ViQzVrV1tSabFivLFuc1GcVyhm3NXQg6UupzAyFlY57fv9JeXpv292FPK3mp2HvhoE3d4rj5sGFpv3fS08QrP_sS8sUImEzVXSAcn6J_SU0o2nfmTzioRmUMuizcVD2mytiQzF5CfZ1EMLBUOMR-thUndbUCd8lwU3vPAQtrWAykIYqKmmTz5sjPd01X7wrntKy33EkZ2fYpMXtCVuYzF4rhuZiVVkqQWf7GahwklhGx8zaGI2v-h55Ap7tkLNQfFMOfFZzO9qlpzTf4w8-t3mWZNext7oKuMvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZhpQTYo_1nXyb5RpD8OCCGJCysSsmxacL8lICv6bFE-xkB4Us2yr4qGCnwtPWuvc67AM9S6kUE5Yq_PgWFXmOBGGrOwB4uZd3xNCYbxMgWenGzhRa3o-vczNSarCadKWp4qgk6a5iy8IBqNZGe8RIaKr80awLBRxkJpjIuxzxqQ094Qe62bFC62zrr7_c_eEzbynIlZUwAiEMqAT-1-pn2oiaoMIWNw3XzMzTDoq7Cn9wBZ_iyBLq-BZAXphNBe64286mCnSGIWhFgHHSe67Sr7ImwZXzBz1eY-gSAgtkmN97QuWgP5ICfp8SMgr74UjOL66h1Iwq8-PvOvVAg2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
