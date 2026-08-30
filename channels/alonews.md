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
<img src="https://cdn4.telesco.pe/file/aZ4WC0Qd41_uZPlFkFonY_ELRs-Y_U9phNYSuq540lw7Lif9W1Z1d-PYp0CaJloPua3dHUJYtPXUWXwglAYquHqVcwuZ6PO9CVAyRil0URHo3cvic4r47myzvvgW7Hq6fNICz65mhZlAJMaaeAUTgUqH0w8uVoItedvOBoWQXj5mzLEpresAAoDgXrcY7MxOOLuwD1iinXBQItHyBvIG1TPhJ9ZEhqPt42E7QiOqA8JFAj2CuUURnRFiltO73PcDR6-JHN0YzjOalZakghnDI6AVFtT-vqvZriziRjVjgiHHnusQVplTNDhAepBnMoENthBEW21iVVuROIyzJ_7iIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-144634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فووووری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/alonews/144634" target="_blank">📅 00:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فووووری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/144633" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/144632" target="_blank">📅 00:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/144631" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/فرودگاه مهرآباد تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/144630" target="_blank">📅 00:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
✅
️فوووووووووووووووووووری/گزارشات از پرواز تعداد زیادی جنگنده اسرائیلی
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/144629" target="_blank">📅 00:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوووووری/حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/144628" target="_blank">📅 00:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/144627" target="_blank">📅 00:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144626" target="_blank">📅 00:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18d748662.mp4?token=el6lWuHxPsHH25ybU7yG1cg14HkYL6wWF42t84gd_mgADkldwd2a_Se0bUSOzFcl4H9eA2JvNTnMu9uevH6edB0eHzDydtpxdeqpia868xVRhVGEDeo3yUp0GLwCuYKeoHGoQy0_IuxMXofVShZQju7CpJbHdWQ6zC5T5jhNwv3bzMjkAktboDDlWpp7mDuenCyOgV8qXzvW3fLvz-X4cOQqDaTVxGVtWAUy-46Ijdrnz3v5OWWeAQ0Cvsgj1cB3B1Wdm3T46DggA2d1UcD6Wg-MbqNPIcNsOoqsFMtuZerADjq6R-K8NlXnUxmDHR2zFQ-pn-9iifYyHHTjE-bhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18d748662.mp4?token=el6lWuHxPsHH25ybU7yG1cg14HkYL6wWF42t84gd_mgADkldwd2a_Se0bUSOzFcl4H9eA2JvNTnMu9uevH6edB0eHzDydtpxdeqpia868xVRhVGEDeo3yUp0GLwCuYKeoHGoQy0_IuxMXofVShZQju7CpJbHdWQ6zC5T5jhNwv3bzMjkAktboDDlWpp7mDuenCyOgV8qXzvW3fLvz-X4cOQqDaTVxGVtWAUy-46Ijdrnz3v5OWWeAQ0Cvsgj1cB3B1Wdm3T46DggA2d1UcD6Wg-MbqNPIcNsOoqsFMtuZerADjq6R-K8NlXnUxmDHR2zFQ-pn-9iifYyHHTjE-bhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره اسرائیل: این، کشور ملی مردم یهود است.
🔴
سایر افراد نیز حقوقی دارند، اما در درجه اول، این کشور ملی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144625" target="_blank">📅 00:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر فعالیت سامانه‌های پدافند هوایی در برخی مناطق منتشر شده است
🔴
تایید یا رد نمیشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144624" target="_blank">📅 00:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزارت کشور بحرین اعلام کرد که یک قایق ماهیگیری بحرینی در خلیج فارس مورد اصابت گلوله قرار گرفته است. در این حادثه، قایق و محتویات آن به دست افراد ناشناس ضبط شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144623" target="_blank">📅 00:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaabb12e7.mp4?token=fvPtdjKbR35-ZkjavKERkKNJ_WzqNVgbI95jXbugKU21rloAtlAvFBk9SgOLYjEv9NhzBhK-wV-jHZtSSO46wseEO0UzcNGFbtb4eD4r8eWJCwmA3Cd4sirml1gLLhjPvORnWnQgfyOU4S2waHUk28B-QxnuOvXBZEmrH3nxR9iLOP7z6zT8EBZ1gYbeuwK4GRACamw9CTF2uXn-BQc3zWI1fWF3-n9cIft0lQ5RWfz_M2XBrpQPqySWf-RQ6qWANl0lGRXIOZFldfs8scu-5CYCfSU2Fty7PZ95uMzExozPAJa20uEa_J0ZUhs7s1jTB7lheWZiLgY-54bzibLrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaabb12e7.mp4?token=fvPtdjKbR35-ZkjavKERkKNJ_WzqNVgbI95jXbugKU21rloAtlAvFBk9SgOLYjEv9NhzBhK-wV-jHZtSSO46wseEO0UzcNGFbtb4eD4r8eWJCwmA3Cd4sirml1gLLhjPvORnWnQgfyOU4S2waHUk28B-QxnuOvXBZEmrH3nxR9iLOP7z6zT8EBZ1gYbeuwK4GRACamw9CTF2uXn-BQc3zWI1fWF3-n9cIft0lQ5RWfz_M2XBrpQPqySWf-RQ6qWANl0lGRXIOZFldfs8scu-5CYCfSU2Fty7PZ95uMzExozPAJa20uEa_J0ZUhs7s1jTB7lheWZiLgY-54bzibLrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری کانال 14 عبری
:
اگر حماس سلاح‌ها را پس ندهد، آیا نیروهای دفاعی اسرائیل (IDF) شهر غزه را تصرف کرده و حماس را از آنجا سرکوب خواهند کرد؟
🔴
نتانیاهو: اگر لازم باشد، این اتفاق خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/144622" target="_blank">📅 00:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSZ8beNGRjisK2WOPqSsaE-0gCEpaZk9rKn3JXagC2_WtveC-xz09D4NyWs0KvL7xwxGl8wsCYZv74-XkWHx6pw3wxLCUFyPLZXzOogHe03j_8xOcMmeeW2_xf9IeAHEF6wjXtRg6qNCirgL3O8H8xAPLIbFvIOk6W0cXIiQiQ-vPSkk98lP-dL32B35R8x6GoKxQ2txMXIwPcS3vscTqRE3BGebz6ipnNlalGUp5MjoPyN5Ecy8B5E_Ra_udF0LwNZbQfOeOUhNRkDCkoyH1Cc8tVC3xSBg0jYM6jLZ7wb6Xzya7BCcp9ZNJSlAQauQ5I9Hs_QlNIOMO1QazFCc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل حمله امشب آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/144621" target="_blank">📅 00:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2pXCTlQL-Z4I2i1MQ2PANSfWkwTjD83x7dLQDjWoQyo_lGTXAQjR60HOQLET3ph8G7DLUSpzkQNIKsxMffDGfq548KEbhbzJ3EBPjmER7ycweHYJzAhurtQYLye0_z2rEYT0fkheU2v8d8b683Di_X3D4DnuNNKDIqTvLeLIHMPbl0XixxVSJ1kRpCrp7OPA4K5Amf43X1OsrjAvM46rbOvmw9ayb1XVykPYbjG9ODj7kH1myG0ScRr_L8ucq_QdtDeVZr3tw9GDHiM3rPrFRoeo6JSV7P1-NFy2Y0Ds0WDAit5HYZqba0QTGpJs3TCDI19YNgqivBUuNA55aui-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سپاه: دشمن در هر دو عرصه اقتصادی و نظامی، تبعات این محاسبه غلط را خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/144620" target="_blank">📅 00:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / صدای انفجار مجدد در لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/144619" target="_blank">📅 00:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حملات متعدد اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/144618" target="_blank">📅 23:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf9vRmTWLO0pWchPGdsR02y3tM_VmSSMQqxPsiYR6JcWOLCv8BTvn5E8MbDMPPNXVop5cw8Y8_5PGUfZUm9m-p7ks3_ML1cnQJ01ZIfUluRusXG0dMYAWLsHJ1VAuwceXo0j-qUw6JOYWIYgx7CcG8C2pXIBjFz4dwfDUkrWB1koqjbgALO_WW2XTYzUjtIUr79L6qlu2UfmxzQOt4PJEMMLPEWnSco1SEO1xKApVrQdKXz_-7jc12jmyy4avsyfDrviOKsqbmCi5_myF3ndce1sWq91Datb3Dpa7U3olfMf1bZrZggEzMIOrcEhBEZnnohVc58QRlaXt_LztE1qQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قهلکی: پیام عاصم منیر به تهران چندان دوستانه نبوده است و خواستار انعطاف تهران شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/144617" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PYl0Auv6p9DXbAbBNjTlVmzuxkbiKBPwj6KVCJQ0ExKWC6wQn6pywbM2Ql3155RQ2ykvc6KrF5edZzmkdfUROv1guMNqodzcEK4w2eF-WV4BqSB3SYlNcXCRFVclxLt79AlcSqc459krC3a9IvWE4KpdzuG4tRPVLzBV7oC8953xaxnh0dXU_m5icnw6olf8opjttHY1r8Vy9RUV4BnRBB0qk2x8Yn2tPHL2m0azlvfkeMBixdOC4ixS53bDGlrEz4MKdP0GCILCm6CWDo4XeACR742_XRdrY5G1uVlitUSMXlBrjvl9q8042O9w2YeRGCZczODsOMuM8NDF0QOz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان ایران و منطقه هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/144616" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/144615" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/144614" target="_blank">📅 23:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گزارش افت شدید سرعت اینترنت، در سراسر کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/144613" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سپاه : تنبیهشون میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/144612" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / آکسیوس: ایران در حال آماده‌سازی برای پرتاب راکت‌های حامل مین‌های دریایی به داخل تنگه هرمز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/144611" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIv41WYNDVVPDBfXTj63G94xzmoBr_sjJXb_hYhTvWwahc9zb8rYhKhhQJdLk3fX5cP_XzGuw1CwQ4uP0YnFv4ic_-hBlBBanlIV2QPyEyHbK3c-aE4yBhggalyTEZuXT2RdFw_Ngk_ITf3dJolqHKhh_yZFlsGTZTBQsYqd6Uljf6fsWv0Qk2Xw5oES6laRWdheyU8HzsArXcWg-B3b0AiGReIl7vaEkE4DMhb2gYEqVVyK7ToAXr87rwXwN6EHcgG6YEi9-Fma1VKQqtKjtS2hSZmhY7ATmt2FSidVAF2R1u_otML1Z0-EdOdKRnS7MpEMjq-1xn1uOekzfWFmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: رژیم ترامپ اشتباه بزرگی مرتکب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/144610" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه : بر اثر اصابت موشک به مقر نیروی دریایی سپاه در جزیره لارک هرمزگان دو نفر کشته و دو تن زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/144609" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144608" target="_blank">📅 23:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آکسیوس: ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/144607" target="_blank">📅 23:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBHOpdG8S0hgV_67MlYUk4DJxEfoG2ClvggeyOVM9iOmNWqIeTt9FjCjkOLK8snESVvkag1Ub-N-JLFk4JKeJV1VyOLeCpdC-Ofxq6rhtpHm_gRdICYo0R71NufndqXeib54JdD3hPylBAYg5cZoVF3pfRM2lwj8oK4FvMFaoZO860n4HPYIpwuxkY80GwtnCgxq0XSHrQE6GhM6WoVF778tXnJy223nrpnd7rku0-BDOAeUE_V8X2nFDPiGi25RH5NpdzwhuWd55EgVPLWHEv7ECS-m_xoivBdO294FgkUuU7sDr2t-RkUaE_oPieUCuJCM_LCursZt3b8WuomXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPTbqXA3Aoxy1V-G_cgxL0SAxQ7LgWa6xrvgX1vMxZC5w1LbwhtYnURBQxu1HqZu0GKUxdzYuUzGoYxGq93KoUEBkbbdLc3EEST_LGgAMmCuO5G-WC3wWkz4pju0seiX8nAfYYKruWjJJ2Q5p8f67raEMyavxaag1eWGuhR03nAKGkaNiUTdPSIulKHhWC8R-E4wf3YgvF3CC3ePjRvV8X1_ILigpmzS0YrNcRZMuTybUkL2CRc7fNHpFPW9yx4xkoUoAySM1pSoSQY3zPxJ-le4-Nimnb_cMHbgvOqJSUgkiYLOCkpKLwXtg32Uo7zG9M0TCdygwLx9KxfpUPSqpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند نفتکشی که ایران روز گذشته هنگام عبور از تنگه هرمز هدف قرار داد، در نزدیکی جزیره اُم‌الغنم در سلطنت عمان متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144605" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/144604" target="_blank">📅 22:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/144603" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو: ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144602" target="_blank">📅 22:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx2nYeGgvmiAgVsyfs3SdNso65pxsOdd0x7RcGPljjE1s8cIyNMxC1HVEjgeD3gsDp_nhcc7PPyg3vWGnVzHrrbMiIgkSnZX4kAjhZzOw-3CnkfzL2OElOPV0eORmX8ssbsNXWRoCJYu-kgS2p-sMEFolil1ac5-6szvDbtnwck1Du2_MIFujRhAG_1EftP665W6JhLk7FEV7ovEfxK1QlLiQ5lTYQbInULrG7eeRzUcS-_Q6yInh-ZqYtrkd0d3PdESA4LRMiiVqiTswARtwX8fK1kLz5J5Bm2iDMvZ7WmmZaaou_qZLge6x3mCgQPFpJemwIerdDkGwgQcDzI1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
از تمام شرکت‌های کانادایی که با آمریکا تجارت می‌کنند، بخواهید فوراً به ایالات متحده نقل مکان کنند.
🔴
بسیاری از این شرکت‌ها سال‌ها پیش به دلیل رهبری احمقانه در ایالات متحده، از این کشور خارج شدند.
🔴
هنگامی که به اینجا بازگردید، هیچ تعرفه‌ای وجود نخواهد داشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/144601" target="_blank">📅 22:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1ZpCFykGajW796AKFXsgBZyoGrzio6jn-2jVs7BTROpBCiCJgRkhH76zp5QsfIfWMaVmc2RSV4Ku8ChZIScFJ702wxdz4b8tRFD6Rc13aOiTBK1_EfMOSRRwqS0iPpzPlAwwgcIhyLviWoT3bklxgii7qoGzerPIEZYaQ1clgYQJ-wZwmt_mB17KMJZfST_RNhqTcRrbgRNgmMjrhRroqpyXqpkzlwlXFHwQXloekBkWR-rtIr4zLrzShJLHSzezDTD86HhC4eXWTdGwZ3D8lUdAJ_aXw3N8RQnJgFcL54p3leMmWSZDqP4EHSGGpAOMcHTSLhrUqhn_qCdmbypOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه حرفای پزشکیان به صداسیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/144600" target="_blank">📅 22:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
لبنان: از روابط حسنه با ایران استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/144599" target="_blank">📅 22:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZX6PcP4fB5NZjJ9wJ4csv9_69ZNE3R2UPXG_bPDriB5tWnNKxM6BuNqCweWRavI8EITvrz0eYjq6RWYhxdBZYKEwAL2NaImxjYpJGVHnlT8fb301yz_ybbdS0p9nA-XCDAzfQoFYLYkL9BE72a-HGlzEv_7gSshqu9jXcmiznfV7MC2ZpXG77KzAzEDBDEPkUiXlp24BHYTMn-4LNwdqoCxtqUTlnmMJJr_6KFmDrxnvbMljcob8iXzWP5B4BaIY9bd9t1wwFHNmjCMbFgl1_q-ZJmadEgGFuhzYHbCDq5u6uV5V1J6ehnKC5C8w5rDc7Y8DJLRQ2wbM_wMOeWI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی ارتش اسرائیل دقایقی پیش به منطقه المانصوری در جنوب لبنان انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/144598" target="_blank">📅 22:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر دفاع کره جنوبی هم برکنار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/144597" target="_blank">📅 22:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdb68de81.mp4?token=Y5YIadfwnCOfdTe0Is6WII9Za-9n15bf7yEtefSfwbYIWW68C6dnFnVeIAiIcIrMdTo9IndRaZ6nADBMzvboMewGQdaWltriQCCjQYfHMFuZoFyS4_jYslFfFAxX3oPY5xDGTUKHTIvHOkqegCLnB6g4JB_0_cAwGke6sBMqHbx2_hJW8xJHJsOBLKXOIwWXL33coFAQp9A0Wnr2HArdIZupezUiEGIss-9hmW5RELdHB1eDuzgmYad2qJqQWiIbaUQzjdXgC7H-jAhP_1cGqSJkM0n0FCuzm2aHim1Du8pMVaPiCuhxSPlyPbP_NC0AylFTChQhEJaa9uBlJ7NTbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdb68de81.mp4?token=Y5YIadfwnCOfdTe0Is6WII9Za-9n15bf7yEtefSfwbYIWW68C6dnFnVeIAiIcIrMdTo9IndRaZ6nADBMzvboMewGQdaWltriQCCjQYfHMFuZoFyS4_jYslFfFAxX3oPY5xDGTUKHTIvHOkqegCLnB6g4JB_0_cAwGke6sBMqHbx2_hJW8xJHJsOBLKXOIwWXL33coFAQp9A0Wnr2HArdIZupezUiEGIss-9hmW5RELdHB1eDuzgmYad2qJqQWiIbaUQzjdXgC7H-jAhP_1cGqSJkM0n0FCuzm2aHim1Du8pMVaPiCuhxSPlyPbP_NC0AylFTChQhEJaa9uBlJ7NTbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فدریک مرس، صدراعظم آلمان، درباره
جمهوری اسلامی : شما نمی‌توانید قیمت ۱۰۰ دلاری نفت را در آلمان با یارانه جبران کنید.
🔴
سیاست باید صادقانه به اندازه کافی باشد تا این موضوع را به جمعیت بگوید. ما نمی‌توانیم این کار را انجام دهیم.
🔴
اما کاری که می‌توانیم انجام دهیم، برای مثال، این است که تمام تلاش خود را — به همراه شرکای اروپایی‌مان — به کار بگیریم تا به پایان جنگ در ایران کمک کنیم و اطمینان حاصل کنیم که تنگه هرمز دوباره باز شود.
🔴
این همان چیزی است که ما به آن می‌پردازیم. و باز شدن تنگه هرمز به این معنا خواهد بود که فوراً شاهد کاهش قیمت‌ها در بازارهای انرژی، از جمله در اینجا در آلمان، خواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/144596" target="_blank">📅 21:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تد کروز سناتور آمریکایی: تعیین حکومت ایران وظیفه ما نیست، اما حکومت آن نباید ضدآمریکایی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/144595" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه کان اسرائیل: اخیرا کشتی‌های جنگی ترکیه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و مسیر دریایی آنها را مشخص کردند.
🔴
نیروی دریایی اسرائیل برای مقابله با هرگونه تحول در دریای مدیترانه، سطح هشدار خود را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144594" target="_blank">📅 21:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سازمان تجارت انگلیس: یک نفتکش هنگام حرکت به سمت خلیج فارس از طریق تنگه هرمز، مورد اصابت پرتابه ناشناس قرار گرفت.
🔴
هیچ گزارشی در مورد تلفات انسانی یا خسارات زیست‌محیطی در حمله به این نفتکش‌ در تنگه هرمز وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144593" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مقام ارشد ناتو: فعلاً تهدید فوری برای حمله به اعضای ائتلاف وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/144592" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مولوی عبدالحمید: تو تهران باید یه مسجد برای سنی ها ساخته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/144591" target="_blank">📅 21:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به بزرگترین مانع جمهوری خواهان در انتخابات نوامبر تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/144590" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933caa4553.mp4?token=M_1BGQKQ33TRtIoTaItPGWWI077k0EJO8OdV0aAWX__1kSLYKnldcA-uRCVWJnvyxF4HdVS7WV3HPCDL8D_drgCtbl62ksssRWK483x42uLymqQmu5381fqA06GNxqXe--YspXayX7Rm-YWXCfAma2mKI4PWqNCw06EvV8n1eFovMhaxZe-XFbro4xsNCz0xNALM41evFApMRGZop6Tzl1A1CLqDibopsBrLFRVWbzvM4RlcMZI8P2zNeyRjaY6MfTEUetiFm5EBzte9Xtw8rT-Sqz6f70Vfmr2GPMxSO6CprnJNWxYByx6LazAB-qDcYPLUOo3gpA4f6zvSt9pxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933caa4553.mp4?token=M_1BGQKQ33TRtIoTaItPGWWI077k0EJO8OdV0aAWX__1kSLYKnldcA-uRCVWJnvyxF4HdVS7WV3HPCDL8D_drgCtbl62ksssRWK483x42uLymqQmu5381fqA06GNxqXe--YspXayX7Rm-YWXCfAma2mKI4PWqNCw06EvV8n1eFovMhaxZe-XFbro4xsNCz0xNALM41evFApMRGZop6Tzl1A1CLqDibopsBrLFRVWbzvM4RlcMZI8P2zNeyRjaY6MfTEUetiFm5EBzte9Xtw8rT-Sqz6f70Vfmr2GPMxSO6CprnJNWxYByx6LazAB-qDcYPLUOo3gpA4f6zvSt9pxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور تد کروز: آنچه من همواره خواستار آن بوده‌ام این است که ترامپ و دولت ترامپ به معترضان سلاح بدهند، بنابراین مردم ایران، کردها را تسلیح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
🔴
نه پاهای نظامیان آمریکایی در خاک، بلکه مردم ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/144589" target="_blank">📅 20:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3bddb2342.mp4?token=XEyvQaEr8_oXXBFn9Zkx9chSnK3g4_fbM-Rz0YEztUtTEsJ2CTLLi8Q5ZmWX_pFgMhPaE7eZq8n15aVvExML8UJVsIpJxc2uwSuAs5BtdEZpSXuZaHznHORI57Gqfwn4qDH9T4s-CkwSQcCpFgHFa3pOZrKDPPqjBZDPZe6oQFQ11GXAacDF051xWiqxrATF7frDdDxOlOOwlDCP2ekcEIrEZoL4-ymeVkH3Y2O7rSrrzZSwLD_y2l-Kd5P-nD5TLJ2wK0FUkO6Fnk6Cr7XgtPQTsY2IaitX0fPk5Cgy6k5_P08vWwxs5QvMWIiEuEB0tvicZKgTGJw-Do8TGIsurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3bddb2342.mp4?token=XEyvQaEr8_oXXBFn9Zkx9chSnK3g4_fbM-Rz0YEztUtTEsJ2CTLLi8Q5ZmWX_pFgMhPaE7eZq8n15aVvExML8UJVsIpJxc2uwSuAs5BtdEZpSXuZaHznHORI57Gqfwn4qDH9T4s-CkwSQcCpFgHFa3pOZrKDPPqjBZDPZe6oQFQ11GXAacDF051xWiqxrATF7frDdDxOlOOwlDCP2ekcEIrEZoL4-ymeVkH3Y2O7rSrrzZSwLD_y2l-Kd5P-nD5TLJ2wK0FUkO6Fnk6Cr7XgtPQTsY2IaitX0fPk5Cgy6k5_P08vWwxs5QvMWIiEuEB0tvicZKgTGJw-Do8TGIsurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود طوفان سهمگین به مرز پرویزخان شهرستان قصرشیرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144588" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اویل پرایس: جنگ با تهران طی ۶ ماه اخیر حدود ۳۳۰ میلیارد دلار هزینه اضافی به واردات انرژی جهان تحمیل کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/144587" target="_blank">📅 20:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e859f8d1.mp4?token=r-FSf7d0mpAMBtSyWf8tzDrLWslrKMx07Lv2N9cXfOQP3NkuAUoLAGGp3N5VL5iw5LORUkRn57KQxTQ2Mgk01v1vlqWOJDGU9rBvdKSSVfLp4uVxNNlNhgRNaLq8w0OYRrATeDjKIfhhCPen--I-Hn7oSgnClbzhf8o5DR1Lh83I705_nPImqilGLssQtnQdU68cmYgsZO1NySHEzeVEs1vSLwE4xItVM0qhY4Sjz8UCldAQDVa1NAmxubEOSmqrzxFp6ACvEob2tIks2H8oqAHo2rHcPjVNs0DKAuy69FK9AepPux07ZQRlYdXrq9q2PU9pHx52TY6p12o1C4V_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e859f8d1.mp4?token=r-FSf7d0mpAMBtSyWf8tzDrLWslrKMx07Lv2N9cXfOQP3NkuAUoLAGGp3N5VL5iw5LORUkRn57KQxTQ2Mgk01v1vlqWOJDGU9rBvdKSSVfLp4uVxNNlNhgRNaLq8w0OYRrATeDjKIfhhCPen--I-Hn7oSgnClbzhf8o5DR1Lh83I705_nPImqilGLssQtnQdU68cmYgsZO1NySHEzeVEs1vSLwE4xItVM0qhY4Sjz8UCldAQDVa1NAmxubEOSmqrzxFp6ACvEob2tIks2H8oqAHo2rHcPjVNs0DKAuy69FK9AepPux07ZQRlYdXrq9q2PU9pHx52TY6p12o1C4V_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما: این خانم ایرانی که طعمه جزیره اپستین شده بود، نجات یافت و الان در تجمعات شبانه شرکت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/144586" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پزشکیان: هرکی بتونه مشکلات کشور رو حل کنه، دستشو می‌بوسم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/144585" target="_blank">📅 20:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی صنعت آب کشور: میانگین بارندگی کشور به حد نرمال رسیده است با این‌وجود یک سوم کشور و به‌ویژه تهران دچار کم‌آبی است و به مدیریت مصرف آب نیاز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144584" target="_blank">📅 20:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
حمله سپاه به یک کشتی تانکر در حال عبور از تنگه هرمز در مسیر ورودی، در فاصله حدود ۱۲ مایل دریایی شمال خصب، عمان.
🔴
هیچ خسارت جانی یا اثر زیست‌محیطی فعلا گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144583" target="_blank">📅 20:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل، الی کوهن:اگر جمهوری اسلامی اشتباه کند و بخواهد برنامه هسته‌ای یا برنامه موشک بالستیک خود را احیا کند، حتی اگر توافق‌نامه‌ای با ایالات متحده وجود داشته باشد، ما برای حمله آنجا خواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/144582" target="_blank">📅 20:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVrdA52YsaUlAZT_SGswQ4YIEdzUCbMSnl6rZYkpUUXBnpwtxr_jcKS3LgqFnv1JMq8TSB0jhf93ZKSzflVxhUPErpaLSDjWoNUHxBnCugf4vaAiE09sa0pjU8MdIW8Z8mhmWEdoR2Ue1Nb0KUTw6eMKmSRMDCwrCyFBxi_G_Vo7GlQQq9GKkVae79EhKYN9oReyMNrHDj1hDQHa6dRLelzC7oUFhn62XqlRGC7PGQ3idoe3Ibp4qaGZ11o7qsSBIKghm6rVk-YhAQ_uAgoI1rTeWx5ibBhNzwk6SzgdMySE5TJUVjplaQTMSR2NmqCvlgOvUW7VPTW8LkSuLbe2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله سپاه به یک کشتی تانکر در حال عبور از تنگه هرمز در مسیر ورودی، در فاصله حدود ۱۲ مایل دریایی شمال خصب، عمان.
🔴
هیچ خسارت جانی یا اثر زیست‌محیطی فعلا گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/144581" target="_blank">📅 20:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144580">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf4b9bcea.mp4?token=LEwmKEaeEDhOFAkHslfrSvB7f8iCIOO1iwXI9pAo8Kt92gGJ9YR96wFlbb0p5IkmSGB6F6XoAZxOj3NRkyBkk4yxT9rfd-QqkUuwnoSoj5QKfVTeJ-6s7jL09qBzJtEMCSI1inNOyzJYFi8zNzHmJE4vHScSYWFSFkAaupLlVW22KOIu_67wsAe03NyuyKP5b8yW2oNAdySyfYpfbJ9k1iBK-7Zxv9ZHARDhta6ghD7c8YVlZJEFUMT3KKjnwaKkuUzSpgQFdee5jE6pyaY3kvWndyYuLPTz33K7harshN4myUvlwv7wN9JZLlJ0pxd6Hgu5od2R5WvSAgGqQCS9fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf4b9bcea.mp4?token=LEwmKEaeEDhOFAkHslfrSvB7f8iCIOO1iwXI9pAo8Kt92gGJ9YR96wFlbb0p5IkmSGB6F6XoAZxOj3NRkyBkk4yxT9rfd-QqkUuwnoSoj5QKfVTeJ-6s7jL09qBzJtEMCSI1inNOyzJYFi8zNzHmJE4vHScSYWFSFkAaupLlVW22KOIu_67wsAe03NyuyKP5b8yW2oNAdySyfYpfbJ9k1iBK-7Zxv9ZHARDhta6ghD7c8YVlZJEFUMT3KKjnwaKkuUzSpgQFdee5jE6pyaY3kvWndyYuLPTz33K7harshN4myUvlwv7wN9JZLlJ0pxd6Hgu5od2R5WvSAgGqQCS9fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل حملاتی هوایی را در جنوب لبنان انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/144580" target="_blank">📅 19:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144579">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گاردین: دولت ترامپ مخفیانه اطلاعات روزنامه‌نگاران را جمع‌آوری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144579" target="_blank">📅 19:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کرملین: نشست پوتین-ترامپ-زلنسکی ممکن است تنها برای رسمی‌سازی توافق‌ها برگزار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144578" target="_blank">📅 19:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کان نیوز: یگان های ارتش اسرائیل در حال پیشروی برای کنترل ارتفاعات علی الطاهر و تصرف مرکز فرماندهی اصلی حزب الله در جنوب لبنان که بزرگ ترین سایت زیرزمینی موشکی حزب الله در آن قرار دارد، است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144577" target="_blank">📅 19:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehxvyTyl9W1r8GQQs62_lWizNBOor17WhxxC2jsRrH-mpJ1TK7Qhi8QR-Rok0701RUNT1d0Y6LBIMuLdoV_msgaqm01xUQyRFYBzr2GMhjDl3fhl8WvwFMzWTePPHHGjkYWMts0kUPxD0nYB_kUJ4V2uS4B-ZRpXQVRIMRMnvFQg6BryBKy-IRzljo90RbgKb5ja4Fa4LI1lm1RurBviQVz1uDcvAHzzyUqoAXj6nsYMeWsz5LFn6dcuF1GzS0MQydJQHtf8qDKt_OQlZ59A2kxSYsrV28Dmi7k7uLWfmfcf6g_LjjtUx6qaM8q3p0yMtCRCiBukLmlPfck-l8CroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بستنی مگنوم پسته‌ای ۴۵۰ هزار تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144576" target="_blank">📅 19:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpY5oI67GByhdniDReCeZvB3fjT5tnBUrZtaSD-Qb8EvIAh1ZD1W-QE8Sv6Fc_hhteav_elCTo6QOFm__q0-TnTzZgzHCIZ4f5sWFhmxwQwd0TKut0Nzeu3AQEsRtTBsTxuT-Bs-CBcHljDxvP4aIKhx8X1sJLsFYUSyNe1-KjJ7C6HojOSzNpr76ALr0BaPzhyIed7mlXq-EcE17l2v3j8Uz4o-tuE8NfNuNxWrXHk-Q1pIavAkJogcHegU5bHIudyDh9NulmmLB12Pm-JrUEf0_a8puGIDqEUb1-L6YRNY85O4wA6uZuIkOoJ3QGpKSj8pfpbYCuP57GWaR3wVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای آمریکایی «CMV-22B Osprey» مستقر در ناو هواپیمابر، کد اضطراری ۷۷۰۰ را بر فراز خلیج عدن ارسال کرده و در حال حرکت به سمت صلاله در سلطنت عمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144575" target="_blank">📅 19:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3bddb2342.mp4?token=IaIRQYpfY9_upmOjKRobzYTDVCqHmssFQw3ZUtnKw40j6mnAl6SHwgqnBY4UlXQQM1FhSZ42sqCth-VN2d0G_aZyQEYy6KR9ksXaUJTSl1Hv9ngDCynR95hTBnCSCrGCU8mCCkX0GTSRx3Vbg8ckgdMVhaea-u86aUAPaFK53q70dQ3z2V9a7rbBAUYu0B0l_SkrT6hHNtXk0Af6Wk8UnWsF_7PvgEUE8iY-cpay8M8Qyh04MlwOodpAX98J77x2AJeEoK81Af-Sa59sNSqKz5jji8F4OlNTAZG4x_ya7EBm5jYpsMywAlrQG2NiwK9RtbscZbJuuoZig06qKWBAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3bddb2342.mp4?token=IaIRQYpfY9_upmOjKRobzYTDVCqHmssFQw3ZUtnKw40j6mnAl6SHwgqnBY4UlXQQM1FhSZ42sqCth-VN2d0G_aZyQEYy6KR9ksXaUJTSl1Hv9ngDCynR95hTBnCSCrGCU8mCCkX0GTSRx3Vbg8ckgdMVhaea-u86aUAPaFK53q70dQ3z2V9a7rbBAUYu0B0l_SkrT6hHNtXk0Af6Wk8UnWsF_7PvgEUE8iY-cpay8M8Qyh04MlwOodpAX98J77x2AJeEoK81Af-Sa59sNSqKz5jji8F4OlNTAZG4x_ya7EBm5jYpsMywAlrQG2NiwK9RtbscZbJuuoZig06qKWBAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
لحظه ورود طوفان سهمگین به مرز پرویزخان شهرستان قصرشیرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144574" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAq0Dy6bdH-FoeVchZF5TiLUr-4IuypJiFVnGS-wo0r0YywNS53TLDXX47tu0EUYCI2L5Ck49_2dYL4gwAZZ7MhIFgkPd-Y_7jyUQLqMrPaoDH8wneZT_fJtbakx_wlG3aO6zQXUl2M7YB_HfoxVL8MhwKmJRPJZNRp7yD-xButfqMl0a9-Y4AmlmDNCCVWk_csxnQbELkONZ_WdyTdh5RgkPF_IshA87e89dP-_A-1ftiQjV_FBipwGqHj2wVq13GQK7mt2DQ8xV466SIzlaIvwgdJZ9vEIcWwKzv18IDLZklYWmBpD3OITzLDjAm_gzCVzsrp4-X27J1uSglLmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلی استیشن 5 با قیمت 255میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144573" target="_blank">📅 18:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=a4BdU6FkGp13JQGSDT_TuA_athYUSOuKE3d3PmGTbZ--Bq3wBKpO1Sw0IK06JjpWMkbsnWBC9IhwIvJoSEsEPqkT_lymfpATLvbKcZXjcUXhjOJhuHG755kUembRqc5Ah_Icw743ytH9N54av1GHBosgWrC1wOiTUkX75xwov0sqvpJx1yqfi-ddiFY9NYMKt9yoIiRMztXEVRz-hWtCeyq9wDxp9N3T46dzWtQ759MiebjtPOr9zRg-ZqGekFjtwGAvttvgS_cHKKBLFn0zWU_m1zF_YIkN4XmvIH8qd3n38Ql_GW0B7I80oBZGGQ8aGUYNsT0v7EZ3-G_wopbj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=a4BdU6FkGp13JQGSDT_TuA_athYUSOuKE3d3PmGTbZ--Bq3wBKpO1Sw0IK06JjpWMkbsnWBC9IhwIvJoSEsEPqkT_lymfpATLvbKcZXjcUXhjOJhuHG755kUembRqc5Ah_Icw743ytH9N54av1GHBosgWrC1wOiTUkX75xwov0sqvpJx1yqfi-ddiFY9NYMKt9yoIiRMztXEVRz-hWtCeyq9wDxp9N3T46dzWtQ759MiebjtPOr9zRg-ZqGekFjtwGAvttvgS_cHKKBLFn0zWU_m1zF_YIkN4XmvIH8qd3n38Ql_GW0B7I80oBZGGQ8aGUYNsT0v7EZ3-G_wopbj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع ایتایی:
بنزین تو اسرائیل لیتری ۴۰۰هزار(۲دلار) تومان شد
🔴
پ.ن: حداقل حقوق تو اسرائیل ماهانه 2160دلار هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144572" target="_blank">📅 18:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9618383d5f.mp4?token=p0gZmoX6mZDy0VLm4kpKWSLLzJ0rsFq91FSdrdx5NvKgTemtCFNycQzCGt3ExAjdDB3TUWlAQWJ9AjmMWr_OGMOmb_H55EY7vDFWkwmNgWAwGldtPHNaN1o3n9_QRuG6_8aVBDGOf30hTPH2cwGZY4zk2tJc6F1uqr37DE7V7xcu0he_88pJFPBms0sHqMpzDc-CU4iqLPDNSquUyb0O2kSxN1fATSOsI1geaqBFWyePSPO54bAl_MPm1P9-Z_whsohJgoJzeKD0Zk5yrhQX--l1iA-PXUJ9iCF2BRne0GDwKTVyRxB-cmN4bTavZBKu-3Q0OOsLVsi0a7tWVmvYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9618383d5f.mp4?token=p0gZmoX6mZDy0VLm4kpKWSLLzJ0rsFq91FSdrdx5NvKgTemtCFNycQzCGt3ExAjdDB3TUWlAQWJ9AjmMWr_OGMOmb_H55EY7vDFWkwmNgWAwGldtPHNaN1o3n9_QRuG6_8aVBDGOf30hTPH2cwGZY4zk2tJc6F1uqr37DE7V7xcu0he_88pJFPBms0sHqMpzDc-CU4iqLPDNSquUyb0O2kSxN1fATSOsI1geaqBFWyePSPO54bAl_MPm1P9-Z_whsohJgoJzeKD0Zk5yrhQX--l1iA-PXUJ9iCF2BRne0GDwKTVyRxB-cmN4bTavZBKu-3Q0OOsLVsi0a7tWVmvYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر از NBC: من می‌شنوم که شما می‌گید اهداف نظامی آمریکا در ایران محقق شده. اگه واقعاً اینطوره، پس چرا نیروها نمی‌تونن برگردن خونه؟
🔴
سناتور تد کروز: عملیات‌های رزمیِ فعال تا حد زیادی متوقف شده. البته بعضی درگیری‌های پراکنده هنوز وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/144571" target="_blank">📅 18:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgWiBzBXzLHzOr49pkhbrK4RrDI9sqFbKucvrRdwoaM8RWHqquhZswP1peDUj0LlsJ6FqoRcryslvpcQtzLkvBXO99NvE3Re8GpJUrwVrDiUQCLtxx3CLBGGQrDFvqPlzWSGZesdC56e_bUeoOB3OyH471jBQChb39yDOdBKJcM02vTA-k9QIwy3KxVx6m7t31trZZqFeDb7zGd42qzfQQ2ZaTUrHZaAKciTJALxeARp1ETRpGY3hfAu2YJ8T6MpRP5Wal_fHD7i0bvFRNaMBZakQJg4Sc2dcYkgAFH0sB5ZyfCOsqAEqMFsq5HsgQaqQZADh2xKkuj_EAZZMo6EfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
یکی از اقداماتی که قرار است با نفت ونزوئلا انجام دهم، پر کردن ذخایر ملی استراتژیک است که به دلیل عملکرد آقای جو بایدن، تقریباً خالی شده است.
🔴
فرآیند "پر کردن کامل" این ذخایر به زودی آغاز خواهد شد و یک هدیه از سوی ونزوئلا به مردم ایالات متحده است. متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/144570" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef540669d.mp4?token=YD_Jlco5_8_818P0I3gB60HxEOCf3r90DDRVo1FXPTbbywZPRbqszFRcbrIMOtADEwKaKzTUXMW5OWEN4AQ6dW4xBpEpVWSmUlPGxXyMUVOYXd3TkVK0g2bnIEMdbEvpTX1b6i2OW25AI7703YLWxb0uXW0fJw_kx0IfCmKLo6cn3_LOJ1SOjod8THnt37X-lZUveKMOloDKZVhke9OGBb9lnwdEn_vK1DqMVs8GtE7T3HwksLSRvwq07gKR79NfloI90f_lml5TbVV_Z4bR9_-HFamWAfrtoajEASMQX8g_B1YE-fr6ntvL7nt3zSnlZXPE91sFdvsEFSwZhpFOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef540669d.mp4?token=YD_Jlco5_8_818P0I3gB60HxEOCf3r90DDRVo1FXPTbbywZPRbqszFRcbrIMOtADEwKaKzTUXMW5OWEN4AQ6dW4xBpEpVWSmUlPGxXyMUVOYXd3TkVK0g2bnIEMdbEvpTX1b6i2OW25AI7703YLWxb0uXW0fJw_kx0IfCmKLo6cn3_LOJ1SOjod8THnt37X-lZUveKMOloDKZVhke9OGBb9lnwdEn_vK1DqMVs8GtE7T3HwksLSRvwq07gKR79NfloI90f_lml5TbVV_Z4bR9_-HFamWAfrtoajEASMQX8g_B1YE-fr6ntvL7nt3zSnlZXPE91sFdvsEFSwZhpFOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی پخش زنده صداوسیما دارن آموزش رقصیدن برگزار میکنن و میگن برای تقویت ترقوه خیلی خوبه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144569" target="_blank">📅 17:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز:
آمادگی نظامی آمریکا کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/144568" target="_blank">📅 17:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است در نشست G۲۰ کشورهای عضو را به کاهش روابط اقتصادی با ایران و همراهی بیشتر با تحریم‌های واشنگتن ترغیب کند.
🔴
یک مقام خزانه‌داری آمریکا گفته هدف واشنگتن، ایجاد «هماهنگی میان همه اعضای G۲۰» در کارزار اقتصادی علیه ایران است.
🔴
نشست دوشنبه و سه‌شنبه G۲۰ در آمریکا، علاوه بر ایران، تعرفه‌های ترامپ، جنگ تجاری و افزایش قیمت انرژی را نیز بررسی خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/144567" target="_blank">📅 17:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5932ec682b.mp4?token=Ovf4VilP8ZN7oczWyh97g_-N9T3AMj9IRR0wSDSapgh-GV8XL6z8nbE7unc9qTMkxRJKV7vuBzPNVSK4tKkydRiytAAgJvUEXHg8ClA05v5Jbjbu7fA0W5tL_6MXSTMhyloqb0jeGjNvHxVEZtbEiIzERDmolAPV0cTKEsiy5DBddt4JIRYXKKA_bpOpWy6vg_iHulxv5ICKj53xqLk6O_nGw8rjlPKAxUB4BMdAr7k4K_FgleEiEX4aSYnDGgV-hgqZDVtbnd_Ca5OrBDGFkuG1x_rSsIeD82g717YtS2AD-Y59BAkqnOaE_KG7nzh-9c3GVPCDGmEBNsoR9YvMFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5932ec682b.mp4?token=Ovf4VilP8ZN7oczWyh97g_-N9T3AMj9IRR0wSDSapgh-GV8XL6z8nbE7unc9qTMkxRJKV7vuBzPNVSK4tKkydRiytAAgJvUEXHg8ClA05v5Jbjbu7fA0W5tL_6MXSTMhyloqb0jeGjNvHxVEZtbEiIzERDmolAPV0cTKEsiy5DBddt4JIRYXKKA_bpOpWy6vg_iHulxv5ICKj53xqLk6O_nGw8rjlPKAxUB4BMdAr7k4K_FgleEiEX4aSYnDGgV-hgqZDVtbnd_Ca5OrBDGFkuG1x_rSsIeD82g717YtS2AD-Y59BAkqnOaE_KG7nzh-9c3GVPCDGmEBNsoR9YvMFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر آیات قرآن کریم توسط محسن نامجو که اخیرا به تهران آمده و بخاطر حمایت از حکومت، یک حکم الهی بخشیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/144566" target="_blank">📅 17:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc5bd3dad.mp4?token=SMuhUFvMF3_0KmOQNJAVflDtkDTxi1fSJqYCV2ZQvlVTDcrU7spuPQzWZ79Mzf3U3UvUNil149FmHXgqg7my1UnZx8UOBHaKCFpIeHH9IMA_BFx4f3hE7xUHI7hS2vseJr-tGWd5yzgVIyWCXxeSSo63fMGck2bGy9O_CJQ29KtbUioYMBKBLhPD67vbnoC5cALVHUIR0Usf46PtYMCK2majtNDkzoSjKJRHOa8Wq0scBNdzf49RSswumPrtLNrrSTCVf2Ly_yw-XgmIcXlm300PRXqpQ4Lb4UodLKO2O5ea944vGDILNzGqKjEKnRrweie28r7eMA5B46AcqZ-uCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc5bd3dad.mp4?token=SMuhUFvMF3_0KmOQNJAVflDtkDTxi1fSJqYCV2ZQvlVTDcrU7spuPQzWZ79Mzf3U3UvUNil149FmHXgqg7my1UnZx8UOBHaKCFpIeHH9IMA_BFx4f3hE7xUHI7hS2vseJr-tGWd5yzgVIyWCXxeSSo63fMGck2bGy9O_CJQ29KtbUioYMBKBLhPD67vbnoC5cALVHUIR0Usf46PtYMCK2majtNDkzoSjKJRHOa8Wq0scBNdzf49RSswumPrtLNrrSTCVf2Ly_yw-XgmIcXlm300PRXqpQ4Lb4UodLKO2O5ea944vGDILNzGqKjEKnRrweie28r7eMA5B46AcqZ-uCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک FPV روسها تلاش کرد یک میل ۱۷ اوکراینی را سرنگون کند که دعای مادر خلبان اوکراینی به فریادش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/144565" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O82rAEWWulu40xhz_fCqbMGLk-2TB7EZjTxP8r5cADk0cs1OzkuHA74X5zifNsMLP-ep93VZ2jfOywzut3NpD7o4voZY3XmmTKXQ2OoeRi5AuU7Fo-Zs_L0FYGryINQdOLAYBTGEg7eKKiRhaXjbmQEQRIx5v_vYXCKGGHhKE_9iIAi9m4DN39Jzn9hCpQSXtjJpsyqQWNfg0U5dgVlCPxEOfhwvnNwJPrAjhX0v1FmbPjHN58ZIg94f0UcMg4T_abklanNaGPyBC2pruhgJnxRZdpc7aZyLHFvzDQ8gv2SF-ORWU2r6uRmnq1WJfLyO4Q0fK-ouoo9C2bdrHA0jqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLOoDBG81jfUJ4O3fSNlLoMBmbwcQWZ9ZaAVv4IORVDebmpDISj9EOKAsFuIVeB7NqYNTT_-CGAmomwaQFcPkM3KuQ7bRD9TjfeIjERKxsd6CTsbCsKoYqlSMJ0pEYhaxdxTz9yahZUolB2IB80u2lpuSaNYn6jf4KGGNbL9iBjSYG4xvbqZ_gZYsKOFrw7jd-YA5tm60mCfO3RIsHVcvoEZ2AqOB27MDwCxrPZv9D8vmVprI5Widn6dhzBJ5Dw4ZdaG6giLtDVPxkUbCa9XgIQi_A2Fychwz18h3Kys27RF_omjKceR1vm5hSPRJqw4t5JAxfpd-S2u6Ix0CIWW-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی که از نیکولاس مادورو در زندان منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/144563" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144562">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: آمادگی نظامی آمریکا کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/144562" target="_blank">📅 16:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=T7zfvYd8TZpXdosq8_mVFFy9wKqYnrxplzRj2Q7XbekO6zyPnbwDqPg5kofF6rHl4OG29_cXH0XTT1h9N8rJp_UcB0E-A7TsLTaeXTc8tqDrOcfHUb5jFYdLQliRZ55MIzwVGqd68xUOVhfP9mbK2-Ap7bcwxLTzd2eTqdIu6x2rLKKaBz15KtmWCmwRJH_BR34JDFG9iBjshK6HIM_I7iqd7BsfqRaswUPnkGvVEYMpTTXYUd3ACTNdTiymYeFdZNdp_uoZy9ZSRBSbVxJ55mpVpg6M2G_cwgotLuP59pznlr9ahieUW8eZOJDqPyNey7xHq0iLARwGrLOVQcWUCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=T7zfvYd8TZpXdosq8_mVFFy9wKqYnrxplzRj2Q7XbekO6zyPnbwDqPg5kofF6rHl4OG29_cXH0XTT1h9N8rJp_UcB0E-A7TsLTaeXTc8tqDrOcfHUb5jFYdLQliRZ55MIzwVGqd68xUOVhfP9mbK2-Ap7bcwxLTzd2eTqdIu6x2rLKKaBz15KtmWCmwRJH_BR34JDFG9iBjshK6HIM_I7iqd7BsfqRaswUPnkGvVEYMpTTXYUd3ACTNdTiymYeFdZNdp_uoZy9ZSRBSbVxJ55mpVpg6M2G_cwgotLuP59pznlr9ahieUW8eZOJDqPyNey7xHq0iLARwGrLOVQcWUCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیمت دلار در بازار آزاد به ۲۰۸هزار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/144561" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9bNpfqjPefzajMX_vqMw74lkshPFlZeKI1UFoXFLa4aVaG43ADaPcVYGsBEMuy2tcA8CXj_N7JymEyGa_St0pIQTqgO1X8Q-c7BGtdwsNTgVBakL0J8kb1nmsgDWd0IA4Z5UUBPjWowRReD-AaL9nIim_RtbD6_dsaj39wDCV4jnVrcQZOxiLjVoSzkm3N0oICQ-C7xEjzcSlNkv0H6J3nkYYgZuhKvD6BOoslOypBnvjzHlo3SurTDSQsQdxlrdFx5zGqxsLs0DJ9o2zMgRxh4EgX6JxWsEOc1pXoq7YqVZhsEkW3l5fWiRmWZjhDxJU0LrGYE64W59srKuUogxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت چیپس دل مزه در سایت باسلام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/144560" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfre-a_5swanI3AOptWPo-7x4gsY2ES0TSoQ9fb15ZR6q7AC4QW-gAedYnjBogtwAGfP2UQfn6dpvvNRVCbzGcZbGw2uD8i6GEy-pUqw-eiJPRsmlM-OsqUhM-UPSdfB7skJDGOdbve5kr0mBEE5OGkWi6njv7rDxcGzGXRlUz1IEvTT6M2wJASg8v3LjWzA9CdcZ0oo6GUqBBmANxGloBESPurikO9XhP1FvWm0B8x4WXzB1Jdf3bctTO7114euzSU2EYxPImnRCZ8IUyLm3536dWY-pbEoozmnVsT6hmiToHiyRFigRGik5ocIWAA0FHnIzJhxXYHtrAH7IHvN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «نظرسنجی‌های جعلی که رسانه‌های فاسد ما از آن‌ها استفاده می‌کنند، از کنترل خارج شده‌اند و باید کاری در این‌باره انجام شود.
🔴
کمیسیون ارتباطات فدرال (FCC) باید وارد عمل شود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/144559" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CckZWi35SH37Ul19X_WE2wgB0j8hKHZYp3AW2pa0-CYUU4VVQF1DCf8oyRNc954vzQPz5NBWfXVwoGa-OEdC-TG_Otq3QxHkIlKps9pOvBHX9Q_GWlj4cRFHcTmb6Jtr2uiFk4hzbggzvwawestlecCUm9yfqQW0QXNj0Y9RCpElaTpvgBT_Ryu0o8-wb9ht9lHJZBjViv5ERp2frb6n05EeHb3wDjdIoUVzUIQdp9UrEPoK47nWUxQNQ3KhIhifKSgYujqAdq-DLFNxPl9Lr7TlnXMk3HUn-H6iH02VC0I2YaxytzDvGIxex6ZujCVKqM6bZ48Pii5L1Rer7Tvb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CckZWi35SH37Ul19X_WE2wgB0j8hKHZYp3AW2pa0-CYUU4VVQF1DCf8oyRNc954vzQPz5NBWfXVwoGa-OEdC-TG_Otq3QxHkIlKps9pOvBHX9Q_GWlj4cRFHcTmb6Jtr2uiFk4hzbggzvwawestlecCUm9yfqQW0QXNj0Y9RCpElaTpvgBT_Ryu0o8-wb9ht9lHJZBjViv5ERp2frb6n05EeHb3wDjdIoUVzUIQdp9UrEPoK47nWUxQNQ3KhIhifKSgYujqAdq-DLFNxPl9Lr7TlnXMk3HUn-H6iH02VC0I2YaxytzDvGIxex6ZujCVKqM6bZ48Pii5L1Rer7Tvb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تجمعات شبانه یه خانم با شلوار جذب رو بردن پشت تریبون و میگه فکر میکنیم شعب ابی طالبه و محاصره تحمل میکنیم
😌
🔴
اما خبری از تحریک امت معکوس نبود چون حرفای این زنه باهاشون همسو هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144557" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بمباران شدید جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144556" target="_blank">📅 16:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhXQSfTvwtDMdV9kRrkNKAhxN3vfVMy5-O7kA83VPQU3ms28OJawBJ3qt4zTWu--zgYaroQlmkysetzvanHrRwmjgRVkGHj-suPI0DqewRWkGmTWB6Zzml7O10-pWKvyYge7tFrRr0WCl00dmGWTuxqsd69CKRBbVuaV2HV_cjRV90GaU7WwR4WtKKVjmEm90fOlNRJwC1saehUdHnzaY0l0wuNm51d6GZ_5jZA2lk3H7IYefLVMsQ5UePJMizFiZ294nEvzMrB2mHf3IyVnbEEPi8yLXOUkIR_FZ4OBbkXyiup5BQtaycL3oAARBEzvTWNoRzDC6IIz4bxsvm5hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار جباری:
آقای شهید از من ۳۰۰هزار دستی قرض کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/144555" target="_blank">📅 16:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بهرام یوسفی فعال اقتصادی نزدیک به دولت:
بنظر میرسد مذاکرات پشت پرده در همان گام های اول به یک بن بست دیگر رسیده است!
🔴
ترامپ به میانجی گران اعلام کرده است محاصره تا تسلیم کامل تهران ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/144554" target="_blank">📅 16:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDO9fcpTgNLCS9R3ce1898Coo6klxRyFvSyCgZqO5oAzyKNzfbhxGo8LjHZKhCjNA8h8y2x8Tk_ZFt3EeP-Hw_HoSaA4l9D_tdeSj6rxQpU-fR52PjwL1-1BOH6lhitvC4A7y4zZ0T4_RjGQH_PKRo_BGIYHDDzU-NMLubMf_lx5fBOw5v0tWaUnU7cIDrmJ5V4usUkCUCVlUxYbEnQhx0W6rlTwYqoTk4e4qrIFhtScfDcuKoJ1O_6urZ6m_zoJLf8XFG4tzmf7TQ6-cr9_RJlY1iUT0y-NEOyQBOH8fQP0Uoz2rQR1h5fjh1UhyR6bPOTgQ_NhiQKZNkL_F00kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پستی را بازنشر کرد: توافق تاریخی نفتی ترامپ با ونزوئلا، معادلات انرژی جهان را تغییر می‌دهد و هشداری جدی برای اوپک و کانادا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/144553" target="_blank">📅 16:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
واشنگتن پست: هشدار محرمانه پنتاگون درباره ادامه جنگ با ایران؛ ادامه عملیات گسترده، خطر تضعیف توانمندی‌های نظامی آمریکا در دیگر نقاط جهان را به همراه دارد
🔴
فرماندهان با تصمیم تمدید مأموریت‌های خود در منطقه مخالفت کرده‌اند
🔴
صحبت فرماندهان درباره خطرات، موضوعی معمول است، اما این بار چشم‌انداز «وخیم‌تر» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144552" target="_blank">📅 16:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIM8gbjTvMNm6eLWnzyqZLvMPunYTel3wF2Yd3PpdQfNqPqc4ifmHQF4UiC0vdqg5It8h8PBOjNkJM8-F_p1drDBCuTIQjNyR6RDkOKotFzAuTHCYGHXPPRvJ9yr6r99wcVKOqkC4wFsWPVWLICnIlHcZ3vr-G8fTQRQP6ZFkCqIt_CHIw2I9CXt8wONl6sxS17_2OuzBfjSjoOp34V-6FglHrtbU6qIgw0ZhoBelV_Pl7tlTMqreLRuBVvFnTxddCXC2Se9YaiJmnQEhGVlkG8zPeBgNku_cL_atuIcDssNskxODcHIwCL1sA0qdGQN3t6bxjooalbkyef177JAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میزان محبوبیت مکرون به 21 درصد سقوط کرد
🔴
بر اساس نظرسنجی «سی‌اس‌ای»، 79 درصد از فرانسوی‌ها از عملکرد او در دوران ریاست‌جمهوری‌ ناراضی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/144551" target="_blank">📅 16:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e105fffe5.mp4?token=kq6yPVkWZ_zIxDNVwZ2KopiMg8CQbvthgrVCWVyEnBLo6go1DJ3B2xsm_VzAHjozJy_T7RWfaIipi7FKekeH2HJReofixs5MZKA2AVXTRNEdkOE98zVcZhXCFVW7YWnNcw8E2o0gaDXARLg4DGTdmKJnz_1yS9FyvjsFlPPSf2O_O8wCwEwx7M1LcxTbicJzcqGUNdUtp90aJVL5NYwxubfnKBq7rDsvWIJoXpJyxwKoF39LbcMQLuBXT-PIgP4q9WYWbdwAGGue85Sm9aAl9_q9aoMrd0ni85RxMwLTlXhWAO0-iG2oGnvSV7Oke3IIxVw3v316PnswcyEhDIAenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e105fffe5.mp4?token=kq6yPVkWZ_zIxDNVwZ2KopiMg8CQbvthgrVCWVyEnBLo6go1DJ3B2xsm_VzAHjozJy_T7RWfaIipi7FKekeH2HJReofixs5MZKA2AVXTRNEdkOE98zVcZhXCFVW7YWnNcw8E2o0gaDXARLg4DGTdmKJnz_1yS9FyvjsFlPPSf2O_O8wCwEwx7M1LcxTbicJzcqGUNdUtp90aJVL5NYwxubfnKBq7rDsvWIJoXpJyxwKoF39LbcMQLuBXT-PIgP4q9WYWbdwAGGue85Sm9aAl9_q9aoMrd0ni85RxMwLTlXhWAO0-iG2oGnvSV7Oke3IIxVw3v316PnswcyEhDIAenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای سبک که توسط خلبانی ناشناس به سرقت رفته بود، در مسیر پرواز به سوی نیروگاه هسته‌ای «پاکس» مجارستان دچار سانحه شد و در مزارع اطراف سقوط کرد.
🔴
مقامات امنیتی مجارستان تحقیقات گسترده‌ای را برای شناسایی هویت سارق و انگیزه اصلی این اقدام خطرناک آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/144550" target="_blank">📅 15:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7iwWsGLD1SNUClZW5ALs8J3w2SwY-uM6MlR4lPK7c_9-9cl_HKvk_0UXj1nnZIx4pVSfZn15SfBfxuFbMCuux5j1OLs2tMgj74A_qUmywrOmY6nk7UqQWzaj88irhIaPDoTFb0JTCzmuPu4zqLHLcpW-aKCYHSr6FcqpKPdBVyzYM8ziKChVrOrRArT5t4ksLZE5-_cAPV2gYcoPaVp9eM3PoYJyHGQkDzHygn-tAGjKYJa2AQy86woHRPT5VGLoXW_F8IH9lBqBvWWIAfV90EQT2mFeC0UFv-bV0KiaJZ6d3gBLNwc6YMkd6yRa4OpKVvSej3zNJXHsl_B3UeqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوگل‌مپ نام دریاچه انتاریوی کانادا را به «دریاچه آمریکا» تغییر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144549" target="_blank">📅 15:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598d3d3b8d.mp4?token=JcoF4p6ExquzY-CfeTfVJnmrCb8O8XGllaowIgopnBygqAJV_-qEGLpCQEQmvkC6lZrXr4HE-wld6q5ij3Vv4O6I98UlK5Zsnd4gaBTRBrYcJed-sxVPjafj8hfJOfcGgIoSpxSsZ8qxCLzKrELimdThgVhI1RgB1zfM5sLjB_SaEXhLZ14L36hDyhpWYKeJxewyOoUZEsKkFYnUcH9Vt1pA9rRCbvt3Q1EaSg5OLoiDpWqSo92EClftWCOpfhdMVUplVrvc5XQt1gVVCbVcRhPftDSOEWHkdZPYB1Cz3KZrtkAggcpaVRbGv7QMnDdzX7lAbsvz5LpP-87Ry0WzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598d3d3b8d.mp4?token=JcoF4p6ExquzY-CfeTfVJnmrCb8O8XGllaowIgopnBygqAJV_-qEGLpCQEQmvkC6lZrXr4HE-wld6q5ij3Vv4O6I98UlK5Zsnd4gaBTRBrYcJed-sxVPjafj8hfJOfcGgIoSpxSsZ8qxCLzKrELimdThgVhI1RgB1zfM5sLjB_SaEXhLZ14L36hDyhpWYKeJxewyOoUZEsKkFYnUcH9Vt1pA9rRCbvt3Q1EaSg5OLoiDpWqSo92EClftWCOpfhdMVUplVrvc5XQt1gVVCbVcRhPftDSOEWHkdZPYB1Cz3KZrtkAggcpaVRbGv7QMnDdzX7lAbsvz5LpP-87Ry0WzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در جلسه هیات دولت خطاب به رئیس صداوسیما: آقای جبلی! اصلا صداوسیما را نگاه نمی‌کنم؛ وقتی می‌بینم اعصابم خراب می‌شود
🔴
من که زندگی‌ام را می‌خواهم برای نظام بگذارم این نگاه را پیدا کرده‌ام، ببینید مردم چه نگاهی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/144548" target="_blank">📅 15:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پلیس اسرائیل اعلام کرد دو نوجوان ۱۴ و ۱۶ ساله از حیفا به اتهام جاسوسی و انجام وظایف پولی برای مامور ادعایی اطلاعات ایران بازداشت شدند.
🔴
آن‌ها پس از پاسخ به آگهی استخدام تلگرامی با این فرد ارتباط برقرار و دوست خود را نیز اضافه کردند. وظایف آن‌ها شامل عکاسی از مکان‌های مرکز اسرائیل، جمع‌آوری اطلاعات امنیتی مراکز خرید تل‌آویو و هرتزلیه، اسپری‌کردن شعارهای ضد دولتی و جذب نوجوانان دیگر بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144547" target="_blank">📅 15:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد با ما تجارت کند. من با این موضوع موافقم
🔴
من از تجارت به‌عنوان ابزاری برای صلح و حل اختلافات استفاده می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/144546" target="_blank">📅 15:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: پزشکیان قرار است روز دوشنبه برای شرکت در اجلاس دو روزه سازمان همکاری شانگهای به بیشکک، پایتخت قرقیزستان سفر کند.
🔴
پیش‌بینی می‌شود مسعود پزشکیان، شی جین‌پینگ و ولادیمیر پوتین در این اجلاس که به مناسبت بیست‌وپنجمین سالگرد تأسیس سازمان همکاری شانگهای برگزار می‌شود، حضور داشته باشند.
🔴
حدود ۱۲ رئیس‌جمهور و مقام ارشد کشورهای عضو و شریک این سازمان نیز در این نشست شرکت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144545" target="_blank">📅 15:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
طالبان امروز در بیانیه ای رسما خواستار پایان جنگ با آمریکا و عادی سازی روابطشون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144544" target="_blank">📅 15:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مدیرعامل شرکت ساخت:
هزینه بازسازی پل کرج ۲.۵ تا ۳۰۰۰ میلیارد تومان برآورد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/144543" target="_blank">📅 14:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
استارلینک در امارات فعال شد؛ اینترنت ماهواره‌ای به کاربران خانگی رسید
🔴
سرویس اینترنت ماهواره‌ای استارلینک در امارات متحده عربی در دسترس کاربران قرار گرفت و این کشور به یکی از بازارهای مهم منطقه برای اینترنت مبتنی بر ماهواره‌های مدار پایین زمین تبدیل شد؛ اقدامی که می‌تواند جایگاه اینترنت ماهواره‌ای را در خاورمیانه بیش از پیش تقویت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/144542" target="_blank">📅 14:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الجزیره: مارک پفایل، مقام سابق امنیت ملی ایالات متحده، اعلام کرد واشنگتن قصد دارد از تحریم‌های ثانویه بر خریداران چینی نفت ایران خودداری کند و این گزینه را برای شرایط ضروری نگه می‌دارد.
🔴
او اشاره کرد که اتخاذ تدابیر گسترده علیه پکن به دلیل پیوندهای اقتصادی عمیق میان ایالات متحده و چین دشوار است، بنابراین واشنگتن می‌کوشد پالایشگاه‌های چینی را تشویق کند تا نفت را از منابع دیگر تأمین کنند.
🔴
پفایل افزود که چین از نفت خام ارزان‌قیمت ایران بهره‌مند می‌شود و انگیزه‌ای برای کمک به واشنگتن در جریان جنگ ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/144541" target="_blank">📅 14:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت امور خارجه ترکیه:پیش‌بینی می‌شود که وزرای امور خارجه و دفاع، و فرماندهان ارتش‌های عربستان سعودی، ترکیه و پاکستان در نشست فردا شرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/144540" target="_blank">📅 14:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiapA5cR4GNtTBucTIlZxbG9tCGkBv08VJwPb9lFDnv-mR6Y1H0h0YAjYcTSyOMz24rg41R0excTA1Up9yykhmyFtGxB3teIgXNKcq7LnqNL0cxZ94jzSI2BR_zrupOxD_hUGB-QrlWC_js3F7cPFTMAjQOhdbisQUoKGz9VYaYnrVxizxkar4cgqt3x5Lq8p8D7RXD5BKEPi8vEiePs0KT3d8FxhhBRRlQqxtK7bGnZWuE7QlQrSHqtk6Vd2yJibwbQd3sTyWuvvWAxHytj7WSCq7J4wcoixns5zsnKIgHOrWRTkens5SrF7Wqjy_r1ZTE5M75_OufI8a6szm-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن از سنگاپور عبور
کرد
🔴
ناو هواپیمابر آبراهام لینکلن آمریکا، بامداد یکشنبه پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پس از مأموریت در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت.
🔴
خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/144539" target="_blank">📅 14:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ادعای تاکر کارلسن، روزنامه نگار معروف آمریکایی: گزینه استفاده از سلاح هسته‌ای تاکتیکی علیه ایران در وزارت جنگ آمریکا مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/144538" target="_blank">📅 14:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144537">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تلویزیون سوریه گزارش داده نیروهای اسرائیلی در حال پیشروی به اطراف شهر «جباثا الخشب» در حومه شمالی قنیطره هستند.
🔴
جزئیات بیشتری درباره ابعاد این تحرک، تعداد نیروها یا درگیری احتمالی منتشر نشده است.
🔴
این پیشروی، تنش در جنوب سوریه و مناطق نزدیک مرزهای جولان را وارد مرحله تازه‌ای می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144537" target="_blank">📅 14:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144536">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بلومبرگ: جناح‌های تندرو ونزوئلا و نیروهای مخالف دولت از دلسـی رودریگز، رئیس‌جمهور موقت، به دلیل توافق نفتی با ترامپ
🔴
این توافق بدون مشارکت مخالفان ونزوئلا مذاکره شده
🔴
رودریگز روی این حساب کرده بود که توافق با ترامپ راه او برای تحکیم بیشتر قدرتش باشد
🔴
این توافق احتمالاً انگیزه‌های امریکا برای حرکت سریع به سمت برگزاری انتخابات جدید را کاهش می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/144536" target="_blank">📅 14:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144535">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puHYaxqqr7JzkZYlm14wGVC8FKruDjtz4zVlOFtbpv2wBisf7KFJalAax508F3cdxV_W5TJ63Z3dowxc0hwpyyeOi76ZSMdP_HsEK2FAaId6LBTYB7IgCHMPDoY27EYS5NRGQ09_y4ubW6s4gQgAjEm5PgOH-rqukr9-pNocM3Srrja5YY5LqazzmhmHTrUVQ5j1geeZtV6ZaSULSpTGzc8hdr_9DF4tSksAWFQpM3-Xb0O8DWYdBgmcb2zf3XW9voHv_LLbIBKFc7bsMR44io2mRiAr6k-dK8a3755_Hxf2ZdwXNKbQljemBtosJdCiZ94UmCGzPdnQXOKTT1fQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزمون تافل هم برای ایرانیان متوقف شد؟
🔴
گزارش‌هایی درباره نبود امکان ثبت‌نام و انتخاب تاریخ آزمون تافل در تهران منتشر شده است
🔴
لغو یا توقف برگزاری تافل برای ایرانیان هنوز به‌صورت رسمی تأیید نشده است اما مجوزی که اخیرا وزارت خزانه‌داری آمریکا لغو کرده شامل این آزمون نیز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/144535" target="_blank">📅 13:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144534">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴.۸ در مقیاس ریشتر، بخش‌های شرقی خلیج عدن را تکان داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144534" target="_blank">📅 13:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144533">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Day-a8Tvlt_hZLjKqMrrwfPmoAZCsCGYA8hXdv6AOw3Zg4HnSYRjGUvTY4vxxb9sTdvFJoWTIAQFwkBF0FOrc9MK5hmjtDK1mpXV_3MFHCFJwh_vr2yuG8xDIhgneM-nrc02MoQ6hfU4p0AH7ucQrLfI8-jh6IXn2iy-5xAKME9s_40tCjVUdYvMsk6ltcx0fHbMQAfPDnC9sD-BntJtP1uwZIbFzLlnO5QZ09g8inQbJZPzw4vePKgIQJj7U3wxU0GyIU87Xy6HRbviNdZcPjyV5V16UrS6IAPPhkGfrgZ1tS2Uai8XCEQP_mMtLUnZMEK_NrobluYwfQIrPO8npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیگار با تورم 160 درصدی رکورددار تورم مرداد ماه شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/144533" target="_blank">📅 13:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144532">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شبکه کان: ایالات متحده درخواست محمد بن سلمان، ولیعهد عربستان سعودی، برای رهبری یک عملیات نظامی علیه حوثی‌های یمن را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/144532" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
