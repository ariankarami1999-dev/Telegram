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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-126487">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/alonews/126487" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126486">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کرملین: میانجیگری آمریکا در مورد اوکراین در حال حاضر متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/126486" target="_blank">📅 13:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126485">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودروی بمب‌گذاری شده در مسکو
🔴
یک نظامی عالی‌رتبه ارتش روسیه در انفجار خودروی بمب گذاری شده در مسکو ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/126485" target="_blank">📅 13:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126484">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: پزشکیان، عارف و من نظرمان این است که وضعیت حکمرانی در فضای مجازی مناسب نیست
🔴
ستاد ویژه ساماندهی و راهبری فضای مجازی با قوت به کار خود ادامه می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/126484" target="_blank">📅 13:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126483">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پروازهای فرودگاه هاشمی‌نژاد مشهد به روال عادی بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/126483" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126482">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=OAe8q-lxOxeXebMvq-SjxqTdvBA8fSfwV3mDYSZrHTeuMtncGZ6LKvL7U80miFZa4aFw-4v9uP8SDeSH6PrAZ3qgjt3QY2gwBFnlFnYbpsqzAMm9hcfuSTrQVx6jOlBXxzCJ9rqSz9RMWD0iJXyaa8-Ings1cnbQhY2aSszOFTqHEIfTK3R8VbcvHtEvwU5S5vJ4vGzMaLBL3p3sq5tgNmob7qEqVVWMyVLhjd4TtQ0SrrxWjO0PPYwV63GEn3qCokpRJpqxFQQwxQdHx7tP3ObUYAFhlhd8lv8aHATPCVzSdFmjzOH15k1WogSlRtARB8HJYrS6WQ0MNWjkdVg9nymaT_MJD8E9KGZPtZSpJJIJ9liYhsGBrdfypitVCDBNpGF7iV7Mz3jTugHriinesT8Coy2Z5-7_l0gGbckRDMZZun9KtJmx1IwHNVVRXjsLn0UDJtvNu1mvSK0OvNSTxaNaL9jxmHHmB6Dak7jpfMIEgnTnk3ig0jDatXGLlQfXSciQABv-TZ7Ad82vJMRcsw-HTofgsgfScpc74bgG0PaVeKF353PGTIyVeN2jl2NW1Ci-jxAlFETY-guhjf2eChotUKUiZMTyhiwZNEqffgFAg1muke_DHVq5FYfpuENZPNazyrIx6vtk8YXydUKnB1J5G6mljuHFmPlLqEpQrCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=OAe8q-lxOxeXebMvq-SjxqTdvBA8fSfwV3mDYSZrHTeuMtncGZ6LKvL7U80miFZa4aFw-4v9uP8SDeSH6PrAZ3qgjt3QY2gwBFnlFnYbpsqzAMm9hcfuSTrQVx6jOlBXxzCJ9rqSz9RMWD0iJXyaa8-Ings1cnbQhY2aSszOFTqHEIfTK3R8VbcvHtEvwU5S5vJ4vGzMaLBL3p3sq5tgNmob7qEqVVWMyVLhjd4TtQ0SrrxWjO0PPYwV63GEn3qCokpRJpqxFQQwxQdHx7tP3ObUYAFhlhd8lv8aHATPCVzSdFmjzOH15k1WogSlRtARB8HJYrS6WQ0MNWjkdVg9nymaT_MJD8E9KGZPtZSpJJIJ9liYhsGBrdfypitVCDBNpGF7iV7Mz3jTugHriinesT8Coy2Z5-7_l0gGbckRDMZZun9KtJmx1IwHNVVRXjsLn0UDJtvNu1mvSK0OvNSTxaNaL9jxmHHmB6Dak7jpfMIEgnTnk3ig0jDatXGLlQfXSciQABv-TZ7Ad82vJMRcsw-HTofgsgfScpc74bgG0PaVeKF353PGTIyVeN2jl2NW1Ci-jxAlFETY-guhjf2eChotUKUiZMTyhiwZNEqffgFAg1muke_DHVq5FYfpuENZPNazyrIx6vtk8YXydUKnB1J5G6mljuHFmPlLqEpQrCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به شهر ساحلی جنوبی صور حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/126482" target="_blank">📅 13:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126481">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f61dlTgV9r-csYjBBn4_-AZ15rq7u543s_yA08yV6BQ5M5Lu2A7aO81d_DLfROGP2UNRYBW7BXV3bNbIFo1CmHlcUTcFBhGDi4i7sJudZjdH7NQ4rkFhZnXXgMs0Ss6D517C3tIfpF6n1fAkS9M2w5MpVp9Tt3cntIDZT8Kh42hKOFO19Zfniw5k2VD2O5e9ZMDUpo4xUfI7O6KleQLiE-x-DBUjm-67jb8ilGwx1W0DbmyeviGXgqHUyDD2_tCwzr9YWywC-2M-pXR-oXMz7xA3KyvbrbuMyfXbALw_4AMiGQ1WvA9vSH0h5cf34iFDoyIoWwtOJtf7_5Fr5pfllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۱۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126481" target="_blank">📅 13:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126480">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیروهای اسرائیلی در یک بازرسی نزدیک اورشلیم، هشت عرب از یهودیه و سامریه را که در دیوار دوجداره یک خودروی تجاری پنهان شده بودند، کشف کردند. راننده تلاش کرد فرار کند، اما پس از تعقیبی کوتاه دستگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126480" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126479">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
به گزارش تسنیم دو عضو از یگان‌های پدافند هوایی روز گذشته در حمله اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126479" target="_blank">📅 13:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126478">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
زلنسکی، رئیس جمهور اوکراین :
- روسیه جنگ رو نمی‌بازه، ولی هر روز داره کم‌کم ابتکار عمل رو از دست می‌ده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126478" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126477">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126477" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126476">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
یک شاهد عینی اعتراضات روز سه‌شنبه در هرات به افغانستان اینترنشنال گفت که یک کشته و دست‌کم ۲۲ زخمی را از نزدیک مشاهده کرده است.
🔴
منابع محلی دیگر نیز زخمی شدن شماری از شهروندان و احتمال کشته شدن یک نفر را تأیید کرده‌اند. با این حال، تاکنون آمار دقیقی از شمار قربانیان در دست نیست.
🔴
اعتراضات روز سه‌شنبه در منطقه جبرئیل هرات در واکنش به موج بازداشت زنان از سوی طالبان آغاز شد. به گفته شاهدان و منابع محلی، نیروهای طا/لبان برای متفرق کردن معترضان به سوی مردم شلیک کردند و تجمعات اعتراضی را سرکوب کردند.
🔴
منابع همچنین گفته‌اند که طالبان شماری از معترضان را بازداشت کرده و برای بازداشت زخمی‌ها و معترضان به شفاخانه‌ها مراجعه کرده‌اند. به گفته منابع محلی، طالبان همزمان نیروهای بیشتری را در منطقه جبرئیل مستقر کرده‌اند و فضای شهر به‌شدت امنیتی و نظامی شده است.
🔴
طالبان تاکنون به‌طور رسمی درباره این رویدادها اظهار نظر نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/126476" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126475">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ به بی‌بی‌سی: اگر به نتانیاهو بگویم کاری انجام دهد، او انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/126475" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126474">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تنکرترکرز: نفت‌کشی که در ۱۵ مایل دریایی سواحل عمان دچار آتش‌سوزی شد، با شلیک جنگنده F-18 آمریکا از کار افتاده است؛ موضوعی که سنتکام نیز در بیانیه‌ای به آن اشاره کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/126474" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126473">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی دولت: ایران و لبنان نه نیروهای نیابتی یکدیگر هستند، نه برای هم می‌جنگند، بلکه دشمنی مشترک دارند
🔴
تیم دیپلماسی ما متشکل از افرادی است که به شدت به میدان آگاهی دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/126473" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126472">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNuJhQ8c3ZSQVXhJtiEPG8Le2U_HMS01QO9qI4i-exiRVdWbsyuL9WV-wxh98956muDb-VpRNQJSSAP8bNc1hL_3G9NodzghmJcHup7U0jTc5FTGhrdq0ix-KKNr8UW2loTQH6qXLkZUoYwVOQ4FZsjZHlUHaGBVjfLBMRpb_rEtIusOZKqTDcQS2_4xKXHOAk0i9u0WjXO6F172ZzhQLprambiAjz7sbk7aeo4hpBss2Z8VXp8MnXXQwuMXct8E17xkAnTia18ryRJXfc_TV68MRAfdi2Af4nWLL-WWFe-fY9TQnAHXBMiIx9YED5WYEkLzaw1cakv-JNkqzjOOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش بیش از 114 هزار واحدی به 4 میلیون و 540 هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/126472" target="_blank">📅 12:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126471">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq67o4AFtEKGHIDMYKSBkhk6JSdqRwugbXeH3I85Uov46z5iJwzXRmnsx6rZdP6fpO4itVjHkKR7SQtUCPhiefeJ_1fY9Ki-JfkuAJXBHBO1JoPNvdBbRk9yVTdxkyXu_0cSvrjMmO3kKNHZQlFKutv-UNulfjob5RkhchiOvdKBCJhA-LJRghPhpSyx2PsAkTFG2P4ZM6TiqjJ6fOJnnomUfezkgjSi-4dg1dmMBsR-f3rbNxB18Y8enqG50PSqYOiPVBz__M70adFQc7tzQfqgTocXokMHSPGbIm1PyUihc3RuTdNLSho9siE0rATz4C2SD6KoTQ0bc1VmOcgiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فکر نمیکنم حالا حالاها جنگ بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/126471" target="_blank">📅 12:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126470">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر ارتباطات: شبکه داخلی ما با قطعی طولانی‌مدت اینترنت، آسیب‌پذیر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/126470" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126469">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/126469" target="_blank">📅 12:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126468">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر ارتباطات: خسارات وارده به وزارت ارتباطات ۶۸ همت برآورد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/126468" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126467">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر ارتباطات: دنیا دنیای هوش مصنوعی است و ما مانده‌ایم ارتباطمان برقرار باشد یا نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/126467" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126466">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=pGOJgaNGrnpbTrdKLv-a2C0859Y4XavJj57qenJPpowjSNerEGDyWXBiLazpCnJLBTFBaJFSaV1S_lge8DLjLQBr_eBnR0b37ZN-gNCToTfLEfvpej9jb2DYQ9jweeWSQ9kTwsAUo4Hk0p97W4_KR8aW9o6SGndXQ1cDwVeFxGP-tuxTrzfoZxzgB-m3FCEei11cscb0LeZdribOIRW5Jh4Jz9VGdgiGNhPk7jHB36daf72_m8Pm7ccicklAiHXxio_sHm7HLvvuxa951b2LuV1qItLBTmm5HLHh1sHOsXSDMDY0WcHbA5tAzrrye9Tf3nTs7rYAJ3Nh13xdgPx29g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=pGOJgaNGrnpbTrdKLv-a2C0859Y4XavJj57qenJPpowjSNerEGDyWXBiLazpCnJLBTFBaJFSaV1S_lge8DLjLQBr_eBnR0b37ZN-gNCToTfLEfvpej9jb2DYQ9jweeWSQ9kTwsAUo4Hk0p97W4_KR8aW9o6SGndXQ1cDwVeFxGP-tuxTrzfoZxzgB-m3FCEei11cscb0LeZdribOIRW5Jh4Jz9VGdgiGNhPk7jHB36daf72_m8Pm7ccicklAiHXxio_sHm7HLvvuxa951b2LuV1qItLBTmm5HLHh1sHOsXSDMDY0WcHbA5tAzrrye9Tf3nTs7rYAJ3Nh13xdgPx29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان/تظاهرات در شهر هرات افغانستان ادامه دارد و طالبان در حال کشتار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/126466" target="_blank">📅 12:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=OITifU4gl-BBbYDA5ferpOp8ng5OdknIq5oLNvp63upKdWGtCMgLIPDfZzVooHqkrUypQbVlc_YjrDq19g2vkz8I0zty8NjngZ4iWrgtC2rzNIuAyBG9FVeYeldP5S1a7WIXKFzkRQFHhlRyrfFuKmzT_DLiUyvwvtJFEmRJa5vKo-LMYEp-0WeMX-LGddLVTOmNSMQIa2xZuW6iFLMbTvu7bAridLLkN5L1_dX8va5nAd8rV0ZNhJsEIq-l3atb9bu-0jz4oK0R3ZlnN_5RF8Sv2Eu9ae_ubzG-eeZ0sg9xj-xcyuhZPxY9EGzmakVtmvoIXBdRhlmnm7ERZpkcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=OITifU4gl-BBbYDA5ferpOp8ng5OdknIq5oLNvp63upKdWGtCMgLIPDfZzVooHqkrUypQbVlc_YjrDq19g2vkz8I0zty8NjngZ4iWrgtC2rzNIuAyBG9FVeYeldP5S1a7WIXKFzkRQFHhlRyrfFuKmzT_DLiUyvwvtJFEmRJa5vKo-LMYEp-0WeMX-LGddLVTOmNSMQIa2xZuW6iFLMbTvu7bAridLLkN5L1_dX8va5nAd8rV0ZNhJsEIq-l3atb9bu-0jz4oK0R3ZlnN_5RF8Sv2Eu9ae_ubzG-eeZ0sg9xj-xcyuhZPxY9EGzmakVtmvoIXBdRhlmnm7ERZpkcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126465" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
چین: مذاکرات آمریکا و ایران در مرحله‌ای مهم قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/126464" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سپاه : اردن به اسرائیل تو حملات به ایران کمک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126463" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=fzSLwDREwLyrcdCH-TWYDajb4B5AxYoIK0_YFpthdrlNq8WYWnhuBOC0PkCsb-RTt6BfOODp_49CvvNInWw1OZxmhraCZwf9Lj_7oOBvqfTtT32WAbjtcUxMAMWmSeiIUSNv1DLr2Bw6hJ7E7owzENXuxCqPBsnSKkj7l3tByGfTVvOsfkMAA5Gnv4AKHxCvnJEw87xFQc_m834HY4_wLk5tciCQgNGrVu9kwcs54dALO_demt4GV6jikKXSe2CH0BqTLdmMVWRT4Iwr1G6xYaEcGSKWXX_sT1TcMwu0ltrZnVZIRSTLLZTeHfG-DU4y_qFAYTOEIm7lwZ_KFflVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=fzSLwDREwLyrcdCH-TWYDajb4B5AxYoIK0_YFpthdrlNq8WYWnhuBOC0PkCsb-RTt6BfOODp_49CvvNInWw1OZxmhraCZwf9Lj_7oOBvqfTtT32WAbjtcUxMAMWmSeiIUSNv1DLr2Bw6hJ7E7owzENXuxCqPBsnSKkj7l3tByGfTVvOsfkMAA5Gnv4AKHxCvnJEw87xFQc_m834HY4_wLk5tciCQgNGrVu9kwcs54dALO_demt4GV6jikKXSe2CH0BqTLdmMVWRT4Iwr1G6xYaEcGSKWXX_sT1TcMwu0ltrZnVZIRSTLLZTeHfG-DU4y_qFAYTOEIm7lwZ_KFflVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به یک خودرو در روستای الشارکیه در منطقه نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/126462" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی دولت: میزان قطعی احتمالی برق تو روزهای گرم پیش‌رو، قابل پیش‌بینی دقیق نیست و مستقیماً به الگوی مصرف و همراهی مردم عزیز بستگی داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126461" target="_blank">📅 12:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پنتاگون در ماه مارس فاش کرد که بخش‌هایی از نیروی هوایی ۸۲ در حال اعزام به خاورمیانه هستند، اما این موضوع را که برخی از آن‌ها به سمت اسرائیل می‌روند، فاش نکرد.
🔴
دستور اعزام ارتشی که توسط کن کلیپنشتین به دست آمده است، نشان می‌دهد که سربازان از تیپ دوم، هنگ پیاده‌نظام ۵۰۱ در آوریل ۲۰۲۶ برای مأموریت موقت به اسرائیل فرستاده شدند.
🔴
یک منبع نظامی می‌گوید که این اعزام به برنامه‌های اضطراری جدید ایالات متحده و اسرائیل مربوط به عملیات‌های احتمالی علیه ایران، از جمله تصرف جزیره خارک، مرتبط است.
🔴
نیروی هوایی ۸۲، که نیروی واکنش سریع ارتش است، برای حمله‌های هوایی و مأموریت‌های «ورود اجباری» آموزش دیده است.
🔴
به‌طور عمومی، پنتاگون فقط گفت که سربازان به فرماندهی مرکزی (CENTCOM) اعزام می‌شوند که باعث شد بسیاری تصور کنند آن‌ها به سمت پایگاه‌هایی در کویت یا قطر می‌روند. مقامات هرگز اعزام به اسرائیل را تأیید نکردند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126460" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=iX5gThMRTPM_2WqXTaTxoUCC_BTtjmWSxTf9g4e9OFol_bwbie7-dNhSf2-earuQtKrzDi0m7n3iUnPD5PPLwwJWuk8LnXlLwMN5RfzmJn19OGp7lxd2eWDNJQYtf2Dfnnw6gFJavstv4g9nZeZLmyCb2sD9Zk0VFf11WKMvmWc9lCvOJYfHJYCr_QOpbFOA0q27Euuc0uwoKcd76SnHCmqDUxcpSWrhw-zRFJrCzXwp_n9aKjgAlBEQkGkx1fH9pLpfC6OF10giVMrhbUdz4Ch74dpW9jnEPdvMPfFD1qJor7kO_Mu4k2x0nUVpxmbRySKn9pGk1ITmf8LyhdrTPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=iX5gThMRTPM_2WqXTaTxoUCC_BTtjmWSxTf9g4e9OFol_bwbie7-dNhSf2-earuQtKrzDi0m7n3iUnPD5PPLwwJWuk8LnXlLwMN5RfzmJn19OGp7lxd2eWDNJQYtf2Dfnnw6gFJavstv4g9nZeZLmyCb2sD9Zk0VFf11WKMvmWc9lCvOJYfHJYCr_QOpbFOA0q27Euuc0uwoKcd76SnHCmqDUxcpSWrhw-zRFJrCzXwp_n9aKjgAlBEQkGkx1fH9pLpfC6OF10giVMrhbUdz4Ch74dpW9jnEPdvMPfFD1qJor7kO_Mu4k2x0nUVpxmbRySKn9pGk1ITmf8LyhdrTPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: اسرائیلی‌ها و ایالات متحده منافع مشترک زیادی دارند، اما همچنین شرایطی وجود دارد که منافع ما در آن‌ها متفاوت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126459" target="_blank">📅 11:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIfZK6FtRVhvdJRnxLa8x0s88qqSvKmPBWniCKx7Mw5qOyuk1Aa-poBcCl_g1ItbqL5HnCVSRa-LxhdW_Jfw0Vm7kI9fmN_zsnJEeiJpoYrZB58l8wMGCOJcbjAZnDkQzRBL9Wyv3fjcXrHaCWY23IrZVE6yp9gVPkjX_wST6gFo11GDBZ13UsqJKmpdZv29QTHbj8gYAIllRo-B_Z1UdPIqJATLWuX2sddrThxtMzm6SIPzT4y7Tekh-utFrw1MPxIyUXjt5WvUJ5oc1qyUWfv7jItwYKweo3BW8RKlGeJEJoDHVMIt3vioqoVtOjKp2KaFQA0C0d91RMcLN_VgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: پنتاگون ایالات متحده فهرست شرکت‌های چینی را که به عقیده آن‌ها به ارتش چین مرتبط هستند یا از آن حمایت می‌کنند، گسترش داده است و شرکت‌های بزرگی مانند علی‌بابا، بدو، بی‌ای‌دی و نیو را به آن اضافه کرده است.
🔴
در حالی که گنجاندن در این فهرست به معنای تحریم نیست، پیامدهای قابل توجهی به همراه دارد.
🔴
طبق قانون ایالات متحده، وزارت دفاع به زودی از خرید محصولات یا خدمات از این شرکت‌ها، چه به صورت مستقیم و چه از طریق واسطه‌ها، منع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126458" target="_blank">📅 11:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126457">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران:
فکر نمی‌کنم هیچ نقطه‌ای وجود داشته باشد که مانع شود. فکر می‌کنم بسیار نزدیک به داشتن یک توافق بسیار، بسیار خوب، قوی و قدرتمند هستیم
🔴
اگر برویم و بمباران کنیم، که اگر بخواهیم بسیار آسان می‌توانیم این کار را انجام دهیم و دو یا سه هفته دیگر بمباران کنیم، دیگر هیچ چیزی برایشان باقی نخواهد ماند.
🔴
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید که بسیاری از مردم کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نه.
🔴
و ما به یک سند امضا شده دست خواهیم یافت که در واقع قوی‌تر از انجام بمباران است.
🔴
شما به یاد دارید ونزوئلا را، درست کمی پیش از این، یک جنگ یک روزه.
🔴
ما آن را تصرف کردیم و روابط بسیار خوب بوده و ما میلیاردها و میلیاردها دلار نفت گرفته‌ایم.
🔴
ما هزینه آن جنگ را بارها و بارها پرداخت کرده‌ایم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/126457" target="_blank">📅 11:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126456">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=rIOdXtkfK5IWiEPY7rP4iiK3kTO0tUvKlnkZ-PAS38uXQZJzoIB3JGYPXG3A7rUXO4SKUcYQhObAZWjoXKfMWMBMFR4XphADh9rb3Ev3YBAN6YdSCFED5tU5Kn6PTPfmET2-LU3qDhUD5OoAkn892rDs0TCGhUU60viqHd9sTIDVxaU5190Fr3nLfNYkfnyL-yO8Xo0GfbhRravMuc9zt7HKTuRypPTcK7_JbZzpx73PW3fBNDKi3_P1TfYiv0wYvBIDUvusrSDm9FDmtpf7SQqBG-f7BI9yNGLwjfjG1EMZ2t2nRqQjBiefC-ap-srABifrGMaAG_AhATQm-Yxx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=rIOdXtkfK5IWiEPY7rP4iiK3kTO0tUvKlnkZ-PAS38uXQZJzoIB3JGYPXG3A7rUXO4SKUcYQhObAZWjoXKfMWMBMFR4XphADh9rb3Ev3YBAN6YdSCFED5tU5Kn6PTPfmET2-LU3qDhUD5OoAkn892rDs0TCGhUU60viqHd9sTIDVxaU5190Fr3nLfNYkfnyL-yO8Xo0GfbhRravMuc9zt7HKTuRypPTcK7_JbZzpx73PW3fBNDKi3_P1TfYiv0wYvBIDUvusrSDm9FDmtpf7SQqBG-f7BI9yNGLwjfjG1EMZ2t2nRqQjBiefC-ap-srABifrGMaAG_AhATQm-Yxx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر نوجوان سنندجی که قربانی خشونت خانوادگی شده بودامروز یکی از مهمترین مراحل درمان خود را با موفقیت پشت سر گذاشت و جراحی فک او در بیمارستان کوثر سنندج با موفقیت انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126456" target="_blank">📅 11:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=AhdYrXfK0oafjMdZFb6-XZ3UULMeueqeJPIxE6GNr-ifYyi2Zo6pbJYn7bnfeazKgzX7SELfDbQ1r_xt315TJNMPMPIMl0dVv6lN6fFSroNYfUGxXDAlkXvfn8W0Stpt-3e2rFiQTlxrN_ILOIdAZydUO2dWcqpGId5kXw5LKWlMpCqPeORGklTJWonoNBZrw51w28L0Bp_a7L1ADm7Rj5TIrDxm7zLrT-cyNLjfIikTjGC5SIPhqPRG6qrS5iA_MXv7vbR1G6dJiRT4UnTNPD_HerSNab_SCKe2vorxRH7j_Q63HaLw31fB7-mCocoETm5gHFV5FHK-zdKJBvAtaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=AhdYrXfK0oafjMdZFb6-XZ3UULMeueqeJPIxE6GNr-ifYyi2Zo6pbJYn7bnfeazKgzX7SELfDbQ1r_xt315TJNMPMPIMl0dVv6lN6fFSroNYfUGxXDAlkXvfn8W0Stpt-3e2rFiQTlxrN_ILOIdAZydUO2dWcqpGId5kXw5LKWlMpCqPeORGklTJWonoNBZrw51w28L0Bp_a7L1ADm7Rj5TIrDxm7zLrT-cyNLjfIikTjGC5SIPhqPRG6qrS5iA_MXv7vbR1G6dJiRT4UnTNPD_HerSNab_SCKe2vorxRH7j_Q63HaLw31fB7-mCocoETm5gHFV5FHK-zdKJBvAtaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران: ما مذاکراتی در جریان در ایران و با ایران داریم و این کار متوقف نشده است.
🔴
ما می‌توانیم حداقل یک ایده را در یک یا دو روز آینده داشته باشیم. اما فکر می‌کنم همه چیز خوب پیش می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126455" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=FHyqUotc8fQeZy6C-fI3zd6vwGZ0cKgZtvMi8WHnZvU-kFuLypBP9BhFP0QB4w5fNyhz3Ne0w1CQCT05d-M5Ktgj-nH8dfkUG-g1O8GVnYdaGbN6vkJ3654D2G6V1NqIk5Lm87jZNOUxT20AtBW1JocXXqJh8-T6W1ZRQciWa2o5OFsEj_jlVuBGXLI4W78ouviBQlmRoXNhAMbzn6k5oY85rXgBy6GhtFaDIBlQHQEOwJKPBDMJAf-1vJPZwRdMec2kMOIzhMnFffBNrFryhzcq9fK1I2svAUPe0aG3JooR71EtLNpugROnkhttn6iLhuVsbgzGy9nLX6TgxjjLrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=FHyqUotc8fQeZy6C-fI3zd6vwGZ0cKgZtvMi8WHnZvU-kFuLypBP9BhFP0QB4w5fNyhz3Ne0w1CQCT05d-M5Ktgj-nH8dfkUG-g1O8GVnYdaGbN6vkJ3654D2G6V1NqIk5Lm87jZNOUxT20AtBW1JocXXqJh8-T6W1ZRQciWa2o5OFsEj_jlVuBGXLI4W78ouviBQlmRoXNhAMbzn6k5oY85rXgBy6GhtFaDIBlQHQEOwJKPBDMJAf-1vJPZwRdMec2kMOIzhMnFffBNrFryhzcq9fK1I2svAUPe0aG3JooR71EtLNpugROnkhttn6iLhuVsbgzGy9nLX6TgxjjLrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در فینال NBA (نیکس در مقابل اسپرز) وقتی که تصویرش در حین پخش سرود ملی در حال ادای احترام نظامی بود، هو شد.
🔴
او بعداً آن را «بیشترین تشویق» نامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126454" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl8C8tv2W1kEP7RxWWYnXbbNBhQ09Oc-SzrBXkBkutj_dCWbhZrOaK4P7-WgTAuRAWG1jFeGkjhcbm4D3zALCko4UOnSB56CY_l5Fg2ytxp2qbbKehu5WH7Q5RBwBxIivjQXSC35f3g1mc-VRgZsTPa7aTpmgSmhHaoriDFXRoFwZOALG838lXBC02q_zPLku5BXGTrl2FeYdqazjC7QD1OBofrjs2-eCU4-29Sfu193KCngFmuLygO0sqjBbXswSb5DJeRnWDWkgNAUEVfM9H-M9FQ1t2W4nt62KBsN80T4l7AnzF5FJL5TSWHFigkfLSLgDMC3xPXF50lqv9RKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: ترامپ ۳۷ بار توافق با ایران را «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126453" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ممکن است اسرائیل از توافق هسته‌ای ایران خوشش نیاید، اما ما به دنبال منافع آمریکا هستیم
🔴
مجری: "شما چقدر نگران جاسوسی اسرائیل از ایالات متحده و اقدامات مستقلانه‌اش در لبنان هستید؟"
🔴
ونس: "ببینید، به نظرم واضح است که اسرائیل و ایالات متحده منافع مشترک زیادی داریم، اما در برخی موارد نیز منافع‌مان از هم جدا می‌شود.
🔴
فکر می‌کنم جایی که رئیس‌جمهور خیلی صریح بوده این است که در حالی که اسرائیل مشخصاً اهداف خاص خودش را دنبال می‌کند، هدف اصلی ایالات متحده در قبال ایران، اطمینان از نداشتن سلاح هسته‌ای توسط ایران است و ما در واقع، به لطف تحولات چند ماه اخیر، بلکه واقعاً یک سال و نیم اخیر، فضای لازم را ایجاد کرده‌ایم که رئیس‌جمهور معتقد است می‌توانیم به یک توافق بلندمدت برای حل مسئلهٔ هسته‌ای ایران دست یابیم.
🔴
حالا، ممکن است اسرائیل از این توافق خوشش بیاید یا نیاید، اما در بنیادی‌ترین سطح، ما فکر می‌کنیم این توافق به نفع ایالات متحدهٔ آمریکاست.
🔴
بنابراین به دنبال آن خواهیم بود، چون رئیس‌جمهور ایالات متحده برای همین کار انتخاب شده است. برای خدمت درست به مردم آمریکا، این کاری است که باید انجام دهیم."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126452" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126451" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر ارتباطات: ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126450" target="_blank">📅 11:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ef04fa4d.mp4?token=qi4k7pvG1v-kpqcvtBhfKELa2Q7GHFyPQ677_t6khhmJ5hjKBQ-aFiQRC1vBvosEZTh93Yq8EDYP9ACNC8Tb8oMhal-I5QBTtYBJiXkO2AhdXD_n3Wrhg55kP9t9tfJ8CihhMho96eNUPyvTNPdxSOPtR5hAidW7VlkuxaMJkiH7Oe0LK8FweQu5Pr9v7a4KuEaZopq8u60KTEoDODP0RuL_DOlfIhDbwljz-DGjzSlTIX42EH3A_fqbSaPGHiTxFeL7g5VGC8MxKM5mOWpDWwAzyntggrP5z8XKODMsOwaGuPuMqwxqR3dSzBy3At1X6hqBdFfP3BQEQ2R0Z8mcXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ef04fa4d.mp4?token=qi4k7pvG1v-kpqcvtBhfKELa2Q7GHFyPQ677_t6khhmJ5hjKBQ-aFiQRC1vBvosEZTh93Yq8EDYP9ACNC8Tb8oMhal-I5QBTtYBJiXkO2AhdXD_n3Wrhg55kP9t9tfJ8CihhMho96eNUPyvTNPdxSOPtR5hAidW7VlkuxaMJkiH7Oe0LK8FweQu5Pr9v7a4KuEaZopq8u60KTEoDODP0RuL_DOlfIhDbwljz-DGjzSlTIX42EH3A_fqbSaPGHiTxFeL7g5VGC8MxKM5mOWpDWwAzyntggrP5z8XKODMsOwaGuPuMqwxqR3dSzBy3At1X6hqBdFfP3BQEQ2R0Z8mcXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از  رهگیری موفق یک پهپاد پرتاب‌شده حوثی‌های یمن توسط پدافند اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126449" target="_blank">📅 11:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در جنوب اصفهان تا ساعت ۱۳ امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126448" target="_blank">📅 10:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6mhwiTtTQhaOE28yQDww-DR5LRsbxTbiBfSndRr60Yf0sRE9cQOgGzBEiOtdxaqVezTz6LOrhh5j5dKv-USJ2LopitMJSW_Fyn-T6ppX0phxq8O4AVQNMqCB9Vac8i2dkjJOxpdwAhKhfSunwru4JdGbHte4p5BMKysYU6pdIUDVyl2oAqpqfgW2-PsNnHnGg6Fw0c6Q27Ej8YyB61AkhhDmsKpriz2GGwa3kymJjScAmNIt_Hx_POHLXb8_bU0Z9aOXZC1tT6RYrelK6oDYKsOWkCllNRkyd5bYd-tlNt3DbX8yWB1_uffiMVCC_ads3PSdQIuHmTWsJKK1qcs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بستن بازوبند رنگین کمانی تکذیب شد؛ درخواست ایرانی ها برای بستن بازوبند مشکی
🔴
از اردوی تیم ملی فوتبال خبر رسید که مسئولان فدراسیون فوتبال ایران از فیفا خواستند در بازی با مصر که همزمان با ایام تاسوعا و عاشورای حسینی برگزار می شود با بازوبند مشکی به میدان بروند.
🔴
ضمن اینکه بخش رسانه ای تیم ملی فوتبال الزام فیفا به بستن بازوبند رنگین کمانی که نماد همجنس گرایی است در بازی مقابل مصر را تکذیب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126447" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7L1NMiiABeMUeUvMxVEsHEqEnQ6w3KQQ8xhLBtWgeBKupnhgbw2AzYwCxnQJadIApa0_0E0jWLdEPyuk6etu9xKTI-_KLi5cBCAHzwpsC7x-M4JDseVpyfXm0zUgpRVOD-KMoOZE-t81dl5W17ZWNZi7Iv1LqPgrnC0WnY_k6IQj9f7q8ay9SRdpO6Z1LDwKGpyNNJju6-zNRUrYnYhE3vwLXCA511RJ1uAyuxsSGdHy5ojNREuEt-Hrz1ZVZJu8_uxE4d8YjEBWh0kX3S7KUk7yhKODzC6syHexLea55dol2hvFZLtglAUGiZVE1AqUMAtJY7Hvm76uL2b5VMMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDsxeLM_VZJMpNGFjvXw1S5vCVgQYtD4peiyaN7Nk6eAQBJeEElU6e4JL8k7BZEq5_yV1IXG7lIQocf2aOAOtStSrIVIzHddmunoMwtEFWZaySX2Iy7oXqQtOHFN1kEJdjXmqeTOhllE4ybPmCn6rSV-y8MbfDN9ovqrFyDKZdvMDHX0nuOpNlMfqXzw17GIh_93BGzRYEzGv_RPk4OYsY7Kic56YfG3-uIuZYpPpOefjn_R1cHUCpw6LB_ma5olV38R1we_2_V3g3eoktYmXKO--ynrnSZdAR2Uzh1452QigHzb5FQZdu4sb_z3seg68586yrzlUrlMTqift0_6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1SZf8EPwT934dVz3HZURuljqYnZ6ljd4SL511oiThuwTjbeaClUVgKPCGyQI6I9QIIRZbj1Xw9Zz1DNl00GinPBmxdAXvb7EF77CFx1mnko3Qn4iB0PaWLhqpaUIfQzRaYw2ERcBM90N2jGDyAdkiS5IVP6X8zwPWl-4d6qMo2fgguRMdeMZEliSuQpu8f6V0IhFPI06FFnWua_KP_pU1jSQXjxp952dYHKcvBdOWqWwT9m0B3IOKvmZCZDvyhtRfQy4xaiomAE7dY9_as0XSnn8vSGckIznJ7Ga54ROz1sG2D0RGw_wGw1zbZ9MB9kUV8t7IWU2Ds4Z5m-56b77Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126444" target="_blank">📅 10:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126443">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت : اینترنت در حال‌ بازگشت است‌ و مشکلات فنی وجود دارد که ان‌شاءالله به تدريج رفع می‌شود.
🔴
موضوع اصلی ما حکمرانی فضای مجازی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126443" target="_blank">📅 10:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126442">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d982e90999.mp4?token=Arn765vwKEtJLGzzt8UXQOF9PKzAoIivtmeHVAsBznCcFKAoQtKUtA-w3Pdgdupg67GTcAJcx71AHt2vv4DfFD2dwFBcleaZGgQqHi2w1IpEdvEfRfWH9VhwHZkvKY4LcdGr-6dn6nJI6hS0EQmgZsG58gHMpUYLc2CT-9Qjm1ooCR862SlAlTTQWtTT2nC82MKDJLWACQDPtyl7M-MDs6mCuL5_Kh70bGXyBbuOKsoU8yi2szHewoNgnLNFwzuyPSalwWtwwgqCDrhAio4acOYaywi0owV_tJ3B7yV9yaQQct-9BjfMDtdz9Mk5SJKafwWgVBgW7suHN2jmSTQp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d982e90999.mp4?token=Arn765vwKEtJLGzzt8UXQOF9PKzAoIivtmeHVAsBznCcFKAoQtKUtA-w3Pdgdupg67GTcAJcx71AHt2vv4DfFD2dwFBcleaZGgQqHi2w1IpEdvEfRfWH9VhwHZkvKY4LcdGr-6dn6nJI6hS0EQmgZsG58gHMpUYLc2CT-9Qjm1ooCR862SlAlTTQWtTT2nC82MKDJLWACQDPtyl7M-MDs6mCuL5_Kh70bGXyBbuOKsoU8yi2szHewoNgnLNFwzuyPSalwWtwwgqCDrhAio4acOYaywi0owV_tJ3B7yV9yaQQct-9BjfMDtdz9Mk5SJKafwWgVBgW7suHN2jmSTQp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره ایران: ایرانی ها نمی خواهند این جنگ ادامه پیدا کند. به نفع آنها نیست.
🔴
فکر می‌کنم آنها به میز می‌آیند و چیزهای واقعی را روی میز می‌گذارند. ما، البته، بررسی می کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126442" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126441">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / ترامپ: توافق با ایران ظرف دو هفته حاصل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126441" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126440">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
الجزیره: برای ترامپ ضروری شده است که نتانیاهو را مجبور به تسلیم شدن در برابر سیاست‌هایش کند، وگرنه با او به ورطه جنگ سقوط خواهد کرد. این امر به ویژه در این برهه حساس که تحت تأثیر حل بحران تنگه هرمز و انتخابات میان‌دوره‌ای آمریکا قرار خواهد گرفت، بسیار حیاتی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126440" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126439">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh6Oj1QMqDOYf7VWeXYe79cVvrkqdyz4z4onXsO85uw5Wf9x6Me7yoNShDra36HY7RTRUSnhk9wnjWvtEboINAf_8uvir6TdrKmqPdaAYPF-VgJ8jVhvoWY0RpoFUVttJaeZOT_uXdFsB_3i-u9JdAdBQL_1hxZlmN9X-WsMacrPUg86Bj2IGckncapiOsjD_5muqWMoiTnAoYBNC83c32RVjWws1IFkQkrlzEHlPQu1x8UTbwjOeGQIQJT-MYkwakJH8wA7JhMospcxuKJL4UumBotBCyCKTw8If9Mdc8CSUy-plFKPO5mjP4VxKHTCVtQedKALTU73m8hJ07Xf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۱۸برابری حجم آب دریاچه ارومیه در کمتر از یک سال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126439" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126438">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMqGtnAHxxaXfK9zbb8SsMvzlGMQfz2Crg9PMgse2pm8aptNAMu3HOJIg8j59kv54Xr_f5-T6lE8i1uVCfRsjqPyi7lrfA38FUqhsBGot73oVHG_BKmemqovFKPmWYWFuBas5qnonh_kCB15cYJFp2uFPznODij3yNX5S6-t3bNsY5iS4Ed2Kr1xnZqXt_SBss33EU6s0DFmD8SyRltCkRfsdulZWdHI3d0zuFK_2Dw7Comtx-RkjAr9d6nL_cY_j3LOoiPUHTpyvZRNSf-UnkeI379sh6weM8Z0FhJTjaUfTAMVr0MQLQsEEJUYMgwqTMjl2AVOCZ8IwEWILm3E3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار تخلیه کامل بندر صور و محیط اطراف از سوی ارتش اسرائیل صادر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126438" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126437">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سازمان سنجش آموزش کشور : ثبت‌نام کاردانی به کارشناسی ناپیوسته از ۲۴ خرداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126437" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126436">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فارس: تجهیزات هدایت و پشتیبانی جنگنده‌های اسرائیلی در جنگل‌های تنکابن کشف شد
🔴
خبرگزاری فارس گزارش داد مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایه که گفته می‌شود برای پشتیبانی و هدایت جنگنده‌های مهاجم مورد استفاده قرار می‌گرفته، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شده است.
🔴
بر اساس این گزارش، این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌ها به حریم هوایی تهران مستقر بوده‌اند.
🔴
فارس مدعی شده منطقه مورد نظر در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126436" target="_blank">📅 10:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126435">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض مادر خانواده پرجمعیت با ۱۰تا بچه به مبلغ کالابرگش: ۱۲ ميليون فقط پول شوینده‌هامون میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126435" target="_blank">📅 09:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126434">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4wZACb44MSFbVUqxFUtLo_wnBOgrebp-FPfyuyjGnS0IBJaNkDtIFckSsrFBa8CcMvNNZxlZqKdEUxmueBX2VSqNV8itmR1Fei98X0YTyAb0WglLmEu3UWtkfNjxEzCjI5h00AIKmK6mYQSv7bDpATMiXgQ2FUtxJ7b0boIBZ1uPDjWhAHTPeZ-zihv5LBrWf1xuoqWeVgxwygil4I44mQb2bAijhbvomGAYlhj8IVe_zlQ1__l7Gxg55Kez_Ds5DuIXuanqu8p08JQXdmFkImSNaLd-bmwrJePIFt2FXiwtO5bXAE8DS2078fTpArYFvQhFbUYxMnL8NmtxQtP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر جلد نشریه آلمانی اشپیگل:
ترامپ، خراب‌کننده‌ی جام‌جهانی
چگونه دونالد ترامپ از جام جهانی فوتبال سوءاستفاده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126434" target="_blank">📅 09:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126433">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teLkdZLBpcqqX3IfdIpjqe_uZF5pSk6MDgnPD1sB3aCgn5xr-c1tnzispX-_DOayRyLZl_XWtf6ssDbwQGhqZaCOoZhOKGvWLHsRk9eBZ-nMTOYr5IA3pO18FNeDWjygHoHiGy__kud6OE15YKrnJ3o9RXBWEJDMijZeKAUZymQ5VUcJL_T3e_3q_ahCAavL2B7xjtTfkmlDUQ3Zpa_feUzpVEfI2Ipq0MUKlht2y6x8NsVBfdGCsSRC1vfJoh4vY9GpfGl0sUqN__DUno7-4_r69YPHNPbQCf0O135cGQZTLPaKCUdclDy9vCGA7wx3IvRmxAutidzc9vV5dg3fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخیره هسته‌ای فرانسه از ۲۹۰ کلاهک در سال ۲۰۲۵ به ۳۷۰ کلاهک در سال ۲۰۲۶ افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126433" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126432">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5QGCea6rAkiCWeWfgQjS5_h-WywY0uGiJLCzeeRxsR5Y6mGD3nGDYENkGBot57zVO9DyWguYQaryTh4lpFvwuPpZnrCep2oJmILc8B5tF0bwVf_1-hU5SOPn3amTldbCquMJhUFaHypOMZ80NSuOAE0JQmP02a0e31fyAX2m9swlS7R2r9C1hI8BsvXv8ve9u7hD4t2Mjf0nPlzGy1u4tD4lXp2jkjvaLOwgGq-ZRof5UlhqhwpCrkgRx7CrpP73IW46zQ5-g3TOHdVolOnkw2FjYBAwSOrpdwatMI9g8Ywqd8EWCeWW0VrTMSX08pO7vsSkl-4OjypajmKgn9tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: همه ما در قبال حفاظت از محیط زیست مسئولیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126432" target="_blank">📅 09:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126431">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=k2prF7LIcErFCyy8uYM0oPoxEoQlHTdYPKlapvjxOYHfyhKuvgC-k5z7y00nNCciApTF1d96LlRrZl-mtZj3L0Yikn4Osa_mjz6KE1Es7pOQ9O6Om9ySDI2lmYEb8oMRZ8krJRqLtB9C8C1v5uLxoLGfIs8W2wr3AkHcYhfb4o2bQCVERy4ExfmuBvyQP0gCZnBfVo8XFw3xMMDixvHGPUeOzG1FOjc38pBeRlfO3E59LkwDokKKsfnr4INxtod6noHImX7W9N987u1H1cPrRlzQ16DWm3vFkpGslxT1nQ977u8Y-JuwWxGw2uxcOyrU-6wUZFWqeqETDeihsxQpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=k2prF7LIcErFCyy8uYM0oPoxEoQlHTdYPKlapvjxOYHfyhKuvgC-k5z7y00nNCciApTF1d96LlRrZl-mtZj3L0Yikn4Osa_mjz6KE1Es7pOQ9O6Om9ySDI2lmYEb8oMRZ8krJRqLtB9C8C1v5uLxoLGfIs8W2wr3AkHcYhfb4o2bQCVERy4ExfmuBvyQP0gCZnBfVo8XFw3xMMDixvHGPUeOzG1FOjc38pBeRlfO3E59LkwDokKKsfnr4INxtod6noHImX7W9N987u1H1cPrRlzQ16DWm3vFkpGslxT1nQ977u8Y-JuwWxGw2uxcOyrU-6wUZFWqeqETDeihsxQpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126431" target="_blank">📅 09:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=recvB2L5NQqLDp7bWFGtakC2bIoVe52kNt1eIYtIIvogRD6y08A4xQkjRQ4ZvrtRux5jiTWL6Mkjj2L7PLw-XrqyHWacFym3TuEUK8bCsY81oxZM2Q04qxS-dMA_2SZbX6pZumgRdx3jv2jzeMQ5SRbRzPuE0fRCsbBpSGF8_Fp98AdEwu66kryua9yuKnO7Tn9MeT8wh02DHkRSS8GoHhKU0i_CgaABjA-W_BHKi5Q0v9YsWqhXyUWEHKHEqXDzAQQ-rs1q1hzQqrH89tvYGNPWVTf-4Nme7eBTiSQ9xvj459KbpCtJaJpvzewA9QeiZZMuVMO3zuJ3-qAYNQqzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=recvB2L5NQqLDp7bWFGtakC2bIoVe52kNt1eIYtIIvogRD6y08A4xQkjRQ4ZvrtRux5jiTWL6Mkjj2L7PLw-XrqyHWacFym3TuEUK8bCsY81oxZM2Q04qxS-dMA_2SZbX6pZumgRdx3jv2jzeMQ5SRbRzPuE0fRCsbBpSGF8_Fp98AdEwu66kryua9yuKnO7Tn9MeT8wh02DHkRSS8GoHhKU0i_CgaABjA-W_BHKi5Q0v9YsWqhXyUWEHKHEqXDzAQQ-rs1q1hzQqrH89tvYGNPWVTf-4Nme7eBTiSQ9xvj459KbpCtJaJpvzewA9QeiZZMuVMO3zuJ3-qAYNQqzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا از نتانیاهو خواستید که علیه ایران تلافی نکند؟
🔴
ترامپ: "نه. من گفتم کاری را که درست است انجام دهید، اما می‌خواهم هر چه سریع‌تر دست از این کار بردارید. چون آنها باید دست از این کار بردارند، این به لبنان مربوط می‌شود و باید دست از این کار بردارند، ما می‌خواهیم این کار تمام شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126430" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126429">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
غریب‌آبادی، معاون عراقچی: شورای اتحادیه اروپا در یک اقدام مزورانه، به اصطلاح تحریم هایی را علیه برخی افراد و نهادهای ایرانی در ارتباط با تنگه هرمز تصویب کرد. هیچ ارزشی برای تحریم‌های اتحادیه اروپا قائل نیستیم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126429" target="_blank">📅 09:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126428">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: ما خواستار آتش‌بس کامل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126428" target="_blank">📅 09:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126427">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: هنوز به متن نهایی برای توافق دست نیافته‌ایم/ ایران و آمریکا در حال پیگیری و تبادل دیدگاه‌ها و نظرات جهت رسیدن به این متن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126427" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSQm1qoUQMjn9jlYKC9SfDMHAMbBPL4N3P0j2YN7XpOGhqOUr7xEuryXBX3kAelnlWXPA6A55EfAivHzIXBCbpVgj1lj4yHSsZKXrGv9OyneLMeKbQRGIjGZKh2OMmzP4FJ2MCuTiJp10D2ktUwkzDpKVtfjyaOI5M1kXa58ypzcHx1-R4l2T1PID7V2iUqunE_X_c82UsEzzUGMj3n4IXR4moB6sNTPc2O9lstHF2OWEEZPaVU0fgMM0Blq8y1ipgyHXdCxqm0pVB_Rs43JhcllFkbCxyXmBOt3NVt3rKPLWrEN57sHzzHxSQQQC7KKPzXVdC-_K3LGXynwVpI21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس جمهور امریکا، با تأکید بر اولویت منافع ملی ایالات متحده، اعلام کرد: واشنگتن به دنبال دستیابی به یک حل و فصل پایدار و طولانی‌مدت در موضوع هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126426" target="_blank">📅 09:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126425">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/017bc45150.mp4?token=Ao6gtOga4Mx3UsVaNNYCPzOw7bqO48yPd4-bhYAnLwDvXr8z6TVNjcQro3tVTcLrXlA6WW5VtuP97GJSw8LSlagLLVCxYM81LL-gnBMOH0P0AynI6WrMkpVJFO5lPTYF68YtWhYmwCvOMc-iKRHrJAlM233nF4d56jCNt82L810sk7wtAO_GPHslnH-tYYP5_mwZ_7IgBN27irtH8__Yq3zSD6sKlUQMialn9n1SAw2bfqSxIbAil3NKm95QW37AJ6mrFYulwZe1vUXSUxnKCuyl3LRu-j__8TCt87gUl5tpDnjruTjGjQjC843JNC_r5kBZWbfSsv9El1c8brxV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/017bc45150.mp4?token=Ao6gtOga4Mx3UsVaNNYCPzOw7bqO48yPd4-bhYAnLwDvXr8z6TVNjcQro3tVTcLrXlA6WW5VtuP97GJSw8LSlagLLVCxYM81LL-gnBMOH0P0AynI6WrMkpVJFO5lPTYF68YtWhYmwCvOMc-iKRHrJAlM233nF4d56jCNt82L810sk7wtAO_GPHslnH-tYYP5_mwZ_7IgBN27irtH8__Yq3zSD6sKlUQMialn9n1SAw2bfqSxIbAil3NKm95QW37AJ6mrFYulwZe1vUXSUxnKCuyl3LRu-j__8TCt87gUl5tpDnjruTjGjQjC843JNC_r5kBZWbfSsv9El1c8brxV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/126425" target="_blank">📅 09:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126424">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
منابع لبنانی از دو حمله جنگنده‌های اسرائیلی به شهر النبطیه در جنوب لبنان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126424" target="_blank">📅 09:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126423">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابعی:
یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/126423" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126422">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
زمین‌لرزه ۵ ریشتری سرگز هرمزگان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126422" target="_blank">📅 09:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سقوط یک فروند بالگرد نظامی آمریکا در نزدیکی تنگه هرمز
🔴
نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/126421" target="_blank">📅 08:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ دربارهٔ ایران:
«ما الان داریم مذاکره می‌کنیم، و آنها می‌خواهند یک توافق بسیار خوب انجام دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/126420" target="_blank">📅 02:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=TPRejzY-W-QgBH7WtpCILfBnHowl9JyzYvUaM85mBUK7gSx5_nUWKlUFgVfeu8rby7pWMKk1I8otu-8oIwUOHFdZrtx-jHW72M429ag9ZGQl2ce_psmnPobbpyI8AH1eNU5c0rXTMVEiPf_3oeWEVo7as2YpWQZoPi9OxQOl-1TbPSkUhZORKM1lYzFYdkKUYR8P0iXLDH4ERWA3g1-GncesDa2lPkCldGmyze8VKKwWD-12A5xWnrJLBd3nNirBlJnNLMUL3ha1EXIVKC1xdvyW70Fo7VofP6OgOz_SZDAzkuXH1C6l15K1w1_dGLr1R3aSqBjOCselytJv5Lz17g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=TPRejzY-W-QgBH7WtpCILfBnHowl9JyzYvUaM85mBUK7gSx5_nUWKlUFgVfeu8rby7pWMKk1I8otu-8oIwUOHFdZrtx-jHW72M429ag9ZGQl2ce_psmnPobbpyI8AH1eNU5c0rXTMVEiPf_3oeWEVo7as2YpWQZoPi9OxQOl-1TbPSkUhZORKM1lYzFYdkKUYR8P0iXLDH4ERWA3g1-GncesDa2lPkCldGmyze8VKKwWD-12A5xWnrJLBd3nNirBlJnNLMUL3ha1EXIVKC1xdvyW70Fo7VofP6OgOz_SZDAzkuXH1C6l15K1w1_dGLr1R3aSqBjOCselytJv5Lz17g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/126419" target="_blank">📅 01:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itTV4KzT_C1sIB5nUUmRbMhKeV0vscV5eBDoCUQYLBsTaGm4Z82DILUZ1XkBxw91nVIX6jiM9pRzIoBEzdB60--wpi19CNnP3vvkx_oNFphsjeoAgvTFehIAKJemJbrOgTlDCIog0lWAn7Y-dxwcpPvzKXCyNKFOwC7uf6CCav0JiI_nDhvDkCW8kykBvooEAUcThDQbeF_aoxzTQdXProWgZLCNmJDmoItMRCVM1ANW1g8_Rx6DfBwcdF_o4X3cH1lclFYetsncg_DR_dXwgZGCpRT9yP9tPHCT115K31DLazvy7ETCOJLDQIQOjRiJ6W77rGXSyeGMyH3xaFaNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لشکر ۸۲ هوابرد ارتش ایالات متحده در اوایل آوریل به طور مخفیانه به اسرائیل اعزام شدند، به عنوان بخشی از برنامه‌ریزی مشترک اضطراری بین اسرائیل و ایالات متحده که از فوریه تکمیل شده است، برای تصرف جزیره خارگ تحت کنترل ایران در خلیج فارس و ایجاد قلمروی ساحلی در داخل ایران، طبق دستوری که کن کلیپنشتاین دیده است.
🔴
این دستور که در ۷ آوریل ۲۰۲۶ صادر شده، به چتربازان از گردان دوم، هنگ ۵۰۱ پیاده‌نظام، لشکر ۸۲ هوابرد - گردان معروف «جرونیمو!» - دستور داده است که به طور «ماموریت موقت» به اسرائیل اعزام شوند، در حرکتی که پیش از این توسط پنتاگون گزارش نشده بود. وقتی درباره تعداد نیروهای اعزام شده به اسرائیل و مأموریت آنها سؤال شد، پنتاگون سوالات را به فرماندهی مرکزی ایالات متحده (سنتکام) ارجاع داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/126418" target="_blank">📅 01:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903677489f.mp4?token=WOT8hyVc5F4rqQ9hQfPzG38h3Q3QO_xuB91kxVK8470k-o0KWyMIEHCc98Iv18kn44II9ftKLQjZifeoZNvCKNcHWuwO_B3ApYMJ5rI7qYIMy5RZBdseOqpQh18CPu8KvGE4-sEh0Dgw5quPezdEmVJLJBwdst5mFDFhnfzdfo0wyCo8aTKPI9uDajtbgr8Agai3GX8YgMOVYHe01BfrjuopReeJKDmsX8nzsxA11qkt6hPz8JKmIdNy-SB9PYeWTp4LqeBZpZS6AhoUmFBnWRhHpJ2JAUNrZWZDpvRvFGJZVYvyapiGM1Re0CsTEm6ghaotg9vv4MGsZleDCSHYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903677489f.mp4?token=WOT8hyVc5F4rqQ9hQfPzG38h3Q3QO_xuB91kxVK8470k-o0KWyMIEHCc98Iv18kn44II9ftKLQjZifeoZNvCKNcHWuwO_B3ApYMJ5rI7qYIMy5RZBdseOqpQh18CPu8KvGE4-sEh0Dgw5quPezdEmVJLJBwdst5mFDFhnfzdfo0wyCo8aTKPI9uDajtbgr8Agai3GX8YgMOVYHe01BfrjuopReeJKDmsX8nzsxA11qkt6hPz8JKmIdNy-SB9PYeWTp4LqeBZpZS6AhoUmFBnWRhHpJ2JAUNrZWZDpvRvFGJZVYvyapiGM1Re0CsTEm6ghaotg9vv4MGsZleDCSHYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در هیئت‌ها چه میگذرد؟
🔴
کُفرخوانی در هیئت‌ها توسط مداح‌ها برای ریتم بهتر و جذب یوزر!
🔴
سالهاست که هیئت‌ها از یک مکان مذهبی به یک مکان جهت فستیوال موزیک جاز و راک با ماسک مذهبی تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/126417" target="_blank">📅 01:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم نتانیاهو دوباره به جنگ با ایران برگردد، چون اوضاع خوب پیش می‌رود و ایران دارد کاری را که باید انجام دهد، انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/126416" target="_blank">📅 01:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126414">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzKNKFLK81xJc3uZftw0VuOWAg4nVgvPUD6mLdv0-QfWlnpcp0DSbeXdyTPYWGt0jjDQuv_cKLRi_-LFiGOFGJ-YUHTXFZRaJeyE-frZs4LMSQLxZcDtkYZa9LvhpsxiavUpjIKNbJXypa3vH3-z1StQVuMZVb_GfwsrZQkmdfIzdAgnC1JE_J612-oCXG0v7mDTv5lFL74ApduEoE-eBhK3LZ01moRoxXXy05Eu65pQH_mRyMEJI0uqvcB5HgjUgq8UnD00WyoUJdp9LwxarXr4k1R0Z-Qfn15rpJ3Fa_VbiBBQjrpdmUyd29lxD1WswHGIK1GD0mjqYsQctoGF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0774815f0.mp4?token=LtVT5Wc-ssa04VtDBmxaOlGFSAECBpW6fuE8hf9-ZX9zAZjxhw3ddbyrcFErFApKDVZrqsDpzfMElRc7JHEsfGWr2SgUsCzBhPwkcYt_Be12kpZDxOJJHynXaxgk51gMrdnqgk9D8gzgHvnZvE3UhQDT1b29xgnSYH9cjXQIXeiGPEK5Za7Px4SnC0oXV00QsO5-8wm4nYNtIVO82qer9pqOAr4bERW6tLzc8yyHD17HXwuACQskJJ0aHO5QSK0Phw4_3OKMkI7qKU2LgXoruB2zWoy47eBg6VLPTBCSleTp9OFjVKKibRCIhvwfEe-Z7gNLp54Z0EnUVOy6XVcl_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0774815f0.mp4?token=LtVT5Wc-ssa04VtDBmxaOlGFSAECBpW6fuE8hf9-ZX9zAZjxhw3ddbyrcFErFApKDVZrqsDpzfMElRc7JHEsfGWr2SgUsCzBhPwkcYt_Be12kpZDxOJJHynXaxgk51gMrdnqgk9D8gzgHvnZvE3UhQDT1b29xgnSYH9cjXQIXeiGPEK5Za7Px4SnC0oXV00QsO5-8wm4nYNtIVO82qer9pqOAr4bERW6tLzc8yyHD17HXwuACQskJJ0aHO5QSK0Phw4_3OKMkI7qKU2LgXoruB2zWoy47eBg6VLPTBCSleTp9OFjVKKibRCIhvwfEe-Z7gNLp54Z0EnUVOy6XVcl_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو عراق یه رستوران به این نام باز شده؛
ملت همیشه در صحنه هم انقدر واسشون کامنت گذاشتن که آخر سر مديريت رستوران هم مجبور شد این کامنت رو بذاره .
#کاظم_صدیقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126414" target="_blank">📅 01:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126413">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ان بی سی: ترامپ به نتانیاهو هشدار داد که سر به سر این نگذارد و الا اسرائیل را در مقابل ایران تنها میگذارد تا آسیب ببیند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/126413" target="_blank">📅 01:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7d98f6a6.mp4?token=PV0hajrNEbQ1UshyBkE_fsnwZg9I2CtkRn0iruYvmEu3uDmbJN0DB-lsRgwoDedRV-8dMyXiu6Czlo5VGzh85R30CLDcPbDqfS0Zlro6y8Tt8MR48D0QgJKZaGjKruGlSgPiyikRLzme4VZj-nyb-qZyQekz7yZVjtNuWyyvXMp8WT0BveIOgHm5mkAazXgqkmAsmaQw04J4m_vb5xDuUde10rjCaJjcAZZvHf1QbU0wdUqlC8ekRzMDS-cw6plm4tDPi4rPAi1sGPq6Aj7O0YOKXs3KHUqBR8TQ5QVY4zKnIscCibWbUBJxbpwjrOwN7rABeQ_JuCCQiuO8bMRVcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7d98f6a6.mp4?token=PV0hajrNEbQ1UshyBkE_fsnwZg9I2CtkRn0iruYvmEu3uDmbJN0DB-lsRgwoDedRV-8dMyXiu6Czlo5VGzh85R30CLDcPbDqfS0Zlro6y8Tt8MR48D0QgJKZaGjKruGlSgPiyikRLzme4VZj-nyb-qZyQekz7yZVjtNuWyyvXMp8WT0BveIOgHm5mkAazXgqkmAsmaQw04J4m_vb5xDuUde10rjCaJjcAZZvHf1QbU0wdUqlC8ekRzMDS-cw6plm4tDPi4rPAi1sGPq6Aj7O0YOKXs3KHUqBR8TQ5QVY4zKnIscCibWbUBJxbpwjrOwN7rABeQ_JuCCQiuO8bMRVcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک رهگیر اسرائیلی روی یک پهپاد در ایلات، جنوب اسرائیل استفاده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/126411" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyvQtS8m4E1wCr5u9PbXkRbmchdr5OxnDgE491fZrm2Hrt4qxfOjy3VKozCjz9FkuH8jQudb3ixcslwb3Ro3EKLN9GAf90u2GM-ENXXaKkbka6RYnEAnaPUHNQ_XGhfcs-PB957KeaQpMHv09DbHC4NplI3cij5cctUpRQbaOl4xf7hXOMTw6TKTW9j4zqhBOf8AIsG5zSaWmTomTbxOU1lBVFjmExv9r_1gzQv8hWEvZayaFTSlMapEl4090d24lG3Cl8MTQ7QAj-sz4K15Zqnq1zoPNFekD63WUpeDd4ho2-ReQJ7Jx2MpvqV1GwTAiEx9Kt1z5i7D7uMVE8JFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر براد کوپر، فرماندهی مرکز فرماندهی مرکزی، امروز در واشنگتن دی‌سی به کمیته زیرمجموعه دفاعی کمیته تخصیص‌های مجلس نمایندگان در مورد اولویت‌های عملیاتی نظامی ایالات متحده در خاورمیانه گزارش داد.
🔴
کوپر همچنین فردا به کمیته در سنا گزارش خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/126410" target="_blank">📅 00:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126409">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibCQUc_x_8ReW1DZVppZ4kXVBRyIU8dBx92TugW5zUcPVKw_OLwDrEbYBW38zbAy5AcQaZoQYtl0oMdD-9CT_EtOgnKcFEhGMbVKo1lyzUVpYP0p4wzQnB9S7gYq5EFdVGPg_0JmwOfnQ7nybOxhe-lt6z6M5Ngs2fyexS6T_2RQZ2cGEvWE46wR-dqdL7Iw_98qCSiKt1N3ICGIIQMJVeLoB3oxn5ujG9JCS3dnOl852CzNNXcQc-kwjW8CHkOxKHow8F73yrrIrNAGqa8i0hFNlGX9htLqoWx0TKpdw1uDEK8DRjdtIUIxByTIYbO_stiBNRkFu6uB6ROsnJxl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حمله پهپادی حزب‌الله به اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/126409" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126408">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
امیرسعید ایروانی، نماینده دائم جمهوری اسلامی ایران در سازمان ملل متحد، روز دوشنبه اعلام کرد که تهران و واشنگتن همچنان در حال تلاش برای مذاکره جهت دست‌یابی به یک توافق صلح هستند.
🔴
ایروانی در گفتگو با «آسوشیتدپرس» ابراز امیدواری کرد که دو طرف «به‌زودی» به یک «نتیجه نهایی» دست می‌یابند.
🔴
او در پاسخ به این سوال که آیا فکر می‌کند این توافق تا پایان ماه جاری میلادی (ژوئن) حاصل خواهد شد یا خیر، گفت: «امیدواریم، امیدواریم که اینطور شود.»
🔴
با این حال، او تاکید کرد که هرگونه آتش‌بس باید جامع بوده و تمام منطقه، از جمله لبنان را شامل شود. شرطی که اسرائیل آن را رد می‌کند. در همین راستا، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه تاکید کرد که این کشور به حملات خود علیه حزب‌الله لبنان ادامه خواهد داد، هرچند که در عین حال از انجام حملات بیشتر علیه ایران عقب‌نشینی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/126408" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126407">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اطلاعات جدید از کمک‌های اردن به اسرائیل در حملات علیه ایران
🔴
یک منبع نظامی در گفت وگو با فارس: بخش عمده‌ای از حملات موشکی جنگنده‌های اسرائیلی علیه ایران، از حریم هوایی اردن صورت گرفته است.
🔴
جنگنده های رژیم صهیونیستی به دلیل جایگزینی تجهیزات راداری و پدافندی غرب ایران، در حمله اخیر از «مهمات دورایستای هوا به زمین» استفاده کرده‌اند.
🔴
همچنین بالگردهای ارتش اردن نیز در عملیات رهگیری موشک‌ها و پهپادهای شلیک‌شده ازسوی ایران نقش حمایتی قابل توجهی به ارتش اسرائیل ایفا کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/126407" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126405">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cadc07182.mp4?token=MX6nbhwWhDciZZgWEWSrFakA6hE-Z91cbQWdTJqqp368dMRLm3KCvskn5W7ggUtr6xySpx8BlFNvh4R4eIh6ZwP76c3RBohvulPaaI1wd10UIhLruNLolP9Brh1MgjP1glK7exLQ9lJPSyHXc9N4KSe0cZpRVw3k49AD9MWZrqIcl-86hgMIyZyWHrFKgSfbNxbLw72-8d0Qo5yNXcBp1lPMWXJpfMhI9ln9rbbIe-bLWb5GH7p2YNDwquEAzOghZPybadm3Ik46oPmAnR9bLtaBCo_yEtHF3t9_n75DkkSKih0BBrkCrMbIZoAD5fukw45-7raGOOzY4UAW2HvBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cadc07182.mp4?token=MX6nbhwWhDciZZgWEWSrFakA6hE-Z91cbQWdTJqqp368dMRLm3KCvskn5W7ggUtr6xySpx8BlFNvh4R4eIh6ZwP76c3RBohvulPaaI1wd10UIhLruNLolP9Brh1MgjP1glK7exLQ9lJPSyHXc9N4KSe0cZpRVw3k49AD9MWZrqIcl-86hgMIyZyWHrFKgSfbNxbLw72-8d0Qo5yNXcBp1lPMWXJpfMhI9ln9rbbIe-bLWb5GH7p2YNDwquEAzOghZPybadm3Ik46oPmAnR9bLtaBCo_yEtHF3t9_n75DkkSKih0BBrkCrMbIZoAD5fukw45-7raGOOzY4UAW2HvBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
هواپیمای سنگال که رسید نیروهای امنیتی ایالات متحده اینطوری ریختن رو سر اعضای تیم ملی سنگال و چکشون کردن
@AloSport</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126405" target="_blank">📅 00:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126404">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4JBdyR8ZxvHZ8raqmg3kn00fz9o-Qjbeq4kh6N_EKizDdmjym9fXgDSfM5zEVynAaG3xmbJ95m6Cd8rxlMJfsA9Eg1o5zQP7zebdXNeVNjyuEmgXnZb6nUpWCOdc9GYkSH3BNgh2pUA2gOqHBxjbUT9eXuRP_XViaw-77QCggnbToG6yNLIEmMymZMqWUXZrPiofJshk6PlAcsudipPgu7wQcZh6H6EdrZpxOGCYGXEa162YUoQug28MH5WLZGLlELgA82H--y6N9yi77QrghJ_VLuOcd2YBaIti7SaIPFlEiMSNPerjQrf1Dlfr_aAunUiOQz00_floJ0Zpev2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
🆓
🆓
🆓
🆓
🆓
🆓
🆓
هر ساعت کانفیگ رایگان میزارن برید رایگان وصل شید
🔥
❤️
سرور هاشونم تضمینیه
❤️
❤️
قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126404" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126403">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: حملات اسرائیل به بیروت تکرار شود، اسرائیل شدیدتر مجازات می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/126403" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126402">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLqQ0arGbuPvAKZY63N7hEA3EKVX3MPYzGzNW65n5VIBG1WqTRKj8hHTDqFGpm9j2igFh4KDCJRFHVNdpd5IQKNZA_FCf70iC0bpviwJDU0JsJyig46K4430sPqLaGehixs4SrJqk7JvFoHJdeGD_SAJ84YYDAV8UrU7KeYqHMysl8t-i3SLzIGXS1XcMVPeOk15HviAL1OJfpcS0xQFK8PpkJcJy0FyqGjhX-L_bDQj0qEZv8lI6yiTIjldX13H9jEe7-9ojH6eJL7saan27ufEBJeDcUt6lGWBtQl0xbzR86VZlgQmltbyolljFSdKdCjor3X7A0LITL31dYz4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تاد بلانش را برای سمت دادستان کل ایالات متحده به سنا معرفی کرده است تا تأیید شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126402" target="_blank">📅 00:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126401">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/126401" target="_blank">📅 23:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/126400" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlLheooDoGCWWahUAxpFJ3S6RBVJcskYb7QRryJDgFKGN2nPMcgJQXLYpT8-LIcMdgrJajBSHZw3DqetyhmCjs8nxKErfSX4BESvSDMfvSxcezvlbky6Poa2YTcFMhP1N9TTyMzJ1OURJEK4hDnLIu7aLQSW5LwRLphc7bmO3XbI8BuXV6-UyhqYEwFJSZv9BtSVqxqQ5FsFcH_zyCnjtaGi-z2nHlCSCOO29RXQd9HZ2Qc_jlCxKgZwN75e8qI0akfk38mSm3RjBGdqC0741hXMveXMxUZQKrC01uQKSoHLvbHIMyeFHY1c19GxlyIg20pohqkVZ91wiDZ23u0dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه عبور نفتکش‌ها از تنگه هرمز در سال‌های مختلف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/126399" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126398" target="_blank">📅 23:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
منابع خبری از شنیده شدن صدای انفجارهایی در سلیمانیه واقع در شمال عراق خبر می دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/126397" target="_blank">📅 23:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5lHOd332OWnsmo2U1NLNAjeWc9n1WKSKSnDpATy0by5JpCjIFMMruhoiAO-VtNKv9H9bmr20gB47bST1vdHgL7pt1h-_5FiSJXAQ6Jb-bLnxG4pXnfVX75E6WZap1WfcmM4IwvZUDNnf6SYzx7QGr5FXIlDOI0fFP3wTwi7uAlyZKYivXUxoOSzEaC5kfcm2GP4nGBsw0h1eiWSIZUmOZRvGa0FxJEgS_3QIlUDyr6EjqGnXroPBcasIB_WvPMpkcb6wjvENFUSj2KVpdjz6hJzEbUT_PAeFF-MwuQt2ZsPP_LgnBE5jd8enacHcGVMtOTCS2K4d8uD7Ky0npR88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به Axios گفت:
بیبی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/126396" target="_blank">📅 23:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL6sFOltxNhfFHg-aOZgo6rriVHCbKpRLyuHefotaHcewd_ONqEIjc7QK3RkHyfvUIIvbK-fqsu1Wc8PErCLPXePGW-dWWbewdBpSq-jfecZPJ9bwVSdCC2OeD7LuSMo9FUbl6dq6kignYvfu6uYZorq8y8o4ZzONNCfETL1hv7MnIQ9qkbxUo7BxmboLP0boxycnc7F61ew5Y9_T8H8wonxOA-jRVLEC8qHUuewp_dMK2HRe_HETUNeX0j6aciaLYVY9tjrc29ePE9kHROsNphkzSw-FRVOJF3oQZCVy_YOVQ3Qau-7Wa-t6w-1BaRMm_kMwCsEa-XK2UnpNLHrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126395" target="_blank">📅 23:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=ikr4ZknwQEUt0i_yh_NCorlb1PRDNsaWDv4Rt2cHuZtBDSnSq6HE15i0WER82-lqxn-N6Oz2AtrulAdMhH3bxeukEXSbpadZlWN6PhY-Lsnza9i1KVjRQm3XDT-K9nS_-mjJ2VyU4ck1_yje-TR6QuBp4IktNh-Wxum8ko6eX6VWR8ptA-VJk5pkTHHfp59v20-MWo1wTmHW8fZz7jpVT6Ncx-OxAALW1GZxLHXbl-9qNWePWxo7lfaIQ74pCtI-2zno8rvDIeBuZgk-BYRQ6Vj6V176IljtELrLxHfOAZuKNdHq0V9dGPo17EgUj84Ct9jEvj0fBKQfKyVsMXnx1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=ikr4ZknwQEUt0i_yh_NCorlb1PRDNsaWDv4Rt2cHuZtBDSnSq6HE15i0WER82-lqxn-N6Oz2AtrulAdMhH3bxeukEXSbpadZlWN6PhY-Lsnza9i1KVjRQm3XDT-K9nS_-mjJ2VyU4ck1_yje-TR6QuBp4IktNh-Wxum8ko6eX6VWR8ptA-VJk5pkTHHfp59v20-MWo1wTmHW8fZz7jpVT6Ncx-OxAALW1GZxLHXbl-9qNWePWxo7lfaIQ74pCtI-2zno8rvDIeBuZgk-BYRQ6Vj6V176IljtELrLxHfOAZuKNdHq0V9dGPo17EgUj84Ct9jEvj0fBKQfKyVsMXnx1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدافند هوایی آمریکا یه موشک بالستیک از ایران به سمت پایگاه آمریکایی تو شمال عراق رو رهگیری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/126394" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwCmEBONNz3fzH-ofwU8fRbSBmEmEzYjebGIfApO5kt2ecSD-m3PF2q1kEW52liG_E4DE2tAqs9mGcOMOn2J848nKw7cNfy_-2tfHqQd50Do9M9nxA0AC1LeyyTzsZz-Sst6rEknRNIoThMpRmixsQ5zJ32GFGRwjZYvreehIpSF_smLzLcWYh0fFkoQ9LnxCF-auoGu2-_4RFNrko9FPjvE9M7Nc9oWzXYrvRSd1PdYyUfk72d6biI-lu5hml9Vypznum0pWDur9uhDlgAawSrk9WQsncLVFNTzjo1AnskH7zt-2x4YiDxKsbpqQt2iIzJA9IZJKw4tIt5PVYTM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=D1npt4Ov9eBbHtd4rW_3bovPCTRL05E0_Bw6_8WzRg_s7UzobODjDMkhc6_4WWbkdsGYYyMKAqHx1yynEGqOEalWfUU2n6d_O8ejVOWY-Hde8YHfTFoigTPbhdiKhIyt3sa3p-YdAkXOKEbj7pMMnlXcXWbezbzUk53ltlljc6f9At0zg1erxhu2FAK_2jgHcUbJZ6okz1PsSNym6RNbPGrKWFFBfyqyoAZ-j--spKulD_yzUoywmGkkz6AGfcgcblYubL5G2nJadwvhvrWf68F0UmYWug-xth841Zp1O5q8WtZiF1cvArpD82fRels8Ac4R2kvZ5UYvXqQfpwrTPnxA46FQ1h3BgMiI_aWyGSYI2FBCFHyLfHSRIs4wTHR7tJaI0nGXclHmM_oFYewS69HmphnNrnPUTst6XtnPya3p79oXknQ_gwkizd3Tu_HKnx9aUOFJVj4YplKviJpD-L1mUk-_M3e5VJfrJ0CUUArlsR9Ywzenles97b9ndgHnX7xi3pxE6e5KoxaiZCa8qP2IWWqyuADoSPrnbKWCrfeZRjVpLBWq_EWQHF-s1r-r3Q8tVDrBqHWW6shs_PXMt9jrnCvlkKF8vyTgnk75CvXahx4mFYR8aSbtKQxoHLHpjtQLS_dk0QEUycXrVPEnmJe69K87iEZ_5Yfw4FjNagc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=D1npt4Ov9eBbHtd4rW_3bovPCTRL05E0_Bw6_8WzRg_s7UzobODjDMkhc6_4WWbkdsGYYyMKAqHx1yynEGqOEalWfUU2n6d_O8ejVOWY-Hde8YHfTFoigTPbhdiKhIyt3sa3p-YdAkXOKEbj7pMMnlXcXWbezbzUk53ltlljc6f9At0zg1erxhu2FAK_2jgHcUbJZ6okz1PsSNym6RNbPGrKWFFBfyqyoAZ-j--spKulD_yzUoywmGkkz6AGfcgcblYubL5G2nJadwvhvrWf68F0UmYWug-xth841Zp1O5q8WtZiF1cvArpD82fRels8Ac4R2kvZ5UYvXqQfpwrTPnxA46FQ1h3BgMiI_aWyGSYI2FBCFHyLfHSRIs4wTHR7tJaI0nGXclHmM_oFYewS69HmphnNrnPUTst6XtnPya3p79oXknQ_gwkizd3Tu_HKnx9aUOFJVj4YplKviJpD-L1mUk-_M3e5VJfrJ0CUUArlsR9Ywzenles97b9ndgHnX7xi3pxE6e5KoxaiZCa8qP2IWWqyuADoSPrnbKWCrfeZRjVpLBWq_EWQHF-s1r-r3Q8tVDrBqHWW6shs_PXMt9jrnCvlkKF8vyTgnk75CvXahx4mFYR8aSbtKQxoHLHpjtQLS_dk0QEUycXrVPEnmJe69K87iEZ_5Yfw4FjNagc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار مهمات عظیم امروز صبح نزدیک بلوفسکویه در منطقه بلگورود روسیه منفجر شد.
🔴
گزارش شده که این انفجار ناشی از هیچ حمله‌ای نبوده است، اگرچه هنوز مشخص نیست چرا این اتفاق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/126392" target="_blank">📅 23:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126391">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آکسیوس: ترامپ صراحتاً به نتانیاهو گفته که از پاسخ به ایران حمایت نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/126391" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس به نقل از منبع اسرائیلی: ارتش اسرائیل پیش از حمله به بیروت، سنتکام را مطلع کرده بود، اما کاخ سفید را در جریان نگذاشته بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/126390" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کارشناس صداوسیما: مردم ایران الان یکصدا میگن جان ما و لبنانی‌ها یکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/126389" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:
آتش بس باید در سراسر لبنان اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/126388" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4u9deo6_zhIjadgrm_jD_3YWZk0Bg-pURjZ35WrCQxhHvL69dY6lUp1rJOpN1I1E7O717dBYTjWlyN0ie0vxDOhefP-dVhP-ewuftWwoYS0nnPO2X5YXKqGcFhCY8jIGCBEyNAegi3gsp1EKbxRjrsTXCRQ98Df7z4eJ8Gs4s5Cm94Z7yqCVWEdJGQ_h1EXm2iqVSMm3uGjHENNbYJ4w4xoPeEeOWghkrD1uLJQLsY2JNa8kkmaNsXKptDvXYAbPVDV7xCNr4KQG5nIaj0xkdGkd8FE4yYOpmeNz9IDmzJNSMWHbNVC-gLDabk3cEcjdpykk2YfmhkptnLZvfQgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیکا به کانال خاله دنیا جهانبخت تیک آبی داد و رسما تاییدش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/126387" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤩
⚽️
کامنت شاهزاده زیر پست فیفا :  آخرین رقص
🔥
😉
The Last dance
🇧🇷
@AloSport</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/126386" target="_blank">📅 23:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسایی: این عنو(اینترنت) قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/126385" target="_blank">📅 23:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=ane4keXGtFqvLboqEEGUha8GetKisw_eJmgsKW-JGFWtf6LDT1v5xwtjo-a76FGbXFV9dztYMz_BXc5bIlsQFnZ_Ssg-tCiPVhS924sQnUzMTDelEmN6d4gqaT2a65KKhrrGK_1dmpze7O-j6oQ6or1jahzpzERoC0Bo20Oglncfv0-Zz6rbwjz3GntdHLJN6vko4dtkxnpv8fMcgBX-VykAK1c0mHkUs2N9cQlka-6G38T4pppfySITtumbkJEX50zmkY52o3kyPro4WN5vTNMYGp5vUAtJF14jlpzzGrLtSVLfsTLNnhZap9nkGKUJ4xfIs1j2ydyoNWDAQo_TyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=ane4keXGtFqvLboqEEGUha8GetKisw_eJmgsKW-JGFWtf6LDT1v5xwtjo-a76FGbXFV9dztYMz_BXc5bIlsQFnZ_Ssg-tCiPVhS924sQnUzMTDelEmN6d4gqaT2a65KKhrrGK_1dmpze7O-j6oQ6or1jahzpzERoC0Bo20Oglncfv0-Zz6rbwjz3GntdHLJN6vko4dtkxnpv8fMcgBX-VykAK1c0mHkUs2N9cQlka-6G38T4pppfySITtumbkJEX50zmkY52o3kyPro4WN5vTNMYGp5vUAtJF14jlpzzGrLtSVLfsTLNnhZap9nkGKUJ4xfIs1j2ydyoNWDAQo_TyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محیا دهقانی، بازیگری که برا نقش رل میزنه: نصف جوونای ایرانی بیکارن ولی دائم در حال خوش گذرونین و خوب زندگی میکنن. خارج کجا اینطوریه؟ اگه برین اونجا باید صبح تا شب کار کنین فقط
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126383" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
اتحادیه اروپا روز دوشنبه تحریم‌هایی را علیه دو شهروند ایرانی و یک واحد از سپاه  اعمال کرد.
🔴
این تحریم‌ها فرماندهی استانی نیروی دریایی سپاه در هرمزگان، همچنین محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، و حمید حسینی، نماینده اتحادیه صادرکنندگان نفت، گاز و محصولات پتروشیمی ایران را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/126382" target="_blank">📅 22:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
🔴
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/126381" target="_blank">📅 22:51 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
