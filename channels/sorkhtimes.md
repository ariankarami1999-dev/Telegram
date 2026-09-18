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
<img src="https://cdn4.telesco.pe/file/JSIMW_Twgzkc6ypIkmj6G6eAmiafQqoZvB7tY_e5S14VYcwsls0aqYLfNdScWjmMSNhNMyjz0X_6QUwb-7Wq4cP_I54OS23C-v3Pepog9G-JbwKgBTlCi5xj8lm9hjXaVNRbKEOyuA8xx4lVZJ9qWQPe7n4OnRxKC-_Ql0NlQxb0xs5IY9cdKeNeSaJGIzj2dhbqcKk8-Du_iuSy0T_Qo4wpr1vXrYCUJIzPrcSABmY4Vwpcz70dGj_o3V6XrtjVcpc8-H71Lasl68cCDnnHWIuzcGGLNcxsxKQIBSOH-ab6HkaJ7rJw1eyrgVsI5CdczGTgGce1e2c2rMHqQgxA2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_I8ZQ8YM4A1IcklQIGCUXkntiPPzpSmmTzH74RmN6M62K0PVutD9l0FQD-umAYW6yXzA-I3tFUlcXnNZpXjwX4UDyucJB0a8m1USYLQhrjA4ZEWsCXUHEh5Ge4Puut3Tl5GRdKJMCnLfs-aaQKoEIUhnS8ceulOf-viYYqB4eWAeWTqtvp781TDrEwgaq6OpO6GILWupHuOJkz6xtbhwe7OXTbn43h69ncEZE-YvnAvciFG64TUpFozZdGa0Al46_T1EBJE6YFSQH3cBpk5f_NKTkzCHg75b2_t8GXSub0QVyj-o-rekDALIf5lXNV6BiGRH-iQFO7XoggiwD1ZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 548 · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=DtK2wRhcgr6c5ao1zHpM2b1pxCfUks9c3CJza-hRlTZhIWaOpsTpCr2SD0ilF8ARH2m-dV9abZlGBoLcojm4BKGNN4kBnFMiuo2_6xLxnvhBGQ54Sgv0Vaqk73V18SwTxc5ugyksWwjvpy2gbBEySNPTqE8TZDlnStdgMvxkWdEFPZHOyQSZ6ZEixgIcftQ0uoVyXS_W4VT0kqjdk0sWAydMWKKARE6x8J6nuOpHt9CJwWmj7CHMC5eaqJ9kkT_OlKLBAOuUzSSFMtz8CaB39fXFyw3i_7E4TNDRw5-up1KEYtL-tuteEoUO_ug2k-aeValXi_iTqGd-L3QJTpOcYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=DtK2wRhcgr6c5ao1zHpM2b1pxCfUks9c3CJza-hRlTZhIWaOpsTpCr2SD0ilF8ARH2m-dV9abZlGBoLcojm4BKGNN4kBnFMiuo2_6xLxnvhBGQ54Sgv0Vaqk73V18SwTxc5ugyksWwjvpy2gbBEySNPTqE8TZDlnStdgMvxkWdEFPZHOyQSZ6ZEixgIcftQ0uoVyXS_W4VT0kqjdk0sWAydMWKKARE6x8J6nuOpHt9CJwWmj7CHMC5eaqJ9kkT_OlKLBAOuUzSSFMtz8CaB39fXFyw3i_7E4TNDRw5-up1KEYtL-tuteEoUO_ug2k-aeValXi_iTqGd-L3QJTpOcYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 762 · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=AUFhQUqnA2lC-mCOA2BnmIpOPx6o35nSLj1rm0eOLp8snwFCYwUXCbt95xBsv81wbWxMFxN-H5JXnpXuoYVe7FXjbfM7BBLiVfiZ-xR2WXd47RtrPoE8Rqo6LwuEl2KNGt27Efl1IXwqLf9DNdCn4vo1xDU4GHdEd6363fAP4FZs8-u92eK_5pJ85Qzoi2JDwQ9k5GWdBrhURgPGcJmluEQ-WXmYD1ZJJJbqj3SZtRATR73XxOFRhlkPAG-bAvT2xnl3989PtdzTJV4DAk-h545yuGdpOFeH-dP7Db-r0w8ih3xyp8pYs93NxX2YTbsgVMHiIgANR2qMEi4nZHGPyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=AUFhQUqnA2lC-mCOA2BnmIpOPx6o35nSLj1rm0eOLp8snwFCYwUXCbt95xBsv81wbWxMFxN-H5JXnpXuoYVe7FXjbfM7BBLiVfiZ-xR2WXd47RtrPoE8Rqo6LwuEl2KNGt27Efl1IXwqLf9DNdCn4vo1xDU4GHdEd6363fAP4FZs8-u92eK_5pJ85Qzoi2JDwQ9k5GWdBrhURgPGcJmluEQ-WXmYD1ZJJJbqj3SZtRATR73XxOFRhlkPAG-bAvT2xnl3989PtdzTJV4DAk-h545yuGdpOFeH-dP7Db-r0w8ih3xyp8pYs93NxX2YTbsgVMHiIgANR2qMEi4nZHGPyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBYTnN2mUfN7cPxUt43SX_kFZhzdnDjUOjqM9Ey0wKtI0tLe0PLMruUdtnKPR6RiPF8LL5sS7xe1w54Krrh6Ln_sTlbchQ-S2hOuneoMpwxL3GUQ5WSond2QgM5YSoxUKiULcKcVRECrxQLBpKTUiHl7U8z8HP7_WzONiGwcJI9wd4-OcvmT8L2SB35SvYoCUQgLPFpmeCQgdPKE8du-IGT2IeKsYvEOeYsYq3P9MVnJm-jJniLJUyVcPOYJ7TlJn4KVlD3koSCdzKSMGhfamZW3kwcKkPbT-Y9R_Z4owNdjGEuSftgV9iy7JkJhvSntT3kDgRG2uCm4p-gJtUZRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgLnuZ2aFWlyFPbWeLb5VNxuS5jjM2kD1dd_hzWrk0-wtQA9lisjt7Wd2C2F6ku-Df8rt_-70XX7O_JSbvwvujKCp5i7AwokBdN4Xh49SbJpUJtyIoIc9GxxTb0xXwbb_7AobTQwQzvh7l-Egk0C-O-JohMhhqGGrXmUYoXHfhwWJtX16fMcV47pXefumpSsGLqjrnyEYTJZDtPVQgmwVKK-sJPS6irU-i1nGUlfVz_IYKj2m6UeO6nRi601mrxjHpwhGg6GEZTwA2ITJCYvv_ZLFZL8vfZhKVYZkp7PwYaTkq-NJJB5nEJenuI7-2f1L4FnqHNGGawtYsak5ejSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن در خانه؛ جایی برای لغزش مقابل یونیون نیست!
[
بایرن‌مونیخ
🔴
🆚
🔴
یونیون‌برلین
]
⚽️
بایرن‌مونیخ با مالکیت و فشار بالا، احتمالاً از همان ابتدا بازی را در زمین یونیون دنبال می‌کند. یونیون برای دوام آوردن، روی فشردگی دفاعی و ضدحملات حساب خواهد کرد و فضای کمی به بایرن می‌دهد. با این حال، کیفیت هجومی بایرن می‌تواند در طول بازی اختلاف را رقم بزند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140225" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140224" target="_blank">📅 12:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140223" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140222" target="_blank">📅 11:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
زگوزی: تراکتور بسیار بسیار پرطرفدار است و پرطرفدارترین تیم ایران است، ما فقط در ایران هوادار نداریم و خارج از کشور عاشقان به تراکتوری زیاد وجود داره
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140221" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
زنوزی به خداداد عزیزی قول داده که با توجه به روابطی که او دارد، محرومیتی برایش در کار نخواهد بود و از این جهت خیالش راحت باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/140220" target="_blank">📅 11:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzFKYvH8wGDkXWFYe5WhxtwW4lKslZdaC4UcVSCWmXmKastGaezEovMEqSctH6bwADEszrrKaiIlSEI4WcleL5tyf9N5-XuG3g1EtM1QrlRtnHCaIfUIe3inWstLr1a0UsGhIgWnaal0I1oSMRD9Oh6NOWu4LIFBFq-7_vMnFP1R1TpfBhUCAWX29UnqA3JO4uTcbIOOWCFOuqtS0kPB54DAwf1ghPflxumucNUy6xFbwvncVAVs0ig6IQuA1dtV5criOMMJ3q3NskT4Q_8xMqpooM4Tl5rHLp1bkT7k2Sb7eao-DJXwyu9mKzFx1zVDM_xMj2802NFaoqkhOXwoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/140219" target="_blank">📅 10:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140218" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140217">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/140217" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
با بهبود وضعیت چمن، تمرینات پرسپولیس به زودی به ورزشگاه شهید کاظمی منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140215" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140214" target="_blank">📅 01:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140213" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇮🇷
محسن خلیلی خبر مذاکره مدیریت باشگاه تراکتور با اوستون اورونوف رو تکذیب کرد و اعلام کرد این بازیکن هییییچ آفری ندارد و در جمع شاگردان مهدی تارتار موندنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140212" target="_blank">📅 00:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbmmmenxINOrXQiPs-He84Ymrevk-gixrBsg-o3kLo2qclrM9YvLjD0AUEQvgsgXKhkUbooBXuFm0TIXM0MRZgN_9oevPx8NlO8XwqZG1Kf_zbcZQppYLA7T1kXignqCACFCV4zkkeGHRNISEvx3Z8zrVW-c_UOkUDH5KIXTJCXQFWHqeRnltKEnD5EIWUStKY9Yi5kJYL-teej7fhj1kiyQUE-3v-_nG6vPOVM2Horh7ZVWb6N9teGcP-vxAc-ohtdayhVdV8ixGKErFlYCUeQGx24gOdTohhFI5E0xuLG9cBf6DDySkl78lxbY7ltnozYzyPwkmlb8dgMuFvK6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140211" target="_blank">📅 00:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
🔻
🔻
توضیحات #تکمیلی در مورد پرونده اموال توقیفی باشگاه؛ از صندلی چرخ دار گرفته تا پرینتر و آب سردکن
🔻
🔻
🔻
در دوره علی اکبر طاهری شرکت امین سیمای کیش(۳۰۹۰) اسپانسر پرسپولیس میشه و به جز اون چصه حق اسپانسری که به هزار مکافات به پرسپولیس پرداخت می‌کنند با همکاری…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140210" target="_blank">📅 00:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140209" target="_blank">📅 23:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=HOwuvCHSub-ey_0piJmLqsKGnRacYQH8RRMqHc9DuPKRAqPMGeaWUYfzW3zmc0Z9ho-FvODSe6l4OTt8VpRdisL0APxcaQeoM1DZgJB8USiNTZ9hoBgnHL9f_5LJedtPLYUvYo15TVAAB3ywJIPwuthTHnUxR7StzL709xUfKvPARj5uCXBU_qAwkLsfRoiA6gbLWvCUW_SNWBv9VpwkuiyEsQOKmAC3zqxC2l3n2D0HNZmBwW4qV9xF1Xlri1qF-sChnxTlY0-uh2qcNvr0in5137z6FnvruFKRPHYH6BznEdAKRw73-yZK_XbZu6F_kf8ephxxAPwaqWS8RclnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=HOwuvCHSub-ey_0piJmLqsKGnRacYQH8RRMqHc9DuPKRAqPMGeaWUYfzW3zmc0Z9ho-FvODSe6l4OTt8VpRdisL0APxcaQeoM1DZgJB8USiNTZ9hoBgnHL9f_5LJedtPLYUvYo15TVAAB3ywJIPwuthTHnUxR7StzL709xUfKvPARj5uCXBU_qAwkLsfRoiA6gbLWvCUW_SNWBv9VpwkuiyEsQOKmAC3zqxC2l3n2D0HNZmBwW4qV9xF1Xlri1qF-sChnxTlY0-uh2qcNvr0in5137z6FnvruFKRPHYH6BznEdAKRw73-yZK_XbZu6F_kf8ephxxAPwaqWS8RclnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140208" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140205" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYTTaK_3yN-5XMUOTmr7o0_lYcbfHY6JsMHwlc_WMk2vhUYrplFrJQx-nrlYLjhAWPxrEKX7L-lyz12ZXAGyAk57MumZFGYNrT8OwiW5RhirM-yqGVyk6njcd8MXxPs_KDMTiMGiKgpYfmq8nSYgOY6lXaeJeAKCJmqLXrs5dBrlbY9vr3KPmrLvYTeHCXL0HFawd2otOHKY8-3aCVhJLxeAS8llBohFbgspi7cPTBolUkcoD4Lo6v5JLphNZ4V1Wj6Z_Pn2qjWgSaLcKVQsqnX3CLX76Gjo3qeCJAY-qkRLqaHR-DAO9LzObUINAfDER4g5TUFo1bZFMmG7mc2l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140204" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140203" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=v99WurgG1DGQtjyceX5xJcVDbrjHD0WLLZsdBGpzYUyJcBGKT6sZTCA62j4BVD9UeYSTvF4dG7PNwDTkrktgIFP8f-gs9LTvYvKniUleJPi58LCvL3SpycO6VktLSuiTP02TxZtq-7TqRfRpdcmIvBjxfTwJ1rBARb2PeK3P-wAJdUE1UquiqxuSumeVLI5NfmR5YlhIp911yB6f9NpC8HnJceNahM6wZSGHqcNCOnH6GivdelMh_yG9d6KRAiO7iJ_mhmnlwlhK_hAMsGDufdbAr3aNjySP_c2Kv4PLSAI8hzbNFheHm6UdCJcG-F2vohf8ApGLe15IqpMgPvsAnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=v99WurgG1DGQtjyceX5xJcVDbrjHD0WLLZsdBGpzYUyJcBGKT6sZTCA62j4BVD9UeYSTvF4dG7PNwDTkrktgIFP8f-gs9LTvYvKniUleJPi58LCvL3SpycO6VktLSuiTP02TxZtq-7TqRfRpdcmIvBjxfTwJ1rBARb2PeK3P-wAJdUE1UquiqxuSumeVLI5NfmR5YlhIp911yB6f9NpC8HnJceNahM6wZSGHqcNCOnH6GivdelMh_yG9d6KRAiO7iJ_mhmnlwlhK_hAMsGDufdbAr3aNjySP_c2Kv4PLSAI8hzbNFheHm6UdCJcG-F2vohf8ApGLe15IqpMgPvsAnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140202" target="_blank">📅 21:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140201" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
#فوری | ترامپ: هر اتفاقی ممکن است بیفتد
🔻
تصمیم بزرگی در پیش دارم؛ آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است
🔻
به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140200" target="_blank">📅 21:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYVSu3VSFhW0MnQSDDDEyOudmPDX5qtDP3jpf_4QjckSYY53RawZh8BrGEMzttBmTqCkG-4-dja7vhbGNanHyKY8ONyrkKlsHHfvSzq3hlwXLMlR8yF4yPAx_PXKYsYJHslEhI3zJ_vBJO7hzIKvjf89rSvCwUkY2bWaW8S_6-Bnr7W9AQWBBusJcIncu_MplVANHR9TB9pOJWamQMqD24v5ba1HIbdBFjDCORMf8g17ra6kuRQmsK4LAjmKVd4uHKBAy61t57obIGEDbwnUstX451nf1XkHmZG4maz1dodzm0oXfRP8Ud4EXrkd5xb5J2k6c3yJVi8_yxjPVJkQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
❌
❌
در اقدامی عجیب علیرضا اشرف مدیر رسانه‌ای پرسپولیس اشتباهی عکس لخت خودش و پسرشو فرستاد توچنل‌رسمی پرسپولیس و زود پاکش کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140199" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔄
🔄
علیرضا اشرف، مدیر رسانه‌ای پرسپولیس: خوشبختانه آسیب دیدگی ابوالفضل جلالی جدی نیست و با استراحت و ریکاوری مناسب، به بازی بعدی میرسه  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140198" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140197" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
پرسپولیس قصد داره قرارداد امیرحسین محمودی رو با بند فسخ ۱.۸ میلیون یورویی تمدید کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140196" target="_blank">📅 19:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
سازمان نظام وظیفه به علیرضا جهانبخش اعلام کرده که معافیت‌تحصیلی‌اش رو به‌پایان است و باید تا اواخر آذر ماه تکلیف خود را روشن کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140195" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIN6FhFVJ0J3aNcTfsjQ1OLNVnQzHHBsv2iCHuJrc1Hdqxqbccc95GAhvVgymJt4vY0j2m4X9QPF9vfbjCvhPDHUNsJq42a3uzsMJEJunJ4psfnAigej0mJ1EK9Kg4BCmoCQuF4RPhdhlVAkJPbs2kDn0hiQA-nlsxN9MJoDNX1-Eii4NZ9EmZDX_8ykyj8H55q43ni4RHTX6MeldjjjDHIsLKCbEUZ_dfdgl-txAw7t-KzQ9xL3T9QXyiGJ1xqlZVOMOKh1ow7QDO7wzP2si9YlSeESnI38hLQEBjWRi9mNJL_sF_ItdyCdyw6PIoNubt8oiN0ZzHportw_W_NvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیتی و نوریچ؛ شبِ امتحان برای سیتیزن‌ها، با یک حریف که چیزی برای از دست دادن ندارد.
[
منچسترسیتی
🔵
🆚
🟢
نوریچ‌سیتی
]
⚽️
سیتی با مالکیت و گردش سریع توپ، از همان ابتدا برای کنترل بازی جلو می‌کشد. نوریچ احتمالاً با دفاع فشرده و ضدحملات به دنبال ایجاد خطر خواهد بود. اختلاف کیفیت دو تیم به سود سیتی است، اما باز کردن خط دفاعی نوریچ چالش اصلی بازی خواهد بود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140194" target="_blank">📅 19:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140193" target="_blank">📅 17:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140192" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
مراقبت از پوریا شهرآبادی از دست ایجنت‌ها جزو اولویت‌های اصلی باشگاه در ادامه فصل باید باشه. پس از درخشش این بازیکن در بازی امروز و احتمالا ادامه تورنمنت آسیایی، اسم پوریا بیشتر سر زبون‌ها میفته و مدیریت رفتار و دقایق بازی کردن این ستاره جوان، جزو مهمترین…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140191" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140190" target="_blank">📅 16:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140189" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
شکایت پرسپولیس از آسانی رد شد
✅
با اعلام کمیته انضباطی، شکایت پرسپولیس از استقلال بابت حضور یاسر آسانی در داربی رد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140188" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140187" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140186" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140185" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140184" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
اورونوف به همراه برادرش که چند روزی کنارش بود، دیروز ایران رو ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140183" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140182" target="_blank">📅 11:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
✅
علی قلی زاده: من از ته قلبم پرسپولیسی هستم و دوست دارم برای این تیم بازی کنم
❌
❌
اینکه به جام ملت‌های آسیا برسم یا نه بستگی به شرایط ریکاوری زانو دارد/ حضور من در جام ملت‌های آسیا نشدنی نیست و باید منتظر باشم
❌
❌
فعلا فقط دو ماه از مصدومیتم گذشته.خدا را…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140181" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140180" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140179" target="_blank">📅 11:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140178" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBNu5Wc1EUJCM-8zZNUmCqBjTQWVFXzBqEMH4-TwSW1HbhyTgd8sFK_fBa5m1NU2J0AfHaOEJozeTfXxPljCd48_DnOoefzc-C7l2eCceIYtLEzOUhZLLAV03MZahRCsy9LyWOgcTFQWiMfyMyzKy7EoU1H2G-sDQQuEQS41jGZkXo8IiIHnwohiVSS57OZjqh-DKsJYj7f9RIMngYA4YgYFoO-awoIado5sQppT3JdfFLei9ns8uA17uRfz0BCbs1ckrbGrDyBhfh7ZCp4jP7vHMaLGvlMSeVchYltlAWEGjPpuH11rxPS41Bf2LQMLnZdqJQcRuM7Sfpb650QKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Juventus -
⚫️
Nijmegen
⏰
Tonight 22:30
🏟
Allianz Stadium
🟠
یوونتوس بعد از شکست پرگل مقابل ساسولو، در شروع اروپایی به دنبال بازگشت به مسیر برد است و فشار بیشتری روی خط حمله خواهد داشت. نایمخن با فوتبال تهاجمی و پرس مداوم وارد بازی می‌شود؛ بنابراین یووه در کنار مالکیت، باید مراقب فضاهای پشت خط میانی باشد. با توجه به شرایط دو تیم، انتظار می‌رود یوونتوس بازی را کنترل کند اما نایمخن می‌تواند در انتقال‌ها دردسرساز شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140177" target="_blank">📅 11:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140176" target="_blank">📅 09:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140175" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140174" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRU8PoCPPd8Z30NyyrS3_excCF2SBfBvaPIuDwTOeEgKKtUwb86YQkepjZ83Yv7Dux0MAQjSbELBrwjvij2Bi8j1dBdUB6WT9jh-pLitUxq0hfCYvRbPo5EQ9CV7nBJ8DMSpv_SHSYfVCN6jVBbr2HowR-tZlpAb0tJTQT0xEyQQYJZ39fPDdyazph7Zq2HWV0iVpTv3C0HQBOUX_nr-x3jQHuHeTnLMuMHwCeoiSKfBo1hw2jFJHnDXdZuQAyDjc7OuqKWq3gC5LVyHw-iI0Wl1u6W1WZCt4A9LUi1Kd1e8DeXzPHNK0ahpGAfgiPHm_CinDzyRCjtMlEkMrvP6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140173" target="_blank">📅 08:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_i7uO_4hPSmkSBHkFpPer8WeeHKrErG2W4P_MH_Woi60VRSBfXLTtuB5V8KyEDmiYOqOiSL-qZOwAicipk5AhJmQi-nWt5Ji_qgElT9fqB3iMwSnkWLh-cZtSzsQb9zwx_qvVKxsIl8sLyHzBqsXh0VnRAHloHxjstdAg_a8TlCfFDZgn3M6B7dFUwx1_gmkwytpwsgAeTMpoqo_SBAr9vJEsVpBswZHJZoUKCdKqvSkPyCdGS99De4YvsQ-1QuCvdAuPo23kzdvmEIroe6tPZPiPsMSOS2WkfDZod9784w1gxR5xakbjT6FLIhwBTNWdIhOXH360eqjyA5FXMoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140172" target="_blank">📅 08:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=MwGr8NYrR1dyOUnhTT-8W9jndyEzbNgG6uSnyVs_KPeeyqPOgZQph1IhKw5J0kqfnJeXsTCvkbRWUDoBjPUH_B_EgM-UvunY1Hr6vnG5d3ygi9O_B2oep6sJhRG3oqfNroYFWWPCCnjgFClsmBO6MT9BiFUxoeAuCvvhxhfRUd_P07x2i41IqG4ZAU4Q-KOxrMb2LIpAuz2syAWyVU68d5W9UnHkJ9o6vTMFUrG0QxS19cfKgiB_KzYBJLxPdinpWnJsDRKdNcOSPKN5Bb1IDihDwpngIU4Bl9JOT8bPFvl_rw-5F9gxHzEaKGH5bQV0BKgSPKe1GXTREU6RTfAUew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=MwGr8NYrR1dyOUnhTT-8W9jndyEzbNgG6uSnyVs_KPeeyqPOgZQph1IhKw5J0kqfnJeXsTCvkbRWUDoBjPUH_B_EgM-UvunY1Hr6vnG5d3ygi9O_B2oep6sJhRG3oqfNroYFWWPCCnjgFClsmBO6MT9BiFUxoeAuCvvhxhfRUd_P07x2i41IqG4ZAU4Q-KOxrMb2LIpAuz2syAWyVU68d5W9UnHkJ9o6vTMFUrG0QxS19cfKgiB_KzYBJLxPdinpWnJsDRKdNcOSPKN5Bb1IDihDwpngIU4Bl9JOT8bPFvl_rw-5F9gxHzEaKGH5bQV0BKgSPKe1GXTREU6RTfAUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140171" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140170" target="_blank">📅 22:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140169" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
مدیریت پرسپولیس در حال انجام کارهای تمدید قرارداد ۲ساله سید پیام نیازمند، است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140168" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140167" target="_blank">📅 22:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
👤
مدیرعامل فجر:
📍
انتقال علی بیرو به تیم ما قطعی شد
❌
چون پنجره نقل و انتقالاتی بستس تا نیم فصل باید بشینه سکو
😃
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/140166" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KERj7tAA3ZcXbmQF8duKA1yG1-afoRV7HZRNh1iqHwswnpE1iwe7tVqQ28yVcXYQzkidiyfyNhc3mCKXTn0kLHFR-g_tdtGzPz9M0ySbKHDscuNvhC0Ps8GOHPskkf32dskx-3qBjBCWxe_Y8XZmuJFpjiva1wD_rceEXe5WZqSmtLJpUSOqV-v3bWX3t9WMJ8TCp_RYrcxiTvtycv_Pwq9yxfl1dPvvjzriV21NJZt0TjxMlQUEaMXkVIX4kfLYSTps2FXj8iiMUCU3jUJcK-Bu0ete4kWfAjG04CwK0a_RHi702bIgeCOxDzP1SqrLwmxyyAJd-WB1e_5Y-PdSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/140165" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
❌
باشگاه پرسپولیس کارهای تمدید قرارداد ستارگان خود را آغاز کرده و امیدوار است بتواند آنها را حفظ کند/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140164" target="_blank">📅 20:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
مدیرعامل باشگاه فجر سپاسی؛ انتقال علیرضا بیرانوند دروازه‌بان تیم تراکتور به فجر سپاسی قطعی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140163" target="_blank">📅 20:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYgB7AVGKZjowuUXkmB3jDvUZc0_wuePbfpdCxFTBoRStFPD2vAdsun6vlL4rYnfdn_FdcL3WBrLp0YL44rMMBByjQD1sm3PEDuqKSE_aTTe5Bw_iYtRV9m4uSUGnChRpAWOa-24yY_qYTXsJCTEKkBlDSYAR232b-DEgl4XWK-hGhEhiFMAjfsef8qm_mq-NpjVI8b_CVcI22VpDht7XDoh0HUj8R6kZiljte9jUzz_MEOfIQ7PEsFhIWb4ILT8a1lz8FMzL9pdF1nXSmzMJTvfe8rd8IEjiBy0YDtbMxymVorfMtaj3Z3up-7EHAYw3iyt_5PSinweM0x213rVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سن‌سیرو امشب شاهد تقابل دو تیم بزرگ اروپایی است؛ میلان و بنفیکا در دیداری که می‌تواند از همان دقایق اول با فشار و درگیری زیادی دنبال شود.
[
🔴
AC Milan
Vs
🔴
Benfica
]
⚽️
میلان روی بازی در عرض و نفوذ از کناره‌ها حساب می‌کند و بنفیکا هم با جابه‌جایی سریع بازیکنانش می‌تواند فضاهایی میان خطوط پیدا کند. اگر پرتغالی‌ها بتوانند از پرس میلان عبور کنند، ضدحملاتشان می‌تواند جدی باشد؛ در طرف مقابل، حفظ توپ و صبر در ساخت حمله برای روسونری اهمیت زیادی خواهد داشت.
🟢
امشب چه کسی برنده این نبرد اروپایی خواهد بود؟
📌
میلان و بنفیکا را با وینکوبت دنبال کنید؛ همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140162" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140161" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
النصر هم به طور عجیبی سه گل خورده از العین ..خدا به داد کیسه برسه با این العین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140160" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140159" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140158" target="_blank">📅 18:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
رسانه های عراقی: بشار رسن دنبال اینه برگرده به پرسپولیس
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140156" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140155" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140154" target="_blank">📅 18:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140153" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
شنیده ها: تراکتور نیم‌ فصل برای جذب حسین ابرقویی وارد میشه!
✔️
✔️
گفته میشه تراکتوری‌ها ابرقویی رو زیر نظر دارن و احتمال اقدام برای جذبش در نیم‌فصل وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140152" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
حسین ابرقویی مدافع میانی29ساله پرسپولیس چند پیشنهاد لیگ برتری دریافت کرده و قصد داره توافقی از جمع شاگردان مهدی تارتار جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140151" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqd5uOd_iYe0dtN8IHo88iNsFNmDK5FnflMVcLJ_8HcH5UX_v1LFawz8XYtRaO5T-OSdhU9lb-pGLVZJzbF_PQuZ7NZcY31MWHUREx-xgrXq3guMHY0J_mg38fu21wm339xpsnPba3B5W30Ht0mHpjpuiXwdb93uc2weoYzpqyagyOZz-4ajGSEMSZaoMUktrA5EebGNaN736uVIln64jHKNl1H1XNlTWo-2ZNBdHRJAwTEDFxpwztrou_QmZaTFO5eNiKMELhuJ9gztXHO7t6aoA9Tjo07QMdb_5rY2T5gwyp-WdLJu-DIWfVLJ8E-ydh2sC06ChUwg1S7EsHO3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❤️
ایشون بعد از اردو ترکیه که مصدوم شد حتی تو یک تمرین تیم شرکت نکرده و حتی نمیدونیم مصدومیت‌ش دقیقا چی هست و داره چی کار می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140150" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkhghT7CLFLWDaubiTZQyuiRgYflBYv3G56YewrFF_8J7nduKi_c3sTlEfxdLI5r2wlNdS2H1M-RtCpqYiy8CxMy_R5pXj2O0P9FJCEwDxHpLw32yw8d83IxNY53VG84h4IyJ3m6qD5pxSxPpTA5C76JNUAUs9DWLyI-SFxjMExrABOem37suXcTtvnl8GK703k9AD3qOytNIJo51-z3IQbi4BrW7M42ELUN6kBHSq2FkoZWAQctfFtSA8Jfrukfu84UX2z2r9VLxihZnwDyZVObUbwsWm7Q-LmViBLKw8rCZGUbewo28srzq3ri4R3gS_BDRw9O4PRhwzD1fnBaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته میشود باشگاه پرسپولیس دیگر برنامه‌ای برای خرید امتیاز تیم لیگ یکی ندارد و به دنبال خرید تیم لیگ دویی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140149" target="_blank">📅 14:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140148" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7iN_WoU4Dgu4UUYsdoNqouEtxxtIvnvcpeyYwSb0_AyZtFMe2NYj7LFrxZWfewnzthtUjF4LDD5LobBXkEw1LsbvEqVAsf_m0yiLBMtNES2UmgJE6c8k0QVNSm-lUFLyIJynnrHzw87S_1TMuuPP4YHlxwKmtQGBOxpGA1HLL_lcfnrNvnaM30qGxEz-Ob52UtG5GM6Ot9nsVDDEStJr1JNhMZqZkMXC_OoT_WsWt6Ktkwo_DZiTat-Z11l4FO6xiMQJKUCm8dpCHwluUjfbKR-cQAvyEyah8hJC9R-SdtkPJ3GHJWDYX4ewP5vuiLkT0LNWaxfIhAMeZXrJHk4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6mOwQXTbGwBVOGKN_ckB3fVZSHnpiGvglHgda6C1h03GR5ChNrqWzLYPPG3Fkds_6-XKw5aYRpOtZIQL9Du9fJbYZ5zwa-4VVgzkxpVXLeYczISX2r6qltIFY0lWzdmShIsvV3zfnfq4sp8tJ-bwnvhlA2A7mpqE8VB7N-juM_No68pkA7ZweNo8oi8ZvhK8NVyrxEj3L4vrmN3EHh89gcJJXgXTbncIJXl3_9FWABG8fIs6VNZSG-FO2pbOO2G23Jq0wj7uBJNX2NJ8_HsZbE5RRhZY-gQITeIQpNSAK8iqmSfnlqAtUD4bt2Rlrl8CXNZ1odYkvATDxrgwvcdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrG2MlgR1gGfqoVXNS8Ca9woW6msigvbc4rV23TXwl4kfwB4Xy2gDna5nwutaQNBB_nx1s4qKj7PqXsNLUyeMQH88KjoA0N-ZcEIGSWybBc0tfDiRf-WxkO0H351ieup1sTXEasku_wDzJmGGKZzGgZp1jic9TTLbKWynXPjtd7Y9WBuH5G4fxWkh4bCQR6xDuDXU5KsKXAUUCXCINAzujxxwhvO3nqhAjlM9vHE2NZyt6h-2NDKHRNH8nwjZTOYaPonpTdisOVxl9iXLRNg2twu6NuBdeZ8RgSh_CfnYBjmri0K5AqWQNK1WzweUAi3TdLnnn6b33xZOLLSDkHeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=HgiweWzhf5PgkEvvypZ3PD_X9nXWYUj0PotWJ8j56RshEyxwFUZbuGvGC4DdqS_tCnpcceMQP1h39ohZXQ9r9zWLy24fqQ_vc6krY1a2xs1GHJhERxE9d2ks97S5m_IUd5CSlTM4HaWT0zprdngIUw9FMPYDlTvArNvo-jNTngCMPFWPj_ZaMoCgARSlN7i31gTQ56Fk8jEaqFNtvi18LtU1ZM-sZ-lt9o5pqAoG9iLjyuX2zCK3cphN1xaxprWWiis3_W7ciXmSO2t4u-saHohh-ViXiqtKlFYdn7xnjxUvDjaBuNogkmxz_abl0qNB_JsXcsO2kvv2GNl7tCMNog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=HgiweWzhf5PgkEvvypZ3PD_X9nXWYUj0PotWJ8j56RshEyxwFUZbuGvGC4DdqS_tCnpcceMQP1h39ohZXQ9r9zWLy24fqQ_vc6krY1a2xs1GHJhERxE9d2ks97S5m_IUd5CSlTM4HaWT0zprdngIUw9FMPYDlTvArNvo-jNTngCMPFWPj_ZaMoCgARSlN7i31gTQ56Fk8jEaqFNtvi18LtU1ZM-sZ-lt9o5pqAoG9iLjyuX2zCK3cphN1xaxprWWiis3_W7ciXmSO2t4u-saHohh-ViXiqtKlFYdn7xnjxUvDjaBuNogkmxz_abl0qNB_JsXcsO2kvv2GNl7tCMNog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=RGHO70xi93tMIritq4cSbrq8yxoLclLKzM7a56nW5I6H47xDBLrSNvLyJcsSyAOJ164KzzmHPdVTvfpiszv3AtH9GvIlxa4R8reKJGz3hiw38IjFEqZlQw03ajjsDPupWfPilnv1WK32n6VgIW5jtxufZ6ix4cFq8SrQJXvCivC1Qtp_hftMTW_d6932uonBSkBBm5uQSfTd0N6REy-IrFaz4sQpJkaHoy4SG1VoDGoBivcv_zciwSqL4L4YpHZfp-wtVM4NlBEAAXjnZTTOKNqY2Yk9tUY9miqULLAsHI7g4XIzRTvtplTuV7kVDhcsqKJUnPVvqdQ0Z2T6-yhSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=RGHO70xi93tMIritq4cSbrq8yxoLclLKzM7a56nW5I6H47xDBLrSNvLyJcsSyAOJ164KzzmHPdVTvfpiszv3AtH9GvIlxa4R8reKJGz3hiw38IjFEqZlQw03ajjsDPupWfPilnv1WK32n6VgIW5jtxufZ6ix4cFq8SrQJXvCivC1Qtp_hftMTW_d6932uonBSkBBm5uQSfTd0N6REy-IrFaz4sQpJkaHoy4SG1VoDGoBivcv_zciwSqL4L4YpHZfp-wtVM4NlBEAAXjnZTTOKNqY2Yk9tUY9miqULLAsHI7g4XIzRTvtplTuV7kVDhcsqKJUnPVvqdQ0Z2T6-yhSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5mI_4My72PNvNJKU5UrcGVBP_jXhJYgfHNgd8KYW9IJ_79ET2pZv12ONdOB7O0Z03dt_mUBjdjLD07oUdMB5JKxksgmCfY-WURmkc82OQyvAKIJNYphXsx43n1H7dI-6kF880qcJSMHRImvRTQfCNzgD2B0U6_zCzpXSzPiw5EhXxMqQ7wMD5QcpGFDST8thK7Ohu0-Wsc9t2VJIvfhIUq_EZKk7EJg5rTj-a3Gkx0wadbPOibDXvta5Iu5s3482FlYaqDWLgS6lFxkjyKm6iIhrbkrQ9rASjEbXBXVKsCy0aHBz9PaKJBwPpVNhdo-LhPkmfP4LdpSxbmNdi3WEwCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5mI_4My72PNvNJKU5UrcGVBP_jXhJYgfHNgd8KYW9IJ_79ET2pZv12ONdOB7O0Z03dt_mUBjdjLD07oUdMB5JKxksgmCfY-WURmkc82OQyvAKIJNYphXsx43n1H7dI-6kF880qcJSMHRImvRTQfCNzgD2B0U6_zCzpXSzPiw5EhXxMqQ7wMD5QcpGFDST8thK7Ohu0-Wsc9t2VJIvfhIUq_EZKk7EJg5rTj-a3Gkx0wadbPOibDXvta5Iu5s3482FlYaqDWLgS6lFxkjyKm6iIhrbkrQ9rASjEbXBXVKsCy0aHBz9PaKJBwPpVNhdo-LhPkmfP4LdpSxbmNdi3WEwCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxIA29nZV87LsbcJe5bds6T_f5RjPhdl1WOzMA01P7w5wgs_OTEiEdAvbz3yabG9gW8vYMtJ3A_htaqCnIoDSHE4x_TVXx09AKCApkXqHOx36QD1Ihca4wVVmzcsZ-6Gi9PVC4aE3cb2wsr-XHVEbr9cuyJpxzfUdDodJtWmCdH7Kv_LpDkOeWP5FTO9TGsZW4GnN8HNL0hGO64wL_opHT2f0IWowljYw0Ajcj_euh8k9rqRcxv-dthtmbopLDbFTR4vG9sBx6pMoyOqWInkwvzicAUssfJA4PWpn3g62e2cxb3dQm_3gKgxKhBIito5H98p42LlJx-nDeU7Fbj02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At8qW6IbtDWmVWm7-N6_FSZv8SRQTQCDzcdSRhh_rdIztUAFWBEXBFWR2Lqh0X2q8k1fVjmw5SVB4RBmiT0A8OwURrgAO-rgvqcGTG8APFaDDVJOxS0SDlaWe6-BVhSxYh8m5MnPFqUGYJiCfLdLqsZaTmjVOl7ZA7qDwK5TLHNhEo0UF5jUK8SUtSD2ThqSWv7Ql-Nykf2ONy-jR0kPv6UWmxYg7Qeb08IMFFLnZH-bhZLfbVKNIAVxKS9EICY82AWc9dzOGU1S1TK-ot37uBPmeU_R9_q78m7gp-c2SKYKwh0X8_UCWxkW_jh9gyKSmTlxGpCjfgKl5nVar8o_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gn9pp2EwZmCRTu-TPtCI1aRQc08Gos9Q_7jnsfuJxlQLAGpN_V99EwSEO55Cx3LgAEu938ygT6sLa0QZ2CLnxP-OPYoKmk1xBkbCDvjIKLZ1-wDJ1mqSMRgDrdvMOUyZGhewKP60QsWEFk-S9RoaGHzHnsMECRiFEsGIvRJo84wEZbPuj7rQwxCZYDRkjoE1iHyR3pSkEhmWu3SXG6TbemTbSXMBs9xmk_MMR5T8tNJr755jDkZQl96FM-ePLA54KoXhzLuwNradkrQYlYu0g23_AiV2o3naOS5k8ie6uEMVA59onOh74SZLEvZR-Cm6GxE2JavDVbZWF2iKJf-7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB76paUKZhCyXod8mT_MZyt_ElPcrDqNLbILKPPsqfLv3lYiCN1GYF_v7i1s498lqt7e9qJEEnsZraNyMff6F-U92UX53wO2bbt__3aLEUy1HYxeXz9FLpNG_4mWRdjLBVx5dt8JAvnyKNzK1bwNuT1tR-b7i7kiXdzQXgx2IRXbfLq60fcHUUHhBxU40PNGD52O4hM45071f5DxNkTHaB2TQBfdE7a1mIeqGjPjysFj7M0voq3nNlOdisPk7Z7zOVeTGxGM68HVxqjxp4hJBXDucwd92uxVuDn9gRRPwQgHrHLh6vWvMfwJ_JQ71DwFqW5DMXqf6i22tT4gygDWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
