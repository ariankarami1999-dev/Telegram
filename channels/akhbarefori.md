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
<img src="https://cdn4.telesco.pe/file/i58JyhUHqgRorKnq0hR06cOP1HlmhmLaf1WZgc_51rUt6ljGSwVDzKAWqDWXz3CmN_twpNIg40yDOQ3PfU_oLn1NT19fjS90MX0wixWFjXJBdTwKp3Tcj2nFW-BwMpVyjJM0U6h6ibjY_R_69D8hm8-7PLJbUrtxn-38GppcDuXDw3z80DSYHthuwmnXRsUvUFeo9X2Xsr2SrEyyntcJwbAjStyQ2owav118SMUaWHup9yOTqCcuNje-xscnlAuUHgdThPnTDMHlHdgrR26YW8w2bDo3cg3OyxOXq1tz3BgxBUkyj4fuYFhT7RtCDnzD3F8HXV1al-5_bzT0Yoo58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-665434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU758CJ3Uv81P8PqiyAqinwxzZCkFxvp4ocIqI1dip8E0HRPHccKFboTquy9sSq_qsG8xducZkiWPMU-5C7j0cazFiez7mbiDWuVwPg4nnDY9mVy9B0xUEPoY314QM8KCR45zgQYxjRPAXgnrcWq5eeKWj-OyCwqVmRJ2YHyyfEKBlrrMgniwe-nyOxa_Am7P8PWUv14J4ynDMpOh9Y00Ig7tRL4fsBjtp384RKLsiVck-q9nSR40EtC32SXs4k1nhAcPzIQMAJlnbui7e_bzlHIpTbaNDJzoRLpNI9LPPNyRapYVRCOR2kABOMVVruek4eb2f6-fCUuZ1KpkBk0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEY96akUPEIqlpxkwm2Y7d6_NkX_2izySqlStI1calVlbQBhfR5L6SLKmmFFzg86gOjlzWdgWYoFyAftQxT24xR7guxVtyeebgB8RALGqOldLVHxbzTyScQwvJm6TOhelXYZIVJaDZ2FdrDz68MXea3CvqUhdLrheIQBoVKndAGP7WklkNgULKm_47goj41CoDfCMsDDVaseokH4Vh4NnFPTjgK3Su48tkdWweIpQVdLegYsunAbftub3gjWRA5OeO2Hp1LNi2FodGa9ozCQQOXJCJvPkTc_LhqT1mq-v_3JZrhbUm-r3VlNfu1B-Mumd9r7GI5JkLmoWzIqnjI4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGNx8pg7WoNBP2eQQc0V7A9PSwLEIYV2YVOm4JmD4bPl89xTTpkCuHVWpFd1yYvj-xKt6fCsHOmb71g_b_8JnTR1NOm_S-OYbZ1vb3Zhepxjv9KVlZBKJyXDpIIiLxSsegsgnBzXal8bjOvFpbkjr-A_MH_WmkMZT26zcs-4HvxHScn0ZsLghJ_E90782OiK8Vf69ZArJW1ju19B-dIwD1ES8UYwsmFfUqmEYM5stg4fzGAusETrYHmtNt9Gq0yhg3Iu8e-deRBpRJ7zifLhcUHiRzpSHsaDGp2IPnZu1Jr9geq5Vpi00w09PIaELwKO2TdXJ_IvTuPkncKAp0WL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9ncgq2hEjFNWmleEl0leW3J7y4guWEnn7sJaSpst0NoCy5LO5hTnQTdIatEy8cUv00q79m3qy4hBiX4S6PDynqY9XEwtW6tJojGww-gHA3QPlxJzd6mSuAX-MDrzGEOx87qpb6Mg8M5FGxGiQfOTSHXd-k_X-DbD4HoJz5hO9cchyg_3botqVxhHEEqMpBd3J4lZGjX-bQBR6mnwMz4AmQP0-d-vu0b_mbKQ-kBgSg81AhiNjuhNJTlxydsIfagKDPBEctiAlTCgh9MlbNYBX8N8GVRE-1JxzXnyRq4c3SDpamfUhiHW8TmkWXi1CdtKP7zL0Y5H1GGYKMhB1RU9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ساختمان
شمالی بهتره یا جنوبی؟
سوالی که همیشه موقع انتخاب خونه برامون پیش میاد، اما میدونی تفاوتشون چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/665434" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آکسیوس: آمریکا به ایران پول نقد نمی‌دهد، طرفین در مورد اولین قسط از دارایی‌های مسدود شده ایران به تفاهم رسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/665433" target="_blank">📅 22:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد
🔹
رهبری نظر می‌دهد و نظرش کارشناسی می‌شود دوباره برمی‌گردد یا می‌پذیرد یا نمی‌پذیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/665432" target="_blank">📅 22:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: استیضاح وزرای نیرو، کشاورزی و کار به قوت خود باقی است
مهرداد بائوج لاهوتی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دلایلی مانند جنگ دوازده روزه، حوادث دی‌ماه و جنگ رمضان باعث شد شرایط استیضاح وزرا در مجلس فراهم نشود؛ اما استیضاح وزیر نیرو، وزیر جهادکشاورزی و وزیر تعاون به قوت خود باقی است و پس از بازگشایی مجلس و در نظر گرفتن عملکرد دولت در جنگ رمضان در‌ این‌ باره تصمیم‌گیری خواهد شد.
🔹
دولت از سال گذشته وارد کردن ۶ الی ۷ هزار مگاوات انرژی خورشیدی را آغاز کرده که این اقدام تا حدودی آسیب‌های ناشی از جنگ را جبران کرده است.
🔹
تصور من این است که قطع شدن چند مرحله‌ای برق در سال گذشته، امسال اتفاق نیفتد و در بدبینانه‌ترین حالت همان یک مرحله قطعی را داشته باشیم و با استفاده درست مردم بتوانیم بهتر از سال گذشته از این گرما عبور کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/akhbarefori/665431" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/665430" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بحرانی بنزین در روسیه
🔹
تاثیرات جنگ به پشت فرمون روس‌ها رسید. قرار بود سوخت اهرم فشار روسیه علیه اوکراین و اروپا باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/665429" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665428">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: دشمن در تلاش است به دستاوردهایی برسد که هنگام جنگ نتوانسته به آن دست پیدا کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/665428" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTxiuTYdKDheWUz32KRYqDNyYMjs_413UUg_ZEEAktqcgLlqdr-1Y5XbH6ZeLw8iTPwwP6LBIeWtzHXptTAW_vyDRKEtwVv8giJJJ9A3C39IF9ImLuSAB6egI_mD2UFqKMrbkBNplSqV2yWZE-_9CcunWRhjNqYRPIeTHBLZj4vkQiyXfQMZdy0QU3t0GGJ3iHxHUHMjksmml8Ae4MeM6v5se3NCfYtrfqyleqxYcP05m96TXJOY4JkWpoo_nT0gZy2fmGWSEnoEx3BgzHQmoFQrr0P5J8F_IUzR2H-gvjk4ZAc0Yhsq1k-0rMzmarNQLSodBBwxTHuZqolL9SP1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpu_i6i1eEXt4VMdstmT_osr350PWfDgiGcMyZQCeSYULxzHlO3znNt16OpJZJSLI-AwXLV5pLeQYz9G68AoJ2imgghw3i9Tc75hPH95ofnnQ6gkozbJplnIWKIMyepBOx6hSBgDxoG06cOcazD5J2vP7c1UIEHnjuLn4Qe5Vd_a_wwsVPb0JYunfQFWb-lK1t8KHDpzn88y4G4hXNojf9ElNH6lv0pcBzfnci0XxcY-b7l6ZXZ12CDNsKY4oYKu8dgI5rpOtOmGexsLSQ3ZYL7zXVk5Exig2cOcUKFKKe7bZLAq0I1uOlrMT9EaCFiFtX5xgFn5jbZaAc0YMblPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byVAzQfvcvuN4nqVaMSx8g3m0LMeN4lLuSxqL6p7D4PX59J8dCduesinu_EfbFY_fpyaeNI18UXsd4V6dEl615Iohi_z4SzqJUoy6ysjvRdWUVO-Ew4RObsqn_zFdzMIAF51ppQLl53RiAZayBeAKoss6z9eLw7HkxuG47IjnY2eK08MaDtewUf7pO3t2_diwF-isfcHiwAnTS6PMDU3xF8xH_Qs-Cs0lWdp1XPu-Fg9mCl5S5BRgW5OXEuQcxvRTYx8tSSGj_6tecIh926azkwhLbAAtAdgHcnbQLqbBkNFTGwAgOY4a-PuXpGFbWzwRtE8bxNT7QocWt35mNjlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtbVhYlYPnDKhbgTURAhkPv0kM9qE0fJRb8zzYVgpPf8z7iJXevkVD38YniWmlwXFfbWSyLTWnrrR6SXTdNawCo27g-Kv6Qj00nkVizah-dYGXnoXBWdQJ_RdJW1CHSU2Cbt-AHaQk2AOb3bbqWZKcIkQdqBgRfZovIT9bciY9X-hD6NK2kAUvDwHr9-EmaA1W0vJoRrH2ukI0y2szOC83pmrFvlFmCkB26jepXEti-sA-L6KIs_JTfITuT3ucW0e5YY0wDb9MwOt4a7fVsTA6bhNN9ShHqlosWO_jljJhXjhYJJwBDuov2MknYeHeZMjNdoXxHs8XlS8I4Xir1h9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمای زیبا و دل‌انگیز از بازار رشت
😍
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/665424" target="_blank">📅 21:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پزشکیان: هیچ‌کس نباید این‌گونه سخن بگوید که گویی دولت و نیروهای مسلح دو مجموعه جدا از یکدیگر هستند. این همان روایتی است که دشمنان جمهوری اسلامی ایران دنبال می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665423" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27152751e1.mp4?token=F2zGJbGWPQ__OwZbs56huVOtlnnBqfkuWu8kOb5_JrXagZ1dkjGLGhqoNt9-EmujMrhq16xq6CWh_ghovpYlZDxzUig2Hu3Rq87aqVeErdL0vD-DKle7N0EbLx2NLM51onYDl5S7Y7JAu_C2zDknKMX3xIEE_rn5RG_M1GW1MSSlQS0SeXOgfVeXqwrqGfO_FV9EKOi5CxM2z9obiZc0XEfZdpy9kpmewn7I_t7VPFZ7V79bv0Z9zjnfIXLKhj60Uy7nKiQhQblj_OVSRP751Aryi2X4EybPoXzI05TBHWC9ERNQ7igIF5dr-eOXLdzWeICFU8ghdEN-eQUsk3NC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27152751e1.mp4?token=F2zGJbGWPQ__OwZbs56huVOtlnnBqfkuWu8kOb5_JrXagZ1dkjGLGhqoNt9-EmujMrhq16xq6CWh_ghovpYlZDxzUig2Hu3Rq87aqVeErdL0vD-DKle7N0EbLx2NLM51onYDl5S7Y7JAu_C2zDknKMX3xIEE_rn5RG_M1GW1MSSlQS0SeXOgfVeXqwrqGfO_FV9EKOi5CxM2z9obiZc0XEfZdpy9kpmewn7I_t7VPFZ7V79bv0Z9zjnfIXLKhj60Uy7nKiQhQblj_OVSRP751Aryi2X4EybPoXzI05TBHWC9ERNQ7igIF5dr-eOXLdzWeICFU8ghdEN-eQUsk3NC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ جمله ماندگار رهبر شهید انقلاب درباره نقش و جایگاه زنان
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665422" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd755b8ce9.mp4?token=KMwPDy6QdHYY3QsKEocMSP1JtEkyGnQlP3WQ5Y80KViRNYALrlGngNG9T-wNhqA01FoDSMq_sBPbXyRSyvtzNavW0G63Y66948D-QBiIZmcJQ-ME3R25kHpaFsENmGgQjHORnqqQ3OdPXB6pXFwOQw-JsSmgAom21S_IwXp6cNFhRSR7OInevWZ2zZ9JlTmDptfeO_sp9SSo3aQ0tsImdoaSprInexHrCfrltU5FOfVYlhhO5uM9bJVQMKRXA2wnjQhT6KMK9p_mLQSZXeHRaWX3sRXyF2pd0eT6BLkvyjiiSI33cT2spWEZekoUw_6naTuxSH8_--WbhPUiNyh6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd755b8ce9.mp4?token=KMwPDy6QdHYY3QsKEocMSP1JtEkyGnQlP3WQ5Y80KViRNYALrlGngNG9T-wNhqA01FoDSMq_sBPbXyRSyvtzNavW0G63Y66948D-QBiIZmcJQ-ME3R25kHpaFsENmGgQjHORnqqQ3OdPXB6pXFwOQw-JsSmgAom21S_IwXp6cNFhRSR7OInevWZ2zZ9JlTmDptfeO_sp9SSo3aQ0tsImdoaSprInexHrCfrltU5FOfVYlhhO5uM9bJVQMKRXA2wnjQhT6KMK9p_mLQSZXeHRaWX3sRXyF2pd0eT6BLkvyjiiSI33cT2spWEZekoUw_6naTuxSH8_--WbhPUiNyh6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران در برنامه پرچمدار: قرار است از همۀ مدارس تهران برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید استفاده شود
🔹
علاوه بر مدارس، مساجد، دانشگاه‌ها، ورزشگاه‌ها و سالن‌های ورزشی نیز برای این منظور پیش‌بینی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/665421" target="_blank">📅 21:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: پیام آمریکا در دوحه به ایران این بود که، بزرگ‌تر فکر کنید
🔹
رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665420" target="_blank">📅 21:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voDxHt5VLzFHsWjh0hK-ZHAKEPmQdunGvD7MTOzhixUb-NDpCzRWubwUR5OlbUVhtYO7rKapyIL9XFiAbNdWGehz2gsT6j1XZ_re7alz-HfMd4F8Y2fdGJ4nw5DiTMlK-ls_PukdKds27ct_ImTnDBsVEF8toO7SbF3MkA-G3jTcYNov81OWwAcTai66klV1_95Fb7KMCCAxib-BsOObRFLl2qi61x7W37_Gfb3g7EW3YobxT-ujA3qkCSTN0vQUiiTgW_mQt8B5lYOLLhjxSMao7GlQNW018i-sI7pKIJw79nZvAZXK9mPGE8cpAE5gp-2djn4uUzJ-7RQrCDs_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
براکت جام جهانی تا این لحظه
🇲🇦
مراکش _ کانادا
🇨🇦
📆
شنبه ۱۳ تیر ساعت ۲۰:۳۰
🇧🇷
برزیل _ نروژ
🇳🇴
📆
یکشنبه ۱۴ تیر ساعت ۲۳:۳۰
🇫🇷
فرانسه _ پاراگوئه
🇵🇾
📆
یکشنبه ۱۴ تیر ساعت ۰۰:۳۰
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس _ مکزیک
🇲🇽
📆
دوشنبه ۱۵ تیر ساعت ۰۳:۳۰
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665419" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: پیام آمریکا در دوحه به ایران این بود که، بزرگ‌تر فکر کنید
🔹
رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/665418" target="_blank">📅 21:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61962be8c.mp4?token=GJ2dNWsqwQn5xibVhKhXmrdmqc-QzxGX8Wsoi3ncsyvHNrstJe0nJZFtq3mMLklDg0NGB3UuB3i96AaIPW33PumiLpnzZr7lwcLFHLC89ap5GYToPZC5RFS_W34OOpvCqAb9xLINjRRxrv9c-JBnkn7T0GTeQwHZ8jxTVOHgD8pQoM7_75B4pT62VdPuHiWRIRPmZf40AwT8Wp4cHfmpEss6vCXXLCwGACtIOz7oxrvh7cQdHQkzXVt25k2gtYC5A5FDFMsHN3DyVk3i__rqanMqOL80NWTLBD-VIegghiwEGdu5HMb_IFqpcw-YBQvtELnQ1mfT1S6bXCPU99cCGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61962be8c.mp4?token=GJ2dNWsqwQn5xibVhKhXmrdmqc-QzxGX8Wsoi3ncsyvHNrstJe0nJZFtq3mMLklDg0NGB3UuB3i96AaIPW33PumiLpnzZr7lwcLFHLC89ap5GYToPZC5RFS_W34OOpvCqAb9xLINjRRxrv9c-JBnkn7T0GTeQwHZ8jxTVOHgD8pQoM7_75B4pT62VdPuHiWRIRPmZf40AwT8Wp4cHfmpEss6vCXXLCwGACtIOz7oxrvh7cQdHQkzXVt25k2gtYC5A5FDFMsHN3DyVk3i__rqanMqOL80NWTLBD-VIegghiwEGdu5HMb_IFqpcw-YBQvtELnQ1mfT1S6bXCPU99cCGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به کنگو روی شوت دیدنی هری کین  در دقیقه ۸۵
🤩
2️⃣
🏆
1️⃣
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/665417" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
غریب آبادی: تصمیم گرفته شد کانال ارتباط فوری گروه نظارت نیز تا فردا تشکیل و نقص های یادداشت تفاهم به صورت رسمی و مستند، اطلاع رسانی شده و در مورد آنها بحث و بررسی و تصمیم گیری شود
🔹
در جلسات با مقامات قطری، از جمله بانک مرکزی، برخی مسائل مربوط به هزینه بخشی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665416" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
رئیس‌جمهور با اشاره به برخی اتهامات مبنی بر عدم اطاعت دولت از نظر رهبری تأکید کرد که دولت تابع نظر رهبر انقلاب بوده و اگر ایشان دستور می‌دادند جلسه یا مذاکره‌ای برگزار نشود، نه جلسه‌ای…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/665415" target="_blank">📅 21:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مریین ترافیک: تنگه هرمز هنوز به حالت عادی بازنگشته است
🔹
ادامه جریان عملیاتی در تنگه هرمز هنوز به بازگشت کامل به مسیریابی عادی منجر نشده است.
🔹
نگرانی‌های امنیت دریایی نیز همچنان بالا باقی مانده و سامانه ثبت حوادث اکنون ۴۹ حادثه تأیید شده منطقه‌ای را فهرست کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665414" target="_blank">📅 21:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891dc36791.mp4?token=g-csQiXVdAhGobSwt5QEUOPuIWO4NH5rDjTzMwjdY49-pf-Z7IHyxJWCMYaVhJtXx4pxgIoyGLffJDpbig4rYDy1QCy_HFF_I5sIws3vPHbRvmecZgAC864sbAjcXxPVhfDz0bhKxmHEvOWH20C5T_fTooLq_YRvi4M1IxFLeuKI1DNHPZPChl_-5iEw567TGO3AmSlQcvaKcyjKre3FU3y5AfQYIXkW3DhRJgV0DPObsj64PzDvPbociCOQklrJ4aeCFzY9qeoReiRWyUZ2yHdjy_4LWCCai5B-ZVYwKXn1hZFwTE-MMA5pVuNuvehydCuzZNU_qMTCII5YJKQhQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891dc36791.mp4?token=g-csQiXVdAhGobSwt5QEUOPuIWO4NH5rDjTzMwjdY49-pf-Z7IHyxJWCMYaVhJtXx4pxgIoyGLffJDpbig4rYDy1QCy_HFF_I5sIws3vPHbRvmecZgAC864sbAjcXxPVhfDz0bhKxmHEvOWH20C5T_fTooLq_YRvi4M1IxFLeuKI1DNHPZPChl_-5iEw567TGO3AmSlQcvaKcyjKre3FU3y5AfQYIXkW3DhRJgV0DPObsj64PzDvPbociCOQklrJ4aeCFzY9qeoReiRWyUZ2yHdjy_4LWCCai5B-ZVYwKXn1hZFwTE-MMA5pVuNuvehydCuzZNU_qMTCII5YJKQhQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به کنگو توسط هری کین دقیقه ۷۵
🤩
1️⃣
🏆
1️⃣
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665413" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7aZ-fLiQnQCiFTMs6SP2vnAXPT2Aft7BsGwvXObLvGmfZ7XjfwgGDNxyWgBg-kI86FQ1mKYZIRlSAnYilL17RU011y4pg95xybX_sTLaUeQnWV8lwfDbGeclvbv8eYjgbAaVEhpBKUY5PsI-Rg_io3mMYna1spaGoHmPFWm47M2_GMKqifnl1HrUBioUigSRhCOIvvwmtkJGhMczBY_8bvLipX_yZx8XXl7BIp1XskRX3JHssaiVXN2HBO4cg2dVa-S_k14abZgS9-z8qz20lGVpIxTu0-5kjhAQbsHCdpUxYfP5-aOxfAi-A1XGAp55ms-Draj_i5n0TUOpILwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: مانیفست ۲۰۲۱_۲۰۱۸| (Manifest)
🔹
ژانر: معمایی، علمی‌تخیلی، درام
🔹
امتیاز (IMDb): ۷.۰
🔹
خلاصه: یک هواپیما پس از پروازی چندساعته فرود می‌آید، اما هنگام فرود متوجه می‌شوند برای تمام دنیا پنج سال گذشته است! مسافران نه پیر شده‌اند و نه می‌دانند چه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665412" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ac2561aa.mp4?token=SghnuUIaL6ONf3ywb1S2QD8lZ-iSueRjBBySd30PezofoOzz93LY0Yjts2iDwKldi-W7RqdRoTdgJesvtzDmrG_gcm50YI4lOhl3fglKOtv946mxZUtHfro9EuQRMRryjwBBVtZhH6BpSg7e0Vh_imuHkZB0g5qBQFbFsqWhb2I0mxRx0vkZ1P7okH0c3hlMWe_YB2pgEwoQmlsZE1z2weZNaygqgM_18UUlG7IhCD3qZaPcfrCTOktzgVNhL4vzcYoYXciCz0_ZiZlEvq29mO_FajyT4tcfgeaqubvJrdIgfDFknmiSWH79aBoXTmTAyKK-TMxi3xHMwHW57oWHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ac2561aa.mp4?token=SghnuUIaL6ONf3ywb1S2QD8lZ-iSueRjBBySd30PezofoOzz93LY0Yjts2iDwKldi-W7RqdRoTdgJesvtzDmrG_gcm50YI4lOhl3fglKOtv946mxZUtHfro9EuQRMRryjwBBVtZhH6BpSg7e0Vh_imuHkZB0g5qBQFbFsqWhb2I0mxRx0vkZ1P7okH0c3hlMWe_YB2pgEwoQmlsZE1z2weZNaygqgM_18UUlG7IhCD3qZaPcfrCTOktzgVNhL4vzcYoYXciCz0_ZiZlEvq29mO_FajyT4tcfgeaqubvJrdIgfDFknmiSWH79aBoXTmTAyKK-TMxi3xHMwHW57oWHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج مرجع تقلید شهید و تأثیرگذار تاریخ شیعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/665411" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
رئیس‌جمهور با اشاره به برخی اتهامات مبنی بر عدم اطاعت دولت از نظر رهبری تأکید کرد که دولت تابع نظر رهبر انقلاب بوده و اگر ایشان دستور می‌دادند جلسه یا مذاکره‌ای برگزار نشود، نه جلسه‌ای تشکیل می‌شد و نه مذاکره‌ای صورت می‌گرفت.
🔹
نباید به هیچ وجه زمینه اختلاف و شکاف در کشور ایجاد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665410" target="_blank">📅 21:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ef9e931.mp4?token=aGFgucfK_HoWIY4TrEr2AAWBsgaAnJjGYv89NLzB-92BF-1C3MV0UJpL1SGvQWyKguoAKLxTqJ7svOzvBjqAw2bZ7a7q4Z6xcR9eSrYWHX4fD4kaO4gO0GhQkGA8YFTdh6TvVd2A3ZU6FR8S1HAq9Xcm-BoQy00KAxr1SoOG_qnYGOyiQl84-5pBtNDNIJCO_quCiZrHpwg0qC3WycrFJGEUuL0sxeQ7fOhey_iC6Ax-FQOontHpPkK9VUtR0juJXusHjohN4B0LovnzxYy-t337wRh3z17UKkBxfv239Y4aPMEmC8jn1RI62LNuicUQrLTBJ7ER2I9KciWqIQugng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ef9e931.mp4?token=aGFgucfK_HoWIY4TrEr2AAWBsgaAnJjGYv89NLzB-92BF-1C3MV0UJpL1SGvQWyKguoAKLxTqJ7svOzvBjqAw2bZ7a7q4Z6xcR9eSrYWHX4fD4kaO4gO0GhQkGA8YFTdh6TvVd2A3ZU6FR8S1HAq9Xcm-BoQy00KAxr1SoOG_qnYGOyiQl84-5pBtNDNIJCO_quCiZrHpwg0qC3WycrFJGEUuL0sxeQ7fOhey_iC6Ax-FQOontHpPkK9VUtR0juJXusHjohN4B0LovnzxYy-t337wRh3z17UKkBxfv239Y4aPMEmC8jn1RI62LNuicUQrLTBJ7ER2I9KciWqIQugng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی خاص از تشییع فرزاد جمشیدی
🔹
فرزاد جمشیدی با حضور مجریان تلویزیون و همکارانش در قطعه هنرمندان بهشت زهرا آرام گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665409" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334e0e88d8.mp4?token=ryxqsdCNRjdZYWYxrNsVZ5ZwPc5UbAro-jYteoxZ7Y5H3SbwEQiFwPKU-JPiFS84pmOTwSydrMbV-j8Lv-ZvTHBrcPlHnjithDetqfPbIQlOcOgi14YrbZEZqmRNdlw9hqaGLJYSFQKkEDPRnPUY1l28TEpuwPNFIl3kpQh5HuL1LV1JbGTCr2fifodkTblsLeMFWaiKoGfaaI3SyIUc-pvwwc4-nXlVHw7fWlSbv-dB5TUkqILyY-HIste7TcDQmlpsO-rWZAmXTHXk26dlqf_pFB-HLcKyesJvoMYrLrANhxUiaLpkdxDQt64FKzcy2iYgkL8dP-vlNs0rrOR6WkKpIybnpZcTfMWoVaXAeiG9c7QFkqDQt1Fi89Wm2uQeKTlb5B2paWqR6P1UgqEV7ZuZ6fgi9dCFS5Ke9XQvzDswcH42uV9526-prRYwXK7tXeNUREuu5epHXFCEwv0A8eSd7Nb-jYGrL2xH5Nb5mfknmalT3txg4WZ23fm-5meeGz-VvDH6_0ly5IWduRczN1So7N2lwUMEXO8T_M9IZ_YInF57_m93bKgiDJpg_JS8Y-9pNNyKwgSIKK0RTcGo-VRfYFq7u7mDX38Zc0AVXuoOXrO0a4dGzN1xxQPfYcjbX-a1nnjTIoGemxVSz-iqQxDhJeXzfAH5UBApGam69XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334e0e88d8.mp4?token=ryxqsdCNRjdZYWYxrNsVZ5ZwPc5UbAro-jYteoxZ7Y5H3SbwEQiFwPKU-JPiFS84pmOTwSydrMbV-j8Lv-ZvTHBrcPlHnjithDetqfPbIQlOcOgi14YrbZEZqmRNdlw9hqaGLJYSFQKkEDPRnPUY1l28TEpuwPNFIl3kpQh5HuL1LV1JbGTCr2fifodkTblsLeMFWaiKoGfaaI3SyIUc-pvwwc4-nXlVHw7fWlSbv-dB5TUkqILyY-HIste7TcDQmlpsO-rWZAmXTHXk26dlqf_pFB-HLcKyesJvoMYrLrANhxUiaLpkdxDQt64FKzcy2iYgkL8dP-vlNs0rrOR6WkKpIybnpZcTfMWoVaXAeiG9c7QFkqDQt1Fi89Wm2uQeKTlb5B2paWqR6P1UgqEV7ZuZ6fgi9dCFS5Ke9XQvzDswcH42uV9526-prRYwXK7tXeNUREuu5epHXFCEwv0A8eSd7Nb-jYGrL2xH5Nb5mfknmalT3txg4WZ23fm-5meeGz-VvDH6_0ly5IWduRczN1So7N2lwUMEXO8T_M9IZ_YInF57_m93bKgiDJpg_JS8Y-9pNNyKwgSIKK0RTcGo-VRfYFq7u7mDX38Zc0AVXuoOXrO0a4dGzN1xxQPfYcjbX-a1nnjTIoGemxVSz-iqQxDhJeXzfAH5UBApGam69XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نان به نرخ روز خوردن شبکه تروریستی اینترنشنال
🔹
رسوایی تلویزیون موساد در پی برملاشدن تناقضات این شبکه اسرائیلی علیه تیم ملّی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665408" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تصویب قانون ممنوعیت پخش اذان در فلسطین اشغالی و واکنش حماس
🔹
ادعای اکسیوس: آمریکا قصد مهار اسرائیل را دارد
🔹
ادعای الحدث: ایران بر تابعیت تنگه هرمز از حاکمیت ایران و عمان پافشاری کرد
🔹
گسترش حضور نیروهای چهارگانه ارتش در سراسر مرزهای کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665407" target="_blank">📅 20:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665403">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc3yt_-fqPJYQUs2EP9T4-wRjmd-GR0sgPHyhOAVvXwhylXI2KnFHeHEqoXdQWWhTHp9EP29JAhRpVl6CjoEMaueGZpnqQQuQVr5TnBHnBvm8XdAUhQBS8Vg_oOtlb8bKJRqYtMC-C7izL9XbMioq3VAYcxS7UTDh41tgDFm62VAHpilE192o3JkEDqipENk_JjmsZCxawfAi4zizaWit30J4OhvkDOXR-jbfa5mr4zhpVaoGHLGBtBA4L71u4QsvTtKuGEiE53aSrEaA7rS3HRtwQRYF9MgJWiP9LgwVNp5r5ri8SLbX3yOebBiqRUcxQztAhsXDLxvJbHMbETu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Urw1pF5Z8L98Xick_iZQhRF0HL9dTw_vrAktBHPourt52rs6pBzEzLTqi6EPBCDb9Dqy9n9ZSSIPJ4XPE0BjVdulcM2aOuK0avUyF2Yf3i0UQa0Ajw6pYuT0rMjlDHMwLenfPqzbGDQIhSl-ebcvPT2YQonVIh4A_TX-r9Z3_Yk-pP97-r_QyuyDMEsLaHYIlnGbWIzHKHgTnQogE0gce1I7lIzKap0HoFs9Z2TEo_UFLlB7HxjgkBS9g7jiDkjZ7kCrOO40Gp0fLoyqjOWXELWHtgjt99XYhFp41KHoZes1NENW9WSt6yStj0Iu3D9pyXUMxIIvaPY6Vgtakmww5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQkLwwrPZOSGdXf_oV8sK_ryMcbBXacPsxZNm_gcK9AHHX72muidHlqMO5cXEhHdbSOZpwBnOMkG4jPt8a1AeehXSiwNMT5JGXscCutRFLQNhp5rKdUHl9ywxN0OVE7sQR3EcNYBbCRLprco0tkpDBLXmgkRNRUPU8EvMydmFMUkFJ4cx5y7xiC4AL5LYtUEzHfaE3-2gAlTOU2daK7wEZgXwe7B-Zo8-h7AmmtrQzNlK4TT0McgYPgvGZWVlrS1m8TkFJmaUKxNCI70nPYk9jsDWFRJ_DlEA6dMxK0E433BGwrYaoIPdWT6_CnDGKgyhALwZzzzqi1hqZgMsXcgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqieSoWoZmKXApilKYvs2HcktefZw3L92e2u_Fm6Ck-IaR80NF15zxNTr7pasTjia6LoJyaBk4XPTiygvstn-KyRSKG1QSn_jdnimJShGxuy3oKBZRoq4x45FYxZprL587QNCkvfZNB9giw1GNwopDgoxkVnJXLrKWxnkZadwWq8Zzt1XJJc11DhvCd5rfvIPhtnv22CXwm3mo0aZW_sBznrwS-obl1fQK6ogQFOPKSGaXjbkQ0YNgP7U4poHzXLjfqXXpZXgZ4d7tDR5V7nGwrLwusJBV2yHDX8J4z-z57KJcNeSaKzaLT_Eicqgs51CyPmcaGEYhWvlj0Oob49BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خنثی‌سازی مهمات آمریکایی صهیونی در سنندج
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665403" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پایان گفتگوهای هیات اعزامی ایران به دوحه   غریب‌آبادی:
🔹
گفتگوهای هیات ایرانی صبح امروز با نخست وزیر و وزیر امور خارجه آغاز شد و سپس، هیات های سه کشور ایران، قطر و پاکستان دو نشست برگزار کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/665401" target="_blank">📅 20:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
پایان گفتگوهای هیات اعزامی ایران به دوحه
غریب‌آبادی:
🔹
گفتگوهای هیات ایرانی صبح امروز با نخست وزیر و وزیر امور خارجه آغاز شد و سپس، هیات های سه کشور ایران، قطر و پاکستان دو نشست برگزار کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665400" target="_blank">📅 20:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db47fc744.mp4?token=T-jLk9P0EEQ7NGxIBmQhxRLYaE0CUBML5oSnbTenLkXcXJqok_iYjR6l14oO8utWz0eaxd7KZLZhi8NC0jWGsBt2Jc6RpknH2O_5TpcE5EeSgys5jKC-kTvrKM-VwQu9ApDBH5dubxrqtHLedolDUvMih8v4vDyGCxwt0uPGOT_BNPSdA5azVqNPR4NsN8P4sNqzhwfjtJEurJm-Ty1VsdrNyXkxlY6XVny5zfi6mgg3_LbMUWIeVNWtoXdiUYkWpNVb9I3G-oeKtypcsHtAKvIzrQNIr1ICMswYiiKgE6bwKgupuAIZymXnryZMCHssSON01d0o-snbwjf9sAUH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db47fc744.mp4?token=T-jLk9P0EEQ7NGxIBmQhxRLYaE0CUBML5oSnbTenLkXcXJqok_iYjR6l14oO8utWz0eaxd7KZLZhi8NC0jWGsBt2Jc6RpknH2O_5TpcE5EeSgys5jKC-kTvrKM-VwQu9ApDBH5dubxrqtHLedolDUvMih8v4vDyGCxwt0uPGOT_BNPSdA5azVqNPR4NsN8P4sNqzhwfjtJEurJm-Ty1VsdrNyXkxlY6XVny5zfi6mgg3_LbMUWIeVNWtoXdiUYkWpNVb9I3G-oeKtypcsHtAKvIzrQNIr1ICMswYiiKgE6bwKgupuAIZymXnryZMCHssSON01d0o-snbwjf9sAUH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد بی‌شرمانه و غیراخلاقی تهیه‌کننده مسن و متأهل سینما به بیتا سحرخیز در حضور همسرش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665399" target="_blank">📅 20:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=mlEDXcRU4_Fmvijo3yUT4nsQvrcfFqRMYWxnQb5C3hmHvG6_dhpvTvqiWCy2Hds1IDn43k_UPcNavnFpx9B8QsGxCNzF0fKssa-IQuAeU1-PZmgM-q4ypogITsR-4SWlC8joPEJapAx_a0Vcbw0VYo_UAXCDk2hhaWdLpMB4C8TQIbWgVRsaP_PyUB8AVMhK1gLou-NpsrsPYRtQ3kbgRzfsXzi2Y9zdWjiaJ6CUlZkox_RcOedbyecbCi16bzo8oIu5LbDc3PdbRM_FoiZWVDDfzPyLSLRsqrUOV9Ae7kpdekbctSMUObL_p2-1NdHPPJPOKgF7afn9XdWKbRqiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=mlEDXcRU4_Fmvijo3yUT4nsQvrcfFqRMYWxnQb5C3hmHvG6_dhpvTvqiWCy2Hds1IDn43k_UPcNavnFpx9B8QsGxCNzF0fKssa-IQuAeU1-PZmgM-q4ypogITsR-4SWlC8joPEJapAx_a0Vcbw0VYo_UAXCDk2hhaWdLpMB4C8TQIbWgVRsaP_PyUB8AVMhK1gLou-NpsrsPYRtQ3kbgRzfsXzi2Y9zdWjiaJ6CUlZkox_RcOedbyecbCi16bzo8oIu5LbDc3PdbRM_FoiZWVDDfzPyLSLRsqrUOV9Ae7kpdekbctSMUObL_p2-1NdHPPJPOKgF7afn9XdWKbRqiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های عجیب فیروز کریمی در پخش زنده خطاب به قلعه‌نویی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665398" target="_blank">📅 20:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا به دلیل تنش‌های عمده با ریاض بر سر جنگ علیه ایران، در حال بررسی خروج نیروهای خود از عربستان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665396" target="_blank">📅 20:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdvf5T8v-hiQbpkrmsNCpTTJ--HwOzwerVzG4JH6twZigPiZw6JsObIrjZvH3R2VvUL8ySHmdZ1U4-9dsBvQPHXBIJJquP6en8cSYXS5Yaac_rnT35S7nlqQclAPMVoU7lkHZFcSla21arlAt6eSTRqBX6pZsl1kCVxSuWHiH5pFSfS4KM9pVql2FLz8DMN5ob3Focu4u8YGf17MqjboaoiknLmj42oI35jVHGG-8qtTmRkYm2ofbc2GSiZSTSZ6ZH2eZI6KM8f5qYbQSWEFMmWwJRl14Cl9h8P5L2OlMXyipGTIofunIoAB2Gx0t9S65OCReNHdaWC4mHUWLL6sBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حجاب دیپلمات ایرانی در ژنو؛ روسری با نقشه ایران و حاشیه خط نستعلیق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665395" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دیدار با ملک‌الموت و سفر به برزخ؟ روایت شنیدنی یک تجربه نزدیک به مرگ
🔹
00:05:40 مچاله شدن بدن بر اثر فشار تمام اجزای اتاق
🔹
00:16:10 توقف گردش زمین و تمام امور دنیا در لحظه جان دادن
🔹
00:35:20 جدایی روح با فشار پای ملک‌الموت روی جسم
🔹
00:43:50 درک عمیق از شعور در ذرات نور
🔹
00:52:00 دلهره و نگرانی روح برای سرنوشت دنیایی فرزندان
🔹
01:03:45 زندگی دوباره در مرور زندگی
🔹
01:21:50 حضور ملک‌الموت در منزل چند روز قبل از تجربه
🔹
قسمت بیست‌وششم (آخرین بازدم)، فصل چهارم
🔹
#تجربه‌گر
: زهره ابراهیمی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/665394" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7V_DsPMEvDltvUJLy8Xj3v_okxNH4ZoIZnKzU7CFWKwRz_yiF00xj7ugojOeRSt97VvhikGQQJE_wAcgcKMt1WlU2TVwBB0r6zQkD7IqUwZZ8NzgtYpTuPPS8SVti4g3noJ-I5UY5rkTB9QyRp2IHCVVdn0dY57vAVdS2xDSX5CebVKtFcrjT3uGMx9ghQW3E71cOANQ_1LKDMgQd-58jDOOlriHSTTvPW9e_xuYDGKv5wZELwS_StCo2AVaEhhTj1BRc00KCIhV47ILPyBX6H-nBeJFOEd9u4MBSnzui4epSE8mIv1NDSOoH5j_c_J9W_7REANspKUCkpxID83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهبرد «اول بکش» اسرائیل اکنون ترکیه را هدف گرفته است | آیا منطقه واکنش نشان خواهد داد؟
🔹
دولت آمریکا در هفته‌های اخیر دو توافق کاملا متفاوت و حتی متناقض درباره پایان دادن به درگیری با ایران امضا کرده است؛ توافق‌هایی که از نگاه بسیاری از ناظران، دو رویکرد متفاوت در قبال آینده خاورمیانه را بازتاب می‌دهند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3227170</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/665393" target="_blank">📅 20:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: مذاکرات درباره ایران در مسیری عالی پیش رفته است و ما در حال تلاش برای تضمین ادامه پیشرفتی هستیم که به دست آورده‌ایم
🔹
در نظام ایران افرادی وجود دارند که درک می‌کنند نیاز به تغییر روابط خود با ما دارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/665392" target="_blank">📅 20:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سردار حسن‌زاده: هم‌وطنانی که به‌صورت کاروانی یا با خودروی شخصی در مراسم تشییع رهبر شهید حضور می‌یابند، حتماً خود را به محدوده تعیین‌شده برای استان خود برسانند
🔹
برای هر استان، محل مشخصی در تهران جهت اسکان و استقرار زائران در نظر گرفته شده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/665391" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما نگران مسئله هسته‌ای هستیم، درباره‌اش شروع به گفت‌وگو می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/665390" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فرود اضطراری بالگرد ارتش آمریکا در دریای عرب، یک نظامی آمریکایی مفقود شده است
‌
🔹
بامداد امروز چهارشنبه، یک فروند بالگرد «MH-60S» متعلق به ناو هواپیمابر «جورج اچ. دبلیو بوش» آمریکا در دریای عرب دچار سانحه شد و مجبور به فرود اضطراری گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/665389" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826940ee5b.mp4?token=EuvDqrqX331BlWYteFO2RcN7w11RbFTO-C1gZGCXZ_lcG_INHOs6gSnHQh-XZqvulWKTJdgMYgeA3TmM3-VNt4uVfMAQcCwaSvycVD2zIJQVvjd5U5kAp859zlkAnhyd-8WNXgDhLy3URv2qLDeqC3MRT1tiUeASWcLB7zHgZb6qiHkXA1aI-lQ2guyuk1gR1OFWViVwIXJBUh36i4Et4YKJN3Ul68pX-xmkqwKsLIV6boY93YdSKukUv8mJHUdQtXSDwz3njK8nk-Pj4BjLYhryyZR7ELNc3dKkNgjA2kwsvMtR7NRWr0HkxV3kCi4p1wc4ybK58WO4baEqqUIWg3HB3NUmLde7_3BmgXvfyoHRSSL1NvXoRCgt_T3nFg1b2G9_jA-vkzTM3NAGbTQYXJ5L_Ptz2T32v8Z315BvFPzcOwYBzzY1dbi4y_Qb2UYljzDyYcagEG0IhGGQAPaeOvokltv5rINSEdQJrRGcrNHoaVtE7M--ojHViOlTyUnVI7yR5XCUNKSFGOShHId0TDuIzHy7VFulSiySS50xeJZdHRtw1BZ6fpDbrY8bttJRh5Ygd5eXWs2kxV_vdkQpbmj0-btu6Wmho1j78SYbMu7YM1QxC6AbdI0nn-n9Cw5J_QQDijVMIqdrlz5Oe2t9XnddLzgQ9ubexR0B3Ac1js0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826940ee5b.mp4?token=EuvDqrqX331BlWYteFO2RcN7w11RbFTO-C1gZGCXZ_lcG_INHOs6gSnHQh-XZqvulWKTJdgMYgeA3TmM3-VNt4uVfMAQcCwaSvycVD2zIJQVvjd5U5kAp859zlkAnhyd-8WNXgDhLy3URv2qLDeqC3MRT1tiUeASWcLB7zHgZb6qiHkXA1aI-lQ2guyuk1gR1OFWViVwIXJBUh36i4Et4YKJN3Ul68pX-xmkqwKsLIV6boY93YdSKukUv8mJHUdQtXSDwz3njK8nk-Pj4BjLYhryyZR7ELNc3dKkNgjA2kwsvMtR7NRWr0HkxV3kCi4p1wc4ybK58WO4baEqqUIWg3HB3NUmLde7_3BmgXvfyoHRSSL1NvXoRCgt_T3nFg1b2G9_jA-vkzTM3NAGbTQYXJ5L_Ptz2T32v8Z315BvFPzcOwYBzzY1dbi4y_Qb2UYljzDyYcagEG0IhGGQAPaeOvokltv5rINSEdQJrRGcrNHoaVtE7M--ojHViOlTyUnVI7yR5XCUNKSFGOShHId0TDuIzHy7VFulSiySS50xeJZdHRtw1BZ6fpDbrY8bttJRh5Ygd5eXWs2kxV_vdkQpbmj0-btu6Wmho1j78SYbMu7YM1QxC6AbdI0nn-n9Cw5J_QQDijVMIqdrlz5Oe2t9XnddLzgQ9ubexR0B3Ac1js0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا زمانی که قیمت‌گذاری برق واقعی و مبتنی بر الگوی مصرف نباشد، هم مصرف بی‌رویه ادامه پیدا می‌کند و هم سرمایه‌گذاری در صنعت برق آسیب می‌بیند.
🔹
تعرفه باید طوری باشد که از کم‌مصرف‌ها حمایت کند و پرمصرف‌ها هزینه واقعی‌تری بپردازند.
#مدیریت_هوشمند_مصرف
#پویش_قرار_همدلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/665388" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ba6755b.mp4?token=lyoiwJlwrkVC7mE4rW0T3Rma-qonzoWr3lsPSJhuAAoa5BdyNGeyLUcI3OuBPBgGdEZvStcltXn9zqc8YIIu9QeFvPVpD-sjRVRrLco4Y5mIVsmMSC0t-mtydGOEdtFy7BQFm1dWsravPaGSt_92yV2iPV5eqHq8mC5oi4eWRMGtr-BOjZGKSa40gPZAmmD90HB55DJnfOg8rER3indS6BMyLcbb4Q2UrZQBqB6AV7B5gKRrAvFvSQLY9eKAtj0StZPawOR540ZF20QRaSOfW5o69547V4UWaP2L0Urq_oU5N6-jLEAaWN0SDB4Izz-ln2L-fycaZdzU_XJw54bGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ba6755b.mp4?token=lyoiwJlwrkVC7mE4rW0T3Rma-qonzoWr3lsPSJhuAAoa5BdyNGeyLUcI3OuBPBgGdEZvStcltXn9zqc8YIIu9QeFvPVpD-sjRVRrLco4Y5mIVsmMSC0t-mtydGOEdtFy7BQFm1dWsravPaGSt_92yV2iPV5eqHq8mC5oi4eWRMGtr-BOjZGKSa40gPZAmmD90HB55DJnfOg8rER3indS6BMyLcbb4Q2UrZQBqB6AV7B5gKRrAvFvSQLY9eKAtj0StZPawOR540ZF20QRaSOfW5o69547V4UWaP2L0Urq_oU5N6-jLEAaWN0SDB4Izz-ln2L-fycaZdzU_XJw54bGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده خلاقانه که به راحتی میتونی تو خونه درست کنی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/665386" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نماز بر پیکر مطهر رهبر شهید ۶ صبح یکشنبه اقامه می‌شود
رئیس ستاد آیین وداع، نماز و تشییع پیکر مطهر رهبر شهید:
🔹
اقامۀ نماز بر پیکر مطهر ساعت ۶ صبح روز یکشنبه برگزار می‌شود و از مردم می‌خواهیم برای حضور در این مراسم زودتر در محل حاضر شوند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/665385" target="_blank">📅 20:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqyp7MjbrE9LPA4cKQU3lwQjBH0BhwSzeOBV4M3UrEUTGN5dqcRTjI63C4EOkR5j-w0VO6-VElLThIZjI127lbxO3TaGqQhaObeUGfzS7iIOadOwQ97qTtLGYI9ShS75pHGK_-zsicQhzYeUKDiXbojTyYkkMD8UBFflK8YsQX7ESZd8WbcnCWtrZhWPtNiKtahUcq-rB8wcL_FT6iIN_Gz6T50U6F69_cnPByISRtdweXVPuBg0qc2nQUS_5S0tTRnUGCRQ0pDNJbhY_lochLXPMwmJf3qcqHCgt0nXJacd6MS7mBFMQNJUq0QcLYB3DXhauzzbEMCLzs8pEfGXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه از بیمه‌بازار، لازم نیست این چند تا کار رو انجام بدید!
• نه لازمِه نگران پیش‌پرداخت باشید،
• نه دنبال ضامن بگردید،
• نه چک و سفته آماده کنید،
• نه دغدغه سود داشته باشید.
✅
در
بیمه‌بازار
می‌تونید بیمه‌ ماشین‌تون رو قسطی بخرید
و هزینه‌ش رو در
۱۱ ماه پرداخت کنید
‌؛
👈🏻
تمدید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/665384" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: تیم‌های مذاکره‌کننده فنی ما در حال برگزاری گفتگو با ایرانی‌ها در دوحه هستند
🔹
ما هنوز در مراحل اولیه هستیم، اما مذاکرات به خوبی پیش می‌رود.
🔹
اگر ایرانی‌ها از ورود بازرسان جلوگیری کنند یا به کشتی‌ها شلیک کنند، رئیس‌جمهور گزینه‌هایی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/665383" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مدیر مدرسه</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/665380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
کتاب صوتی مدیر مدرسه با صدای ماندگار بهروز رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665380" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aa14doIilJlcORVSL6lGNAizjTRJ-uzi8sxaiYXhmXsyjr9qbexH_3jXGzwQXTAbr1p8vrW8pyz2juEz7-czxgSGL53-MM3urTsdFasQ2FetGHPZka7OkhmcVs2kFbTKT6YSpTs6DVN1NpC-cUIJKrfMpvSNyO0zdGWHCyXNRv7OLlhjP3E4k976LVdUDwqLAZs0_G9Bmlaf9NolEsAPEUU_FoMU8TDefvMSMwLTie0bgBvmqBegCAWcjk4wQ7HhX7ihTl-yAgzU5m1lxZWfCqH40XpC0keGCbyPCjFW4xmNVCRHHxNDkHPHkmtLYpAEAIuBUNj5lE-xF0DuRtwRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLm1lVI56SJs9MSZIYd1X3_VcYyuCipS2tHCq-RW35cu7mVlTXB_MOQQ2QTuk52iwMn2S6bQ50V8up7pKjPNGdGyqY2bbtXuBe612hYLI9KQCq0pRAtRunOhPm91niLW7cfT9b909xFvKyQYjEzrxfSYNZhpSJjKPRZ9umE0WvVzJBjIkyqnT_VAopfGpJhNnPmcAZANM5Cc1xTUcHBBHgeLUiIipdr5m9qKTuBuELZfpgWmxflF4BEu-vfkm3v0aHOSXOEpyW_X4kaUrezZXU_KBY5XtwlHJljz0Z1uVZXTUlvR9kVreCROJY941GJ1VnFWGfsPD6kZXncXYguNHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر از فساد و تبعیض خسته‌ای، این رمان کوتاه را بخوان
🔹
«مدیر مدرسه» اثر جلال آل‌احمد، فقط داستان یک مدیر نیست؛ روایتی تلخ، گزنده و واقع‌گرایانه از نظام آموزشی، بروکراسی، فساد، تبعیض و مشکلات اجتماعی ایران است و نشان می‌دهد چگونه ساختارهای معیوب می‌تواند انسان‌های آرمان‌گرا را نیز به فرسودگی و سازش بکشاند؛ مسائلی که با گذشت دهه‌ها هنوز هم آشنا به نظر می‌رسند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/665378" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/665377" target="_blank">📅 19:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cveDLIOkAPyvS_AhFc5NBsQIuY03ldWr2TI3Re1p85E0JFZYQ2h-7eUcKM2kq4ppZyHFCUNSCoynvofpYWLzcL8FYzJ-SmznDCGEgLdnEwuLgSn8JHaqQCW4fb5eU7tC4rYXw0hn-NjVDFmt9UfdxKaZ0Szj-41pgejYIZd2uER0K1BhdpojOgzZfDl-Dt5tk3tctIM6VBYLaj7Be1GXAr0TC5Npd_hUMcfh55d6roEg8U40pyvgH_fm1Ys7dOaODfYGQZDZV94lKbhU7VVTkB_v73TUrtZZZsztVc8XHD-qN5c-0XrkWUuZnl-htkqe6lwG5tuWBF-scslh5HisfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران در آستانه میزبانی از بزرگ‌ترین رویداد ادبی تشییع امام شهید
🔹
آیین بزرگداشت بین‌المللی شهید آیت‌الله سید علی خامنه‌ای با حضور شاعر برجسته فلسطینی و چهره برتر ادبیات و هنر مقاومت، استاد تمیم البرغوثی و دیگر چهره‌های شاخص رسانه‌ای جهان عرب؛ به همت پردیس بین‌الملل سازمان هنری رسانه‌ای اوج برگزار خواهد شد.
🕓
جمعه ۱۲ تیرماه ساعت ۱۷ الی ۱۹
📍
تهران، شیان، میدان شهید تجرلو،
مرکز همایش‌های بین‌المللی کشتیرانی جمهوری اسلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/665376" target="_blank">📅 19:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: ایران امروز از هر زمان دیگری در بیست یا سی سال گذشته، از ساخت بمب هسته‌ای دورتر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/665375" target="_blank">📅 19:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوشکی: اگر قرار بر ارتباط با کانادا باشد، باید متهمانی مثل خاوری را تحویل دهند
محمدصادق کوشکی، کارشناس خاورمیانه در
#گفتگو
با خبرفوری:
🔹
پس از بسته شدن سفارت کانادا، تحولات بعدی از جمله نبرد رمضان باعث شد کانادا به ضرورت حفظ ارتباط با جمهوری اسلامی پی ببرد.
🔹
حضور ایرانیان مقیم کانادا، ضرورت ارائه خدمات کنسولی را افزایش داده و متهمان زیادی داریم مثل خاوری که خانه امنی در کانادا دارند و اگر قرار است روابطی برقرار شود، باید بازگشت چنین افرادی را هم مطالبه کرد.
🔹
وزارت خارجه باید کانادا و برخی کشورهای اروپایی را برای اصلاح مواضع خود درباره سپاه پاسداران انقلاب اسلامی، تفهیم و متوجه خود کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/665374" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a09f77d74.mp4?token=XTa0pOID7etFNWzgiL4THsBe5BzclOgnVTRz2_76x7iZY3AY6hAEAtu3cTLXIKGJKhwjyTZn1Du0jYqpknN0eOQMJvQ9cNvDds1ptgdI8WBKTrw3TiWjvPTD7wW0qYFtWK3-HQAQ6G7j0PC9C75yktYITu_2V-l-1Sf6MpAu3-0pO-As9pMqBO5ZXFjao6A61KbeZoJkyyCr4inKqVgmFKSole4JTNeB8-jOmNPeikK-4_oDO5_bo9y6FoL-ucgdCFKchJnyw0ZkvOzN56F0sFxoZYQos71fpuSvGUq4hDAG3XMdqJcu8S3KriRrvlutSRlUPUiJJmyA0PFYaNi1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a09f77d74.mp4?token=XTa0pOID7etFNWzgiL4THsBe5BzclOgnVTRz2_76x7iZY3AY6hAEAtu3cTLXIKGJKhwjyTZn1Du0jYqpknN0eOQMJvQ9cNvDds1ptgdI8WBKTrw3TiWjvPTD7wW0qYFtWK3-HQAQ6G7j0PC9C75yktYITu_2V-l-1Sf6MpAu3-0pO-As9pMqBO5ZXFjao6A61KbeZoJkyyCr4inKqVgmFKSole4JTNeB8-jOmNPeikK-4_oDO5_bo9y6FoL-ucgdCFKchJnyw0ZkvOzN56F0sFxoZYQos71fpuSvGUq4hDAG3XMdqJcu8S3KriRrvlutSRlUPUiJJmyA0PFYaNi1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کنگو به  انگلیس توسط برایان سیپنگا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
0️⃣
🏆
1️⃣
🇨🇩
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/665373" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
غریب‌آبادی: مذاکرات برای توافق نهایی هنوز آغاز نشده است
معاون وزیر امور خارجه ایران:
🔹
جلسات هیات ایرانی در دوحه صرفا به طور مشترک و سه جانبه با هیات های قطری و پاکستانی برای پیگیری اجرای مفاد یادداشت تفاهم اسلام آباد، به ویژه لبنان و آزادسازی دارایی‌های مسدودشده برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/665372" target="_blank">📅 19:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: ایران امروز از هر زمان دیگری در بیست یا سی سال گذشته، از ساخت بمب هسته‌ای دورتر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/665370" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh76wdtvwl-m9ES2w6sMGUxjnCOsxIjb6ZYKNtQKHKxMXdKBAUouGlxH0lQdBegtBCYloVXBHc26tvnDWONlc1AyZoL2yGvN_7jTHyG2u6x_2F_X8X5e_O-LRhir7T2iMiKnlpbIG0VZwydmDMA9efbWGIK35qd0O8oKq38yQ-AqX8nxeaZJp3cCNScjnrYyh_ImkkEYQ6AdQ-XsLr2ocIPa_e2yDnCKfnpL7pXZriDXbssFGFeRY2PGTUfd4qOXRiGxpqPH7rEUcUtUVkD_n6qn6_UycMtAEInw41UeZ4T3CshBM-Hy08jy2Ug2_Pw_Ajb9fNwlSH3WsRlbKsLRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدال بر سر اسرائیل در آمریکا؛ جمهوری‌خواهان یک چیز می‌گویند و دموکرات‌ها چیز دیگر
🔹
نتایج تازه‌ترین نظرسنجی مجله اکونومیست نشان می‌دهد ۵۵ درصد جمهوری‌خواهان معتقدند میزان حمایت واشنگتن از اسرائیل «متناسب» بوده، اما ۳۰ درصد آن را بیش از حد ارزیابی کرده‌اند.
🔹
در مقابل، ۵۵ درصد دموکرات‌ها معتقدند آمریکا بیش از اندازه از اسرائیل حمایت کرده است. تنها ۱۰ درصد حمایت انجام‌ شده را کافی و مناسب دانسته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/665369" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc7ad112a.mp4?token=tng16mcKGpbrlfG7uoh-0AQhbrSTbesIHoJj0xuSYc-SLRi4_GJiW_eUv8KylebNP_JkkqU-f3e9Y50vNQh2lDPEIeCN9CIRzf23Zrc3QjuinCTAcBTjW8nBxvhFxn8R9aJLkRN7eUc-ZleP5fEXB6In_g7DH6EPG2wXvNdzJ8pXFWyuZOFHgTjFHukCtAtHFdiBgyh0W2pizQWPMw3PLskJOrw3NTAptMB7g2qRLqS5funyodDUrZG56ArqdFk0i1Vj2Ztlx2yJxApJ6DWL0feT_Ed0ohpecv25kQjUVmZbBbWwQPLJ7y41CKn3nayU07y2H9IeLn_jed6yEU6mEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc7ad112a.mp4?token=tng16mcKGpbrlfG7uoh-0AQhbrSTbesIHoJj0xuSYc-SLRi4_GJiW_eUv8KylebNP_JkkqU-f3e9Y50vNQh2lDPEIeCN9CIRzf23Zrc3QjuinCTAcBTjW8nBxvhFxn8R9aJLkRN7eUc-ZleP5fEXB6In_g7DH6EPG2wXvNdzJ8pXFWyuZOFHgTjFHukCtAtHFdiBgyh0W2pizQWPMw3PLskJOrw3NTAptMB7g2qRLqS5funyodDUrZG56ArqdFk0i1Vj2Ztlx2yJxApJ6DWL0feT_Ed0ohpecv25kQjUVmZbBbWwQPLJ7y41CKn3nayU07y2H9IeLn_jed6yEU6mEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قلعه‌نویی: بعد از بازی با مصر خواستم بگویم فوتبال با ما سر ناسازگاری دارد اما اشتباهی گفتم خدا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/665368" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKMwl4zdKW8FxiCkMGA_8Rdqact1FX7a4EjRavVfNjuDgj_IPP-44wuC69X7tV2j-aQUuz-VW_LqQ4X3YFht_Y4rLXaKgLNM6szdvRyELXtwfjJjxPQX_S-DYfhb70EconbBTyy9HfhGdVh7TMPfKMnxv9WAgzqVEOgEZefWaD_2ZaVRuZF4If4jb09CTobGX8rhvrz0dESa8g3agJNBPeSaH89gUKWTV9S7Yh9UeRvlPabBg3I8RPMD5xgdBw4tAP5TBiZ-I-IlPL-l2nsyg94uSmCIsVHHYPWPlA4rvYYymzPQo-ScR9Q-xK0rujbuopg8xED8f3KFascW8gbQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش پیج معروف ترول فوتبال به بازی آمریکا و بوسنی در رقابت‌های جام‌جهانی
🔹
امروز همه با بوسنی هستند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/665367" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPjCdcE2v-fiu_EKiV-sRQhi_0YK__5SXOqFfsQ5kEYXxCJH9hllgfFU8gG2OIQ9lLb4usSVm1w3Iy686tP9GlDHV-edH-FsC6I7cOo0MHjf87hE-s16w5RrQiSeASnuzHAqiXO8mT01ug-oPCSpCzMaxAcfgCJtZ1vaMlDz6yJ0PljGFDCSx8UIE9GZ8C6lXQn0l_RR8SG5hCIVS1NnY74d6PYRLTESGm2Mx7hI1TkgC_OtHjJJ-1obv4rpJe3V-PBHC4cdZMClhzCuBQL-OMG2X05EX0Y9ZnBQKBQOXXqbEZBpjL2VluyrxotdXNfxsMMg5FJpnfQh58A_4vaG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKAXyf2jTY4c2PB-ZGTQ4kRiAp25jkBRmqFthAJZvW4eH4eRuU_k2fk9DojoZmu9ExDek4L01vNfUI281_bimG6iv9syf5yQH-WQoon9Cr8ITl-7wVlK95iq9F62ttmldkE4gXLNP1rq3rDan18Vt2qeCHRQVJIFTPLtoqBjsxwfpaYMcV1y5UH-VAQfSJppnXG9nEeQWvWPItLmImHmi3y_TLnGC1bvhFKDF22Fd_d3_1E5mV4E7DstP4ZV7pOUuvIYGoa3UG5S2iLvxY48VIMLfUFgne9uMvO99T8EweFSjArPiQkfo8ceiBQB7wBtW-W-jFamET78mGTIaDHLMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت بابک خرمدین؛ مقاومت، خیانت و مرگ
🔹
بابک خرمدین (حدود ۷۹۸–۸۳۸ میلادی) رهبر جنبش خرمدینان در آذربایجان بود که بیش از ۲۰ سال علیه خلافت عباسی جنگید. او از دژ «بذ» مقاومت را هدایت کرد و سرانجام پس از خیانت دستگیر و در سال ۸۳۸ میلادی اعدام شد. منابع تاریخی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/665365" target="_blank">📅 19:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
غریب‌آبادی: دیداری میان ایران و آمریکا در دوحه انجام نشد
🔹
جلسات هیئت ایرانی در دوحه فقط به‌صورت سه‌جانبه با قطر و پاکستان برای پیگیری مفاد تفاهم‌نامه اسلام‌آباد، از جمله لبنان و آزادسازی دارایی‌های مسدودشده برگزار شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665364" target="_blank">📅 19:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نامه اعتراضی ایران به شورای امنیت در پی تهدید رهبر معظم انقلاب از سوی رژیم صهیونیستی
🔹
ایران در نامه‌ای به شورای امنیت، تهدید وزیر جنگ رژیم صهیونیستی علیه آیت‌الله سید مجتبی خامنه‌ای را تروریسم دولتی و نقض منشور ملل متحد خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/665363" target="_blank">📅 19:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0IjB46X4BEk7RYt-eEAxvOjgAPL6b-JSiYkm2D2-J9M82BG26-Nq1b8m5RtlHVUEfD1k9A6Q8qfPLf9nFdKngiWa5YuW0z5h_X_sqeogz2F8nlcYMpReGte5vj3P_ExdAu-8aniz863xzhjz8sEXvZZcew0qxrgrzdT9CsN0hocfHNUYrSNExG2ncQ34LKE18N8Ew628iz3OVdl4-xX12W3sx-yYte4T2OGydou1QVJeHa3n_1sbdZL7Jw63E-49_0nYin0VN2bXQwT5mVod7H4rQxta1D8e3EX-40wrR1mMWGpHJgYhIlCO7insuEPdKxlBOmHvBKT_dZW4bEOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/665362" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665361">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frJdUhLGqSS20d8eBEmx80B6eJ90lfMxcUl76eE6YKFfjuQSF9_C-b-1T53kv_bbl3OF1VZPtOYaAR8aoHQLrUu2JIcDZjT_RzPUs3BlMJbPejVqxdQj5HHynHKSkHYWbk3GDy9K7LGmC1UMx4gnTQnOw-LDvXQLAv7ODjWSksKy1DSMTLDnsetfhM-gUPZT9UKb06STUeTryHzlR8a0O1_mFwfDX58zcylBVG6ufPWo4SvLQ60KjsIsm16-jyOdEkFwSkHrpQT4HT56extVIjzvj3DbMpKoJ0cvYeFOyjao9ui1jnhATKyz645s2-Rv5IE4XwrrLre-NszZMEQKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مدیرعامل بانک صادرات ایران در آیین تودیع و معارفه عنوان کرد:
✅
اعتماد مشتریان، سرمایه انسانی و ارزش‌آفرینی؛ سه محور توسعه پایدار بانک صادرات ایران
🔹
مدیرعامل بانک صادرات ایران با تأکید بر اینکه اعتماد مشتریان، سرمایه انسانی و ارزش‌آفرینی برای سهامداران سه رکن اصلی موفقیت این بانک هستند، گفت: تحقق همزمان این سه شاخص، مسیر توسعه پایدار بانک را هموار می‌کند.
⬇️
افشین خانی، مدیرعامل بانک صادرات ایران:
◀️
این بانک صرفاً با صورت‌های مالی و ترازنامه شناخته نمی‌شود، بلکه سرمایه اصلی آن اعتماد مشتریان، انگیزه و توان سرمایه انسانی و ارزش‌آفرینی برای سهامداران است.
◀️
تجربه این روزها بار دیگر نشان داد هیچ عاملی جایگزین سرمایه انسانی متعهد، متخصص و باانگیزه نخواهد شد و تلاش شبانه‌روزی مدیران و کارکنان شبکه بانکی برای حفظ و بازگرداندن خدمات، اهمیت این سرمایه ارزشمند را بیش از گذشته نمایان کرد.
◀️
بهره‌گیری هوشمندانه از فناوری در کنار اتکا به نیروی انسانی متخصص، لازمه استمرار خدمت‌رسانی و عبور موفق از شرایط پیچیده است.
◀️
این بانک با برخورداری از نیروهای فرهیخته و توانمند، حافظه اقتصادی کشور محسوب می‌شود و در مقاطع مختلف از جمله دوران جنگ، تحریم، بازسازی و نوسازی، همواره نقش مؤثری در حمایت از اقتصاد ملی ایفا کرده است.
◀️
با تأکید بر ضرورت تحقق همزمان سه شاخص اعتماد مشتریان، انگیزه کارکنان و ارزش‌آفرینی برای سهامداران، زمانی می‌توانیم بانک را موفق بدانیم که هر سه شاخص به‌صورت متوازن رشد کنند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665361" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766a8912c3.mp4?token=djYp30nE-ZQNnRNuevgbaErAZIB3cSW6fD2gBfIiYeHgPIs2LVN6jo5BOhMRYgcYinogiGekLESBZwsY-NRtIBFUklXO6ALwzc4qTgCRh1sfmfDYaaoyTf3pefdGhir-Fyl6oWO8Zsr70kke--I2Q6IHnhu3zoGXTbwXDwgdF-9xWFE7dgWPzCNZKKRkt7hSsmRyhbe23OfcRpUXc_G-6J9LZeqY_8Me-N40LL6LL1KnJCOsXuIDvNIt1tyv02Yqaj7OWQAl7C27yJQFXJVDivsGQ-k7q2dVeMul3MNnC-ulatD4ZH3RZV65RT5oueuE3uNiICVe2WIm4wshPe4oYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766a8912c3.mp4?token=djYp30nE-ZQNnRNuevgbaErAZIB3cSW6fD2gBfIiYeHgPIs2LVN6jo5BOhMRYgcYinogiGekLESBZwsY-NRtIBFUklXO6ALwzc4qTgCRh1sfmfDYaaoyTf3pefdGhir-Fyl6oWO8Zsr70kke--I2Q6IHnhu3zoGXTbwXDwgdF-9xWFE7dgWPzCNZKKRkt7hSsmRyhbe23OfcRpUXc_G-6J9LZeqY_8Me-N40LL6LL1KnJCOsXuIDvNIt1tyv02Yqaj7OWQAl7C27yJQFXJVDivsGQ-k7q2dVeMul3MNnC-ulatD4ZH3RZV65RT5oueuE3uNiICVe2WIm4wshPe4oYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش سنگین تگرگ، بخش‌هایی از استان عسیر عربستان را سفیدپوش کرد
❄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665360" target="_blank">📅 18:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
با حکم رهبر معظم انقلاب حضرت سیدمجتبی خامنه‌ای، حجت‌الاسلام‌والمسلمین محسنی اژه‌ای برای یک دوره پنج ساله دیگر، به سمت رئیس قوه قضائیه منصوب شدند/ هم‌میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/665359" target="_blank">📅 18:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5bde9fb2.mp4?token=Vg754Y0zbMcaAAmDSY-uWPh1VgaEwIET1ncupQaGjl4SoKbuvCST1_SkWgdzMro7Pr6Vxj7foWuTGI4bGS4KAta6SHIT8MMLjdp85AZ2RJm5OlAgY9Nu6UyRBwxIPMvllTijrktFJ2W6nyPjnsZ1CygI1yf1fMn-_NqT5HZaiUwTDfkGWp4UAgXUfoMT4nzDdsO-0DvW9zixGGTuIdeli9JKVwozIPVSkyOJU9Ct_NRNNdJJCL2sA5vuoieXJJ5ap7Tcf8mUltNSBJjA0GmEs5UZJStH3QpPYrsxGJsULXQvXrpX7Dp-q_3hc0rQeiNKmyekLdZSTsB-3JyyQWtmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5bde9fb2.mp4?token=Vg754Y0zbMcaAAmDSY-uWPh1VgaEwIET1ncupQaGjl4SoKbuvCST1_SkWgdzMro7Pr6Vxj7foWuTGI4bGS4KAta6SHIT8MMLjdp85AZ2RJm5OlAgY9Nu6UyRBwxIPMvllTijrktFJ2W6nyPjnsZ1CygI1yf1fMn-_NqT5HZaiUwTDfkGWp4UAgXUfoMT4nzDdsO-0DvW9zixGGTuIdeli9JKVwozIPVSkyOJU9Ct_NRNNdJJCL2sA5vuoieXJJ5ap7Tcf8mUltNSBJjA0GmEs5UZJStH3QpPYrsxGJsULXQvXrpX7Dp-q_3hc0rQeiNKmyekLdZSTsB-3JyyQWtmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از دانش‌آموز آدامس فروش
🔹
بعضی وقتا به‌جای اینکه خونه بشینم و اکسپلور بچرخم، میام یه‌کم آدامس می‌فروشم؛ حداقل از هیچی بهتره.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665357" target="_blank">📅 18:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1s17Veh9rddTQaaJmdElZtUlTNfXBK8GmMKqutyMCcJqd3JOPnHAgbTXifAdeJHmrMhMkaVCIEtn6ZzctmPNyUFcYTnqN3D-Qq5Zmq-zjYQbOXUQE6GrR-_BdsU2svnNWzOic85zpjV0mZYzGnuXIgqqcWKKWTdlUA7VrgQkjp8lgHosfHB9TuRQZM1cpTrymLXxpjkZjVARxNckaKcKoMRMTgeeAwZNrTl30839zqHpcMbx3CdGdg4w0Y4HZEw9j_Ok2-hbEGHeOtZ3vf2-JrtRCMtAdJd3V-ITl-Q_IZ_b6hopq1zbAhkYxdAhIkBwjfIbiZitUfVjvGL8hR_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان خطاب به تیم ملی فوتبال: خداقوت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665356" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665350">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFyxS7FkQH7z06lpGAAsF4Pgu8d5BM113ocsRQF_w3oPImn1_wTwnvS7ZTOYPlIgRyrHQ6XS4J4eAoftnm9eCipAgUn4krq9eAbgzZ1XttDNt_1ns-jlANkk_F_ljYweFCw68dJYid226SDwDJWKWArAqeGNhYV17-p4KQ8Srulh7-VYSPxeWsWXAppN5XY3s8ZZDKp6tWGUl1QmIFkojJ7rROzvK7piXen7wDNUsW5DohD9TI62HkAa-CTaC3BlsIhQIPsg87XMrAcQiDIXxU-YiIl-Xk2dQrsMecrp0SgmPfMamFNEFHBrZ1mel1J-SJdUv2RoH43bzxtAtB-nuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkExwzaJHs3d6Ibu0bDpYAtksHBiJEnNCGVkN0kJbq1pBsVishvbGjZuXUSZ83uSmixPRT-vadvM2Gavdvf362WmRvGWt6IdsBLXhhQth2f3qeoEddFXBhsSNffJh6bODg_GsaTy3XVwNYcOYdLwSsPkpIZrpdoNCqk7F2vsQTr_x1x_FzuQg8n7Vmx9jEFFbDSlUYWQNk-ramI7Us8hDZUtR_U_Eu7TZLOCOICe5cLfET6kYp1rD9ugkKEG_mOGTiO3484Tx-xRiKB5lmvqi8YDh6-07fis0ibfqHaPTw2wyzaD9CbgYBgycSj4wPfvdoNXC_vyssh_FJte2sEg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKT7nUOzZFyLb25XCOwlO2gP9hQ9D5AKNgO7fmutPC3ETblRvG6P1_rI6uionu5CclcRNjj2EaIBEzq1VjJqLjpzsCuK0ndrRieVui9F8oCvCnPKf1enTsl2oDpjMhiMDU9MELvyiUYhW-S55A8PI85HuPWRjUVzYveMyVkRkp57KLnapKMAeNOSIHp-BgFs0Lur6x4Xn8OLO5tqchS_hSZYD7qUBwECQFJQIMsaLTX2RZKFv2muBCWrUMFcr7WnyqhE1YuaIujN4XaELFQhTK5sCmJbNTGYmTjxxN02D8kF8dC5eJHzPRRz62Ckakh6qSLDjN9xJl2mWEv4E_yzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mojoNeYcosuHiglTxOLxeUe1hYiPUsjND5YKeDr5Pwtj0WUOMNKjjAqbJ4IPcSWklqHuYDxmo6EPCmGNraH9YCX_-gg-pXbd8RPoFwKkrcIi8V1X52CtA0c5Z-BElDoje2kISsOCIT1J5HyfP9FCtRL0MI37inabnIE_dUzA_CTsr3KcBBK4Vk1gWaQEAmxqtfj-rYCA7sHB_TeqkxBv4kVtu4xoAOXX7xe3oqSeyWW7m0phZbTJXjWU0K03KV20WdkaLFpTkBMagJZMb3b8VKa7c01MS9zlyYCU4fGF1mO73o4q_vlJvWILZCBFSGhJoej6gPRzNiHOxhMHbHKcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJyXHecMrh2vNeJjU0y2PlH44Kxac2AQF8VzxNXvgYw5dqQx7OH8THN3OCDwAVk3CL63jJlO7-rAuPY094OOzzexhVxm9w0L5EYUJyXnCLhdKK_gQO55_0aNFjgl5Iotc8Bme88fcniD3Ohr5n_6Ds7SdHP7Ij0DFPMv-5J-e5K8-52QXENyDohjR9DwqZ-256-VUf0SRowzKEy96UvPwtWICR7zN77hmLNuCaHR2L2vTHBdnMZSjB_ru9jTjvKSJxnAvkCbVAVztHNXKMEmdhgmmZ00itBdYiVPRca1d2DsnaRgAQWEUnqlCTnpNyav6G04NeWOgBob36A1t8O6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmaBA_24U4_bcaWxFNUGjgQgNAmMxqrC_38ADo7iS0fxskzAsWQrHgcssBRbZ11xUi86wQYsKfiIbBy-MemtDRSIVD6Ig2FAj0TjFO87_-ysSu2fOgaXtmx0vsgcNcReRVBt6_Fw91S5zXaUXmL4UF8koSeW2igvFxjETc1cu1VsIdi-pkrGKarJ_lbYNtB77b05N2sdi6UrH4tMZB3I7jvIFZ9aPzr7uWob3kS_KqPBc8OAAUOV40RV2UPiv9zrcVYp-gT-DJ0SSz5msQ9flmX1_PXWk6RNvA3I3NleDybo-p7bTYmsfOenJFdLNmi3VcYfM5Ap2U3fSXkJyG3URg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بهترین حوزه برنامه‌نویسی در ایران ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/665350" target="_blank">📅 18:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665349">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be4a6bb48.mp4?token=WmNJZLMhDy-k4W5oqftINFnNqHT-TRa8dk3B6H4Qbg-1hV6ikTKoGEhGHJYMsXl5RCo4n88sHqNv_gqPUJDQ8dD_Xdbixw-wfpSxfe2AzMOoIfkxeKgluiva_w_-FcsPEjNBuDqu_xNLhb3EMX9O0qRNg74FHNrVlsRAcQ71czOE-F8QudhqwTuTOI3B9hUXgyGJSZiXinn_i-07vmTysUjqGgiOiReYAx3P5T4kBjxzceyBhvK2l90ooLKPBV9ELJkyXQEIxbR2o_dDGtYh4Ld2F4pWWJn0KTmztDHeXqR8i7lkf423bhY8RblqScXSIJLH12F1jCKMMgQijXRkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be4a6bb48.mp4?token=WmNJZLMhDy-k4W5oqftINFnNqHT-TRa8dk3B6H4Qbg-1hV6ikTKoGEhGHJYMsXl5RCo4n88sHqNv_gqPUJDQ8dD_Xdbixw-wfpSxfe2AzMOoIfkxeKgluiva_w_-FcsPEjNBuDqu_xNLhb3EMX9O0qRNg74FHNrVlsRAcQ71czOE-F8QudhqwTuTOI3B9hUXgyGJSZiXinn_i-07vmTysUjqGgiOiReYAx3P5T4kBjxzceyBhvK2l90ooLKPBV9ELJkyXQEIxbR2o_dDGtYh4Ld2F4pWWJn0KTmztDHeXqR8i7lkf423bhY8RblqScXSIJLH12F1jCKMMgQijXRkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قلعه‌نویی: بازی‌های با کیفیتی در جام‌جهانی انجام دادیم و از بازیکنان تشکر می‌کنم که بخاطر مردم ایران و شهدا جنگیدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/665349" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665348">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKf9VSNU_ChIR7XmOM7tvuwRrc5fk0aPxsfkDBbI31HoVY-LUg_LH2KNoHbruQhuzjaLkGKNcUTRqBOTht7BAjr2vzhK_wGXi5mfcAN1vEjtstEc3XkhLsKUCo2IlzKpZ4E7xZYs-gU1czrCNszrmbHIaLQMkksXewuRD0_3YfF2nZoGURManM2ic_rMPxAbVLTuM9bba26XxxfHY199h_Vb1_WdKpfH7YQYLdSkkVTwir8pz-qfLnc0viGMyy6Thy3k_MZL6dbaUifJ5iFgQODX6fQBg5GJchCngHVVwfK6lA1phAwe1eBFmAOK6ojdcI6ENgU3cD-rbvmOwazZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/665348" target="_blank">📅 18:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665347">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
امیر قلعه‌نویی: بازی‌های با کیفیتی در جام‌جهانی انجام دادیم و از بازیکنان تشکر می‌کنم که بخاطر مردم ایران و شهدا جنگیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665347" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665346">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICnqihiJQEc-qUqhlWrmM8y44RbXrPs9zvcgtLiNlx1M1ISXdECrmrmNX1ZPcCVfeQdSD4QYwKSUvgt0-jw2XmtxqgAdsh1UCYEMGjyrAuiz8A4mIdU0mGAUVK_yVHlykcDwKoPFiCSqvwGRMDaxEpuGliX0b4CZagkDaifOJD9n7cYl04euZFOHienWCzq_RspNs1jEPYDDp590O9ipvPmDbiyxyLb1C-95rhQ9LrR5LeoCrfz9uv3OgFIwnu0j6wUzUoZQEWmm2rcYCO6CSTciaYMBP3S6EGaAhzlRf6sCxEDGhkULR6mNKYStssUEe61dg2x6Uah0L_gZCDaOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدامات لازم برای نجات اقتصاد ایران از نگاه رهبر شهید انقلاب
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665346" target="_blank">📅 18:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665345">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5877f3cb1.mp4?token=TKzTLVXbLLAPg2H_AL2gC8AGz0mtp75C7L-xodygkL7NL6dkFWeuM7z43JbBl42F7x3k8zXfwYGnGsVCrz6DGUoB9OWA58UnCidLvSRESGqV5XUx-CuJUPPaYwjUGV1IFVDH9ms7M6A0XWXJwLGdRui1DdPw_dw_NJzL-NqYZe4lMlobXJtBHhLWsOTPTSxOlA3Pgo41hw9lubs68ZSP_ff1rnBt7Kbr7lQ-PF5gwK1N251by8n1jupqia9ShhRtQ-vSnCPg-JTo4BX92-upw19j2yd9aMchGscL8kyomGR03liEP5DylH0PJL5QGKuUcfkCMtasQcWorKZroXuusA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5877f3cb1.mp4?token=TKzTLVXbLLAPg2H_AL2gC8AGz0mtp75C7L-xodygkL7NL6dkFWeuM7z43JbBl42F7x3k8zXfwYGnGsVCrz6DGUoB9OWA58UnCidLvSRESGqV5XUx-CuJUPPaYwjUGV1IFVDH9ms7M6A0XWXJwLGdRui1DdPw_dw_NJzL-NqYZe4lMlobXJtBHhLWsOTPTSxOlA3Pgo41hw9lubs68ZSP_ff1rnBt7Kbr7lQ-PF5gwK1N251by8n1jupqia9ShhRtQ-vSnCPg-JTo4BX92-upw19j2yd9aMchGscL8kyomGR03liEP5DylH0PJL5QGKuUcfkCMtasQcWorKZroXuusA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ملی پوشان فوتبال ایران به فرودگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665345" target="_blank">📅 18:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665344">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLihdu66tfhGTTOTYqScC2LYzvTrXfAKcwDyHmD-EEEEXpX8uOFkvrDnTxpAOIwgDi1zawkOcMawV1Kfn2_qYc_zsxBrn2l6jL3gLU7NLNsJwd5LaDSDHX1tpO-p4UkxW618tDg4c1yBN4lMtuOqeDIs7E8fy6bbc8udwU3oCE0HD_ZbLer-8FUfLuHKe9Q6xqkxc_eWwLpCiZQgixGMM9rDk-CLmChlkoqs3kirBukNsEPfmvfRMHb-mvENvnzMiuOuCs41oJ8EyuPzR7ROyQfW1Ox9hYC8diwUGpJDqREMgAzM-pxD9uG64I-pJ20r4Vt2karLHMxCBRGM28C_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر مرتضی شیخ؛ طبیبی که «پزشک فقرا» بود
🔹
او از پیشگامان پزشکی نوین خراسان و از محبوب‌ترین پزشکان مشهد بود. سال‌ها بیماران نیازمند را رایگان درمان کرد، هیچ کس را به دلیل نداشتن پول از مطبش بازنگرداند و طبابت را رسالتی انسانی می‌دانست. محل زندگی او همچنان…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665344" target="_blank">📅 18:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkf7sxfWwKBClkE9enjQ9Lpc-G0hw-U5uY7fNrv4CKtsmz5as3IsRk0JUNWjZ2Fr3f-9bt4Jg4-Z5y4fKwmljO6mFAYU2UWBk2N0LScbANjoCpJPMXCGf8BpJaQRGyBHX_aMeuz2dGQYHBiq_ucWudn6oQe7jX_e5RhhxcZ-rXtxGEPaX4dod8tyRcmGGD_VakmXqAm1I4dn5oo8Jj5rTsCPiBdZcr5i1_sobAEH4Ej5QisZyfvYO0V6UrDfZLoUzZznBorVvU9gJmNAgZy6TeXNGvW7XRTT--G5Fb7XH5jZ-YmiDm2byT1vsITd-D2rEf2PO8W5Rj1tar2MbKYyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn2p-06um9u9PF6Kqwt5xhQQ3Q5cQdEOMg_lz2IKmlREyzc7QnBYLcrn2b1zQMu8mi_Tst4keD0eTcigHdg0W-QHcr-VeQoWuvgF8y0p8aQBJUnbEREOxZrVVGI0l-b7UwC0VlyFjarfmbJxlHAgXLR2G8EhIkmQuF40WJap1lgw9CFkXx_lqC2yHIy7Hpge8FmeyKkCIqSV1k4R5l80QPNRgPdCDMO25rPyDV2XF4yT1ovlIGxqpQZ3YHuGr33Jy5ZmC_xLThlSAlIX6hkKeigUOtesKc1s5I_SFNfLxq2vn32cEhTFTyJcjNHaxuIWVhzAPKcXztIrIEE2Gs7Hsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2I9PUJnhE4fiK5moOcwM1x1j1poxjh4iMbovT_vGBfoLPcT72Y_wIHOLN2EV7cvM6O5RdM13N9OYIkc6HE2e9iHXoBu8GnrIqbNlWB2ZmQMedxakkBXM7NaT5F8ho6-8EkW_VydxraoTyExgSs90oBGmjxLmc5W8pEMYDfVnIGC3DZ4v2iAurAbgw4_HFM1Dr_jkpgzBU5K8esWDE9u-lzw__qEuFfOcpKuM7eEV-X11o3iH8NSVWr1mVjYOnRGr77KwucWKpY4RGX39TMzB6TPYG3F_U_v0Z7RFAFHpi-s33c5ng4KuC2po9Fn-j5rgAm4op674jFo7U0-IW3RYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کارگر جدید بی‌ام‌و؛ ربات انسان‌نمایی که با ظاهرش همه را شوکه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665341" target="_blank">📅 17:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تلگراف: کشورهای عربی، مستقل از آمریکا با ایران گفتگو می‌کنند
تلگراف:
🔹
این گفت‌وگوها ابتدا میان ایران و عمان آغاز شد و سپس به مذاکرات عمان و قطر، ایران و عربستان و قطر و عربستان گسترش یافت.
🔹
محور اصلی مذاکرات، مدیریت تردد در تنگه هرمز، کاهش تنش‌های امنیتی و ایجاد چارچوبی برای همزیستی منطقه‌ای پس از جنگ است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665340" target="_blank">📅 17:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f54d31d7.mp4?token=V4axIt-zoLExMdFBIR4qGUSVGcTV0E08Y-47oV7VncHFWfJDYZmw7b5T-VHJDVsDm8517cDGhuSP3pCHp8y5fjaj8ZFTZ_Ga3RYu2vEYUO7KuOPwVU1TfL0pTalJ5ynQkU-ewIMuecjYfwD_Jlyv7LofH0D2bVoCnT-N68gw6kDQCl73mnf2pU7809hTlXAILdecyBwCXp-yvD6VuxTuJhcCMcccXZuB0lKEgxE8dOcLhCK541oHqO83-uQTZ-jznA4AkzK5Q-vxaISSIs8PktFqRG1HdOdQ_HyTAuXJGoO7dpUwlg8eXZ3artjjTNOvQ_7auFv-E_HASLBhD1k5BcAOvQoSa-Mu0n5o_4Y6MwUn7q55VPnwoMb42nARm0MBHmD7Gj4TbkgXTsiavIa0oHVVvTnFENgLoTMj-oHpM3PRMehqbjOneOUfPnsSMIxARTY4mSPpS-WPr7Aqap0h1WgiYjRJwdrL_peFbNS7MnZYnu4eJqWHkjIFrgZvPuPyTxwvRJ7pmvLTx0tOx8daijg7C-8d7sLxcZeC0t1CdjCS0Tyx29X_OBUZHFZc3tiT02DCEbKmNxRh1Rvt-LVhvTohiACTD2Xku_6Shf-35aALKZKfkHkHsoRHWnbzpfx4ApCBbH2FlQ8MUO-RTiOV1ZSk38uB84S8zJwiN-Qrbak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f54d31d7.mp4?token=V4axIt-zoLExMdFBIR4qGUSVGcTV0E08Y-47oV7VncHFWfJDYZmw7b5T-VHJDVsDm8517cDGhuSP3pCHp8y5fjaj8ZFTZ_Ga3RYu2vEYUO7KuOPwVU1TfL0pTalJ5ynQkU-ewIMuecjYfwD_Jlyv7LofH0D2bVoCnT-N68gw6kDQCl73mnf2pU7809hTlXAILdecyBwCXp-yvD6VuxTuJhcCMcccXZuB0lKEgxE8dOcLhCK541oHqO83-uQTZ-jznA4AkzK5Q-vxaISSIs8PktFqRG1HdOdQ_HyTAuXJGoO7dpUwlg8eXZ3artjjTNOvQ_7auFv-E_HASLBhD1k5BcAOvQoSa-Mu0n5o_4Y6MwUn7q55VPnwoMb42nARm0MBHmD7Gj4TbkgXTsiavIa0oHVVvTnFENgLoTMj-oHpM3PRMehqbjOneOUfPnsSMIxARTY4mSPpS-WPr7Aqap0h1WgiYjRJwdrL_peFbNS7MnZYnu4eJqWHkjIFrgZvPuPyTxwvRJ7pmvLTx0tOx8daijg7C-8d7sLxcZeC0t1CdjCS0Tyx29X_OBUZHFZc3tiT02DCEbKmNxRh1Rvt-LVhvTohiACTD2Xku_6Shf-35aALKZKfkHkHsoRHWnbzpfx4ApCBbH2FlQ8MUO-RTiOV1ZSk38uB84S8zJwiN-Qrbak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلسلة‌الذهب؛ حدیثی که تاریخ را روشن کرد
🔹
در نیشابور، هنگام عبور کاروان علی بن موسی الرضا، جمعیت از ایشان حدیث خواستند؛ امام حدیث «سلسلة‌الذهب» را نقل کردند و با تأکید بر توحید و ولایت، آن را در تاریخ ماندگار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/665339" target="_blank">📅 17:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هتل‌های تهران هفته آینده نیم‌بها می‌شوند
جامعه هتل‌داران تهران:
🔹
تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665338" target="_blank">📅 17:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات الکساندریا کورتز، نماینده کنگره آمریکا به لایحه توقف ارسال تسلیحات دفاعی و تهاجمی به اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665337" target="_blank">📅 17:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کاخ سفید: گفت‌وگوها درباره توافق با ایران ادامه دارد.
🔹
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم.
🔹
طبق اعلام باشگاه پرسپولیس، همکاری با اوسمار ویرا سرمربی برزیلی به پایان رسید.
🔹
مدودف در آیین تشییع رهبر شهید انقلاب شرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665335" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAukRGzH84hgBWN_YQ4pix28A0-grRT12Hi5TDis-MC3eunkJLRimCApidAhYXuRqNCD0ZHsk_PG-utvid562unArkAX_HY059XyE3h1-CT1lk2r2RV5Ivix-efRf1D6WTxtpUmcN6FZtdbmp7711YaJkosrPYkI9znXjEjwYiijo6kzEe0Mg-7Sg0fOgJaXyiBRp2YaWoVAVTw1MFkhWygsgUpyts_fjWoIUf4ZnEHKGo6UXmEqgZZOTfZS9DNxrXZX6BezyqUC6N-0HyB34oyzgGkPhlvZwXINZnxerRz-ELRA6aLzH0R0KiRAs_bx7aoJ6hV3Bgl_9fJMZhsPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این چند اتفاق سرنوشت ایران و منطقه را مشخص می کند/ شبه کودتا در عراق مقدمه «سونامی» است؟
🔹
اگرچه ایران در حال حاضر، درگیر مساله جنگ با آمریکا و آتش بس در لبنان است اما این تمام ماجرا نیست. اتفاقاتی به مراتب کم سر و صداتر اما مهم تر در حال رخ دادن است. شاید یکی از مهم ترین این وقایع، دستگیری برخی نمایندگان عراق باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227179</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/665334" target="_blank">📅 17:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA0VvW1ukfgBGeYULbCHbuinfrkaK5pIJC0qmk6n-qD1_BotyVuDBZqu5pNH5vmXrx-U3liNdSh9BRkwWsUoWSxyT9BGxrvuAnEErmgiNN-gQcu48cfIgQyNzcpTvRIIJY0aaFHLw2nYvvEqQZuNrnb6edyCgjjXQl9XpH5F9ameuWUh1Au7XJQS28x1pnUf0xGGXI2oM-kH81mFbyaoF3M6jTb0A83MSX4tmBpREnhh0r9roCGohaMreRB4j3DGsr4WHBujPsBoUO9b8rJKjwkmRjou9Fqa3AucfvyUdQ4hAP5MdlEkxieS-F0UJA_BNq_NkmE3NUU9oMDY7zQynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه رنگ‌ها در قلب شیراز؛ سرای مشیر چشم‌ها را خیره می‌کند
😍
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/665333" target="_blank">📅 17:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
متفکر آزاد، عضو هیأت رئیسه مجلس: حتی اگر آمریکا گندم را به ما ارزان‌تر هم بفروشد، نباید از این کشور خرید کنیم/ نباید پول به جیب قاتلان رهبر شهید انقلاب بریزیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/665332" target="_blank">📅 17:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر مستقیم واردات کالا یا دور زدن‌های پرهزینه؟!
مجید شاکری، کارشناس اقتصادی:
🔹
مابین وضعیتی که شما از یک مسیر پرفساد و پر اشکال و با سه مرحله دور زدن از کانال آمریکا خرید بکنید و مسیری که مستقیم از آمریکا خرید بکنید، حتماً دومی بهتره و حرف‌های همتی به لحاظ فنی درست است.
🔹
همتی قبل از رفتن به ژنو، به روسیه سفر کرد و در عمل ابتدا در روسیه ترتیبات جدیدی در حوزه تنوع مبادی واردات کالای اساسی ایجاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665331" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
روایت بابک خرمدین؛ مقاومت، خیانت و مرگ
🔹
بابک خرمدین (حدود ۷۹۸–۸۳۸ میلادی) رهبر جنبش خرمدینان در آذربایجان بود که بیش از ۲۰ سال علیه خلافت عباسی جنگید. او از دژ «بذ» مقاومت را هدایت کرد و سرانجام پس از خیانت دستگیر و در سال ۸۳۸ میلادی اعدام شد. منابع تاریخی درباره جزئیات زندگی او اختلاف‌نظر دارند، اما نقش او در تاریخ ایران بسیار شناخته‌شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665330" target="_blank">📅 17:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت کار: تعطیلات هفته آینده شامل کارگران بخش خصوصی هم می‌شود.
🔹
موزه‌ها و اماکن تاریخی ۱۵ تیر تعطیل است.
🔹
رویترز: کویت پدافند هوایی خود را با کمک نروژ تقویت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665329" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
امیر قطر با فرستادگان آمریکا درباره ایران گفتگو کرد
🔹
شیخ تمیم بن حمد آل ثانی در دیدار با ویتکاف و کوشنر، دو فرستاده آمریکایی،  تازه‌ترین تحولات سیاسی منطقه و به‌ویژه وضعیت لبنان را مورد بحث قرار داد.
🔹
محور اصلی گفتگوها، بررسی آخرین وضعیت مسیر مذاکرات ایران و آمریکا بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/665328" target="_blank">📅 17:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
در حمله افراد مسلح به ایست بازرسی سبدلو در بانه تعداد شهدا به ۳ نفر رسید و ۵ نفر دیگر مجروح شدند  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665327" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665325">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
هشدار گوگل به میلیون‌ها شهروند ونزوئلایی قبل از وقوع زلزله
🔹
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/665325" target="_blank">📅 16:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای نماینده مجلس: تا زمانی که ۱۲ میلیارد دلار آزاد نشود، هیچ مذاکره‌ای در کار نخواهد بود
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات برای آزادسازی ۱۲ میلیارد دلار از منابع بلوکه‌ شده ایران به توافق اولیه رسیده و تنها موانع اداری و اختلاف بر سر بازرسی‌های سرزده باقی مانده است.
🔹
ادعای ترامپ درباره آغاز مذاکرات در دوحه شانتاژ خبری است و تا پیش از آزادسازی این منابع، مذاکره‌ای انجام نخواهد شد.
🔹
همچنین ادعا شده است که پس از توافق نهایی، زمینه سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران طی یک دوره ۶۰ روزه فراهم خواهد شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665324" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665323" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjpvhcknutsc5d97qJVFBV6SudsbRY5-D5mjMqzcTohQlxUcDEh15CaAc7lFIDMRqvKTQNgXwwGycQPEQhV_60HVMA_4TfyW9puqxHr9lWHcjkUn5cNzafKCjdO_3BFn2dP9q6N0YYNEqujdxS49D1fX9kzHO7mRdGdZgwbDb4OngLljMzijt-CiaiGCTI1eWa-zvTT-gxrZLFErazGPTd2LWASNa4payiPDl7ERMB-ZYOFHIK3p3ryGyr-N8h8iVFwN35aV5OyWe2Qk11O1eAkLHls1CgsxUdlziqGqAEo_kC74TZPnSh5OkB7C669G--8U1pPe92JJLjAWBy0dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBkdWI4Rm2J_5b9ZbY4OktZ9mO-DYEMyP7lZ7SrCPbZe1u9Nr0HSU22drFJZ8iTyuWySjMtT1Jv6yX8A81YrrMdRsyNOZeXW5bDKglr2wmRFesNK16GPp2DlN1iGfrVDbHDhbM7uVNAHPN_aT3N2j31T5AoTizCGfmFSXUKrTnlSIuG9vWFgVmL4BhDFAOcusU-8oqtHmooOgzwQ6HcpGoAC27sZU32GDtEJ61DAGT5-8ExjIyKKFwXZSG31uFi7KoeymKVx1daa_flNuc7UrhPZ68brtyLpkAW65UP2vlkXOcgOPcxUqHTsRlaS3mcvvuVvmxd_Cmoer_q95rtyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یک چراغ خیابانی در وروتسواف، لهستان که کاملاً با پیچک‌ها پوشیده شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665321" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665320" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665317">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ روز دهم</div>
  <div class="tg-doc-extra">محمد حسین حدادیان قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/665317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک ویژه مداحی هیئت قرار ویژه تشییع رهبر شهیدمان
💔
🥀
بر سنگ مزارم حك کنید؛
او غریبی بود که جز آغوش قمر، پناهی نداشت.
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/665317" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4BKyIbcgg255TWyUsZsAKzWnelgjhvae_LosvBXcUStUi9R3537fI7BcAba_8nq7W3BXoIPUCRZLZFv0UVeuYOJ5Skql2KzBX7BOe2T8CK0PDN76Aw0Xck4YaA6MzPlQ9zhoXZBx100xBxydCeEYyk-AKXMXAbx78F42DbAIo_BQ-S03ieOWFh8y1FcxRPqG0E5td9BVc1Z9iTI2RAXd475v46GxE-tKlzrXXQIwd0_foUQD--zyKkX9lryh8hmuXWkYCvhW2hsRRBjJy1AriVssZGyC1zUS208fNcgSWfHhIKUdvOoRJy8UxYutoXoM1AhBWL0aAIGgYglS3eCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtRJXojo3pL0LM9uHpndP9OpISXeyRKvJh3ReZ7Fd8mIz8NTiBTtqDOMY14G8wRpF01cvCPZfbT3lOdxuTMctfIj2J0FhDmY2p44--ooNQoAtfrZCXf-QyejXY7Ee_AoQslh8aWKR9GyV8Hr8KCc4mSdh5gitwYXMLrkhxItQC_MQKSKIsiuiXNtesVftQL0wIGO81tfpch8ua0TrwnqSXolvW4QsVFVX0qQExpg_sL-_pSu0uRM7-ljE0W8b7xr4DbUweRds6EcEoUHWuO2CiHnJkyuWyx_6zq_6o6qP02E89J9nzH1CM4oBt00Q7CuEvgWXp-3FL8juIuMieDgrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست رونالدو، سرنوشت عکاس پرتغالی را تغییر داد
🔹
یک عکاس با ثبت تصویری از رونالدو و بازیکنان پرتغال از روی سکوها و درخواست هزینه آن در کامنت، علاوه بر تگ شدن توسط رونالدو، موفق به امضای قرارداد با تیم ملی پرتغال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665314" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCmCY5RuzT3Be52aLFtrMSEKXrMzuLpUOpenl6iqYMtn8a6GCkjYwSgohuLkvC8IcCppwkAIrHIaScufBqhVQ1m6exs1lVGVbBCvMHa8MebrNqEKg26XISOphvoFp5pti1P3RHvza9KGj2bmbFjEWsEczJEfRZe26K1VWzZx3bJ4V6mZPN9nqe7IMRObqo9mW_JuHLi8Wlx71xNmpd6uOScm2cBBcyrg6KWJmXmLQub5G-uBxnS1i32yi4RcHjQ5nlSm13jWAf53JvLjKXtcac1OWy5Bt0bnib77i1imN6HS6FT-aDuhpegHBDJK7IVjMXlnGtzW4FVPlldgY4_fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در حضور وزیر امور اقتصادی و دارایی و با برگزاری آیین تودیع و معارفه
✅
افشین خانی مدیرعامل بانک صادرات ایران شد
🔹
با حضور وزیر امور اقتصادی و دارایی، آیین معارفه افشین خانی، مدیرعامل جدید بانک صادرات ایران برگزار و از خدمات محسن سیفی، مدیرعامل سابق این بانک قدردانی شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665313" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbrash Group</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه کارخانجات ابرش
🏭
با بیش از دو دهه تجربه، به‌عنوان
تنها تولیدکننده
هم‌زمان
شیرآلات
،
لوله‌های پنج‌لایه
و انواع اتصالات برنجی در
شمال شرق کشور
،
فرارسیدن روز صنعت و معدن
⚙️
را به تمامی صنعتگران، تولیدکنندگان و فعالان ارزشمند این عرصه تبریک عرض می‌نماید.
🤩
با آرزوی تداوم
پیشرفت
،
نوآوری
و
شکوفایی
در صنعت
ایران
.
✅
ما را در فضای آنلاین دنبال کنید
https://www.instagram.com/abrash_group
https://t.me/Abrashmedia</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665312" target="_blank">📅 16:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفاوت حقوق ۱۸ تا ۵۰ میلیونی در بین صندوق‌های بازنشستگی!
ولی‌داداشی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بر اساس قانون برنامه هفتم، صندوق‌های بازنشستگی باید برای کاهش آشفتگی مدیریتی تجمیع شوند.
🔹
برخورد با تخلفات احتمالی در روند ادغام، تداوم نظارت مجلس و سازمان بازرسی و یکسان‌سازی حقوق بازنشستگان با کاهش اختلاف پرداختی بین صندوق‌ها لازم است.
🔹
تفاوت فاحش حقوق بین صندوق‌ها مثلاً ۵۰ میلیون تومان در برخی صندوق‌ها در مقابل ۱۸ میلیون تومان در تأمین اجتماعی با عدالت اجتماعی منافات دارد و ادغام به یکسان‌سازی حقوق کمک خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665311" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665310" target="_blank">📅 16:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnm09lz3RQUBeNQR1EzzGsDOt8ExdDqAjWvo_gArdgiKENy5_pFJlqDjembcCiOncll_RJ0dLa7nrNAByQ_gwhTFFpAWVajXk62dHg977mrQyrOronXMyKvqLfq4ClAnHwzqIGM4foVq0gKJvCc9ssJxmg4J2b_ye3-WPJY6IurGuAhY8EBXR-DuoDjjnHFyl5wvTpfnhrjtEYMKsY5BWAPV1WOUjMzC5T0Rz2eEkcLij8NDVp20CP1AIZTtWjL7UKTDg1-kkHPC8Xr1Wwc72AskgEQE_3FOKrcFirRBHW2f4znuZPORxezUqzcg-arXXuFNJxgbAxziH8kSyJE2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ تهدیدی خاموش برای طبیعت و سلامت انسان
🔹
پلاستیک فقط یک زباله نیست؛ تهدیدی است که از دریاها و جنگل‌ها تا سفره غذای انسان نفوذ کرده است.  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/665309" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/665308" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb7qOeFBnOWOVR4Z59ALaMWFARwcRqaI2aMZMD6NfNFQyK-zlOHW29sUGVE5dvirtdZOox6EEbf8JROJW9PzXi5H_eyQBN9sSrDLPbjLSyripDtEssDHKn-AblLsQCLXYJByma5KP6NR-In7AY-fYt8JQMEfKUNOrMklHYn4Kp0uaJGcXmX8fugwQ-13VGeSJihE5Wxs8RpfXLE-lxLzq-Jd02iNmIgA0P6x9PZ8usv-5K5RRfR1X5qHLDyGKCD9AxJamkBSSYVclipRYFVvzsXyr2hRjs1LLbuv6dWS6i8m1y4mMLcWQzbiXoxJYqUVXroynIjmuuaKhXt9LY8kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند پایان استعمار در جهان
🔹
در سال ۱۹۲۵، ۹۷ کشور امروزی تحت استعمار قدرت‌های اروپایی بودند.
🔹
پس از جنگ جهانی دوم، موج استقلال‌خواهی باعث فروپاشی سریع امپراتوری‌های استعماری شد.
🔹
بریتانیا و فرانسه بیشترین تعداد مستعمرات را در اختیار داشتند و بیشترین کاهش را تجربه کردند.
@amarfact</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665307" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SH-e8iw90vVKjJDdubr7eYUWws95mER1DMIHXNTibrueZBoLExjgn5rFDBr8nvGJfUlXz1mdsbBU3aauW0DjxtgsiNj06X8JrTeau2SWHH17xsNt9Fg-NC9oXLzpwAiYgcD2_Zmi23AC1wTDSZxMI590OccnCjwKz5VCAkqEHYbvFi36gZ7ASP8u_HuJFtW2wSZe5UlgNwKloFsONI8RDJtDIEn72S2AjhnFZz8NZ8p2E3i4pf8tx6CplpEz-V0EPfjiYXvaEkj51XJnvOggokDm-dGy0l8_a1q3b9FsHP9Xg6WgN8aLytaAvfVoELWUHpa0xHsPgPLO8uIO32eWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbzmWUxARPBGY9JsBzTWb9glrMjwLLInglLvydn1erw4tmBtPVHeXCyDf9bcvjrcX11SK2A5Is3JDBMwxnPEo1hv8gzZClwBU-hs1Qd5_jXU4NHp9tU7p85ubsNTGRgDxxw216W9Z-FF_qQsGizxyehrWImOWRDEcdlwLfRI4MEbgSVrgf9eMxJ8a_4VeTLtoJJ8pdi7k-52p-BIK63orX9tVR4QFLXiAagMVwJPaZIdKLwwmF75w9rNsIPy5QgEeXLDymEWxjbIW2ufBR1yI0MSWTsUibKxCnEaYz2blTdI2MxLAnENaW1LyftxsNzgXBKUqu4e7Bufv2Sip8uJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvAZ388wmSGf7f9U2j2cXtP15E2M-9XM9P8eTw9n7_barF27g73mVkFgDjdePWorMBtci0bxMpfX3nSmcGBsERNtJYXRd3jzEbPNs1MtZSLbK2k1751wGbZwpMKGWhFwSMir3yN6DhCIm5emLPRF5uwSsg3KpQJAdZKfJXIE_x-3GAMDDXdhKjFzeBjC486hkRUe00tD2pti1BZmzpvjr9llSow29jq0EvEba2Pe9hMHPrZd6z5afpra0iOFX0fOiPliaxJ9J5S1uI_mdX5lzfcc6oMgFB-Gxi7ybuTghzgbukRb2HLrh5i2ZA7MDUrcvEfhRO0ZfVs7lTfPRcjbpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ اشتباه والدین در آموزش سواد مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665304" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
